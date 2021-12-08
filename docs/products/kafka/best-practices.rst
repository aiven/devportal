Best practices
==============

We recommend to follow these best practices to ensure that your Apache Kafka service is fast and reliable.

Apache Kafka
-------------

Check your topic replication factors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apache Kafka services rely on replication between brokers to preserve data in
case of the loss of a node. Consider how business critical the data in
each topic is and make sure that replication is set high enough for it.

You can set the replication factor in `Aiven web console <https://console.aiven.io/>`_ when you create a new topic or edit an existing one.

.. note:: Do not set the replication factor below 2 in order to prevent data loss from unexpected node termination.

Choose a reasonable number of partitions for a topic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Too few partitions can cause bottlenecks in data processing. In the most
extreme case, a single partition means that messages are effectively
processed sequentially. However, too many partitions causes strain on
the cluster because of an additional overhead. As you cannot reduce the
number of partitions for existing topics, it is usually best to start
with a low number that allows efficient data processing and increase it
if needed.

As a general rule of thumb, the recommendation is to have max 4000
partitions per broker, and max 200 000 partitions per cluster (`source <https://blogs.apache.org/kafka/entry/apache-kafka-supports-more-partitions>`_).

Periodically examine topics with entity-based partitioning for imbalances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you partition messages based on an entity ID (for example, user ID),
there is a risk of heavily imbalanced partitions. This results in uneven
load in your cluster and reduces how effectively it can process messages
in parallel.

You can check the size of each partition in `Aiven web console <https://console.aiven.io/>`_ in the topic details, in the *Partitions* tab.


Find the right balance between throughput and latency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To find the right balance try different batch sizes in your producer and consumer configurations. Bigger batches increase throughput but also increase the latency for individual messages. Conversely, using smaller batches decreases message processing latency, but the overhead per message increases and the overall throughput decreases.

You can, for example, set ``batch.size`` and
``linger.ms`` in the producer configuration of your application code (see `official Apache Kafka documentation <https://kafka.apache.org/documentation/>`_ for reference).

Apache Kafka Connect
--------------------

Pay attention to ``tasks.max`` for connector configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, connectors run a maximum of **1** task, which usually leads
to under-utilization for large  Apache Kafka Connect services (unless you have
many connectors with one task each). In general, it is good to keep the
cluster CPUs occupied with connector tasks without overloading them. If
your connector is under-performing, you can try increasing ``tasks.max``
to match the number of partitions.

Consider a standalone  Apache Kafka Connect service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can run Apache Kafka Connect as part of your existing Aiven for Apache
Kafka service (for *business-4* and higher service plans). While this
allows you to try out Apache Kafka Connect by enabling the feature within your
existing service, for heavy usage we recommend that you enable a
standalone Apache Kafka Connect service to run your connectors. This allows you
to scale the Apache Kafka service and the connector service independently and
offers more CPU time and memory for the Apache Kafka Connect service.
