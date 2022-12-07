Active-active setup
########################

An active-active setup of MM2 allows for data to be replicated between Cluster A and Cluster B simultaneously. It implies a bidirectional mirroring between the 2 clusters. In order to do this MM2 uses topic prefixes in the form of **<cluster alias>.<topic name>**
In this setup, there are two actively used Apache Kafka® clusters: K1 and K2. Topic topic exists in both cluster.

.. image:: /images/products/kafka/kafka-mirrormaker/Mirrormaker-Active-Active.png
    :alt: MirrorMaker 2 Active-Active Setup

Each cluster has it's own producers and consumers. Producers produce to topic. Consumers consume from topic using the same group.id. MirrorMaker 2 replicates data between clusters in both directions, therefore remote topics K1.topic and K2.topic exists in K2 and K1 correspondingly.

In case a disaster happens to K1 cluster and it becomes inaccessible for a long time for all the clients as well as MirrorMaker 2, the replication stops and some data may remain un-replicated in both clusters.

The clients (Producers 1 and Consumers 1) switch from K1 to K2. Consumers 1 continue consuming from the remote (i.e. replicated) topic K1.topic, Producers 1 start producing into topic.

When Consumers 1 finish consuming K1.topic, they switch to topic. All consumers act as one group now.

When K1 is recovered, its clients can switch back. Data that have been produced by Producers 1 into topic in K2 will be processed by Consumers 2.

**DR / HA**

This mode allows clients to produce to both clusters and consume from both clusters at the same time.

Typically this setup is used for HA but can be useful for DR to make recovery simpler

Gotchas:

* Consumers will need to be aware of the prefixed topics and can do this using wildcards or a priority knowledge of the topics to consume from

* Karapace schemas and topic configurations are not synced and must be created in both clusters

**Failover**

It is much easier to failover in this scenario as data is actively replicated between the clusters at all times.