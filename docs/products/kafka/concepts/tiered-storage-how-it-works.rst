How tiered storage works in Aiven for Apache Kafka®
===================================================

.. important:: 
  
  Aiven for Apache Kafka® tiered storage is an :doc:`early availability feature </docs/platform/concepts/beta_services>`. If you're interested in trying out this feature, contact the sales team at sales@Aiven.io.

Aiven for Apache Kafka® tiered storage is a feature that optimizes data management across two distinct storage tiers:

* **Local tier**: Primarily consists of faster and typically more expensive storage solutions like solid-state drives (SSDs).
* **Remote tier**: Relies on slower, cost-effective options like cloud object storage.

In Aiven for Apache Kafka's tiered storage architecture, **remote storage** refers to storage options external to the Kafka broker's local disk. This typically includes cloud-based or self-hosted object storage solutions like AWS S3 and Google Cloud Storage. Although network-attached block storage solutions like AWS EBS are technically external to the Kafka broker, Apache Kafka considers them local storage within its tiered storage architecture.

Tiered storage operates in a way that is seamless for both Apache Kafka producers and consumers. This means that producers and consumers interact with Apache Kafka in the same way, regardless of whether tiered storage is enabled or not. 

Administrators can configure tiered storage per topic by defining the retention period and retention bytes to specify how much data should be retained on the local disk instead of remote storage.


Local vs. remote data retention
---------------------------------
When tiered storage is enabled, data produced to a topic is initially stored on the local disk of the Kafka broker. Data is then asynchronously transferred to remote storage based on the pre-defined local retention threshold. During periods of high data ingestion or transient errors, such as network connectivity issues, the local storage might temporarily hold more data than specified by the local retention threshold.

.. image:: /images/products/kafka/tiered-storage/data-retention.png
  :alt: Diagram depicting the concept of local vs. remote data retention in a tiered storage system.

Segment management
-------------------
Data is organized into segments, which are uploaded to remote storage individually. The active (newest) segment remains in local storage, which means that the segment size can also influence local data retention. For instance, if the local retention threshold is 1 GB, but the segment size is 2 GB, the local storage will exceed the 1 GB limit until the active segment is rolled over and uploaded to remote storage.


Asynchronous uploads and replication
--------------------------------------
Data is transferred to remote storage asynchronously and does not interfere with the producer activity. While the Kafka broker aims to move data as swiftly as possible, certain conditions, such as high ingestion rate or connectivity issues, may cause more data to be stored in the local storage than the specified local retention policy.

Any data exceeding the local retention threshold will not be purged by the log cleaner until it is successfully uploaded to remote storage.
The replication factor is not considered during the upload process, and only one copy of each segment is uploaded to the remote storage. Most remote storage options have their own measures, including data replication, to ensure data durability.


Data retrieval
-----------------
When consumers fetch records stored in remote storage, the Kafka broker downloads and caches these records locally. This allows for quicker access in subsequent retrieval operations.

Aiven allocates a small amount of disk space, ranging from 2GB to 16GB, equivalent to 5% of the Kafka broker's total available disk, for the temporary storage of fetched records.

Security
--------
Segments are encrypted with 256-bit AES encryption before being uploaded to the remote storage. The encryption keys are not shared with the cloud storage provider and generally do not leave Aiven management machines and the Kafka brokers.




Related pages
----------------

* :doc:`Tiered storage in Aiven for Apache Kafka® overview </docs/products/kafka/concepts/kafka-tiered-storage>`
* :doc:`Guarantees </docs/products/kafka/concepts/tiered-storage-guarantees>`
* :doc:`Limitations </docs/products/kafka/concepts/tiered-storage-limitations>`
* :doc:`Enabled tiered storage for Aiven for Apache Kafka® service </docs/products/kafka/howto/enable-kafka-tiered-storage>`


