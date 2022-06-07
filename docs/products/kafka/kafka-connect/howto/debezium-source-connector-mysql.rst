Create a Debezium source connector for MySQL
==================================================

The MySQL Debezium source connector extracts the changes committed to the database binary log (binlog), and writes them to an Apache Kafka® topic in a standard format where they can be transformed and read by multiple consumers.

.. _connect_debezium_mysql_schema_versioning:

Schema versioning
-----------------

Database table's schema can evolve over time by adding, modifying or removing columns. The MySQL Debezium source connector keeps track of schema changes by storing them in a separate "history" topic that you can setup with dedicated ``history.*`` configuration parameters.

.. Warning::

    The MySQL Debezium source connector ``history.*`` parameters are not visible in the list of options available in the `Aiven Console <https://console.aiven.io/>`_ but can be inserted/modified by editing the JSON configuration settings in the **Connector configuration** section.


.. _connect_debezium_mysql_source_prereq:

Prerequisites
-------------

To setup a Debezium source connector pointing to MySQL, you need an Aiven for Apache Kafka service :doc:`with Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`. 

Furthermore you need to collect the following information about the source MySQL database upfront:

* ``MYSQL_HOST``: The database hostname
* ``MYSQL_PORT``: The database port
* ``MYSQL_USER``: The database user to connect
* ``MYSQL_PASSWORD``: The database password for the ``MYSQL_USER``
* ``MYSQL_DATABASE_NAME``: The database name
* ``SSL_MODE``: The `SSL mode <https://dev.mysql.com/doc/refman/5.7/en/connection-options.html>`_
* ``MYSQL_TABLES``: The list of database tables to be included in Apache Kafka; the list must be in the form of ``schema_name1.table_name1,schema_name2.table_name2``
* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service, needed when storing the :ref:`schema definition changes <connect_debezium_mysql_schema_versioning>`
* ``APACHE_KAFKA_PORT``: The port of the Apache Kafka service, needed when storing the :ref:`schema definition changes <connect_debezium_mysql_schema_versioning>`
* ``SCHEMA_REGISTRY_PORT``: The Apache Kafka's schema registry port, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_USER``: The Apache Kafka's schema registry username, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PASSWORD``: The Apache Kafka's schema registry user password, only needed when using Avro as data format


.. Note::

    If you're using Aiven for MySQL and Aiven for Apache Kafka the above details are available in the `Aiven console <https://console.aiven.io/>`_ service Overview tab or via the dedicated ``avn service get`` command with the :ref:`Aiven CLI <avn_service_get>`.

Setup a MySQL Debezium source connector with Aiven Console
-----------------------------------------------------------

The following example demonstrates how to setup a Debezium source Connector for Apache Kafka to a MySQL database using the `Aiven Console <https://console.aiven.io/>`_.

Define a Kafka Connect configuration file
'''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``debezium_source_mysql.json``) with the following content, creating a file is not strictly necessary but allows to have all the information in one place before copy/pasting them in the `Aiven Console <https://console.aiven.io/>`_:

.. code-block:: json

    {
        "name":"CONNECTOR_NAME",
        "connector.class": "io.debezium.connector.mysql.MySqlConnector",
        "database.hostname": "MYSQL_HOST",
        "database.port": "MYSQL_PORT",
        "database.user": "MYSQL_USER",
        "database.password": "MYSQL_PASSWORD",
        "database.dbname": "MYSQL_DATABASE_NAME",
        "database.sslmode": "SSL_MODE",
        "database.server.name": "KAFKA_TOPIC_PREFIX",
        "table.include.list": "MYSQL_TABLES",
        "tasks.max":"NR_TASKS",
        "key.converter": "io.confluent.connect.avro.AvroConverter",
        "key.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "key.converter.basic.auth.credentials.source": "USER_INFO",
        "key.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD",
        "value.converter": "io.confluent.connect.avro.AvroConverter",
        "value.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "value.converter.basic.auth.credentials.source": "USER_INFO",
        "value.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD",
        "database.history.kafka.topic": "HISTORY_TOPIC_NAME",
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

* ``name``: the connector name, replace CONNECTOR_NAME with the name you want to use for the connector.
* ``MYSQL_HOST``, ``MYSQL_PORT``, ``MYSQL_DATABASE_NAME``, ``SSL_MODE``, ``MYSQL_USER``, ``MYSQL_PASSWORD``, ``MYSQL_TABLES``: source database parameters collected in the :ref:`prerequisite <connect_debezium_mysql_source_prereq>` phase. 
* ``database.server.name``: the logical name of the database, dictates the prefix that will be used for Apache Kafka topic names. The resulting topic name will be the concatenation of the ``database.server.name`` and the table name.
* ``tasks.max``: maximum number of tasks to execute in parallel. By default this is 1, the connector can use at most 1 task for each source table defined. Replace ``NR_TASKS`` with the amount of parallel task based on the number of tables.
* ``database.history.kafka.topic``: the name of the Apache Kafka topic that will contain the history of schema changes.
* ``database.history.kafka.bootstrap.servers``: points to the Aiven for Apache Kafka service where the connector is running and is needed to store :ref:`schema definition changes <connect_debezium_mysql_schema_versioning>`
* ``database.history.producer`` and ``database.history.consumer``: points to truststores and keystores pre-created on the Aiven for Apache Kafka node to handle SSL authentication

  .. Warning::

    The values defined for each ``database.history.producer`` and ``database.history.consumer`` parameters are already set to work with the predefined truststore and keystore created in the Aiven for Apache Kafka nodes. Therefore, they **should not be changed**.

* ``key.converter`` and ``value.converter``:  defines the messages data format in the Apache Kafka topic. The ``io.confluent.connect.avro.AvroConverter`` converter pushes messages in Avro format. To store the messages schema we use Aiven's `Karapace schema registry <https://github.com/aiven/karapace>`_ as specified by the ``schema.registry.url`` parameter and related credentials.

  .. Note::

    The ``key.converter`` and ``value.converter`` sections are only needed when pushing data in Avro format. If omitted the messages will be defined in JSON format.

    The ``USER_INFO`` is not a placeholder, no substitution is needed for that parameter.


Create a Kafka Connect connector with the Aiven Console
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, access the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Apache Kafka® or Aiven for Apache Kafka Connect® service where the connector needs to be defined, then:

1. Click on the **Connectors** tab
2. Clink on **Create New Connector**, the button is enabled only for services :doc:`with Kafka Connect enabled <enable-connect>`.
3. Select the **Debezium - MySQL**
4. Under the *Common* tab, locate the **Connector configuration** text box and click on **Edit**
5. Paste the connector configuration (stored in the ``debezium_source_mysql.json`` file) in the form
6. Click on **Apply**

   .. note::

    The Aiven Console parses the configuration file and fills the relevant UI fields. You can review the UI fields across the various tabs and change them if necessary. The changes will be reflected in JSON format in the **Connector configuration** text box.

7. After all the settings are correctly configured, click on **Create new connector**

   .. Tip::

    If you're using Aiven for Apache Kafka, topics will not be created automatically. Either create them manually following the ``database.server.name.schema_name.table_name`` naming pattern or enable the ``kafka.auto_create_topics_enable`` advanced parameter.

8. Verify the connector status under the **Connectors** tab
9. Verify the presence of the data in the target Apache Kafka topic coming from the MySQL dataset. The topic name is equal to concatenation of the database and table name. If you need to change the target table name, you can do so using the Kafka Connect ``RegexRouter`` transformation.

.. note::

    Connectors can be created also using the dedicated :ref:`Aiven CLI command <avn_service_connector_create>`.
