Create a Debezium source connector for PostgreSQL
=================================================

The Debezium source connector extracts the changes committed to the transaction log in a relational database, such as PostgreSQL, and writes them to an Apache Kafka topic in a standard format where they can be transformed and read by multiple consumers. 

.. Tip::

    Sourcing data from a database into Apache Kafka decouples the database from the set of consumers. Once the data is in Apache Kafka, multiple applications can access it without adding any additional query overhead to the source database.

.. _connect_debezium_pg_source_prereq:

Prerequisites
-------------

To setup a Debezium source connector pointing to PostgreSQL, you need an Aiven for Apache Kafka service :doc:`with Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`. 

Furthermore you need to collect the following information about the source PostgreSQL database upfront:

* ``PG_HOST``: The database hostname
* ``PG_PORT``: The database port
* ``PG_USER``: The database user to connect
* ``PG_PASSWORD``: The database password for the ``PG_USER``
* ``PG_DATABASE_NAME``: The database name
* ``SSL_MODE``: The `SSL mode <https://www.postgresql.org/docs/current/libpq-ssl.html>`_
* ``PG_TABLES``: The list of database tables to be included in Apache Kafka; the list must be in the form of ``schema_name1.table_name1,schema_name2.table_name2``
* ``PG_PUBLICATION_NAME``: The name of the `PostgreSQL logical replication publication <https://www.postgresql.org/docs/current/logical-replication-publication.html>`_, if left empty, ``debezium`` is used as default.
* ``PG_SLOT_NAME``: name of the `PostgreSQL replication slot <https://developer.aiven.io/docs/products/postgresql/howto/setup-logical-replication>`_, if left empty, ``debezium`` is be used as default
* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PORT``: The Apache Kafka's schema registry port, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_USER``: The Apache Kafka's schema registry username, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PASSWORD``: The Apache Kafka's schema registry user password, only needed when using Avro as data format


.. Note::

    If you're using Aiven for PostgreSQL and Aiven for Apache Kafka the above details are available in the `Aiven console <https://console.aiven.io/>`_ service Overview tab or via the dedicated ``avn service get`` command with the :ref:`Aiven CLI <avn_service_get>`.

Setup a PostgreSQL Debezium source connector with Aiven CLI
-----------------------------------------------------------

The following example demonstrates how to setup an Apache Kafka Debezium source connector to a PostgreSQL database using the :ref:`Aiven CLI dedicated command <avn_service_connector_create>`.

Define a Kafka Connect configuration file
'''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``debezium_source_pg.json``) with the following content:

::

    {
        "name":"CONNECTOR_NAME",
        "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
        "database.hostname": "PG_HOST",
        "database.port": "PG_PORT",
        "database.user": "PG_USER",
        "database.password": "PG_PASSWORD",
        "database.dbname": "PG_DATABASE_NAME",
        "database.sslmode": "SSL_MODE",
        "plugin.name": "wal2json",
        "slot.name": "PG_SLOT_NAME",
        "publication.name": "PG_PUBLICATION_NAME",
        "database.server.name": "KAFKA_TOPIC_PREFIX",
        "table.include.list": "PG_TABLES",
        "tasks.max":"NR_TASKS",
        "key.converter": "io.confluent.connect.avro.AvroConverter",
        "key.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "key.converter.basic.auth.credentials.source": "USER_INFO",
        "key.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD",
        "value.converter": "io.confluent.connect.avro.AvroConverter",
        "value.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "value.converter.basic.auth.credentials.source": "USER_INFO",
        "value.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD",
    }

The configuration file contains the following entries:

* ``name``: the connector name
* ``PG_HOST``, ``PG_PORT``, ``PG_DATABASE_NAME``, ``SSL_MODE``, ``PG_USER``, ``PG_PASSWORD``, ``PG_TABLES``, ``PG_PUBLICATION_NAME`` and ``PG_SLOT_NAME``: source database parameters collected in the :ref:`prerequisite <connect_debezium_pg_source_prereq>` phase. 
* ``database.server.name``: the logical name of the database, dictates the prefix that will be used for Apache Kafka topic names. The resulting topic name will be the concatenation of the ``database.server.name`` and the table name.
* ``tasks.max``: maximum number of tasks to execute in parallel. By default this is 1, the connector can use at most 1 task for each source table defined.
* ``plugin.name``: defines the `PostgreSQL output plugin <https://debezium.io/documentation/reference/connectors/postgresql.html>`_ to convert changes in the database into events in Apache Kafka.
* ``key.converter`` and ``value.converter``:  defines the messages data format in the Apache Kafka topic. The ``io.confluent.connect.avro.AvroConverter`` converter pushes messages in Avro format. To store the messages schema we use Aiven's `Karapace schema registry <https://github.com/aiven/karapace>`_ as specified by the ``schema.registry.url`` parameter and related credentials.

.. Note::

    The ``key.converter`` and ``value.converter`` sections are only needed when pushing data in Avro format. If omitted the messages will be defined in JSON format.


Create a Kafka Connect connector with Aiven CLI
'''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, execute the following :ref:`Aiven CLI command <avn_service_connector_create>`, replacing the ``SERVICE_NAME`` with the name of the Aiven service where the connector needs to run:

:: 

    avn service connector create SERVICE_NAME @debezium_source_pg.json

Check the connector status with the following command, replacing the ``SERVICE_NAME`` with the Aiven service and the ``CONNECTOR_NAME`` with the name of the connector defined before:

::

    avn service connector status SERVICE_NAME CONNECTOR_NAME

Verify the presence of the topic and data in the Apache Kafka target instance.

.. Tip::

    If you're using Aiven for Apache Kafka, topics will not be created automatically. Either create them manually following the ``database.server.name.schema_name.table_name`` naming pattern or enable the ``kafka.auto_create_topics_enable`` advanced parameter.