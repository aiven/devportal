Terminology for M3
==================

Time series
    unique series of data identified by a set of labels, containing value(s) for specific points in time

Point
    (time, value) entry in single time series 

Namespace
    retention-period limited view of the database, with (most of the time) all time series included; either unaggregated (all points), or aggregated at some resolution (at most only one point per resolution duration)

Replication factor
    M3 stores data redundantly (if replication factor > 1), and uses by default quorum writes and best-effort quorum reads. In Aiven for M3, replication factor is hardcoded at 3, which means that single availability zone's worth of nodes can be lost and database still stays functional.

Shard
    M3 databases have defined number of shards, and all namespaces within M3 are split also to the shards and replicated based on replication factor. In Aiven for M3, shard count is hardcoded at 60 but can be changed by request for particular service (however, all data is lost if the count is changed).


