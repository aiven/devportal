ClickHouse® metrics exposed in Grafana®
=======================================

Learn what metrics are available via Grafana® for an Aiven for ClickHouse® service.

Current counts
--------------

The following metrics are displayed on dashboards as counts reflecting the current status:

- ``Databases``: Number of databases
- ``Tables``: Number of tables
- ``Parts``: Total number of MergeTree table parts
- ``Rows total``: Total number of rows
- ``Running Queries``: Total number of queries currently executed
- ``Running Merges``: Number of merges currently executed in the background
- ``Parts Merged``: Number of times data parts of ReplicatedMergeTree tables were successfully merged
- ``Readonly Tables``: Number of replicated tables that are currently in the read-only state due to re-initialization after ZooKeeper session loss or due to startup without ZooKeeper configured

Charts
------

The following metrics are displayed on dashboards as charts reflecting data changes over time:

``Connections``
^^^^^^^^^^^^^^^

- Number of connections to the TCP server (clients with native interface), also included server-server distributed query connections
- Number of connections to the HTTP server
- Number of connections from other replicas to fetch parts

``Queries``
^^^^^^^^^^^

- Number of executed SELECT queries (includes internal/monitoring queries)
- Number of executed INSERT queries
- Number of failed queries

``Delayed Queries``
^^^^^^^^^^^^^^^^^^^

- Number of INSERT queries that are throttled due to high number of active data parts for partition in a MergeTree table
- Number of queries that are stopped and waiting due to 'priority' setting

``Locks``
^^^^^^^^^
  
- Number of threads holding read lock in a table ``RWLock``
- Number of threads holding write lock in a table ``RWLock``
- Number of threads waiting for read on a table ``RWLock``
- Number of threads waiting for write on a table ``RWLock``

``Replicated Part Fetches``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Number of data parts being checked for consistency
- Number of data parts being fetched from replica
  Each fetch consumes disk IO and inter-server network IO.

Miscellaneous
^^^^^^^^^^^^^

- ``Merges``
  Merge operations reduce the number of parts and improve SELECT performance.
  Each merge consumes disk IO (read and write). A new part will be merged approximately 15 min after being inserted.
- ``Inserted Rows``: Number of rows INSERTed to all tables
- ``Inserted Bytes``: Number of bytes (uncompressed) INSERTed to all tables
- ``Merged Rows``: Rows read for background merges (before merge)
- ``Merged: Data Read``: Uncompressed bytes that were read for background merges
- ``Astacus Op duration``: Duration of each step of backups
- ``ZooKeeper``: Zookeeper sessions, watches, requests and ephemeral nodes coming from ClickHouse
- ``Compressed Data Read``: Number of bytes before decompression read from compressed sources
- ``Rows Delta``: Difference in number of rows between nodes
- ``Parts``: Total number of MergeTree table parts. Each INSERT creates a new part.
- ``Replicated Part Merged``
