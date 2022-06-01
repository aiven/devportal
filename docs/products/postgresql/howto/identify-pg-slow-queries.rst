Identify PostgreSQL® slow queries 
=================================

PostgreSQL® allows you to keep track of queries with certain performance metrics and statistics, which comes in handy when identifying slow queries.

.. Tip::

    When using Aiven for PostgreSQL®, you can check the **Query Statistics** tab for your service in the `Aiven Console <https://console.aiven.io/>`_ to identify long running queries.

Under the hood, the Query Statistics tab uses the ``pg_stat_statements`` `extension <https://www.postgresql.org/docs/current/pgstatstatements.html>`_, a module that provides a means for tracking the planning and execution statistics of all SQL statements executed by your PostgreSQL® server, to provide you with the basic information that can be useful for identifying slow queries.

Query statistics
''''''''''''''''

These are the entries provided by the Query Statistics which are deduced via the ``pg_stat_statements``:

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

You can also create custom queries using the ``pg_stat_statements`` view and use all the `available columns <https://www.postgresql.org/docs/current/pgstatstatements.html>`_ to investigate your use case.

Pre-requisites
''''''''''''''

To query the ``pg_stat_statements`` view, you'll need to create the ``pg_stat_statements`` extension (included in the :doc:`list of available extensions <../reference/list-of-extensions>`) that can be done via the following ``CREATE EXTENSION`` command::

  CREATE EXTENSION pg_stat_statements;


Discover slow queries
'''''''''''''''''''''

You can run the following command to display the ``pg_stat_statements`` view and all the columns contained:

.. code-block:: shell

    \d pg_stat_statements;

With the result being for PostgreSQL 13:

.. code-block:: text

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


On older PostgreSQL versions you might find different column names (e.g. the column previously named ``max_time`` is now ``max_exec_time``). Always refer to the `PostgreSQL® official documentation <https://www.postgresql.org/docs/current/pgstatstatements.html>`_ with the version you are using for accurate column matching.

.. Tip::

    You can write custom queries to ``pg_stat_statements`` to help you analyze recently run queries in your database.

Sort database queries based on ``total_exec_time``
''''''''''''''''''''''''''''''''''''''''''''''''''

The following query, inspired by a `GitHub repository <https://github.com/heroku/heroku-pg-extras/blob/ece431777dd34ff6c2a8dfb790b24db99f114165/commands/outliers.js>`_, uses the ``pg_stat_statements`` view, shows the running queries sorted descending by ``total_exec_time``, re-formats the ``calls`` column and deduces the ``prop_exec_time`` and ``sync_io_time``:

.. code-block:: postgresql

    SELECT interval '1 millisecond' * total_exec_time AS total_exec_time,
        to_char((total_exec_time/sum(total_exec_time) OVER()) * 100, 'FM90D0') || '%'  AS prop_exec_time,
        to_char(calls, 'FM999G999G999G990') AS calls,
        interval '1 millisecond' * (blk_read_time + blk_write_time) AS sync_io_time,
        query AS query
    FROM pg_stat_statements 
    WHERE userid = 
        (
            SELECT usesysid 
            FROM pg_user 
            WHERE usename = current_user 
            LIMIT 1
        )
    ORDER BY total_exec_time DESC
    LIMIT 10;

You can run the above commands on your own PostgreSQL® to gather more information about how the recent queries are performing.

.. Tip::
    It is possible to discard the ``pg_stat_statements`` previously gathered statistics by using the following command:

    .. code-block:: sql

        SELECT pg_stat_statements_reset()

Find top queries with high I/O activity
'''''''''''''''''''''''''''''''''''''''

The following SQL shows queries with their ``id`` and mean time in seconds. The result set is ordered based on the sum of ``blk_read_time`` and ``blk_write_time`` meaning that queries with the highest read/write are shown at the top.

.. code-block:: postgresql

    SELECT userid::regrole, 
        dbid, 
        query,
        queryid,
        mean_time/1000 as mean_time_seconds 
    FROM pg_stat_statements
    ORDER by (blk_read_time+blk_write_time) DESC
    LIMIT 10;

See top time-consuming queries
''''''''''''''''''''''''''''''

Aside from the relevant information to the database, the following SQL retrieves the number of calls, consumption time in milliseconds as ``total_time_seconds``, and the minimum, maximum, and mean times such query has ever been executed in milliseconds. The result set is ordered in descending order by ``mean_time`` showing the queries with most consumption time first.

.. code-block:: postgresql

    SELECT userid::regrole, 
        dbid, 
        query,
        calls, 
        total_time/1000 as total_time_seconds,
        min_time/1000 as min_time_seconds,
        max_time/1000 as max_time_seconds,
        mean_time/1000 as mean_time_seconds
    FROM pg_stat_statements
    ORDER by mean_time desc
    LIMIT 10;

Check queries with high memory usage
''''''''''''''''''''''''''''''''''''

The following SQL retrieves the query, its ``id``, and relevant information about the database. The result set in this case is ordered by showing the queries with the highest memory usage at the top, summing the number of shared memory blocks returned from the cache (``shared_blks_hit``), and 
the number of shared memory blocks marked as "dirty" during a request needed to be written to disk (``shared_blks_dirtied``).

.. code-block:: postgresql

    SELECT userid::regrole, 
        dbid, 
        queryid,
        query
    FROM pg_stat_statements 
    ORDER by (shared_blks_hit+shared_blks_dirtied) DESC limit 10;

.. Tip::

    Once you have identified slow queries, you can inspect the query plan and execution using `EXPLAIN ANALYZE <https://www.postgresql.org/docs/current/using-explain.html>`_ to understand how you can optimise your design to improve the performance. 
    
    The :doc:`how to optimize slow PostgreSQL® queries <../howto/optimize-pg-slow-queries>` contains some common suggestion for query optimisation.
