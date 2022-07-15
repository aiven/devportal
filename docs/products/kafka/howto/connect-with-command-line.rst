Connect to Aiven for Apache Kafka® with command line tools
==========================================================

These examples show how to send messages to and receive messages from an Aiven for Apache Kafka® service using command line tools.

Pre-requisites
--------------

``kafka-console-producer`` and ``kafka-console-consumer`` are part of the Apache Kafka® toolbox included with the `open source Apache Kafka® code <https://kafka.apache.org/downloads>`_. Follow
`the guide to set up properties to use the Apache Kafka toolbox <kafka-tools-config-file.html>`_
For ``kafka-avro-console-producer`` follow the installation instructions in `its GitHub repository <https://github.com/confluentinc/schema-registry>`_.

Variables
---------

========================     ===========================================================================================
Variable                     Description
========================     ===========================================================================================
``HOST``                     Host name for the connection
``PORT``                     Port number to use for the Kafka service
``CONFIGURATION_PATH``       Path to your configuration file `for Apache Kafka toolbox <kafka-tools-config-file.html>`_.
``SCHEMA_REGISTRY_HOST``     Host name for your schema registry
``SCHEMA_REGISTRY_PORT``     Port number for your schema registry
``SCHEMA_REGISTRY_USER``     User name for your schema registry
``SCHEMA_REGISTRY_PWD``      Password for your schema registry
========================     ===========================================================================================

Produce messages
-----------------

With ``kafka-console-producer`` you can send multiple messages into your topic.

.. code::

    kafka-console-producer --broker-list {HOST}:{PORT} \
      --topic target-topic \
      --producer.config {CONFIGURATION_PATH}

Once the connection is successfully established you can send messages one after another by typing them in the terminal. For example:

.. code::

    message1
    message2

Produce messages with schema
----------------------------

With ``kafka-avro-console-producer`` you can include the schema by connecting to your schema registry

.. code::

    kafka-avro-console-producer --broker-list {HOST}:{PORT} \
      --producer.config {CONFIGURATION_PATH} \
      --topic target-topic \
      --property value.schema='{"type":"record","name":"Test","fields":[{"name":"id","type":"string"}]}' \
      --property schema.registry.url={SCHEMA_REGISTRY_HOST}:{SCHEMA_REGISTRY_PASSWORD} \
      --property basic.auth.credentials.source=USER_INFO \
      --property basic.auth.user.info={SCHEMA_REGISTRY_USER}:{SCHEMA_REGISTRY_PASSWORD}

After the connection is established you can send messages according to selected schema. For example:

.. code::

    {"id": "1"}

.. note::

    For more details how to use ``kafka-avro-console-producer`` check `Confluent developer documentation <https://docs.confluent.io/platform/current/tutorials/examples/clients/docs/kafka-commands.html#consume-avro-records>`_.

Consume messages
-----------------

With ``kafka-console-consumer`` you can read messages from your topic. For example, run the command below to start reading from the beginning of the topic.

.. code::

    kafka-console-consumer --bootstrap-server {HOST}:{PORT} \
      --topic target-topic  \
      --consumer.config {CONFIGURATION_PATH} \
      --from-beginning
