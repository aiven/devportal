S3 sink connector by Aiven naming and data formats
==================================================

The Apache Kafka Connect® S3 sink connector by Aiven enables you to move data from an Aiven for Apache Kafka® cluster to Amazon S3 for long term storage. The following document describes advanced parameters defining the naming and data formats.

.. Warning::

    Aiven provides, as managed service, two version of S3 sink connector: one developed by Aiven, another developed by Confluent. 
    
    This article is about the **Aiven** version. Documentation for the Confluent version is available at the :doc:`dedicated page <s3-sink-additional-parameters-confluent>`.


S3 naming format
---------------- 

The Apache Kafka Connect® S3 sink connector by Aiven stores a series of files as objects in the specified S3 bucket. By default, each object is named using the pattern:

::

    <AWS_S3_PREFIX><TOPIC_NAME>-<PARTITION_NUMBER>-<START_OFFSET>.<FILE_EXTENSION>

The placeholders are the following:

* ``AWS_S3_PREFIX``: Can be any string and use placeholders like ``{{ utc_date }}`` and ``{{ local_date }}`` to create different files for each date.
* ``TOPIC_NAME``: Name of the topic to be pushed to S3
* ``PARTITION_NUMBER``: Topic partitions number
* ``START_OFFSET``: File starting offset
* ``FILE_EXTENSION``: The file extension depends on the compression defined in the ``file.compression.type`` parameter. The ``gz`` extension is generated when using the ``gzip`` compression.

.. Tip::

    You can customise the S3 object naming and how records are grouped into files, see the `documentation in GitHub on the file naming format <https://github.com/aiven/aiven-kafka-connect-s3>`_ for further details.

The Apache Kafka Connect® connector creates one file per period defined by the ``offset.flush.interval.ms``  parameter. The file is generated for every partition that has received at least one new message during the period. The setting defaults to 60 seconds.

S3 data format
--------------

By default, data is stored in one record per line in S3 in CSV format.

.. Tip::

    You can change the output data format to JSON or `Parquet <https://parquet.apache.org/documentation/latest/>`_ by setting the ``format.output.type``. More details can be found in the `GitHub connector repository documentation <https://github.com/aiven/aiven-kafka-connect-s3>`_

You can define the output data fields with the ``format.output.fields`` connector configuration. The message key and value, if included in the output, are encoded in ``Base64``. 

For example, setting ``format.output.fields`` to ``value,key,timestamp`` results in rows in the S3 files like the following:

::

    bWVzc2FnZV9jb250ZW50,cGFydGl0aW9uX2tleQ==,1511801218777 

.. Tip::

    You can disable the `Base64` encoding by setting the ``format.output.fields.value.encoding`` to ``none``
