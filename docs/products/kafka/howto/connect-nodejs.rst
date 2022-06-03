Connect with NodeJS
====================

In this article you'll find code samples demonstrating how to connect to your Aiven for Apache Kafka® service with NodeJS, send a messages into the topic and pull the messages from the topic.


Prerequisites
---------------

#. Install `node-rdkafka <https://github.com/blizzard/node-rdkafka>`_. Make sure that you have OpenSSL set up on your machine.
#. Go to the *Topics* page for your service and add a new topic named ``demo-topic``.

Relying on SSL authentication
-----------------------------

1. Download the SSL certificate files in the Aiven web console.
    a. Go to the *Overview* page of your Aiven for Apache Kafka service.
    b. Click **Download** next to *Access Key* and save the ``service.key`` file.
    c. Click **Download** next to *Access Certificate* and save the ``service.cert`` file.
    d. Click **Download** next to *CA Certificate* and save the ``ca.pem`` file.
2. Create and run the producer:

   .. code:: js

      const Kafka = require('node-rdkafka');
      console.log(Kafka.features); // this should print 'ssl', among other things

      const producer = new Kafka.Producer({
          'metadata.broker.list': 'your-kafka-service.aivencloud.com:port',
          'security.protocol': 'ssl',
          'ssl.key.location': 'service.key',
          'ssl.certificate.location': 'service.cert',
          'ssl.ca.location': 'ca.pem',
          'dr_cb': true
      });

      producer.connect();

      producer.on('ready', function() {
          try {
              producer.produce(
                  'demo-topic',  // topic to send the message to
                  null,  // partition, null for librdkafka default partitioner
                  Buffer.from('Hello world!'),  // value
                  null,  // optional key
                  Date.now()  // optional timestamp
              );  
              producer.flush(2000);
              console.log('Message sent successfully');
          } catch (err) {
              console.log('Failed to send message', err);
          }   
          producer.disconnect();
      });

3. Create and run the consumer:

   .. code:: js

      const Kafka = require('node-rdkafka');

      const stream = new Kafka.createReadStream({
          'metadata.broker.list': 'your-kafka-service.aivencloud.com:port',
          'group.id': 'demo-consumer-group',
          'security.protocol': 'ssl',
          'ssl.key.location': 'service.key',
          'ssl.certificate.location': 'service.cert',
          'ssl.ca.location': 'ca.pem'
      }, {}, {'topics': ['demo-topic']});

      stream.on('data', (message) => {
        console.log('Got message');
        console.log(message.value.toString());
      });


Relying on SASL authentication
-------------------------------

1. Copy your password from the Aiven web console.
2. Create and run the producer:

.. code:: js

    const Kafka = require('node-rdkafka');
    console.log(Kafka.features); // this should print 'sasl_ssl', among other things

    const producer = new Kafka.Producer({
        'metadata.broker.list': 'getting-started-with-kafka.htn-aiven-demo.aivencloud.com:24960',
        'security.protocol': 'sasl_ssl',
        'sasl.mechanism': 'SCRAM-SHA-512', // supports: PLAIN, SCRAM-SHA-256, SCRAM-SHA-512
        'sasl.username': 'avnadmin',
        'sasl.password': 'your_password_from_step1',
        'ssl.ca.location': 'ca.pem',
        'dr_cb': true
    });

    producer.connect();

    producer.on('ready', () => {
      try {
          producer.produce(
              'demo-topic',  // topic to send the message to
              null,  // partition, null for librdkafka default partitioner
              Buffer.from('Hello world!'),  // value
              null,  // optional key
              Date.now()  // optional timestamp
          );
          producer.flush(2000);
          console.log('Message sent successfully');
      } catch (err) {
          console.log('Failed to send message', err);
      }
      producer.disconnect();
    });

3. Create the consumer:

.. code:: js

    const Kafka = require('node-rdkafka');

    const stream = new Kafka.createReadStream({
        'metadata.broker.list': 'getting-started-with-kafka.htn-aiven-demo.aivencloud.com:24960',
        'group.id': 'demo-consumer-group',
        'security.protocol': 'sasl_ssl',
        'sasl.mechanism': 'SCRAM-SHA-512', // supports: PLAIN, SCRAM-SHA-256, SCRAM-SHA-512
        'sasl.username': 'avnadmin',
        'sasl.password': 'your_password_from_step1',
        'ssl.ca.location': 'ca.pem'
    }, {}, {'topics': ['demo-topic']});

    stream.on('data', (message) => {
        console.log('Got message');
        console.log(message.value.toString());
    });
