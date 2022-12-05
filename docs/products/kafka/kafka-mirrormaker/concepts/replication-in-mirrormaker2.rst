Replication in Apache Kafka® MirrorMaker 2
===========================================

**Q: What guarantees in replication does MirrorMaker 2 provide?**

A: The replication by MirrorMaker 2 is asynchronous in nature, which limits what can be guaranteed by it:

* In case of the source cluster failure, it can't be guaranteed that all records accepted in the source cluster will be replicated to the target cluster. For example, the source cluster accepts records R1, R2, R3, MirrorMaker 2 replicates R1 and R2 and then the source cluster becomes unavailable. Record R3 will not reach the target cluster in this case.
* It can't be guaranteed that when an offset is committed in a consumer group in the target cluster, the checkpoint for it immediately appear in the target cluster. It means, committed offset mapping between clusters is not absolutely precise and in case of failover some records that were consumed from the source cluster will be re-consumed from the target cluster.
* It can't be guaranteed that a record's schema (from schema topic) will be replicated to the target cluster before the record itself. In case of the source cluster failure, it can't be guaranteed that a schema will be replicated at all. So it's possible that a replicated record in the target cluster will not deserialize at the moment of consumption due to its schema missing in the target cluster.

**Q: Can it be guaranteed that no record is dropped during the replication?**

A: Yes.

**Q: Can it be guaranteed that replicated records will be in the same order as in the source topic?**

A: No, unless max.in.flight.requests.per.connection=1 is set (will affect performance badly, most likely).

**Q: Can it be guaranteed that there's no duplicates created during replication?**

A: No. Duplicates are currently unavoidable.

.. note:: Check `discussion <https://lists.apache.org/thread/lvh8mpfvk66wvyxtbxons3dlxx9tk0lv>`_ for the above questions

**Q: Is it possible to map committed offsets from the source cluster to offsets in the target cluster, for example, to perform a switch-over?**

A: Yes, it's possible. MirrorMaker 2 sends offset checkpoints to the target cluster periodically. For each consumer group, the records contain the current committed offsets in the source cluster and the corresponding offsets in the target cluster. Kafka's client library has a tool for this RemoteClusterUtils.translateOffsets. No access to the source cluster is needed to do this. It will give offsets and topics names in the target cluster to subscribe to to continue consumption. Please note, that checkpoints are asynchronous and are not guaranteed to always contain the latest committed offsets.

**Q: Does MirrorMaker 2 treat compacted topics any differently?**

A: No. Compaction doesn't change offsets of records, so offset mapping should work. As with normal topics, it can lose records due to long unavailability (e.g. tombstone records are collected from compacted topics eventually). Check `MirrorMaker 2.0 and compacted topics <https://lists.apache.org/thread/x84d1ggdyf48rv8hv9vzvdfq81d9z7qz>`_ for more information.

**Q: Will all topic configurations be replicated to the target cluster?**

A: By default, yes. It can't be configured, but not supported at the moment. Check `Discussion <https://lists.apache.org/thread/z844wtpl411pbr4jrn41n02zv09w6fj4>`_ for more information.

**Q: Will Aiven ACLs be replicated?**

A: No. Aiven ACLs are external to Kafka clusters, they won't be replicated by MirrorMaker 2.

**Q: Is it possible to throttle replication using quotas?**

A: It is not implemented at the moment. For more information check `MirrorMaker 2 throttling <https://lists.apache.org/thread/0nbvjrchtjmgj5qf2l809svx40b87xtt>`_

**Q: Does MirrorMaker 2 start replication from the earliest offset in the topic of from the latest?**

A: From the earliest. Currently, it is not configurable.

**Q: Is it possible to drop topic prefixes and replicate topic names as is?**

A: Yes, see https://app.intercom.com/a/apps/reo7593q/articles/articles/5411861/show

**Q: If topics replicated with prefixes, will the schema registry client work?** 

A: The schema registry client (e.g. used by the Avro converter) won't be able to find schemas for prefixed topics with a default configuration. However, it's possible to specify a custom {key,value}.subject.name.strategy on the client side.

**Q: What happens if one of the clusters MM is configured to work with is inaccessible?**

A: The MirrorMaker 2 process will not run, i.e. a single bad replication flow kills the whole replication.
