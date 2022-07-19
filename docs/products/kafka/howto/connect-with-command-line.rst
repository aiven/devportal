Connect to Aiven for Apache Kafka® with command line tools
==========================================================

These examples show how to send messages to and receive messages from an Aiven for Apache Kafka® service using command line tools.

Pre-requisites
--------------

``kafka-console-producer.sh`` and ``kafka-console-consumer.sh`` are part of the Apache Kafka® toolbox included with the `open source Apache Kafka® code <https://kafka.apache.org/downloads>`_. They may be found in the ``bin`` directory of the unpacked archive.

For ``kafka-avro-console-producer`` follow the installation instructions in `its GitHub repository <https://github.com/confluentinc/schema-registry>`_, or
get the Confluent platform using the **Tar archive** option at `Quick Start for Confluent Platform <https://docs.confluent.io/platform/current/quickstart/ce-docker-quickstart.html>`_. The ``kafka-avro-console-producer`` tool is in the ``bin`` directory of the unpacked Confluent archive.

.. note:: You do not need to install the Confluent platform to use the ``kafka-avro-console-producer`` tool with an Aiven for Apache Kafka service that is using Karapace.

To setup the configuration file needed by all three tools, follow
`the guide to set up properties to use the Apache Kafka toolbox`_.

Variables
---------

========================     ===========================================================================================
Variable                     Description
========================     ===========================================================================================
``HOST``                     Host name for the connection
``PORT``                     Port number to use for the Kafka service
``CONFIGURATION_PATH``       Path to your configuration file `for Apache Kafka toolbox`_
``SCHEMA_REGISTRY_HOST``     Host name for your schema registry
``SCHEMA_REGISTRY_PORT``     Port number for your schema registry
``SCHEMA_REGISTRY_USER``     User name for your schema registry
``SCHEMA_REGISTRY_PWD``      Password for your schema registry
``TARGET_TOPIC``             The name of the Kafka topic to be written to/read from
========================     ===========================================================================================

.. _`the guide to set up properties to use the Apache Kafka toolbox`: toolbox_
.. _`for Apache Kafka toolbox`: toolbox_
.. _toolbox: https://developer.aiven.io/docs/products/kafka/howto/kafka-tools-config-file.html

In the command lines below, values in ``{`` and ``}`` are to be replaced - so ``{PORT}`` would be replaced by the appropriate port number, for instance ``12345``.

Produce messages
-----------------

With ``kafka-console-producer`` you can send multiple messages into your topic.

.. code::

    kafka-console-producer.sh --broker-list {HOST}:{PORT} \
      --topic {TARGET_TOPIC} \
      --producer.config {CONFIGURATION_PATH}

Once the connection is successfully established you can send messages one after another by typing them in the terminal. For example:

.. code::

    message1
    message2

Produce messages with schema
----------------------------

With ``kafka-avro-console-producer`` you can include the schema by connecting to your schema registry

.. note::

   1. The ``schema.registry.url`` value must be a full URL, typically starting with ``https://``
   2. Aiven's `Karapace <https://karapace.io/>`_ is an acceptable schema registry for this purpose.
      See `Use Karapace with Aiven for Apache Kafka® <https://developer.aiven.io/docs/products/kafka/howto/enable-karapace.html>`_ for how to enable it for your Aiven for Kafka service. The ``SCHEMA_REGISTRY_`` values for the command line can be found on the service Overview page, on the **Schema registry** tab.

.. code::

    kafka-avro-console-producer --broker-list {HOST}:{PORT} \
      --producer.config {CONFIGURATION_PATH} \
      --topic {TARGET_TOPIC} \
      --property value.schema='{"type":"record","name":"Test","fields":[{"name":"id","type":"string"}]}' \
      --property schema.registry.url={SCHEMA_REGISTRY_HOST}:{SCHEMA_REGISTRY_PORT} \
      --property basic.auth.credentials.source=USER_INFO \
      --property basic.auth.user.info={SCHEMA_REGISTRY_USER}:{SCHEMA_REGISTRY_PASSWORD}

After the connection is established you can send messages according to selected schema. For example:

.. code::

    {"id": "1"}

.. note::

    For more information on how to use ``kafka-avro-console-producer`` see the `Confluent developer documentation <https://docs.confluent.io/platform/current/tutorials/examples/clients/docs/kafka-commands.html#consume-avro-records>`_.

Consume messages
-----------------

With ``kafka-console-consumer`` you can read messages from your topic. For example, run the command below to start reading from the beginning of the topic.

.. code::

    kafka-console-consumer.sh --bootstrap-server {HOST}:{PORT} \
      --topic {TARGET_TOPIC}  \
      --consumer.config {CONFIGURATION_PATH} \
      --from-beginning
