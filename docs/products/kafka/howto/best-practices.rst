Get the best from Apache Kafka
==============================

We recommend to follow these best practices to ensure that your Apache Kafka service is fast and reliable.

Check your topic replication factors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apache Kafka services rely on replication between brokers to preserve data in
case of the loss of a node. Consider how business critical the data in
each topic is and make sure that replication is set high enough for it.

You can set the replication factor in `Aiven web console <https://console.aiven.io/>`_ when you create a new topic or edit an existing one.

.. note:: We do not allow to set the replication factor below 2 in order to prevent data loss from unexpected node termination.

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

.. note:: Ordering is guaranteed only per partition. If you require relative ordering of records, you need to put that subset of data into the same partition.

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

Acknowledgements of received data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can  specify a value for acknowledgements setting ``acks`` in the client producer configuration. This will have an impact on how the success of a write operation is determined.

With ``acks`` equal to **0** after the producer sends the data, it does not wait for a confirmation from the broker. This will make communication faster. However, there is a potential loss of data in case of the broker being down when the producer sends the data. This configuration is only appropriate when you can afford loss of data.

With ``acks`` equal to **1** (default value and recommended behaviour), the producer waits for the leader broker to acknowledge that the data was received. This mode partially prevents data loss, however, the data loss still can occur if the broker goes down between the moment it sent acknowledgement and the data was replicated.

With ``acks`` equal to **all**, the leader and all the replicas will send confirmation of the received data. This configuration slows the communication, but ensures that there will be no data loss, since the replicas also confirm that the data was received.