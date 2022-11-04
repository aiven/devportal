Connect to Aiven for Apache Kafka® with NodeJS
==============================================

These examples show how to connect to an Aiven for Apache Kafka® service using the `node-rdkafka <https://github.com/blizzard/node-rdkafka>`_ library.

Pre-requisites
---------------

#. Install `node-rdkafka <https://github.com/blizzard/node-rdkafka>`_. Make sure that you have OpenSSL set up on your machine.

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

Note that the *CA Certificate* ``ca.pem`` file has the same contents by either route.

.. Warning::

  In the below examples, we just pass the name of the certificate files, but in actual use, the full path should be used.

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
``SASL_MECHANISM``           Supported SASL mechanisms are PLAIN, SCRAM-SHA-256, SCRAM-SHA-512
``CONSUMER_GROUP``           Consumer group to read the data
========================     =======================================================================================================

Replace the variables above in the code examples below.


Connect a producer
------------------

Add the ``producer.produce()`` command with the details of the message to produce.

.. tip:: The consumer example expects the messages to be in a topic named ``demo-topic``,

With SSL authentication
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: js

    const Kafka = require('node-rdkafka');
    console.log(Kafka.features); // this should print 'ssl', among other things

    const producer = new Kafka.Producer({
        'metadata.broker.list': HOST:SSL_PORT,
        'security.protocol': 'ssl',
        'ssl.key.location': 'service.key',
        'ssl.certificate.location': 'service.cert',
        'ssl.ca.location': 'ca.pem',
        'dr_cb': true
    });

    producer.connect();

    producer.on('ready', () => {
        // produce the messages and disconnect
    });

With SASL authentication
~~~~~~~~~~~~~~~~~~~~~~~~~

If you prefer to authenticate with SASL, the setup looks slightly different.

.. code:: js

    const Kafka = require('node-rdkafka');
    console.log(Kafka.features); // this should print 'sasl_ssl', among other things

    const producer = new Kafka.Producer({
        'metadata.broker.list': HOST:SASL_PORT,
        'security.protocol': 'sasl_ssl',
        'sasl.mechanism': SASL_MECHANISM,
        'sasl.username': USER_NAME,
        'sasl.password': SASL_PASSWORD,
        'ssl.ca.location': 'ca.pem',
        'dr_cb': true
    });

    producer.connect();

    producer.on('ready', () => {
      // produce the messages and disconnect
    });

Connect a consumer
------------------

The consumer will consume new messages sent to the topics listed. To see your consumer in action, run the producer as well, and try using ``console.log`` to inspect the message that is received.

With SSL authentication
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: js

    const Kafka = require('node-rdkafka');

    const stream = new Kafka.createReadStream({
        'metadata.broker.list': HOST:SSL_PORT,
        'group.id': CONSUMER_GROUP,
        'security.protocol': 'ssl',
        'ssl.key.location': 'service.key',
        'ssl.certificate.location': 'service.cert',
        'ssl.ca.location': 'ca.pem'
    }, {}, {'topics': ['demo-topic']});

    stream.on('data', (message) => {
        // process message
    });

With SASL authentication
~~~~~~~~~~~~~~~~~~~~~~~~~

If you prefer to authenticate with SASL, the setup looks slightly different.

.. code:: js

    const Kafka = require('node-rdkafka');

    const stream = new Kafka.createReadStream({
        'metadata.broker.list': HOST:SASL_PORT,
        'group.id': CONSUMER_GROUP,
        'security.protocol': 'sasl_ssl',
        'sasl.mechanism': SASL_MECHANISM,
        'sasl.username': USER_NAME,
        'sasl.password': SASL_PASSWORD,
        'ssl.ca.location': 'ca.pem'
    }, {}, {'topics': ['demo-topic']});

    stream.on('data', (message) => {
        // process message
    });