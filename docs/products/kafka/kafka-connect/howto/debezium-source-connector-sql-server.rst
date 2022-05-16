Create a Debezium source connector for SQL Server
==================================================

The SQL Server Debezium source connector is based on the `change data capture feature <https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-data-capture-sql-server?view=sql-server-2017>`, extracts the database changes captured in specific `change tables <https://debezium.io/documentation/reference/stable/connectors/sqlserver.html>`_ on a polling interval, and writes them to an Apache Kafka® topic in a standard format where they can be transformed and read by multiple consumers.

.. _connect_debezium_sql_server_schema_versioning:

Enable CDC in SQL Server
------------------------

The Change Data Capture (CDC) needs to be enabled at database level and table level.

Enable CDC at database level
''''''''''''''''''''''''''''

To enable the CDC at database level, you can use the following command::

    USE <DATABASE_NAME>
    GO
    EXEC sys.sp_cdc_enable_db
    GO

.. Note::

    If you're using GCP Cloud SQL for SQL Server, you can enable database CDC with::
    
        EXEC msdb.dbo.gcloudsql_cdc_enable_db '<DATABASE_NAME>'

Once the CDC is enabled, a new schema called ``cdc`` is created for the target database, containing all the required tables.

Enable CDC at table level
'''''''''''''''''''''''''

To enable CDC for a table you can execute the following command::

    USE <DATABASE_NAME>
    GO

    EXEC sys.sp_cdc_enable_table
    @source_schema = N'<SCHEMA_NAME>',
    @source_name   = N'<TABLE_NAME>', 
    @role_name     = N'<ROLE_NAME>',  
    @filegroup_name = N'<FILEGROUP_NAME>',
    @supports_net_changes = 0
    GO

The command above has the following parameters:

* ``<DATABASE_NAME>``, ``<SCHEMA_NAME>``, ``<TABLE_NAME>``: the references to the table where CDC needs to be setup
* ``<ROLE_NAME>``: the database role that will have access to the change tables. Leave it ``NULL`` to only allow access to members of ``sysadmin`` or ``db_owner`` groups
* ``<FILEGROUP_NAME>``: Specifies the `file group <https://docs.microsoft.com/en-us/sql/relational-databases/databases/database-files-and-filegroups>`_ where the files will be written, needs to be pre-existing

.. Note::

    If you're using GCP Cloud SQL for SQL Server, you can enable database CDC on a table with::

        EXEC sys.sp_cdc_enable_table
        @source_schema = N'<SCHEMA_NAME>',
        @source_name = N'<TABLE_NAME>',
        @role_name = N'<ROLE_NAME>'

.. Warning::

    When evolving table schemas in online mode, new columns information might be lost until the CDC is re-enabled for the table. More information are available in the `related Debezium documentation <https://debezium.io/documentation/reference/stable/connectors/sqlserver.html#sqlserver-schema-evolution>`_.


.. _connect_debezium_sql_server_source_prereq:

Prerequisites
-------------

To setup a Debezium source connector pointing to SQL Server, you need an Aiven for Apache Kafka service :doc:`with Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`. 

Furthermore you need to collect the following information about the source SQL Server database upfront:

* ``SQLSERVER_HOST``: The database hostname
* ``SQLSERVER_PORT``: The database port
* ``SQLSERVER_USER``: The database user to connect
* ``SQLSERVER_PASSWORD``: The database password for the ``SQLSERVER_USER``
* ``SQLSERVER_DATABASE_NAME``: The database name
* ``SQLSERVER_TABLES``: The list of database tables to be included in Apache Kafka; the list must be in the form of ``schema_name1.table_name1,schema_name2.table_name2``
* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service, needed when storing the :ref:`schema definition changes <connect_debezium_sql_server_schema_versioning>`
* ``APACHE_KAFKA_PORT``: The port of the Apache Kafka service, needed when storing the :ref:`schema definition changes <connect_debezium_sql_server_schema_versioning>`
* ``SCHEMA_REGISTRY_PORT``: The Apache Kafka's schema registry port, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_USER``: The Apache Kafka's schema registry username, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PASSWORD``: The Apache Kafka's schema registry user password, only needed when using Avro as data format


.. Note::

    If you're using Aiven for SQL Server and Aiven for Apache Kafka the above details are available in the `Aiven console <https://console.aiven.io/>`_ service Overview tab or via the dedicated ``avn service get`` command with the :ref:`Aiven CLI <avn_service_get>`.

Setup a SQL Server Debezium source connector with Aiven CLI
-----------------------------------------------------------

The following example demonstrates how to setup a Debezium source Connector for Apache Kafka to a SQL Server database using the :ref:`Aiven CLI dedicated command <avn_service_connector_create>`.

Define a Kafka Connect configuration file
'''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``debezium_source_sql_server.json``) with the following content:

.. code-block:: json

    {
        "name":"CONNECTOR_NAME",
        "connector.class": "io.debezium.connector.sqlserver.SqlServerConnector",
        "database.hostname": "SQLSERVER_HOST",
        "database.port": "SQLSERVER_PORT",
        "database.user": "SQLSERVER_USER",
        "database.password": "SQLSERVER_PASSWORD",
        "database.dbname": "SQLSERVER_DATABASE_NAME",
        "database.server.name": "KAFKA_TOPIC_PREFIX",
        "table.include.list": "SQLSERVER_TABLES",
        "tasks.max":"NR_TASKS",
        "poll.interval.ms": 500,
        "key.converter": "io.confluent.connect.avro.AvroConverter",
        "key.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "key.converter.basic.auth.credentials.source": "USER_INFO",
        "key.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD",
        "value.converter": "io.confluent.connect.avro.AvroConverter",
        "value.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "value.converter.basic.auth.credentials.source": "USER_INFO",
        "value.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD",
        "database.history.kafka.bootstrap.servers": "APACHE_KAFKA_HOST:APACHE_KAFKA_PORT",
        "database.history.producer.security.protocol": "SSL",
        "database.history.producer.ssl.keystore.type": "PKCS12",
        "database.history.producer.ssl.keystore.location": "/run/aiven/keys/public.keystore.p12",
        "database.history.producer.ssl.keystore.password": "password",
        "database.history.producer.ssl.truststore.location": "/run/aiven/keys/public.truststore.jks",
        "database.history.producer.ssl.truststore.password": "password",
        "database.history.producer.ssl.key.password": "password",
        "database.history.consumer.security.protocol": "SSL",
        "database.history.consumer.ssl.keystore.type": "PKCS12",
        "database.history.consumer.ssl.keystore.location": "/run/aiven/keys/public.keystore.p12",
        "database.history.consumer.ssl.keystore.password": "password",
        "database.history.consumer.ssl.truststore.location": "/run/aiven/keys/public.truststore.jks",
        "database.history.consumer.ssl.truststore.password": "password",
        "database.history.consumer.ssl.key.password": "password",
        "include.schema.changes": "true"
    }

The configuration file contains the following entries:

* ``name``: the connector name
* ``SQLSERVER_HOST``, ``SQLSERVER_PORT``, ``SQLSERVER_DATABASE_NAME``, ``SSL_MODE``, ``SQLSERVER_USER``, ``SQLSERVER_PASSWORD``, ``SQLSERVER_TABLES``: source database parameters collected in the :ref:`prerequisite <connect_debezium_sql_server_source_prereq>` phase. 
* ``database.server.name``: the logical name of the database, dictates the prefix that will be used for Apache Kafka topic names. The resulting topic name will be the concatenation of the ``database.server.name`` and the table name.
* ``tasks.max``: maximum number of tasks to execute in parallel. By default this is 1, the connector can use at most 1 task for each source table defined.
* ``poll.interval.ms``: the frequency of the queries to the CDC tables.
* ``database.history.kafka.bootstrap.servers``: points to the Aiven for Apache Kafka service where the connector is running and is needed to store :ref:`schema definition changes <connect_debezium_sql_server_schema_versioning>`
* ``database.history.producer`` and ``database.history.consumer``: points to truststores and keystores pre-created on the Aiven for Apache Kafka node to handle SSL authentication

.. Warning::

    The values defined for each ``database.history.producer`` and ``database.history.consumer`` parameters are already set to work with the predefined truststore and keystore created in the Aiven for Apache Kafka nodes. Therefore, they **should not be changed**.

* ``key.converter`` and ``value.converter``:  defines the messages data format in the Apache Kafka topic. The ``io.confluent.connect.avro.AvroConverter`` converter pushes messages in Avro format. To store the messages schema we use Aiven's `Karapace schema registry <https://github.com/aiven/karapace>`_ as specified by the ``schema.registry.url`` parameter and related credentials.

.. Note::

    The ``key.converter`` and ``value.converter`` sections are only needed when pushing data in Avro format. If omitted the messages will be defined in JSON format.


Create a Kafka Connect connector with Aiven CLI
'''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, execute the following :ref:`Aiven CLI command <avn_service_connector_create>`, replacing the ``SERVICE_NAME`` with the name of the Aiven service where the connector needs to run:

:: 

    avn service connector create SERVICE_NAME @debezium_source_sql_server.json

Check the connector status with the following command, replacing the ``SERVICE_NAME`` with the Aiven service and the ``CONNECTOR_NAME`` with the name of the connector defined before:

::

    avn service connector status SERVICE_NAME CONNECTOR_NAME

Verify the presence of the topic and data in the Apache Kafka target instance.

.. Tip::

    If you're using Aiven for Apache Kafka, topics will not be created automatically. Either create them manually following the ``database.server.name.schema_name.table_name`` naming pattern or enable the ``kafka.auto_create_topics_enable`` advanced parameter.
