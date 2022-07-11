Tombstones in Apache Cassandra®
===============================

Apache Cassandra manages deletion of data via a mechanism called *tombstones*. Because Cassandra is a distributed system,
it cannot delete data immediately in the same way as a traditional relational database. On a high-level, when a row is
deleted, instead of immediately deleting it, Cassandra will mark it as a tombstone row. Then, as part of regularly scheduled
maintenance, the row will actually get deleted. This maintenance is called *compaction* and the threshold is controlled by
the table-level setting ``gc_grace_seconds``. Any tombstone older than this setting will be removed completely during
compaction (with some caveats - more details in the Cassandra `documentation <compaction-tombstones_>`_ on compaction). The
default value for this setting is 864000 seconds (10 days).

Problems caused by tombstones
-----------------------------

Excessive amounts of tombstone rows can lead to various problems since the data is still there on disk, it's just got a
tombstone marker attached to it. If your workload includes a lot of data deletion, you are more likely to face problems.
Tombstones also result in a lot of garbage collection, which can affect cluster stability. The two main things affected are
read performance and disk usage.

**Read performance**: if read queries have to scan large numbers of tombstones, the query performance can be significantly
degraded. In particularly bad cases, the query can even time out. There are a couple of types of queries that are more likely
to be affected by this. They all involve scanning all or a large part of a table.

* Full table scans like ``SELECT * from inventory.items``
* Any query that requires adding ``ALLOW FILTERING``
* Range queries, i.e. queries with ``WHERE item_cost > threshold`` or similar

**Disk usage**: if you are rapidly filling up your cluster with data at the same time as you are doing a lot of
deletions, you will reach size limits sooner. This is because the tombstone data is not actually deleted and still taking up
space on disk.


If you suspect problems caused by tombstones for your cluster, you can check the logs. By default, if a query encounters over
1000 tombstones (configured by `tombstone_warn_threshold <cassandra-tombstone-warn_>`_) it will generate a log entry. The
entry will be in the format ``Read <X> live rows and <Y> tombstone cells for query <query> [...] (see tombstone_warn_threshold)``.

If it encounters over 100 000 tombstones (configured by ``tombstone_failure_threshold)``, the query will be aborted with a
``TombstoneOverwhelmingException`` (or just time out). To investigate a query that is encountering tombstones, the easiest
way is to connect with a ``cqlsh`` session and run ``TRACING ON`` followed by the query of interest. You can view values of
Cassandra settings with ``SELECT * FROM system_views.settings WHERE name = '<setting name>';``.

Preventing tombstone problems
-----------------------------

Often there is no "quick fix" solution for tombstone-related performance problems. Instead, you might want to rethink your
data model or your query strategy. Implementing something like table-level `time-to-live <cassandra-ttl_>`_ (TTL) or using
`TimeWindowCompactionStrategy <cassandra-twcs_>`_ (TWCS) as the compaction strategy might help mitigate these issues. In
short, some of the solutions available are:

* Review your data model and compaction strategy and consider implementing table TTL and TWCS.
* Avoid queries that end up running on all partitions in a table (queries with no ``WHERE`` clause, queries that need
  ``ALLOW FILTERING``).
* Update your queries so that they don't have to scan over tombstone rows in the same manner. For range queries, this might
  mean investigating if you can use a narrower range, or use a different approach to the query.
* If you are planning to delete all the data in a table, you can truncate the table to avoid creating tombstones.

Removing existing tombstones
----------------------------

The best is to wait for it to happen automatically as part of regular operations. Once more time than ``gc_grace_seconds``
has elapsed and a compaction happens, the tombstoned data will be removed from disk.

.. _compaction-tombstones: https://cassandra.apache.org/doc/latest/cassandra/operating/compaction/index.html#the-gc_grace_seconds-parameter-and-tombstone-removal
.. _cassandra-tombstone-warn: https://cassandra.apache.org/doc/latest/cassandra/configuration/cass_yaml_file.html#tombstone_warn_threshold
.. _cassandra-twcs: https://cassandra.apache.org/doc/latest/cassandra/operating/compaction/twcs.html
.. _cassandra-ttl: https://cassandra.apache.org/doc/latest/cassandra/operating/compaction/#ttl
