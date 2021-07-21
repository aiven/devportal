PostgreSQL metrics exposed in Grafana
=====================================

The metrics/dashboard integration in the Aiven console enables you to push PostgreSQL metrics to an external endpoint like DataDog or to create an integration and a prebuilt dashboard in Aiven for Grafana. For more information on enabling the integration, see :doc:`../howto/report-metrics-grafana`. This article describes the default dashboard created in Grafana for any PostgreSQL instance.

General info about default dashboards
-------------------------------------

A few key points about the default dashboards pre-created by Aiven in Grafana:

1. The PostgreSQL dashboards show all tables and indexes for all logical databases since Aiven cannot determine tables or indexes relevance.
2. Some metrics are gathered but not shown in the default dashboard, you can access all available metrics by creating new dashboards.
3. New dashboards can be created to show any metrics or use any filtering criteria. The default dashboard can be used as a template to make the process easier.

.. Warning::
    When creating new dashboards, do not prefix the names with **“Aiven”** because they may be removed or replaced. The "Aiven" prefix is used to identify Aiven's system-managed dashboards. This also applies to the default dashboard, for which any direct editing to it could be lost.

PostgreSQL metrics prebuilt dashboard
-------------------------------------

The PostgreSQL default dashboard is split into several sections under two main categories: Generic and PostgreSQL. **Generic** metrics are not specific to the type of service running on the node and mostly related to CPU, memory, disk, and network. **PostgreSQL** metrics are specific for the service.

General metrics
---------------

Overview
""""""""

This section shows a high-level overview of the service node health. Major issues with the service are often visible directly in this section.

.. Note::
    In the Overview section, the figures for Business and Premium services are averages of all nodes that belong to the service. For some metrics, such as disk space, this typically does not matter since it's equal across all the nodes. For other metrics, especially when related to load concentrated only on the primary node, high values can be dampened by the average. Node-specific values are shown in the **system metrics** section.


.. image:: /images/products/postgresql/metrics-dashboard-overview.png
    :alt: Aiven Grafana Dashboard for PostgreSQL Overview Section

The following metrics are shown

.. list-table::
    :header-rows: 1

    * - Parameter Name
      - Parameter Definition
      - Additional Notes
    * - ``Uptime``
      - The time the service has been up and running.
      -
    * - ``Load average``
      - The number of processes that would want to run.
      - If the ``Load average`` figure is higher than the number of CPUs on the nodes, the service might be **under-provisioned**.
    * - ``Memory available``
      - Memory not allocated by running processes.
      -
    * - ``Disk free``
      - Amount of unused disk space.
      -


System metrics
""""""""""""""

This section shows a more detailed listing of various generic system-related metrics.


.. image:: /images/products/postgresql/metrics-dashboard-system.png
    :alt: Aiven Grafana Dashboard for PostgreSQL System Metrics Section

The following metrics are shown

.. list-table::
    :header-rows: 1

    * - Parameter Name
      - Parameter Definition
      - Additional Notes
    * - ``CPU``
      - ``System``, ``user``, ``iowait``, and ``interrupt`` request (IRQ) CPU usage.
      - A high ``iowait`` is an indication that the system is writing or reading too much data to or from disk.
    * - ``Load average``
      - The number of processes that would want to run.
      - the ``Load average`` figure is higher than the number of CPUs on the nodes, the service might be **under-provisioned**.
    * - ``Memory available``
      - The amount of memory not allocated by running processes.
      -
    * - ``Memory unused``
      - The amount of memory not allocated by running processes or used for buffer caches.
      -
    * - ``Context switches``
      - The number of switches from one process or thread to another.
      -
    * - ``Interrupts``
      - The number of interrupts per second.
      -
    * - ``Processes``
      - The number of processes that are actively doing something.
      - Processes that are mostly idle are not included.
    * - ``Disk free``
      - The current amount of remaining disk space.
      - Aiven suggest to actively monitor this value and associate it with an alert. The database will stop working correctly if it runs out of disk space.
    * - ``Disk i/o``
      - The number of bytes read and written per second on each of the nodes.
      -
    * - ``Data disk usage``
      - The amount of disk space that is in use on the service's data disk.
      -
    * - ``CPU iowait``
      - The percentage of CPU time spent waiting for the disk to become available for read and write operations
      - Aiven suggest to create an alert that is triggered when ``iowait`` goes beyond a certain threshold for an extended time. This gives you an opportunity to respond quickly when the database starts to slow down from too many read and write operations.
    * - ``Network``
      - The number of inbound and outbound bytes per second for a node.
      -
    * - ``Network (sum of all nodes)``
      - The same as the ``Network`` graph, but values are not grouped by service node.
      -
    * - ``TCP connections``
      - The number of open TCP connections, grouped by node.
      -
    * - ``TCP socket state total on all nodes``
      - The number of TCP connections across all service nodes, grouped by the TCP connection state.
      -

PostgreSQL-specific metrics
---------------------------

For most metrics, the metric name identifies the internal PostgreSQL statistics view. See the `PostgreSQL documentation <https://www.postgresql.org/docs/current/static/monitoring-stats.html>`_ for more detailed explanations of the various metric values.

Metrics that are currently recorded but not shown in the default dashboard include ``postgresql.pg_stat_bgwriter`` and ``postgresql.pg_class`` metrics as a whole, as well as some individual values from other metrics.

PostgreSQL overview
"""""""""""""""""""

The metrics in the PostgreSQL overview section are grouped by logical database. In addition, some metrics are grouped by host.


.. image:: /images/products/postgresql/metrics-dashboard-pg-overview.png
    :alt: Aiven Grafana Dashboard for PostgreSQL database Overview Section


.. list-table::
    :header-rows: 1

    * - Parameter Name
      - Parameter Definition
      - Additional Notes
    * - ``Database size``
      - The size of the files associated with a logical database
      - Some potentially large files that are not included in this value. Most notably, the write-ahead log (WAL) is not included in the size of the logical databases as it is not tied to any specific logical database.
    * - ``Connections``
      - The number of open connections to the database
      - Each connection puts a large burden on the PostgreSQL server and this number :doc:`should typically be fairly small even for large plans <pg-connection-limits>`. Use connection pooling to :doc:`reduce the number of connections <../concepts/pg-connection-pooling>` to the actual database server.
    * - ``Oldest running query age``
      - The age of the oldest running query
      - Typical queries run in milliseconds, and having queries that run for minutes often indicates an issue.
    * - ``Oldest connection age``
      - The age of the oldest connection.
      - Old open connections with open transactions are a problem, because they prevent ``VACUUM`` from performing correctly, resulting in bloat and performance degradation.
    * - ``Commits / sec``
      - The number of commits per second
      -
    * - ``Rollbacks / sec``
      - The number of rollbacks per second
      -
    * - ``Disk block reads / sec``
      - The number of 8 kB disk blocks that PostgreSQL reads per second, excluding reads that were satisfied by the buffer cache.
      - The read operations may have been satisfied by the operating system's file system cache.
    * - ``Buffer cache disk block reads / sec``
      - The number of 8 kB disk blocks that PostgreSQL reads per second that were already in buffer cache.
      -
    * - ``Temp files created / min``
      - The number of temporary files that PostgreSQL created per minute.
      - Temporary files are usually created when a query requests a large result set that can't fit in memory and needs to be sorted or when a query joins large result sets. A high number of temporary files or temporary file bytes may indicate that you should increase the working memory setting.
    * - ``Temp file bytes written / sec``
      - The number of bytes written to temporary files per second
      - This value should be kept at reasonable levels to avoid the server becoming IO-bound from having to write so much data to temporary files.
    * - ``Deadlocks / min``
      - The number of deadlocks per minute.
      - Deadlocks occur when different transactions obtain row-level locks for two or more of the same rows in a different order. You can resolve deadlock situations by retrying the transactions on the client side, but deadlocks can create significant bottlenecks and high counts are something that you should investigate.

PostgreSQL indexes
""""""""""""""""""

This section contains graphs related to the size and use of **indexes**. Since the default dashboard contains all indexes in all logical databases, it is easily convoluted for complex databases.

.. Tip::
    You might want to make a copy of the default dashboard and add additional constraints for the graphs to filter out uninteresting indexes. For example, for the size graph, you might want to include only indexes that are above ``X`` megabytes in size.


.. image:: /images/products/postgresql/metrics-dashboard-pg-indexes.png
    :alt: Aiven Grafana Dashboard for PostgreSQL database Indexes Section


.. list-table::
    :header-rows: 1

    * - Parameter Name
      - Parameter Definition
      - Additional Notes
    * - ``Index size``
      - The size of indexes on disk
      -
    * - ``Index scans / sec``
      - The number of scans per second per index
      -
    * - ``Index tuple reads / sec``
      - The number or tuples read from an index during index scans
      -
    * - ``Index tuple fetches / sec``
      - The number of table rows fetched during index scans
      -

Tables
------

This section contains graphs related to the size and use of **tables**. As with indexes, the graph will be convoluted for complex databases, and you may want to make a copy of the dashboard to add additional filters that exclude uninteresting tables.

.. image:: /images/products/postgresql/metrics-dashboard-pg-tables.png
    :alt: Aiven Grafana Dashboard for PostgreSQL database Indexes Section

.. list-table::
    :header-rows: 1

    * - Parameter Name
      - Parameter Definition
      - Additional Notes
    * - ``Table size``
      - The size of tables, excluding indexes and `TOAST data <https://www.postgresql.org/docs/current/storage-toast.html>`_
      -
    * - ``Table size total``
      - The total size of tables, including indexes and `TOAST data <https://www.postgresql.org/docs/current/storage-toast.html>`_
      -
    * - ``Table seq scans / sec``
      - The number of sequential scans per table per second
      - For small tables, sequential scans may be the best way of accessing the table data and having a lot of sequential scans may be normal, but for larger tables, sequential scans should be very rare.
    * - ``Table tuple inserts / sec``
      - The number of tuples inserted per second
      -
    * - ``Table tuple updates / sec``
      - The number of tuples updated per second
      -
    * - ``Table tuple deletions / sec``
      - The number of tuples deleted per second
      -
    * - ``Table dead tuples``
      - The number of rows that have become un-referenced due to an update or deletion for the same row, and uncommitted transactions older than the update or delete operation are no longer running. The rows will be marked reusable during the next ``VACUUM``.
      - High values here may indicate that vacuuming is not aggressive enough. Consider adjusting its configuration to make it run more often, because frequent vacuums reduce table bloat and make the system work better. The ``n_live_tup`` value is available and can be used to create graphs that show tables with high ratios of dead and live tuples.
    * - ``Table modifications since analyze``
      - The number of inserts, updates, or deletions since the last ``ANALYZE`` operation
      - A high number for this parameter means that the query planner may end up creating bad query plans because it is operating on obsolete data. Vacuuming also performs ``ANALYZE``, and you may want to adjust your vacuum settings if you see slow queries and high table modification counts for the related tables.

PostgreSQL vacuum and analyse
"""""""""""""""""""""""""""""

This section contains graphs related to **vacuum** and **analyze** operations. The graphs are grouped by table and, for complex databases, you probably want to add additional filter criteria to only show results where values are outside the expected range.


.. image:: /images/products/postgresql/metrics-dashboard-pg-vacuum.png
    :alt: Aiven Grafana Dashboard for PostgreSQL database Vacuum and Analyse Section

.. list-table::
    :header-rows: 1

    * - Parameter Name
      - Parameter Definition
      - Additional Notes
    * - ``Last vacuum age``
      - Time since the last manual vacuum operation for a table
      -
    * - ``Last autovacuum age``
      - Time since the last automatic vacuum operation for a table
      -
    * - ``Last analyze age``
      - Time since the last manual analyze operation for a table
      -
    * - ``Last autoanalyze age``
      - Time since last automatic analyze operation for a table
      -
    * - ``Maint ops / min``
      - The number of vacuum and analyze operations per table, per minute
      -

PostgreSQL miscellaneous
""""""""""""""""""""""""

This section contains PostgreSQL metrics graphs that are not covered by the previous sections.


.. image:: /images/products/postgresql/metrics-dashboard-pg-miscellaneous.png
    :alt: Aiven Grafana Dashboard for PostgreSQL database Miscellaneous Section

.. list-table::
    :header-rows: 1

    * - Parameter Name
      - Parameter Definition
      - Additional Notes
    * - ``Xact replay lag``
      - The replication lag between primary and standby nodes
      -
    * - ``Replication bytes diff``
      - The replication lag in bytes. This is the total diff across all replication clients.
      - To differentiate between different standby nodes, you can additionally group by the ``client_addr`` tag. This graph shows a difference based on ``write_lsn``; ``flush_lsn`` is also available.
    * - ``Unfrozen transactions``
      - The number of transactions that have not been frozen as well as the freeze limit
      - In very busy systems, the number of transactions that have not been frozen by vacuum operations may rise rapidly and you should monitor this value to ensure the freeze limit is not reached. Reaching the limit causes the system to stop working. If the ``txns`` values get close to the freeze limit, vacuum settings need to be made more aggressive, and you must resolve any problems that prevent vacuum operations from completing, such as long-running open transactions.
