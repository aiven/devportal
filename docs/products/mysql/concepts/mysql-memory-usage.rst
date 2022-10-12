Understanding MySQL memory usage
==================================

**MySQL memory utilization can appear high, even if the service is relatively idle.**

:doc:`All services are subject to operating overhead </docs/platform/concepts/service-memory-limits>`, but some services, including MySQL, pre-allocate memory.
This can lead to a false impression that the service is misbehaving, when it is actually operating under normal conditions.


The InnoDB buffer pool
----------------------

Arguably, the most important MySQL component is the InnoDB Buffer Pool. 

Every time an operation happens to a table (read or write), the page where the records (and indexes) are located is loaded into the Buffer Pool.

This means that if the data you read and write the most has its pages in the Buffer Pool, the performance will be better than if you have to read pages from disk. When there are no more free pages in the pool, older pages must be evicted and if they were modified, synchronized back to disk (checkpointing).

The `MySQL 8.0 Reference <https://dev.mysql.com/doc/refman/8.0/en/innodb-buffer-pool.html>`_ says:

    The buffer pool is an area in main memory where InnoDB caches table and index data as it is accessed. The buffer pool permits frequently used data to be accessed directly from memory, which speeds up processing.

And `How MySQL Uses Memory <https://dev.mysql.com/doc/refman/8.0/en/memory-use.html>`_ says:

    InnoDB allocates memory for the entire buffer pool at server startup, using ``malloc()`` operations. The ``innodb_buffer_pool_size`` system variable defines the buffer pool size. Typically, a recommended ``innodb_buffer_pool_size`` value is 50 to 75 percent of system memory.

However, the InnoDB buffer pool isn't the only pre-allocated buffer.


Global buffers
--------------

The InnoDB buffer pool is part of the global buffers MySQL allocates to improve performance of database operations.

An explanation of these various buffers (or code areas) can be found in the MySQL documentation: `How MySQL Uses Memory <https://dev.mysql.com/doc/refman/8.0/en/memory-use.html>`_.

Using a 4GB service as an example, a view of the global buffers shows what memory has been allocated:

.. code-block:: sql

    SELECT SUBSTRING_INDEX(event_name,'/',2) AS code_area, 
       format_bytes(SUM(current_alloc)) AS current_alloc 
    FROM sys.x$memory_global_by_current_bytes 
    GROUP BY SUBSTRING_INDEX(event_name,'/',2) 
    ORDER BY SUM(current_alloc) DESC;

    +---------------------------+---------------+
    | code_area                 | current_alloc |
    +---------------------------+---------------+
    | memory/innodb             | 1.37 GiB      |
    | memory/performance_schema | 213.22 MiB    |
    | memory/sql                | 18.73 MiB     |
    | memory/mysys              | 8.82 MiB      |
    | memory/temptable          | 1.00 MiB      |
    | memory/mysqld_openssl     | 459.71 KiB    |
    | memory/mysqlx             | 3.25 KiB      |
    | memory/myisam             |  728 bytes    |
    | memory/csv                |  120 bytes    |
    | memory/vio                |   80 bytes    |
    +---------------------------+---------------+

Although allocated, the buffers may be relatively empty:

.. code-block:: sql

    SELECT CONCAT(FORMAT(A.num * 100.0 / B.num,2),'%') `BufferPool %` FROM
        (SELECT variable_value num FROM performance_schema.global_status
        WHERE variable_name = 'Innodb_buffer_pool_pages_data') A,
        (SELECT variable_value num FROM performance_schema.global_status
        WHERE variable_name = 'Innodb_buffer_pool_pages_total') B;

    +--------------+
    | BufferPool % |
    +--------------+
    | 0.45%        |
    +--------------+

.. Important::
        
    **High memory utilization, by itself, does not indicate a performance issue**. 

In the above example, the global buffers consume ~1.6 GiB of memory; almost half the RAM on a 4GB service. However, this does not denote any particular issue, but rather, standard operating conditions. 

When memory issues are suspected, or the service is encountering :doc:`/docs/platform/concepts/out-of-memory-conditions`, the buffers, queries, and concurrency should be examined to determine if:

- The buffer pool is full and checkpointing frequently
- The sum of the buffer pools are greater than the :doc:`available service memory </docs/platform/concepts/service-memory-limits>`
- Queries are generating excessive temporary (spill) files
