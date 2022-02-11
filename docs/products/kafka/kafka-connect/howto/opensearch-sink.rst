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

    If you're using Aiven for OpenSearch® and Aiven for Apache Kafka® the above details are available in the `Aiven console <https://console.aiven.io/>`_ service Overview tab or via the dedicated ``avn service get`` command with the :ref:`Aiven CLI <avn_service_get>`.

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
        "connection.url": "ES_CONNECTION_URL",
        "connection.username": "ES_USERNAME",
        "connection.password": "ES_PASSWORD",
        "type.name": "TYPE_NAME",
        "tasks.max":"NR_TASKS",
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
* ``OS_CONNECTION_URL``, ``OS_USERNAME``, ``OS_PASSWORD``: sink OpenSearch parameters collected in the :ref:`prerequisite <connect_opensearch_sink_prereq>` phase. 
* ``type.name``: the OpenSearch type name to be used when indexing.
* ``key.ignore``: boolean flag dictating if to ignore the message key. If set to true, the document ID is generated as message's ``topic+partition+offset``, the message key is used as ID otherwise.
* ``tasks.max``: maximum number of tasks to execute in parallel. By default this is 1.
* ``key.converter`` and ``value.converter``:  defines the messages data format in the Apache Kafka topic. The ``io.confluent.connect.avro.AvroConverter`` converter translates messages from the Avro format. To retrieve the messages schema we use Aiven's `Karapace schema registry <https://github.com/aiven/karapace>`_ as specified by the ``schema.registry.url`` parameter and related credentials.

.. Note::

    The ``key.converter`` and ``value.converter`` sections are only needed when pushing data in Avro format. If omitted the messages will be defined in binary format.


Create a Kafka Connect connector with Aiven CLI
'''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, execute the following :ref:`Aiven CLI command <avn_service_connector_create>`, replacing the ``SERVICE_NAME`` with the name of the Aiven service where the connector needs to run:

:: 

    avn service connector create SERVICE_NAME @opensearch_sink.json

Check the connector status with the following command, replacing the ``SERVICE_NAME`` with the Aiven service and the ``CONNECTOR_NAME`` with the name of the connector defined before:

::

    avn service connector status SERVICE_NAME CONNECTOR_NAME

Verify the presence of the data in the target OpenSearch service, the index name is equal to the Apache Kafka topic name.

Create daily OpenSearch indexes
----------------------------------

You might need to create a new OpenSearch index on daily basis to store the Apache Kafka messages. 
Adding the following ``TimestampRouter`` transformation in the connector properties file provides a way to define the index name as concatenation of the topic name and message date.

::

    "transforms": "TimestampRouter",
    "transforms.TimestampRouter.topic.format": "${topic}-${timestamp}",
    "transforms.TimestampRouter.timestamp.format": "yyyy-MM-dd",
    "transforms.TimestampRouter.type": "org.apache.kafka.connect.transforms.TimestampRouter"

.. Warning::

    The current version of the OpenSearch sink connector is not able to automatically create daily indexes in OpenSearch. Therefore you need to create the indexes with the correct name before starting the sink connector. You can create OpenSearch indexes in many ways including :doc:`CURL commands </docs/products/opensearch/howto/opensearch-with-curl>`.