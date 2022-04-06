Create an Snowflake sink connector
==================================

The Apache Kafka Connect® Snowflake sink connector enables you to move data from an Aiven for Apache Kafka® cluster to a Snowflake database. The full connector documentation is available in the dedicated `GitHub repository <https://docs.snowflake.com/en/user-guide/kafka-connector.html>`_.

.. _connect_sink_snowflake_prereq:

Prerequisites
-------------

To setup the Snowflake sink connector, you need an Aiven for Apache Kafka® service :doc:`with Apache Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`.

Furthermore you need to follow the steps :doc:`to prepare the Snowflake account <snowflake-sink-prereq>` and collect the following information about the target Snowflake database upfront:

* ``SNOWFLAKE_URL``: The URL used to access the Snowflake account in the format of ``https://ACCOUNT_LOCATOR.REGION_ID.snowflakecomputing.com:443`` where
    *  ``ACCOUNT_LOCATOR`` is the name of the account, more information are available in the dedicated `Snowflake documentation <https://docs.snowflake.com/en/user-guide/admin-account-identifier.html>`_
    * ``REGION_ID`` is the Id of the region where the Snowflake service is available, you can review the region Ids in the `dedicated documentation <https://docs.snowflake.com/en/user-guide/intro-regions.html>`_

    .. Tip::

        The Snowflake Account id and region name can be obtained in the Snowflake UI by issuing the following query in a worksheet::

            select current_account(), current_region() 

* ``SNOWFLAKE_USERNAME``: A valid Snowflake username with enough privileges to write data in the target database as mentioned in the :doc:`prerequisite document <snowflake-sink-prereq>`.
* ``SNOWFLAKE_PRIVATE_KEY``: The private key associated to the ``SNOWFLAKE_USERNAME`` as mentioned in the :doc:`prerequisite document <snowflake-sink-prereq>`.
* ``SNOWFLAKE_PRIVATE_KEY_PASSPHRASE``: The private key passphrase
* ``SNOWFLAKE_DATABASE``: The target Snowflake database name
* ``SNOWFLAKE_SCHEMA``: The target Snowflake database schema
* ``TOPIC_LIST``: The list of topics to sink divided by comma
* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PORT``: The Apache Kafka's schema registry port, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_USER``: The Apache Kafka's schema registry username, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PASSWORD``: The Apache Kafka's schema registry user password, only needed when using Avro as data format

Setup a Snowflake sink connector with Aiven Console
---------------------------------------------------

The following example demonstrates how to setup an Apache Kafka Connect® Snowflake sink connector using the `Aiven Console <https://console.aiven.io/>`_.

Define an Apache Kafka Connect® configuration file
''''''''''''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``snowflake_sink.json``) with the following content:

.. code-block:: json

    {
        "name": "my-test-snowflake",
        "connector.class": "com.snowflake.kafka.connector.SnowflakeSinkConnector",
        "topics": "TOPIC_LIST",
        "key.converter": "io.confluent.connect.avro.AvroConverter",
        "key.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "key.converter.basic.auth.credentials.source": "USER_INFO",
        "key.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD",
        "value.converter": "io.confluent.connect.avro.AvroConverter",
        "value.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "value.converter.basic.auth.credentials.source": "USER_INFO",
        "value.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD",
        "snowflake.url.name": "SNOWFLAKE_URL",
        "snowflake.user.name": "SNOWFLAKE_USERNAME",
        "snowflake.private.key": "SNOWFLAKE_PRIVATE_KEY",
        "snowflake.private.key.passphrase": "SNOWFLAKE_PRIVATE_KEY_PASSPHRASE",
        "snowflake.database.name": "SNOWFLAKE_DATABASE",
        "snowflake.schema.name": "SNOWFLAKE_SCHEMA"
    }

The configuration file contains the following entries:

* ``name``: The connector name
* ``topics``: The list of Apache Kafka® topics to sink to the GCS bucket
* ``key.converter`` and ``value.converter``:  defines the messages data format in the Apache Kafka topic. The ``io.confluent.connect.avro.AvroConverter`` converter translates messages from the Avro format. To retrieve the messages schema we use Aiven's `Karapace schema registry <https://github.com/aiven/karapace>`_ as specified by the ``schema.registry.url`` parameter and related credentials.

.. Note::

    The ``key.converter`` and ``value.converter`` sections define how the topic messages will be parsed and needs to be included in the connector configuration. 

    When using Avro as source data format, you need to set following parameters

    * ``value.converter.schema.registry.url``: pointing to the Aiven for Apache Kafka schema registry URL in the form of ``https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT`` with the ``APACHE_KAFKA_HOST`` and ``SCHEMA_REGISTRY_PORT`` parameters :ref:`retrieved in the previous step <connect_sink_snowflake_prereq>`.
    * ``value.converter.basic.auth.credentials.source``: to the value ``USER_INFO``, since you're going to login to the schema registry using username and password.
    * ``value.converter.schema.registry.basic.auth.user.info``: passing the required schema registry credentials in the form of ``SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD`` with the ``SCHEMA_REGISTRY_USER`` and ``SCHEMA_REGISTRY_PASSWORD`` parameters :ref:`retrieved in the previous step <connect_sink_snowflake_prereq>`. 


* ``snowflake.url.name``: The URL to access the Snowflake service
* ``snowflake.user.name``: The connection user
* ``snowflake.private.key``: The user's private key
* ``snowflake.private.key.passphrase``: The private key passphrase
* ``snowflake.database.name``: The Snowflake database name
* ``snowflake.schema.name``: The Snowflake schema name


Create a Kafka Connect connector with the Aiven Console
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, access the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Apache Kafka® or Aiven for Apache Kafka Connect® service where the connector needs to be defined, then:

1. Click on the **Connectors** tab
2. Clink on **Create New Connector**, the button is enabled only for services :doc:`with Kafka Connect enabled <enable-connect>`.
3. Select the **Snowflake Sink**
4. Under the *Common* tab, locate the **Connector configuration** text box and click on **Edit**
5. Paste the connector configuration (stored in the ``snowflake_sink.json`` file) in the form
6. Click on **Apply**

.. Note::

    The Aiven Console parses the configuration file and fills the relevant UI fields. You can review the UI fields across the various tab and change them if necessary. The changes will be reflected in JSON format in the **Connector configuration** text box.

7. After all the settings are correctly configured, click on **Create new connector**
8. Verify the connector status under the **Connectors** tab
9. Verify the presence of the data in the target Snowflake database

.. Note::

    Connectors can be created also using the dedicated :ref:`Aiven CLI command <avn_service_connector_create>`.


Example: Create a Snowflake sink connector on a topic in Avro format
--------------------------------------------------------------------

The example creates an Snowflake sink connector with the following properties:

* connector name: ``my_snowflake_sink``
* source topics: ``test``
* Snowflake database: ``testdb``
* Snowflake schema: ``testschema``
* Snowflake URL: ``https://XX0000.eu-central-1.snowflakecomputing.com:443``
* Snowflake user: ``testuser``
* User private key:: 

    XXXXXXXYYY
    ZZZZZZZZZZ
    KKKKKKKKKK
    YY

* User private key passphrase: ``password123``


The connector configuration is the following:

.. code-block:: json

    {
        "name": "my_snowflake_sink",
        "connector.class": "com.snowflake.kafka.connector.SnowflakeSinkConnector",
        "key.converter": "io.confluent.connect.avro.AvroConverter",
        "key.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "key.converter.basic.auth.credentials.source": "USER_INFO",
        "key.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD",
        "value.converter": "io.confluent.connect.avro.AvroConverter",
        "value.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "value.converter.basic.auth.credentials.source": "USER_INFO",
        "value.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD",
        "topics": "test",
        "snowflake.url.name": "https://XX0000.eu-central-1.snowflakecomputing.com:443",
        "snowflake.user.name": "testkafka",
        "snowflake.private.key": "XXXXXXXYYY
            ZZZZZZZZZZ
            KKKKKKKKKK
            YY",
        "snowflake.private.key.passphrase": "password123",
        "snowflake.database.name": "testdb",
        "snowflake.schema.name": "testschema"
    }

Example: Create a Snowflake sink connector on a topic with a JSON schema
------------------------------------------------------------------------

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

You can sink the ``iot_measurements`` topic to PostgreSQL with the following connector configuration, after replacing the placeholders for ``SNOWFLAKE_URL``, ``SNOWFLAKE_USERNAME``, ``SNOWFLAKE_PRIVATE_KEY``, ``SNOWFLAKE_PRIVATE_KEY_PASSPHRASE``, ``SNOWFLAKE_DATABASE`` and ``SNOWFLAKE_SCHEMA``:

.. code-block:: json

    {
        "name": "my-test-snowflake-1",
        "connector.class": "com.snowflake.kafka.connector.SnowflakeSinkConnector",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "topics": "iot_measurements",
        "snowflake.url.name": "SNOWFLAKE_URL",
        "snowflake.user.name": "SNOWFLAKE_USERNAME",
        "snowflake.private.key": "SNOWFLAKE_PRIVATE_KEY",
        "snowflake.private.key.passphrase": "SNOWFLAKE_PRIVATE_KEY_PASSPHRASE",
        "snowflake.database.name": "SNOWFLAKE_DATABASE",
        "snowflake.schema.name": "SNOWFLAKE_SCHEMA"
    }

The configuration file contains the following peculiarities:

* ``"topics": "iot_measurements"``: setting the topic to sink
* ``"value.converter": "org.apache.kafka.connect.json.JsonConverter"``: the message value is in JSON format with a schema, there is not key converter defined for the key since it's empty