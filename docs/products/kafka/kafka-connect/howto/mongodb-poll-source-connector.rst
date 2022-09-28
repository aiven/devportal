Create a MongoDB source connector
=================================

The MongoDB source connector periodically queries MongoDB collections and copies the new documents to Apache Kafka® where they can be transformed and read by multiple consumers.

.. Tip::

    The query bases approach used by this MongoDB source connector periodically pulls the new changes from a collection. The polling interval can be set as a parameter. For a log based change data capture please check the Debezium source connector for MongoDB.

.. _connect_mongodb_pull_source_prereq:

Prerequisites
-------------

To set up a MongoDB source connector, you need an Aiven for Apache Kafka service :doc:`with Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`. 

.. Tip::

  The connector will write to a topic named ``DATABASE.COLLECTION`` so either create the topic in your Kafka service, or enable the ``auto_create_topic`` parameter so that the topic will be created automatically.

Furthermore you need to collect the following information about the source MongoDB database upfront:

* ``MONGODB_CONNECTION_URI``: The MongoDB database connection URL in the format ``mongodb://USERNAME:PASSWORD@HOST:PORT`` where:

  * ``USERNAME``: The database username to connect
  * ``PASSWORD``: The password for the username selected
  * ``HOST``: the MongoDB hostname
  * ``PORT``: the MongoDB port

* ``MONGODB_DATABASE_NAME``: The name of the MongoDB database
* ``MONGODB_COLLECTION_NAME``: The name of the MongoDB collection

The complete list of parameters and customization options is available in the `MongoDB dedicated documentation <https://docs.mongodb.com/kafka-connector/current/>`_.

Setup a MongoDB source connector with Aiven Console
-------------------------------------------------------

The following example demonstrates how to setup an Apache Kafka MongoDB source connector using the `Aiven Console <https://console.aiven.io/>`_.

Define a Kafka Connect configuration file
'''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``mongodb_source.json``) with the following content, creating a file is not strictly necessary but allows to have all the information in one place before copy/pasting them in the `Aiven Console <https://console.aiven.io/>`_:

::

    {
        "name":"CONNECTOR_NAME",
        "connector.class": "com.mongodb.kafka.connect.MongoSourceConnector",
        "connection.uri": "MONGODB_CONNECTION_URI",
        "database": "MONGODB_DATABASE_NAME",
        "collection": "MONGODB_COLLECTION_NAME",
        "poll.await.time.ms": "POLL_INTERVAL",
        "output.format.value": "VALUE_OUTPUT_FORMAT",
        "output.format.key": "KEY_OUTPUT_FORMAT",
        "publish.full.document.only": "true"
    }

The configuration file contains the following entries:

* ``name``: the connector name, replace ``CONNECTOR_NAME`` with the name you want to use for the connector.
* ``connection.uri``, ``database``, ``collection``: source database parameters collected in the :ref:`prerequisite <connect_mongodb_pull_source_prereq>` phase. 
* ``poll.await.time.ms``: polling period, time between two queries to the collection, default 5000 milliseconds.
* ``output.format.value`` and ``output.format.key``: the output format of the data produced by the connector for the key/value. Supported formats are: 
    
  * ``json``: Raw JSON strings 
  * ``bson``: Binary JavaScript Object Notation byte array
  * ``schema``: Avro schema output, using this option an additional parameter (``output.schema.key`` or ``output.schema.value``) needs to be passed defining the documents schema

* ``publish.full.document.only``: only publishes the actual document rather than the full change stream document including additional metadata. Defaults to ``false``.


Check out the `dedicated documentation <https://docs.mongodb.com/kafka-connector/current/>`_ for the full list of parameters.

Create a Kafka Connect connector with the Aiven Console
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, access the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Apache Kafka® or Aiven for Apache Kafka Connect® service where the connector needs to be defined, then:

1. Click on the **Connectors** tab
2. Clink on **Create New Connector**, the button is enabled only for services :doc:`with Kafka Connect enabled <enable-connect>`.
3. Select the **MongoDB Kafka Source Connector**
4. Under the *Common* tab, locate the **Connector configuration** text box and click on **Edit**
5. Paste the connector configuration (stored in the ``mongodb_source.json`` file) in the form
6. Click on **Apply**

.. Note::

    The Aiven Console parses the configuration file and fills the relevant UI fields. You can review the UI fields across the various tab and change them if necessary. The changes will be reflected in JSON format in the **Connector configuration** text box.

7. After all the settings are correctly configured, click on **Create new connector**
8. Verify the connector status under the **Connectors** tab
9. Verify the presence of the data in the target Apache Kafka topic, the topic name is equal to the concatenation of MongoDB database and collection names

.. Note::

    Connectors can be created also using the dedicated :ref:`Aiven CLI command <avn_service_connector_create>`.

Example: Create a MongoDB source connector
------------------------------------------

If you have in MongoDB a collection named ``students`` in a database named ``districtA`` containing the following data that you want to move to Apache Kafka:

.. code-block:: json

    {"name":"carlo", "age": 77}
    {"name":"lucy", "age": 55}
    {"name":"carlo", "age": 33}

You can create a source connector taking the ``students`` MongoDB collection to Apache Kafka with the following connector configuration, after replacing the placeholders for ``MONGODB_HOST``, ``MONGODB_PORT``, ``MONGODB_DB_NAME``, ``MONGODB_USERNAME`` and ``MONGODB_PASSWORD``:

.. code-block:: json

    {
        "name": "my-mongodb-source",
        "connector.class": "com.mongodb.kafka.connect.MongoSourceConnector",
        "connection.uri": "mongodb://MONGODB_USERNAME:MONGODB_PASSWORD@MONGODB_HOST:MONGODB_PORT",
        "database": "MONGODB_DB_NAME",
        "collection": "students",
        "output.format.key": "json",
        "output.format.value": "json",
        "output.schema.infer.value": "true",
        "poll.await.time.ms": "1000"   
    }

The configuration file contains the following peculiarities:

* ``"collection": "students"``: setting the collection to source.
* ``"database": "MONGODB_DB_NAME"``: the database used is the one referenced by the placeholder ``MONGODB_DB_NAME``.
* ``"output.format.key"`` and ``"output.format.value"``: are both set to produce messages in JSON format.
* ``"output.schema.infer.value": "true"``: the schema is automatically inferred.
* ``"poll.await.time.ms": "1000"``: One second polling time

Once the connector is created successfully, you should see a topic named ``MONGODB_DB_NAME.students`` in Aiven for Apache Kafka.