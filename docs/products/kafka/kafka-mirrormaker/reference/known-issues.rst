Known issues
############

MirrorMaker 2 may translate offsets incorrectly if LAG shows negative on the target cluster
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
The following are known issues that are expected to be resolved in version 3.3.0. See  :doc:`recommended tuning paramters</docs/products/kafka/kafka-mirrormaker/reference/advanced-params>` to minimize hitting this issue.

* **MirrorMaker 2 offset sync is incorrect if the target partition is empty**: https://issues.apache.org/jira/browse/KAFKA-12635 
* ``Kafka-12635``: **Don't emit checkpoints for partitions without any offset**: https://github.com/apache/kafka/pull/11748
* **MM2 creates invalid checkpoint when offset mapping is not available**: https://issues.apache.org/jira/browse/KAFKA-13452 
* ``Kafka-13452``: **MM2 shouldn't checkpoint when offset mapping is unavailable**: https://github.com/apache/kafka/pull/11492


MirrorMaker 2 is always set ``min.insync.replicas = 1`` in destination cluster topics
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
If a topic on the destination cluster is updated or pre-created with ``min.insync.replicas > 1`` , MirrorMaker 2 would always be overwritten with ``min.insync.replicas = 1`` in target topics. 
The replication factor of target topics does not match the replication factor of source topics either when they are newly created by MirrorMaker 2, or when they exist beforehand.

* MirrorMaker 2 does not update ``replicas``.
* MirrorMaker 2 always overwrites ``min.insync.replicas`` as 1.