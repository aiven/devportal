Avoid ``OutOfMemoryError`` errors in Aiven for Apache Kafka®
============================================================

When a node in an Aiven for Apache Kafka® or Aiven for Apache Kafka® Connect cluster runs low on memory, the Java virtual machine (JVM) running the service may not be able to allocate the memory, and will raise a ``java.lang.OutOfMemoryError`` exception.
As a result, Apache Kafka may stop processing messages in topics, and Apache Kafka Connect may be unable to manage connectors.

For example, you could have a :doc:`Kafka Connect S3 sink connector <../kafka-connect/howto/s3-sink-connector-aiven>` with a ``TimeBasedPartitioner`` that is configured to generate data directories with a ``path.format=YYYY/MM`` format.

This means that each output S3 object contains the data for a full month of the year. Internally, the connector uses a buffer in memory for each S3 object before it is flushed to AWS. If the total amount of data for any single month exceeds the amount of available RAM at the time of data ingestion, the JVM executing the Kafka Connect worker, throws a ``java.lang.OutOfMemoryError`` exception and cannot manage the workload.

How to avoid ``OutOfMemoryError`` issues
----------------------------------------

There are three options for handling heavy workloads and potentially avoiding ``java.lang.OutOfMemoryError`` exceptions:

* Decrease the maximum amount of data simultaneously kept in memory
* Increase the available memory for Kafka services or Kafka Connect workers
* Create a dedicated Kafka Connect cluster

The strategy to apply depends on a number of factors, and may combine more than one option.

Keep memory peak usage low
~~~~~~~~~~~~~~~~~~~~~~~~~~

The first option is to minimise the amount of memory needed to process the data.

.. Note::

    This approach usually requires some configuration changes in the data pipeline.

In the S3 example above, you could change the settings for the S3 sink connector to limit each S3 object to the data for one day, rather than one month, by using the data directory format ``path.format=YYYY/MM/dd``.

You could also fine tune the connector settings such as ``rotate.schedule.interval.ms``, ``rotate.interval.ms``, and ``partition.duration.ms`` and set them to smaller values enabling the connector to commit S3 objects at a higher frequency. 

All the above options will decrease peak memory usage by forcing the connector to write fewer data items to S3 at shorter intervals, allowing the JVM to release smaller memory buffers more often.

Upgrade to a larger plan
~~~~~~~~~~~~~~~~~~~~~~~~

The above approach requires configuration changes in the data pipeline. If this is not possible, the alternative is to upgrade your Aiven for Apache Kafka service to a bigger plan with more memory. You can do this in the `Aiven Console <https://console.aiven.io/>`_ or with the :ref:`Aiven CLI <avn-cli-service-update>`.

Create a dedicated Kafka Connect cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another possible scenario preventing you from handling large workloads is if you are running Kafka Connect on the same nodes as your Aiven for Apache Kafka cluster. This forces the connectors to share available memory with the Apache Kafka brokers and reduces the total amount of memory available for each connector.

If this is the case, you could separate the services and create a dedicated Aiven for Apache Kafka Connect cluster using an appropriate service plan. This separation provides the added advantage of allowing you to scale the Kafka brokers and Kafka Connect services independently.

.. Note::

    When upgrading or expanding the cluster, Aiven automatically launches new nodes and transfers the data from the old nodes to the new ones. To know more about horizontal and vertical scaling options, check the :doc:`dedicated article <../concepts/horizontal-vertical-scaling>`.
