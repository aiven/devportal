
``migration`` => *['object', 'null']*
  **Migrate data from existing server** 



``ip_filter`` => *array*
  **IP filter** Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'



``static_ips`` => *boolean*
  **Static IP addresses** Use static public IP addresses



``enable_ipv6`` => *boolean*
  **Enable IPv6** Register AAAA DNS records for the service, and allow IPv6 packets to service ports



``admin_username`` => *['string', 'null']*
  **Custom username for admin user. This must be set only when a new service is being created.** 



``admin_password`` => *['string', 'null']*
  **Custom password for admin user. Defaults to random string. This must be set only when a new service is being created.** 



``backup_hour`` => *['integer', 'null']*
  **The hour of day (in UTC) when backup for the service is started. New backup is only started if previous backup has already completed.** 



``backup_minute`` => *['integer', 'null']*
  **The minute of an hour when backup for the service is started. New backup is only started if previous backup has already completed.** 



``pglookout`` => *object*
  **PGLookout settings** 

  ``max_failover_replication_time_lag`` => *integer*
    **max_failover_replication_time_lag** Number of seconds of master unavailability before triggering database failover to standby



``pg_service_to_fork_from`` => *['string', 'null']*
  **Name of the PG Service from which to fork (deprecated, use service_to_fork_from). This has effect only when a new service is being created.** 



``service_to_fork_from`` => *['string', 'null']*
  **Name of another service to fork from. This has effect only when a new service is being created.** 



``project_to_fork_from`` => *['string', 'null']*
  **Name of another project to fork a service from. This has effect only when a new service is being created.** 



``synchronous_replication`` => *string*
  **Synchronous replication type. Note that the service plan also needs to support synchronous replication.** 



``pg_read_replica`` => *['boolean', 'null']*
  **Should the service which is being forked be a read replica (deprecated, use read_replica service integration instead).** This setting is deprecated. Use read_replica service integration instead.



``pg_version`` => *['string', 'null']*
  **PostgreSQL major version** 



``pgbouncer`` => *object*
  **PGBouncer connection pooling settings** 

  ``server_reset_query_always`` => *boolean*
    **Run server_reset_query (DISCARD ALL) in all pooling modes** 

  ``ignore_startup_parameters`` => *array*
    **List of parameters to ignore when given in startup packet** 

  ``min_pool_size`` => *integer*
    **Add more server connections to pool if below this number. Improves behavior when usual load comes suddenly back after period of total inactivity. The value is effectively capped at the pool size.** 

  ``server_lifetime`` => *integer*
    **The pooler will close an unused server connection that has been connected longer than this. [seconds]** 

  ``server_idle_timeout`` => *integer*
    **If a server connection has been idle more than this many seconds it will be dropped. If 0 then timeout is disabled. [seconds]** 

  ``autodb_pool_size`` => *integer*
    **If non-zero then create automatically a pool of that size per user when a pool doesn't exist.** 

  ``autodb_pool_mode`` => *string*
    **PGBouncer pool mode** 

  ``autodb_max_db_connections`` => *integer*
    **Do not allow more than this many server connections per database (regardless of user). Setting it to 0 means unlimited.** 

  ``autodb_idle_timeout`` => *integer*
    **If the automatically created database pools have been unused this many seconds, they are freed. If 0 then timeout is disabled. [seconds]** 



``recovery_target_time`` => *['string', 'null']*
  **Recovery target time when forking a service. This has effect only when a new service is being created.** 



``variant`` => *['string', 'null']*
  **Variant of the PostgreSQL service, may affect the features that are exposed by default** 



``private_access`` => *object*
  **Allow access to selected service ports from private networks** 

  ``pg`` => *boolean*
    **Allow clients to connect to pg with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 

  ``pgbouncer`` => *boolean*
    **Allow clients to connect to pgbouncer with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 

  ``prometheus`` => *boolean*
    **Allow clients to connect to prometheus with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 



``privatelink_access`` => *object*
  **Allow access to selected service components through Privatelink** 

  ``pg`` => *boolean*
    **Enable pg** 

  ``pgbouncer`` => *boolean*
    **Enable pgbouncer** 

  ``prometheus`` => *boolean*
    **Enable prometheus** 



``public_access`` => *object*
  **Allow access to selected service ports from the public Internet** 

  ``pg`` => *boolean*
    **Allow clients to connect to pg from the public internet for service nodes that are in a project VPC or another type of private network** 

  ``pgbouncer`` => *boolean*
    **Allow clients to connect to pgbouncer from the public internet for service nodes that are in a project VPC or another type of private network** 

  ``prometheus`` => *boolean*
    **Allow clients to connect to prometheus from the public internet for service nodes that are in a project VPC or another type of private network** 



``pg`` => *object*
  **postgresql.conf configuration values** 

  ``autovacuum_freeze_max_age`` => *integer*
    **autovacuum_freeze_max_age** Specifies the maximum age (in transactions) that a table's pg_class.relfrozenxid field can attain before a VACUUM operation is forced to prevent transaction ID wraparound within the table. Note that the system will launch autovacuum processes to prevent wraparound even when autovacuum is otherwise disabled. This parameter will cause the server to be restarted.

  ``autovacuum_max_workers`` => *integer*
    **autovacuum_max_workers** Specifies the maximum number of autovacuum processes (other than the autovacuum launcher) that may be running at any one time. The default is three. This parameter can only be set at server start.

  ``autovacuum_naptime`` => *integer*
    **autovacuum_naptime** Specifies the minimum delay between autovacuum runs on any given database. The delay is measured in seconds, and the default is one minute

  ``autovacuum_vacuum_threshold`` => *integer*
    **autovacuum_vacuum_threshold** Specifies the minimum number of updated or deleted tuples needed to trigger a VACUUM in any one table. The default is 50 tuples

  ``autovacuum_analyze_threshold`` => *integer*
    **autovacuum_analyze_threshold** Specifies the minimum number of inserted, updated or deleted tuples needed to trigger an  ANALYZE in any one table. The default is 50 tuples.

  ``autovacuum_vacuum_scale_factor`` => *number*
    **autovacuum_vacuum_scale_factor** Specifies a fraction of the table size to add to autovacuum_vacuum_threshold when deciding whether to trigger a VACUUM. The default is 0.2 (20% of table size)

  ``autovacuum_analyze_scale_factor`` => *number*
    **autovacuum_analyze_scale_factor** Specifies a fraction of the table size to add to autovacuum_analyze_threshold when deciding whether to trigger an ANALYZE. The default is 0.2 (20% of table size)

  ``autovacuum_vacuum_cost_delay`` => *integer*
    **autovacuum_vacuum_cost_delay** Specifies the cost delay value that will be used in automatic VACUUM operations. If -1 is specified, the regular vacuum_cost_delay value will be used. The default value is 20 milliseconds

  ``autovacuum_vacuum_cost_limit`` => *integer*
    **autovacuum_vacuum_cost_limit** Specifies the cost limit value that will be used in automatic VACUUM operations. If -1 is specified (which is the default), the regular vacuum_cost_limit value will be used.

  ``bgwriter_delay`` => *integer*
    **bgwriter_delay** Specifies the delay between activity rounds for the background writer in milliseconds. Default is 200.

  ``bgwriter_flush_after`` => *integer*
    **bgwriter_flush_after** Whenever more than bgwriter_flush_after bytes have been written by the background writer, attempt to force the OS to issue these writes to the underlying storage. Specified in kilobytes, default is 512. Setting of 0 disables forced writeback.

  ``bgwriter_lru_maxpages`` => *integer*
    **bgwriter_lru_maxpages** In each round, no more than this many buffers will be written by the background writer. Setting this to zero disables background writing. Default is 100.

  ``bgwriter_lru_multiplier`` => *number*
    **bgwriter_lru_multiplier** The average recent need for new buffers is multiplied by bgwriter_lru_multiplier to arrive at an estimate of the number that will be needed during the next round, (up to bgwriter_lru_maxpages). 1.0 represents a “just in time” policy of writing exactly the number of buffers predicted to be needed. Larger values provide some cushion against spikes in demand, while smaller values intentionally leave writes to be done by server processes. The default is 2.0.

  ``deadlock_timeout`` => *integer*
    **deadlock_timeout** This is the amount of time, in milliseconds, to wait on a lock before checking to see if there is a deadlock condition.

  ``default_toast_compression`` => *string*
    **default_toast_compression** Specifies the default TOAST compression method for values of compressible columns (the default is lz4).

  ``idle_in_transaction_session_timeout`` => *integer*
    **idle_in_transaction_session_timeout** Time out sessions with open transactions after this number of milliseconds

  ``jit`` => *boolean*
    **jit** Controls system-wide use of Just-in-Time Compilation (JIT).

  ``log_autovacuum_min_duration`` => *integer*
    **log_autovacuum_min_duration** Causes each action executed by autovacuum to be logged if it ran for at least the specified number of milliseconds. Setting this to zero logs all autovacuum actions. Minus-one (the default) disables logging autovacuum actions.

  ``log_error_verbosity`` => *string*
    **log_error_verbosity** Controls the amount of detail written in the server log for each message that is logged.

  ``log_line_prefix`` => *string*
    **log_line_prefix** Choose from one of the available log-formats. These can support popular log analyzers like pgbadger, pganalyze etc.

  ``log_min_duration_statement`` => *integer*
    **log_min_duration_statement** Log statements that take more than this number of milliseconds to run, -1 disables

  ``max_files_per_process`` => *integer*
    **max_files_per_process** PostgreSQL maximum number of files that can be open per process

  ``max_prepared_transactions`` => *integer*
    **max_prepared_transactions** PostgreSQL maximum prepared transactions

  ``max_pred_locks_per_transaction`` => *integer*
    **max_pred_locks_per_transaction** PostgreSQL maximum predicate locks per transaction

  ``max_locks_per_transaction`` => *integer*
    **max_locks_per_transaction** PostgreSQL maximum locks per transaction

  ``max_slot_wal_keep_size`` => *integer*
    **max_slot_wal_keep_size** PostgreSQL maximum WAL size (MB) reserved for replication slots. Default is -1 (unlimited). wal_keep_size minimum WAL size setting takes precedence over this.

  ``max_stack_depth`` => *integer*
    **max_stack_depth** Maximum depth of the stack in bytes

  ``max_standby_archive_delay`` => *integer*
    **max_standby_archive_delay** Max standby archive delay in milliseconds

  ``max_standby_streaming_delay`` => *integer*
    **max_standby_streaming_delay** Max standby streaming delay in milliseconds

  ``max_replication_slots`` => *integer*
    **max_replication_slots** PostgreSQL maximum replication slots

  ``max_logical_replication_workers`` => *integer*
    **max_logical_replication_workers** PostgreSQL maximum logical replication workers (taken from the pool of max_parallel_workers)

  ``max_parallel_workers`` => *integer*
    **max_parallel_workers** Sets the maximum number of workers that the system can support for parallel queries

  ``max_parallel_workers_per_gather`` => *integer*
    **max_parallel_workers_per_gather** Sets the maximum number of workers that can be started by a single Gather or Gather Merge node

  ``max_worker_processes`` => *integer*
    **max_worker_processes** Sets the maximum number of background processes that the system can support

  ``pg_partman_bgw.role`` => *string*
    **pg_partman_bgw.role** Controls which role to use for pg_partman's scheduled background tasks.

  ``pg_partman_bgw.interval`` => *integer*
    **pg_partman_bgw.interval** Sets the time interval to run pg_partman's scheduled tasks

  ``pg_stat_statements.track`` => *['string']*
    **pg_stat_statements.track** Controls which statements are counted. Specify top to track top-level statements (those issued directly by clients), all to also track nested statements (such as statements invoked within functions), or none to disable statement statistics collection. The default value is top.

  ``temp_file_limit`` => *integer*
    **temp_file_limit** PostgreSQL temporary file limit in KiB, -1 for unlimited

  ``timezone`` => *string*
    **timezone** PostgreSQL service timezone

  ``track_activity_query_size`` => *integer*
    **track_activity_query_size** Specifies the number of bytes reserved to track the currently executing command for each active session.

  ``track_commit_timestamp`` => *string*
    **track_commit_timestamp** Record commit time of transactions.

  ``track_functions`` => *string*
    **track_functions** Enables tracking of function call counts and time used.

  ``track_io_timing`` => *string*
    **track_io_timing** Enables timing of database I/O calls. This parameter is off by default, because it will repeatedly query the operating system for the current time, which may cause significant overhead on some platforms.

  ``max_wal_senders`` => *integer*
    **max_wal_senders** PostgreSQL maximum WAL senders

  ``wal_sender_timeout`` => *integer*
    **wal_sender_timeout** Terminate replication connections that are inactive for longer than this amount of time, in milliseconds. Setting this value to zero disables the timeout.

  ``wal_writer_delay`` => *integer*
    **wal_writer_delay** WAL flush interval in milliseconds. Note that setting this value to lower than the default 200ms may negatively impact performance



``shared_buffers_percentage`` => *number*
  **shared_buffers_percentage** Percentage of total RAM that the database server uses for shared memory buffers. Valid range is 20-60 (float), which corresponds to 20% - 60%. This setting adjusts the shared_buffers configuration value.



``timescaledb`` => *object*
  **TimescaleDB extension configuration values** 

  ``max_background_workers`` => *integer*
    **timescaledb.max_background_workers** The number of background workers for timescaledb operations. You should configure this setting to the sum of your number of databases and the total number of concurrent background workers you want running at any given point in time.



``work_mem`` => *integer*
  **work_mem** Sets the maximum amount of memory to be used by a query operation (such as a sort or hash table) before writing to temporary disk files, in MB. Default is 1MB + 0.075% of total RAM (up to 32MB).



