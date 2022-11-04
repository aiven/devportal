Create a Google Pub/Sub sink connector
========================================

The `Google Pub/Sub sink connector <https://github.com/GoogleCloudPlatform/pubsub>`_ enables you to push data from an Aiven for Apache Kafka® topic to a Google Pub/Sub topic. 

.. note::

    You can check the full set of available parameters and configuration options in the `connector's documentation <https://github.com/GoogleCloudPlatform/pubsub>`_.

.. _connect_pubsub_sink_prereq:

Prerequisites
-------------

To setup an Google Pub/Sub sink connector, you need an Aiven for Apache Kafka service :doc:`with Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`. 

Furthermore you need to collect the following information about the target Google Pub/Sub upfront:

* ``GCP_PROJECT_NAME``: The GCP project name where the target Google Pub/Sub is located
* ``GCP_TOPIC``: the name of the target Google Pub/Sub topic
* ``GCP_SERVICE_KEY``: A valid GCP service account key for the ``GCP_PROJECT_NAME``. To create the project key review the :ref:`dedicated document <gcp-bigquery-sink-connector-google-account>`

  .. Warning::

     The GCP Pub/Sub sink connector accepts the ``GCP_SERVICE_KEY`` JSON service key as a string, therefore all  ``"`` symbols within it must be escaped ``\"``.

     The ``GCP_SERVICE_KEY`` parameter should be in the format ``{\"type\": \"service_account\",\"project_id\": \"XXXXXX\", ...}``

     Additionally, any ``\n`` symbols contained in the ``private_key`` field need to be escaped (by substituting with ``\\n``)

* ``KAFKA_TOPIC``: The name of the target topic in Aiven for Apache Kafka
* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PORT``: The Apache Kafka's schema registry port, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_USER``: The Apache Kafka's schema registry username, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PASSWORD``: The Apache Kafka's schema registry user password, only needed when using Avro as data format


.. Note::

    The ``SCHEMA_REGISTRY`` related parameters are available in the Aiven for Apache Kafka® service page, *Overview* tab, and *Schema Registry* subtab

    As of version 3.0, Aiven for Apache Kafka no longer supports Confluent Schema Registry. For more information, read `the article describing the replacement, Karapace <https://help.aiven.io/en/articles/5651983>`_

Setup a Google Pub/Sub sink connector with Aiven Console
--------------------------------------------------------

The following example demonstrates how to setup a Google Pub/Sub sink connector for Apache Kafka using the `Aiven Console <https://console.aiven.io/>`_.

Define a Kafka Connect configuration file
'''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``pubsub_sink.json``) with the following content:

.. code-block:: json

    {
        "name":"CONNECTOR_NAME",
        "connector.class": "com.google.pubsub.kafka.sink.CloudPubSubSinkConnector",
        "topics": "KAFKA_TOPIC",
        "cps.project": "GCP_PROJECT_NAME",
        "cps.topic": "GCP_TOPIC",
        "gcp.credentials.json": "GCP_SERVICE_KEY",
        "key.converter": "io.confluent.connect.avro.AvroConverter",
        "key.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "key.converter.basic.auth.credentials.sink": "USER_INFO",
        "key.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD",
        "value.converter": "io.confluent.connect.avro.AvroConverter",
        "value.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "value.converter.basic.auth.credentials.sink": "USER_INFO",
        "value.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD"
    }

The configuration file contains the following entries:

* ``name``: the connector name
* ``topics``: the source Apache Kafka topic names, divided by comma
* ``cps.project``: the GCP project name where the target Google Pub/Sub is located
* ``cps.topic``: the name of the target Google Pub/Sub topic
* ``gcp.credentials.json``: contains the GCP service account key, correctly escaped as defined in the :ref:`prerequisite phase <connect_pubsub_sink_prereq>`
* ``key.converter`` and ``value.converter``:  define the message data format in the Apache Kafka topic. The ``io.confluent.connect.avro.AvroConverter`` converter translates messages from the Avro format. To retrieve the message schema we use Aiven's `Karapace schema registry <https://github.com/aiven/karapace>`_, as specified by the ``schema.registry.url`` parameter and related credentials.

  .. note::

     The ``key.converter`` and ``value.converter`` sections are only needed when the sink data is in Avro format. If omitted the messages will be read as binary format.

     When using Avro as sink data format, you need to set following parameters

     * ``value.converter.schema.registry.url``: pointing to the Aiven for Apache Kafka schema registry URL in the form of ``https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT`` with the ``APACHE_KAFKA_HOST`` and ``SCHEMA_REGISTRY_PORT`` parameters :ref:`retrieved in the previous step <connect_pubsub_sink_prereq>`.
     * ``value.converter.basic.auth.credentials.sink``: to the value ``USER_INFO``, since you're going to login to the schema registry using username and password.
     * ``value.converter.schema.registry.basic.auth.user.info``: passing the required schema registry credentials in the form of ``SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD`` with the ``SCHEMA_REGISTRY_USER`` and ``SCHEMA_REGISTRY_PASSWORD`` parameters :ref:`retrieved in the previous step <connect_pubsub_sink_prereq>`.

  
The full list of parameters is available in the `dedicated GitHub page <https://github.com/GoogleCloudPlatform/pubsub/>`_.

Create a Kafka Connect connector with the Aiven Console
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, access the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Apache Kafka® or Aiven for Apache Kafka Connect® service where the connector needs to be defined, then:

1. Click on the **Connectors** tab
2. Clink on **Create New Connector**, the button is enabled only for services :doc:`with Kafka Connect enabled <enable-connect>`.
3. Select the **Google Pub/Sub sink**
4. Under the *Common* tab, locate the **Connector configuration** text box and click on **Edit**
5. Paste the connector configuration (stored in the ``pubsub_sink.json`` file) in the form
6. Click on **Apply**

   .. note::

      The Aiven Console parses the configuration file and fills the relevant UI fields. You can review the UI fields across the various tabs and change them if necessary. The changes will be reflected in JSON format in the **Connector configuration** text box.

7. After all the settings are correctly configured, click on **Create new connector**
8. Verify the connector status under the **Connectors** tab
9. Verify the presence of the data in the target Pub/Sub dataset, the table name is equal to the Apache Kafka topic name.

   .. note::

      Connectors can be created also using the dedicated :ref:`Aiven CLI command <avn_service_connector_create>`.

Example: Create a Google Pub/Sub sink connector
-------------------------------------------------

You have an Apache Kafka topic ``iot_metrics`` that you want to push to a Google Pub/Sub topic ``iot_metrics_pubsub``, you can create a sink connector with the following configuration, after replacing the placeholders for ``GCP_PROJECT_NAME`` and ``GCP_SERVICE_KEY``:

.. code-block:: json

     {
        "name":"CONNECTOR_NAME",
        "connector.class": "com.google.pubsub.kafka.sink.CloudPubSubSinkConnector",
        "topics": "iot_metrics",
        "cps.project": "GCP_PROJECT_NAME",
        "cps.topic": "iot_metrics_pubsub",
        "gcp.credentials.json": "GCP_SERVICE_KEY"
    }
