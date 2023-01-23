Active-passive setup
########################

In this setup, there are two Apache Kafka® clusters: primary and secondary. Topic *topic* exists in primary. The “active” cluster serves all produce and consume requests and the "passive" cluster is a copy of the “active” but without applications running against it.


.. image:: /images/products/kafka/kafka-mirrormaker/Mirrormaker-Active-Passive.png
    :alt: MirrorMaker 2 Active-Passive Setup

All the clients (producers and consumers) work with primary. MirrorMaker 2 replicates topic from primary to secondary (the remote topic name is ``primary_alias.topic_name`` where `primary_alias` is remote topic name).

In case a disaster happens to the primary cluster and it becomes inaccessible for a long time for all the clients as well as MirrorMaker 2, the replication stops and some data may remain un-replicated in the primary cluster, i.e. it may not reach secondary cluster before the disaster.

The clients switch to secondary cluster. Consumers continue consuming from the remote (i.e. replicated) topic primary.topic, and the producers start producing into it.

Alternatively, topic identical to the namesake from primary cluster, can be created in secondary. The producers start producing into it directly and consumers switch to it when they are done processing remote primary.topic.
This approach might be more convenient when the fallback to the primary cluster is needed in the future.

**Disaster Recovery**  

To enable a DR scenario the backup cluster (Cluster B) must have topics with the exact same name as the primary cluster (Cluster A). By default this is not the case so all replication flows must use the ``org.apache.Kafka.connect.mirror.IdentityReplicationPolicy`` to guarantee this.
 
When a replication flow is created it will mirror all topics based upon the allow list or deny list configuration of the replication flow. The allow list should be set .* to guarantee that all internal topics such as consumer offsets for Apache Kafka® Connectors and consumer groups, and schemas for Karapace.

**Failover** 

A cluster that is replicated using MM2 will have a different service URI as well as certificates which will need to be accounted for when transitioning applications to use the backup cluster instead of the primary.

Given that Cluster B is designed for DR failover, in order to promote Cluster A as the primary cluster after a failover scenario, the data will have to be recreated in Cluster A from Cluster B using MM2 but in reverse.
This will involve deleting existing data in Cluster A other than consumer offset data.