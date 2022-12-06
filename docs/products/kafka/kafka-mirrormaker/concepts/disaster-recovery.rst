Disaster Recovery
#############

**Disaster recovery** is one of the primary use cases for MirrorMaker 2. MirrorMaker 2 replicates data between Kafka clusters, including clusters located in different data centres. Thus it's possible to minimize the period of unavailability of Apache Kafka®.

However, it's important to remember that MirrorMaker 2 *doesn't provide synchronous replication*, so it's possible that the latest records accepted into a topic in the source cluster might not be replicated to the target cluster before the source cluster fails.

Another important note is that planning disaster recovery scenarios with MirrorMaker 2, one should be prepared for dealing with out-of-order (can be mitigated with max.in.flight.requests.per.connection=1 probably) and duplicate records. So if the record interpretation depend on their strict order (even within a single partition), MirrorMaker 2 might not provide the desired solution.

MirrorMaker 2 is still under active development and hopefully at some point it will be able to provide stricter guarantees.
There is no one-size-fits-all disaster recovery solution. Various requirements such as the nature of the data, its volume, acceptable ops overhead, and costs should be taken into account. 

**To create a disaster recovery procedure that is right for your data, several questions must be carefully answered:**
-----------------

* **What data needs replication?**
.. note:: Some data may be less important or not important at all and replicating all of it will unnecessary consume resource.

* **Is the strict order of the records important?**

* **What are the implications of out-of-order records?**

* **Can duplicate records be tolerated?**

* **What are the implications of duplicate records?**
.. note:: MM2 can be set up using any Aiven standard provisioning method Console, API, CLI, and TF.

Disaster recovery building blocks
---------
1. Data replication performed by MirrorMaker 2. The replication flow is the way for copying data between clusters.
2. Offset translation performed by MirrorMaker 2.
3. Monitoring of the replication process.
4. Disaster recovery playbooks, that must be written and tested.

Migration and DR high level approach
-------------------------------------

MirrorMaker 2 (MM2) is the standard replication tool packaged with the Apache Kafka and can be run as a managed service on the Aiven platform. Under the hood, MM2 utilizes Kafka Connect to both consume from one Kafka cluster and then simultaneously produce to a second cluster. MM2 can be used to enable either an Active-Passive disaster recovery (DR) architecture or an active-active (HA) architecture.

Setup
--------------

MM2 is enabled on the Aiven platform as a service integration between two Aiven for Apache Kafka clusters or a Kafka cluster and an external Kafka integration. Once the integration is created MM2 uses the concept of replication flows to direct traffic in the desired direction between Kafka clusters.

MM2 can be set up using any Aiven standard provisioning method Console, API, CLI, and TF.

Active-passive setup
--------------------

In this setup, there are two Kafka clusters: primary and secondary. Topic topic exists in primary.

.. image:: /images/products/kafka/kafka-mirrormaker/Mirrormaker-Active-Passive.png
    :alt: MirrorMaker 2 Active-Passive Setup

All the clients (producers and consumers) work with primary. MirrorMaker 2 replicates topic from primary to secondary (the remote topic is primary.topic).

A disaster happens to primary cluster and it becomes inaccessible for long time for all the clients and MirrorMaker 2 as well. The replication stops. Some data may remain un-replicated in primary cluster, i.e. not reach secondary before the disaster.\

The clients switch to secondary cluster. Consumers continue consuming from the remote (i.e. replicated) topic primary.topic, producers start producing into it.

Alternatively, topic identical to the namesake from primary cluster, can be created in secondary. The producers start producing into it directly and consumers switch to it when they are done processing remote primary.topic.
This approach might be more convenient when the fallback to the primary cluster is needed in the future.

**Disaster Recovery**  

To enable a DR scenario the backup cluster (Cluster B) must have topics with the exact same name as the primary cluster (Cluster A). By default this is not the case so all replication flows must use the org.apache.Kafka.connect.mirror.IdentityReplicationPolicy to guarantee this.
 
When a replication flow is created it will mirror all topics based upon the allow list or deny list configuration of the replication flow. The allow list should be set .* to guarantee that all internal topics such as consumer offsets for Kafka Connectors and consumer groups, and schemas for Karapace.

**Failover** 

A cluster that is replicated using MM2 will have a different service URI as well as certificates which will need to be accounted for when transitioning applications to use the backup cluster instead of the primary.

Given that Cluster B is designed for DR failover, in order to promote Cluster A as the primary cluster after a failover scenario, the data will have to be recreated in Cluster A from Cluster B using MM2 but in reverse.
This will involve deleting existing data in Cluster A other than consumer offset data

Active-active setup
--------------------

In this setup, there are two actively used Kafka clusters: K1 and K2. Topic topic exists in both cluster.

.. image:: /images/products/kafka/kafka-mirrormaker/Mirrormaker-Active-Active.png
    :alt: MirrorMaker 2 Active-Active Setup

Each cluster has it's own producers and consumers. Producers produce to topic. Consumers consume from topic using the same group.id. MirrorMaker 2 replicates data between clusters in both directions, therefore remote topics K1.topic and K2.topic exists in K2 and K1 correspondingly.

A disaster happens to K1 cluster and it becomes inaccessible for long time for all the clients and MirrorMaker 2 as well. The replication stops. Some data may remain un-replicated in both clusters.

The clients (Producers 1 and Consumers 1) switch from K1 to K2. Consumers 1 continue consuming from the remote (i.e. replicated) topic K1.topic, Producers 1 start producing into topic.

When Consumers 1 finish consuming K1.topic, they switch to topic. All consumers act as one group now.

When K1 is recovered, its clients can switch back. Data that have been produced by Producers 1 into topic in K2 will be processed by Consumers 2.

**DR / HA**

An active-active setup of MM2 allows for data to be replicated between Cluster A and Cluster B simultaneously. In order to do this MM2 uses topic prefixes in the form of 
**<cluster alias>.<topic name>**

This mode allows clients to produce to both clusters and consume from both clusters at the same time.

Typically this setup is used for HA but can be useful for DR to make recovery simpler

Gotchas:

* Consumers will need to be aware of the prefixed topics and can do this using wildcards or a priority knowledge of the topics to consume from

* Karapace schemas and topic configurations are not synced and must be created in both clusters

**Failover**

It is much easier to failover in this scenario as data is actively replicated between the clusters at all times.

Migration
--------------------
Migrating a Kafka cluster to Aiven will utilize the same pattern as DR. In this case however, you will need to utilize an external Kafka integration via the Aiven platform and can use this registered integration in the replication flow to migrate data from an external Kafka cluster to an Aiven for Apache Kafka cluster.

Checklist
--------------------
* MM2 does not guarantee absolute ordering, it only guarantees key ordering
* Aiven’s MM2 service currently has a bug whereby topic replication factor and min.insync.replicas are reset
   * In order to work around this, these values can be reset after the MM2 replication flows have been created
   * This bug is expected to be fixed Q4/22
* Offsets may not be preserved upon mirroring. This will be the case if some offsets have been deleted either through data age off or compaction.
* MM2 will preserve the correlation between consumer offsets between clusters.