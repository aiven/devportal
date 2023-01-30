Tutorial: Let's talk to Kafka. How to send and receive application data from Apache Kafka®?
==============================================================================================

.. Note::

    This tutorial doesn't assume any existing knowledge on Apache Kafka.

Learning objectives
--------------------

- Ease of a managed Kafka service
- How to make your app send and receive data to/from Kafka using Java?
- How to make your app send and receive data to/from Kafka using Python?

Overview
--------

Getting started with Apache Kafka can be simple as you download the binary and start the bootstrap server. However, getting a production-ready Kafka cluster stand up with security and high-availability is a different story. If your goal is to use Kafka to benefit your application or data needs and NOT to learn Kafka administration, you can consider using `a managed Kafka service <https://aiven.io/kafka>`_.
In this tutorial, we will learn how to create an Aiven for Apache Kafka® service and transfer messages to and from the broker using commonly used programming languages.

Here is how the setup looks like:

.. mermaid::

    graph LR;

        id2(kafka-python library) --producing messages-->id5(Kafka Broker);
        id3(kafka-clients java library) --producing messages-->id5(Kafka Broker);

        id5(Kafka Broker)--consuming messages-->id2(kafka-python library);
        id5(Kafka Broker)--consuming messages-->id3(kafka-clients java library);

Under the hood, the libraries make use of the `Producer API <https://kafka.apache.org/documentation/#producerapi>`_ and the `Consumer API <https://kafka.apache.org/documentation/#consumerapi>`_. 

.. Note::

    Although this tutorial covers two popular libraries for Python and Java, you can find one or more Kafka libraries for any modern programming language.

Prerequisites
-------------

While the entire tutorial can be completed using open-source Kafka, we're using Aiven for Apache Kafka® for ease and speed of setup. 

To get started, you'll need:

- `Java installed <https://www.java.com/en/download/help/download_options.html>`_
- `Python installed <https://www.python.org/downloads/>`_
- An `Aiven account <https://console.aiven.io/signup>`_


Create an Aiven for Apache Kafka® service
-----------------------------------------

To create an :doc:`Aiven for Apache Kafka </docs/products/kafka>` service, you need to:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. On the *Services* page, click **Create a new service**.

   This opens a new page with the available service options.

   .. image:: /images/platform/concepts/console_create_service.png
      :alt: Aiven Console view for creating a new service

3. Select **Apache Kafka®**.

4. Select the cloud provider and region that you want to run your service on.

5. Select `business-4` as service plan.

5. Enter ``demo-kafka`` as name for your service.

6. Click **Create Service** under the summary on the right side of the console.

The blinking blue icon besides your service name will indicate that VMs are being provisioned. Once the icon turns solid green, your Apache Kafka service is up and running.

Making a note of the connection parameters
------------------------------------------

Let's start by copying the connection information for the newly created Apache Kafka service in order to authenticate and authorize to the Kafka broker. This information will be used for both the programs we write in Java and Python.

.. image:: /images/tutorials/kafka-basics/kafka_service_overview.png
    :alt: Host, port, username, password and other 

Go to the *Overview* page of your Aiven for Apache Kafka service.

* If you are going to connect with SSL authentication:

  * In the *Connection information* section:

    #. If **Authentication Method** is shown, choose **Client Certificate**
    #. Next to *Access Key*, click **Download** and save the ``service.key`` file.
    #. Next to *Access Certificate*, click **Download** and save the ``service.cert`` file.
    #. Next to *CA Certificate*, click **Download** and save the ``ca.pem`` file.

* If you are going to connect using SASL authentication:

  #. Follow the instructions at `Use SASL Authentication with Apache Kafka® <https://docs.aiven.io/docs/products/kafka/howto/kafka-sasl-auth.html>`_ to enable SASL.

  #. In the *Connection Information* section

     #. Select **SASL** as the **Authentication Method**
     #. Next to *CA Certificate*, click **Download** and save the ``ca.pem`` file
     #. Note the *Password* required for the SASL, we'll need it for authentication

* Created the keystore ``client.keystore.p12`` and truststore ``client.truststore.jks`` by following  :doc:`our article on configuring Java SSL to access Kafka <../products/kafka/howto/keystore-truststore>`

.. Warning::

  In the below examples, we just pass the name of the keystore and truststore files, but in actual use, the full path should be used.

You can also use the `Aiven command line tool <https://docs.aiven.io/docs/tools/cli.html>`_ to download the files. See the documentation for `avn service user-creds-download <https://docs.aiven.io/docs/tools/cli/service/user.html#avn-service-user-creds-download>`_

Variables
---------

==================================  ===============================================================================================================================================================================
Variable                            Description
==================================  ===============================================================================================================================================================================
``HOST``                            Host name for the connection
``USER_NAME`` or ``SASL_USERNAME``  Name of the user for the connection
``SSL_PORT``                        Port number to use for SSL
``SASL_PORT``                       Port number to use for SASL
``SASL_PASSWORD``                   Password required to connect using SASL
``TRUSTSTORE_LOCATION``             Location of your truststore (named by default as client.truststore.jks)
``TRUSTSTORE_PASSWORD``             Password you used when creating a truststore
``KEYSTORE_LOCATION``               Location of you keystore (named by default as client.keystore.p12)
``KEYSTORE_PASSWORD``               Password you used when creating a keystore
``KEY_PASSWORD``                    Password for the key in the keystore, if you chose a different password than the one for keystore
``SERIALIZER``                      How to serialize data, you can find available options  `in the Apache Kafka documentation <https://kafka.apache.org/0102/javadoc/org/apache/kafka/common/serialization/>`_.
``DESERIALIZER``                    How to de-serialize data, you can find available options  `in the Apache Kafka documentation <https://kafka.apache.org/0102/javadoc/org/apache/kafka/common/serialization/>`_.
==================================  ===============================================================================================================================================================================

For consumers you will also need:

=================     =============================================================
Variable              Description
=================     =============================================================
``TOPIC_NAME``        The name of the topic to read from
-----------------     -------------------------------------------------------------
``START_FROM``        The value to use for the ``auto_offset_reset`` parameter,
                      which says which message to start consuming from.

                      Allowed values are:

                      * ``latest`` - consume from the end of the topic partition.
                        This is the default.
                      * ``earliest`` - consume from the beginning of the topic
                        partition
=================     =============================================================

For more information on ``auto_offset_reset``, see the Kafka documentation on
`auto.offset.reset <https://kafka.apache.org/documentation/#consumerconfigs_auto.offset.reset>`_
and
`Consumer Position <https://kafka.apache.org/documentation/#design_consumerposition>`_.

Talk to Kafka using Java
--------------------------

Connect a producer
~~~~~~~~~~~~~~~~~~

Set up properties to connect to the cluster and create a producer:

With SSL authentication
"""""""""""""""""""""""

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
        properties.put("value.serializer", "{SERIALIZER}");

        // create a producer
        KafkaProducer<String, String> producer = new KafkaProducer<>(properties);

With SASL authentication
"""""""""""""""""""""""""

.. code::    
      
        String sasl_username = "{USER_NAME}";
        String sasl_password = "{SASL_PASSWORD}";
        String jaasTemplate = "org.apache.kafka.common.security.scram.ScramLoginModule required username=\"%s\" password=\"%s\";";
        String jaasConfig = String.format(jaasTemplate, sasl_username, sasl_password);
          
        Properties properties = new Properties();
        properties.put("bootstrap.servers", "{HOST}:{SASL_PORT}");
        properties.put("security.protocol", "SASL_SSL");
        properties.put("sasl.mechanism", "SCRAM-SHA-256");
        properties.put("sasl.jaas.config", jaasConfig);
        properties.put("ssl.endpoint.identification.algorithm", ""); 
        properties.put("ssl.truststore.type", "jks");
        properties.put("ssl.truststore.location", "{TRUSTSTORE_LOCATION}");
        properties.put("ssl.truststore.password", "{TRUSTSTORE_PASSWORD}");
        properties.put("key.serializer", "{SERIALIZER}");
        properties.put("value.serializer", "{SERIALIZER}");
          
        // create a producer
        KafkaProducer<String, String> producer = new KafkaProducer<>(properties);

Connect a consumer
~~~~~~~~~~~~~~~~~~

Set up properties to connect to the cluster and create a consumer:

With SSL authentication
"""""""""""""""""""""""

.. code::

        String group_id = "groupid";

        Properties properties = new Properties();
        properties.put("bootstrap.servers", "{HOST}:{SSL_PORT}");
        properties.put("security.protocol", "SSL");
        properties.put("ssl.truststore.location", "{TRUSTSTORE_LOCATION}");
        properties.put("ssl.truststore.password", "{TRUSTSTORE_PASSWORD}");
        properties.put("ssl.keystore.type", "PKCS12");
        properties.put("ssl.keystore.location", "{KEYSTORE_LOCATION}");
        properties.put("ssl.keystore.password", "{KEYSTORE_PASSWORD}");
        properties.put("ssl.key.password", "{KEY_PASSWORD}");
        properties.put("key.deserializer", "{DESERIALIZER}");
        properties.put("value.deserializer", "{DESERIALIZER}");
        properties.put("group.id", group_id);

        // create a consumer
        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(properties);

With SASL authentication
"""""""""""""""""""""""""

.. code::

        String group_id = "groupid";
        String sasl_username = "{USER_NAME}";
        String sasl_password = "{SASL_PASSWORD}";
        String jaasTemplate = "org.apache.kafka.common.security.scram.ScramLoginModule required username=\"%s\" password=\"%s\";";
        String jaasConfig = String.format(jaasTemplate, sasl_username, sasl_password);
          
        Properties properties = new Properties();
        properties.put("bootstrap.servers", "{HOST}:{SASL_PORT}");
        properties.put("security.protocol", "SASL_SSL");
        properties.put("sasl.mechanism", "SCRAM-SHA-256");
        properties.put("sasl.jaas.config", jaasConfig);
        properties.put("ssl.endpoint.identification.algorithm", ""); 
        properties.put("ssl.truststore.type", "jks");
        properties.put("ssl.truststore.location", "{TRUSTSTORE_LOCATION}");
        properties.put("ssl.truststore.password", "{TRUSTSTORE_PASSWORD}");
        properties.put("key.deserializer", "{DESERIALIZER}");
        properties.put("value.deserializer", "{DESERIALIZER}");
        properties.put("group.id", group_id);

        // create a consumer
        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(properties);

Talk to Kafka using Python
--------------------------

Install the Python `kafka-python <https://github.com/dpkp/kafka-python>`_ library:

.. code:: bash

    pip install kafka-python

Connect a producer
------------------

With SSL authentication
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

        from kafka import KafkaProducer

        producer = KafkaProducer(
            bootstrap_servers=f"{HOST}:{SSL_PORT}",
            security_protocol="SSL",
            ssl_cafile="ca.pem",
            ssl_certfile="service.cert",
            ssl_keyfile="service.key",
        )

With SASL authentication
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

         from kafka import KafkaProducer

         # Choose an appropriate SASL mechanism, for instance:
         SASL_MECHANISM = 'SCRAM-SHA-256'

         producer = KafkaProducer(
            bootstrap_servers=f"{HOST}:{SASL_PORT}",
            sasl_mechanism = SASL_MECHANISM,
            sasl_plain_username = SASL_USERNAME,
            sasl_plain_password = SASL_PASSWORD,
            security_protocol="SASL_SSL",
            ssl_cafile="ca.pem",
         )

Connect a consumer
------------------

With SSL authentication
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

        from kafka import KafkaConsumer

        consumer = KafkaConsumer(
            "TOPIC_NAME",
            auto_offset_reset="START_FROM",
            bootstrap_servers=f"{HOST}:{SSL_PORT}",
            client_id = CONSUMER_CLIENT_ID,
            group_id = CONSUMER_GROUP_ID,
            security_protocol="SSL",
            ssl_cafile="ca.pem",
            ssl_certfile="service.cert",
            ssl_keyfile="service.key",
        )


With SASL authentication
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

        from kafka import KafkaConsumer

        # Choose an appropriate SASL mechanism, for instance:
        SASL_MECHANISM = 'SCRAM-SHA-256'

        consumer = KafkaConsumer(
            "TOPIC_NAME",
            auto_offset_reset = "START_FROM",
            bootstrap_servers = f'{HOST}:{SASL_PORT}',
            client_id = CONSUMER_CLIENT_ID,
            group_id = CONSUMER_GROUP_ID,
            sasl_mechanism = SASL_MECHANISM,
            sasl_plain_username = SASL_USERNAME,
            sasl_plain_password = SASL_PASSWORD,
            security_protocol = "SASL_SSL",
            ssl_cafile = "ca.pem"
        )

Next steps
-----------

Check out :doc:`more Aiven tutorials <../>` to learn about open-source data infrastructure. 