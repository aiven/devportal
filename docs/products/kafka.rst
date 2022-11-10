Aiven for Apache Kafka®
=======================

What is Aiven for Apache Kafka®?
--------------------------------

Aiven for Apache Kafka® is a fully managed **distributed data streaming platform**, deployable in the cloud of your choice. Apache Kafka is an open source data streaming platform, ideal for event-driven applications, near-real-time data transfer and pipelines, stream analytics, and many more applications where a lot of data needs to move between applications in a speedy manner.

Kafka stores a potentially large number of records, each contains a small amount of data, usually for a limited period of time. The storage is organised into "topics" and "partitions" so that many data streams can be handled at once, regardless of how much data is flowing into or out of your Aiven for Apache Kafka service.


Why Apache Kafka?
-----------------

Apache Kafka itself is technically a distributed log storage mechanism; in reality it is a best-in-class, highly-available data streaming solution. Oh, and it just happens to have an incredibly rich ecosystem of open source tooling that connects to and extends the existing platform.

Aiven for Apache Kafka® MirrorMaker 2
'''''''''''''''''''''''''''''''''''''

By adding Aiven for Apache Kafka MirrorMaker 2 to your setup, you gain replication superpowers. Whether you need data replication across clusters, availability zones or clouds, MirrorMaker 2 is the answer.

Aiven for Apache Kafka® Connect
'''''''''''''''''''''''''''''''

Apache Kafka moves data between systems, and Apache Kafka Connect is how to interface between Apache Kafka and the rest of your data architecture. Connectors are available for many databases, storage platforms and other common integrations.

Get started with Aiven for Apache Kafka
---------------------------------------

Take your first steps with Aiven for Apache Kafka by following our :doc:`/docs/products/kafka/getting-started` article, or browse through our full list of articles:

.. grid:: 1 2 2 2

    .. grid-item-card::
        :shadow: md
        :margin: 2 2 0 0

        📚 :doc:`Concepts </docs/products/kafka/concepts>`

    .. grid-item-card::
        :shadow: md
        :margin: 2 2 0 0

        💻 :doc:`HowTo </docs/products/kafka/howto>`

    .. grid-item-card::
        :shadow: md
        :margin: 2 2 0 0

        📖 :doc:`/docs/products/kafka/reference`

    .. grid-item-card::
        :shadow: md
        :margin: 2 2 0 0

        🧰 :doc:`Code samples </docs/products/kafka/howto/list-code-samples>`

Apache Kafka resources
----------------------

If you are new to Apache Kafka, try these resources to learn more:

* The main Apache Kafka project page: https://kafka.apache.org/

* The Karapace schema registry that Aiven maintains and makes available for every Aiven for Apache Kafka service: https://karapace.io/

* Our code samples repository, to get you started quickly: https://github.com/aiven/aiven-examples

* A lighthearted sample data generator to give you some fun (pizza order) data to try out: https://github.com/aiven/python-fake-data-producer-for-apache-kafka
