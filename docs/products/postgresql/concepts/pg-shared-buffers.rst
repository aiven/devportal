PostgreSQL® shared buffers
===========================

In a very simplified view of PostgreSQL® memory, when a query is executed, there are 2 primary memory allocations that will drastically impact query performance: ``shared_buffers`` and ``work_mem``.

To paraphrase the PostgreSQL® documentation_:
  The ``shared_buffers`` parameter controls the amount of memory allocated to the database server to use for disk page caching.
  To get good performance, on a dedicated database server has 1 gigabyte or more of RAM, it is usually necessary to set this value to `~25%` of the system memory. 
  For systems with less than 1gb of RAM, a smaller portion of RAM is preferable to allow for the operating system.

It's important to note that ``shared_buffers`` is not allocated per-session or per-user and it is allocated only once, at startup.

**It is shared among all sessions, and is useable for every worker and ,therefore, every query.**

The primary purpose of ``shared_buffers`` is not explicitly to avoid reading from disk, PostgreSQL® still relies on the filesystem cache for some optimization. 
Rather, the objective is simply to share memory over multiple sessions that may want to access the same blocks concurrently; managing access in memory avoids unnecessary locking. 

While it may initially appear that allocating more memory to ``shared_buffers`` would be optimal for any configuration, the remaining free memory is allocated to workers (queries) and the filesystem cache.

There are some workloads where larger ``shared_buffers`` are effective, but it is unlikely that an allocation of more than `40%` will work better than a smaller amount.

The optimal setting, for any service, will depend on the available RAM, the working data set, and the workload applied.

To examine the current value:

.. code-block:: sql

  SHOW shared_buffers


Tuning guidelines
-----------------
PostgreSQL® actively tracks data access patterns, updates the ``shared_buffers`` with frequently accessed data, and ejects `Least Recently Used (LRU)` when necessary.

With many applications, only a fraction of the entire data set is accessed regularly. 
This may be referred to as a ``working set`` or a ``frequent read set``, and will often follow the ``80/20 rule``: `80%` of the reads is in `20%` of the data. 

.. Tip::

  For optimal performance, a ``shared_buffers`` cache hit rate of `97-99%` is ideal.

You can find an overview of ``shared_buffers`` cache hit rates using ``pg_statio_user_tables``:

.. code-block:: shell

  defaultdb=> SELECT * FROM pg_statio_user_tables;

   relid | schemaname | relname | heap_blks_read | heap_blks_hit | idx_blks_read | idx_blks_hit | toast_blks_read | toast_blks_hit | tidx_blks_read | tidx_blks_hit
  -------+------------+---------+----------------+---------------+---------------+--------------+-----------------+----------------+----------------+---------------
   16415 | public     | records |        1042770 |      88157826 |        184280 |     40282404 |               0 |              0 |              0 |             0
  (1 row)

Calculate the database cache hit rate with:

.. code-block:: shell

  SELECT 
    sum(heap_blks_read) as heap_read,
    sum(heap_blks_hit)  as heap_hit,
    sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) as hit_ratio
  FROM 
    pg_statio_user_tables;

     heap_read | heap_hit |         ratio
    -----------+----------+------------------------
       6942770 | 88157826 | 0.9883098315
    (1 row)

If the cache hit rate is significantly lower than 95%, this may be an indicator of several issues: 

* There is insufficient data activity to generate accurate statistics (new database)
* The current ``shared_buffers_percentage`` value is too low
* The size of the ``working set`` may be larger than the maximum available ``shared_buffers_percentage`` (`60%`)

You will never get optimal performance when the ``working set`` does not fit in shared buffers. 
While the ``shared_buffers_percentage`` has a maximum value of `60%`, exceeding a value of `40%` suggests more RAM is required.

.. Tip::

  In many cases, the Aiven default value of `20%`, requires no further modification.


Inspecting database cache performance
--------------------------------------
For a deeper examination into the contents of the ``shared_buffers``, enable the ``pg_buffercache`` extension:

.. code-block:: shell

  CREATE EXTENSION pg_buffercache;
  CREATE EXTENSION

The following query will calculate how many blocks from tables (r), indexes (i), sequences (S), and other objects are currently cached:

.. code-block:: shell

  SELECT c.relname, c.relkind
    , pg_size_pretty(count(*) * 8193) as buffered
    , round(100.0 * count(*) / ( SELECT setting FROM pg_settings WHERE name='shared_buffers')::integer,1) AS buffers_percent
    , round(100.0 * count(*) * 8192 / pg_relation_size(c.oid),1) AS percent_of_relation
  FROM pg_class c
  INNER JOIN pg_buffercache b ON b.relfilenode = c.relfilenode
  INNER JOIN pg_database d ON (b.reldatabase = d.oid AND d.datname = current_database())
  WHERE c.oid >= 16384
  AND pg_relation_size(c.oid) > 0
  GROUP BY c.oid, c.relname
  ORDER BY 3 DESC
  LIMIT 10;

   relname | relkind | buffered | buffers_percent | percent_of_relation
  ---------+---------+----------+-----------------+---------------------
   records | r       | 781 MB   |            99.7 |                27.2

Relations with object ID below `16384` are reserved system objects.

Inspecting query cache performance
----------------------------------
Queries can also be inspected for cache hit performance using `EXPLAIN`:

.. code-block:: shell
  
  EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
  defaultdb-> SELECT * from records;
                                                            QUERY PLAN
  --------------------------------------------------------------------------------------------------------------------------------
  Seq Scan on public.records  (cost=0.00..480095.20 rows=11207220 width=77) (actual time=0.158..16863.051 rows=11600000 loops=1)
    Output: id, "timestamp", data
    Buffers: shared hit=92345 read=275678 dirtied=10938
  Query Identifier: 2582883386000135492
  Planning:
    Buffers: shared hit=30 dirtied=2
  Planning Time: 1.081 ms
  Execution Time: 17467.342 ms
  (8 rows)

Using `hit / (hit + read)` shows `~25%` of this full table scan was in the ``shared_buffers``

Putting data into cache manually
--------------------------------
Occasionally, it may be desirable to prewarm the ``shared_buffers`` in anticipation of a specific workload, such as a large analytical query set used for reporting.
This can be accomplished using the ``pg_prewarm`` extension.

.. code-block:: shell

  CREATE EXTENSION pg_prewarm;
  CREATE EXTENSION

In the simplest operation, call the ``pg_prewarm`` function and pass the name of the desired table.

.. code-block:: shell

 SELECT * FROM pg_prewarm('public.records');
 pg_prewarm
 ------------
      368023

  SELECT pg_size_pretty(pg_relation_size('public.records'));
  pg_size_pretty
  ----------------
  2875 MB

In this example, 368023 pages have be read into the cache (or ~2875 MB).

If the ``shared buffers`` size is less than pre-loaded data, only the tailing end of the data will be cached as the earlier data will encounter forced ejection.


.. _documentation: https://www.postgresql.org/docs/current/runtime-config-resource.html
