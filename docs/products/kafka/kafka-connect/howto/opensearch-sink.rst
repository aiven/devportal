Create an OpenSearch® sink connector
======================================

The OpenSearch sink connector enables you to move data from an Aiven for Apache Kafka® cluster to an OpenSearch® instance for further processing and analysis. 

.. Warning::

    This article describes how to create a sink connector to OpenSearch®. Similar instructions are available also for Elasticsearch® in the :doc:`dedicated article <elasticsearch-sink>`.

.. _connect_opensearch_sink_prereq:

Prerequisites
-------------

To setup an OpenSearch sink connector, you need an Aiven for Apache Kafka service :doc:`with Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`. 

Furthermore you need to collect the following information about the target OpenSearch service upfront:

* ``OS_CONNECTION_URL``: The OpenSearch connection URL
* ``OS_USERNAME``: The OpenSearch username to connect
* ``OS_PASSWORD``: The password for the username selected
* ``TOPIC_LIST``: The list of topics to sink
* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PORT``: The Apache Kafka's schema registry port, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_USER``: The Apache Kafka's schema registry username, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PASSWORD``: The Apache Kafka's schema registry user password, only needed when using Avro as data format


.. Note::

    If you're using Aiven for OpenSearch® and Aiven for Apache Kafka® the above details are available in the `Aiven console <https://console.aiven.io/>`_ service *Overview tab* or via the dedicated ``avn service get`` command with the :ref:`Aiven CLI <avn_service_get>`.

    The ``SCHEMA_REGISTRY`` related parameters are available in the Aiven for Apache Kafka® service page, *Overview* tab, and *Schema Registry* subtab

Setup an OpenSearch sink connector with Aiven CLI
---------------------------------------------------

The following example demonstrates how to setup a OpenSearch sink connector for Apache Kafka using the :ref:`Aiven CLI dedicated command <avn_service_connector_create>`.

Define a Kafka Connect configuration file
'''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``opensearch_sink.json``) with the following content:

.. code-block:: json

    {
        "name":"CONNECTOR_NAME",
        "connector.class": "io.aiven.kafka.connect.opensearch.OpensearchSinkConnector",
        "topics": "TOPIC_LIST",
        "connection.url": "OS_CONNECTION_URL",
        "connection.username": "OS_USERNAME",
        "connection.password": "OS_PASSWORD",
        "type.name": "TYPE_NAME",
        "tasks.max":"1",
        "key.ignore": "true",
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
* ``connection.url``, ``connection.username``, ``connection.password``: sink OpenSearch parameters collected in the :ref:`prerequisite <connect_opensearch_sink_prereq>` phase. 
* ``type.name``: the OpenSearch type name to be used when indexing.
* ``key.ignore``: boolean flag dictating if to ignore the message key. If set to true, the document ID is generated as message's ``topic+partition+offset``, the message key is used as ID otherwise.
* ``tasks.max``: maximum number of tasks to execute in parallel. By default this is 1.
* ``key.converter`` and ``value.converter``:  defines the messages data format in the Apache Kafka topic. The ``io.confluent.connect.avro.AvroConverter`` converter translates messages from the Avro format. To retrieve the messages schema we use Aiven's `Karapace schema registry <https://github.com/aiven/karapace>`_ as specified by the ``schema.registry.url`` parameter and related credentials.

.. Note::

    The ``key.converter`` and ``value.converter`` sections are only needed when the source data is in Avro format. If omitted the messages will be read as binary format. 

    When using Avro as source data format, you need to set following parameters

    * ``value.converter.schema.registry.url``: pointing to the Aiven for Apache Kafka schema registry URL in the form of ``https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT`` with the ``APACHE_KAFKA_HOST`` and ``SCHEMA_REGISTRY_PORT`` parameters :ref:`retrieved in the previous step <connect_opensearch_sink_prereq>`.
    * ``value.converter.basic.auth.credentials.source``: to the value ``USER_INFO``, since you're going to login to the schema registry using username and password.
    * ``value.converter.schema.registry.basic.auth.user.info``: passing the required schema registry credentials in the form of ``SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD`` with the ``SCHEMA_REGISTRY_USER`` and ``SCHEMA_REGISTRY_PASSWORD`` parameters :ref:`retrieved in the previous step <connect_elasticsearch_sink_prereq>`. 


Create a Kafka Connect connector with the Aiven CLI
'''''''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, execute the following :ref:`Aiven CLI command <avn_service_connector_create>`, replacing the ``SERVICE_NAME`` with the name of the Aiven for Apache Kafka® service where the connector needs to run:

.. code-block:: console 

    avn service connector create SERVICE_NAME @opensearch_sink.json

Check the connector status with the following command, replacing the ``SERVICE_NAME`` with the Aiven for Apache Kafka® service and the ``CONNECTOR_NAME`` with the name of the connector defined before:

.. code-block:: console

    avn service connector status SERVICE_NAME CONNECTOR_NAME

Verify the presence of the data in the target OpenSearch service, the index name is equal to the Apache Kafka topic name.

Create daily OpenSearch indexes
----------------------------------

You might need to create a new OpenSearch index on daily basis to store the Apache Kafka messages. 
Adding the following ``TimestampRouter`` transformation in the connector properties file provides a way to define the index name as concatenation of the topic name and message date.

.. code-block:: json

    "transforms": "TimestampRouter",
    "transforms.TimestampRouter.topic.format": "${topic}-${timestamp}",
    "transforms.TimestampRouter.timestamp.format": "yyyy-MM-dd",
    "transforms.TimestampRouter.type": "org.apache.kafka.connect.transforms.TimestampRouter"

.. Warning::

    The current version of the OpenSearch sink connector is not able to automatically create daily indexes in OpenSearch. Therefore you need to create the indexes with the correct name before starting the sink connector. You can create OpenSearch indexes in many ways including :doc:`CURL commands </docs/products/opensearch/howto/opensearch-with-curl>`.

Example: Create an OpenSearch® sink connector on a topic with a JSON schema
-----------------------------------------------------------------------------

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
        "payload":{"iot_id":2, "metric":"Humidity", "measurement":60}}
    }

.. Note::

    Since the JSON schema needs to be defined in every message, there is a big overhead to transmit the information. To achieve a better performance in term of information-message ratio you should use the Avro format together with the `Karapace schema registry <https://karapace.io/>`__ provided by Aiven

You can sink the ``iot_measurements`` topic to OpenSearch with the following connector configuration, after replacing the placeholders for ``OS_CONNECTION_URL``, ``OS_USERNAME`` and ``OS_PASSWORD``:

.. code-block:: json

    {
        "name":"sink_iot_json_schema",
        "connector.class": "io.aiven.kafka.connect.opensearch.OpensearchSinkConnector",
        "topics": "iot_measurements",
        "connection.url": "OS_CONNECTION_URL",
        "connection.username": "OS_USERNAME",
        "connection.password": "OS_PASSWORD",
        "type.name": "iot_measurements",
        "tasks.max":"1",
        "key.ignore": "true",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter"
    }

The configuration file contains the following peculiarities:

* ``"topics": "iot_measurements"``: setting the topic to sink
* ``"value.converter": "org.apache.kafka.connect.json.JsonConverter"``: the message value is in plain JSON format without a schema
* ``"key.ignore": "true"``: the connector is ignoring the message key (empty), and generating documents with ID equal to ``topic+partition+offset``


Example: Create an OpenSearch® sink connector on a topic in plain JSON format
-----------------------------------------------------------------------------

If you have a topic named ``students`` containing the following data in JSON format, without a defined schema:

.. code-block:: text

    Key: 1 Value: {"student_id":1, "student_name":"Carla"}
    Key: 2 Value: {"student_id":2, "student_name":"Ugo"}
    Key: 3 Value: {"student_id":3, "student_name":"Mary"}

You can sink the ``students`` topic to OpenSearch with the following connector configuration, after replacing the placeholders for ``OS_CONNECTION_URL``, ``OS_USERNAME`` and ``OS_PASSWORD``:

.. code-block:: json

    {
        "name":"sink_students_json",
        "connector.class": "io.aiven.kafka.connect.opensearch.OpensearchSinkConnector",
        "topics": "students",
        "connection.url": "OS_CONNECTION_URL",
        "connection.username": "OS_USERNAME",
        "connection.password": "OS_PASSWORD",
        "type.name": "students",
        "tasks.max":"1",
        "key.converter": "org.apache.kafka.connect.storage.StringConverter",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "value.converter.schemas.enable": "false",
        "schema.ignore": "true"
    }

The configuration file contains the following peculiarities:

* ``"topics": "students"``: setting the topic to sink
* ``"key.converter": "org.apache.kafka.connect.storage.StringConverter"``: the message key is a string
* ``"value.converter": "org.apache.kafka.connect.json.JsonConverter"``: the message value is in plain JSON format without a schema
* ``"value.converter.schemas.enable": "false"``: since the data in the value doesn't have a schema, the connector shouldn't try to read it and sets it to null
* ``"schema.ignore": "true"``: since the value schema is null, the connector doesn't infer it before pushing the data to OpenSearch

.. Note::

    The OpenSearch document ID is set as the message key