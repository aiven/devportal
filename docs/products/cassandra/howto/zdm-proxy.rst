Migrate to Aiven for Apache Cassandra® with no downtime using ZDM Proxy
=======================================================================

Zero Downtime Migration (ZDM) Proxy is an open-source component developed in Go and based on client-server archtecture. It enables you to migrate from one Apache Cassandra® cluster to another without downtime or code changes in the application client.

.. seealso::

   For details on ZDM Proxy, check out `zdm-proxy GitHub <https://github.com/datastax/zdm-proxy>`_.

Check out this article to learn how to enable and use ZDM Proxy to migrate to Aiven for Apache Cassandra®.

How it works
------------

When using ZDM Proxy, the client connects to the proxy rather than to the source cluster. The proxy connects both to the source cluster and the target cluster. It sends read requests to the source cluster only, while write requests are forwrded to both clusters.

.. seealso::

   For details on how ZDM Proxy works, check out `Introduction to Zero Downtime Migration <https://docs.datastax.com/en/astra-serverless/docs/migrate/introduction.html>`_.

Prerequisites
-------------

* Aiven organization
* Depending on the method you choose to use for enabling CCR

  * Access to `Aiven Console <https://console.aiven.io/>`_
  * `cURL` CLI tool
  * `Aiven CLI tool <https://github.com/aiven/aiven-client>`_

Set up the source cluster
-------------------------

For demonstration purposes we'll use a simple Cassandra instance running in a container, so that it’s easy to follow the document if you don’t have or don’t want to touch any real service. If you have another source - you can use it instead.

I'm using podman to run Cassandra container. You can find installation instructions [here](https://podman.io/docs/installation) (or use docker instead, the syntax is the same, just replace `podman` with `docker`).

Create a test cluster
'''''''''''''''''''''

First we need to pull the image:

```sh
podman pull docker.io/library/cassandra:4.0.11
```

```
[denis.potapov@localhost aiven-core]$ podman pull docker.io/library/cassandra:4.0.11
Trying to pull docker.io/library/cassandra:4.0.11...
Getting image source signatures
Copying blob 8e39c5e3185a skipped: already exists  
Copying blob edab87ea811e skipped: already exists  
Copying blob e165ca30b01b skipped: already exists  
Copying blob 36d3de389f9f skipped: already exists  
Copying blob 3eb579eeb6ef skipped: already exists  
Copying blob 0c4de13af4ea skipped: already exists  
Copying blob 63c53c5e2051 skipped: already exists  
Copying blob 77bcf72cd207 skipped: already exists  
Copying blob b46c05b41df4 done  
Copying blob 140c1b53fcde done  
Copying config c504a7ac22 done  
Writing manifest to image destination
Storing signatures
c504a7ac22cfa53cb80af0e08cc355c23309d8b2a53d4b2270e2202bc8a1b266
```

Then we start the container:

```sh
podman run --name test_cassandra -d --network=host cassandra
```

```
[denis.potapov@localhost zdm]$ podman run --name test_cassandra -d --network=host cassandra
8f42a1f94650bacfcead58bb1fc2ba5423b5d75e4cb9d1f854a329481cb63325
```

Let's add some toy data. To get into the container we use:

```sh
podman exec -it test_cassandra bash
```

Insert test data
''''''''''''''''

Make sure that Cassandra has started. You can check logs:

```sh
tail -f /var/log/cassandra/system.log
```

Then we can start `cqlsh`:

```sh
cqlsh
```

And add some data

```sql
create keyspace test_migration with replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
create table test_migration.data (n_id int, value int, primary key (n_id));

insert into test_migration.data (n_id, value) values (1, 42);
insert into test_migration.data (n_id, value) values (2, 44);
insert into test_migration.data (n_id, value) values (3, 46);

select * from test_migration.data;
```

```
[denis.potapov@localhost zdm]$ podman run --name test_cassandra -d -p 9042:9042 cassandra
84fd654428c609e179878a6cb295d3ddaec7cd66b02a15fc355685f9b5f050b2
[denis.potapov@localhost zdm]$ podman exec -it test_cassandra bash
root@84fd654428c6:/# tail -f /var/log/cassandra/system.log
...
INFO  [main] 2023-09-14 16:35:27,998 PipelineConfigurator.java:126 - Starting listening for CQL clients on /0.0.0.0:9042 (unencrypted)...
INFO  [main] 2023-09-14 16:35:28,000 CassandraDaemon.java:768 - Startup complete
...
^C
root@84fd654428c6:/# cqlsh
Connected to Test Cluster at 127.0.0.1:9042
[cqlsh 6.1.0 | Cassandra 4.1.3 | CQL spec 3.4.6 | Native protocol v5]
Use HELP for help.
cqlsh> create keyspace test_migration with replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
cqlsh> create table test_migration.data (n_id int, value int, primary key (n_id));
cqlsh> insert into test_migration.data (n_id, value) values (1, 42);
cqlsh> insert into test_migration.data (n_id, value) values (2, 44);
cqlsh> insert into test_migration.data (n_id, value) values (3, 46);
cqlsh> select * from test_migration.data;

 n_id | value
------+-------
    1 |    42
    2 |    44
    3 |    46

(3 rows)
cqlsh> exit
root@84fd654428c6:/# exit
exit
[denis.potapov@localhost zdm]$ 
```

(Do not forget to exit the container shell)


Connect with ``cqlsh`` from outside of the container
''''''''''''''''''''''''''''''''''''''''''''''''''''

At this point you should be able to connect to localhost:9042 using cqlsh

```
[denis.potapov@localhost zdm]$ cqlsh
Connected to Test Cluster at 127.0.0.1:9042
[cqlsh 6.1.0 | Cassandra 4.1.3 | CQL spec 3.4.6 | Native protocol v5]
Use HELP for help.
cqlsh> select * from test_migration.data;

 n_id | value
------+-------
    1 |    42
    2 |    44
    3 |    46

(3 rows)
cqlsh> exit
```

If you do not have cqlsh installed, you can use one from the conainer image:

```
alias cqlsh='podman run -it --rm --network=host --entrypoint="" cassandra cqlsh'
cqlsh
```

Set up the target cluster
-------------------------

Create a service
''''''''''''''''

We’re migrating to Aiven, so let’s create a service:

```sh
avn service create --project test -t "cassandra" -p "startup-4" --cloud "aws-eu-west-1" "cassandra-denis-potapov"
```

Alternatively you can use the web console to create one.

Make sure that the service has reached RUNNING state.

```sh
avn service list --project test
```

Result should look something like:

```
[denis.potapov@localhost aiven-core]$ avn service list --project test
SERVICE_NAME             SERVICE_TYPE  STATE    CLOUD_NAME     PLAN       CREATE_TIME           UPDATE_TIME           NOTIFICATIONS
=======================  ============  =======  =============  =========  ====================  ====================  =============
cassandra-denis-potapov  cassandra     RUNNING  aws-eu-west-1  startup-4  2023-09-14T10:28:26Z  2023-09-14T13:39:49Z
```

Get credentials and connection information
''''''''''''''''''''''''''''''''''''''''''

We need username and password:

```sh
avn service user-list --format '{username} {password}' --project test cassandra-denis-potapov
```

```
[denis.potapov@localhost aiven-core]$ avn service user-list --format '{username} {password}' --project test cassandra-denis-potapov
avnadmin MY_SECRET_PASSWORD
```

And CA certificate:
```sh
avn service user-creds-download --project test --username avnadmin -d /tmp cassandra-denis-potapov
```
This will download it the certificate to `/tmp/ca.pem`.

Alternatively you can find out the credentials using the web console.

To get hostname and port use:

```sh
avn service get --format '{service_uri}' --project test cassandra-denis-potapov
```

```
[denis.potapov@localhost aiven-core]$ avn service get --format '{service_uri}' --project test cassandra-denis-potapov
cassandra-denis-potapov-test-denis-potapov-test.a.avns.net:24756
```

So in this example the host is `cassandra-denis-potapov-test-denis-potapov-test.a.avns.net` and the port is `24756`.


Connect with ``cqlsh``
''''''''''''''''''''''

You should be able to connect using cqlsh

```
cqlsh --ssl -u avnadmin -p MY_SECRET_PASSWORD cassandra-denis-potapov-test-denis-potapov-test.a.avns.net 24756
```

If you do not have cqlsh installed, you can use cqlsh from cassandra container image, but in this case it's a bit more difficult - it requires passing CA certificate to the container:

```
alias cqlsh='podman run -it --rm --network=host --entrypoint="" -e SSL_CERTFILE -v${SSL_CERTFILE}:${SSL_CERTFILE}:z cassandra cqlsh'
```

Create keyspaces and tables
'''''''''''''''''''''''''''

ZDM Proxy requires the same keyspaces and tables on target to exist, so let's create them:

```
create keyspace test_migration with replication = {'class': 'SimpleStrategy', 'replication_factor': 3};
create table test_migration.data (n_id int, value int, primary key (n_id));
```

Note that we use different replication factor, because target claster has 3 nodes.

```
[denis.potapov@localhost zdm-proxy]$ cqlsh --ssl -u avnadmin -p MY_SECRET_PASSWORD cassandra-denis-potapov-test-denis-potapov-test.a.avns.net 24756

Warning: Using a password on the command line interface can be insecure.
Recommendation: use the credentials file to securely provide the password.

Connected to d4e5c00e-1fb1-473f-805f-9c5c53b6828f at cassandra-denis-potapov-test-denis-potapov-test.a.avns.net:24756
[cqlsh 6.1.0 | Cassandra 4.0.11 | CQL spec 3.4.5 | Native protocol v5]
Use HELP for help.
avnadmin@cqlsh> create keyspace test_migration with replication = {'class': 'SimpleStrategy', 'replication_factor': 3};
avnadmin@cqlsh> create table test_migration.data (n_id int, value int, primary key (n_id));
avnadmin@cqlsh> 
```

Run ZDM Proxy
---------------

Download the binary
'''''''''''''''''''

You can download ZDM Proxy binary [here](https://github.com/datastax/zdm-proxy/releases)

For example:

```sh
wget https://github.com/datastax/zdm-proxy/releases/download/v2.1.0/zdm-proxy-linux-amd64-v2.1.0.tgz
tar xf zdm-proxy-linux-amd64-v2.1.0.tgz
```

The result should look something like:

```
[denis.potapov@localhost zdm]$ ls
LICENSE  zdm-proxy-linux-amd64-v2.1.0.tgz  zdm-proxy-v2.1.0
```

Run it
''''''

To run ZDM Proxy we need to specify connection information by setting ZDM_* environment variables and then just run the binary.

```sh
export ZDM_ORIGIN_CONTACT_POINTS=localhost
export ZDM_ORIGIN_USERNAME=cassandra
export ZDM_ORIGIN_PASSWORD=cassandra
export ZDM_ORIGIN_PORT=9042

export ZDM_TARGET_CONTACT_POINTS=cassandra-denis-potapov-test-denis-potapov-test.a.avns.net
export ZDM_TARGET_USERNAME=avnadmin
export ZDM_TARGET_PASSWORD=MY_SECRET_PASSWORD
export ZDM_TARGET_PORT=24756
export ZDM_TARGET_TLS_SERVER_CA_PATH="/tmp/ca.pem"

export ZDM_TARGET_ENABLE_HOST_ASSIGNMENT=false

./zdm-proxy-v2.1.0
```

ZDM_TARGET_ENABLE_HOST_ASSIGNMENT variable is particularly important for Aiven target cluster. Otherwise ZDM Proxy will try to connect to one of internal addresses of the cluster nodes (and internal addresses are obviously unavailable from outside). If you have the similar situation with the origin cluster, you should set `ZDM_ORIGIN_ENABLE_HOST_ASSIGNMENT=false`.

Check how it works
------------------

Proxy works on port 14002 (can be overriden) and we can use cqlsh to connect. In our case both origin and target has authentication - this means we must specify target username and password. You can see more details [here](https://docs.datastax.com/en/astra-serverless/docs/migrate/connect-clients-to-proxy.html#_client_application_credentials).

```sh
cqlsh -u avnadmin -p MY_SECRET_PASSWORD localhost 14002
```

```
[denis.potapov@localhost zdm-proxy]$ cqlsh -u avnadmin -p MY_SECRET_PASSWORD localhost 14002

Warning: Using a password on the command line interface can be insecure.
Recommendation: use the credentials file to securely provide the password.

Connected to Test Cluster at localhost:14002
[cqlsh 6.1.0 | Cassandra 4.1.3 | CQL spec 3.4.6 | Native protocol v4]
Use HELP for help.
avnadmin@cqlsh> 
```

Let's check if we see the data in the table:

```sql
select * from test_migration.data;
```

```
avnadmin@cqlsh> select * from test_migration.data;

 n_id | value
------+-------
    1 |    42
    2 |    44
    3 |    46

(3 rows)
avnadmin@cqlsh> 
```

```sql
insert into test_migration.data (n_id, value) values (4, 48);
insert into test_migration.data (n_id, value) values (5, 50);

```

```
avnadmin@cqlsh> insert into test_migration.data (n_id, value) values (4, 48);
avnadmin@cqlsh> insert into test_migration.data (n_id, value) values (5, 50);
avnadmin@cqlsh> select * from test_migration.data;

 n_id | value
------+-------
    5 |    50
    1 |    42
    2 |    44
    4 |    48
    3 |    46

(5 rows)
avnadmin@cqlsh> exit
```

Let's check the data in origin Cassandra:

```
[denis.potapov@localhost zdm-proxy]$ cqlsh localhost 9042
Connected to Test Cluster at localhost:9042
[cqlsh 6.1.0 | Cassandra 4.1.3 | CQL spec 3.4.6 | Native protocol v5]
Use HELP for help.
cqlsh> select * from test_migration.data;

 n_id | value
------+-------
    5 |    50
    1 |    42
    2 |    44
    4 |    48
    3 |    46

(5 rows)
cqlsh> 
```

And on the target:

```
[denis.potapov@localhost zdm-proxy]$ cqlsh --ssl -u avnadmin -p MY_SECRET_PASSWORD cassandra-denis-potapov-test-denis-potapov-test.a.avns.net 24756

Warning: Using a password on the command line interface can be insecure.
Recommendation: use the credentials file to securely provide the password.

Connected to d4e5c00e-1fb1-473f-805f-9c5c53b6828f at cassandra-denis-potapov-test-denis-potapov-test.a.avns.net:24756
[cqlsh 6.1.0 | Cassandra 4.0.11 | CQL spec 3.4.5 | Native protocol v5]
Use HELP for help.
avnadmin@cqlsh> select * from test_migration.data;

 n_id | value
------+-------
    5 |    50
    4 |    48

(2 rows)
avnadmin@cqlsh> 
```

Related reading
---------------

* `zdm-proxy GitHub <https://github.com/datastax/zdm-proxy>`_
* `Introduction to Zero Downtime Migration <https://docs.datastax.com/en/astra-serverless/docs/migrate/introduction.html>`_
