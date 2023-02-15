Tutorial: Let's talk to Kafka. How to send and receive application data from Apache Kafka®?
==============================================================================================

.. Note::

    This tutorial assumes basic knowledge on Apache Kafka.

Learning objectives
--------------------

- Basic overview of Apache Kafka and creating a highly available Apache Kafka service
- The concept of topic, partition, producer, consumer, and consumer groups 
- The need for data serialization in Kafka and use of Apache Avro™ to produce and consume messages

Overview
--------

Getting started with Apache Kafka can be simple as you download the binary and start the bootstrap server. However, getting a production-ready Kafka cluster stand up with security and high-availability is a different story. 
If your goal is to use Kafka to benefit your application or data needs and NOT to learn Kafka administration, you can consider using `a managed Kafka service <https://aiven.io/kafka>`_.

In this tutorial, we will learn how to create a highly available Apache Kafka service, go over the common tasks of producing and consuming messages, and finally use the popular Apache Avro specification to communicate with your Kafka service. 
This tutorial will use Python programming language.
Under the hood, the Python library will make use of the `Producer API <https://kafka.apache.org/documentation>`_ and the `Consumer API <https://kafka.apache.org/documentation>`_.

Prerequisites
-------------

To get started, you'll need:

- A Kafka service - either local or managed 
- `Python installed <https://www.python.org/downloads/>`_
- `Kafka-python <https://github.com/dpkp/kafka-python>`_ library installed, you can install it with the following command:

  .. code:: bash

    pip install kafka-python

- `confluent-kafka <https://github.com/confluentinc/confluent-kafka-python>`_ library installed, you can install it with the following command:  

  .. code:: bash

    pip install confluent-kafka

If you already have a Kafka service, jump to :ref:`tutorial-kaka-python-create-a-topic` section. 

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

.. _tutorial-kaka-python-create-a-topic:

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

.. mermaid::

    graph TD

        A(Topic) -- Partition 3 --> D[/Consumer 3/]
        A(Topic) -- Partition 4 --> E[/Consumer 4/]
        subgraph Consumer Group 2
        D
        E
        end

        A(Topic) -- Partition 1 --> B[/Consumer 1/]
        A(Topic) -- Partition 2 --> C[/Consumer 2/]
        subgraph Consumer Group 1
        B
        C
        end

In the above diagram, there are four consumers that are subscribed to a topic. ``Consumer 1`` and ``Consumer 2`` are part of ``Consumer Group 1`` and the other two consumers are part of ``Consumer Group 2``. Each consumer is assigned to a partition (``Consumer 1`` to ``Partition 1`` and so on). 
Now imagine a producer publishing messages to this topic. Messages within each partition are read in order but they are read in parallel across partitions. 
Consumers read data in consumer groups and each consumer within a group reads from exclusive partitions. From this diagram, consumers within ``Consumer Group 1`` reads from ``Partition 1`` and ``Partition 2`` whereas consumers within ``Consumer Group 2`` reads from the other two partitions.
A message will never be read by more than one customer in the group thanks to the consumer group concept.

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

Once messages are produced, they are written to the single partition ``p0`` of ``demo-topic``. All the messages will be consumed by the single consumer ``co0`` which is part of the single consumer group `consumer group A`. 

Once you run one of the above consumer program ``python consumer.py``, you'll see the program running in the terminal but not doing anything!
That's because the consumer instance is listening for messages and currently, there's no message to print out. 
To see some action on this terminal, run the producer code in another terminal. You will see the same record appear on the producer program terminal.

What would happen if there were two partitions in this case, ``p0`` and ``p1``? In this case, messages would be published to partition randomly. The consumer ``co0`` would take a round robin approach when consuming messages from this topic.

1 topic : 1 partition : 2 consumers : 1 consumer group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's take a look at this setup where there are two consumers. ``co0`` and ``co1`` are registered to the same `consumer group A`. 

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

If the first consumer ``co0`` crashes for some reason, the other consumer ``co1`` in the consumer group will begin consuming messages from the last committed offset of the partition. 

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

Apache Avro™ to produce and consume messages
---------------------------------------------

The Kafka brokers understand data as stream of bytes so one needs to pick a serializer and deserializer to convert the bytes into meaningful messages. 
Any format would do as long as it's consistent. For this tutorial, we're selecting Apache Avro which is an open-source project and one of the most popular serialization format.
Avro is defined by a schema and the schema is written in JSON. You can consider Avro as JSON with a schema attached to it.

Setting up a consumer to listen to Avro messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here's an example of a Kafka consumer in Python using the `confluent-kafka-python <https://github.com/confluentinc/confluent-kafka-python>`_ library to consume Avro-encoded messages.
On a terminal window, run one of the following consumer code. You won't see anything happening yet since there's no message to consume yet. 
Keep the program running and you'll create the producer program in the next section.

With SSL authentication:

.. code:: python

    from confluent_kafka.avro import AvroConsumer
    from confluent_kafka.avro.serializer import SerializerError
    import ssl

    # Kafka broker and schema registry URLs
    broker_url = "kafka-broker-url:9093"
    schema_registry_url = "https://schema-registry-url:443"

    # SSL configuration
    ssl_context = ssl.create_default_context()
    ssl_context.load_cert_chain("client.pem", keyfile="client.key", password="password")
    ssl_context.load_verify_locations("ca.pem")

    # Avro schema for message
    schema_str = """
    {
        "namespace": "example.avro",
        "type": "record",
        "name": "Message",
        "fields": [
            {"name": "id", "type": "int"},
            {"name": "text", "type": "string"}
        ]
    }
    """

    # Create AvroConsumer configuration
    avro_consumer_config = {
        "bootstrap.servers": broker_url,
        "schema.registry.url": schema_registry_url,
        "security.protocol": "SSL",
        "ssl.ca.location": "ca.pem",
        "ssl.key.location": "client.key",
        "ssl.certificate.location": "client.pem",
        "key.deserializer": "io.confluent.kafka.serializers.KafkaAvroDeserializer",
        "value.deserializer": "io.confluent.kafka.serializers.KafkaAvroDeserializer",
        "schema.registry.ssl.ca.location": "ca.pem",
        "schema.registry.ssl.certificate.location": "client.pem",
        "schema.registry.ssl.key.location": "client.key",
        "schema.registry.ssl.key.password": "password",
        "group.id": "example-group",
        "auto.offset.reset": "earliest"
    }

    # Create AvroConsumer instance
    avro_consumer = AvroConsumer(avro_consumer_config)

    # Subscribe to topic
    avro_consumer.subscribe(["example-topic"])

    # Consume messages from Kafka
    while True:
        msg = avro_consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print("Reached end of partition")
        else:
            print("Error while consuming message:", msg.error())
    else:
        try:
            # Deserialize message value
            message = msg.value()

            # Process message
            print(f"Received message with id {message['id']} and text {message['text']}")
        except SerializerError as e:
            print("Message deserialization failed:", e)

With SASL authentication:

.. code:: python

    from confluent_kafka.avro import AvroConsumer
    from confluent_kafka.avro.serializer import SerializerError

    # Kafka broker and schema registry URLs
    broker_url = "kafka-broker-url:9092"
    schema_registry_url = "https://schema-registry-url:443"

    # SASL authentication configuration
    sasl_username = "username"
    sasl_password = "password"
    sasl_mechanism = "PLAIN"

    # Avro schema for message
    schema_str = """
    {
        "namespace": "example.avro",
        "type": "record",
        "name": "Message",
        "fields": [
            {"name": "id", "type": "int"},
            {"name": "text", "type": "string"}
        ]
    }
    """

    # Create AvroConsumer configuration
    avro_consumer_config = {
        "bootstrap.servers": broker_url,
        "schema.registry.url": schema_registry_url,
        "security.protocol": "SASL_PLAINTEXT",
        "sasl.mechanisms": sasl_mechanism,
        "sasl.username": sasl_username,
        "sasl.password": sasl_password,
        "key.deserializer": "io.confluent.kafka.serializers.KafkaAvroDeserializer",
        "value.deserializer": "io.confluent.kafka.serializers.KafkaAvroDeserializer",
        "schema.registry.ssl.ca.location": "ca.pem",
        "schema.registry.ssl.certificate.location": "client.pem",
        "schema.registry.ssl.key.location": "client.key",
        "schema.registry.ssl.key.password": "password",
        "group.id": "example-group",
        "auto.offset.reset": "earliest"
    }

    # Create AvroConsumer instance
    avro_consumer = AvroConsumer(avro_consumer_config)

    # Subscribe to topic
    avro_consumer.subscribe(["example-topic"])

    # Consume messages from Kafka
    while True:
        msg = avro_consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print("Reached end of partition")
        else:
            print("Error while consuming message:", msg.error())
    else:
        try:
            # Deserialize message value
            message = msg.value()

            # Process message
            print(f"Received message with id {message['id']} and text {message['text']}")
        except SerializerError as e:
            print("Message deserialization failed:", e)

Setting up a producer to send Avro-encoded messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the consumer program running on a terminal, open up another terminal and run one of the following producer program.

With SSL authentication:

.. code:: python

    from confluent_kafka.avro import AvroProducer
    from confluent_kafka.avro.serializer import SerializerError
    import ssl

    # Kafka broker and schema registry URLs
    broker_url = "kafka-broker-url:9093"
    schema_registry_url = "https://schema-registry-url:443"

    # SSL configuration
    ssl_context = ssl.create_default_context()
    ssl_context.load_cert_chain("client.pem", keyfile="client.key", password="password")
    ssl_context.load_verify_locations("ca.pem")

    # Avro schema for message
    schema_str = """
    {
        "namespace": "example.avro",
        "type": "record",
        "name": "Message",
        "fields": [
            {"name": "id", "type": "int"},
            {"name": "text", "type": "string"}
        ]
    }
    """

    # Create AvroProducer configuration
    avro_producer_config = {
        "bootstrap.servers": broker_url,
        "schema.registry.url": schema_registry_url,
        "security.protocol": "SSL",
        "ssl.ca.location": "ca.pem",
        "ssl.key.location": "client.key",
        "ssl.certificate.location": "client.pem",
        "key.serializer": "io.confluent.kafka.serializers.KafkaAvroSerializer",
        "value.serializer": "io.confluent.kafka.serializers.KafkaAvroSerializer",
        "schema.registry.ssl.ca.location": "ca.pem",
        "schema.registry.ssl.certificate.location": "client.pem",
        "schema.registry.ssl.key.location": "client.key",
        "schema.registry.ssl.key.password": "password"
    }

    # Create AvroProducer instance
    avro_producer = AvroProducer(avro_producer_config, default_value_schema=schema_str)

    # Define message
    message = {"id": 1, "text": "Hello World!"}

    # Send message to Kafka
    try:
        avro_producer.produce(topic="example-topic", value=message)
    except SerializerError as e:
        print("Message serialization failed:", e)

    # Flush producer buffer
    avro_producer.flush()

With SASL authentication:

.. code:: python

    from confluent_kafka.avro import AvroProducer
    from confluent_kafka.avro.serializer import SerializerError
    import ssl

    # Kafka broker and schema registry URLs
    broker_url = "kafka-broker-url:9093"
    schema_registry_url = "https://schema-registry-url:443"

    # SASL authentication configuration
    sasl_username = "username"
    sasl_password = "password"
    sasl_mechanism = "PLAIN"

    # Avro schema for message
    schema_str = """
    {
        "namespace": "example.avro",
        "type": "record",
        "name": "Message",
        "fields": [
            {"name": "id", "type": "int"},
            {"name": "text", "type": "string"}
        ]
    }
    """

    # Create AvroProducer configuration
    avro_producer_config = {
        "bootstrap.servers": broker_url,
        "schema.registry.url": schema_registry_url,    
        "security.protocol": "SASL_PLAINTEXT",
        "sasl.mechanisms": sasl_mechanism,
        "sasl.username": sasl_username,
        "sasl.password": sasl_password,
        "key.serializer": "io.confluent.kafka.serializers.KafkaAvroSerializer",
        "value.serializer": "io.confluent.kafka.serializers.KafkaAvroSerializer",

    # Create AvroProducer instance
    avro_producer = AvroProducer(avro_producer_config, default_value_schema=schema_str)

    # Define message
    message = {"id": 1, "text": "Hello World!"}

    # Send message to Kafka
    try:
        avro_producer.produce(topic="example-topic", value=message)
    except SerializerError as e:
        print("Message serialization failed:", e)

    # Flush producer buffer
    avro_producer.flush()

Observation
~~~~~~~~~~~

In the above examples, we're using ``confluent-kafka-python`` library to send and consume Avro messages to/from a Kafka broker. Two programs for each of producer and consumer are provided for SSL protocol and SASL protocol. Here's an overview of what each program does:

Consumer program
"""""""""""""""""
The consumer program uses the ``confluent-kafka`` library to create an AvroConsumer instance and receive Avro messages from a Kafka broker. Here's a breakdown of what the program does:

- Import the necessary libraries: ``confluent_kafka``, ``confluent_kafka.avro``, and ``ssl``.
- Define the URL of the Kafka broker, the URL of the schema registry, and the Avro schema for the message.
- Set up SSL configuration by creating an SSL context and loading the client certificate, key, and CA certificate.
- Define the AvroConsumer configuration, including the SSL settings and the Avro schema.
- Create an AvroConsumer instance and subscribe to the Kafka topic.
- Consume messages from Kafka and deserialize them using the Avro schema.
- Process the messages as desired.

Producer program
""""""""""""""""""

The producer program uses the ``confluent-kafka`` library to create an AvroProducer instance and send Avro messages to a Kafka broker. Here's a breakdown of what the program does:

- Import the necessary libraries: confluent_kafka, confluent_kafka.avro, ssl, and io.
- Define the URL of the Kafka broker and the Avro schema for the message.
- Set up SSL configuration by creating an SSL context and loading the client certificate, key, and CA certificate.
- Define the AvroProducer configuration, including the SSL settings and the Avro schema.
- Create an AvroProducer instance.
- Send a sample Avro message to the Kafka broker.

Overall, these two programs demonstrate how to use Avro serialization and SSL/SASL protocols to send and receive messages to/from a Kafka broker.

Wrap up
--------

In this tutorial, we went over creating a highly available Apache Kafka service and some key Kafka concepts like topic, partition, producer, consumer, and consumer groups. 
We also learned the need for data serialization in Kafka and use of Apache Avro™ to produce and consume messages. Finally, we validated our understanding by creating multiple Python programs to send and receive messages to/from Kafka.


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