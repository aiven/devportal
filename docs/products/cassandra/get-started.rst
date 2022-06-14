Getting started with Aiven for Apache Cassandra®
================================================

Aiven services are managed from the Aiven `web console <https://console.aiven.io/>`_. First, log in to the console with your email address and password, and you will be automatically taken to the "Services" view that shows all of the services under the currently selected project.

**Projects** allows you to organize groups of services under different topics and each project can even have different billing settings. An empty project is automatically created for you upon sign up and the free credits are attached to this project. 

You can create new projects by clicking the project dropdown at the top of the sidebar and selecting "Create a new project". The same menu can also be used to switch between projects.

To get started with Cassandra, first click the "Create a new service" button.

.. image:: /images/products/cassandra/cassandra-console.png
   :alt: Create a new Cassandra service from the Aiven Console

The dialog that opens allows you to specify the main service properties:

* **Service name**: A short name for the service used to distinguish it from others. A random name is provided, but you can type in a more user-friendly one.

* **Service type**: Select "Apache Cassandra".

* **Plan**: How many servers and what kind of memory/CPU/disk resources will be allocated to run your service.

* **Cloud**: Which cloud and region to run the service on. *Note*: the pricing of the same service may differ between cloud providers and their regions.

After selecting your service properties, click the "Create" button and you will be taken back to the service list view displaying the newly selected service with an indicator that it is being created.

Click the service name in the list and the service's "Overview" information page will open. Aside from displaying the service's connection parameters and its status, this view is where you can make changes to the service.

The "Status" indicator will say "REBUILDING" while the service is being created for you. Once the service is up and running, the light will change to green and it will say "RUNNING". Note: while services typically start in minutes, the performance between clouds varies and it can take longer in some cases.

.. image:: /images/products/cassandra/cassandra-console-cluster.png
   :alt: Running Cassandra cluster in Console view

The Cassandra cluster is initiated with a superuser role named avnadmin. The role can be used to create keyspaces and additional roles with any tool or library supporting the Cassandra protocol.

Data center and replication
---------------------------

Your Cassandra cluster is created with all nodes in a Data Center (DC) named aiven. It's strongly recommended to use the ``NetworkTopologyStrategy`` replication strategy when creating keyspaces to ensure replicas of your data are distributed on nodes in different Availability Zones (AZ) within the service's selected cloud. 

While ``SimpleStrategy`` has a replication factor property, it may place the replicas in the same AZ. The examples below demonstrate how to create keyspaces with ``NetworkTopologyStrategy`` using the aiven DC.

We strongly recommend the use of a replication factor that is more than 1 (and no more than the number of nodes in your cluster). Using a replication factor of 1 can potentially result in data loss as the node storing it is still a single point of failure.

``cqlsh`` example
-------------

The CQL shell is an easy way to try out your new Cassandra service. 

**Download cqlsh**

1. Download Cassandra binaries from `archive.apache.org/dist/cassandra <http://archive.apache.org/dist/cassandra/>`_
2. Find the matching version with the Aiven Cassandra service you have created.
3. Extract the tarball without installing Cassandra, we'll just need to use ``cqlsh`` from `apache-cassandra-x.y.z/bin/cqlsh <https://apache-cassandra-x.y.z/bin/cqlsh>`_

**Download service certificate**

Since `connections to Aiven are always encrypted <https://help.aiven.io/security/cloud-security-overview>`_ and cqlsh needs a certificate file to validate the server, click on the Show CA certificate button and download the certificate. 

Point the SSL_CERTIFICATE environment variable to the downloaded file and run cqlsh with command-line parameters for username, password, hostname and port copied from the Connection parameters section of the Cassandra service view:::

   $ SSL_VERSION=TLSv1_2 SSL_CERTFILE=ca.pem apache-cassandra-x.y.z/bin/cqlsh --ssl -u avnadmin -p cevt9db1v7vxgrxu cassandra-1e39e4d8-myfirstcloudhub.aivencloud.com 20985
   Connected to 7ad8a118-d885-4077-9db4-95dbc53cd258 at cassandra-1e39e4d8-myfirstcloudhub.aivencloud.com:26882.
   [cqlsh 5.0.1 | Cassandra 3.11.1 | CQL spec 3.4.4 | Native protocol v4]
   Use HELP for help.
   avnadmin@cqlsh> CREATE KEYSPACE example_keyspace WITH REPLICATION = {'class': 'NetworkTopologyStrategy', 'aiven': 3};
   avnadmin@cqlsh> USE example_keyspace;
   avnadmin@cqlsh:example_keyspace> CREATE TABLE example_table (id int PRIMARY KEY, message text);
   avnadmin@cqlsh:example_keyspace> INSERT INTO example_table (id, message) VALUES (123, 'Hello world!');
   avnadmin@cqlsh:example_keyspace> SELECT id, message FROM example_table;

   id  | message
   -----+--------------
   123 | Hello world!

   (1 rows)

Programming language examples
-----------------------------

* `Python <https://github.com/aiven/aiven-examples/blob/master/cassandra/python/cassandra_example.py>`_ 

* `Go <https://github.com/aiven/aiven-examples/blob/master/cassandra/go/cassandra_example.go>`_

* `Java <https://github.com/aiven/aiven-examples/blob/master/cassandra/java/src/main/java/aiven/CassandraExample.java>`_

* `NodeJS <https://github.com/aiven/aiven-examples/blob/master/cassandra/nodejs/index.js>`_