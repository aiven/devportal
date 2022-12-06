Aiven for ClickHouse® service architecture
==========================================

Aiven for ClickHouse is implemented as a multi-master cluster where replication of data is managed by ClickHouse itself, replication of schema and users is managed through ZooKeeper, and data backup and restoration is managed by Astacus. Discover a technical design behind the Aiven for ClickHouse® structure and behavior. This article helps you understand how Aiven for ClickHouse is set up and configured to work as a managed service.

Deployment modes
----------------

Aiven for ClickHouse can be deployed either as a single node, a single shard of 3 nodes, or multiple shards of 3 nodes each.
With a single shard, all data is present in all servers and all servers can be used for reads and writes (no main server, leader, or replica). With multiple shards, the data is split between all shards, the data of each shard is present in all nodes of the shard. 
Each Aiven for ClickHouse service is exposed as a single server URL pointing to both servers with connections going randomly to any of the servers. Aiven for ClickHouse is responsible for replicating the writes between the servers.
For synchronizing critical low-volume information between servers, Aiven for ClickHouse relies on ZooKeeper, which runs on each ClickHouse server.
The Aiven for ClickHouse multi-node service is exposed as an high-availability group.

Coordinating services
---------------------

Each Aiven for Clickhouse node runs Clickhouse, ZooKeeper, and Astacus.

* ZooKeeper - coordination and synchronization across nodes: one process per node accessible only from within the cluster.

  * By Clickhouse's Replicated database engine, to replicate database changes across the cluster (i.e. CREATE, UPDATE or ALTER TABLE)
  * By Clickhouse's ReplicatedMergeTree table engine, to coordinate replicating table data across the cluster. Data itself is not written to ZK, it is transferred directly between Clickhouse nodes over the interserver_http_port.
  * By Clickhouse for Replicated Access Entity Storage, this is storage of Users, Roles, Quotas, Row Policies for the whole cluster, in ZooKeeper so that all cluster nodes have the same view of these entites. This storage was developed at Aiven and is now part of the upstream Clickhouse.

* Astacus - Open-source project originated at Aiven which coordinates backups of cluster DBs including Clickhouse.

Data architecture
-----------------

* Aiven for ClickHouse enforces full schema replication: all databases, tables, users & grants are the same on all nodes.
* Aiven for ClickHouse enforces full data replication: table rows are the same on all nodes within a shard.
* We have some ZooKeeper data to backup in addition to Clickhouse data.
* Astacus does most of the backup & restore operations.

.. image:: /images/products/clickhouse/data-architecture.png
   :width: 800px
   :alt: Data architecture

Engines: database and table
---------------------------

ClickHouse has engines in two flavors: table engines and database engines.
The table engine decides how to store data on disk (or pretend it is stored but actually read data from somewhere else and expose it as a virtual table).
The database engine decides what happens when you try to list, create, or delete a table. It can be used to restrict a database to specific table engines. In addition to manipulating tables, the database engine handles some other tasks, such as managing replication.

Replicated database engine
''''''''''''''''''''''''''

The default ClickHouse database engine is the Atomic engine, which does nothing specific, it just creates tables on disk and allows most table engines.
In our case, we use the Replicated database engine. It's a variant of the Atomic, except that when we CREATE, UPDATE or ALTER TABLE the query is replicated to all other servers, using ZooKeeper.
This is how we ensure and enforce that all servers have the same table schema. This is what makes our servers a data cluster and not just two independent servers that can talk to each other when they want.

Replicated table engine
'''''''''''''''''''''''

The Table Engine is responsible for INSERT and SELECT queries.
There are a large variety of available engine, but each new one adds a significant burden to support their backup, their update and to make them safe to use. The most common one is the MergeTree engine. It's actually a family of seven engines but the differences between them does not matter to us and our support, all seven are allowed.
We also support other table engines that do not actually store data on disk, for views, distributed queries, etc.

.. list of supported engines / link

A core aspect of a MergeTree engine is that at least one new file is created for each INSERT query, and any created file is written once and never modified. These files are called "parts" in ClickHouse.
In the background, small files will be re-read, merged and rewritten more compactly. This way of writing data in parts is the cause of the performance profile of ClickHouse:

* INSERT need to be done in large batch to avoid handling tons of small parts.
* UPDATE and DELETE should be avoided or batched because removing a single "row" actually means rewriting an entire parts with all the rows except the one we want to remove, same logic applies for an update.
* SELECT can be fast because we know all the data found in a part is valid and all files can be cached since they never change.

Each engine of the MergeTree family has a matching ReplicatedMergeTree engine, it does the same thing except that all writes are replicated using ZooKeeper.
The data itself does not travel through ZooKeeper: a shared log of update queries is maintained with ZooKeeper, all nodes add entries on the queue and watch for changes to execute these queries. The data itself is directly fetched from one to the other over the interserver_http_port.
When a user asks to create a table using the MergeTree engine, we automatically rewrite the query to use the ReplicatedMergeTree. We do not let people create tables that are not replicated, this is how we make sure that all server have the same table data. This is what makes our pair of servers a high-availability pair and not just a cluster of unspecified shape.
This enforced replication is also active on ClickHouse services with a single node, this is used during maintenance updates.
