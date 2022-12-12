Aiven Service metrics
=====================

Aiven platform provides service metrics integrations to monitor the
states of your Aiven services. It helps you to quickly get to the bottom
of performance issues, as well as anticipate and prevent future
problems.

By default, our service integrations enable a pre-defined set of service
metrics to be monitored. They are listed below by service type. In
addition, we also collect many more metrics that are not configured by
default. Please visit  :doc:`this article </docs/platform/howto/additional-service-metrics>`
to read more about the additional metrics available.


**Default set of metrics available for all service types**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  metric: cpu, field: usage_iowait

-  metric: cpu, field: usage_irq

-  metric: cpu, field: usage_system

-  metric: cpu, field: usage_user

-  metric: disk, field: free

-  metric: diskio, field: read_bytes

-  metric: diskio, field: write_bytes

-  metric: disk, field: used

-  metric: kernel, field: context_switches

-  metric: kernel, field: interrupts

-  metric: mem, field: available

-  metric: mem, field: free

-  metric: mem, field: used

-  metric: net, field: bytes_recv

-  metric: net, field: bytes_sent

-  metric: netstat, field: tcp_close

-  metric: netstat, field: tcp_close_wait

-  metric: netstat, field: tcp_closing

-  metric: netstat, field: tcp_established

-  metric: netstat, field: tcp_fin_wait1

-  metric: netstat, field: tcp_fin_wait2

-  metric: netstat, field: tcp_last_ack

-  metric: processes, field: blocked

-  metric: processes, field: paging

-  metric: processes, field: running

-  metric: processes, field: zombies

-  metric: system, field: load1

-  metric: system, field: uptime

.. _h_c4d3a90477:

Default metrics for Aiven for PostgreSQL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  metric: postgresql.database_size, field: database_size

-  metric: postgresql.pg_stat_activity, field: conn_count

-  metric: postgresql.pg_stat_activity, field: oldest_conn_age

-  metric: postgresql.pg_stat_activity, field: oldest_running_query_age

-  metric: postgresql.pg_stat_database, field: blks_hit

-  metric: postgresql.pg_stat_database, field: blks_read

-  metric: postgresql.pg_stat_database, field: deadlocks

-  metric: postgresql.pg_stat_database, field: temp_bytes

-  metric: postgresql.pg_stat_database, field: temp_files

-  metric: postgresql.pg_stat_database, field: xact_commit

-  metric: postgresql.pg_stat_database, field: xact_rollback

-  metric: postgresql.transactions, field: freeze_limit

-  metric: postgresql.transactions, field: txns

.. _h_ea73f647b3:

Default metrics for Aiven for Apache Kafka
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  metric: java.lang:GarbageCollector.G1_Young_Generation, field:
   CollectionCount

-  metric: java.lang:GarbageCollector.G1_Young_Generation, field:
   CollectionTime

-  metric: java.lang:Memory, field: used

-  metric: kafka.controller:ControllerStats.LeaderElectionRateAndTimeMs,
   field: Count

-  metric: kafka.controller:ControllerStats.LeaderElectionRateAndTimeMs,
   field: OneMinuteRate

-  metric:
   kafka.controller:ControllerStats.UncleanLeaderElectionsPerSec, field:
   Count

-  metric: kafka.network:RequestMetrics.RequestsPerSec, field: Count

-  metric: kafka.network:SocketServer.NetworkProcessorAvgIdlePercent,
   field: Value

-  metric: kafka.server:BrokerTopicMetrics.BytesInPerSec, field: Count

-  metric: kafka.server:BrokerTopicMetrics.BytesOutPerSec, field: Count

-  metric: kafka.server:BrokerTopicMetrics.FailedFetchRequestsPerSec,
   field: Count

-  metric: kafka.server:BrokerTopicMetrics.MessagesInPerSec, field:
   Count

-  metric: kafka.server:DelayedOperationPurgatory.NumDelayedOperations,
   field: Value

-  metric: kafka.server:DelayedOperationPurgatory.PurgatorySize, field:
   Value

-  metric:
   kafka.server:KafkaRequestHandlerPool.RequestHandlerAvgIdlePercent,
   field: OneMinuteRate

-  metric: kafka.server:ReplicaManager.IsrExpandsPerSec, field: Count

-  metric: kafka.server:ReplicaManager.IsrShrinksPerSec, field: Count

-  metric: kafka.server:ReplicaManager.UnderReplicatedPartitions, field:
   Value

.. _h_69fbc93a86:

Default metrics for Aiven for Redis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  metric: redis, field: clients

-  metric: redis, field: evicted_keys

-  metric: redis, field: expired_keys

-  metric: redis, field: keyspace_hitrate

-  metric: redis, field: keyspace_hits

-  metric: redis, field: keyspace_misses

-  metric: redis, field: maxmemory

-  metric: redis, field: mem_fragmentation_ratio

-  metric: redis, field: pubsub_channels

-  metric: redis, field: pubsub_patterns

-  metric: redis, field: rejected_connections

-  metric: redis, field: total_commands_processed

-  metric: redis, field: uptime

-  metric: redis, field: used_memory

-  metric: redis, field: used_memory_dataset

-  metric: redis, field: used_memory_lua

.. _h_496fd8fd55:

Default metrics for Aiven for Cassandra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  metric: java.lang:GarbageCollector.G1_Young_Generation, field:
   CollectionCount

-  metric: java.lang:GarbageCollector.G1_Young_Generation, field:
   CollectionTime

-  metric: java.lang:Memory, field: used

-  metric: org.apache.cassandra.metrics:Cache.Entries, field: Value

-  metric: org.apache.cassandra.metrics:Cache.HitRate, field: Value

-  metric: org.apache.cassandra.metrics:Cache.MissLatency, field:
   95thPercentile

-  metric: org.apache.cassandra.metrics:Cache.MissLatency, field:
   99thPercentile

-  metric: org.apache.cassandra.metrics:Cache.MissLatency, field: Count

-  metric: org.apache.cassandra.metrics:Cache.Size, field: Value

-  metric: org.apache.cassandra.metrics:Client.connectedNativeClients,
   field: Value

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.AllMemtablesLiveDataSize,
   field: Value

-  metric: org.apache.cassandra.metrics:ColumnFamily.CompressionRatio,
   field: Value

-  metric: org.apache.cassandra.metrics:ColumnFamily.EstimatedRowCount,
   field: Value

-  metric: org.apache.cassandra.metrics:ColumnFamily.LiveSSTableCount,
   field: Value

-  metric: org.apache.cassandra.metrics:ColumnFamily.MaxRowSize, field:
   Value

-  metric: org.apache.cassandra.metrics:ColumnFamily.MeanRowSize, field:
   Value

-  metric: org.apache.cassandra.metrics:ColumnFamily.PendingCompactions,
   field: Value

-  metric: org.apache.cassandra.metrics:CommitLog.PendingTasks, field:
   Value

-  metric: org.apache.cassandra.metrics:CommitLog.TotalCommitLogSize,
   field: Value

-  metric: org.apache.cassandra.metrics:CommitLog.WaitingOnCommit,
   field: 95thPercentile

-  metric: org.apache.cassandra.metrics:CommitLog.WaitingOnCommit,
   field: 99thPercentile

-  metric: org.apache.cassandra.metrics:CommitLog.WaitingOnCommit,
   field: Count

-  metric:
   org.apache.cassandra.metrics:CommitLog.WaitingOnSegmentAllocation,
   field: 95thPercentile

-  metric:
   org.apache.cassandra.metrics:CommitLog.WaitingOnSegmentAllocation,
   field: 99thPercentile

-  metric:
   org.apache.cassandra.metrics:CommitLog.WaitingOnSegmentAllocation,
   field: Count

-  metric: org.apache.cassandra.metrics:Storage.TotalHints, field: Count

-  metric: org.apache.cassandra.metrics:ThreadPools.ActiveTasks, field:
   Value

-  metric:
   org.apache.cassandra.metrics:ThreadPools.CurrentlyBlockedTasks,
   field: Count

-  metric: org.apache.cassandra.metrics:ThreadPools.PendingTasks, field:
   Value

.. _h_4727d2e5e5:

Default metrics for Aiven for MySQL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  metric: mysql, field: bytes_sent

-  metric: mysql, field: connection_errors_max_connections

-  metric: mysql, field: connections

-  metric: mysql_innodb, field: file_num_open_files

-  metric: mysql_innodb, field: lock_deadlocks

-  metric: mysql_innodb, field: lock_row_lock_time_avg

-  metric: mysql_innodb, field: os_data_reads

-  metric: mysql_innodb, field: os_data_writes

-  metric: mysql, field: max_execution_time_exceeded

-  metric: mysql, field: open_tables

-  metric: mysql, field: slow_queries

-  metric: mysql, field: table_locks_immediate

-  metric: mysql, field: table_locks_waited

-  metric: mysql, field: uptime

-  metric: mysql_users, field: connections

.. _h_a343500a39:

Default metrics for Aiven for Elasticsearch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  metric: elasticsearch_cluster_health, field: active_primary_shards

-  metric: elasticsearch_cluster_health, field: active_shards

-  metric: elasticsearch_cluster_health, field: initializing_shards

-  metric: elasticsearch_cluster_health, field: number_of_pending_tasks

-  metric: elasticsearch_cluster_health, field: relocating_shards

-  metric: elasticsearch_cluster_health, field: status_code

-  metric: elasticsearch_cluster_health, field:
   task_max_waiting_in_queue_millis

-  metric: elasticsearch_cluster_health, field: unassigned_shards

-  metric: elasticsearch_clusterstats_indices, field: count

-  metric: elasticsearch_clusterstats_indices, field: docs_count

-  metric: elasticsearch_clusterstats_indices, field: docs_deleted

-  metric: elasticsearch_clusterstats_indices, field:
   store_size_in_bytes

-  metric: elasticsearch_http, field: current_open

-  metric: elasticsearch_http, field: total_opened

-  metric: elasticsearch_indices, field: docs_count

-  metric: elasticsearch_indices, field: docs_deleted

-  metric: elasticsearch_indices, field: store_size_in_bytes

-  metric: elasticsearch_jvm, field: gc_collectors_old_collection_count

-  metric: elasticsearch_jvm, field:
   gc_collectors_old_collection_time_in_millis

-  metric: elasticsearch_jvm, field:
   gc_collectors_young_collection_count

-  metric: elasticsearch_jvm, field:
   gc_collectors_young_collection_time_in_millis

-  metric: elasticsearch_jvm, field: mem_heap_used_percent

-  metric: elasticsearch_transport, field: rx_size_in_bytes

-  metric: elasticsearch_transport, field: tx_size_in_bytes