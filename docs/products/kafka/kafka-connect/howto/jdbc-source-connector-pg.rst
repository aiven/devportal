JDBC source connector with PostgreSQL
=====================================

The JDBC source connector pushes data from a relational database, such as PostgreSQL, to Apache Kafka where can be transformed and read by multiple consumers. 

.. Tip::

    Sourcing data from a database into Apache Kafka decouples the database from the set of consumers, enabling multiple applications to access the data without adding a per-consumer query overhead to the source database.

.. _connect_jdbc_pg_source_prereq:

Prerequisites
-------------

To setup a JDBC source connector pointing to PostgreSQL, you need an Aiven for Apache Kafka service :doc:`with Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`. 
Furthermore you need to collect the following information about the source PostgreSQL database upfront:

* ``PG_HOST``: The database hostname
* ``PG_PORT``: The database port
* ``PG_USER``: The database user to connect
* ``PG_PASSWORD``: The database password for the ``PG_USER``
* ``PG_DATABASE_NAME``: the database name
* ``SSL_MODE``: the `SSL mode <https://www.postgresql.org/docs/current/libpq-ssl.html>`_
* ``PG_TABLES``: the list of database tables to be included in Apache Kafka; the list must be in the form of ``schema_name1.table_name1,schema_name2.table_name2``

.. Note::

    If you're using Aiven for PostgreSQL the above details are available in the `Aiven console <https://console.aiven.io/>`_ service Overview tab or via the dedicated ``avn service get`` command with the :ref:`Aiven CLI <avn_service_get>`.

Setup a PostgreSQL JDBC source connector with Aiven CLI
-------------------------------------------------------

The following example demonstrates how to setup an Apache Kafka JDBC source connector to a PostgreSQL database using the :ref:`Aiven CLI dedicated command <avn_service_connector_create>`:

1. In a file named ``jdbc_source_pg.json`` define the connector configuration with the following content:

::

    {
        "name":"CONNECTOR_NAME",
        "connector.class":"io.aiven.connect.jdbc.JdbcSourceConnector",
        "connection.url":"jdbc:postgresql://PG_HOST:PG_PORT/PG_DATABASE_NAME?sslmode=SSL_MODE",
        "connection.user":"PG_USER",
        "connection.password":"PG_PASSWORD",
        "table.whitelist":"PG_TABLES",
        "mode":"JDBC_MODE",
        "topic.prefix":"KAFKA_TOPIC_PREFIX",
        "tasks.max":"NR_TASKS",
        "poll.interval.ms":"POLL_INTERVAL"
    }

.. Note::

    The ``PG_HOST``, ``PG_PORT``, ``PG_DATABASE_NAME``, ``SSL_MODE``, ``PG_USER``, ``PG_PASSWORD`` and ``PG_TABLES`` are the parameters collected in the :ref:`prerequisite <connect_jdbc_pg_source_prereq>` phase. 
    The following additional parameters need to be set:

    * ``name``: the connector name
    * ``mode``: the query mode, more information in the :doc:`dedicated page <../concepts/jdbc-source-modes>`; depending on the selected mode, additional configuration entries might be required.
    * ``topic.prefix``: the prefix that will be used for topic names; the resulting topic name is the concatenation of the ``topic.prefix`` and the table name.
    * ``tasks.max``: maximum number of tasks to execute in parallel
    * ``poll.interval.ms``: query frequency

    Check out the `dedicated documentation <https://github.com/aiven/jdbc-connector-for-apache-kafka/blob/master/docs/source-connector-config-options.rst>`_ for the full list of parameters.

2. Execute the following :ref:`Aiven CLI command <avn_service_connector_create>` to create the connector, replacing the ``SERVICE_NAME`` with the name of the Aiven service where the connector needs to run:

:: 

    avn service connector create SERVICE_NAME @jdbc_source_pg.json

3. Check the connector status with the following command, replacing the ``SERVICE_NAME`` with the Aiven service and the ``CONNECTOR_NAME`` with the name of the connector defined before:

::

    avn service connector status SERVICE_NAME CONNECTOR_NAME

4. Verify in the Aiven for Apache Kafka target instance, the presence of the topic and the data

Example: define a JDBC incremental connector
--------------------------------------------

The example creates an :doc:`incremental <../concepts/jdbc-source-modes>` JDBC connector with the following properties:

* connector name: ``jdbc_source_pg_increment``
* source tables: ``students`` and ``exams`` from the ``public`` schema, available in an Aiven for PostgreSQL database 
* :doc:`incremental column name <../concepts/jdbc-source-modes>`: ``id``
* topic prefix: ``jdbc_source_pg_increment.``
* maximum number of concurrent tasks: ``1``
* time interval between queries: 5 seconds

The connector configuration is the following:

::

    {
        "name":"jdbc_source_pg_increment",
        "connector.class":"io.aiven.connect.jdbc.JdbcSourceConnector",
        "connection.url":"jdbc:postgresql://demo-pg-myproject.aivencloud.com:13039/defaultdb?sslmode=require",
        "connection.user":"avnadmin",
        "connection.password":"mypassword123",
        "table.whitelist":"public.students,public.exams",
        "mode":"incrementing",
        "incrementing.column.name":"id",
        "topic.prefix":"jdbc_source_pg_increment.",
        "tasks.max":"1",
        "poll.interval.ms":"5000"
    }

With the above configuration stored in a ``jdbc_incremental_source_pg.json`` file, you can create the connector in the ``demo-kafka`` instance with:

::

    avn service connector create demo-kafka @jdbc_incremental_source_pg.json