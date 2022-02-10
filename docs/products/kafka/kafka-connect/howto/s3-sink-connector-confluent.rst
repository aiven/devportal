Create an S3 sink connector by Confluent
========================================

The Apache Kafka Connect® S3 sink connector by Aiven enables you to move data from an Aiven for Apache Kafka® cluster to Amazon S3 for long term storage.

.. Note::

    There are two versions of S3 sink connector available with Aiven for Apache Kafka Connect®: One is developed by Aiven, another developed by Confluent. This article uses the Confluent version. The S3 sink connector by Aiven is discussed in a :doc:`dedicated page <s3-sink-connector-aiven>`.

Prerequisites
-------------

To setup the S3 sink connector by Confluent, you need an Aiven for Apache Kafka® service :doc:`with Apache Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`.

Furthermore you need to follow the steps :doc:`to prepare the AWS account and S3 sink <s3-sink-prereq>` and collect the following information about the target S3 bucket upfront:

* ``AWS_S3_NAME``: The name of the S3 bucket
* ``AWS_S3_REGION``: The AWS region where the S3 bucket has been created
* ``AWS_USER_ACCESS_KEY_ID``: The AWS user access key ID
* ``AWS_USER_SECRET_ACCESS_KEY``: The AWS user secret access key

Setup an S3 sink connector with Aiven CLI
-----------------------------------------

The following example demonstrates how to setup an Apache Kafka Connect® S3 sink connector using the :ref:`Aiven CLI dedicated command <avn_service_connector_create>`.

Define a Kafka Connect® configuration file
''''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``s3_sink.json``) with the following content:

::

    {
        "name": "<CONECTOR_NAME>",
        "topics": "<TOPIC_NAME>",
        "connector.class": "io.confluent.connect.s3.S3SinkConnector",
        "key.converter": "org.apache.kafka.connect.converters.ByteArrayConverter"",
        "value.converter": "org.apache.kafka.connect.converters.ByteArrayConverter",
        "format.class": "io.confluent.connect.s3.format.bytearray.ByteArrayFormat",
        "flush.size": "1",
        "s3.bucket.name": "<AWS_S3_NAME>",
        "s3.region": "<AWS_S3_REGION>",
        "s3.credentials.provider.class": "io.aiven.kafka.connect.util.AivenAWSCredentialsProvider",
        "storage.class": "io.confluent.connect.s3.storage.S3Storage",
        "s3.credentials.provider.secret_access_key": "<AWS_USER_SECRET_ACCESS_KEY>",
        "s3.credentials.provider.access_key_id": "<AWS_USER_ACCESS_KEY_ID>"
    }

The configuration file contains the following entries:

* ``name``: The connector name
* ``topics``: The list of Apache Kafka® topics to sink to the S3 bucket
* ``key.converter`` and ``value.converter``: Data converters, depending on the topic data format. Check the `related documentation <https://docs.confluent.io/5.0.0/connect/kafka-connect-s3/index.html>`_ for more information
* ``format.class``: Defines the output data format in the S3 bucket. The ``io.confluent.connect.s3.format.bytearray.ByteArrayFormat`` writes messages in binary format.
* ``flush.size``: Defines how many messages to write per file in the S3 bucket. E.g. setting ``flush.size`` to ``3`` generates a file every three messages in a topic and partition.
* ``s3.bucket.name``: The name of the S3 bucket
* ``s3.region``: The AWS region where the S3 bucket has been created
* ``s3.credentials.provider.class``: The name of the class implementing the ``com.amazonaws.auth.AWSCredentialsProvider`` and ``org.apache.kafka.common.Configurable`` interfaces. Use ``io.aiven.kafka.connect.util.AivenAWSCredentialsProvider``.
* ``s3.credentials.provider.secret_access_key``: The AWS user access key ID
* ``s3.credentials.provider.access_key_id``: The AWS user secret access key

Check out the `dedicated documentation <https://docs.confluent.io/5.0.0/connect/kafka-connect-s3/index.html>`_ for the full list of configuration options.


Create an S3 sink connector with Aiven CLI
''''''''''''''''''''''''''''''''''''''''''

To create the connector, execute the following :ref:`Aiven CLI command <avn_service_connector_create>`, replacing the ``SERVICE_NAME`` with the name of the existing Aiven for Apache Kafka® service where the connector needs to run:

:: 

    avn service connector create SERVICE_NAME @s3_sink.json

Check the connector status with the following command, replacing the ``SERVICE_NAME`` with the existing Aiven for Apache Kafka® service and the ``CONNECTOR_NAME`` with the name of the connector defined before:

::

    avn service connector status SERVICE_NAME CONNECTOR_NAME

With the connection in place, verify that the data is flowing to the target S3 bucket.


Example: define a S3 sink connector
-----------------------------------

The example creates an S3 sink connector with the following properties:

* connector name: ``my_s3_sink``
* source topics: ``students``
* target S3 bucket name: ``my-test-bucket``
* target S3 bucket region: ``eu-central-1``
* AWS user access key id: ``AKIAXXXXXXXXXX``
* AWS user secret access key: ``hELuXXXXXXXXXXXXXXXXXXXXXXXXXX``
* generating a file in the S3 bucket every 10 messages

The connector configuration is the following:

::

    {
        "name": "my_s3_sink",
        "topics": "students",
        "connector.class": "io.confluent.connect.s3.S3SinkConnector",
        "key.converter": "org.apache.kafka.connect.converters.ByteArrayConverter",
        "value.converter": "org.apache.kafka.connect.converters.ByteArrayConverter",
        "format.class": "io.confluent.connect.s3.format.bytearray.ByteArrayFormat",
        "flush.size": "10",
        "s3.bucket.name": "my-test-bucket",
        "s3.region": "eu-central-1",
        "s3.credentials.provider.class": "io.aiven.kafka.connect.util.AivenAWSCredentialsProvider",
        "storage.class": "io.confluent.connect.s3.storage.S3Storage",
        "s3.credentials.provider.secret_access_key": "hELuXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "s3.credentials.provider.access_key_id": "AKIAXXXXXXXXXX"
    }

With the above configuration stored in a ``s3_sink.json`` file, you can create the connector in the ``demo-kafka`` instance with:

::

    avn service connector create demo-kafka @s3_sink.json
