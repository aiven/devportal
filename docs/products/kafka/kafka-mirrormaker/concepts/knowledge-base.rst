Knowledge base
#############

General
--------------

**Q: How does MirrorMaker 2 work?**

A: MirrorMaker 2 leverages Apache Kafka® Connect framework to run its code on it. It runs three types of connectors and its tasks: MirrorSourceConnector (replication itself), MirrorCheckpointConnector (committed offset checkpointing), and MirrorHeartbeatConnector (emitting heartbeat records that a replicated between clusters in order to check connectivity). All guarantees and limitations that Connect has, thus apply to MirrorMaker 2.

**Q: Can MirrorMaker 2 work with older Apache Kafka® clusters (2.3-)?**

A: Yes. MirrorMaker 2 works with older version of Apache Kafka®. Reportedly even 0.10.2 with some limitation. 0.10.1 doesn't have OffsetFetch v2 API, which make checkpointing inoperable. 

**Q: Is it necessary for the source and target cluster to run on the same version of Apache Kafka®?**

A: Not, it's not necessary.

**Q: Does MM write anything to the source cluster?**

A: It writes replicated offsets to the source cluster in its own topic in the current implementation.

**Q: Does MM use consumer group in the source cluster?**

A: No. It uses mm2-offsets.<cluster_alias> topic for tracking offsets that have been replicated. Also it assigns topic-partitions directly to tasks without consumer groups (`code <https://github.com/apache/kafka/blob/4ac892ca783acab8e574b9b24d17e767eedb3d5f/connect/mirror/src/main/java/org/apache/kafka/connect/mirror/MirrorSourceTask.java#L93>`).

**Q: Where is it recommended to run MirrorMaker 2: close to the source or target?**

A: It's recommended to run it close to the target cluster, since producer connectivity and lag is much more problematic than consumer.

**Q: What happens the replication factor or other parameters for a topic can't be satisfied in the target cluster?**

A: If MirrorMaker 2 can't satisfy the replication factor or other parameters in the target cluster, the topic in the target cluster won’t be created and replication won’t happen.

**Q: How does the number of partition that must be replicated affect MirrorMaker 2 performance?**

A: Each partition adds some overhead. If there are lots of partitions, some delay (minutes) might be observable before the replication starts after the restart of MirrorMaker 2.

**Q: Does MirrorMaker 2 work with Apache Kafka® in Aiven VPC?**

A: Yes. Any of Apache Kafka® services and MirrorMaker 2 itself can be located in any project's VPC or in a public cloud.

**Q: Does MirrorMaker 2 on Aiven support external Apache Kafka® cluster (not managed by Aiven)?**

A: Yes. Documented :doc: `here <https://docs.aiven.io/docs/products/kafka/kafka-mirrormaker>`.

**Q: Is it possible to integrate a Apache Kafka® service from a different Aiven project?**

A: Yes. A Apache Kafka® service from a different project can be integrated as an external Kafka (see above ⬆️).
