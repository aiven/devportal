Aiven for PostgreSQL® shared buffers
====================================

Learn what Aiven for PostgreSQL® shared buffers are and why use them. Find out how using shared buffers impacts performance and how to set them up properly. Finally, discover how to inspect the database cache performance and and the query cache performance and check out how to put data into cache manually.

About shared buffers
--------------------

There are two primary memory allocations in Aiven for PostgreSQL that drastically impact the performance of queries: ``shared_buffers`` (the amount of RAM used for shared memory buffers) and ``work_mem`` (the maximum amount of memory to be used by a query operation before writing to temporary disk files).

Purpose of shared buffers
'''''''''''''''''''''''''

The ``shared_buffers`` parameter controls the amount of memory allocated to the database server for disk page caching.
The primary purpose of ``shared_buffers`` is to share memory over multiple sessions that may want to access the same blocks concurrently. Managing the access using the memory helps avoid unnecessary locking.

.. note::

    Even with ``shared_buffers``, Aiven for PostgreSQL relies on the filesystem cache for optimization so reading from the disk is still needed.

Allocation and setup
''''''''''''''''''''

``shared_buffers`` is allocated only once at startup; thus, it's not allocated per-session or per-user. It is shared among all sessions and useable for each worker and, therefore, each query.

To obtain a good performance of a database server with 1 GB or more of RAM, it is usually necessary to set this value to ~25% of the system memory. For systems with less than 1 GB of RAM, a smaller portion of RAM is preferable to allow for the operating system.

Allocating a lot of memory to ``shared_buffers`` is not always optimal for your configuration since the remaining free memory is allocated to workers (queries) and the filesystem cache. There are workloads where large ``shared_buffers`` are effective, but the allocation of more than 40% is unlikely to work better than a smaller-amount allocation.

The optimal setting for any service depends on the available RAM, the working data set, and the workload applied.

To examine the current ``shared_buffers`` value, run the following query:

.. code-block:: shell

   SHOW shared_buffers;

Tuning guidelines
-----------------

Aiven for PostgreSQL actively tracks data access patterns, updates the ``shared_buffers`` with frequently accessed data, and ejects Least Recently Used (LRU) when necessary. With many applications, only a fraction of the entire data set is accessed regularly. This data set fraction can be referred to as a *working set* or a *frequent read set* and often follows the 80/20 rule: 80% of the reads is in 20% of the data.

.. Tip::

   For optimal performance, a ``shared_buffers`` cache hit rate of 97-99% is ideal.

You can find an overview of ``shared_buffers`` cache hit rates using ``pg_statio_user_tables``:

.. code-block:: shell

   SELECT * FROM pg_statio_user_tables;

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

* Insufficient data activity to generate accurate statistics (new database)
* Current ``shared_buffers_percentage`` value too low
* Size of the working set larger than the maximum available ``shared_buffers_percentage`` (60%)

To achieve an optimal performance, the working set needs to fit in ``shared buffers``.

While the ``shared_buffers_percentage`` has a maximum value of `60%`, exceeding a value of `40%` suggests more RAM is required.

.. Tip::

   In many cases, the Aiven default value of 20% requires no further modification.


Inspecting the database cache performance
-----------------------------------------

For a deeper examination into the contents of the ``shared_buffers``, enable the ``pg_buffercache`` extension:

.. code-block:: shell

  CREATE EXTENSION pg_buffercache;

Calculate how many blocks from tables (r), indexes (i), sequences (S), and other objects are currently cached using the following query:

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

Relations with object IDs (``oid``) below ``16384`` are reserved system objects.

Inspecting the query cache performance
--------------------------------------

Queries can also be inspected for the cache hit performance using ``EXPLAIN``:

.. code-block:: shell
  
  EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
  SELECT * from records;
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

Putting data into the cache manually
------------------------------------

You may want to prewarm the ``shared_buffers`` in anticipation of a specific workload, such as a large analytical query set used for reporting. This can be accomplished using the ``pg_prewarm`` extension.

.. code-block:: shell

  CREATE EXTENSION pg_prewarm;

.. topic:: Example

   Call the ``pg_prewarm`` function and pass the name of a desired table.

   .. code-block:: shell

      SELECT * FROM pg_prewarm('public.records');
      pg_prewarm
      ------------
           368023

       SELECT pg_size_pretty(pg_relation_size('public.records'));
       pg_size_pretty
       ----------------
       2875 MB

   368023 pages have been read into the cache (or ~2875 MB).

If the ``shared buffers`` size is less than pre-loaded data, only the tailing end of the data is cached as the earlier data encounters a forced ejection.

Read more
-----------

For more information on shared buffers, see `Resource Consumption <https://www.postgresql.org/docs/current/runtime-config-resource.html>`_ in the PostgreSQL documentation.
