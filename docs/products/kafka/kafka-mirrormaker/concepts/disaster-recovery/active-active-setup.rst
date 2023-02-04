MirrorMaker 2 active-active setup
#################################

An active-active setup of MM2 allows for data to be replicated between 2 clusters simultaneously. It implies a bidirectional mirroring between the 2 clusters. In order to do this MM2 uses topic prefixes in the form of **<cluster alias>.<topic name>**
In this setup, there are two actively used Apache Kafka® clusters: Cluster K1 and cluster K2. Topic topic exists in both clusters.

.. image:: /images/products/kafka/kafka-mirrormaker/Mirrormaker-Active-Active.png
    :alt: MirrorMaker 2 Active-Active Setup

Each cluster has it's own producers and consumers. Producers produce to topic. Consumers consume from topic using the same group.id. MirrorMaker 2 replicates data between clusters in both directions, therefore remote topics K1.topic and K2.topic exists in K2 and K1 correspondingly.

In case a disaster happens to K1 cluster and it becomes inaccessible for a long time for all the clients as well as MirrorMaker 2, the replication stops and some data may remain un-replicated in both clusters.

The clients (Producers 1 and Consumers 1) switch from K1 to K2. Consumers 1 continue consuming from the remote (i.e. replicated) topic K1.topic, Producers 1 start producing into topic.

When Consumers 1 finish consuming K1.topic, they switch to topic. All consumers act as one group now.

When K1 is recovered, its clients can switch back. Data that have been produced by Producers 1 into topic in K2 will be processed by Consumers 2.

Disaster recovery / high availability
'''''''''''''''''''''''''''''''''''''

This mode have data bidirectional mirroring between the 2 clusters, it allows clients to produce to both clusters and consume from both clusters at the same time as data can be produced and consumed from either cluster.

Typically this setup is used for high availability but can be useful for disaster recovery to make recovery simpler, as data is actively replicated between the clusters at all times, data in both clusters are identical which makes failover easy to either cluster.

**Implementation details**

* Consumers will need to be aware of the prefixed topics and can do this using wildcards or a priority knowledge of the topics to consume from, 
  see how to :doc:`configure here </docs/products/kafka/kafka-mirrormaker/concepts/replication-flow-topics-regex>`.

* :doc:`Karapace </docs/products/kafka/karapace>` schemas and topic configurations are not synced and must be created in both clusters.