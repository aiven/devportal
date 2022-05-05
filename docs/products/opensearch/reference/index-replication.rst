Automatic adjustment of replication factors
===========================================

Aiven for OpenSearch® automatically adjusts index replication factors
to ensure data availability and service functionality.

When is the replication factor automatically adjusted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The maximum value for ``number_of_replicas`` is the number of nodes in the cluster - 1, as it is not possible to replicate indexes (shards) to a larger number of nodes than exist on the cluster

For example, for a 3-node cluster, the maximum ``number_of_replicas`` is 2, which means all shards on the index are replicated to all 3 nodes.

If ``number_of_replicas`` is set to 0 in a multi-node cluster, it is automatically increased to 1 to ensure no data-loss occurs if one node is lost.
