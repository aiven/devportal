S3 sink connector by Confluent naming and data formats
======================================================

The Apache Kafka Connect® S3 sink connector enables you to move data from an Aiven for Apache Kafka® cluster to Amazon S3 for long term storage. The following document describes advanced parameters defining the naming and data formats.

.. Warning::

    Aiven provides two version of S3 sink connector: one developed by Aiven, another developed by Confluent. 
    
    This article is about the **Confluent** version. Documentation for the Aiven version is available in the :doc:`dedicated page <s3-sink-additional-parameters>`.


S3 naming format
---------------- 

The Apache Kafka Connect® S3 sink connector by Confluent stores a series of files as objects in the specified S3 bucket. By default, each object is named using the pattern:

::

    topics/<TOPIC_NAME>/partition=<PARTITION_NUMBER>/<TOPIC_NAME>+<PARTITIOIN_NUMBER>+<START_OFFSET>.<FILE_EXTENSION>

The placeholders are the following:

* ``TOPIC_NAME``: Name of the topic to be pushed to S3
* ``PARTITION_NUMBER``: Topic partitions number
* ``START_OFFSET``: File starting offset
* ``FILE_EXTENSION``: The file extension depends on serialization format defined. The ``bin`` extension is generated when serializing messages in binary format.

For example, a topic with 3 partitions generates initially the following files in the destination S3 bucket:

::

    topics/<TOPIC_NAME>/partition=0/<TOPIC_NAME>+0+0000000000.bin
    topics/<TOPIC_NAME>/partition=1/<TOPIC_NAME>+1+0000000000.bin
    topics/<TOPIC_NAME>/partition=2/<TOPIC_NAME>+2+0000000000.bin

S3 data format
--------------

By default, data is stored in binary format, one line per message. The connector creates a file every ``X`` messages, where ``X`` is defined by the ``flush.size`` parameter. Setting the ``flush.size`` parameter to ``1`` generates a file for each message in a topic. 

In the above example, having a topic with 3 partitions and 10 messages, setting the ``flush.size`` parameter to 1 generates the following files (one per message) in the destination S3 bucket:

::

    topics/<TOPIC_NAME>/partition=0/<TOPIC_NAME>+0+0000000000.bin
    topics/<TOPIC_NAME>/partition=0/<TOPIC_NAME>+0+0000000001.bin
    topics/<TOPIC_NAME>/partition=0/<TOPIC_NAME>+0+0000000002.bin
    topics/<TOPIC_NAME>/partition=0/<TOPIC_NAME>+0+0000000003.bin
    topics/<TOPIC_NAME>/partition=1/<TOPIC_NAME>+1+0000000000.bin
    topics/<TOPIC_NAME>/partition=1/<TOPIC_NAME>+1+0000000001.bin
    topics/<TOPIC_NAME>/partition=1/<TOPIC_NAME>+1+0000000002.bin
    topics/<TOPIC_NAME>/partition=2/<TOPIC_NAME>+2+0000000000.bin
    topics/<TOPIC_NAME>/partition=2/<TOPIC_NAME>+2+0000000001.bin
    topics/<TOPIC_NAME>/partition=2/<TOPIC_NAME>+2+0000000002.bin

You can find additional documentation at the `dedicated page <https://docs.confluent.io/5.0.0/connect/kafka-connect-s3/index.html>`_.
