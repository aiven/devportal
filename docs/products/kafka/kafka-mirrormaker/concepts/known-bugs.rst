Known bugs
###############

MirrorMaker 2 is translating the offsets incorrectly if LAG shows negative on the target cluster and these are know issues which are expected to be resolved in 3.3.0 and :doc:`tuning </docs/products/kafka/kafka-mirrormaker/concepts/mirrormaker2-tuning>` can be done to minimize hitting this issue.

* **MirrorMaker 2 offset sync is incorrect if the target partition is empty**: https://issues.apache.org/jira/browse/KAFKA-12635 
* **Kafka-12635: Don't emit checkpoints for partitions without any offset**: https://github.com/apache/kafka/pull/11748
* **MM2 creates invalid checkpoint when offset mapping is not available**: https://issues.apache.org/jira/browse/KAFKA-13452 
* **Kafka-13452: MM2 shouldn't checkpoint when offset mapping is unavailable**: https://github.com/apache/kafka/pull/11492
* **MirrorMaker 2 is always set ``min.insync.replicas = 1`` in destination cluster topics**

MirrorMaker 2 always set ``min.insync.replicas = 1`` in destination cluster topics
-----------------------------------------------------------------------------------

**Description**

If a topic on destination cluster is updated or pre-created with ``min.insync.replicas > 1`` , MirrorMaker 2 would always be overwritten with ``min.insync.replicas = 1`` in target topics. 
The replication factor of target topics does not match the replication factor of source topics either when they are newly-created by MM2, or when they exist beforehand.

Steps to reproduce:

Create the following topics on destination Apache Kafka®:

* topic04 -  partitions: 3 replicas: 3 min.insync.replicas: 3
* topic05 - partitions: 6 replicas: 3 min.insync.replicas: 3

Create the following topics on source Apache Kafka®:

* topic04 -  partitions: 6 replicas: 2 min.insync.replicas: 1
* topic05 - partitions: 6 replicas: 3 min.insync.replicas: 3

Start MirrorMaker 2 with the following settings:

* 4. after > 15 minutes

topic configuration on destination Apache Kafka® got updated as the following:

* topic04 -  partitions: 6 replicas: 3 min.insync.replicas: 1
* topic05 - partitions: 6 replicas: 3 min.insync.replicas: 1

Findings:

* replicas does not get updated by MM2
* min.insync.replicas would be overwritten as 1 by MM2