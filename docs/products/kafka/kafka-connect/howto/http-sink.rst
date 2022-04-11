Create an HTTP sink connector
=============================

The HTTP sink connector enables you to move data from an Aiven for Apache Kafka® cluster to a remote server via HTTP. The full list of parameters and setup details is available in the `dedicated GitHub repository <https://github.com/aiven/http-connector-for-apache-kafka/>`_.


.. _connect_http_sink_prereq:

Prerequisites
-------------

To setup an HTTP sink connector, you need an Aiven for Apache Kafka service :doc:`with Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`.

Furthermore you need to collect the following information about the target server:

* ``SERVER_URL``: The remote server URL that will be called via POST method
* ``SERVER_AUTHORIZATION_TYPE``: The HTTP authorization type, supported types are ``none``, ``oauth2`` and ``static``
* ``TOPIC_LIST``: The list of topics to sink divided by comma

and, if you are using Avro as the data format:

* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service
* ``SCHEMA_REGISTRY_PORT``: The Apache Kafka's schema registry port
* ``SCHEMA_REGISTRY_USER``: The Apache Kafka's schema registry username
* ``SCHEMA_REGISTRY_PASSWORD``: The Apache Kafka's schema registry user password

.. Note::

    You can browse the additional parameters available for the ``static`` and ``oauth2`` authorization types in the `dedicated documentation <https://github.com/aiven/http-connector-for-apache-kafka/blob/main/docs/sink-connector-config-options.rst>`_.

Setup an HTTP sink connector with Aiven Console
----------------------------------------------------

The following example demonstrates how to setup an HTTP sink connector for Apache Kafka using the `Aiven Console <https://console.aiven.io/>`_.

Define a Kafka Connect configuration file
'''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``http_sink.json``) with the following content:

.. code-block:: json

    {
        "name":"CONNECTOR_NAME",
        "connector.class": "io.aiven.kafka.connect.http.HttpSinkConnector",
        "topics": "TOPIC_LIST",
        "http.url": "SERVER_URL",
        "http.authorization.type": "SERVER_AUTHORIZATION_TYPE",
        "key.converter": "org.apache.kafka.connect.storage.StringConverter",
        "value.converter": "org.apache.kafka.connect.storage.StringConverter"
    }

The configuration file contains the following entries:

* ``name``: the connector name
* ``http.url`` and ``http.authorization.type``: remote server URL and authorization parameters collected in the :ref:`prerequisite <connect_http_sink_prereq>` phase. 
* ``key.converter`` and ``value.converter``:  defines the message data format in the Apache Kafka topic. The ``io.confluent.connect.avro.AvroConverter`` converter translates messages from the Avro format. To retrieve the message schema we use Aiven's `Karapace schema registry <https://github.com/aiven/karapace>`_ as specified by the ``schema.registry.url`` parameter and related credentials.

.. Note::

    The ``key.converter`` and ``value.converter`` sections define how the topic messages will be parsed and need to be included in the connector configuration.

    When using Avro as source data format, you need to set the following parameters

    * ``value.converter.schema.registry.url``: pointing to the Aiven for Apache Kafka schema registry URL in the form of ``https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT`` with the ``APACHE_KAFKA_HOST`` and ``SCHEMA_REGISTRY_PORT`` parameters :ref:`retrieved in the previous step <connect_http_sink_prereq>`.
    * ``value.converter.basic.auth.credentials.source``: to the value ``USER_INFO``, since you're going to login to the schema registry using username and password.
    * ``value.converter.schema.registry.basic.auth.user.info``: passing the required schema registry credentials in the form of ``SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD`` with the ``SCHEMA_REGISTRY_USER`` and ``SCHEMA_REGISTRY_PASSWORD`` parameters :ref:`retrieved in the previous step <connect_http_sink_prereq>`. 


Create a Kafka Connect connector with the Aiven Console
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, access the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Apache Kafka® or Aiven for Apache Kafka Connect® service where the connector needs to be defined, then:

1. Click on the **Connectors** tab
2. Clink on **Create New Connector**. This button is only enabled for services :doc:`with Kafka Connect enabled <enable-connect>`.
3. Select the **HTTP sink**
4. Under the *Common* tab, locate the **Connector configuration** text box and click on **Edit**
5. Paste the connector configuration (stored in the ``http_sink.json`` file) in the form
6. Click on **Apply**

.. Note::

    The Aiven Console parses the configuration file and fills the relevant UI fields. You can review the UI fields across the various tabs and change them if necessary. The changes will be reflected in JSON format in the **Connector configuration** text box.

7. After all the settings are correctly configured, click on **Create new connector**
8. Verify the connector status under the **Connectors** tab
9. Verify the flow of HTTP POST calls in the target server

.. Note::

    Connectors can also be created using the dedicated :ref:`Aiven CLI command <avn_service_connector_create>`.

Example: Create an HTTP sink connector with a server having no authorization
----------------------------------------------------------------------------

If you have a topic named ``iot_measurements`` containing the following data in JSON format:

.. code-block::

    Key: 1 Value: {"iot_id":1, "metric":"Temperature", "measurement":14}
    Key: 2 Value: {"iot_id":2, "metric":"Humidity", "measurement":60}
    Key: 1 Value: {"iot_id":1, "metric":"Temperature", "measurement":16}

You can sink the ``iot_measurements`` topic to a remote server over HTTP with the following connector configuration, after replacing the placeholders for ``SERVER_URL``, and ``SERVER_AUTHORIZATION_TYPE``:

.. code-block:: json

    {
        "name":"iot_measurements_sink",
        "connector.class": "io.aiven.kafka.connect.http.HttpSinkConnector",
        "topics": "iot_measurements",
        "http.url": "SERVER_URL",
        "http.authorization.type": "SERVER_AUTHORIZATION_TYPE",
        "key.converter": "org.apache.kafka.connect.storage.StringConverter",
        "value.converter": "org.apache.kafka.connect.storage.StringConverter"
    }

The configuration file contains the following things to note:

* ``"topics": "iot_measurements"``: setting the topic to sink
* ``"value.converter": "org.apache.kafka.connect.json.StringConverter"``: the message value and key are in plain JSON format without a schema, therefore we can just pass them as plain string via HTTP

