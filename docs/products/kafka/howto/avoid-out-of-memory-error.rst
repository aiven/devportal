Avoid ``OutOfMemoryError`` errors in Aiven for Apache Kafka®
============================================================

When a node in a Aiven for Apache Kafka® or Aiven for Apache Kafka Connect cluster runs low on memory and cannot allocate more RAM for the execution, the related Java virtual machine (JVM) raises a ``java.lang.OutOfMemoryError`` exception. As a result, the JVM may stop processing Apache Kafka messages in topics or manage connectors.

.. Note::

    For example, you could have a :doc:`Kafka Connect S3 sink connector <../kafka-connect/howto/s3-sink-connector-aiven>` with a ``TimeBasedPartitioner`` that is configured to generate data directories with a ``path.format=YYYY/MM`` format. 
    
    Therefore, each output S3 object contains the data for a full month of the year. Internally, the connector uses a buffer in memory for each S3 object before it is flushed to AWS. If the total amount of data for any single month exceeds the amount of available RAM at the time of data ingestion, the JVM executing the Kafka Connect worker throws a ``java.lang.OutOfMemoryError`` exception and cannot manage the workload.

The reason for such the ``java.lang.OutOfMemoryError`` exception is that the Apache Kafka node or Kafka Connect worker is running on a machine that does not have enough free RAM available for the given data processing tasks.

How to avoid ``OutOfMemoryError`` issues
----------------------------------------

There are three options for handling heavy workloads and potentially avoid ``java.lang.OutOfMemoryError`` exceptions: 

* Decrease the maximum amount of data simultaneously kept in memory
* Increase the available memory for Kafka services or Kafka Connect workers
* Create a dedicated Kafka Connect cluster

The strategy to apply depends on a number of factors, and potentially combine of both options.

Keep memory peak usage low
~~~~~~~~~~~~~~~~~~~~~~~~~~

The first option is to minimise the amount of used memory needed to process the data. 

.. Note::

    This approach usually requires some configuration changes in the data pipeline.

In the S3 example above, you could change the settings for the S3 sink connector and use a different data directory format, like ``path.format=YYYY/MM/dd`` that would limit the maximum amount of data used in any S3 object to a single day worth of data rather than a month.

You could also fine tune the connector settings such as ``rotate.schedule.interval.ms``, ``rotate.interval.ms``, and ``partition.duration.ms``, and set them to smaller values enabling the connector to commit S3 objects at a higher frequency. 

All the above options will decreases peak memory usage by forcing the connector to write fewer data items to S3 at shorter intervals, while the JVM would release smaller memory buffers more often.

Upgrade to a larger plan
~~~~~~~~~~~~~~~~~~~~~~~~

The above approach requires configuration changes in the data pipeline. If this is not possible, the alternative is to upgrade your Aiven for Apache Kafka service to a bigger plan with more memory. You can do this in the `Aiven Console <https://console.aiven.io/>`_ or with the :ref:`Aiven CLI <avn-cli-service-update>`.

Create a dedicated Kafka Connect cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A possible scenario preventing you from handling large workloads is when runing Kafka Connect on the same nodes of your Aiven for Apache Kafka cluster. This setting forces the connectors to share available memory with the Apache Kafka brokers and reduces the total amount of memory available for each connector. 
    
If this is the case, you could separate the services and create a dedicated Aiven for Apache Kafka Connect cluster using an appropriate service plan. This separation provides the added advantage of allowing you to scale the Kafka brokers and Kafka Connect services independently.

.. Note::

    When upgrading or expanding the cluster, Aiven automatically launches new nodes and transfers the data from the old nodes to the new ones. To know more about horizontal and vertical scaling options, check the :doc:`dedicated article <../concepts/horizontal-vertical-scaling>`.