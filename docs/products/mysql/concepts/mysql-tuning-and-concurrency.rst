MySQL tuning for concurrency
============================

**Determining how much memory is available for queries, and tuning concurrency accordingly, requires calculation of service memory, query analysis, and monitoring.**

Global buffers, thread buffers, and some uncontrolled memory allocations (`TRIGGERS`, `PROCEDURES` and `FUNCTIONS`), all contribute to the memory MySQL will require for a given workload.

There are several key calculations which are fundamental to tuning:

- Service memory
- Global buffers 
- Thread buffers
- Concurrency

.. Important::
  |  **Query output is for reference only**
  |  Queries should be run per service for accuracy and re-evaluated periodically for change. 


Service memory
--------------

The :doc:`service memory </docs/platform/concepts/service-memory-limits>` can be calculated as:

  |service_memory|

Where the overhead is currently: |vm_overhead|


Global buffers 
--------------

**MySQL pre-allocates global buffers to improve performance of database operations.**

An explanation of these various buffers (or code areas) can be found in the MySQL documentation: `How MySQL Uses Memory <https://dev.mysql.com/doc/refman/8.0/en/memory-use.html>`_.

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

Thread buffers
--------------

**Thread buffers are memory allocated per thread (or connection) to the database.**

Queries may use part or all of the allocation.

.. code-block:: sql 

  SELECT ( @@read_buffer_size
  + @@read_rnd_buffer_size
  + @@sort_buffer_size
  + @@join_buffer_size
  + @@binlog_cache_size
  + @@thread_stack
  + @@tmp_table_size
  + 2*@@net_buffer_length
  ) / (1024 * 1024) AS MEMORY_PER_CON_MB;

  +-------------------+
  | MEMORY_PER_CON_MB |
  +-------------------+
  |           17.9375 |
  +-------------------+

.. Important::
  | **The actual amount of memory a query could use is technically unbounded.**.
  | Uncontrolled memory allocations and temporary table usage can adversely affect the memory allocation.
  | The data dictionary size is based on the number of tables, fields and indexes within the database.


Concurrency
------------

Aiven configures a default value for the ``max_connections`` parameter for all MySQL services.

The :doc:`max_connections <max-number-of-connections>` parameter is based off the service :doc:`usable memory </docs/platform/concepts/service-memory-limits>`.

.. code-block:: sql 

  select @@max_connections;
  +-------------------+
  | @@max_connections |
  +-------------------+
  |               226 |
  +-------------------+ 

.. Important::
    **This parameter should be used as a guideline only**. 
    
    By default, ``max_connections`` is configured for *optimistic* concurrency using all available memory.
    
    In many instances, if the ``max connections`` are fully utilized, resource overcommitment and :doc:`/docs/platform/concepts/out-of-memory-conditions` will occur.

At ~18 MB per connection, a 4 GiB service has a potential memory usage of 4068 MB (18 * 226).
This is less than the service RAM, but exceeds the :doc:`service memory limit </docs/platform/concepts/service-memory-limits>`.

**For performance and stability, the following calculation is recommended:**

  :math:`max_concurrency =` |mysql_max_concurrency|

This value may be pessimistic for a workload that does not require the full thread buffer, but is an advisable starting point for concurrency testing and monitoring. Concurrency can be incremented, if service memory permits.

.. include:: /includes/platform-variables.rst
