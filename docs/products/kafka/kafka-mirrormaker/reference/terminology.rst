Terminology for Aiven for Apache Kafka MirrorMaker2
==================================================

.. _Terminology MM2ClusterAlias:

Cluster alias 
    The name alias defined in MirrorMaker2 for a certain Apache Kafka source or target cluster.

.. _Terminology MM2ReplicationFlow:

Replication flow
    The flow of data between two Apache Kafka clusters (called source and target) executed by Apache Kafka MirrorMaker2. 
    One Apache Kafka MirrorMaker2 service can execute multiple replication flows.

.. _Terminology MM2RemoteTopics:

Remote topics
    Topics replicated by MirrorMaker from a source Apache Kafka cluster to a target Apache Kafka cluster. 
    There is only one source topic for each remote topic. 
    Remote topics refer to the source cluster by the topic name prefix: ``{source_cluster_alias}.{source_topic_name}``.