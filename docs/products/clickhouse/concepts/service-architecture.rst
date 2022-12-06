Aiven for ClickHouse® service architecture
==========================================

Aiven for ClickHouse® is implemented as a multi-master cluster where the replication of data is managed by ClickHouse itself, the replication of schema and users is managed through ZooKeeper, and data backup and restoration is managed by Astacus. Discover a technical design behind the Aiven for ClickHouse®: its structure and operation. This article helps you understand how Aiven for ClickHouse is set up and configured to work as a managed service.

Deployment modes
----------------

Aiven for ClickHouse can be deployed either as a single node, a single shard of three nodes, or multiple shards of three nodes each.

* With a single shard, all data is present in all servers and all servers can be used for reads and writes (no main server, leader, or replica).
* With multiple shards, the data is split between all shards, the data of each shard is present in all nodes of the shard.
* With multiple nodes, the service is exposed as a high-availability group.

Each Aiven for ClickHouse service is exposed as a single server URL pointing to all servers with connections going randomly to any of the servers. Aiven for ClickHouse is responsible for replicating the writes between the servers.
For synchronizing critical low-volume information between servers, Aiven for ClickHouse relies on :ref:`ZooKeeper <zookeeper>`, which runs on each ClickHouse server.

Coordinating services
---------------------

Each Aiven for Clickhouse node runs Clickhouse, ZooKeeper, and Astacus.

.. _zookeeper:

ZooKeeper
'''''''''

ZooKeeper is responsible for coordination and synchronization across the nodes: one process per node, accessible only from within the cluster.

* By Clickhouse's replicated :ref:`database engine <replicated-database-engine>`, to replicate database changes across the cluster (CREATE, UPDATE or ALTER TABLE)
* By Clickhouse's ReplicatedMergeTree :ref:`table engine <replicated-table-engine>`, to coordinate replicating table data across the cluster. Data itself is not written to ZK, it is transferred directly between Clickhouse servers
* By Clickhouse for Replicated Access Entity Storage, this is storage of Users, Roles, Quotas, Row Policies for the whole cluster, in ZooKeeper so that all cluster nodes have the same view of these entities. This storage was developed at Aiven and is now part of the upstream Clickhouse.

Astacus
'''''''

Astacus is an open-source project originated at Aiven that coordinates backups of cluster databases, including ClickHouse.

Data architecture
-----------------

* Aiven for ClickHouse enforces full schema replication: all databases, tables, users & grants are the same on all nodes.
* Aiven for ClickHouse enforces full data replication: table rows are the same on all nodes within a shard.
* Astacus does most of the backup & restore operations.

.. image:: /images/products/clickhouse/data-architecture.png
   :width: 800px
   :alt: Data architecture

Engines: database and table
---------------------------

ClickHouse has engines in two flavors: table engines and database engines.

* Database engine is responsible for manipulating tables and decides what happens when you try to list, create, or delete a table. It can also be used to restrict a database to specific table engine or to manage replication.
* Table engine decides how to store data on a disk or how to enable reading data from outside the disk to expose it as a virtual table.

.. _replicated-database-engine:

Replicated database engine
''''''''''''''''''''''''''

The default ClickHouse database engine is the Atomic engine responsbile for createing tables on the disk and authorizing table engines to databases.

Aiven for ClickHouse uses the replicated database engine, which is a variant of Atomic. With this engine variant, queries for creating, updating, or altering tables are replicated to all other servers using :ref:`ZooKeeper <zookeeper>`.
As a result, all servers can have the same table schema, which makes them an actual data cluster and not multiple independent servers that can talk to each other.

.. _replicated-table-engine:

Replicated table engine
'''''''''''''''''''''''

The table engine is responsible for the INSERT and SELECT queries. From a wide variety of available table engines, the MergeTree engine is the most common one supported in Aiven for ClickHouse.

.. seealso::

    For a list of all the table engines that you can use in Aiven for ClickHouse, see :doc:`Supported table engines in Aiven for ClickHouse </docs/products/clickhouse/reference/supported-table-engines>`.

MergeTree engine
~~~~~~~~~~~~~~~~

With the MergeTree engine, at least one new file is created for each INSERT query and each new file is written once and never modified. In the background, new files (called *parts*) are re-read, merged, and rewritten into compact form. Writing data in parts determines the performance profile of ClickHouse.

* INSERT queries need to be batched to avoid handling a number of small parts.
* UPDATE and DELETE queries need to be batched. Removing or updating a single row requires rewriting an entire part with all the rows except the one we want to remove or update.
* SELECT queries are executed fast because all the data found in a part is valid and all files can be cached since they never change.

ReplicatedMergeTree engine
~~~~~~~~~~~~~~~~~~~~~~~~~~

Each engine of the MergeTree family has a matching ReplicatedMergeTree engine, which additionally enables the replication of all writes using :ref:`ZooKeeper <zookeeper>`. The data itself doesn't travel through ZooKeeper and is actually fetched from one ClickHouse server to the other. A shared log of update queries is maintained with ZooKeeper. All nodes add entries to the queue and watch for changes to execute the queries.

When a query to create a table using the MergeTree engine arrives, Aiven for ClickHouse automatically rewrites the query to use the ReplicatedMergeTree engine so that all tables are replicated and all servers have the same table data, which in fact makes the group of servers a high-availability cluster.
