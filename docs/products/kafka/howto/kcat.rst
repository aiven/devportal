Use ``kcat`` with Aiven for Apache Kafka®
=========================================

The ``kcat`` `tool <https://github.com/edenhill/kcat>`__
(formerly known as ``kafkacat``) is a generic non-JVM producer and consumer for Apache Kafka®.
It can be used to produce and consume records to Apache Kafka topics as well as to list service configurations.


Install ``kcat``
----------------

``kcat`` is an open source tool available from GitHub at https://github.com/edenhill/kcat. Installation instructions are provided in the repository README.

Retrieve Aiven for Apache Kafka® SSL certificate files
------------------------------------------------------

Aiven for Apache Kafka by default enables TLS security. 
The certificates can be manually downloaded from the service overview page in the Aiven console, or via the :ref:`dedicated Aiven CLI command <avn_service_user_creds_download>`.

Setup a ``kcat`` configuration file
-----------------------------------

While ``kcat`` accepts all connection configuration parameters in the command line, using a configuration file helps minimising the code needed for any following calls.
A ``kcat`` configuration file enabling the connection to an Aiven for Apache Kafka® service with TLS security must contain the following entries:

* ``bootstrap.servers``: Aiven for Apache Kafka® service URI, that can be found in the service overview in Aiven console
* ``security.protocol``: security protocol, SSL for the default TLS security settings
* ``ssl.key.location``: location of the `service.key` file downloaded from the service overview in Aiven console
* ``ssl.certificate.location``: location of the `service.cert` file downloaded from the service overview in Aiven console
* ``ssl.ca.location``: location of the `ca.pem` file downloaded from the service overview in Aiven console

An example of the ``kcat`` configuration file is provided below:

::

   bootstrap.servers=demo-kafka.my-demo-project.aivencloud.com:17072
   security.protocol=ssl
   ssl.key.location=service.key
   ssl.certificate.location=service.cert
   ssl.ca.location=ca.pem

Once the content is stored in a file named ``kcat.config``, this can be referenced using the ``-F`` flag:

::

   kcat -F kcat.config

Alternatively, the same settings can be specified directly on the command line with:

::

   kcat \
       -b demo-kafka.my-demo-project.aivencloud.com:17072 \
       -X security.protocol=ssl \
       -X ssl.key.location=service.key \
       -X ssl.certificate.location=service.cert \
       -X ssl.ca.location=ca.pem

If :doc:`SASL authentication <kafka-sasl-auth>` is enabled, then the ``kcat`` configuration file requires the following entries:

::

   bootstrap.servers=demo-kafka.my-demo-project.aivencloud.com:17072
   ssl.ca.location=ca.pem
   security.protocol=SASL_SSL
   sasl.mechanisms=SCRAM-SHA-256
   sasl.username=avnadmin
   sasl.password=yourpassword

.. Tip::

   If you're using Aiven for Apache Kafka®, you can retrieve the ``kcat`` command parameters using the dedicated :ref:`Aiven CLI command <avn_cli_service_connection_info_kcat>`.

Produce data to an Apache Kafka® topic
--------------------------------------

Use the following code to produce a single message into topic named ``test-topic``:

::
    
    echo test-message-content | kcat -F kcat.config -P -t test-topic -k test-message-key

* ``-P``: sets the producer mode
* ``-t``: specifies the topic
* ``-k``: sets the message key

The output of the above comment is a message sent to Apache Kafka® ``test-topic`` containing ``test-message-key`` as key and ``test-message-content`` as payload.

.. Note:

    ``kcat`` can use a file as input input and specify a delimiter (``-D``) for splitting rows into individual records for bulk loading of data.

Consume data from an Apache Kafka® topic
-----------------------------------------

Use the following code to consume messages coming from a topic named ``test-topic``:

::

   kcat -F kcat.config -C -t test-topic -o -1 -e

* ``-C``: sets for consumer mode
* ``-t``: specifies the topic again 
* ``-o``: defines the topic starting message offset (negative values are considered relative to the latest offset)
* ``-e``: stops ``kcat`` once the end of the topic is reached; without it, it will continuously poll Apache Kafka for new messages.

The above command retrieves the last message (``-o -1``) from the topic named ``test-topic``. Consult the ``kcat`` helper (by adding the ``-h`` flag) for the full list of parameters.

.. Tip::

    When consuming from a topic, setting the ``-f`` flag to ``%t-%p: %o %S`` returns the topic name, partition, offset and size for each message.
