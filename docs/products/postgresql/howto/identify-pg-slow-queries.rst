Identify PostgreSQL® slow queries 
=========================================

PostgreSQL® allows you to keep track of queries with certain performance metrics and statistics, which comes in handy when identifying slow queries.

While using Aiven for PostgreSQL®, you can check the **Query Statistics** tab for your service in the Aiven Console to identify queries that take too long to run.

Under the hood, the Query Statistics tab uses the ``pg_stat_statements`` `extension <https://www.postgresql.org/docs/current/pgstatstatements.html>`_, a module that provides a means for tracking the planning and execution statistics of all SQL statements executed by your PostgreSQL® server, to provide you with the basic information that would be useful for identifying slow queries.

Query statistics
''''''''''''''''

These are the entries provided by the Query Statistics which are deduced via the pg_stat_statements:

==================      =======================================================================
Column Type                Description
==================      =======================================================================
``Query``               Text of a representative statement
``Rows``                Total number of rows retrieved or affected by the statement
``Calls``               Number of times the statement was executed
``Min (ms)``            Minimum time spent executing the statement
``Max (ms)``            Maximum time spent executing the statement
``Mean (ms)``           Mean time spent executing the statement
``Stddev (ms)``         Population standard deviation of time spent executing the statement
``Total (ms)``          Total time spent executing the statement
==================      =======================================================================

However, creating custom queries using the ``pg_stat_statements`` yourself and leveraging all of `pg_stat_statements' view column types <https://www.postgresql.org/docs/current/pgstatstatements.html>`_ it offers might be something that helps you with your investigation use case.

Pre-requisites
''''''''''''''

To use ``pg_stat_statements``, you'll need the pg_stat_statements extension already created which is within the :doc:`../reference/list-of-extensions` approved list, which can be done via the following ``CREATE EXTENSION`` command::

  CREATE EXTENSION pg_stat_statements;


Discovering slow queries
''''''''''''''''''''''''

You can run the following command to display the ``pg_stat_statements`` view::

    defaultdb=> \d pg_stat_statements;
                            View "public.pg_stat_statements"
              Column        |       Type       | Collation | Nullable | Default 
       ---------------------+------------------+-----------+----------+---------
        userid              | oid              |           |          | 
        dbid                | oid              |           |          | 
        toplevel            | boolean          |           |          | 
        queryid             | bigint           |           |          | 
        query               | text             |           |          | 
        plans               | bigint           |           |          | 
        total_plan_time     | double precision |           |          | 
        min_plan_time       | double precision |           |          | 
        max_plan_time       | double precision |           |          | 
        mean_plan_time      | double precision |           |          | 
        stddev_plan_time    | double precision |           |          | 
        calls               | bigint           |           |          | 
        total_exec_time     | double precision |           |          | 
        min_exec_time       | double precision |           |          | 
        max_exec_time       | double precision |           |          | 
        mean_exec_time      | double precision |           |          | 
        stddev_exec_time    | double precision |           |          | 
        rows                | bigint           |           |          | 
        shared_blks_hit     | bigint           |           |          | 
        shared_blks_read    | bigint           |           |          | 
        shared_blks_dirtied | bigint           |           |          | 
        shared_blks_written | bigint           |           |          | 
        local_blks_hit      | bigint           |           |          | 
        local_blks_read     | bigint           |           |          | 
        local_blks_dirtied  | bigint           |           |          | 
        local_blks_written  | bigint           |           |          | 
        temp_blks_read      | bigint           |           |          | 
        temp_blks_written   | bigint           |           |          | 
        blk_read_time       | double precision |           |          | 
        blk_write_time      | double precision |           |          | 
        wal_records         | bigint           |           |          | 
        wal_fpi             | bigint           |           |          | 
        wal_bytes           | numeric          |           |          | 

The following output is from PostgreSQL® ``V13``, on older versions you might find different column names such as previously ``max_time`` which is now ``max_exec_time``, always refer to the PostgreSQL® official documentation with the version you are using for accurate column matching.
You can come up with your own query to help you analyze relevant information about your recently run queries.

Here is an example query that use the view to display relevant information about some previously run queries that some of them are relatively slow.
This query is inspired by `this <https://github.com/heroku/heroku-pg-extras/blob/ece431777dd34ff6c2a8dfb790b24db99f114165/commands/outliers.js>`_ implementation, it re-formats the ``calls`` column and deduces the ``prop_exec_time`` and ``sync_io_time``::

    SELECT interval '1 millisecond' * total_exec_time AS total_exec_time,
        to_char((total_exec_time/sum(total_exec_time) OVER()) * 100, 'FM90D0') || '%'  AS prop_exec_time,
        to_char(calls, 'FM999G999G999G990') AS calls,
        interval '1 millisecond' * (blk_read_time + blk_write_time) AS sync_io_time,
        query AS query
    FROM pg_stat_statements WHERE userid = (SELECT usesysid FROM pg_user WHERE usename = current_user LIMIT 1)
    ORDER BY total_exec_time DESC
    LIMIT 10;

You can run the above commands on your own PostgreSQL® to gather more information about how the recent queries are performing.

.. Tip::
    It is possible to discards gathered statistics so far by ``pg_stat_statements`` by using the following command::
        
        SELECT pg_stat_statements_reset()

SQL queries having high I/O activity
------------------------------------

You can run this command to select queries with their id and mean time in seconds, with the order where queries with the highest read/write are shown at the top, along with database relevant information such as ``userid`` and ``dbid``.

::

    SELECT userid::regrole, dbid, query,queryid,mean_time/1000 as mean_time_seconds 
    FROM pg_stat_statements
    ORDER by (blk_read_time+blk_write_time) DESC
    LIMIT 10;

Top time consuming queries
--------------------------

Aside from the relevant information to the database, this query shows the number of calls, consumption time in milliseconds as total_time_seconds, and the minimum, maximum, and mean times such query has ever been executed in milliseconds, whereas it is ordered by showing the ones with most consumption times first.

::

    SELECT userid::regrole, dbid, query ,calls, total_time/1000 as total_time_seconds ,min_time/1000 as min_time_seconds,max_time/1000 as max_time_seconds,mean_time/1000 as mean_time_seconds
    FROM pg_stat_statements
    ORDER by mean_time desc
    LIMIT 10;

Queries with high memory usage
------------------------------

This query mainly shows the query, its id, and relevant information about the database, similar to previous queries. However, what matters here is that it is
ordered by showing the queries with the highest memory usage, and that is by summing the number of shared memory blocks returned from the cache, using ``shared_blks_hit``, and 
the number of shared memory blocks marked as "dirty" during a request needed to be written to disk, using ``shared_blks_dirtied``.

::

    SELECT userid::regrole, dbid, queryid,query
    FROM pg_stat_statements 
    ORDER by (shared_blks_hit+shared_blks_dirtied) DESC limit 10;

When you have identified slow queries, you can inspect the query plan and execution using `EXPLAIN ANALYZE <https://www.postgresql.org/docs/current/using-explain.html>`_ to see if you need to add any missing indexes or restructure your schema to improve the performance.

Now that slow queries are identified, you can have a read on :doc:`how to optimize slow PostgreSQL® queries <../howto/optimize-pg-slow-queries>`
