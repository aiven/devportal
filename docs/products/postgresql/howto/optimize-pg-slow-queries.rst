Optimize PostgreSQL® slow queries 
=========================================

When using PostgreSQL® it is more likely that you'd want to optimize the performance of your identified slow queries. You can have a read on :doc:`how to track down slow PostgreSQL® queries <../howto/identify-pg-slow-queries>`, whereas this article will be more about things to keep in mind and to perhaps do to optimize slow queries.

Pre-requisites
''''''''''''''

To use ``pg_stat_statements``, you'll need the pg_stat_statements extension already created which is within the :doc:`../reference/list-of-extensions` approved list, which can be done via the following ``CREATE EXTENSION`` command::

  CREATE EXTENSION pg_stat_statements;


Common slow queries optimizations
'''''''''''''''''''''''''''''''''

It is worth knowing that many database indexes on a table can also cause problems for write performance due to the overhead of maintaining them.

Handle an increase in database connections
------------------------------------------

When using a PostgreSQL® database, there might be more than one application that wants to connect to it, hence the need to handle a number of database connections.
YOu can use ``connection pooling`` to handle an increase in database connections.

When your application code scales horizontally to accommodate high loads, you might find that you inadvertently reach the :doc:`connection limits <../reference/pg-connection-limits>` for your plan. Each connection in PostgreSQL runs in a separate process, and this makes them more expensive (compared to threads, for example) in terms of inter-process communication and memory usage, since each connection consumes a certain amount of RAM.

The most effective solution to support a large number of connections is to use Aiven connection pooling which is implemented using `PgBouncer <https://www.pgbouncer.org>`_. You can add and configure the connection pooling for your service on the ``Pools`` tab in the Aiven console.

Move read-only queries to standby nodes
---------------------------------------

If your service is running a business-* or premium-* plan, you have standby nodes available in a high availability setup. These support :doc:`support read-only <create-read-replica>` by direct connections to the Read-only replica URL to reduce the effect of slow queries on the primary node.

Move read-only queries to a remote read replica
-----------------------------------------------

We also offer the option to create a :doc:`remote read replica <create-read-replica>` service that can be set up in the same cloud and region or in a different one. This provides a dedicated read-only service that you can use to reduce the load on the main service if it is under heavy write load.

