Automatic adjustment of replication factors
===========================================

Aiven for OpenSearch automatically adjusts index replication factors
to ensure data availability and service functionality.

When replication factor is automatically adjusted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  If ``number_of_replicas`` is too large for current cluster size, it
   is automatically lowered to maximum possible value (number of nodes
   on the cluster - 1).

-  If ``number_of_replicas`` is 0 on a multi-node cluster, it is
   automatically increased to 1.

-  If ``number_of_replicas`` is anywhere between 1 and maximum value, it
   is not automatically adjusted.

Lowering replication factor
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When replication factor ( ``number_of_replicas`` ) is set to larger than
size of the cluster, ``number_of_replicas`` is automatically lowered, as
it is not possible to replicate indexes (shards) to a larger number of
nodes than what exists on the cluster. Do note number replication factor
is ``number_of_replicas`` + 1. For example, for three-node cluster,
maximum ``number_of_replicas`` is 2, which means all shards on the index
are replicated to all three nodes.

Increasing replication factor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For multi-node clusters, Aiven for OpenSearch automatically increases
``number_of_replicas`` to 1, if it is set to 0. This is to ensure no
data-loss occurs if one node is lost.
