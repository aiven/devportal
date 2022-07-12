
``ip_filter`` => *array*
  **IP filter** Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'



``static_ips`` => *boolean*
  **Static IP addresses** Use static public IP addresses



``admin_username`` => *['string', 'null']*
  **Custom username for admin user. This must be set only when a new service is being created.** 



``admin_password`` => *['string', 'null']*
  **Custom password for admin user. Defaults to random string. This must be set only when a new service is being created.** 



``backup_hour`` => *['integer', 'null']*
  **The hour of day (in UTC) when backup for the service is started. New backup is only started if previous backup has already completed.** 



``backup_minute`` => *['integer', 'null']*
  **The minute of an hour when backup for the service is started. New backup is only started if previous backup has already completed.** 



``migration`` => *['object', 'null']*
  **Migrate data from existing server** 



``private_access`` => *object*
  **Allow access to selected service ports from private networks** 

  ``mysql`` => *boolean*
    **Allow clients to connect to mysql with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 

  ``mysqlx`` => *boolean*
    **Allow clients to connect to mysqlx with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 

  ``prometheus`` => *boolean*
    **Allow clients to connect to prometheus with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** 



``privatelink_access`` => *object*
  **Allow access to selected service components through Privatelink** 

  ``mysql`` => *boolean*
    **Enable mysql** 

  ``mysqlx`` => *boolean*
    **Enable mysqlx** 

  ``prometheus`` => *boolean*
    **Enable prometheus** 



``public_access`` => *object*
  **Allow access to selected service ports from the public Internet** 

  ``mysql`` => *boolean*
    **Allow clients to connect to mysql from the public internet for service nodes that are in a project VPC or another type of private network** 

  ``mysqlx`` => *boolean*
    **Allow clients to connect to mysqlx from the public internet for service nodes that are in a project VPC or another type of private network** 

  ``prometheus`` => *boolean*
    **Allow clients to connect to prometheus from the public internet for service nodes that are in a project VPC or another type of private network** 



``service_to_fork_from`` => *['string', 'null']*
  **Name of another service to fork from. This has effect only when a new service is being created.** 



``project_to_fork_from`` => *['string', 'null']*
  **Name of another project to fork a service from. This has effect only when a new service is being created.** 



``mysql_version`` => *['string', 'null']*
  **MySQL major version** 



``recovery_target_time`` => *['string', 'null']*
  **Recovery target time when forking a service. This has effect only when a new service is being created.** 



``binlog_retention_period`` => *integer*
  **The minimum amount of time in seconds to keep binlog entries before deletion. This may be extended for services that require binlog entries for longer than the default for example if using the MySQL Debezium Kafka connector.** 



``mysql`` => *object*
  **mysql.conf configuration values** 

  ``sql_mode`` => *string*
    **sql_mode** Global SQL mode. Set to empty to use MySQL server defaults. When creating a new service and not setting this field Aiven default SQL mode (strict, SQL standard compliant) will be assigned.

  ``connect_timeout`` => *integer*
    **connect_timeout** The number of seconds that the mysqld server waits for a connect packet before responding with Bad handshake

  ``default_time_zone`` => *string*
    **default_time_zone** Default server time zone as an offset from UTC (from -12:00 to +12:00), a time zone name, or 'SYSTEM' to use the MySQL server default.

  ``group_concat_max_len`` => *integer*
    **group_concat_max_len** The maximum permitted result length in bytes for the GROUP_CONCAT() function.

  ``information_schema_stats_expiry`` => *integer*
    **information_schema_stats_expiry** The time, in seconds, before cached statistics expire

  ``innodb_change_buffer_max_size`` => *integer*
    **innodb_change_buffer_max_size** Maximum size for the InnoDB change buffer, as a percentage of the total size of the buffer pool. Default is 25

  ``innodb_flush_neighbors`` => *integer*
    **innodb_flush_neighbors** Specifies whether flushing a page from the InnoDB buffer pool also flushes other dirty pages in the same extent (default is 1): 0 - dirty pages in the same extent are not flushed,  1 - flush contiguous dirty pages in the same extent,  2 - flush dirty pages in the same extent

  ``innodb_ft_min_token_size`` => *integer*
    **innodb_ft_min_token_size** Minimum length of words that are stored in an InnoDB FULLTEXT index. Changing this parameter will lead to a restart of the MySQL service.

  ``innodb_ft_server_stopword_table`` => *['null', 'string']*
    **innodb_ft_server_stopword_table** This option is used to specify your own InnoDB FULLTEXT index stopword list for all InnoDB tables.

  ``innodb_lock_wait_timeout`` => *integer*
    **innodb_lock_wait_timeout** The length of time in seconds an InnoDB transaction waits for a row lock before giving up.

  ``innodb_log_buffer_size`` => *integer*
    **innodb_log_buffer_size** The size in bytes of the buffer that InnoDB uses to write to the log files on disk.

  ``innodb_online_alter_log_max_size`` => *integer*
    **innodb_online_alter_log_max_size** The upper limit in bytes on the size of the temporary log files used during online DDL operations for InnoDB tables.

  ``innodb_print_all_deadlocks`` => *boolean*
    **innodb_print_all_deadlocks** When enabled, information about all deadlocks in InnoDB user transactions is recorded in the error log. Disabled by default.

  ``innodb_read_io_threads`` => *integer*
    **innodb_read_io_threads** The number of I/O threads for read operations in InnoDB. Default is 4. Changing this parameter will lead to a restart of the MySQL service.

  ``innodb_rollback_on_timeout`` => *boolean*
    **innodb_rollback_on_timeout** When enabled a transaction timeout causes InnoDB to abort and roll back the entire transaction. Changing this parameter will lead to a restart of the MySQL service.

  ``innodb_thread_concurrency`` => *integer*
    **innodb_thread_concurrency** Defines the maximum number of threads permitted inside of InnoDB. Default is 0 (infinite concurrency - no limit)

  ``innodb_write_io_threads`` => *integer*
    **innodb_write_io_threads** The number of I/O threads for write operations in InnoDB. Default is 4. Changing this parameter will lead to a restart of the MySQL service.

  ``interactive_timeout`` => *integer*
    **interactive_timeout** The number of seconds the server waits for activity on an interactive connection before closing it.

  ``internal_tmp_mem_storage_engine`` => *string*
    **internal_tmp_mem_storage_engine** The storage engine for in-memory internal temporary tables.

  ``net_buffer_length`` => *integer*
    **net_buffer_length** Start sizes of connection buffer and result buffer. Default is 16384 (16K). Changing this parameter will lead to a restart of the MySQL service.

  ``net_read_timeout`` => *integer*
    **net_read_timeout** The number of seconds to wait for more data from a connection before aborting the read.

  ``net_write_timeout`` => *integer*
    **net_write_timeout** The number of seconds to wait for a block to be written to a connection before aborting the write.

  ``sql_require_primary_key`` => *boolean*
    **sql_require_primary_key** Require primary key to be defined for new tables or old tables modified with ALTER TABLE and fail if missing. It is recommended to always have primary keys because various functionality may break if any large table is missing them.

  ``wait_timeout`` => *integer*
    **wait_timeout** The number of seconds the server waits for activity on a noninteractive connection before closing it.

  ``max_allowed_packet`` => *integer*
    **max_allowed_packet** Size of the largest message in bytes that can be received by the server. Default is 67108864 (64M)

  ``max_heap_table_size`` => *integer*
    **max_heap_table_size** Limits the size of internal in-memory tables. Also set tmp_table_size. Default is 16777216 (16M)

  ``sort_buffer_size`` => *integer*
    **sort_buffer_size** Sort buffer size in bytes for ORDER BY optimization. Default is 262144 (256K)

  ``tmp_table_size`` => *integer*
    **tmp_table_size** Limits the size of internal in-memory tables. Also set max_heap_table_size. Default is 16777216 (16M)

  ``slow_query_log`` => *boolean*
    **slow_query_log** Slow query log enables capturing of slow queries. Setting slow_query_log to false also truncates the mysql.slow_log table. Default is off

  ``long_query_time`` => *number*
    **long_query_time** The slow_query_logs work as SQL statements that take more than long_query_time seconds to execute. Default is 10s



