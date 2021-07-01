List of advanced parameters
============================

On creating a PostgreSQL database, you can customize it using a series of the following advanced parameters:

General parameters
--------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``admin_password``
    - string
    - Custom password for admin user. Defaults to random string. Must be set only when a new service is being created.
  * - ``admin_username``
    - string
    - Custom username for admin user. Must be set only when a new service is being created.

      The default value is: ``avnadmin``
  * - ``backup_hour``
    - integer
    - The hour of day (in UTC) when backup for the service is started. New backup is only started if previous backup has already completed.

      A valid range is: 0-24
  * - ``backup_minute``
    - integer
    - The minute of an hour when backup for the service is started. New backup is only started if previous backup has already completed.

      A valid range is: 0-60
  * - ``ip_filter``
    - array
    - Restricts incoming connections from CIDR address block, e.g. ``10.20.0.0/16``

      The default value is: ``0.0.0.0/0``
  * - ``pg.deadlock_timeout``
    - integer
    - Amount of time, in milliseconds, to wait on a lock before checking to see if there is a deadlock condition.
  * - ``pg.idle_in_transaction_session_timeout``
    - integer
    - Time out sessions with open transactions after this number of milliseconds
  * - ``pg.jit``
    - boolean
    - Controls system-wide use of Just-in-Time Compilation (JIT).
  * - ``pg.log_error_verbosity``
    - string
    - Controls the amount of detail written in the server log for each message that is logged.

      A valid range is: terse, default, verbose
  * - ``pg.log_line_prefix``
    - string
    - Choose from one of the available log-formats. These can support popular log analysers like ``pgbadger``, ``pganalyze`` etc.
  * - ``pg.log_min_duration_statement``
    - integer
    - Log statements that take more than this number of milliseconds to run, -1 disables
  * - ``pg.max_files_per_process``
    - integer
    - PostgreSQL maximum number of files that can be open per process
  * - ``pg.max_locks_per_transaction``
    - integer
    - PostgreSQL maximum locks per transaction
  * - ``pg.max_logical_replication_workers``
    - integer
    - PostgreSQL maximum logical replication workers (taken from the pool of ``max_parallel_workers``)
  * - ``pg.max_parallel_workers``
    - integer
    - Maximum number of workers that the system can support for parallel queries
  * - ``pg.max_parallel_workers_per_gather``
    - integer
    - Maximum number of workers that can be started by a single ``Gather`` or ``Gather Merge`` node
  * - ``pg.max_pred_locks_per_transaction``
    - integer
    - Maximum predicate locks per transaction
  * - ``pg.max_prepared_transactions``
    - integer
    - Maximum prepared transactions
  * - ``pg.max_replication_slots``
    - integer
    - Maximum replication slots
  * - ``pg.max_stack_depth``
    - integer
    - Maximum depth of the stack in bytes
  * - ``pg.max_standby_archive_delay``
    - integer
    - Maximum standby archive delay in milliseconds
  * - ``pg.max_standby_streaming_delay``
    - integer
    - Maximum standby streaming delay in milliseconds
  * - ``pg.max_wal_senders``
    - integer
    - Maximum WAL senders
  * - ``pg.max_worker_processes``
    - integer
    - Maximum number of background processes that the system can support
  * - ``pg.pg_partman_bgw.interval``
    - integer
    - Time interval between ``pg_partman``'s scheduled tasks
  * - ``pg.pg_partman_bgw.role``
    - string
    - Controls which role to use for ``pg_partman``'s scheduled background tasks.
  * - ``pg.pg_stat_statements.track``
    - string
    - Controls which statements are counted. Specify ``top`` to track top-level statements (those issued directly by clients), ``all`` to also track nested statements (such as statements invoked within functions), or ``none`` to disable statement statistics collection.

      The default value is: `top``

      A valid range is: ``top``, ``all``, ``none``
  * - ``pg.temp_file_limit``
    - integer
    - Temporary file limit in KiB, -1 for unlimited
  * - ``pg.timezone``
    - string
    - Service timezone
  * - ``pg.track_activity_query_size``
    - integer
    - Number of bytes reserved to track the currently executing command for each active session.
  * - ``pg.track_commit_timestamp``
    - string
    - Recording of transactions commit time.
  * - ``pg.track_functions``
    - string
    - Tracking of function call counts and time used.
  * - ``pg.track_io_timing``
    - string
    - Timing of database I/O calls. The parameter is off by default, because it will repeatedly query the operating system for the current time, which may cause significant overhead on some platforms.

      The default value is: ``off``
  * - ``pg.wal_sender_timeout``
    - integer
    - Terminate replication connections that are inactive for longer than this amount of time, in milliseconds. Setting this value to zero disables the timeout.
  * - ``pg.wal_writer_delay``
    - integer
    - ``WAL`` flush interval in milliseconds. Note that setting this value to lower than the default ``200ms`` may negatively impact performance.

      The default value is: ``200ms``
  * - ``pg_read_replica``
    - boolean
    - Defines the forked service as a read replica: The setting is **deprecated**. Use read-replica service integration instead.
  * - ``pg_service_to_fork_from``
    - string
    - Name of the PG Service from which to fork. The setting is **deprecated**, use ``service_to_fork_from``).
  * - ``project_to_fork_from``
    - string
    - Name of another project to fork a service from. It has effect only when a new service is being created.
  * - ``pg_version``
    - string
    - PostgreSQL major version
  * - ``private_access.pg``
    - boolean
    - Allow clients to connect to PostgreSQL with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations
  * - ``private_access.prometheus``
    - boolean
    - Allow clients to connect to Prometheus with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations
  * - ``privatelink_access.pg``
    - boolean
    - Enable PostgreSQL over private link
  * - ``public_access.pg``
    - boolean
    - Allow clients to connect to pg from the public internet for service nodes that are in a project VPC or another type of private network
  * - ``public_access.prometheus``
    - boolean
    - Allow clients to connect to Prometheus from the public internet for service nodes that are in a project VPC or another type of private network
  * - ``recovery_target_time``
    - string
    - Recovery target time when forking a service. It has effect only when a new service is being created.
  * - ``service_to_fork_from``
    - string
    - Name of another service to fork from. This has effect only when a new service is being created.
  * - ``shared_buffers_percentage``
    - number
    - Percentage of total RAM that the database server uses for shared memory buffers. Valid range is 20-60 (float), which corresponds to 20% - 60%. This setting adjusts the shared_buffers configuration value.

      A valid range is: 20-60 (float)
  * - ``static_ips``
    - boolean
    - Static IP addresses: Use static public IP addresses
  * - ``synchronous_replication``
    - string
    - Enables synchronous replication type. Note that the service plan also needs to support synchronous replication.
  * - ``timescaledb.max_background_workers``
    - integer
    - The number of background workers for ``timescaledb`` operations. You should configure this setting to the sum of your number of databases and the total number of concurrent background workers you want running at any given point in time.
  * - ``variant``
    - string
    - Variant of the PostgreSQL service, may affect the features that are exposed by default
  * - ``work_mem``
    - integer
    - Sets the maximum amount of memory to be used by a query operation (such as a sort or hash table) before writing to temporary disk files, in MB.

      Default is 1MB + 0.075% of total RAM (up to 32MB).

Migration parameters
--------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``--remove-option migration``
    - Removes migration option
    -
  * - ``migration.dbname``
    - string
    - Database name for bootstrapping the initial connection
  * - ``migration.host``
    - string
    - Hostname or IP address of the server where to migrate data from
  * - ``migration.ignore_dbs``
    - string
    - Comma-separated list of databases, which should be ignored during migration (supported by MySQL only at the moment)
  * - ``migration.password``
    - string
    - Password for authentication with the server where to migrate data from
  * - ``migration.port``
    - integer
    - Port number of the server where to migrate data from
  * - ``migration.ssl``
    - boolean
    - ``True`` if the server where to migrate data from is secured with SSL
  * - ``migration.username``
    - string
    - User name for authentication with the server where to migrate data from

``autovacuum`` parameters
-------------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``pg.autovacuum_analyze_scale_factor``
    - number
    - The fraction of the table size to add to ``autovacuum_analyze_threshold`` when deciding whether to trigger an ``ANALYZE``.

      The default value is: 0.2 (20% of table size)

      A valid range is: 0-1
  * - ``pg.autovacuum_analyze_threshold``
    - integer
    - Minimum number of inserted, updated or deleted tuples needed to trigger an ``ANALYZE`` in any one table.

      The default value is: 50
  * - ``pg.autovacuum_freeze_max_age``
    - integer
    - Maximum age (in transactions) that a table's ``pg_class.relfrozenxid`` field can attain before a ``VACUUM`` operation is forced to prevent transaction ID wraparound within the table. Note that the system will launch ``autovacuum`` processes to prevent wraparound even when ``autovacuum`` is otherwise disabled. This parameter will cause the server to be restarted.
  * - ``pg.autovacuum_max_workers``
    - integer
    - Maximum number of ``autovacuum`` processes (other than the ``autovacuum`` launcher) that may be running at any one time. This parameter can only be set at server start.

      The default value is: 3
  * - ``pg.autovacuum_naptime``
    - integer
    - Minimum delay between ``autovacuum`` runs on any given database. The delay is measured in seconds.

      The default value is: 60
  * - ``pg.autovacuum_vacuum_cost_delay``
    - integer
    - Cost delay value that will be used in automatic ``VACUUM`` operations. If -1 is specified, the regular ``vacuum_cost_delay`` value will be used.

      The default value is: 20
  * - ``pg.autovacuum_vacuum_cost_limit``
    - integer
    - Cost limit value that will be used in automatic ``VACUUM`` operations. If -1 is specified, the regular ``vacuum_cost_limit`` value will be used.

      The default value is: -1
  * - ``pg.autovacuum_vacuum_scale_factor``
    - number
    - The fraction of the table size to add to ``autovacuum_vacuum_threshold`` when deciding whether to trigger a ``VACUUM``.

      The default value is: 0.2 (20% of table size)

      A valid range is: 0-1
  * - ``pg.autovacuum_vacuum_threshold``
    - integer
    - Minimum number of updated or deleted tuples needed to trigger a VACUUM in any one table.

      The default value is: 50
  * - ``pg.log_autovacuum_min_duration``
    - integer
    - Causes each action executed by ``autovacuum`` to be logged if it ran for at least the specified number of milliseconds. Setting this to zero logs all ``autovacuum`` actions. -1 (the default) disables logging ``autovacuum`` actions.

      The default value is: -1


``bgwriter`` parameters
-----------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``pg.bgwriter_delay``
    - integer
    - Specifies the delay between activity rounds for the background writer in milliseconds.

      The default value is: 200
  * - ``pg.bgwriter_flush_after``
    - integer
    - Whenever more than ``bgwriter_flush_after`` bytes have been written by the background writer, attempt to force the OS to issue these writes to the underlying storage. Specified in kilobytes, Setting of 0 disables forced write-back.

      The default value is: 512 (kilobytes)
  * - ``pg.bgwriter_lru_maxpages``
    - integer
    - Maximum number of buffers to be written by the background writer on each round. Setting this to zero disables background writing.

      The default value is: 100
  * - ``pg.bgwriter_lru_multiplier``
    - number
    - The average recent need for new buffers is multiplied by ``bgwriter_lru_multiplier`` to arrive at an estimate of the number that will be needed during the next round, (up to ``bgwriter_lru_maxpages``). 1.0 represents a “just in time” policy of writing exactly the number of buffers predicted to be needed. Larger values provide some cushion against spikes in demand, while smaller values intentionally leave writes to be done by server processes.

      The default value is: 2.0

``pgbouncer`` parameters
------------------------

.. list-table::
  :header-rows: 1

  * - Parameter
    - Value Type
    - Description
  * - ``pgbouncer.autodb_idle_timeout``
    - integer
    - If the automatically created database pools have been unused this many seconds, they are freed. If 0 then timeout is disabled.
  * - ``pgbouncer.autodb_max_db_connections``
    - integer
    - Overall Maximum number of server connections per database (regardless of user). Setting it to 0 means unlimited.
  * - ``pgbouncer.autodb_pool_mode``
    - string
    - ``PGBouncer`` pool mode: with ``session`` the server is released back to pool after client disconnects. With ``transaction`` the server is released back to pool after transaction finishes. With ``statement`` the server is released back to pool after query finishes (transactions spanning multiple statements are disallowed in this mode).

      The default value is: ``session`` A valid range is: ``session``, ``transaction``, ``statement``
  * - ``pgbouncer.autodb_pool_size``
    - integer
    - If non-zero creates automatically a pool of that size per user when a pool doesn't exist.
  * - ``pgbouncer.ignore_startup_parameters``
    - array
    - List of parameters to ignore when given in startup packet
  * - ``pgbouncer.min_pool_size``
    - integer
    - Add more server connections to pool if below this number. Improves behavior when usual load comes suddenly back after period of total inactivity. The value is capped at the pool size.
  * - ``pgbouncer.server_idle_timeout``
    - integer
    - If a server connection has been idle more than this many seconds it will be dropped. If 0 then timeout is disabled.
  * - ``pgbouncer.server_lifetime``
    - integer
    - The pooler will close an unused server connection that has been connected longer than this.
  * - ``pgbouncer.server_reset_query_always``
    - boolean
    - Run ``server_reset_query`` (``DISCARD ALL``) in all pooling modes
  * - ``pglookout.max_failover_replication_time_lag``
    - integer
    -  Number of seconds of master unavailability before triggering database failover to standby.

       The default value is: 60
  * - ``private_access.pgbouncer``
    - boolean
    - Allow clients to connect to ``pgbouncer`` with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations
  * - ``privatelink_access.pgbouncer``
    - boolean
    - Enable ``PGbouncer`` over a private link
  * - ``public_access.pgbouncer``
    - boolean
    - Allows clients to connect to `PGbouncer`` from the public internet for service nodes that are in a project VPC or another type of private network
