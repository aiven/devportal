
Get started with tiered storage for Aiven for Apache Kafka® 
====================================================================

Aiven for Apache Kafka®'s tiered storage expands storage beyond local disks. It stores frequently accessed data on the faster tier and less active data on cost-effective, the slower tier, ensuring both performance and cost efficiency are optimized.

For an in-depth understanding of tiered storage, how it works, and its benefits, see `Tiered Storage in Aiven for Apache Kafka®`.

.. important:: 
    
   Aiven for Apache Kafka® tiered storage is an early availability feature, which means it has some restrictions on the functionality and service level agreement. It is intended for non-production environments, but you can test it with production-like workloads to assess the performance. To enable this feature, navigate to the :doc:`Feature preview </docs/platform/howto/feature-preview>` page within your user profile.

Enable tiered storage for service
----------------------------------
To use tiered storage, you need to first :doc:`enable </docs/products/kafka/howto/enable-kafka-tiered-storage>` it for your Aiven for Apache Kafka service® service. This foundational step ensures that the necessary infrastructure is in place.

.. important:: 
    Tiered storage is supported on Aiven for Apache Kafka services with Apache Kafka version 3.6.


Configure tiered storage per topic
----------------------------------
Once the tiered storage is enabled at the service level, you can configure it for individual topics. In the Aiven for Apache Kafka Topics page, topics using tiered storage will display **Active** in the **Tiered storage** column.

For detailed instructions, see :doc:`Configuring tiered storage for topics </docs/products/kafka/howto/configure-topic-tiered-storage>`.


Tiered storage usage overview
------------------------------
Gain insights into tiered storage usage from the **Tiered Storage Overview** page in your Aiven for Apache Kafka service. This includes details on billing, settings, and specific storage aspects.

For more information, see :doc:`Tiered Storage Overview in Aiven Console </docs/products/kafka/howto/tiered-storage-overview>`.





