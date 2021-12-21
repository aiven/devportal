Create a JDBC source connector for MySQL
==============================================

The JDBC source connector pushes data from a relational database, such as MySQL, to Apache Kafka where can be transformed and read by multiple consumers. 

.. Tip::

    Sourcing data from a database into Apache Kafka decouples the database from the set of consumers. Once the data is in Apache Kafka, multiple applications can access it without adding any additional query overhead to the source database.

.. _connect_jdbc_mysql_source_prereq:

Prerequisites
-------------

To setup a JDBC source connector pointing to MySQL, you need an Aiven for Apache Kafka service :doc:`with Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`. 

Furthermore you need to collect the following information about the source MySQL database upfront:

* ``MYSQL_HOST``: The database hostname
* ``MYSQL_PORT``: The database port
* ``MYSQL_USER``: The database user to connect
* ``MYSQL_PASSWORD``: The database password for the ``PG_USER``
* ``MYSQL_DATABASE_NAME``: the database name
* ``MYSQL_TABLES``: the list of database tables to be included in Apache Kafka; the list must be in the form of ``table_name1,table_name2``

.. Note::

    If you're using Aiven for MySQL the above details are available in the `Aiven console <https://console.aiven.io/>`_ service Overview tab or via the dedicated ``avn service get`` command with the :ref:`Aiven CLI <avn_service_get>`.

Setup a MySQL JDBC source connector with Aiven CLI
-------------------------------------------------------

The following example demonstrates how to setup an Apache Kafka JDBC source connector to a MySQL database using the :ref:`Aiven CLI dedicated command <avn_service_connector_create>`.

Define a Kafka Connect configuration file
'''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``jdbc_source_mysql.json``) with the following content:

::

    {
        "name":"CONNECTOR_NAME",
        "connector.class":"io.aiven.connect.jdbc.JdbcSourceConnector",
        "connection.url":"jdbc:mysql://MYSQL_HOST:MYSQL_PORT/MYSQL_DATABASE_NAME?&verifyServerCertificate=false&useSSL=true&requireSSL=true",
        "connection.user":"MYSQL_USER",
        "connection.password":"MYSQL_PASSWORD",
        "table.whitelist":"MYSQL_TABLES",
        "mode":"JDBC_MODE",
        "topic.prefix":"KAFKA_TOPIC_PREFIX",
        "tasks.max":"NR_TASKS",
        "poll.interval.ms":"POLL_INTERVAL"
    }

The configuration file contains the following entries:

* ``name``: the connector name
* ``MYSQL_HOST``, ``MYSQL_PORT``, ``MYSQL_DATABASE_NAME``, ``MYSQL_USER``, ``MYSQL_PASSWORD`` and ``MYSQL_TABLES``: source database parameters collected in the :ref:`prerequisite <connect_jdbc_pg_source_prereq>` phase. 
* ``mode``: the query mode, more information in the :doc:`dedicated page <../concepts/jdbc-source-modes>`; depending on the selected mode, additional configuration entries might be required.
* ``topic.prefix``: the prefix that will be used for topic names. The resulting topic name will be the concatenation of the ``topic.prefix`` and the schema and table name.
* ``tasks.max``: maximum number of tasks to execute in parallel. By default is 1, the connector can use at max 1 task for each source table defined.
* ``poll.interval.ms``: query frequency, default 5000 milliseconds

Check out the `dedicated documentation <https://github.com/aiven/jdbc-connector-for-apache-kafka/blob/master/docs/source-connector-config-options.rst>`_ for the full list of parameters.

Create a Kafka Connect connector with Aiven CLI
'''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, execute the following :ref:`Aiven CLI command <avn_service_connector_create>`, replacing the ``SERVICE_NAME`` with the name of the Aiven service where the connector needs to run:

:: 

    avn service connector create SERVICE_NAME @jdbc_source_mysql.json

Check the connector status with the following command, replacing the ``SERVICE_NAME`` with the Aiven service and the ``CONNECTOR_NAME`` with the name of the connector defined before:

::

    avn service connector status SERVICE_NAME CONNECTOR_NAME

Verify in the Apache Kafka target instance, the presence of the topic and the data

.. Tip::

    If you're using Aiven for Apache Kafka, topics will not be created automatically. Either create them manually following the ``topic.prefix.schema_name.table_name`` naming pattern or enable the ``kafka.auto_create_topics_enable`` advanced parameter.

Example: define a JDBC incremental connector
--------------------------------------------

The example creates an :doc:`incremental <../concepts/jdbc-source-modes>` JDBC connector with the following properties:

* connector name: ``jdbc_source_mysql_increment``
* source tables: ``students`` and ``exams``, available in an Aiven for MySQL database 
* :doc:`incremental column name <../concepts/jdbc-source-modes>`: ``id``
* topic prefix: ``jdbc_source_mysql_increment.``
* maximum number of concurrent tasks: ``1``
* time interval between queries: 5 seconds

The connector configuration is the following:

::

    {
        "name":"jdbc_source_mysql_increment",
        "connector.class":"io.aiven.connect.jdbc.JdbcSourceConnector",
        "connection.url":"jdbc:mysql://demo-mysql-myproject.aivencloud.com:13039/defaultdb?sslmode=require",
        "connection.user":"avnadmin",
        "connection.password":"mypassword123",
        "table.whitelist":"students,exams",
        "mode":"incrementing",
        "incrementing.column.name":"id",
        "topic.prefix":"jdbc_source_mysql_increment.",
        "tasks.max":"1",
        "poll.interval.ms":"5000"
    }

With the above configuration stored in a ``jdbc_incremental_source_mysql.json`` file, you can create the connector in the ``demo-kafka`` instance with:

::

    avn service connector create demo-kafka @jdbc_incremental_source_mysql.json