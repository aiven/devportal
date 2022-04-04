Create a Google BigQuery sink connector
=======================================

The Google BigQuery sink connector enables you to move data from an Aiven for Apache Kafka® cluster to a set of Google BigQuery tables for further processing and analysis. 


.. _connect_bigquery_sink_prereq:

Prerequisites
-------------

To setup an Google BigQuery sink connector, you need an Aiven for Apache Kafka service :doc:`with Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`. 

Furthermore you need to follow the steps :doc:`to prepare the GCP account <gcp-bigquery-sink-prereq>` and collect the following information about the target BigQuery upfront:

* ``GCP_PROJECT_NAME``: The GCP project name where the target Google BigQuery is located
* ``GCP_SERVICE_KEY``: A valid GCP service account key for the ``GCP_PROJECT_NAME``. To create the project key review the :ref:`dedicated document <gcp-bigquery-sink-connector-google-account>`

.. Warning::

    The GCP BigQuery sink connector accepts the ``GCP_SERVICE_KEY`` JSON service key as string, therefore all  ``"`` symbols within it must be escaped ``\"``.

    The ``GCP_SERVICE_KEY`` parameter should be in the format ``{\"type\": \"service_account\",\"project_id\": \"XXXXXX\", ...}``

    Additionally, any ``\n`` symbols contained in the ``private_key`` field need to be escaped (by substituting with ``\\n``)

* ``BIGQUERY_DATASET_NAME``: The BigQuery dataset name, as defined in the :ref:`dedicated pre-requisite step <gcp-bigquery-sink-connector-bigquery-dataset>`
* ``TOPIC_LIST``: The list of topics to sink divided by comma
* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PORT``: The Apache Kafka's schema registry port, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_USER``: The Apache Kafka's schema registry username, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PASSWORD``: The Apache Kafka's schema registry user password, only needed when using Avro as data format


.. Note::

    The ``SCHEMA_REGISTRY`` related parameters are available in the Aiven for Apache Kafka® service page, *Overview* tab, and *Schema Registry* subtab

    As of version 3.0, Aiven for Apache Kafka no longer supports Confluent Schema Registry. For more information, read `the article describing the replacement, Karapace <https://help.aiven.io/en/articles/5651983>`_

Setup an Google BigQuery sink connector with Aiven Console
----------------------------------------------------------

The following example demonstrates how to setup a Google BigQuery sink connector for Apache Kafka using the `Aiven Console <https://console.aiven.io/>`_.

Define a Kafka Connect configuration file
'''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``bigquery_sink.json``) with the following content:

.. code-block:: json

    {
        "name":"CONNECTOR_NAME",
        "connector.class": "io.aiven.kafka.connect.opensearch.OpensearchSinkConnector",
        "topics": "TOPIC_LIST",
        "project": "GCP_PROJECT_NAME",
        "datasets": "BIGQUERY_DATASET_NAME",
        "schemaRetriever": "com.wepay.kafka.connect.bigquery.schemaregistry.schemaretriever.SchemaRegistrySchemaRetriever",
        "schemaRegistryClient.basic.auth.credentials.source": "URL",
        "schemaRegistryLocation":"https://SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD@APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "key.converter": "io.confluent.connect.avro.AvroConverter",
        "key.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "key.converter.basic.auth.credentials.source": "USER_INFO",
        "key.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD",
        "value.converter": "io.confluent.connect.avro.AvroConverter",
        "value.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "value.converter.basic.auth.credentials.source": "USER_INFO",
        "value.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD",
        "batch.size": 1,
        "autoCreateTables": "true",
        "keySource": "JSON",
        "keyfile": "GCP_SERVICE_KEY"
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


Create a Kafka Connect connector with the Aiven Console
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, access the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Apache Kafka® or Aiven for Apache Kafka Connect® service where the connector needs to be defined, then:

1. Click on the **Connectors** tab
2. Clink on **Create New Connector**, the button is enabled only for services :doc:`with Kafka Connect enabled <enable-connect>`.
3. Select the **OpenSearch sink**
4. Under the *Common* tab, locate the **Connector configuration** text box and click on **Edit**
5. Paste the connector configuration (stored in the ``opensearch_sink.json`` file) in the form
6. Click on **Apply**

.. Note::

    The Aiven Console parses the configuration file and fills the relevant UI fields. You can review the UI fields across the various tab and change them if necessary. The changes will be reflected in JSON format in the **Connector configuration** text box.

7. After all the settings are correctly configured, click on **Create new connector**
8. Verify the connector status under the **Connectors** tab
9. Verify the presence of the data in the target OpenSearch service, the index name is equal to the Apache Kafka topic name

.. Note::

    Connectors can be created also using the dedicated :ref:`Aiven CLI command <avn_service_connector_create>`.

Create daily OpenSearch indices
----------------------------------

You might need to create a new OpenSearch index on daily basis to store the Apache Kafka messages. 
Adding the following ``TimestampRouter`` transformation in the connector properties file provides a way to define the index name as concatenation of the topic name and message date.

.. code-block:: json

    "transforms": "TimestampRouter",
    "transforms.TimestampRouter.topic.format": "${topic}-${timestamp}",
    "transforms.TimestampRouter.timestamp.format": "yyyy-MM-dd",
    "transforms.TimestampRouter.type": "org.apache.kafka.connect.transforms.TimestampRouter"

.. Warning::

    The current version of the OpenSearch sink connector is not able to automatically create daily indices in OpenSearch. Therefore you need to create the indices with the correct name before starting the sink connector. You can create OpenSearch indices in many ways including :doc:`CURL commands </docs/products/opensearch/howto/opensearch-with-curl>`.

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

------

*Elasticsearch is a trademark of Elasticsearch B.V., registered in the U.S. and in other countries.*
