Apache Kafka® concepts
======================

A comprehensive glossary of essential Apache Kafka® terms and their meanings.

.. _Broker:

Broker
------

A server that operates Apache Kafka, responsible for message storage, processing, and delivery. Typically part of a cluster for enhanced scalability and reliability, each broker functions independently but is integral to Kafka's overall operations, separate from tools like Apache Kafka Connect.

Consumer
--------

An application that reads data from Apache Kafka, often processing or acting upon it. Various tools used with Apache Kafka ultimately function as either a producer or a consumer when communicating with Apache Kafka.

Consumer groups
---------------

Groups of consumers in Apache Kafka are used to scale beyond a single application instance. Multiple instances of an application coordinate to handle messages, with each group allocated to different partitions for even workload distribution.

Event-driven architecture
-------------------------

Application architecture centered around responding to and processing events.

.. _Event:

Event
-----

A single discrete data unit in Apache Kafka, consisting of a ``value`` (the message body) and often a ``key`` (for quick identification) and ``headers`` (metadata about the message).

Kafka node
----------

See :ref:`Broker`

Kafka server
------------

See :ref:`Broker`

Message
-------

See :ref:`Event`

Partitioning
------------

A method used by Apache Kafka to distribute a topic across multiple servers. Each server acts as the ``leader`` for a partition, ensuring data sharding and message order within each partition.

Producer
--------

An application that writes data into Apache Kafka without concern for the data's consumers. The data can range from well-structured to simple text, often accompanied by metadata.

Pub/sub
-------

A publish-subscribe messaging architecture where messages are broadcasted by publishers and received by any listening subscribers, unlike point-to-point systems.

Queueing
--------

A messaging system where messages are sent and received in the order they are produced. Apache Kafka maintains a watermark for each consumer to track the most recent message read.

Record
------

See :ref:`Event`

Replication
-----------

Apache Kafka's feature for data replication across multiple servers, ensuring data preservation even if a server fails. This is configurable per topic.

Topic
-----

Logical channels in Apache Kafka through which messages are organized. Topics are named in a human-readable manner, like ``sensor-readings`` or ``kubernetes-logs``.
