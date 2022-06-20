Connect to Aiven for Apache Kafka® with Java
=============================================

These examples show how to connect to an Aiven for Apache Kafka® service using the Java client library for Apache Kafka.

.. note::

    The examples in this article provide two different options for authentication: SSL and SASL-SSL. For more information on these  authentication methods read :doc:`our article on Kafka authentication types <../concepts/auth-types>`.


Pre-requisites
---------------
Add a dependency for `kafka-clients` from your preferred artifact repository, for example `Maven <https://mvnrepository.com/artifact/org.apache.kafka>`_ into your Java project.

Go to the *Overview* page of your Aiven for Apache Kafka service.

* If you are going to connect with SSL authentication:

  * In the *Connection information* section:

    #. If **Authentication Method** is shown, choose **Client Certificate**
    #. Next to *Access Key*, click **Download** and save the ``service.key`` file.
    #. Next to *Access Certificate*, click **Download** and save the ``service.cert`` file.
    #. Next to *CA Certificate*, click **Download** and save the ``ca.pem`` file.

* If you are going to connect using SASL authentication:

  #. Follow the instructions at `Use SASL Authentication with Apache Kafka® <https://developer.aiven.io/docs/products/kafka/howto/kafka-sasl-auth.html>`_ to enable SASL.

  #. In the *Connection Information* section

     #. Select **SASL** as the **Authentication Method**
     #. Next to *CA Certificate*, click **Download** and save the ``ca.pem`` file
     #. Note the *Password* required for the SASL, we'll need it for authentication

* Created the keystore ``client.keystore.p12`` and truststore ``client.truststore.jks`` by following  :doc:`our article on configuring Java SSL to access Kafka <../howto/keystore-truststore>`

.. Warning::

  In the below examples, we just pass the name of the keystore and truststore files, but in actual use, the full path should be used.

Variables
---------

========================     =======================================================================================================
Variable                     Description
========================     =======================================================================================================
``HOST``                     Host name for the connection
``USER_NAME``                Name of the user for the connection
``SSL_PORT``                 Port number to use for SSL
``SASL_PORT``                Port number to use for SASL
``SASL_PASSWORD``            Password required to connect using SASL
``TRUSTSTORE_LOCATION``      Location of your truststore (named by default as client.truststore.jks)
``TRUSTSTORE_PASSWORD``      Password you used when creating a truststore
``TRUSTSTORE_PASSWORD``      Password you used when creating a truststore
``KEYSTORE_LOCATION``        Location of you keystore (named by default as client.keystore.p12)
``KEYSTORE_PASSWORD``        Password you used when creating a keystore
``KEY_PASSWORD``             Password for the key in the keystore, if you chose a different password than the one for keystore
``SERIALIZER``               How to serialize data, you can find available options  `in the Apache Kafka documentation <https://kafka.apache.org/0102/javadoc/org/apache/kafka/common/serialization/>`_.
``DESERIALIZER``             How to deserialize data, you can find available options  `in the Apache Kafka documentation <https://kafka.apache.org/0102/javadoc/org/apache/kafka/common/serialization/>`_.
========================     =======================================================================================================



With SSL authentication
-----------------------

Set up properties to connect to the cluster and create a producer and a consumer:

.. code::

     Properties properties = new Properties();
     properties.put("bootstrap.servers", "{HOST}:{SSL_PORT}");
     properties.put("security.protocol", "SSL");
     properties.put("ssl.truststore.location", "{TRUSTSTORE_LOCATION}");
     properties.put("ssl.truststore.password", "{TRUSTSTORE_PASSWORD}");
     properties.put("ssl.keystore.type", "PKCS12");
     properties.put("ssl.keystore.location", "{KEYSTORE_LOCATION}");
     properties.put("ssl.keystore.password", "{KEYSTORE_PASSWORD}");
     properties.put("ssl.key.password", "{KEY_PASSWORD}");
     properties.put("key.serializer", "{SERIALIZER}");
     properties.put("value.serializer", {SERIALIZER}");
     properties.put("key.deserializer", "{DESERIALIZER}");
     properties.put("value.deserializer", {DESERIALIZER}");

     // create a producer
     KafkaProducer<String, String> producer = new KafkaProducer<>(properties);
     // create a consumer
     KafkaConsumer<String, String> consumer = new KafkaConsumer<>(properties);

With SASL-SSL authentication
-----------------------------

Set up properties to connect to the cluster and create a producer and a consumer:

.. code::

    Properties properties = new Properties();

    String sasl_username = "{USER_NAME}";
    String sasl_password = "{SASL_PASSWORD}";

    String jaasTemplate = "org.apache.kafka.common.security.scram.ScramLoginModule required username=\"%s\" password=\"%s\";";
    String jaasConfig = String.format(jaasTemplate, sasl_username, sasl_password);

    properties.put("bootstrap.servers", "{HOST}:{SASL_PORT}");
    properties.put("security.protocol", "SASL_SSL");
    properties.put("sasl.mechanism", "SCRAM-SHA-256");
    properties.put("sasl.jaas.config", jaasConfig);
    properties.put("ssl.endpoint.identification.algorithm", "");

    properties.put("ssl.truststore.type", "jks");
    properties.put("ssl.truststore.location", "{TRUSTSTORE_LOCATION}");
    properties.put("ssl.truststore.password", "{TRUSTSTORE_PASSWORD}");

    properties.put("key.serializer", "{SERIALIZER}");
    properties.put("value.serializer", {SERIALIZER}");
     properties.put("key.deserializer", "{DESERIALIZER}");
     properties.put("value.deserializer", {DESERIALIZER}");

    // create a producer
    KafkaProducer<String, String> producer = new KafkaProducer<>(properties);
    // create a consumer
    KafkaConsumer<String, String> consumer = new KafkaConsumer<>(properties);
