Apache Kafka® MirrorMaker 2 migration and DR high level approach
#############

MirrorMaker 2 (MM2) is the standard replication tool packaged with the Apache Kafka and can be run as a managed service on the Aiven platform. Under the hood, MM2 utilizes Kafka Connect to both consume from one Kafka cluster and then simultaneously produce to a second cluster. MM2 can be used to enable either an Active-Passive disaster recovery (DR) architecture or an active-active (HA) architecture.

MirrorMaker 2 Set Up
--------------

MM2 is enabled on the Aiven platform as a service integration between two Aiven Kafka clusters or an Aiven Kafka cluster and an external Kafka integration. Once the integration is created MM2 uses the concept of replication flows to direct traffic in the desired direction between Kafka clusters.

MM2 can be set up using any Aiven standard provisioning method Console, API, CLI, and TF.

Active - Passive Set Up
--------------------

**DR**  
To enable a DR scenario the backup cluster (Cluster B) must have topics with the exact same name as the primary cluster (Cluster A). By default this is not the case so all replication flows must use the org.apache.Kafka.connect.mirror.IdentityReplicationPolicy to guarantee this.
 
When a replication flow is created it will mirror all topics based upon the allow list or deny list configuration of the replication flow. The allow list should be set .* to guarantee that all internal topics such as '__consumer_offsets' for Kafka Connectors and consumer groups and '_schemas' for Karapace.

**Failover** 
A cluster that is replicated using MM2 will have a different 'service_uri' as well as certificates which will need to be accounted for when transitioning applications to use the backup cluster instead of the primary.

Given that Cluster B is designed for DR failover, in order to promote Cluster A as the primary cluster after a failover scenario, the data will have to be recreated in Cluster A from Cluster B using MM2 but in reverse.
This will involve deleting existing data in Cluster A other than consumer offset data

Active - Active Set Up
--------------------

**DR / HA**
An active-active setup of MM2 allows for data to be replicated between Cluster A and Cluster B simultaneously. In order to do this MM2 uses topic prefixes in the form of 
<cluster alias>.<topic name>

This mode allows clients to produce to both clusters and consume from both clusters at the same time.

Typically this setup is used for HA but can be useful for DR to make recovery simpler

Gotchas:
* Consumers will need to be aware of the prefixed topics and can do this using wildcards or a priority knowledge of the topics to consume from
* Karapace schemas and topic configurations are not synced and must be created in both clusters

**Failover**
It is much easier to failover and failback in this scenario as data is actively replicated between the clusters at all times.

Migration
--------------------
Migrating a Kafka cluster to Aiven will utilize the same pattern as DR. In this case however, you will need to utilize an external Kafka integration via the Aiven platform and can use this registered integration in the replication flow to migrate data from an external Kafka cluster to an Aiven Kafka cluster.

Checklist
--------------------
* MM2 does not guarantee absolute ordering it only guarantees key ordering
* Aiven’s MM2 service currently has a bug whereby topic replication factor and min.insync.replicas are reset
   * In order to work around this these values can be reset after the MM2 replication flows have been created
   * This bug is expected to be fixed Q4/22
* Offsets may not be preserved upon mirroring. This will be the case if some offsets have been deleted either through data age off or compaction.
* MM2 will preserve the correlation between consumer offsets between clusters.