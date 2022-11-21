Create Splunk sink connector
=============================

The `Splunk <https://www.splunk.com/>`_ sink connector enables you to move data from an Aiven for Apache Kafka® cluster to a remote Splunk server via `HTTP event collector <https://docs.splunk.com/Documentation/Splunk/latest/Data/FormateventsforHTTPEventCollector>`_ (HEC).

.. note::

    You can check the full set of available parameters and configuration options in the `connector's documentation <https://github.com/splunk/kafka-connect-splunk>`_.

.. _connect_splunk_sink_prereq:

Prerequisites
-------------

To setup an Splunk sink connector, you need an Aiven for Apache Kafka service :doc:`with Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`.

Furthermore you need to collect the following information about the target server:

* ``SPLUNK_HEC_TOKEN``: The `HEC authentication token <https://docs.splunk.com/Documentation/Splunk/latest/Data/FormateventsforHTTPEventCollector>`_
* ``SPLUNK_HEC_URI``: The `Splunk endpoint URI <https://docs.splunk.com/Documentation/Splunk/9.0.1/Data/UsetheHTTPEventCollector>`_
* ``TOPIC_LIST``: The list of topics to sink divided by comma
* ``SPLUNK_INDEXES``: The list of Splunk indexes where the data will be landing

and, if you are using Avro as the data format:

* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service
* ``SCHEMA_REGISTRY_PORT``: The Apache Kafka's schema registry port
* ``SCHEMA_REGISTRY_USER``: The Apache Kafka's schema registry username
* ``SCHEMA_REGISTRY_PASSWORD``: The Apache Kafka's schema registry user password

.. Note::

    You can browse the additional parameters available for the ``static`` and ``oauth2`` authorization types in the `dedicated documentation <https://github.com/aiven/http-connector-for-apache-kafka/blob/main/docs/sink-connector-config-options.rst>`_.

Setup an Splunk sink connector with Aiven Console
----------------------------------------------------

The following example demonstrates how to setup an Splunk sink connector for Apache Kafka using the `Aiven Console <https://console.aiven.io/>`_.

Define a Kafka Connect configuration file
'''''''''''''''''''''''''''''''''''''''''

Create a file (we'll refer to this one as ``splunk_sink.json``) to hold the connector configuration. As an example, here's some configuration for sending JSON payloads to Splunk:

.. code-block:: json

    {
        "name":"CONNECTOR_NAME",
        "connector.class": "com.splunk.kafka.connect.SplunkSinkConnector",
        "splunk.hec.token": "SPLUNK_HEC_TOKEN",
        "splunk.hec.uri": "SPLUNK_HEC_URI",
        "splunk.indexes": "SPLUNK_INDEXES",
        "topics": "TOPIC_LIST",
        "splunk.hec.raw" : false,
        "splunk.hec.ack.enabled" : false,
        "splunk.hec.ssl.validate.certs": "false",
        "config.splunk.hec.json.event.formatted": false,
        "tasks.max":1
    }

The configuration file contains the following entries:

* ``name``: the connector name
* ``splunk.hec.token`` and ``splunk.hec.uri``: remote Splunk server URI and authorization parameters collected in the :ref:`prerequisite <connect_splunk_sink_prereq>` phase. 
* ``key.converter`` and ``value.converter``:  defines the message data format in the Apache Kafka topic. The ``io.confluent.connect.avro.AvroConverter`` converter translates messages from the Avro format. To retrieve the message schema we use Aiven's `Karapace schema registry <https://github.com/aiven/karapace>`_ as specified by the ``schema.registry.url`` parameter and related credentials.

.. Note::

    The ``key.converter`` and ``value.converter`` sections define how the topic messages will be parsed and need to be included in the connector configuration.

    When using Avro as source data format, you need to set the following parameters

    * ``value.converter.schema.registry.url``: pointing to the Aiven for Apache Kafka schema registry URL in the form of ``https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT`` with the ``APACHE_KAFKA_HOST`` and ``SCHEMA_REGISTRY_PORT`` parameters :ref:`retrieved in the previous step <connect_splunk_sink_prereq>`.
    * ``value.converter.basic.auth.credentials.source``: to the value ``USER_INFO``, since you're going to login to the schema registry using username and password.
    * ``value.converter.schema.registry.basic.auth.user.info``: passing the required schema registry credentials in the form of ``SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD`` with the ``SCHEMA_REGISTRY_USER`` and ``SCHEMA_REGISTRY_PASSWORD`` parameters :ref:`retrieved in the previous step <connect_splunk_sink_prereq>`. 


Create a Kafka Connect connector with the Aiven Console
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, access the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Apache Kafka® or Aiven for Apache Kafka Connect® service where the connector needs to be defined, then:

1. Click on the **Connectors** tab
2. Clink on **Create New Connector**. This button is only enabled for services :doc:`with Kafka Connect enabled <enable-connect>`.
3. Select the **Splunk sink**
4. Under the *Common* tab, locate the **Connector configuration** text box and click on **Edit**
5. Paste the connector configuration (stored in the ``splunk_sink.json`` file) in the form
6. Click on **Apply**

.. Note::

    The Aiven Console parses the configuration file and fills the relevant UI fields. You can review the UI fields across the various tabs and change them if necessary. The changes will be reflected in JSON format in the **Connector configuration** text box.

7. After all the settings are correctly configured, click on **Create new connector**
8. Verify the connector status under the **Connectors** tab
9. Verify the data in the target Splunk instance

.. Note::

    Connectors can also be created using the dedicated :ref:`Aiven CLI command <avn_service_connector_create>`.

Example: Create an Splunk sink connector with a server having no authorization
----------------------------------------------------------------------------

If you have a topic named ``data_logs`` that you want to sink to a Splunk server in the ``kafka_logs`` index:

.. code-block:: json

    {
        "name":"data_logs_splunk_sink",
        "connector.class": "com.splunk.kafka.connect.SplunkSinkConnector",
        "splunk.hec.token": "SPLUNK_HEC_TOKEN",
        "splunk.hec.uri": "SPLUNK_HEC_URI",
        "splunk.indexes": "kafka_logs",
        "topics": "data_logs"
    }

The configuration file contains the following things to note:

* ``"topics": "data_logs"``: setting the topic to sink

