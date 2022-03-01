Create a JDBC sink connector
============================

The JDBC (Java Database Connectivity) sink connector enables you to move data from an Aiven for Apache Kafka® cluster to any relational database offering JDBC drivers like PostgreSQL® or MySQL.

.. Warning::

    Since the JDBC sink connector is pushing data to relational databases, it can work only with topics having a schema, either defined in every message or in the schema registry features offered by `Karapace <https://help.aiven.io/en/articles/5651983>`_

.. _connect_jdbc_sink_prereq:

Prerequisites
-------------

To setup n JDBC sink connector, you need an Aiven for Apache Kafka service :doc:`with Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`.

Furthermore you need to collect the following information about the target database service upfront:

* ``DB_CONNECTION_URL``: The database JDBC connection URL, the following are few examples based on different technologies:
    * PostgreSQL: ``jdbc:postgresql://HOST:PORT/DB_NAME?sslmode=SSL_MODE``
    * MySQL: ``jdbc:mysql://HOST:PORT/DB_NAME?ssl-mode=SSL_MODE``

* ``DB_USERNAME``: The database username to connect
* ``DB_PASSWORD``: The password for the username selected
* ``TOPIC_LIST``: The list of topics to sink divided by comma
* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PORT``: The Apache Kafka's schema registry port, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_USER``: The Apache Kafka's schema registry username, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PASSWORD``: The Apache Kafka's schema registry user password, only needed when using Avro as data format


.. Note::

    If you're using Aiven for PostgreSQL® and Aiven for MySQL® the above details are available in the `Aiven console <https://console.aiven.io/>`_ service *Overview tab* or via the dedicated ``avn service get`` command with the :ref:`Aiven CLI <avn_service_get>`.

    The ``SCHEMA_REGISTRY`` related parameters are available in the Aiven for Apache Kafka® service page, *Overview* tab, and *Schema Registry* subtab

    As of version 3.0, Aiven for Apache Kafka no longer supports Confluent Schema Registry. For more information, read `the article describing the replacement, Karapace <https://help.aiven.io/en/articles/5651983>`_

Setup a JDBC sink connector with Aiven Console
----------------------------------------------------

The following example demonstrates how to setup a JDBC sink connector for Apache Kafka using the `Aiven Console <https://console.aiven.io/>`_.

Define a Kafka Connect configuration file
'''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``jdbc_sink.json``) with the following content:

.. code-block:: json

    {
        "name":"CONNECTOR_NAME",
        "connector.class": "io.aiven.connect.jdbc.JdbcSinkConnector",
        "topics": "TOPIC_LIST",
        "connection.url": "DB_CONNECTION_URL",
        "connection.user": "DB_USERNAME",
        "connection.password": "DB_PASSWORD",
        "tasks.max":"1",
        "auto.create": "true",
        "auto.evolve": "true",
        "insert.mode": "upsert",
        "delete.enabled": "true",
        "pk.mode": "record_key",
        "pk.fields": "field1,field2",
        "key.converter": "io.confluent.connect.avro.AvroConverter",
        "key.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "key.converter.basic.auth.credentials.source": "USER_INFO",
        "key.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD",
        "value.converter": "io.confluent.connect.avro.AvroConverter",
        "value.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "value.converter.basic.auth.credentials.source": "USER_INFO",
        "value.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD"
    }

The configuration file contains the following entries:

* ``name``: the connector name
* ``connection.url``, ``connection.username``, ``connection.password``: sink JDBC parameters collected in the :ref:`prerequisite <connect_jdbc_sink_prereq>` phase. 
* ``tasks.max``: maximum number of tasks to execute in parallel. The maximum is 1 per topic and partition.
* ``auto.create``: boolean flag enabling the target table creation if it doesn't exists.
* ``auto.evolve``: boolean flag enabling the target table modification in cases of schema modification of the messages in the topic.
* ``insert.mode``: defines the insert mode, it can be:
    * ``insert``: uses standard ``INSERT`` statements.
    * ``upsert``: uses the upsert semantics supported by the target database, more information in the `dedicated GitHub repository <https://github.com/aiven/jdbc-connector-for-apache-kafka/blob/master/docs/sink-connector.md>`__
    * ``update``: uses the update semantics supported by the target database. E.g. ``UPDATE``, more information in the `dedicated GitHub repository <https://github.com/aiven/jdbc-connector-for-apache-kafka/blob/master/docs/sink-connector.md>`__

* ``delete.enabled``: boolean flag enabling the deletion of rows in the target table on tombstone messages.

.. Note::

    A tombstone message has:
    
    * a not null **key**
    * a null **value**

    In case of tombstone messages and ``delete.enabled`` set to ``true``, the JDBC sink connector will delete the row referenced by the message key. If set to ``true``, it requires the ``pk.mode`` to be ``record_key`` to be able to identify the rows to delete.


* ``pk.mode``: defines the fields to use as primary key. Allowed options are:
    * ``none``: no primary key is used.
    * ``kafka``: the Apache Kafka coordinates are used.
    * ``record_key``: the entire (or part of the) message key is used.
    * ``record_value``: the entire (or part of the) message value is used.

    More information are available in the `dedicated GitHub repository <https://github.com/aiven/jdbc-connector-for-apache-kafka/blob/master/docs/sink-connector.md>`__.
    
* ``pk.fields``: defines which fields of the composite key or value to use as record key in the database.

* ``key.converter`` and ``value.converter``:  defines the messages data format in the Apache Kafka topic. The ``io.confluent.connect.avro.AvroConverter`` converter translates messages from the Avro format. To retrieve the messages schema we use Aiven's `Karapace schema registry <https://github.com/aiven/karapace>`_ as specified by the ``schema.registry.url`` parameter and related credentials.

.. Note::

    The ``key.converter`` and ``value.converter`` sections define how the topic messages will be parsed and needs to be included in the connector configuration. 

    When using Avro as source data format, you need to set following parameters

    * ``value.converter.schema.registry.url``: pointing to the Aiven for Apache Kafka schema registry URL in the form of ``https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT`` with the ``APACHE_KAFKA_HOST`` and ``SCHEMA_REGISTRY_PORT`` parameters :ref:`retrieved in the previous step <connect_jdbc_sink_prereq>`.
    * ``value.converter.basic.auth.credentials.source``: to the value ``USER_INFO``, since you're going to login to the schema registry using username and password.
    * ``value.converter.schema.registry.basic.auth.user.info``: passing the required schema registry credentials in the form of ``SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD`` with the ``SCHEMA_REGISTRY_USER`` and ``SCHEMA_REGISTRY_PASSWORD`` parameters :ref:`retrieved in the previous step <connect_jdbc_sink_prereq>`. 


Create a Kafka Connect connector with the Aiven Console
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, access the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Apache Kafka® or Aiven for Apache Kafka Connect® service where the connector needs to be defined, then:

1. Click on the **Connectors** tab
2. Clink on **Create New Connector**, the button is enabled only for services :doc:`with Kafka Connect enabled <enable-connect>`.
3. Select the **JDBC sink**
4. Under the *Common* tab, locate the **Connector configuration** text box and click on **Edit**
5. Paste the connector configuration (stored in the ``jdbc_sink.json`` file) in the form
6. Click on **Apply**

.. Note::

    The Aiven Console parses the configuration file and fills the relevant UI fields. You can review the UI fields across the various tab and change them if necessary. The changes will be reflected in JSON format in the **Connector configuration** text box.

7. After all the settings are correctly configured, click on **Create new connector**
8. Verify the connector status under the **Connectors** tab
9. Verify the presence of the data in the target OpenSearch® service, the index name is equal to the Apache Kafka topic name

.. Note::

    Connectors can be created also using the dedicated :ref:`Aiven CLI command <avn_service_connector_create>`.

Example: Create a JDBC sink connector to PostgreSQL® on a topic with a JSON schema
----------------------------------------------------------------------------------

If you have a topic named ``iot_measurements`` containing the following data in JSON format, with a defined JSON schema:

.. code-block:: json

    {
        "schema": {
            "type":"struct",
            "fields":[{
                "type":"int64",
                "optional": false,
                "field": "iot_id"
                },{
                "type":"string",
                "optional": false,
                "field": "metric"
                },{
                "type":"int32",
                "optional": false,
                "field": "measurement"
                }]
        }, 
        "payload":{ "iot_id":1, "metric":"Temperature", "measurement":14}
    }
    {
        "schema": {
            "type":"struct",
            "fields":[{
                "type":"int64",
                "optional": false,
                "field": "iot_id"
                },{
                "type":"string",
                "optional": false,
                "field": "metric"
                },{
                "type":"int32",
                "optional": false,
                "field": "measurement"
                }]
        }, 
        "payload":{"iot_id":2, "metric":"Humidity", "measurement":60}
    }

.. Note::

    Since the JSON schema needs to be defined in every message, there is a big overhead to transmit the information. To achieve a better performance in term of information-message ratio you should use the Avro format together with the `Karapace schema registry <https://karapace.io/>`__ provided by Aiven

You can sink the ``iot_measurements`` topic to PostgreSQL with the following connector configuration, after replacing the placeholders for ``DB_HOST``, ``DB_PORT``, ``DB_NAME``, ``DB_SSL_MODE``, ``DB_USERNAME`` and ``DB_PASSWORD``:

.. code-block:: json

    {
        "name":"sink_iot_json_schema",
        "connector.class": "io.aiven.connect.jdbc.JdbcSinkConnector",
        "topics": "iot_measurements",
        "connection.url": "jdbc:postgresql://DB_HOST:DB_PORT/DB_NAME?sslmode=DB_SSL_MODE",
        "connection.user": "DB_USERNAME",
        "connection.password": "DB_PASSWORD",
        "tasks.max":"1",
        "auto.create": "true",
        "auto.evolve": "true",
        "insert.mode": "upsert",
        "delete.enabled": "false",
        "pk.mode": "record_value",
        "pk.fields": "iot_id",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter"
    }

The configuration file contains the following peculiarities:

* ``"topics": "iot_measurements"``: setting the topic to sink
* ``"value.converter": "org.apache.kafka.connect.json.JsonConverter"``: the message value is in plain JSON format without a schema, there is not converter defined for the key since it's empty
* ``"pk.mode": "record_value"``: the connector is using the message value to set the target database key
* ``"pk.fields": "iot_id"``: the connector is using the field ``iot_id`` on the message value to set the target database key
* ``"delete.enabled": "false"``: the connector is not enabling deletes on tombstones since they would require to have the valid record key and the ``pk.mode`` set to ``record_key``


Example: Create a JDBC sink connector to MySQL on a topic using Avro and schema registry
----------------------------------------------------------------------------------------

If you have a topic named ``students`` containing data in Avro format with the schema stored in the schema registry provided by `Karapace <https://help.aiven.io/en/articles/5651983>`_ with the following structure:

.. code-block:: text

    key: {"student_id": 1234}
    value: {"student_name": "Mary", "exam": "Math", "exam_result":"A"} 

You can sink the ``students`` topic to MySQL with the following connector configuration, after replacing the placeholders for ``DB_HOST``, ``DB_PORT``, ``DB_NAME``, ``DB_SSL_MODE``, ``DB_USERNAME``, ``DB_PASSWORD``, ``APACHE_KAFKA_HOST``, ``SCHEMA_REGISTRY_PORT``, ``SCHEMA_REGISTRY_USER`` and ``SCHEMA_REGISTRY_PASSWORD``:

.. code-block:: json

    {
        "name": "sink_students_avro_schema",
        "connector.class": "io.aiven.connect.jdbc.JdbcSinkConnector",
        "topics": "my_pgnordics2022_pgsource.public.pasta",
        "connection.url": "jdbc:mysql://DB_HOST:DB_PORT/DB_NAME?ssl-mode=DB_SSL_MODE",
        "connection.user": "DB_USERNAME",
        "connection.password": "DB_PASSWORD",
        "insert.mode": "upsert",
        "table.name.format": "students",
        "pk.mode": "record_key",
        "pk.fields": "student_id",
        "auto.create": "true",
        "auto.evolve": "true",
        "delete.enabled": "true",
        "key.converter": "io.confluent.connect.avro.AvroConverter",
        "key.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "key.converter.basic.auth.credentials.source": "USER_INFO",
        "key.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD",
        "value.converter": "io.confluent.connect.avro.AvroConverter",
        "value.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "value.converter.basic.auth.credentials.source": "USER_INFO",
        "value.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD"
    }

The configuration file contains the following peculiarities:

* ``"topics": "students"``: setting the topic to sink
* ``"pk.mode": "record_key"``: the connector is using the message key to set the target database key
* ``"pk.fields": "student_id"``: the connector is using the field ``student_id`` on the message key to set the target database key
* ``"delete.enabled": "true"``: the connector is enabling deletes on tombstones
* ``key.converter`` and ``value.converter``: defining the Avro data format with ``io.confluent.connect.avro.AvroConverter``, the URL, and credentials to connect to the `Karapace <https://help.aiven.io/en/articles/5651983>`_ schema registry

The connector will automatically create ``"auto.create": "true"`` a table in the target MySQL database called ``students`` with ``student_id``, ``student_name``, ``exam`` and ``exam_result`` as columns and populate it with the data coming from the ``students`` Apache Kafka topic.
