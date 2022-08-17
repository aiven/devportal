Use Apache Flink® with Aiven for Apache Kafka®
======================================================

`Apache Flink® <https://flink.apache.org/>`_ is an open source platform for processing distributed streaming and batch data.
Where Apache Kafka® excels at receiving and sending event streams, Flink consumes, transforms, aggregates, and enriches your data.

The example in this article shows you how to create a simple Java Flink job that reads data from a Kafka topic, processes it, and then pushes it to a different Kafka topic.

.. Note::

   If you want to experience the power of streaming SQL transformations with Flink, Aiven provides a managed :doc:`/docs/products/flink` with built-in data flow integration with Aiven for Apache Kafka®.

   This example demonstrates using the Java API on a `local installation of Apache Flink 1.15.1 <https://nightlies.apache.org/flink/flink-docs-release-1.15/docs/try-flink/local_installation/>`_, but it can be applied to use Aiven for Apache Kafka with any self-hosted cluster.

.. _kafka-flink-prereq:

Prerequisites
-------------

You need an Aiven for Apache Kafka service up and running with two topics, named ``test-flink-input`` and ``test-flink-output``, already `created <https://developer.aiven.io/docs/products/kafka/howto/create-topic.html>`_.
Furthermore, for the example, you need to collect the following information about the Aiven for Apache Kafka service:

* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service
* ``APACHE_KAFKA_PORT``: The port of the Apache Kafka service

You need to have `Apache Maven™ <https://maven.apache.org/install.html>`_ installed to build the example.

Setup the truststore and keystore
''''''''''''''''''''''''''''''''''

Create a :doc:`Java keystore and truststore <keystore-truststore>` for the Aiven for Apache Kafka service.
For the following example we assume:

* The keystore is available at ``KEYSTORE_PATH/client.keystore.p12``
* The truststore is available at ``TRUSTSTORE_PATH/client.truststore.jks``
* For simplicity, the same secret (password) is used for both the keystore and the truststore, and is shown here as ``KEY_TRUST_SECRET``


Use Flink with Aiven for Apache Kafka
-------------------------------------

The following example shows how to customise the ``DataStreamJob`` generated from the `Quickstart <https://nightlies.apache.org/flink/flink-docs-release-1.15/docs/dev/configuration/overview/>`_ to work with Aiven for Apache Kafka.

The full code to run this example can be found in the `Aiven examples GitHub repository <https://github.com/aiven/aiven-examples/tree/master/kafka/flink-capitalizer>`_.

1. Generate a Flink job skeleton named ``flink-capitalizer`` using the Maven archetype:

   .. code:: shell

      mvn archetype:generate -DinteractiveMode=false \
        -DarchetypeGroupId=org.apache.flink -DarchetypeArtifactId=flink-quickstart-java \
        -DarchetypeVersion=1.15.1 -DgroupId=io.aiven.example -DartifactId=flink-capitalizer \
        -Dpackage=io.aiven.example.flinkcapitalizer -Dversion=0.0.1-SNAPSHOT

2. Uncomment the Kafka connector in `pom.xml`:

   .. code:: xml

      <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-connector-kafka</artifactId>
        <version>${flink.version}</version>
      </dependency>

Customizing the ``DataStreamJob`` application
'''''''''''''''''''''''''''''''''''''''''''''

In the generated code, ``DataStreamJob`` is the main entry point, and has already been configured with all of the context necessary to interact with the cluster for your processing.

1. Create a new class called ``io.aiven.example.flinkcapitalizer.StringCapitalizer`` which performs a simple ``MapFunction`` transformation on incoming records.
   Every incoming string will be emitted as uppercase.
   
   .. code:: java
      
      package io.aiven.example.flinkcapitalizer;

      import org.apache.flink.api.common.functions.MapFunction;

      public class StringCapitalizer implements MapFunction<String, String> {
        public String map(String s) {
          return s.toUpperCase();
        }
      }

2. Import the following classes in the ``DataStreamJob``

   .. code:: java
      
      import java.util.Properties;
      import org.apache.flink.api.common.eventtime.WatermarkStrategy;
      import org.apache.flink.api.common.serialization.SimpleStringSchema;
      import org.apache.flink.connector.base.DeliveryGuarantee;
      import org.apache.flink.connector.kafka.sink.KafkaRecordSerializationSchema;
      import org.apache.flink.connector.kafka.sink.KafkaSink;
      import org.apache.flink.connector.kafka.source.KafkaSource;
      import org.apache.flink.connector.kafka.source.enumerator.initializer.OffsetsInitializer;

3. Modify the ``main`` method in ``DataStreamJob`` to read and write from the Kafka topics, replacing the ``APACHE_KAFKA_HOST``, ``APACHE_KAFKA_PORT``, ``KEYSTORE_PATH``, ``TRUSTSTORE_PATH`` and ``KEY_TRUST_SECRET`` placeholders with the values from the :ref:`prerequisites <kafka-flink-prereq>`.

   .. code:: java
      
      public static void main(String[] args) throws Exception {
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        Properties props = new Properties();
        props.put("security.protocol", "SSL");
        props.put("ssl.endpoint.identification.algorithm", "");
        props.put("ssl.truststore.location", "TRUSTSTORE_PATH/client.truststore.jks");
        props.put("ssl.truststore.password", "KEY_TRUST_SECRET");
        props.put("ssl.keystore.type", "PKCS12");
        props.put("ssl.keystore.location", "KEYSTORE_PATH/client.keystore.p12");
        props.put("ssl.keystore.password", "KEY_TRUST_SECRET");
        props.put("ssl.key.password", "KEY_TRUST_SECRET");

        KafkaSource<String> source = KafkaSource.<String>builder()
            .setBootstrapServers("APACHE_KAFKA_HOST:APACHE_KAFKA_PORT")
            .setGroupId("test-flink-input-group")
            .setTopics("test-flink-input")
            .setProperties(props)
            .setStartingOffsets(OffsetsInitializer.earliest())
            .setValueOnlyDeserializer(new SimpleStringSchema())
            .build();

        KafkaSink<String> sink = KafkaSink.<String>builder()
            .setBootstrapServers("APACHE_KAFKA_HOST:APACHE_KAFKA_PORT")
            .setKafkaProducerConfig(props)
            .setRecordSerializer(KafkaRecordSerializationSchema.builder()
                .setTopic("test-flink-output")
                .setValueSerializationSchema(new SimpleStringSchema())
                .build()
            )
            .setDeliverGuarantee(DeliveryGuarantee.AT_LEAST_ONCE)
            .build();

         // ... processing continues here
      }
   
4. Tie the Kafka sources and sinks together with the ``StringCapitalizer`` in a single processing pipeline.

   .. code:: java

      // ... processing continues here
      env
        .fromSource(source, WatermarkStrategy.noWatermarks(), "Kafka Source")
        .map(new StringCapitalizer())
        .sinkTo(sink);
      env.execute("Flink Java capitalizer");

Build the application
''''''''''''''''''''''''''''''''''''

From the main ``flink-capitalizer`` folder, execute the following Maven command to build the application:

.. code:: shell

   mvn -DskipTests=true clean package

The above command should create a ``jar`` file named ``target/flink-capitalizer-0.0.1-SNAPSHOT.jar``.

Run the applications
''''''''''''''''''''

If you have installed a `local cluster installation of Apache Flink 1.15.1 <https://nightlies.apache.org/flink/flink-docs-release-1.15/docs/try-flink/local_installation/>`_, you can launch the job on your local machine.
``$FLINK_HOME`` is the Flink installation directory.

.. code:: shell

   $FLINK_HOME/bin/flink run target/flink-capitalizer-0.0.1-SNAPSHOT.jar

You can see that the job is running in the Flink web UI at ``http://localhost:8081``.

By following the article :doc:`/docs/products/kafka/howto/connect-with-command-line`, you can send string events to the input topic and verify that the messages are forwarded to the output topic in upper case.

