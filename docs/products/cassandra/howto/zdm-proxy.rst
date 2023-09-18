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

* Migration source - an Apache Cassandra instance outside the Aiven platform
* Migration target - an Aiven for Apache Cassandra service
* ``cqlsh`` installed

Migrate to Aiven
----------------

Connect to the target
'''''''''''''''''''''

:doc:`Connect to your Aiven for Apache Cassandra service </docs/products/cassandra/howto/connect-cqlsh-cli>` using ``cqlsh``, for example.

Create keyspaces and tables
'''''''''''''''''''''''''''

In your target service, create the same keyspaces and tables you have in your source Cassandra instance. For ``replication_factor``, specify the number of nodes that the taget cluster has.

.. code-block:: bash

    create keyspace SOURCE_KEYSPACE_NAME with replication = {'class': 'SimpleStrategy', 'replication_factor': NUMBER_OF_NODES_OF_TARGET};
    create table SOURCE_TABLE_NAME.SOURCE_DATABASE_NAME (n_id int, value int, primary key (n_id));

Reconnect to the target
'''''''''''''''''''''''

:doc:`Connect to your Aiven for Apache Cassandra service </docs/products/cassandra/howto/connect-cqlsh-cli>` again using ``cqlsh``, for example.

You can expect to receive output similar to the following:

.. code-block:: bash

    Connected to a1b2c3d4-1a2b-3c4d-5e6f-a1b2c3d4e5f6 at cassandra-instance-name.a.avns.net:12345
    [cqlsh 6.1.0 | Cassandra 4.0.11 | CQL spec 3.4.5 | Native protocol v5]
    Use HELP for help.
    avnadmin@cqlsh> create keyspace KEYSPACE_NAME with replication = {'class': 'SimpleStrategy', 'replication_factor': 3};
    avnadmin@cqlsh> create table TABLE_NAME.DATABASE_NAME (n_id int, value int, primary key (n_id));
    avnadmin@cqlsh>

Download the binary
'''''''''''''''''''

Download the ZDM Proxy's binary from `ZDM Proxy releases <https://github.com/datastax/zdm-proxy/releases>`_.

.. code-block:: bash

    wget https://github.com/datastax/zdm-proxy/releases/download/v2.1.0/zdm-proxy-linux-amd64-v2.1.0.tgz
    tar xf zdm-proxy-linux-amd64-v2.1.0.tgz

You can expect to receive output similar to the following:

.. code-block:: bash

    [john.doe@localhost zdm]$ ls
    LICENSE  zdm-proxy-linux-amd64-v2.1.0.tgz  zdm-proxy-v2.1.0

Run ZDM Proxy
'''''''''''''

To run ZDM Proxy, specify connection information by setting ZDM_* environment variables using the ``export`` command. Next, run the binary.

.. code-block:: bash

    export ZDM_SOURCE_CONTACT_POINTS=localhost
    export ZDM_SOURCE_USERNAME=cassandra
    export ZDM_SOURCE_PASSWORD=cassandra
    export ZDM_SOURCE_PORT=1234

    export ZDM_TARGET_CONTACT_POINTS=cassandra-instance-name.a.avns.net
    export ZDM_TARGET_USERNAME=avnadmin
    export ZDM_TARGET_PASSWORD=YOUR_SECRET_PASSWORD
    export ZDM_TARGET_PORT=54321
    export ZDM_TARGET_TLS_SERVER_CA_PATH="/tmp/ca.pem"

    export ZDM_TARGET_ENABLE_HOST_ASSIGNMENT=false

    ./zdm-proxy-v2.1.0

.. topic:: ENABLE_HOST_ASSIGNMENT

    Make sure you set the ZDM_TARGET_ENABLE_HOST_ASSIGNMENT variable. Otherwise, ZDM Proxy tries to connect to one of internal addresses of the cluster nodes, which are unavailable from outside. If this occurs to your source cluster, set ``ZDM_SOURCE_ENABLE_HOST_ASSIGNMENT=false``.

Check how it works
------------------

Check data at the proxy
'''''''''''''''''''''''

To connect to ZDM Proxy, use, for exmaple, ``cqlsh`` and provide connection details. If your source or target require authentication, specify target username and password.

.. seealso::
    
    Check more details on using the credentials in `Client application credentials <https://docs.datastax.com/en/astra-serverless/docs/migrate/connect-clients-to-proxy.html#_client_application_credentials>`_.

The port that ZDM Proxy uses is 14002, which can be overriden.

.. code-block:: bash

    cqlsh -u avnadmin -p YOUR_SECRET_PASSWORD localhost 14002

You can expect to receive output similar to the following:

.. code-block:: bash

    Connected to CLUSTER_NAME at localhost:14002
    [cqlsh 6.1.0 | Cassandra 4.1.3 | CQL spec 3.4.6 | Native protocol v4]
    Use HELP for help.
    avnadmin@cqlsh>

Check if the data is in the table:

.. code-block:: bash

    select * from TABLE_NAME.DATABASE_NAME;

You can expect to receive output similar to the following:

.. code-block:: bash

    n_id | value
    ------+-------
        1 |    42
        2 |    44
        3 |    46

    (3 rows)
    avnadmin@cqlsh>

Try to insert more data into the table and check again data inside the table:

.. code-block:: bash

    insert into TABLE_NAME.DATABASE_NAME (n_id, value) values (4, 48);
    insert into TABLE_NAME.DATABASE_NAME (n_id, value) values (5, 50);
    select * from TABLE_NAME.DATABASE_NAME;

You can expect to receive output similar to the following:

.. code-block:: bash

    n_id | value
    ------+-------
        5 |    50
        1 |    42
        2 |    44
        4 |    48
        3 |    46

    (5 rows)
    avnadmin@cqlsh> exit

Check data in the source
''''''''''''''''''''''''

.. code-block:: bash

    [john.doe@localhost zdm-proxy]$ cqlsh localhost 9042
    Connected to CLUSTER_NAME at localhost:9042
    [cqlsh 6.1.0 | Cassandra 4.1.3 | CQL spec 3.4.6 | Native protocol v5]
    Use HELP for help.
    cqlsh> select * from TABLE_NAME.DATABASE_NAME;

    n_id | value
    ------+-------
        5 |    50
        1 |    42
        2 |    44
        4 |    48
        3 |    46

    (5 rows)
    cqlsh>

Check data in the target
''''''''''''''''''''''''

.. code-block:: bash

    [john.doe@localhost zdm-proxy]$ cqlsh --ssl -u avnadmin -p YOUR_SECRET_PASSWORD cassandra-cluster-name.a.avns.net 24756

    Connected to d4e5c00e-1fb1-473f-805f-9c5c53b6828f at cassandra-cluster-name.a.avns.net:24756
    [cqlsh 6.1.0 | Cassandra 4.0.11 | CQL spec 3.4.5 | Native protocol v5]
    Use HELP for help.
    avnadmin@cqlsh> select * from TABLE_NAME.DATABASE_NAME;

    n_id | value
    ------+-------
        5 |    50
        4 |    48

    (2 rows)
    avnadmin@cqlsh>

Related reading
---------------

* `zdm-proxy GitHub <https://github.com/datastax/zdm-proxy>`_
* `Introduction to Zero Downtime Migration <https://docs.datastax.com/en/astra-serverless/docs/migrate/introduction.html>`_
* `ZDM Proxy releases <https://github.com/datastax/zdm-proxy/releases>`_
* `Client application credentials <https://docs.datastax.com/en/astra-serverless/docs/migrate/connect-clients-to-proxy.html#_client_application_credentials>`_
