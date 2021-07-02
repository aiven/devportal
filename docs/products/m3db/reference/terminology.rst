Terminology for M3
==================

Time series
    Unique series of data identified by a set of labels, containing value(s) for specific points in time

Point
    A value and timestamp pair. This item can also include labels to denote which series of data this point belongs to.

Namespace
    A collection of data points. Namespaces are either unaggregated (includes all points as they arrived) or aggregated (with only one data point stored for each duration configured for the namespace).

Replication factor
    M3 stores data redundantly (if replication factor > 1), and uses by default quorum writes and best-effort quorum reads. In Aiven for M3, replication factor is hardcoded at 3, which means that single availability zone's worth of nodes can be lost and database still stays functional.

.. _Terminology Shard:

Shard
    M3 databases have their storage partitioned over multiple shards (Aiven for M3 services usually have 60 shards, although this can be changed by request). The M3 namespaces are spread across the shards and replicated based on their replication factor. Beware that changing the number of shards will cause all data to be lost, however the default value of 60 works well for most use cases.
