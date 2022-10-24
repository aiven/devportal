Create an InfluxDB® sink connector
==================================

The InfluxDB® sink connector enables you to move data from an Aiven for Apache Kafka® cluster to an InfluxDB instance for further processing and analysis.

.. note::

    You can check the full set of available parameters and configuration options in the `connector's documentation <https://docs.lenses.io/connectors/sink/influx.html>`_.

.. _connect_influxdb_lenses_sink_prereq:

Prerequisites
-------------

To setup a InfluxDB sink connector, you need an Aiven for Apache Kafka service :doc:`with Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`.

Furthermore you need to collect the following information about the target influxdb database upfront:

* ``INFLUXDB_USERNAME``: The database username to connect
* ``INFLUXDB_PASSWORD``: The password for the username selected
* ``INFLUXDB_HOST``: the influxdb hostname
* ``INFLUXDB_PORT``: the influxdb port
* ``INFLUXDB_DATABASE_NAME``: The name of the influxdb database
* ``TOPIC_LIST``: The list of topics to sink divided by comma
* ``KCQL_TRANSFORMATION``: The KCQL syntax to parse the topic data, should be in the format

  ::

    INSERT
    INTO INFLUXDB_COLLECTION_NAME
    SELECT LIST_OF_FIELDS 
    FROM APACHE_KAFKA_TOPIC


* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PORT``: The Apache Kafka's schema registry port, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_USER``: The Apache Kafka's schema registry username, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PASSWORD``: The Apache Kafka's schema registry user password, only needed when using Avro as data format


.. Note::

    The Apache Kafka related details are available in the `Aiven console <https://console.aiven.io/>`_ service *Overview tab* or via the dedicated ``avn service get`` command with the :ref:`Aiven CLI <avn_service_get>`.

    The ``SCHEMA_REGISTRY`` related parameters are available in the Aiven for Apache Kafka® service page, *Overview* tab, and *Schema Registry* subtab

    As of version 3.0, Aiven for Apache Kafka no longer supports Confluent Schema Registry. For more information, read `the article describing the replacement, Karapace <https://help.aiven.io/en/articles/5651983>`_

Setup a influxdb sink connector with Aiven Console
----------------------------------------------------

The following example demonstrates how to setup a influxdb sink connector for Apache Kafka using the `Aiven Console <https://console.aiven.io/>`_.

Define a Kafka Connect configuration file
'''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``influxdb_sink.json``) with the following content, creating a file is not strictly necessary but allows to have all the information in one place before copy/pasting them in the `Aiven Console <https://console.aiven.io/>`_:

.. code-block:: json

    {
        "name":"CONNECTOR_NAME",
        "connector.class": "com.datamountaineer.streamreactor.connect.influx.InfluxSinkConnector",
        "topics": "TOPIC_LIST",
        "connect.influx.url": "https://INFLUXDB_HOST:INFLUXDB_PORT",
        "connect.influx.db": "INFLUXDB_DATABASE_NAME",
        "connect.influx.username": "INFLUXDB_USERNAME",
        "connect.influx.password": "INFLUXDB_PASSWORD",
        "connect.influx.kcql": "KCQL_TRANSFORMATION",
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

* ``name``: the connector name, replace ``CONNECTOR_NAME`` with the name you want to use for the connector.
* ``connect.influx.connection``: sink parameters collected in the :ref:`prerequisite <connect_influxdb_lenses_sink_prereq>` phase. 

* ``key.converter`` and ``value.converter``:  defines the messages data format in the Apache Kafka topic. The ``io.confluent.connect.avro.AvroConverter`` converter translates messages from the Avro format. To retrieve the messages schema we use Aiven's `Karapace schema registry <https://github.com/aiven/karapace>`_ as specified by the ``schema.registry.url`` parameter and related credentials.

.. Note::

    The ``key.converter`` and ``value.converter`` sections define how the topic messages will be parsed and needs to be included in the connector configuration. 

    When using Avro as source data format, you need to set following parameters

    * ``value.converter.schema.registry.url``: pointing to the Aiven for Apache Kafka schema registry URL in the form of ``https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT`` with the ``APACHE_KAFKA_HOST`` and ``SCHEMA_REGISTRY_PORT`` parameters :ref:`retrieved in the previous step <connect_influxdb_lenses_sink_prereq>`.
    * ``value.converter.basic.auth.credentials.source``: to the value ``USER_INFO``, since you're going to login to the schema registry using username and password.
    * ``value.converter.schema.registry.basic.auth.user.info``: passing the required schema registry credentials in the form of ``SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD`` with the ``SCHEMA_REGISTRY_USER`` and ``SCHEMA_REGISTRY_PASSWORD`` parameters :ref:`retrieved in the previous step <connect_influxdb_lenses_sink_prereq>`. 


Create a Kafka Connect connector with the Aiven Console
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, access the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Apache Kafka® or Aiven for Apache Kafka Connect® service where the connector needs to be defined, then:

1. Click on the **Connectors** tab
2. Clink on **Create New Connector**, the button is enabled only for services :doc:`with Kafka Connect enabled <enable-connect>`.
3. Select the **Stream Reactor influxdb Sink**
4. Under the *Common* tab, locate the **Connector configuration** text box and click on **Edit**
5. Paste the connector configuration (stored in the ``influxdb_sink.json`` file) in the form
6. Click on **Apply**

.. Note::

    The Aiven Console parses the configuration file and fills the relevant UI fields. You can review the UI fields across the various tab and change them if necessary. The changes will be reflected in JSON format in the **Connector configuration** text box.

7. After all the settings are correctly configured, click on **Create new connector**
8. Verify the connector status under the **Connectors** tab
9. Verify the presence of the data in the target influxdb service, the index name is equal to the Apache Kafka topic name

.. Note::

    Connectors can be created also using the dedicated :ref:`Aiven CLI command <avn_service_connector_create>`.

Example: Create a InfluxDB sink connector
-----------------------------------------

If you have a topic named ``measurements`` containing the following data in AVRO format that you want to move to InfluxDB:

.. code-block::

    {
        "ts":"2022-10-24T13:09:43.406000Z"
        "device_name": "mydevice1",
        "measurement": 17
    }

You can sink the ``measurements`` topic to InfluxDB with the following connector configuration, after replacing the placeholders for ``INFLUXDB_HOST``, ``INFLUXDB_PORT``, ``INFLUXDB_DB_NAME``, ``INFLUXDB_USERNAME``, ``INFLUXDB_PASSWORD`` and schema registry:

.. code-block:: json

    {
        "name": "my-influxdb-sink",
        "connector.class": "com.datamountaineer.streamreactor.connect.influx.InfluxSinkConnector",
        "topics": "measurements",
        "connect.influx.url": "https://INFLUXDB_HOST:INFLUXDB_PORT",
        "connect.influx.db": "INFLUXDB_DATABASE_NAME",
        "connect.influx.username": "INFLUXDB_USERNAME",
        "connect.influx.password": "INFLUXDB_PASSWORD",
        "connect.mongo.kcql": "select into measurements select ts, device_name, measurement from measurements",
        "value.converter": "io.confluent.connect.avro.AvroConverter",
        "value.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "value.converter.basic.auth.credentials.source": "USER_INFO",
        "value.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD"    
    }

The configuration file contains the following peculiarities:

* ``"topics": "measurements"``: setting the topic to sink
* ``"connect.mongo.kcql": "select into measurements select ts, device_name, measurement from measurements"``: the connector logic is to insert every topic message as new document into a table called ``measurements``.

Once the connector is created successfully, you should see a table named ``measurements`` in the influxdb database referenced by the ``INFLUXDB_DB_NAME`` placeholder with the record in it.