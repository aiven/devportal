Java samples for testing Aiven for Apache Kafka®
=================================================

The sample Java code in this article demonstrates how to connect to your Aiven for Apache Kafka service and send messages into a topic.

.. note::

    The examples in this article provide two different options for authentication: SSL and SASL-SSL. For more information on these  authentication methods read :doc:`our article on Kafka authentication types <../concepts/auth-types>`.

.. note::

    The instructions below assume that there is existing topic with name ``demo-topic`` and that you have created the keystore ``client.keystore.p12`` and truststore ``client.truststore.jks``. For details, see :doc:`our article on configuring Java SSL to access Kafka <../howto/keystore-truststore>`.

Relying on SSL authentication
-----------------------------

Create and run a producer, that sends a message into the topic ``demo-topic``:

.. code::

         package io.aiven.kafkaExample;
         import java.io.IOException;
         import java.util.Properties;
         import org.apache.kafka.clients.producer.KafkaProducer;
         import org.apache.kafka.clients.producer.ProducerRecord;

         public class Producer {
             public static void main(String[] args) throws IOException {
                 Properties props = new Properties();
                 props.put("bootstrap.servers", "service-uri.aivencloud.com:port");
                 props.put("security.protocol", "SSL");
                 props.put("ssl.truststore.location", "client.truststore.jks");
                 props.put("ssl.truststore.password", "secret");
                 props.put("ssl.keystore.type", "PKCS12");
                 props.put("ssl.keystore.location", "client.keystore.p12");
                 props.put("ssl.keystore.password", "secret");
                 props.put("ssl.key.password", "secret");
                 props.put("key.serializer",
                     "org.apache.kafka.common.serialization.StringSerializer");
                 props.put("value.serializer",
                     "org.apache.kafka.common.serialization.StringSerializer");
                 KafkaProducer<String, String> producer = new KafkaProducer<>(props);
                 producer.send(new ProducerRecord<String, String>("demo-topic", "test-message"));
                 producer.close();
             }
         }

Create and run a consumer that pulls and outputs the data from ``demo-topic``:

.. code::

         import java.io.IOException;
         import java.util.Arrays;
         import java.util.Properties;
         import org.apache.kafka.clients.consumer.ConsumerRecord;
         import org.apache.kafka.clients.consumer.ConsumerRecords;
         import org.apache.kafka.clients.consumer.KafkaConsumer;

         public class Consumer {
             public static void main(String[] args) throws IOException {
                 Properties props = new Properties();
                 props.put("bootstrap.servers", "service-uri.aivencloud.com:port");
                 props.put("security.protocol", "SSL");
                 props.put("ssl.truststore.location", "client.truststore.jks");
                 props.put("ssl.truststore.password", "secret");
                 props.put("ssl.keystore.type", "PKCS12");
                 props.put("ssl.keystore.location", "client.keystore.p12");
                 props.put("ssl.keystore.password", "secret");
                 props.put("ssl.key.password", "secret");
                 props.put("group.id", "demo-group");
                 props.put("key.deserializer",
                   "org.apache.kafka.common.serialization.StringDeserializer");
                 props.put("value.deserializer",
                   "org.apache.kafka.common.serialization.StringDeserializer");
                 KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
                 consumer.subscribe(Arrays.asList("demo-topic"));
                 while (true) {
                     ConsumerRecords<String, String> records = consumer.poll(1000);
                     for (ConsumerRecord<String, String> record : records) {
                         System.out.printf("offset = %d, key = %s, value = %s",
                             record.offset(), record.key(), record.value());
                     }
                 }
             }
         }

Relying on SASL-SSL authentication
-----------------------------------

If you want to use SASL authentication, turn on **kafka_authentication_methods.sasl** under *Advanced configuration* on the *Overview* page of your service.

Create and run a producer, that sends a message into the topic ``demo-topic``:

.. code::

         package io.aiven.kafkaExample;
         import java.io.IOException;
         import java.util.Properties;
         import org.apache.kafka.clients.producer.KafkaProducer;
         import org.apache.kafka.clients.producer.ProducerRecord;

         public class Producer {
         public static void main(String[] args) throws IOException {
             Properties props = new Properties();

             String sasl_username = "avnadmin";
             String sasl_password = "<avnadmin-pw>";

             String jaasTemplate = "org.apache.kafka.common.security.scram.ScramLoginModule required username=\"%s\" password=\"%s\";";
             String jaasConfig = String.format(jaasTemplate, sasl_username, sasl_password);

             props.put("bootstrap.servers", "service-uri.aivencloud.com:<SASL_PORT>");
             props.put("security.protocol", "SASL_SSL");
             props.put("sasl.mechanism", "SCRAM-SHA-256");
             props.put("sasl.jaas.config", jaasConfig);
             props.put("ssl.endpoint.identification.algorithm", "");

             props.put("ssl.truststore.type", "jks");
                     props.put("ssl.truststore.location", "client.truststore.jks");
                     props.put("ssl.truststore.password", "secret");

                     props.put("key.serializer",
                       "org.apache.kafka.common.serialization.StringSerializer");
                     props.put("value.serializer",
                         "org.apache.kafka.common.serialization.StringSerializer");

                     KafkaProducer<String, String> producer = new KafkaProducer<>(props);
                     producer.send(new ProducerRecord<String, String>("demo-topic", "test-message"));
                     producer.close();
                 }
         }

Create and run a consumer that pulls and outputs the data from ``demo-topic``:

.. code::

         import java.io.IOException;
         import java.util.Arrays;
         import java.util.Properties;
         import org.apache.kafka.clients.consumer.ConsumerRecord;
         import org.apache.kafka.clients.consumer.ConsumerRecords;
         import org.apache.kafka.clients.consumer.KafkaConsumer;

         public class Consumer {
             public static void main(String[] args) throws IOException {
                 Properties props = new Properties();

                 String sasl_username = "avnadmin";
                 String sasl_password = "<avnadmin-pw>";

                 String jaasTemplate = "org.apache.kafka.common.security.scram.ScramLoginModule required username=\"%s\" password=\"%s\";";
                 String jaasConfig = String.format(jaasTemplate, sasl_username, sasl_password);

                 props.put("bootstrap.servers", "service-uri.aivencloud.com:<SASL_PORT>");
                 props.put("security.protocol", "SASL_SSL");
                 props.put("sasl.mechanism", "SCRAM-SHA-256");
                 props.put("sasl.jaas.config", jaasConfig);

                 props.put("ssl.truststore.type", "jks");
                 props.put("ssl.truststore.location", "client.truststore.jks");
                 props.put("ssl.truststore.password", "secret");

                 props.put("group.id", "demo-group");
                 props.put("key.deserializer",
                   "org.apache.kafka.common.serialization.StringDeserializer");
                 props.put("value.deserializer",
                   "org.apache.kafka.common.serialization.StringDeserializer");
                 KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
                 consumer.subscribe(Arrays.asList("demo-topic"));
                 while (true) {
                     ConsumerRecords<String, String> records = consumer.poll(1000);
                     for (ConsumerRecord<String, String> record : records) {
                         System.out.printf("offset = %d, key = %s, value = %s",
                             record.offset(), record.key(), record.value());
                     }
                 }
             }
         }
