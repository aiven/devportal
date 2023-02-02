Tutorial: Let's talk to Kafka. How to send and receive application data from Apache Kafka®?
==============================================================================================

.. Note::

    This tutorial assumes basic knowledge on Apache Kafka.

Learning objectives
--------------------

- Basic overview of Apache Kafka and creating a highly available Apache Kafka service
- The concept of topic, partition, producer, consumer, and consumer groups explained by example
- The need for a schema registry and the use of Karapace to work with Apache Kafka over HTTP

Overview
--------

Getting started with Apache Kafka can be simple as you download the binary and start the bootstrap server. However, getting a production-ready Kafka cluster stand up with security and high-availability is a different story. 
If your goal is to use Kafka to benefit your application or data needs and NOT to learn Kafka administration, you can consider using `a managed Kafka service <https://aiven.io/kafka>`_.
In this tutorial, we will learn how to create a highly available Apache Kafka service, go over the common tasks of producing and consuming messages, use a schema registry to manage your schemas and metadata, and finally use REST API to communicate with your Kafka service. 
This tutorial will use Python programming language.
Under the hood, the Python library will make use of the `Producer API <https://kafka.apache.org/documentation>`_ and the `Consumer API <https://kafka.apache.org/documentation>`_.

Prerequisites
-------------

To get started, you'll need:

- A Kafka service - either local or managed 
- `Karapace <https://www.karapace.io/install>`_ installed (if you're using a local Kafka instance)
- `Python installed <https://www.python.org/downloads/>`_
- `Kafka-python <https://github.com/dpkp/kafka-python>`_ library installed

.. code:: bash

    pip install kafka-python

If you already have a Kafka service, jump to :ref:`create-a-topic`section. 

Else, `sign up for an Aiven account <https://console.aiven.io/signup>`_ and follow the tutorial to create a Kafka service on Aiven.

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

Let's start by copying the connection information for the newly created Apache Kafka service in order to authenticate and authorize to the Kafka broker. 

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

* Create the keystore ``client.keystore.p12`` and truststore ``client.truststore.jks`` by following  :doc:`our article on configuring Java SSL to access Kafka <../products/kafka/howto/keystore-truststore>`

.. Warning::

  In the below examples, we just pass the name of the keystore and truststore files, but in actual use, the full path should be used.

You can also use the `Aiven command line tool <https://docs.aiven.io/docs/tools/cli.html>`_ to download the files. See the documentation for `avn service user-creds-download <https://docs.aiven.io/docs/tools/cli/service/user.html#avn-service-user-creds-download>`_

Details on the Aiven for Apache Kafka configuration can be found under the :ref:`kafka-tutorial-reference` section.

.. _create-a-topic:

Create a topic
---------------

A topic in Kafka is a named stream of records that is stored within a Kafka cluster. Let's create a Kafka topic. 

If you have a local Kafka instance running, the command to create the topic might be something like this:

.. code:: bash

    bin/kafka-topics.sh --create --topic demo-topic --bootstrap-server localhost:9092

For an Aiven for Apache Kafka service, you can create the topic from the Aiven console. 
From the **Topics** tab or the Kafka service overview page, click **Add topic**. Give the topic a name "demo-topic". Click **Add topic**.
Once this topic is created, we can see that the number of partitions is 1. 

The concept of consumer group and consuming messages on Kafka
------------------------------------------------------------------

Consumer group is the logical grouping of consumers. In Kafka, the consumer(s) must belong to a consumer group, even if it's the default consumer group. 
For a Kafka cluster with multiple nodes, consumers within the same consumer group can exist on different nodes. 

1 topic : 1 partition : 1 consumer : 1 consumer group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's start with a setup where we have a single producer writing to a single topic with one partition. 
A consumer is reading messages from this topic which is part of a consumer group.

.. mermaid::
    
    graph LR;

        pr0(kafka producer pr0) -->p0(partition p0);
        subgraph topic
        p0
        end
        co0(kafka consumer co0)
        subgraph consumer group A
        co0
        end
        p0 -->co0

Set up a consumer instance to start listening for messages
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The following code samples include configuration related to SSL or SASL authentication. If you're running a local Kafka instance and not using SSL/SASL, you can exclude these configurations. 
Please note that excluding SSL/SASL configurations is not suggested for production Kafka environments. 

With SSL authentication:

.. code:: python

        # Import the required library
        from kafka import KafkaConsumer

        # Create the consumer instance  
        consumer = KafkaConsumer(
            "demo-topic",
            auto_offset_reset="earliest",
            bootstrap_servers=f"{HOST}:{SSL_PORT}", # From the connection information for managed service
            group_id="demo-consumer-group",
            security_protocol="SSL",
            ssl_cafile="ca.pem", # From the connection information for managed service
            ssl_certfile="service.cert", # From the connection information for managed service
            ssl_keyfile="service.key", # From the connection information for managed service
            value_deserializer=lambda m: m.decode("utf-8"),
            key_deserializer=lambda m: m.decode("utf-8"),
        )

        # Continuously poll for new messages
        for msg in consumer:
          print("Message: ", msg.value)

With SASL authentication:

.. code:: python

        # Import the required library
        from kafka import KafkaConsumer

        # Choose an appropriate SASL mechanism, for instance:
        SASL_MECHANISM = 'SCRAM-SHA-256'

        consumer = KafkaConsumer(
            "demo-topic",
            auto_offset_reset="earliest",
            bootstrap_servers = f'{HOST}:{SASL_PORT}', # From the connection information for managed service
            group_id="demo-consumer-group",
            sasl_mechanism = SASL_MECHANISM,
            sasl_plain_username = SASL_USERNAME, # From the connection information for managed service
            sasl_plain_password = SASL_PASSWORD, # From the connection information for managed service
            security_protocol = "SASL_SSL",
            ssl_cafile = "ca.pem" # From the connection information for managed service
        )

        # Continuously poll for new messages
        for msg in consumer:
          print("Message: ", msg.value)

Set up a producer instance to send a message to the cluster
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The following Python code generates some messages to the "demo-topic" topic using the `Kafka-python` library:

With SSL authentication:

.. code:: python

        from kafka import KafkaProducer
        import time

        producer = KafkaProducer(
            bootstrap_servers=f"{HOST}:{SSL_PORT}", # From the connection information for managed service
            security_protocol="SSL",
            ssl_cafile="ca.pem", # From the connection information for managed service
            ssl_certfile="service.cert", # From the connection information for managed service
            ssl_keyfile="service.key", # From the connection information for managed service
            value_serializer=lambda v: v.encode("utf-8"),
            key_serializer=lambda k: k.encode("utf-8"),
        )

        # Generate 10 messages in total with 1 second interval
        for i in range(10):
          message = f"Hello from Python using SSL {i + 1}!"
          producer.send("demo-topic", message.encode('utf-8'))
          print(f"Message sent: {message}")
          time.sleep(1)

        producer.close()

With SASL authentication:

.. code:: python

        from kafka import KafkaProducer
        import time

         # Choose an appropriate SASL mechanism, for instance:
         SASL_MECHANISM = 'SCRAM-SHA-256'

         producer = KafkaProducer(
            bootstrap_servers=f"{HOST}:{SASL_PORT}", # From the connection information for managed service
            sasl_mechanism = SASL_MECHANISM,
            sasl_plain_username = SASL_USERNAME, # From the connection information for managed service
            sasl_plain_password = SASL_PASSWORD, # From the connection information for managed service
            security_protocol="SASL_SSL", 
            ssl_cafile="ca.pem", # From the connection information for managed service
            value_serializer=lambda v: v.encode("utf-8"),
            key_serializer=lambda k: k.encode("utf-8"),
         )

        # Generate 10 messages in total with 1 second interval
        for i in range(10):
          message = f"Hello from Python using SASL {i + 1}!"
          producer.send("demo-topic", message.encode('utf-8'))
          print(f"Message sent: {message}")
          time.sleep(1)

        producer.close()

Observation
"""""""""""

You might have noticed ``key_deserializer``, ``key_serializer``, ``value_deserializer``, and ``value_serializer`` in these programs. Since Kafka brokers don't know about the records and only deal in bytes, the programs need to serialize 
and deserialize data before making sense of them. 

Once messages are produced, they are written to the single partition `p0` of `demo-topic`. All the messages will be consumed by the single consumer `co0` which is part of the single consumer group `consumer group A`. 

Once you run one of the above consumer program ``python consumer.py``, you'll see the program running in the terminal but not doing anything!
That's because the consumer instance is listening for messages and currently, there's no message to print out. 
To see some action on this terminal, run the producer code in another terminal. You will see the same record appear on the producer program terminal.

What would happen if there were two partitions in this case, `p0` and `p1`? In this case, messages would be published to partition randomly. The consumer `co0` would take a round robin approach when consuming messages from this topic.

1 topic : 1 partition : 2 consumers : 1 consumer group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's take a look at this setup where there are two consumers. `co0` and `co1` are registered to the same `consumer group A`. 

In this setup, one consumer will be sitting idle. This highlights an important concept in Kafka - records are processed in parallel and same partition cannot be assigned to multiple consumers in the same consumer group.

.. mermaid::
    
    graph LR;

        pr0(kafka producer pr0) -->p0(partition p0);
        subgraph topic
        p0
        end
        co0(kafka consumer co0)
        co1(kafka consumer co1)
        subgraph consumer group A
        co0
        co1
        end
        p0 -->co0 

If the first consumer `co0` crashes for some reason, the other consumer `co1` in the consumer group will begin consuming messages from the last committed offset of the partition. 

.. mermaid::
    
    graph LR;

        pr0(kafka producer pr0) -->p0(partition p0);
        subgraph topic
        p0
        end
        co0(CRASHED)
        co1(kafka consumer co1)
        subgraph consumer group A
        co0
        co1
        end
        p0 -->co1

Karapace schema registry
-------------------------

Karapace is an open-source project for schema registry functionality with support for JSON Schema, Avro and Protobuf data formats. 
Using a schema registry allows all components of an application to share a common data structure definition. Besides this, Karapace exposes
RESTful API endpoints for Apache Kafka so that you can work with metadata, manage topics, messages, and producer/consumer information over the API.

Enable Karapace schema registry and REST APIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a local Kafka instance, follow `Karapace installation <https://www.karapace.io/install>`_ instructions and use the `getting started <https://www.karapace.io/quickstart>`_ guide. 

For Aiven for Apache Kafka, enable **Karapace schema registry** and **REST APIs** for your ``demo-kafka`` service following these steps from the Aiven Console: 

1. In the `Aiven Console <https://console.aiven.io/>`_, click on the service to view its overview screen. 
2. Look for **Schema Registry (Karapace)** or **Apache Kafka REST API (Karapace)**, and enable the setting for either one or both of the features based on your requirements. 

**TODO section**

How to use Karapace to manage Apache Kafka over REST endpoints.

.. _kafka-tutorial-reference:

Reference
----------

Variables
~~~~~~~~~~

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


Next steps
-----------

Check out :doc:`more Aiven tutorials <../tutorials>` to learn about open-source data infrastructure. 