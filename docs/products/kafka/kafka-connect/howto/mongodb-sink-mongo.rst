Create a MongoDB sink connector by MongoDB
==========================================

The MongoDB sink connector enables you to move data from an Aiven for Apache Kafka® cluster to a MongoDB database. 

.. Note::

    Aiven offers two distinct MongoDB sink connectors, each one having different implementation and parameters:
    
    * The standard `MongoDB sink connector by MongoDB <https://docs.mongodb.com/kafka-connector/current/>`_ 
    * The `MongoDB sink connector by Lenses.io <https://docs.lenses.io/connectors/sink/mongo.html>`_ enabling KCQL transformations on the topic data before sending it to the MongoDB database.

    This document refers to the MongoDB sink connector by MongoDB, you can browse the Lenses.io implementation in the :doc:`related document <mongodb-sink-lenses>`

.. _connect_mongodb_sink_prereq:

Prerequisites
-------------

To setup a MongoDB sink connector, you need an Aiven for Apache Kafka service :doc:`with Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`.

Furthermore you need to collect the following information about the target MongoDB database upfront:

* ``MONGODB_USERNAME``: The database username to connect
* ``MONGODB_PASSWORD``: The password for the username selected
* ``MONGODB_HOST``: the MongoDB hostname
* ``MONGODB_PORT``: the MongoDB port
* ``MONGODB_DATABASE_NAME``: The name of the MongoDB database
* ``TOPIC_LIST``: The list of topics to sink divided by comma
* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PORT``: The Apache Kafka's schema registry port, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_USER``: The Apache Kafka's schema registry username, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PASSWORD``: The Apache Kafka's schema registry user password, only needed when using Avro as data format


.. Note::

    The Apache Kafka related details are available in the `Aiven console <https://console.aiven.io/>`_ service *Overview tab* or via the dedicated ``avn service get`` command with the :ref:`Aiven CLI <avn_service_get>`.

    The ``SCHEMA_REGISTRY`` related parameters are available in the Aiven for Apache Kafka® service page, *Overview* tab, and *Schema Registry* subtab

    As of version 3.0, Aiven for Apache Kafka no longer supports Confluent Schema Registry. For more information, read `the article describing the replacement, Karapace <https://help.aiven.io/en/articles/5651983>`_

Setup a MongoDB sink connector with Aiven Console
----------------------------------------------------

The following example demonstrates how to setup a MongoDB sink connector for Apache Kafka using the `Aiven Console <https://console.aiven.io/>`_.

Define a Kafka Connect configuration file
'''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``mongodb_sink.json``) with the following content, creating a file is not strictly necessary but allows to have all the information in one place before copy/pasting them in the `Aiven Console <https://console.aiven.io/>`_:

.. code-block:: json

    {
        "name":"CONNECTOR_NAME",
        "connector.class": "com.mongodb.kafka.connect.MongoSinkConnector",
        "topics": "TOPIC_LIST",
        "connection.uri": "MONGODB_CONNECTION_URI",
        "database": "MONGODB_DATABASE_NAME",
        "tasks.max": "NR_TASKS",
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
* ``connection.uri``: sink parameters collected in the :ref:`prerequisite <connect_mongodb_sink_prereq>` phase. 
* ``tasks.max``: maximum number of tasks to execute in parallel. The maximum is 1 per topic and partition. Replace ``NR_TASKS`` with the amount of parallel task needed.

* ``key.converter`` and ``value.converter``:  defines the messages data format in the Apache Kafka topic. The ``io.confluent.connect.avro.AvroConverter`` converter translates messages from the Avro format. To retrieve the messages schema we use Aiven's `Karapace schema registry <https://github.com/aiven/karapace>`_ as specified by the ``schema.registry.url`` parameter and related credentials.

.. Note::

    The ``key.converter`` and ``value.converter`` sections define how the topic messages will be parsed and needs to be included in the connector configuration. 

    When using Avro as source data format, you need to set following parameters

    * ``value.converter.schema.registry.url``: pointing to the Aiven for Apache Kafka schema registry URL in the form of ``https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT`` with the ``APACHE_KAFKA_HOST`` and ``SCHEMA_REGISTRY_PORT`` parameters :ref:`retrieved in the previous step <connect_mongodb_sink_prereq>`.
    * ``value.converter.basic.auth.credentials.source``: to the value ``USER_INFO``, since you're going to login to the schema registry using username and password.
    * ``value.converter.schema.registry.basic.auth.user.info``: passing the required schema registry credentials in the form of ``SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD`` with the ``SCHEMA_REGISTRY_USER`` and ``SCHEMA_REGISTRY_PASSWORD`` parameters :ref:`retrieved in the previous step <connect_mongodb_sink_prereq>`. 


Create a Kafka Connect connector with the Aiven Console
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, access the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Apache Kafka® or Aiven for Apache Kafka Connect® service where the connector needs to be defined, then:

1. Click on the **Connectors** tab
2. Clink on **Create New Connector**, the button is enabled only for services :doc:`with Kafka Connect enabled <enable-connect>`.
3. Select the **MongoDB Kafka Sink Connector**
4. Under the *Common* tab, locate the **Connector configuration** text box and click on **Edit**
5. Paste the connector configuration (stored in the ``mongodb_sink.json`` file) in the form
6. Click on **Apply**

.. Note::

    The Aiven Console parses the configuration file and fills the relevant UI fields. You can review the UI fields across the various tab and change them if necessary. The changes will be reflected in JSON format in the **Connector configuration** text box.

7. After all the settings are correctly configured, click on **Create new connector**
8. Verify the connector status under the **Connectors** tab
9. Verify the presence of the data in the target MongoDB service, the index name is equal to the Apache Kafka topic name

.. Note::

    Connectors can be created also using the dedicated :ref:`Aiven CLI command <avn_service_connector_create>`.

Example: Create a MongoDB sink connector
----------------------------------------

If you have a topic named ``students`` containing the following data:

.. code-block:: json

    key: 1       value: {"name":"carlo"}
    key: 2       value: {"name":"lucy"}
    key: 3       value: {"name":"mary"}

You can sink the ``students`` topic to MongoDB with the following connector configuration, after replacing the placeholders for ``MONGODB_HOST``, ``MONGODB_PORT``, ``MONGODB_DB_NAME``, ``MONGODB_USERNAME`` and ``MONGODB_PASSWORD``:

.. code-block:: json

    {
        "name": "my-mongodb-sink",
        "connector.class": "com.mongodb.kafka.connect.MongoSinkConnector",
        "connection.uri": "mongodb://MONGODB_USERNAME:MONGODB_PASSWORD@MONGODB_HOST:MONGODB_PORT",
        "topics": "students",
        "tasks.max": "1",
        "database": "MONGODB_DB_NAME"
    }

The configuration file contains the following peculiarities:

* ``"topics": "students"``: setting the topic to sink
* ``"database": "MONGODB_DB_NAME"``: the database used is the one referenced by the placeholder ``MONGODB_DB_NAME``
* ``"tasks.max": "1"``: the maximum amount of parallel tasks is 1, this can vary depending on the amount of topics and partitions

Once the connector is created successfully, you should see a collection named ``students`` in the MongoDB database referenced by the ``MONGODB_DB_NAME`` placeholder.