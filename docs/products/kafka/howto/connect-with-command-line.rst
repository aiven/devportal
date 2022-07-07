Connect to Aiven for Apache Kafka® with command line tools
==========================================================

These examples show how to connect to an Aiven for Apache Kafka® command line clients.

Pre-requisites
--------------

Follow `Apache Kafka documentation <https://kafka.apache.org/downloads>`_ to set up ``kafka-console-producer`` and ``kafka-console-consumer``. For ``kafka-avro-console-producer`` follow the instructions in `its GitHub repository <https://github.com/confluentinc/schema-registry>`_.

Create the keystore ``client.keystore.p12`` and truststore ``client.truststore.jks`` by following  :doc:`our article on configuring Java SSL to access Kafka <../howto/keystore-truststore>`.

.. Warning::

  In the below examples, we just pass the name of the certificate files, but in actual use, the full path should be used.

Variables
---------

========================     =======================================================================================================
Variable                     Description
========================     =======================================================================================================
``HOST``                     Host name for the Kafka service
``PORT``                     Port number to use for the Kafka service
``KEYSTORE_LOCATION``        Location of you keystore (named by default as client.keystore.p12)
``KEYSTORE_PASSWORD``        Password you used when creating a keystore
``KEY_PASSWORD``             Password for the key in the keystore, if you chose a different password than the one for keystore
``TRUSTSTORE_LOCATION``      Location of your truststore (named by default as client.truststore.jks)
``TRUSTSTORE_PASSWORD``      Password you used when creating a truststore
``CONFIGURATION_PATH``       Path to your configuration file with security protocol details.
``SCHEMA_REGISTRY_HOST``     Host name for your schema registry
``SCHEMA_REGISTRY_PORT``     Port number for your schema registry
``SCHEMA_REGISTRY_USER``     User name for your schema registry
``SCHEMA_REGISTRY_PWD``      Password for your schema registry
========================     =======================================================================================================

Create configuration file
-------------------------

Both producer and consumer will need to securely connect to the Apache Kafka service. Put your connection properties into a configuration file:

.. code::

   security.protocol=SSL
   ssl.protocol=TLS
   ssl.key.password={KEY_PASSWORD}
   ssl.keystore.location={KEYSTORE_LOCATION}
   ssl.keystore.password={KEYSTORE_PASSWORD}
   ssl.keystore.type=PKCS12
   ssl.truststore.location={TRUSTSTORE_LOCATION}
   ssl.truststore.password={TRUSTSTORE_PASSWORD}
   ssl.truststore.type=JKS


Produce messages
-----------------

With ``kafka-console-producer`` you can send multiple messages into your topic.

.. code::

    kafka-console-producer --broker-list {HOST}:{PORT} \
    --topic target-topic \
    --producer.config {CONFIGURATION_PATH}

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

Consume messages
-----------------

With ``kafka-console-consumer`` you can read messages from your topic. For example, run the command below to start reading from the beginning of the topic.

.. code::

    kafka-console-consumer --bootstrap-server {HOST}:{PORT} \
    --topic target-topic  \
    --consumer.config {CONFIGURATION_PATH} \
    --from-beginning
