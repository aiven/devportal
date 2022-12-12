Additional Service Metrics
==========================

Aiven platform provides service metrics integrations to monitor the
states of your Aiven services. It helps you to quickly get to the bottom
of performance issues, as well as anticipate and prevent future
problems.

To help you get started easily, our service integrations enable a
pre-defined set of service metrics to be monitored. This article lists
the additional metrics that are available for use. If you'd like to see
what's in the pre-defined list of metrics, please read :doc:`this article </docs/platform/howto/aiven-service-metrics>`.

Additional metrics available for all service types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  metric: cpu, field: usage_guest

-  metric: cpu, field: usage_guest_nice

-  metric: cpu, field: usage_idle

-  metric: cpu, field: usage_nice

-  metric: cpu, field: usage_softirq

-  metric: cpu, field: usage_steal

-  metric: disk, field: inodes_free

-  metric: disk, field: inodes_total

-  metric: disk, field: inodes_used

-  metric: diskio, field: iops_in_progress

-  metric: diskio, field: io_time

-  metric: diskio, field: merged_reads

-  metric: diskio, field: merged_writes

-  metric: diskio, field: reads

-  metric: diskio, field: read_time

-  metric: diskio, field: weighted_io_time

-  metric: diskio, field: writes

-  metric: diskio, field: write_time

-  metric: disk, field: total

-  metric: disk, field: used_percent

-  metric: kernel, field: boot_time

-  metric: kernel, field: entropy_avail

-  metric: kernel, field: processes_forked

-  metric: mem, field: active

-  metric: mem, field: available_percent

-  metric: mem, field: buffered

-  metric: mem, field: cached

-  metric: mem, field: commit_limit

-  metric: mem, field: committed_as

-  metric: mem, field: dirty

-  metric: mem, field: high_free

-  metric: mem, field: high_total

-  metric: mem, field: huge_pages_free

-  metric: mem, field: huge_page_size

-  metric: mem, field: huge_pages_total

-  metric: mem, field: inactive

-  metric: mem, field: low_free

-  metric: mem, field: low_total

-  metric: mem, field: mapped

-  metric: mem, field: page_tables

-  metric: mem, field: shared

-  metric: mem, field: slab

-  metric: mem, field: sreclaimable

-  metric: mem, field: sunreclaim

-  metric: mem, field: swap_cached

-  metric: mem, field: swap_free

-  metric: mem, field: swap_total

-  metric: mem, field: total

-  metric: mem, field: used_percent

-  metric: mem, field: vmalloc_chunk

-  metric: mem, field: vmalloc_total

-  metric: mem, field: vmalloc_used

-  metric: mem, field: write_back

-  metric: mem, field: write_back_tmp

-  metric: processes, field: dead

-  metric: processes, field: idle

-  metric: processes, field: sleeping

-  metric: processes, field: stopped

-  metric: processes, field: total

-  metric: processes, field: total_threads

-  metric: processes, field: unknown

-  metric: procstat, field: cpu_usage

-  metric: procstat, field: memory_data

-  metric: procstat, field: memory_rss

-  metric: procstat, field: num_fds

-  metric: procstat, field: rlimit_num_fds_soft

-  metric: service_connections, field: accepted

-  metric: service_connections, field: dropped

-  metric: service_connections, field: limit_avg_per_second

-  metric: service_connections, field: limit_burst

-  metric: swap, field: free

-  metric: swap, field: in

-  metric: swap, field: out

-  metric: swap, field: total

-  metric: swap, field: used

-  metric: swap, field: used_percent

-  metric: system, field: load15

-  metric: system, field: load5

-  metric: system, field: n_cpus

-  metric: system, field: n_users

.. _h_687c77a1f9:

Additional metrics for Aiven for Elasticsearch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  metric: elasticsearch_breakers, field:
   accounting_estimated_size_in_bytes

-  metric: elasticsearch_breakers, field: accounting_limit_size_in_bytes

-  metric: elasticsearch_breakers, field: accounting_overhead

-  metric: elasticsearch_breakers, field: accounting_tripped

-  metric: elasticsearch_breakers, field:
   fielddata_estimated_size_in_bytes

-  metric: elasticsearch_breakers, field: fielddata_limit_size_in_bytes

-  metric: elasticsearch_breakers, field: fielddata_overhead

-  metric: elasticsearch_breakers, field: fielddata_tripped

-  metric: elasticsearch_breakers, field:
   in_flight_requests_estimated_size_in_bytes

-  metric: elasticsearch_breakers, field:
   in_flight_requests_limit_size_in_bytes

-  metric: elasticsearch_breakers, field: in_flight_requests_overhead

-  metric: elasticsearch_breakers, field: in_flight_requests_tripped

-  metric: elasticsearch_breakers, field: parent_estimated_size_in_bytes

-  metric: elasticsearch_breakers, field: parent_limit_size_in_bytes

-  metric: elasticsearch_breakers, field: parent_overhead

-  metric: elasticsearch_breakers, field: parent_tripped

-  metric: elasticsearch_breakers, field:
   request_estimated_size_in_bytes

-  metric: elasticsearch_breakers, field: request_limit_size_in_bytes

-  metric: elasticsearch_breakers, field: request_overhead

-  metric: elasticsearch_breakers, field: request_tripped

-  metric: elasticsearch_cluster_health, field:
   active_shards_percent_as_number

-  metric: elasticsearch_cluster_health, field:
   delayed_unassigned_shards

-  metric: elasticsearch_cluster_health_indices, field:
   active_primary_shards

-  metric: elasticsearch_cluster_health_indices, field: active_shards

-  metric: elasticsearch_cluster_health_indices, field:
   initializing_shards

-  metric: elasticsearch_cluster_health_indices, field:
   number_of_replicas

-  metric: elasticsearch_cluster_health_indices, field: number_of_shards

-  metric: elasticsearch_cluster_health_indices, field:
   relocating_shards

-  metric: elasticsearch_cluster_health_indices, field: status

-  metric: elasticsearch_cluster_health_indices, field: status_code

-  metric: elasticsearch_cluster_health_indices, field:
   unassigned_shards

-  metric: elasticsearch_cluster_health, field: number_of_data_nodes

-  metric: elasticsearch_cluster_health, field:
   number_of_in_flight_fetch

-  metric: elasticsearch_cluster_health, field: number_of_nodes

-  metric: elasticsearch_cluster_health, field: status

-  metric: elasticsearch_cluster_health, field: timed_out

-  metric: elasticsearch_clusterstats_indices, field:
   completion_size_in_bytes

-  metric: elasticsearch_clusterstats_indices, field:
   fielddata_evictions

-  metric: elasticsearch_clusterstats_indices, field:
   fielddata_memory_size_in_bytes

-  metric: elasticsearch_clusterstats_indices, field:
   mappings_field_types_0_count

-  metric: elasticsearch_clusterstats_indices, field:
   mappings_field_types_0_index_count

-  metric: elasticsearch_clusterstats_indices, field:
   mappings_field_types_0_name

-  metric: elasticsearch_clusterstats_indices, field:
   query_cache_cache_count

-  metric: elasticsearch_clusterstats_indices, field:
   query_cache_cache_size

-  metric: elasticsearch_clusterstats_indices, field:
   query_cache_evictions

-  metric: elasticsearch_clusterstats_indices, field:
   query_cache_hit_count

-  metric: elasticsearch_clusterstats_indices, field:
   query_cache_memory_size_in_bytes

-  metric: elasticsearch_clusterstats_indices, field:
   query_cache_miss_count

-  metric: elasticsearch_clusterstats_indices, field:
   query_cache_total_count

-  metric: elasticsearch_clusterstats_indices, field: segments_count

-  metric: elasticsearch_clusterstats_indices, field:
   segments_doc_values_memory_in_bytes

-  metric: elasticsearch_clusterstats_indices, field:
   segments_fixed_bit_set_memory_in_bytes

-  metric: elasticsearch_clusterstats_indices, field:
   segments_index_writer_memory_in_bytes

-  metric: elasticsearch_clusterstats_indices, field:
   segments_max_unsafe_auto_id_timestamp

-  metric: elasticsearch_clusterstats_indices, field:
   segments_memory_in_bytes

-  metric: elasticsearch_clusterstats_indices, field:
   segments_norms_memory_in_bytes

-  metric: elasticsearch_clusterstats_indices, field:
   segments_points_memory_in_bytes

-  metric: elasticsearch_clusterstats_indices, field:
   segments_stored_fields_memory_in_bytes

-  metric: elasticsearch_clusterstats_indices, field:
   segments_terms_memory_in_bytes

-  metric: elasticsearch_clusterstats_indices, field:
   segments_term_vectors_memory_in_bytes

-  metric: elasticsearch_clusterstats_indices, field:
   segments_version_map_memory_in_bytes

-  metric: elasticsearch_clusterstats_indices, field:
   shards_index_primaries_avg

-  metric: elasticsearch_clusterstats_indices, field:
   shards_index_primaries_max

-  metric: elasticsearch_clusterstats_indices, field:
   shards_index_primaries_min

-  metric: elasticsearch_clusterstats_indices, field:
   shards_index_replication_avg

-  metric: elasticsearch_clusterstats_indices, field:
   shards_index_replication_max

-  metric: elasticsearch_clusterstats_indices, field:
   shards_index_replication_min

-  metric: elasticsearch_clusterstats_indices, field:
   shards_index_shards_avg

-  metric: elasticsearch_clusterstats_indices, field:
   shards_index_shards_max

-  metric: elasticsearch_clusterstats_indices, field:
   shards_index_shards_min

-  metric: elasticsearch_clusterstats_indices, field: shards_primaries

-  metric: elasticsearch_clusterstats_indices, field: shards_replication

-  metric: elasticsearch_clusterstats_indices, field: shards_total

-  metric: elasticsearch_clusterstats_indices, field:
   store_reserved_in_bytes

-  metric: elasticsearch_fs, field: data_0_available_in_bytes

-  metric: elasticsearch_fs, field: data_0_free_in_bytes

-  metric: elasticsearch_fs, field: data_0_total_in_bytes

-  metric: elasticsearch_fs, field: io_stats_devices_0_operations

-  metric: elasticsearch_fs, field: io_stats_devices_0_read_kilobytes

-  metric: elasticsearch_fs, field: io_stats_devices_0_read_operations

-  metric: elasticsearch_fs, field: io_stats_devices_0_write_kilobytes

-  metric: elasticsearch_fs, field: io_stats_devices_0_write_operations

-  metric: elasticsearch_fs, field: io_stats_total_operations

-  metric: elasticsearch_fs, field: io_stats_total_read_kilobytes

-  metric: elasticsearch_fs, field: io_stats_total_read_operations

-  metric: elasticsearch_fs, field: io_stats_total_write_kilobytes

-  metric: elasticsearch_fs, field: io_stats_total_write_operations

-  metric: elasticsearch_fs, field: timestamp

-  metric: elasticsearch_fs, field: total_available_in_bytes

-  metric: elasticsearch_fs, field: total_free_in_bytes

-  metric: elasticsearch_fs, field: total_total_in_bytes

-  metric: elasticsearch_indices, field: completion_size_in_bytes

-  metric: elasticsearch_indices, field: fielddata_evictions

-  metric: elasticsearch_indices, field: fielddata_memory_size_in_bytes

-  metric: elasticsearch_indices, field: flush_periodic

-  metric: elasticsearch_indices, field: flush_total

-  metric: elasticsearch_indices, field: flush_total_time_in_millis

-  metric: elasticsearch_indices, field: get_current

-  metric: elasticsearch_indices, field: get_exists_time_in_millis

-  metric: elasticsearch_indices, field: get_exists_total

-  metric: elasticsearch_indices, field: get_missing_time_in_millis

-  metric: elasticsearch_indices, field: get_missing_total

-  metric: elasticsearch_indices, field: get_time_in_millis

-  metric: elasticsearch_indices, field: get_total

-  metric: elasticsearch_indices, field: indexing_delete_current

-  metric: elasticsearch_indices, field: indexing_delete_time_in_millis

-  metric: elasticsearch_indices, field: indexing_delete_total

-  metric: elasticsearch_indices, field: indexing_index_current

-  metric: elasticsearch_indices, field: indexing_index_failed

-  metric: elasticsearch_indices, field: indexing_index_time_in_millis

-  metric: elasticsearch_indices, field: indexing_index_total

-  metric: elasticsearch_indices, field: indexing_noop_update_total

-  metric: elasticsearch_indices, field:
   indexing_throttle_time_in_millis

-  metric: elasticsearch_indices, field: merges_current

-  metric: elasticsearch_indices, field: merges_current_docs

-  metric: elasticsearch_indices, field: merges_current_size_in_bytes

-  metric: elasticsearch_indices, field: merges_total

-  metric: elasticsearch_indices, field:
   merges_total_auto_throttle_in_bytes

-  metric: elasticsearch_indices, field: merges_total_docs

-  metric: elasticsearch_indices, field: merges_total_size_in_bytes

-  metric: elasticsearch_indices, field:
   merges_total_stopped_time_in_millis

-  metric: elasticsearch_indices, field:
   merges_total_throttled_time_in_millis

-  metric: elasticsearch_indices, field: merges_total_time_in_millis

-  metric: elasticsearch_indices, field: query_cache_cache_count

-  metric: elasticsearch_indices, field: query_cache_cache_size

-  metric: elasticsearch_indices, field: query_cache_evictions

-  metric: elasticsearch_indices, field: query_cache_hit_count

-  metric: elasticsearch_indices, field:
   query_cache_memory_size_in_bytes

-  metric: elasticsearch_indices, field: query_cache_miss_count

-  metric: elasticsearch_indices, field: query_cache_total_count

-  metric: elasticsearch_indices, field: recovery_current_as_source

-  metric: elasticsearch_indices, field: recovery_current_as_target

-  metric: elasticsearch_indices, field:
   recovery_throttle_time_in_millis

-  metric: elasticsearch_indices, field: refresh_external_total

-  metric: elasticsearch_indices, field:
   refresh_external_total_time_in_millis

-  metric: elasticsearch_indices, field: refresh_listeners

-  metric: elasticsearch_indices, field: refresh_total

-  metric: elasticsearch_indices, field: refresh_total_time_in_millis

-  metric: elasticsearch_indices, field: request_cache_evictions

-  metric: elasticsearch_indices, field: request_cache_hit_count

-  metric: elasticsearch_indices, field:
   request_cache_memory_size_in_bytes

-  metric: elasticsearch_indices, field: request_cache_miss_count

-  metric: elasticsearch_indices, field: search_fetch_current

-  metric: elasticsearch_indices, field: search_fetch_time_in_millis

-  metric: elasticsearch_indices, field: search_fetch_total

-  metric: elasticsearch_indices, field: search_open_contexts

-  metric: elasticsearch_indices, field: search_query_current

-  metric: elasticsearch_indices, field: search_query_time_in_millis

-  metric: elasticsearch_indices, field: search_query_total

-  metric: elasticsearch_indices, field: search_scroll_current

-  metric: elasticsearch_indices, field: search_scroll_time_in_millis

-  metric: elasticsearch_indices, field: search_scroll_total

-  metric: elasticsearch_indices, field: search_suggest_current

-  metric: elasticsearch_indices, field: search_suggest_time_in_millis

-  metric: elasticsearch_indices, field: search_suggest_total

-  metric: elasticsearch_indices, field: segments_count

-  metric: elasticsearch_indices, field:
   segments_doc_values_memory_in_bytes

-  metric: elasticsearch_indices, field:
   segments_fixed_bit_set_memory_in_bytes

-  metric: elasticsearch_indices, field:
   segments_index_writer_memory_in_bytes

-  metric: elasticsearch_indices, field:
   segments_max_unsafe_auto_id_timestamp

-  metric: elasticsearch_indices, field: segments_memory_in_bytes

-  metric: elasticsearch_indices, field: segments_norms_memory_in_bytes

-  metric: elasticsearch_indices, field: segments_points_memory_in_bytes

-  metric: elasticsearch_indices, field:
   segments_stored_fields_memory_in_bytes

-  metric: elasticsearch_indices, field: segments_terms_memory_in_bytes

-  metric: elasticsearch_indices, field:
   segments_term_vectors_memory_in_bytes

-  metric: elasticsearch_indices, field:
   segments_version_map_memory_in_bytes

-  metric: elasticsearch_indices, field: store_reserved_in_bytes

-  metric: elasticsearch_indices, field:
   translog_earliest_last_modified_age

-  metric: elasticsearch_indices, field: translog_operations

-  metric: elasticsearch_indices, field: translog_size_in_bytes

-  metric: elasticsearch_indices, field: translog_uncommitted_operations

-  metric: elasticsearch_indices, field:
   translog_uncommitted_size_in_bytes

-  metric: elasticsearch_indices, field: warmer_current

-  metric: elasticsearch_indices, field: warmer_total

-  metric: elasticsearch_indices, field: warmer_total_time_in_millis

-  metric: elasticsearch_jvm, field: buffer_pools_direct_count

-  metric: elasticsearch_jvm, field:
   buffer_pools_direct_total_capacity_in_bytes

-  metric: elasticsearch_jvm, field: buffer_pools_direct_used_in_bytes

-  metric: elasticsearch_jvm, field: buffer_pools_mapped_count

-  metric: elasticsearch_jvm, field:
   buffer_pools_mapped_total_capacity_in_bytes

-  metric: elasticsearch_jvm, field: buffer_pools_mapped_used_in_bytes

-  metric: elasticsearch_jvm, field: classes_current_loaded_count

-  metric: elasticsearch_jvm, field: classes_total_loaded_count

-  metric: elasticsearch_jvm, field: classes_total_unloaded_count

-  metric: elasticsearch_jvm, field: mem_heap_committed_in_bytes

-  metric: elasticsearch_jvm, field: mem_heap_max_in_bytes

-  metric: elasticsearch_jvm, field: mem_heap_used_in_bytes

-  metric: elasticsearch_jvm, field: mem_non_heap_committed_in_bytes

-  metric: elasticsearch_jvm, field: mem_non_heap_used_in_bytes

-  metric: elasticsearch_jvm, field: mem_pools_old_max_in_bytes

-  metric: elasticsearch_jvm, field: mem_pools_old_peak_max_in_bytes

-  metric: elasticsearch_jvm, field: mem_pools_old_peak_used_in_bytes

-  metric: elasticsearch_jvm, field: mem_pools_old_used_in_bytes

-  metric: elasticsearch_jvm, field: mem_pools_survivor_max_in_bytes

-  metric: elasticsearch_jvm, field:
   mem_pools_survivor_peak_max_in_bytes

-  metric: elasticsearch_jvm, field:
   mem_pools_survivor_peak_used_in_bytes

-  metric: elasticsearch_jvm, field: mem_pools_survivor_used_in_bytes

-  metric: elasticsearch_jvm, field: mem_pools_young_max_in_bytes

-  metric: elasticsearch_jvm, field: mem_pools_young_peak_max_in_bytes

-  metric: elasticsearch_jvm, field: mem_pools_young_peak_used_in_bytes

-  metric: elasticsearch_jvm, field: mem_pools_young_used_in_bytes

-  metric: elasticsearch_jvm, field: threads_count

-  metric: elasticsearch_jvm, field: threads_peak_count

-  metric: elasticsearch_jvm, field: timestamp

-  metric: elasticsearch_jvm, field: uptime_in_millis

-  metric: elasticsearch_os, field: cpu_load_average_15m

-  metric: elasticsearch_os, field: cpu_load_average_1m

-  metric: elasticsearch_os, field: cpu_load_average_5m

-  metric: elasticsearch_os, field: cpu_percent

-  metric: elasticsearch_os, field: mem_free_in_bytes

-  metric: elasticsearch_os, field: mem_free_percent

-  metric: elasticsearch_os, field: mem_total_in_bytes

-  metric: elasticsearch_os, field: mem_used_in_bytes

-  metric: elasticsearch_os, field: mem_used_percent

-  metric: elasticsearch_os, field: swap_free_in_bytes

-  metric: elasticsearch_os, field: swap_total_in_bytes

-  metric: elasticsearch_os, field: swap_used_in_bytes

-  metric: elasticsearch_os, field: timestamp

-  metric: elasticsearch_process, field: cpu_percent

-  metric: elasticsearch_process, field: cpu_total_in_millis

-  metric: elasticsearch_process, field: max_file_descriptors

-  metric: elasticsearch_process, field: mem_total_virtual_in_bytes

-  metric: elasticsearch_process, field: open_file_descriptors

-  metric: elasticsearch_process, field: timestamp

-  metric: elasticsearch_thread_pool, field: analyze_active

-  metric: elasticsearch_thread_pool, field: analyze_completed

-  metric: elasticsearch_thread_pool, field: analyze_largest

-  metric: elasticsearch_thread_pool, field: analyze_queue

-  metric: elasticsearch_thread_pool, field: analyze_rejected

-  metric: elasticsearch_thread_pool, field: analyze_threads

-  metric: elasticsearch_thread_pool, field: fetch_shard_started_active

-  metric: elasticsearch_thread_pool, field:
   fetch_shard_started_completed

-  metric: elasticsearch_thread_pool, field: fetch_shard_started_largest

-  metric: elasticsearch_thread_pool, field: fetch_shard_started_queue

-  metric: elasticsearch_thread_pool, field:
   fetch_shard_started_rejected

-  metric: elasticsearch_thread_pool, field: fetch_shard_started_threads

-  metric: elasticsearch_thread_pool, field: fetch_shard_store_active

-  metric: elasticsearch_thread_pool, field: fetch_shard_store_completed

-  metric: elasticsearch_thread_pool, field: fetch_shard_store_largest

-  metric: elasticsearch_thread_pool, field: fetch_shard_store_queue

-  metric: elasticsearch_thread_pool, field: fetch_shard_store_rejected

-  metric: elasticsearch_thread_pool, field: fetch_shard_store_threads

-  metric: elasticsearch_thread_pool, field: flush_active

-  metric: elasticsearch_thread_pool, field: flush_completed

-  metric: elasticsearch_thread_pool, field: flush_largest

-  metric: elasticsearch_thread_pool, field: flush_queue

-  metric: elasticsearch_thread_pool, field: flush_rejected

-  metric: elasticsearch_thread_pool, field: flush_threads

-  metric: elasticsearch_thread_pool, field: force_merge_active

-  metric: elasticsearch_thread_pool, field: force_merge_completed

-  metric: elasticsearch_thread_pool, field: force_merge_largest

-  metric: elasticsearch_thread_pool, field: force_merge_queue

-  metric: elasticsearch_thread_pool, field: force_merge_rejected

-  metric: elasticsearch_thread_pool, field: force_merge_threads

-  metric: elasticsearch_thread_pool, field: generic_active

-  metric: elasticsearch_thread_pool, field: generic_completed

-  metric: elasticsearch_thread_pool, field: generic_largest

-  metric: elasticsearch_thread_pool, field: generic_queue

-  metric: elasticsearch_thread_pool, field: generic_rejected

-  metric: elasticsearch_thread_pool, field: generic_threads

-  metric: elasticsearch_thread_pool, field: get_active

-  metric: elasticsearch_thread_pool, field: get_completed

-  metric: elasticsearch_thread_pool, field: get_largest

-  metric: elasticsearch_thread_pool, field: get_queue

-  metric: elasticsearch_thread_pool, field: get_rejected

-  metric: elasticsearch_thread_pool, field: get_threads

-  metric: elasticsearch_thread_pool, field: listener_active

-  metric: elasticsearch_thread_pool, field: listener_completed

-  metric: elasticsearch_thread_pool, field: listener_largest

-  metric: elasticsearch_thread_pool, field: listener_queue

-  metric: elasticsearch_thread_pool, field: listener_rejected

-  metric: elasticsearch_thread_pool, field: listener_threads

-  metric: elasticsearch_thread_pool, field: management_active

-  metric: elasticsearch_thread_pool, field: management_completed

-  metric: elasticsearch_thread_pool, field: management_largest

-  metric: elasticsearch_thread_pool, field: management_queue

-  metric: elasticsearch_thread_pool, field: management_rejected

-  metric: elasticsearch_thread_pool, field: management_threads

-  metric: elasticsearch_thread_pool, field: refresh_active

-  metric: elasticsearch_thread_pool, field: refresh_completed

-  metric: elasticsearch_thread_pool, field: refresh_largest

-  metric: elasticsearch_thread_pool, field: refresh_queue

-  metric: elasticsearch_thread_pool, field: refresh_rejected

-  metric: elasticsearch_thread_pool, field: refresh_threads

-  metric: elasticsearch_thread_pool, field: repository_azure_active

-  metric: elasticsearch_thread_pool, field: repository_azure_completed

-  metric: elasticsearch_thread_pool, field: repository_azure_largest

-  metric: elasticsearch_thread_pool, field: repository_azure_queue

-  metric: elasticsearch_thread_pool, field: repository_azure_rejected

-  metric: elasticsearch_thread_pool, field: repository_azure_threads

-  metric: elasticsearch_thread_pool, field: search_active

-  metric: elasticsearch_thread_pool, field: search_completed

-  metric: elasticsearch_thread_pool, field: search_largest

-  metric: elasticsearch_thread_pool, field: search_queue

-  metric: elasticsearch_thread_pool, field: search_rejected

-  metric: elasticsearch_thread_pool, field: search_threads

-  metric: elasticsearch_thread_pool, field: search_throttled_active

-  metric: elasticsearch_thread_pool, field: search_throttled_completed

-  metric: elasticsearch_thread_pool, field: search_throttled_largest

-  metric: elasticsearch_thread_pool, field: search_throttled_queue

-  metric: elasticsearch_thread_pool, field: search_throttled_rejected

-  metric: elasticsearch_thread_pool, field: search_throttled_threads

-  metric: elasticsearch_thread_pool, field: snapshot_active

-  metric: elasticsearch_thread_pool, field: snapshot_completed

-  metric: elasticsearch_thread_pool, field: snapshot_largest

-  metric: elasticsearch_thread_pool, field: snapshot_queue

-  metric: elasticsearch_thread_pool, field: snapshot_rejected

-  metric: elasticsearch_thread_pool, field: snapshot_threads

-  metric: elasticsearch_thread_pool, field: sql-worker_active

-  metric: elasticsearch_thread_pool, field: sql-worker_completed

-  metric: elasticsearch_thread_pool, field: sql-worker_largest

-  metric: elasticsearch_thread_pool, field: sql-worker_queue

-  metric: elasticsearch_thread_pool, field: sql-worker_rejected

-  metric: elasticsearch_thread_pool, field: sql-worker_threads

-  metric: elasticsearch_thread_pool, field: system_read_active

-  metric: elasticsearch_thread_pool, field: system_read_completed

-  metric: elasticsearch_thread_pool, field: system_read_largest

-  metric: elasticsearch_thread_pool, field: system_read_queue

-  metric: elasticsearch_thread_pool, field: system_read_rejected

-  metric: elasticsearch_thread_pool, field: system_read_threads

-  metric: elasticsearch_thread_pool, field: system_write_active

-  metric: elasticsearch_thread_pool, field: system_write_completed

-  metric: elasticsearch_thread_pool, field: system_write_largest

-  metric: elasticsearch_thread_pool, field: system_write_queue

-  metric: elasticsearch_thread_pool, field: system_write_rejected

-  metric: elasticsearch_thread_pool, field: system_write_threads

-  metric: elasticsearch_thread_pool, field: warmer_active

-  metric: elasticsearch_thread_pool, field: warmer_completed

-  metric: elasticsearch_thread_pool, field: warmer_largest

-  metric: elasticsearch_thread_pool, field: warmer_queue

-  metric: elasticsearch_thread_pool, field: warmer_rejected

-  metric: elasticsearch_thread_pool, field: warmer_threads

-  metric: elasticsearch_thread_pool, field: write_active

-  metric: elasticsearch_thread_pool, field: write_completed

-  metric: elasticsearch_thread_pool, field: write_largest

-  metric: elasticsearch_thread_pool, field: write_queue

-  metric: elasticsearch_thread_pool, field: write_rejected

-  metric: elasticsearch_thread_pool, field: write_threads

-  metric: elasticsearch_transport, field: rx_count

-  metric: elasticsearch_transport, field: server_open

-  metric: elasticsearch_transport, field: total_outbound_connections

-  metric: elasticsearch_transport, field: tx_count

-  metric: java.lang:Memory, field: committed

-  metric: java.lang:Memory, field: init

-  metric: java.lang:Memory, field: max

-  metric: java.lang:Memory, field: ObjectPendingFinalizationCount

.. _h_f04a4e48e2:

Additional metrics for Aiven for Apache Kafka
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  metric: kafka.controller:ControllerChannelManager.TotalQueueSize,
   field: Value

-  metric: kafka.controller:ControllerEventManager.EventQueueSize,
   field: Value

-  metric: kafka.controller:ControllerEventManager.EventQueueTimeMs,
   field: 50thPercentile

-  metric: kafka.controller:ControllerEventManager.EventQueueTimeMs,
   field: 75thPercentile

-  metric: kafka.controller:ControllerEventManager.EventQueueTimeMs,
   field: 95thPercentile

-  metric: kafka.controller:ControllerEventManager.EventQueueTimeMs,
   field: 98thPercentile

-  metric: kafka.controller:ControllerEventManager.EventQueueTimeMs,
   field: 999thPercentile

-  metric: kafka.controller:ControllerEventManager.EventQueueTimeMs,
   field: 99thPercentile

-  metric: kafka.controller:ControllerEventManager.EventQueueTimeMs,
   field: Count

-  metric: kafka.controller:ControllerEventManager.EventQueueTimeMs,
   field: Max

-  metric: kafka.controller:ControllerEventManager.EventQueueTimeMs,
   field: Mean

-  metric: kafka.controller:ControllerEventManager.EventQueueTimeMs,
   field: Min

-  metric: kafka.controller:ControllerEventManager.EventQueueTimeMs,
   field: StdDev

-  metric: kafka.controller:ControllerStats.LeaderElectionRateAndTimeMs,
   field: 50thPercentile

-  metric: kafka.controller:ControllerStats.LeaderElectionRateAndTimeMs,
   field: 75thPercentile

-  metric: kafka.controller:ControllerStats.LeaderElectionRateAndTimeMs,
   field: 95thPercentile

-  metric: kafka.controller:ControllerStats.LeaderElectionRateAndTimeMs,
   field: 98thPercentile

-  metric: kafka.controller:ControllerStats.LeaderElectionRateAndTimeMs,
   field: 999thPercentile

-  metric: kafka.controller:ControllerStats.LeaderElectionRateAndTimeMs,
   field: 99thPercentile

-  metric: kafka.controller:ControllerStats.LeaderElectionRateAndTimeMs,
   field: FifteenMinuteRate

-  metric: kafka.controller:ControllerStats.LeaderElectionRateAndTimeMs,
   field: FiveMinuteRate

-  metric: kafka.controller:ControllerStats.LeaderElectionRateAndTimeMs,
   field: Max

-  metric: kafka.controller:ControllerStats.LeaderElectionRateAndTimeMs,
   field: Mean

-  metric: kafka.controller:ControllerStats.LeaderElectionRateAndTimeMs,
   field: MeanRate

-  metric: kafka.controller:ControllerStats.LeaderElectionRateAndTimeMs,
   field: Min

-  metric: kafka.controller:ControllerStats.LeaderElectionRateAndTimeMs,
   field: StdDev

-  metric: kafka.controller:KafkaController.ActiveControllerCount,
   field: Value

-  metric: kafka.controller:KafkaController.OfflinePartitionsCount,
   field: Value

-  metric: kafka.jolokia_collector, field: collect_time

-  metric: kafka.log:LogCleaner.cleaner-recopy-percent, field: Value

-  metric: kafka.log:LogCleanerManager.time-since-last-run-ms, field:
   Value

-  metric: kafka.log:LogCleaner.max-clean-time-secs, field: Value

-  metric: kafka.network:RequestChannel.RequestQueueSize, field: Value

-  metric: kafka.network:RequestChannel.ResponseQueueSize, field: Value

-  metric: kafka.network:RequestMetrics.TotalTimeMs, field:
   95thPercentile

-  metric: kafka.network:RequestMetrics.TotalTimeMs, field: Count

-  metric: kafka.network:RequestMetrics.TotalTimeMs, field: Mean

-  metric: kafka.server:BrokerTopicMetrics.BytesRejectedPerSec, field:
   Count

-  metric: kafka.server:BrokerTopicMetrics.FailedProduceRequestsPerSec,
   field: Count

-  metric:
   kafka.server:BrokerTopicMetrics.FetchMessageConversionsPerSec, field:
   Count

-  metric: kafka.server:BrokerTopicMetrics.TotalFetchRequestsPerSec,
   field: Count

-  metric: kafka.server:BrokerTopicMetrics.TotalProduceRequestsPerSec,
   field: Count

-  metric: kafka.server:KafkaServer.BrokerState, field: Value

-  metric: kafka.server:ReplicaManager.LeaderCount, field: Value

-  metric: kafka.server:ReplicaManager.PartitionCount, field: Value

-  metric: kafka.server:ReplicaManager.UnderMinIsrPartitionCount, field:
   Value

.. _h_84c84c23fa:

Additional metrics for Aiven for MySQL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  metric: mysql, field: com_alter_tablespace

-  metric: mysql, field: com_alter_user

-  metric: mysql, field: com_alter_user_default_role

-  metric: mysql, field: com_analyze

-  metric: mysql, field: com_begin

-  metric: mysql, field: com_binlog

-  metric: mysql, field: com_call_procedure

-  metric: mysql, field: com_change_db

-  metric: mysql, field: com_change_master

-  metric: mysql, field: com_change_repl_filter

-  metric: mysql, field: com_change_replication_source

-  metric: mysql, field: com_check

-  metric: mysql, field: com_checksum

-  metric: mysql, field: com_clone

-  metric: mysql, field: com_commit

-  metric: mysql, field: com_create_db

-  metric: mysql, field: com_create_event

-  metric: mysql, field: com_create_function

-  metric: mysql, field: com_create_index

-  metric: mysql, field: com_create_procedure

-  metric: mysql, field: com_create_resource_group

-  metric: mysql, field: com_create_role

-  metric: mysql, field: com_create_server

-  metric: mysql, field: com_create_spatial_reference_system

-  metric: mysql, field: com_create_table

-  metric: mysql, field: com_create_trigger

-  metric: mysql, field: com_create_udf

-  metric: mysql, field: com_create_user

-  metric: mysql, field: com_create_view

-  metric: mysql, field: com_dealloc_sql

-  metric: mysql, field: com_delete

-  metric: mysql, field: com_delete_multi

-  metric: mysql, field: com_do

-  metric: mysql, field: com_drop_db

-  metric: mysql, field: com_drop_event

-  metric: mysql, field: com_drop_function

-  metric: mysql, field: com_drop_index

-  metric: mysql, field: com_drop_procedure

-  metric: mysql, field: com_drop_resource_group

-  metric: mysql, field: com_drop_role

-  metric: mysql, field: com_drop_server

-  metric: mysql, field: com_drop_spatial_reference_system

-  metric: mysql, field: com_drop_table

-  metric: mysql, field: com_drop_trigger

-  metric: mysql, field: com_drop_user

-  metric: mysql, field: com_drop_view

-  metric: mysql, field: com_empty_query

-  metric: mysql, field: com_execute_sql

-  metric: mysql, field: com_explain_other

-  metric: mysql, field: com_flush

-  metric: mysql, field: com_get_diagnostics

-  metric: mysql, field: com_grant

-  metric: mysql, field: com_grant_roles

-  metric: mysql, field: com_group_replication_start

-  metric: mysql, field: com_group_replication_stop

-  metric: mysql, field: com_ha_close

-  metric: mysql, field: com_ha_open

-  metric: mysql, field: com_ha_read

-  metric: mysql, field: com_help

-  metric: mysql, field: com_import

-  metric: mysql, field: com_insert

-  metric: mysql, field: com_insert_select

-  metric: mysql, field: com_install_component

-  metric: mysql, field: com_install_plugin

-  metric: mysql, field: com_kill

-  metric: mysql, field: com_load

-  metric: mysql, field: com_lock_instance

-  metric: mysql, field: com_lock_tables

-  metric: mysql, field: com_optimize

-  metric: mysql, field: com_preload_keys

-  metric: mysql, field: com_prepare_sql

-  metric: mysql, field: com_purge

-  metric: mysql, field: com_purge_before_date

-  metric: mysql, field: com_release_savepoint

-  metric: mysql, field: com_rename_table

-  metric: mysql, field: com_rename_user

-  metric: mysql, field: com_repair

-  metric: mysql, field: com_replace

-  metric: mysql, field: com_replace_select

-  metric: mysql, field: com_replica_start

-  metric: mysql, field: com_replica_stop

-  metric: mysql, field: com_reset

-  metric: mysql, field: com_resignal

-  metric: mysql, field: com_restart

-  metric: mysql, field: com_revoke

-  metric: mysql, field: com_revoke_all

-  metric: mysql, field: com_revoke_roles

-  metric: mysql, field: com_rollback

-  metric: mysql, field: com_rollback_to_savepoint

-  metric: mysql, field: com_savepoint

-  metric: mysql, field: com_select

-  metric: mysql, field: com_set_option

-  metric: mysql, field: com_set_password

-  metric: mysql, field: com_set_resource_group

-  metric: mysql, field: com_set_role

-  metric: mysql, field: com_show_binlog_events

-  metric: mysql, field: com_show_binlogs

-  metric: mysql, field: com_show_charsets

-  metric: mysql, field: com_show_collations

-  metric: mysql, field: com_show_create_db

-  metric: mysql, field: com_show_create_event

-  metric: mysql, field: com_show_create_func

-  metric: mysql, field: com_show_create_proc

-  metric: mysql, field: com_show_create_table

-  metric: mysql, field: com_show_create_trigger

-  metric: mysql, field: com_show_create_user

-  metric: mysql, field: com_show_databases

-  metric: mysql, field: com_show_engine_logs

-  metric: mysql, field: com_show_engine_mutex

-  metric: mysql, field: com_show_engine_status

-  metric: mysql, field: com_show_errors

-  metric: mysql, field: com_show_events

-  metric: mysql, field: com_show_fields

-  metric: mysql, field: com_show_function_code

-  metric: mysql, field: com_show_function_status

-  metric: mysql, field: com_show_grants

-  metric: mysql, field: com_show_keys

-  metric: mysql, field: com_show_master_status

-  metric: mysql, field: com_show_open_tables

-  metric: mysql, field: com_show_plugins

-  metric: mysql, field: com_show_privileges

-  metric: mysql, field: com_show_procedure_code

-  metric: mysql, field: com_show_procedure_status

-  metric: mysql, field: com_show_processlist

-  metric: mysql, field: com_show_profile

-  metric: mysql, field: com_show_profiles

-  metric: mysql, field: com_show_relaylog_events

-  metric: mysql, field: com_show_replicas

-  metric: mysql, field: com_show_replica_status

-  metric: mysql, field: com_show_slave_hosts

-  metric: mysql, field: com_show_slave_status

-  metric: mysql, field: com_show_status

-  metric: mysql, field: com_show_storage_engines

-  metric: mysql, field: com_show_tables

-  metric: mysql, field: com_show_table_status

-  metric: mysql, field: com_show_triggers

-  metric: mysql, field: com_show_variables

-  metric: mysql, field: com_show_warnings

-  metric: mysql, field: com_shutdown

-  metric: mysql, field: com_signal

-  metric: mysql, field: com_slave_start

-  metric: mysql, field: com_slave_stop

-  metric: mysql, field: com_stmt_close

-  metric: mysql, field: com_stmt_execute

-  metric: mysql, field: com_stmt_fetch

-  metric: mysql, field: com_stmt_prepare

-  metric: mysql, field: com_stmt_reprepare

-  metric: mysql, field: com_stmt_reset

-  metric: mysql, field: com_stmt_send_long_data

-  metric: mysql, field: com_truncate

-  metric: mysql, field: com_uninstall_component

-  metric: mysql, field: com_uninstall_plugin

-  metric: mysql, field: com_unlock_instance

-  metric: mysql, field: com_unlock_tables

-  metric: mysql, field: com_update

-  metric: mysql, field: com_update_multi

-  metric: mysql, field: com_xa_commit

-  metric: mysql, field: com_xa_end

-  metric: mysql, field: com_xa_prepare

-  metric: mysql, field: com_xa_recover

-  metric: mysql, field: com_xa_rollback

-  metric: mysql, field: com_xa_start

-  metric: mysql, field: connection_errors_accept

-  metric: mysql, field: connection_errors_internal

-  metric: mysql, field: connection_errors_peer_address

-  metric: mysql, field: connection_errors_select

-  metric: mysql, field: connection_errors_tcpwrap

-  metric: mysql, field: created_tmp_disk_tables

-  metric: mysql, field: created_tmp_files

-  metric: mysql, field: created_tmp_tables

-  metric: mysql, field: current_tls_ca

-  metric: mysql, field: current_tls_cert

-  metric: mysql, field: current_tls_key

-  metric: mysql, field: current_tls_version

-  metric: mysql, field: delayed_errors

-  metric: mysql, field: delayed_insert_threads

-  metric: mysql, field: delayed_writes

-  metric: mysql, field: error_log_buffered_bytes

-  metric: mysql, field: error_log_buffered_events

-  metric: mysql, field: error_log_expired_events

-  metric: mysql, field: error_log_latest_write

-  metric: mysql, field: flush_commands

-  metric: mysql, field: handler_commit

-  metric: mysql, field: handler_delete

-  metric: mysql, field: handler_discover

-  metric: mysql, field: handler_external_lock

-  metric: mysql, field: handler_mrr_init

-  metric: mysql, field: handler_prepare

-  metric: mysql, field: handler_read_first

-  metric: mysql, field: handler_read_key

-  metric: mysql, field: handler_read_last

-  metric: mysql, field: handler_read_next

-  metric: mysql, field: handler_read_prev

-  metric: mysql_innodb, field: adaptive_hash_searches

-  metric: mysql_innodb, field: adaptive_hash_searches_btree

-  metric: mysql_innodb, field: buffer_data_reads

-  metric: mysql_innodb, field: buffer_data_written

-  metric: mysql_innodb, field: buffer_pages_created

-  metric: mysql_innodb, field: buffer_pages_read

-  metric: mysql_innodb, field: buffer_pages_written

-  metric: mysql_innodb, field: buffer_pool_bytes_data

-  metric: mysql_innodb, field: buffer_pool_bytes_dirty

-  metric: mysql_innodb, field: buffer_pool_pages_data

-  metric: mysql_innodb, field: buffer_pool_pages_dirty

-  metric: mysql_innodb, field: buffer_pool_pages_free

-  metric: mysql_innodb, field: buffer_pool_pages_misc

-  metric: mysql_innodb, field: buffer_pool_pages_total

-  metric: mysql_innodb, field: buffer_pool_read_ahead

-  metric: mysql, field: innodb_buffer_pool_read_ahead_evicted

-  metric: mysql_innodb, field: buffer_pool_read_ahead_evicted

-  metric: mysql, field: innodb_buffer_pool_read_requests

-  metric: mysql_innodb, field: buffer_pool_read_requests

-  metric: mysql, field: innodb_buffer_pool_reads

-  metric: mysql_innodb, field: buffer_pool_reads

-  metric: mysql_innodb, field: buffer_pool_size

-  metric: mysql, field: innodb_buffer_pool_wait_free

-  metric: mysql_innodb, field: buffer_pool_wait_free

-  metric: mysql, field: innodb_buffer_pool_write_requests

-  metric: mysql_innodb, field: buffer_pool_write_requests

-  metric: mysql, field: innodb_data_fsyncs

-  metric: mysql, field: innodb_data_pending_fsyncs

-  metric: mysql, field: innodb_data_pending_reads

-  metric: mysql, field: innodb_data_pending_writes

-  metric: mysql, field: innodb_data_read

-  metric: mysql, field: innodb_data_reads

-  metric: mysql, field: innodb_data_writes

-  metric: mysql, field: innodb_data_written

-  metric: mysql, field: innodb_dblwr_pages_written

-  metric: mysql, field: innodb_dblwr_writes

-  metric: mysql_innodb, field: dml_deletes

-  metric: mysql_innodb, field: dml_inserts

-  metric: mysql_innodb, field: dml_system_deletes

-  metric: mysql_innodb, field: dml_system_inserts

-  metric: mysql_innodb, field: dml_system_reads

-  metric: mysql_innodb, field: dml_system_updates

-  metric: mysql_innodb, field: dml_updates

-  metric: mysql_innodb, field: ibuf_merges

-  metric: mysql_innodb, field: ibuf_merges_delete

-  metric: mysql_innodb, field: ibuf_merges_delete_mark

-  metric: mysql_innodb, field: ibuf_merges_discard_delete

-  metric: mysql_innodb, field: ibuf_merges_discard_delete_mark

-  metric: mysql_innodb, field: ibuf_merges_discard_insert

-  metric: mysql_innodb, field: ibuf_merges_insert

-  metric: mysql_innodb, field: ibuf_size

-  metric: mysql_innodb, field: innodb_activity_count

-  metric: mysql_innodb, field: innodb_dblwr_pages_written

-  metric: mysql_innodb, field: innodb_dblwr_writes

-  metric: mysql_innodb, field: innodb_page_size

-  metric: mysql_innodb, field: innodb_rwlock_s_os_waits

-  metric: mysql_innodb, field: innodb_rwlock_s_spin_rounds

-  metric: mysql_innodb, field: innodb_rwlock_s_spin_waits

-  metric: mysql_innodb, field: innodb_rwlock_sx_os_waits

-  metric: mysql_innodb, field: innodb_rwlock_sx_spin_rounds

-  metric: mysql_innodb, field: innodb_rwlock_sx_spin_waits

-  metric: mysql_innodb, field: innodb_rwlock_x_os_waits

-  metric: mysql_innodb, field: innodb_rwlock_x_spin_rounds

-  metric: mysql_innodb, field: innodb_rwlock_x_spin_waits

-  metric: mysql_innodb, field: lock_deadlock_false_positives

-  metric: mysql_innodb, field: lock_deadlock_rounds

-  metric: mysql_innodb, field: lock_rec_grant_attempts

-  metric: mysql_innodb, field: lock_rec_release_attempts

-  metric: mysql_innodb, field: lock_row_lock_current_waits

-  metric: mysql_innodb, field: lock_row_lock_time

-  metric: mysql_innodb, field: lock_row_lock_time_max

-  metric: mysql_innodb, field: lock_row_lock_waits

-  metric: mysql_innodb, field: lock_schedule_refreshes

-  metric: mysql_innodb, field: lock_threads_waiting

-  metric: mysql_innodb, field: lock_timeouts

-  metric: mysql, field: innodb_log_waits

-  metric: mysql_innodb, field: log_waits

-  metric: mysql, field: innodb_log_write_requests

-  metric: mysql_innodb, field: log_write_requests

-  metric: mysql, field: innodb_log_writes

-  metric: mysql_innodb, field: log_writes

-  metric: mysql, field: innodb_num_open_files

-  metric: mysql_innodb, field: os_data_fsyncs

-  metric: mysql_innodb, field: os_log_bytes_written

-  metric: mysql, field: innodb_os_log_fsyncs

-  metric: mysql_innodb, field: os_log_fsyncs

-  metric: mysql, field: innodb_os_log_pending_fsyncs

-  metric: mysql_innodb, field: os_log_pending_fsyncs

-  metric: mysql, field: innodb_os_log_pending_writes

-  metric: mysql_innodb, field: os_log_pending_writes

-  metric: mysql, field: innodb_os_log_written

-  metric: mysql, field: innodb_pages_created

-  metric: mysql, field: innodb_page_size

-  metric: mysql, field: innodb_pages_read

-  metric: mysql, field: innodb_pages_written

-  metric: mysql, field: innodb_redo_log_enabled

-  metric: mysql, field: innodb_row_lock_current_waits

-  metric: mysql, field: innodb_row_lock_time

-  metric: mysql, field: innodb_row_lock_time_avg

-  metric: mysql, field: innodb_row_lock_time_max

-  metric: mysql, field: innodb_row_lock_waits

-  metric: mysql, field: innodb_rows_deleted

-  metric: mysql, field: innodb_rows_inserted

-  metric: mysql, field: innodb_rows_read

-  metric: mysql, field: innodb_rows_updated

-  metric: mysql, field: innodb_sampled_pages_read

-  metric: mysql, field: innodb_sampled_pages_skipped

-  metric: mysql, field: innodb_system_rows_deleted

-  metric: mysql, field: innodb_system_rows_inserted

-  metric: mysql, field: innodb_system_rows_read

-  metric: mysql, field: innodb_system_rows_updated

-  metric: mysql, field: innodb_truncated_status_writes

-  metric: mysql_innodb, field: trx_rseg_history_len

-  metric: mysql, field: innodb_undo_tablespaces_active

-  metric: mysql, field: innodb_undo_tablespaces_explicit

-  metric: mysql, field: innodb_undo_tablespaces_implicit

-  metric: mysql, field: innodb_undo_tablespaces_total

-  metric: mysql, field: key_blocks_not_flushed

-  metric: mysql, field: key_blocks_unused

-  metric: mysql, field: key_blocks_used

-  metric: mysql, field: key_read_requests

-  metric: mysql, field: key_reads

-  metric: mysql, field: key_write_requests

-  metric: mysql, field: key_writes

-  metric: mysql, field: locked_connects

-  metric: mysql, field: max_execution_time_set

-  metric: mysql, field: max_execution_time_set_failed

-  metric: mysql, field: max_used_connections

-  metric: mysql, field: performance_schema_memory_classes_lost

-  metric: mysql, field: performance_schema_metadata_lock_lost

-  metric: mysql, field: performance_schema_mutex_classes_lost

-  metric: mysql, field: performance_schema_mutex_instances_lost

-  metric: mysql, field: performance_schema_nested_statement_lost

-  metric: mysql, field: performance_schema_prepared_statements_lost

-  metric: mysql, field: performance_schema_program_lost

-  metric: mysql, field: performance_schema_rwlock_classes_lost

-  metric: mysql, field: performance_schema_rwlock_instances_lost

-  metric: mysql, field:
   performance_schema_session_connect_attrs_longest_seen

-  metric: mysql, field: performance_schema_session_connect_attrs_lost

-  metric: mysql, field: performance_schema_socket_classes_lost

-  metric: mysql, field: performance_schema_socket_instances_lost

-  metric: mysql, field: performance_schema_stage_classes_lost

-  metric: mysql, field: performance_schema_statement_classes_lost

-  metric: mysql, field: performance_schema_table_handles_lost

-  metric: mysql, field: performance_schema_table_instances_lost

-  metric: mysql, field: performance_schema_table_lock_stat_lost

-  metric: mysql, field: performance_schema_thread_classes_lost

-  metric: mysql, field: performance_schema_thread_instances_lost

-  metric: mysql_process_list, field: threads_after_create

-  metric: mysql_process_list, field: threads_altering_table

-  metric: mysql_process_list, field: threads_analyzing

-  metric: mysql_process_list, field: threads_checking_permissions

-  metric: mysql_process_list, field: threads_checking_table

-  metric: mysql_process_list, field: threads_cleaning_up

-  metric: mysql_process_list, field: threads_closing_tables

-  metric: mysql_process_list, field: threads_converting_heap_to_myisam

-  metric: mysql_process_list, field: threads_copying_to_tmp_table

-  metric: mysql_process_list, field: threads_creating_sort_index

-  metric: mysql_process_list, field: threads_creating_table

-  metric: mysql_process_list, field: threads_creating_tmp_table

-  metric: mysql_process_list, field: threads_deleting

-  metric: mysql_process_list, field: threads_end

-  metric: mysql_process_list, field: threads_executing

-  metric: mysql_process_list, field: threads_execution_of_init_command

-  metric: mysql_process_list, field: threads_flushing_tables

-  metric: mysql_process_list, field: threads_freeing_items

-  metric: mysql_process_list, field: threads_fulltext_initialization

-  metric: mysql_process_list, field: threads_idle

-  metric: mysql_process_list, field: threads_init

-  metric: mysql_process_list, field: threads_killed

-  metric: mysql_process_list, field: threads_logging_slow_query

-  metric: mysql_process_list, field: threads_login

-  metric: mysql_process_list, field: threads_manage_keys

-  metric: mysql_process_list, field: threads_opening_tables

-  metric: mysql_process_list, field: threads_optimizing

-  metric: mysql_process_list, field: threads_other

-  metric: mysql_process_list, field: threads_preparing

-  metric: mysql_process_list, field: threads_reading_from_net

-  metric: mysql_process_list, field: threads_removing_duplicates

-  metric: mysql_process_list, field: threads_removing_tmp_table

-  metric: mysql_process_list, field: threads_reopen_tables

-  metric: mysql_process_list, field: threads_repair_by_sorting

-  metric: mysql_process_list, field: threads_repair_done

-  metric: mysql_process_list, field: threads_repair_with_keycache

-  metric: mysql_process_list, field: threads_replication_master

-  metric: mysql_process_list, field: threads_rolling_back

-  metric: mysql_process_list, field: threads_searching_rows_for_update

-  metric: mysql_process_list, field: threads_sending_data

-  metric: mysql_process_list, field: threads_sorting_for_group

-  metric: mysql_process_list, field: threads_sorting_for_order

-  metric: mysql_process_list, field: threads_sorting_index

-  metric: mysql_process_list, field: threads_sorting_result

-  metric: mysql_process_list, field: threads_statistics

-  metric: mysql_process_list, field: threads_updating

-  metric: mysql_process_list, field: threads_waiting_for_lock

-  metric: mysql_process_list, field: threads_waiting_for_table_flush

-  metric: mysql_process_list, field: threads_waiting_for_tables

-  metric: mysql_process_list, field: threads_waiting_on_cond

-  metric: mysql_process_list, field: threads_writing_to_net

-  metric: mysql, field: secondary_engine_execution_count

-  metric: mysql, field: select_full_join

-  metric: mysql, field: select_full_range_join

-  metric: mysql, field: select_range

-  metric: mysql, field: select_range_check

-  metric: mysql, field: select_scan

-  metric: mysql, field: slave_open_temp_tables

-  metric: mysql, field: slow_launch_threads

-  metric: mysql, field: sort_merge_passes

-  metric: mysql, field: sort_range

-  metric: mysql, field: sort_rows

-  metric: mysql, field: sort_scan

-  metric: mysql, field: ssl_accept_renegotiates

-  metric: mysql, field: ssl_accepts

-  metric: mysql, field: ssl_callback_cache_hits

-  metric: mysql, field: ssl_client_connects

-  metric: mysql, field: ssl_connect_renegotiates

-  metric: mysql, field: table_open_cache_hits

-  metric: mysql, field: table_open_cache_misses

-  metric: mysql, field: table_open_cache_overflows

-  metric: mysql, field: tc_log_max_pages_used

-  metric: mysql, field: tc_log_page_size

-  metric: mysql, field: tc_log_page_waits

-  metric: mysql, field: threads_cached

-  metric: mysql, field: threads_connected

-  metric: mysql, field: threads_created

-  metric: mysql, field: threads_running

-  metric: mysql, field: uptime_since_flush_status

.. _h_7b265f708c:

Additional metrics for Aiven for Cassandra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  metric: org.apache.cassandra.metrics:Cache.Capacity, field: Value

-  metric: org.apache.cassandra.metrics:Cache.FifteenMinuteHitRate,
   field: Value

-  metric: org.apache.cassandra.metrics:Cache.FiveMinuteHitRate, field:
   Value

-  metric: org.apache.cassandra.metrics:Cache.Hits, field: Count

-  metric: org.apache.cassandra.metrics:Cache.Hits, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Cache.Hits, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Cache.Hits, field: MeanRate

-  metric: org.apache.cassandra.metrics:Cache.Hits, field: OneMinuteRate

-  metric: org.apache.cassandra.metrics:Cache.Misses, field: Count

-  metric: org.apache.cassandra.metrics:Cache.Misses, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Cache.Misses, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Cache.Misses, field: MeanRate

-  metric: org.apache.cassandra.metrics:Cache.Misses, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:Cache.MissLatency, field:
   50thPercentile

-  metric: org.apache.cassandra.metrics:Cache.MissLatency, field:
   75thPercentile

-  metric: org.apache.cassandra.metrics:Cache.MissLatency, field:
   98thPercentile

-  metric: org.apache.cassandra.metrics:Cache.MissLatency, field:
   999thPercentile

-  metric: org.apache.cassandra.metrics:Cache.MissLatency, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Cache.MissLatency, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Cache.MissLatency, field: Max

-  metric: org.apache.cassandra.metrics:Cache.MissLatency, field:
   MeanRate

-  metric: org.apache.cassandra.metrics:Cache.MissLatency, field: Min

-  metric: org.apache.cassandra.metrics:Cache.MissLatency, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:Cache.MissLatency, field: StdDev

-  metric: org.apache.cassandra.metrics:Cache.OneMinuteHitRate, field:
   Value

-  metric: org.apache.cassandra.metrics:Cache.Requests, field: Count

-  metric: org.apache.cassandra.metrics:Cache.Requests, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Cache.Requests, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Cache.Requests, field: MeanRate

-  metric: org.apache.cassandra.metrics:Cache.Requests, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:Client.AuthFailure, field: Count

-  metric: org.apache.cassandra.metrics:Client.AuthFailure, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Client.AuthFailure, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Client.AuthFailure, field:
   MeanRate

-  metric: org.apache.cassandra.metrics:Client.AuthFailure, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:Client.AuthSuccess, field: Count

-  metric: org.apache.cassandra.metrics:Client.AuthSuccess, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Client.AuthSuccess, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Client.AuthSuccess, field:
   MeanRate

-  metric: org.apache.cassandra.metrics:Client.AuthSuccess, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:Client.PausedConnections, field:
   Value

-  metric: org.apache.cassandra.metrics:ClientRequest.ConditionNotMet,
   field: Count

-  metric:
   org.apache.cassandra.metrics:ClientRequest.ContentionHistogram,
   field: 50thPercentile

-  metric:
   org.apache.cassandra.metrics:ClientRequest.ContentionHistogram,
   field: 75thPercentile

-  metric:
   org.apache.cassandra.metrics:ClientRequest.ContentionHistogram,
   field: 95thPercentile

-  metric:
   org.apache.cassandra.metrics:ClientRequest.ContentionHistogram,
   field: 98thPercentile

-  metric:
   org.apache.cassandra.metrics:ClientRequest.ContentionHistogram,
   field: 999thPercentile

-  metric:
   org.apache.cassandra.metrics:ClientRequest.ContentionHistogram,
   field: 99thPercentile

-  metric:
   org.apache.cassandra.metrics:ClientRequest.ContentionHistogram,
   field: Count

-  metric:
   org.apache.cassandra.metrics:ClientRequest.ContentionHistogram,
   field: Max

-  metric:
   org.apache.cassandra.metrics:ClientRequest.ContentionHistogram,
   field: Min

-  metric:
   org.apache.cassandra.metrics:ClientRequest.ContentionHistogram,
   field: StdDev

-  metric: org.apache.cassandra.metrics:Client.RequestDiscarded, field:
   Count

-  metric: org.apache.cassandra.metrics:Client.RequestDiscarded, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Client.RequestDiscarded, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Client.RequestDiscarded, field:
   MeanRate

-  metric: org.apache.cassandra.metrics:Client.RequestDiscarded, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:ClientRequest.Failures, field:
   Count

-  metric: org.apache.cassandra.metrics:ClientRequest.Failures, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:ClientRequest.Failures, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:ClientRequest.Failures, field:
   MeanRate

-  metric: org.apache.cassandra.metrics:ClientRequest.Failures, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:ClientRequest.Latency, field:
   50thPercentile

-  metric: org.apache.cassandra.metrics:ClientRequest.Latency, field:
   75thPercentile

-  metric: org.apache.cassandra.metrics:ClientRequest.Latency, field:
   95thPercentile

-  metric: org.apache.cassandra.metrics:ClientRequest.Latency, field:
   98thPercentile

-  metric: org.apache.cassandra.metrics:ClientRequest.Latency, field:
   999thPercentile

-  metric: org.apache.cassandra.metrics:ClientRequest.Latency, field:
   99thPercentile

-  metric: org.apache.cassandra.metrics:ClientRequest.Latency, field:
   Count

-  metric: org.apache.cassandra.metrics:ClientRequest.Latency, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:ClientRequest.Latency, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:ClientRequest.Latency, field:
   Max

-  metric: org.apache.cassandra.metrics:ClientRequest.Latency, field:
   Mean

-  metric: org.apache.cassandra.metrics:ClientRequest.Latency, field:
   MeanRate

-  metric: org.apache.cassandra.metrics:ClientRequest.Latency, field:
   Min

-  metric: org.apache.cassandra.metrics:ClientRequest.Latency, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:ClientRequest.Latency, field:
   StdDev

-  metric: org.apache.cassandra.metrics:ClientRequest.Timeouts, field:
   Count

-  metric: org.apache.cassandra.metrics:ClientRequest.Timeouts, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:ClientRequest.Timeouts, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:ClientRequest.Timeouts, field:
   MeanRate

-  metric: org.apache.cassandra.metrics:ClientRequest.Timeouts, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:ClientRequest.TotalLatency,
   field: Count

-  metric: org.apache.cassandra.metrics:ClientRequest.Unavailables,
   field: Count

-  metric: org.apache.cassandra.metrics:ClientRequest.Unavailables,
   field: FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:ClientRequest.Unavailables,
   field: FiveMinuteRate

-  metric: org.apache.cassandra.metrics:ClientRequest.Unavailables,
   field: MeanRate

-  metric: org.apache.cassandra.metrics:ClientRequest.Unavailables,
   field: OneMinuteRate

-  metric: org.apache.cassandra.metrics:ClientRequest.UnfinishedCommit,
   field: Count

-  metric:
   org.apache.cassandra.metrics:ClientRequest.ViewPendingMutations,
   field: Value

-  metric:
   org.apache.cassandra.metrics:ClientRequest.ViewReplicasAttempted,
   field: Count

-  metric:
   org.apache.cassandra.metrics:ClientRequest.ViewReplicasSuccess,
   field: Count

-  metric: org.apache.cassandra.metrics:ClientRequest.ViewWriteLatency,
   field: 50thPercentile

-  metric: org.apache.cassandra.metrics:ClientRequest.ViewWriteLatency,
   field: 75thPercentile

-  metric: org.apache.cassandra.metrics:ClientRequest.ViewWriteLatency,
   field: 95thPercentile

-  metric: org.apache.cassandra.metrics:ClientRequest.ViewWriteLatency,
   field: 98thPercentile

-  metric: org.apache.cassandra.metrics:ClientRequest.ViewWriteLatency,
   field: 999thPercentile

-  metric: org.apache.cassandra.metrics:ClientRequest.ViewWriteLatency,
   field: 99thPercentile

-  metric: org.apache.cassandra.metrics:ClientRequest.ViewWriteLatency,
   field: Count

-  metric: org.apache.cassandra.metrics:ClientRequest.ViewWriteLatency,
   field: FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:ClientRequest.ViewWriteLatency,
   field: FiveMinuteRate

-  metric: org.apache.cassandra.metrics:ClientRequest.ViewWriteLatency,
   field: Max

-  metric: org.apache.cassandra.metrics:ClientRequest.ViewWriteLatency,
   field: MeanRate

-  metric: org.apache.cassandra.metrics:ClientRequest.ViewWriteLatency,
   field: Min

-  metric: org.apache.cassandra.metrics:ClientRequest.ViewWriteLatency,
   field: OneMinuteRate

-  metric: org.apache.cassandra.metrics:ClientRequest.ViewWriteLatency,
   field: StdDev

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.AllMemtablesHeapSize,
   field: Value

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.AllMemtablesOffHeapSize,
   field: Value

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.BloomFilterDiskSpaceUsed,
   field: Value

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.BloomFilterFalsePositives,
   field: Value

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.BloomFilterFalseRatio,
   field: Value

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.BloomFilterOffHeapMemoryUsed,
   field: Value

-  metric: org.apache.cassandra.metrics:ColumnFamily.BytesFlushed,
   field: Count

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ColUpdateTimeDeltaHistogram,
   field: 50thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ColUpdateTimeDeltaHistogram,
   field: 75thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ColUpdateTimeDeltaHistogram,
   field: 95thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ColUpdateTimeDeltaHistogram,
   field: 98thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ColUpdateTimeDeltaHistogram,
   field: 999thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ColUpdateTimeDeltaHistogram,
   field: 99thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ColUpdateTimeDeltaHistogram,
   field: Count

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ColUpdateTimeDeltaHistogram,
   field: Max

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ColUpdateTimeDeltaHistogram,
   field: Mean

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ColUpdateTimeDeltaHistogram,
   field: Min

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ColUpdateTimeDeltaHistogram,
   field: StdDev

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.CompactionBytesWritten,
   field: Count

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.CompressionMetadataOffHeapMemoryUsed,
   field: Value

-  metric: org.apache.cassandra.metrics:ColumnFamily.DroppedMutations,
   field: Count

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.IndexSummaryOffHeapMemoryUsed,
   field: Value

-  metric: org.apache.cassandra.metrics:ColumnFamily.KeyCacheHitRate,
   field: Value

-  metric: org.apache.cassandra.metrics:ColumnFamily.LiveDiskSpaceUsed,
   field: Count

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.LiveScannedHistogram,
   field: 50thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.LiveScannedHistogram,
   field: 75thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.LiveScannedHistogram,
   field: 95thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.LiveScannedHistogram,
   field: 98thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.LiveScannedHistogram,
   field: 999thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.LiveScannedHistogram,
   field: 99thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.LiveScannedHistogram,
   field: Count

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.LiveScannedHistogram,
   field: Max

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.LiveScannedHistogram,
   field: Mean

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.LiveScannedHistogram,
   field: Min

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.LiveScannedHistogram,
   field: StdDev

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.MemtableColumnsCount,
   field: Value

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.MemtableLiveDataSize,
   field: Value

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.MemtableOffHeapSize, field:
   Value

-  metric: org.apache.cassandra.metrics:ColumnFamily.MemtableOnHeapSize,
   field: Value

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.MemtableSwitchCount, field:
   Count

-  metric: org.apache.cassandra.metrics:ColumnFamily.MinRowSize, field:
   Value

-  metric: org.apache.cassandra.metrics:ColumnFamily.PendingFlushes,
   field: Count

-  metric: org.apache.cassandra.metrics:ColumnFamily.PercentRepaired,
   field: Value

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.RecentBloomFilterFalsePositives,
   field: Value

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.RecentBloomFilterFalseRatio,
   field: Value

-  metric: org.apache.cassandra.metrics:ColumnFamily.RowCacheHit, field:
   Count

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.RowCacheHitOutOfRange,
   field: Count

-  metric: org.apache.cassandra.metrics:ColumnFamily.RowCacheMiss,
   field: Count

-  metric: org.apache.cassandra.metrics:ColumnFamily.SnapshotsSize,
   field: Value

-  metric: org.apache.cassandra.metrics:ColumnFamily.SpeculativeRetries,
   field: Count

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.SSTablesPerReadHistogram,
   field: 50thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.SSTablesPerReadHistogram,
   field: 75thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.SSTablesPerReadHistogram,
   field: 95thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.SSTablesPerReadHistogram,
   field: 98thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.SSTablesPerReadHistogram,
   field: 999thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.SSTablesPerReadHistogram,
   field: 99thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.SSTablesPerReadHistogram,
   field: Count

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.SSTablesPerReadHistogram,
   field: Max

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.SSTablesPerReadHistogram,
   field: Mean

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.SSTablesPerReadHistogram,
   field: Min

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.SSTablesPerReadHistogram,
   field: StdDev

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.TombstoneScannedHistogram,
   field: 50thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.TombstoneScannedHistogram,
   field: 75thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.TombstoneScannedHistogram,
   field: 95thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.TombstoneScannedHistogram,
   field: 98thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.TombstoneScannedHistogram,
   field: 999thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.TombstoneScannedHistogram,
   field: 99thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.TombstoneScannedHistogram,
   field: Count

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.TombstoneScannedHistogram,
   field: Max

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.TombstoneScannedHistogram,
   field: Mean

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.TombstoneScannedHistogram,
   field: Min

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.TombstoneScannedHistogram,
   field: StdDev

-  metric: org.apache.cassandra.metrics:ColumnFamily.TotalDiskSpaceUsed,
   field: Count

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ViewLockAcquireTime, field:
   50thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ViewLockAcquireTime, field:
   75thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ViewLockAcquireTime, field:
   95thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ViewLockAcquireTime, field:
   98thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ViewLockAcquireTime, field:
   999thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ViewLockAcquireTime, field:
   99thPercentile

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ViewLockAcquireTime, field:
   Count

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ViewLockAcquireTime, field:
   FifteenMinuteRate

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ViewLockAcquireTime, field:
   FiveMinuteRate

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ViewLockAcquireTime, field:
   Max

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ViewLockAcquireTime, field:
   MeanRate

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ViewLockAcquireTime, field:
   Min

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ViewLockAcquireTime, field:
   OneMinuteRate

-  metric:
   org.apache.cassandra.metrics:ColumnFamily.ViewLockAcquireTime, field:
   StdDev

-  metric: org.apache.cassandra.metrics:ColumnFamily.ViewReadTime,
   field: 50thPercentile

-  metric: org.apache.cassandra.metrics:ColumnFamily.ViewReadTime,
   field: 75thPercentile

-  metric: org.apache.cassandra.metrics:ColumnFamily.ViewReadTime,
   field: 95thPercentile

-  metric: org.apache.cassandra.metrics:ColumnFamily.ViewReadTime,
   field: 98thPercentile

-  metric: org.apache.cassandra.metrics:ColumnFamily.ViewReadTime,
   field: 999thPercentile

-  metric: org.apache.cassandra.metrics:ColumnFamily.ViewReadTime,
   field: 99thPercentile

-  metric: org.apache.cassandra.metrics:ColumnFamily.ViewReadTime,
   field: Count

-  metric: org.apache.cassandra.metrics:ColumnFamily.ViewReadTime,
   field: FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:ColumnFamily.ViewReadTime,
   field: FiveMinuteRate

-  metric: org.apache.cassandra.metrics:ColumnFamily.ViewReadTime,
   field: Max

-  metric: org.apache.cassandra.metrics:ColumnFamily.ViewReadTime,
   field: MeanRate

-  metric: org.apache.cassandra.metrics:ColumnFamily.ViewReadTime,
   field: Min

-  metric: org.apache.cassandra.metrics:ColumnFamily.ViewReadTime,
   field: OneMinuteRate

-  metric: org.apache.cassandra.metrics:ColumnFamily.ViewReadTime,
   field: StdDev

-  metric: org.apache.cassandra.metrics:CommitLog.CompletedTasks, field:
   Value

-  metric: org.apache.cassandra.metrics:CommitLog.WaitingOnCommit,
   field: 50thPercentile

-  metric: org.apache.cassandra.metrics:CommitLog.WaitingOnCommit,
   field: 75thPercentile

-  metric: org.apache.cassandra.metrics:CommitLog.WaitingOnCommit,
   field: 98thPercentile

-  metric: org.apache.cassandra.metrics:CommitLog.WaitingOnCommit,
   field: 999thPercentile

-  metric: org.apache.cassandra.metrics:CommitLog.WaitingOnCommit,
   field: FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:CommitLog.WaitingOnCommit,
   field: FiveMinuteRate

-  metric: org.apache.cassandra.metrics:CommitLog.WaitingOnCommit,
   field: Max

-  metric: org.apache.cassandra.metrics:CommitLog.WaitingOnCommit,
   field: MeanRate

-  metric: org.apache.cassandra.metrics:CommitLog.WaitingOnCommit,
   field: Min

-  metric: org.apache.cassandra.metrics:CommitLog.WaitingOnCommit,
   field: OneMinuteRate

-  metric: org.apache.cassandra.metrics:CommitLog.WaitingOnCommit,
   field: StdDev

-  metric:
   org.apache.cassandra.metrics:CommitLog.WaitingOnSegmentAllocation,
   field: 50thPercentile

-  metric:
   org.apache.cassandra.metrics:CommitLog.WaitingOnSegmentAllocation,
   field: 75thPercentile

-  metric:
   org.apache.cassandra.metrics:CommitLog.WaitingOnSegmentAllocation,
   field: 98thPercentile

-  metric:
   org.apache.cassandra.metrics:CommitLog.WaitingOnSegmentAllocation,
   field: 999thPercentile

-  metric:
   org.apache.cassandra.metrics:CommitLog.WaitingOnSegmentAllocation,
   field: FifteenMinuteRate

-  metric:
   org.apache.cassandra.metrics:CommitLog.WaitingOnSegmentAllocation,
   field: FiveMinuteRate

-  metric:
   org.apache.cassandra.metrics:CommitLog.WaitingOnSegmentAllocation,
   field: Max

-  metric:
   org.apache.cassandra.metrics:CommitLog.WaitingOnSegmentAllocation,
   field: MeanRate

-  metric:
   org.apache.cassandra.metrics:CommitLog.WaitingOnSegmentAllocation,
   field: Min

-  metric:
   org.apache.cassandra.metrics:CommitLog.WaitingOnSegmentAllocation,
   field: OneMinuteRate

-  metric:
   org.apache.cassandra.metrics:CommitLog.WaitingOnSegmentAllocation,
   field: StdDev

-  metric: org.apache.cassandra.metrics:Compaction.BytesCompacted,
   field: Count

-  metric: org.apache.cassandra.metrics:Compaction.CompletedTasks,
   field: Value

-  metric: org.apache.cassandra.metrics:Compaction.PendingTasks, field:
   Value

-  metric:
   org.apache.cassandra.metrics:Compaction.TotalCompactionsCompleted,
   field: Count

-  metric:
   org.apache.cassandra.metrics:Compaction.TotalCompactionsCompleted,
   field: FifteenMinuteRate

-  metric:
   org.apache.cassandra.metrics:Compaction.TotalCompactionsCompleted,
   field: FiveMinuteRate

-  metric:
   org.apache.cassandra.metrics:Compaction.TotalCompactionsCompleted,
   field: MeanRate

-  metric:
   org.apache.cassandra.metrics:Compaction.TotalCompactionsCompleted,
   field: OneMinuteRate

-  metric: org.apache.cassandra.metrics:CQL.PreparedStatementsCount,
   field: Value

-  metric: org.apache.cassandra.metrics:CQL.PreparedStatementsEvicted,
   field: Count

-  metric: org.apache.cassandra.metrics:CQL.PreparedStatementsExecuted,
   field: Count

-  metric: org.apache.cassandra.metrics:CQL.PreparedStatementsRatio,
   field: Value

-  metric: org.apache.cassandra.metrics:CQL.RegularStatementsExecuted,
   field: Count

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.CrossNodeDroppedLatency,
   field: 50thPercentile

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.CrossNodeDroppedLatency,
   field: 75thPercentile

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.CrossNodeDroppedLatency,
   field: 95thPercentile

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.CrossNodeDroppedLatency,
   field: 98thPercentile

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.CrossNodeDroppedLatency,
   field: 999thPercentile

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.CrossNodeDroppedLatency,
   field: 99thPercentile

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.CrossNodeDroppedLatency,
   field: Count

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.CrossNodeDroppedLatency,
   field: FifteenMinuteRate

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.CrossNodeDroppedLatency,
   field: FiveMinuteRate

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.CrossNodeDroppedLatency,
   field: Max

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.CrossNodeDroppedLatency,
   field: MeanRate

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.CrossNodeDroppedLatency,
   field: Min

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.CrossNodeDroppedLatency,
   field: OneMinuteRate

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.CrossNodeDroppedLatency,
   field: StdDev

-  metric: org.apache.cassandra.metrics:DroppedMessage.Dropped, field:
   Count

-  metric: org.apache.cassandra.metrics:DroppedMessage.Dropped, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:DroppedMessage.Dropped, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:DroppedMessage.Dropped, field:
   MeanRate

-  metric: org.apache.cassandra.metrics:DroppedMessage.Dropped, field:
   OneMinuteRate

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.InternalDroppedLatency,
   field: 50thPercentile

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.InternalDroppedLatency,
   field: 75thPercentile

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.InternalDroppedLatency,
   field: 95thPercentile

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.InternalDroppedLatency,
   field: 98thPercentile

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.InternalDroppedLatency,
   field: 999thPercentile

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.InternalDroppedLatency,
   field: 99thPercentile

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.InternalDroppedLatency,
   field: Count

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.InternalDroppedLatency,
   field: FifteenMinuteRate

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.InternalDroppedLatency,
   field: FiveMinuteRate

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.InternalDroppedLatency,
   field: Max

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.InternalDroppedLatency,
   field: MeanRate

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.InternalDroppedLatency,
   field: Min

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.InternalDroppedLatency,
   field: OneMinuteRate

-  metric:
   org.apache.cassandra.metrics:DroppedMessage.InternalDroppedLatency,
   field: StdDev

-  metric: org.apache.cassandra.metrics:Storage.Exceptions, field: Count

-  metric: org.apache.cassandra.metrics:Storage.Load, field: Count

-  metric: org.apache.cassandra.metrics:Storage.TotalHintsInProgress,
   field: Count

-  metric: org.apache.cassandra.metrics:Table.AllMemtablesHeapSize,
   field: Value

-  metric: org.apache.cassandra.metrics:Table.AllMemtablesLiveDataSize,
   field: Value

-  metric: org.apache.cassandra.metrics:Table.AllMemtablesOffHeapSize,
   field: Value

-  metric: org.apache.cassandra.metrics:Table.BloomFilterDiskSpaceUsed,
   field: Value

-  metric: org.apache.cassandra.metrics:Table.BloomFilterFalsePositives,
   field: Value

-  metric: org.apache.cassandra.metrics:Table.BloomFilterFalseRatio,
   field: Value

-  metric:
   org.apache.cassandra.metrics:Table.BloomFilterOffHeapMemoryUsed,
   field: Value

-  metric: org.apache.cassandra.metrics:Table.BytesFlushed, field: Count

-  metric: org.apache.cassandra.metrics:Table.CasCommitLatency, field:
   50thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasCommitLatency, field:
   75thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasCommitLatency, field:
   95thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasCommitLatency, field:
   98thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasCommitLatency, field:
   999thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasCommitLatency, field:
   99thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasCommitLatency, field:
   Count

-  metric: org.apache.cassandra.metrics:Table.CasCommitLatency, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Table.CasCommitLatency, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Table.CasCommitLatency, field:
   Max

-  metric: org.apache.cassandra.metrics:Table.CasCommitLatency, field:
   MeanRate

-  metric: org.apache.cassandra.metrics:Table.CasCommitLatency, field:
   Min

-  metric: org.apache.cassandra.metrics:Table.CasCommitLatency, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:Table.CasCommitLatency, field:
   StdDev

-  metric: org.apache.cassandra.metrics:Table.CasCommitTotalLatency,
   field: Count

-  metric: org.apache.cassandra.metrics:Table.CasPrepareLatency, field:
   50thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasPrepareLatency, field:
   75thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasPrepareLatency, field:
   95thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasPrepareLatency, field:
   98thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasPrepareLatency, field:
   999thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasPrepareLatency, field:
   99thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasPrepareLatency, field:
   Count

-  metric: org.apache.cassandra.metrics:Table.CasPrepareLatency, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Table.CasPrepareLatency, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Table.CasPrepareLatency, field:
   Max

-  metric: org.apache.cassandra.metrics:Table.CasPrepareLatency, field:
   MeanRate

-  metric: org.apache.cassandra.metrics:Table.CasPrepareLatency, field:
   Min

-  metric: org.apache.cassandra.metrics:Table.CasPrepareLatency, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:Table.CasPrepareLatency, field:
   StdDev

-  metric: org.apache.cassandra.metrics:Table.CasPrepareTotalLatency,
   field: Count

-  metric: org.apache.cassandra.metrics:Table.CasProposeLatency, field:
   50thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasProposeLatency, field:
   75thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasProposeLatency, field:
   95thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasProposeLatency, field:
   98thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasProposeLatency, field:
   999thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasProposeLatency, field:
   99thPercentile

-  metric: org.apache.cassandra.metrics:Table.CasProposeLatency, field:
   Count

-  metric: org.apache.cassandra.metrics:Table.CasProposeLatency, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Table.CasProposeLatency, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Table.CasProposeLatency, field:
   Max

-  metric: org.apache.cassandra.metrics:Table.CasProposeLatency, field:
   MeanRate

-  metric: org.apache.cassandra.metrics:Table.CasProposeLatency, field:
   Min

-  metric: org.apache.cassandra.metrics:Table.CasProposeLatency, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:Table.CasProposeLatency, field:
   StdDev

-  metric: org.apache.cassandra.metrics:Table.CasProposeTotalLatency,
   field: Count

-  metric:
   org.apache.cassandra.metrics:Table.ColUpdateTimeDeltaHistogram,
   field: 50thPercentile

-  metric:
   org.apache.cassandra.metrics:Table.ColUpdateTimeDeltaHistogram,
   field: 75thPercentile

-  metric:
   org.apache.cassandra.metrics:Table.ColUpdateTimeDeltaHistogram,
   field: 95thPercentile

-  metric:
   org.apache.cassandra.metrics:Table.ColUpdateTimeDeltaHistogram,
   field: 98thPercentile

-  metric:
   org.apache.cassandra.metrics:Table.ColUpdateTimeDeltaHistogram,
   field: 999thPercentile

-  metric:
   org.apache.cassandra.metrics:Table.ColUpdateTimeDeltaHistogram,
   field: 99thPercentile

-  metric:
   org.apache.cassandra.metrics:Table.ColUpdateTimeDeltaHistogram,
   field: Count

-  metric:
   org.apache.cassandra.metrics:Table.ColUpdateTimeDeltaHistogram,
   field: Max

-  metric:
   org.apache.cassandra.metrics:Table.ColUpdateTimeDeltaHistogram,
   field: Mean

-  metric:
   org.apache.cassandra.metrics:Table.ColUpdateTimeDeltaHistogram,
   field: Min

-  metric:
   org.apache.cassandra.metrics:Table.ColUpdateTimeDeltaHistogram,
   field: StdDev

-  metric: org.apache.cassandra.metrics:Table.CompactionBytesWritten,
   field: Count

-  metric:
   org.apache.cassandra.metrics:Table.CompressionMetadataOffHeapMemoryUsed,
   field: Value

-  metric: org.apache.cassandra.metrics:Table.CompressionRatio, field:
   Value

-  metric: org.apache.cassandra.metrics:Table.CoordinatorReadLatency,
   field: 50thPercentile

-  metric: org.apache.cassandra.metrics:Table.CoordinatorReadLatency,
   field: 75thPercentile

-  metric: org.apache.cassandra.metrics:Table.CoordinatorReadLatency,
   field: 95thPercentile

-  metric: org.apache.cassandra.metrics:Table.CoordinatorReadLatency,
   field: 98thPercentile

-  metric: org.apache.cassandra.metrics:Table.CoordinatorReadLatency,
   field: 999thPercentile

-  metric: org.apache.cassandra.metrics:Table.CoordinatorReadLatency,
   field: 99thPercentile

-  metric: org.apache.cassandra.metrics:Table.CoordinatorReadLatency,
   field: Count

-  metric: org.apache.cassandra.metrics:Table.CoordinatorReadLatency,
   field: FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Table.CoordinatorReadLatency,
   field: FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Table.CoordinatorReadLatency,
   field: Max

-  metric: org.apache.cassandra.metrics:Table.CoordinatorReadLatency,
   field: Mean

-  metric: org.apache.cassandra.metrics:Table.CoordinatorReadLatency,
   field: MeanRate

-  metric: org.apache.cassandra.metrics:Table.CoordinatorReadLatency,
   field: Min

-  metric: org.apache.cassandra.metrics:Table.CoordinatorReadLatency,
   field: OneMinuteRate

-  metric: org.apache.cassandra.metrics:Table.CoordinatorReadLatency,
   field: StdDev

-  metric: org.apache.cassandra.metrics:Table.CoordinatorScanLatency,
   field: 50thPercentile

-  metric: org.apache.cassandra.metrics:Table.CoordinatorScanLatency,
   field: 75thPercentile

-  metric: org.apache.cassandra.metrics:Table.CoordinatorScanLatency,
   field: 95thPercentile

-  metric: org.apache.cassandra.metrics:Table.CoordinatorScanLatency,
   field: 98thPercentile

-  metric: org.apache.cassandra.metrics:Table.CoordinatorScanLatency,
   field: 999thPercentile

-  metric: org.apache.cassandra.metrics:Table.CoordinatorScanLatency,
   field: 99thPercentile

-  metric: org.apache.cassandra.metrics:Table.CoordinatorScanLatency,
   field: Count

-  metric: org.apache.cassandra.metrics:Table.CoordinatorScanLatency,
   field: FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Table.CoordinatorScanLatency,
   field: FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Table.CoordinatorScanLatency,
   field: Max

-  metric: org.apache.cassandra.metrics:Table.CoordinatorScanLatency,
   field: Mean

-  metric: org.apache.cassandra.metrics:Table.CoordinatorScanLatency,
   field: MeanRate

-  metric: org.apache.cassandra.metrics:Table.CoordinatorScanLatency,
   field: Min

-  metric: org.apache.cassandra.metrics:Table.CoordinatorScanLatency,
   field: OneMinuteRate

-  metric: org.apache.cassandra.metrics:Table.CoordinatorScanLatency,
   field: StdDev

-  metric: org.apache.cassandra.metrics:Table.DroppedMutations, field:
   Count

-  metric: org.apache.cassandra.metrics:Table.EstimatedPartitionCount,
   field: Value

-  metric:
   org.apache.cassandra.metrics:Table.IndexSummaryOffHeapMemoryUsed,
   field: Value

-  metric: org.apache.cassandra.metrics:Table.KeyCacheHitRate, field:
   Value

-  metric: org.apache.cassandra.metrics:Table.LiveDiskSpaceUsed, field:
   Count

-  metric: org.apache.cassandra.metrics:Table.LiveScannedHistogram,
   field: 50thPercentile

-  metric: org.apache.cassandra.metrics:Table.LiveScannedHistogram,
   field: 75thPercentile

-  metric: org.apache.cassandra.metrics:Table.LiveScannedHistogram,
   field: 95thPercentile

-  metric: org.apache.cassandra.metrics:Table.LiveScannedHistogram,
   field: 98thPercentile

-  metric: org.apache.cassandra.metrics:Table.LiveScannedHistogram,
   field: 999thPercentile

-  metric: org.apache.cassandra.metrics:Table.LiveScannedHistogram,
   field: 99thPercentile

-  metric: org.apache.cassandra.metrics:Table.LiveScannedHistogram,
   field: Count

-  metric: org.apache.cassandra.metrics:Table.LiveScannedHistogram,
   field: Max

-  metric: org.apache.cassandra.metrics:Table.LiveScannedHistogram,
   field: Mean

-  metric: org.apache.cassandra.metrics:Table.LiveScannedHistogram,
   field: Min

-  metric: org.apache.cassandra.metrics:Table.LiveScannedHistogram,
   field: StdDev

-  metric: org.apache.cassandra.metrics:Table.LiveSSTableCount, field:
   Value

-  metric: org.apache.cassandra.metrics:Table.MaxPartitionSize, field:
   Value

-  metric: org.apache.cassandra.metrics:Table.MeanPartitionSize, field:
   Value

-  metric: org.apache.cassandra.metrics:Table.MemtableColumnsCount,
   field: Value

-  metric: org.apache.cassandra.metrics:Table.MemtableLiveDataSize,
   field: Value

-  metric: org.apache.cassandra.metrics:Table.MemtableOffHeapSize,
   field: Value

-  metric: org.apache.cassandra.metrics:Table.MemtableOnHeapSize, field:
   Value

-  metric: org.apache.cassandra.metrics:Table.MemtableSwitchCount,
   field: Count

-  metric: org.apache.cassandra.metrics:Table.MinPartitionSize, field:
   Value

-  metric: org.apache.cassandra.metrics:Table.PendingCompactions, field:
   Value

-  metric: org.apache.cassandra.metrics:Table.PendingFlushes, field:
   Count

-  metric: org.apache.cassandra.metrics:Table.PercentRepaired, field:
   Value

-  metric: org.apache.cassandra.metrics:Table.RangeLatency, field:
   50thPercentile

-  metric: org.apache.cassandra.metrics:Table.RangeLatency, field:
   75thPercentile

-  metric: org.apache.cassandra.metrics:Table.RangeLatency, field:
   95thPercentile

-  metric: org.apache.cassandra.metrics:Table.RangeLatency, field:
   98thPercentile

-  metric: org.apache.cassandra.metrics:Table.RangeLatency, field:
   999thPercentile

-  metric: org.apache.cassandra.metrics:Table.RangeLatency, field:
   99thPercentile

-  metric: org.apache.cassandra.metrics:Table.RangeLatency, field: Count

-  metric: org.apache.cassandra.metrics:Table.RangeLatency, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Table.RangeLatency, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Table.RangeLatency, field: Max

-  metric: org.apache.cassandra.metrics:Table.RangeLatency, field: Mean

-  metric: org.apache.cassandra.metrics:Table.RangeLatency, field:
   MeanRate

-  metric: org.apache.cassandra.metrics:Table.RangeLatency, field: Min

-  metric: org.apache.cassandra.metrics:Table.RangeLatency, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:Table.RangeLatency, field:
   StdDev

-  metric: org.apache.cassandra.metrics:Table.RangeTotalLatency, field:
   Count

-  metric: org.apache.cassandra.metrics:Table.ReadLatency, field:
   50thPercentile

-  metric: org.apache.cassandra.metrics:Table.ReadLatency, field:
   75thPercentile

-  metric: org.apache.cassandra.metrics:Table.ReadLatency, field:
   95thPercentile

-  metric: org.apache.cassandra.metrics:Table.ReadLatency, field:
   98thPercentile

-  metric: org.apache.cassandra.metrics:Table.ReadLatency, field:
   999thPercentile

-  metric: org.apache.cassandra.metrics:Table.ReadLatency, field:
   99thPercentile

-  metric: org.apache.cassandra.metrics:Table.ReadLatency, field: Count

-  metric: org.apache.cassandra.metrics:Table.ReadLatency, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Table.ReadLatency, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Table.ReadLatency, field: Max

-  metric: org.apache.cassandra.metrics:Table.ReadLatency, field: Mean

-  metric: org.apache.cassandra.metrics:Table.ReadLatency, field:
   MeanRate

-  metric: org.apache.cassandra.metrics:Table.ReadLatency, field: Min

-  metric: org.apache.cassandra.metrics:Table.ReadLatency, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:Table.ReadLatency, field: StdDev

-  metric: org.apache.cassandra.metrics:Table.ReadRepairRequests, field:
   Count

-  metric: org.apache.cassandra.metrics:Table.ReadRepairRequests, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Table.ReadRepairRequests, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Table.ReadRepairRequests, field:
   MeanRate

-  metric: org.apache.cassandra.metrics:Table.ReadRepairRequests, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:Table.ReadTotalLatency, field:
   Count

-  metric:
   org.apache.cassandra.metrics:Table.RecentBloomFilterFalsePositives,
   field: Value

-  metric:
   org.apache.cassandra.metrics:Table.RecentBloomFilterFalseRatio,
   field: Value

-  metric: org.apache.cassandra.metrics:Table.RowCacheHit, field: Count

-  metric: org.apache.cassandra.metrics:Table.RowCacheHitOutOfRange,
   field: Count

-  metric: org.apache.cassandra.metrics:Table.RowCacheMiss, field: Count

-  metric:
   org.apache.cassandra.metrics:Table.ShortReadProtectionRequests,
   field: Count

-  metric:
   org.apache.cassandra.metrics:Table.ShortReadProtectionRequests,
   field: FifteenMinuteRate

-  metric:
   org.apache.cassandra.metrics:Table.ShortReadProtectionRequests,
   field: FiveMinuteRate

-  metric:
   org.apache.cassandra.metrics:Table.ShortReadProtectionRequests,
   field: MeanRate

-  metric:
   org.apache.cassandra.metrics:Table.ShortReadProtectionRequests,
   field: OneMinuteRate

-  metric: org.apache.cassandra.metrics:Table.SnapshotsSize, field:
   Value

-  metric: org.apache.cassandra.metrics:Table.SpeculativeRetries, field:
   Count

-  metric: org.apache.cassandra.metrics:Table.SSTablesPerReadHistogram,
   field: 50thPercentile

-  metric: org.apache.cassandra.metrics:Table.SSTablesPerReadHistogram,
   field: 75thPercentile

-  metric: org.apache.cassandra.metrics:Table.SSTablesPerReadHistogram,
   field: 95thPercentile

-  metric: org.apache.cassandra.metrics:Table.SSTablesPerReadHistogram,
   field: 98thPercentile

-  metric: org.apache.cassandra.metrics:Table.SSTablesPerReadHistogram,
   field: 999thPercentile

-  metric: org.apache.cassandra.metrics:Table.SSTablesPerReadHistogram,
   field: 99thPercentile

-  metric: org.apache.cassandra.metrics:Table.SSTablesPerReadHistogram,
   field: Count

-  metric: org.apache.cassandra.metrics:Table.SSTablesPerReadHistogram,
   field: Max

-  metric: org.apache.cassandra.metrics:Table.SSTablesPerReadHistogram,
   field: Mean

-  metric: org.apache.cassandra.metrics:Table.SSTablesPerReadHistogram,
   field: Min

-  metric: org.apache.cassandra.metrics:Table.SSTablesPerReadHistogram,
   field: StdDev

-  metric: org.apache.cassandra.metrics:Table.TombstoneScannedHistogram,
   field: 50thPercentile

-  metric: org.apache.cassandra.metrics:Table.TombstoneScannedHistogram,
   field: 75thPercentile

-  metric: org.apache.cassandra.metrics:Table.TombstoneScannedHistogram,
   field: 95thPercentile

-  metric: org.apache.cassandra.metrics:Table.TombstoneScannedHistogram,
   field: 98thPercentile

-  metric: org.apache.cassandra.metrics:Table.TombstoneScannedHistogram,
   field: 999thPercentile

-  metric: org.apache.cassandra.metrics:Table.TombstoneScannedHistogram,
   field: 99thPercentile

-  metric: org.apache.cassandra.metrics:Table.TombstoneScannedHistogram,
   field: Count

-  metric: org.apache.cassandra.metrics:Table.TombstoneScannedHistogram,
   field: Max

-  metric: org.apache.cassandra.metrics:Table.TombstoneScannedHistogram,
   field: Mean

-  metric: org.apache.cassandra.metrics:Table.TombstoneScannedHistogram,
   field: Min

-  metric: org.apache.cassandra.metrics:Table.TombstoneScannedHistogram,
   field: StdDev

-  metric: org.apache.cassandra.metrics:Table.TotalDiskSpaceUsed, field:
   Count

-  metric: org.apache.cassandra.metrics:Table.ViewLockAcquireTime,
   field: 50thPercentile

-  metric: org.apache.cassandra.metrics:Table.ViewLockAcquireTime,
   field: 75thPercentile

-  metric: org.apache.cassandra.metrics:Table.ViewLockAcquireTime,
   field: 95thPercentile

-  metric: org.apache.cassandra.metrics:Table.ViewLockAcquireTime,
   field: 98thPercentile

-  metric: org.apache.cassandra.metrics:Table.ViewLockAcquireTime,
   field: 999thPercentile

-  metric: org.apache.cassandra.metrics:Table.ViewLockAcquireTime,
   field: 99thPercentile

-  metric: org.apache.cassandra.metrics:Table.ViewLockAcquireTime,
   field: Count

-  metric: org.apache.cassandra.metrics:Table.ViewLockAcquireTime,
   field: FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Table.ViewLockAcquireTime,
   field: FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Table.ViewLockAcquireTime,
   field: Max

-  metric: org.apache.cassandra.metrics:Table.ViewLockAcquireTime,
   field: MeanRate

-  metric: org.apache.cassandra.metrics:Table.ViewLockAcquireTime,
   field: Min

-  metric: org.apache.cassandra.metrics:Table.ViewLockAcquireTime,
   field: OneMinuteRate

-  metric: org.apache.cassandra.metrics:Table.ViewLockAcquireTime,
   field: StdDev

-  metric: org.apache.cassandra.metrics:Table.ViewReadTime, field:
   50thPercentile

-  metric: org.apache.cassandra.metrics:Table.ViewReadTime, field:
   75thPercentile

-  metric: org.apache.cassandra.metrics:Table.ViewReadTime, field:
   95thPercentile

-  metric: org.apache.cassandra.metrics:Table.ViewReadTime, field:
   98thPercentile

-  metric: org.apache.cassandra.metrics:Table.ViewReadTime, field:
   999thPercentile

-  metric: org.apache.cassandra.metrics:Table.ViewReadTime, field:
   99thPercentile

-  metric: org.apache.cassandra.metrics:Table.ViewReadTime, field: Count

-  metric: org.apache.cassandra.metrics:Table.ViewReadTime, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Table.ViewReadTime, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Table.ViewReadTime, field: Max

-  metric: org.apache.cassandra.metrics:Table.ViewReadTime, field:
   MeanRate

-  metric: org.apache.cassandra.metrics:Table.ViewReadTime, field: Min

-  metric: org.apache.cassandra.metrics:Table.ViewReadTime, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:Table.ViewReadTime, field:
   StdDev

-  metric:
   org.apache.cassandra.metrics:Table.WaitingOnFreeMemtableSpace, field:
   50thPercentile

-  metric:
   org.apache.cassandra.metrics:Table.WaitingOnFreeMemtableSpace, field:
   75thPercentile

-  metric:
   org.apache.cassandra.metrics:Table.WaitingOnFreeMemtableSpace, field:
   95thPercentile

-  metric:
   org.apache.cassandra.metrics:Table.WaitingOnFreeMemtableSpace, field:
   98thPercentile

-  metric:
   org.apache.cassandra.metrics:Table.WaitingOnFreeMemtableSpace, field:
   999thPercentile

-  metric:
   org.apache.cassandra.metrics:Table.WaitingOnFreeMemtableSpace, field:
   99thPercentile

-  metric:
   org.apache.cassandra.metrics:Table.WaitingOnFreeMemtableSpace, field:
   Count

-  metric:
   org.apache.cassandra.metrics:Table.WaitingOnFreeMemtableSpace, field:
   Max

-  metric:
   org.apache.cassandra.metrics:Table.WaitingOnFreeMemtableSpace, field:
   Min

-  metric:
   org.apache.cassandra.metrics:Table.WaitingOnFreeMemtableSpace, field:
   StdDev

-  metric: org.apache.cassandra.metrics:Table.WriteLatency, field:
   50thPercentile

-  metric: org.apache.cassandra.metrics:Table.WriteLatency, field:
   75thPercentile

-  metric: org.apache.cassandra.metrics:Table.WriteLatency, field:
   95thPercentile

-  metric: org.apache.cassandra.metrics:Table.WriteLatency, field:
   98thPercentile

-  metric: org.apache.cassandra.metrics:Table.WriteLatency, field:
   999thPercentile

-  metric: org.apache.cassandra.metrics:Table.WriteLatency, field:
   99thPercentile

-  metric: org.apache.cassandra.metrics:Table.WriteLatency, field: Count

-  metric: org.apache.cassandra.metrics:Table.WriteLatency, field:
   FifteenMinuteRate

-  metric: org.apache.cassandra.metrics:Table.WriteLatency, field:
   FiveMinuteRate

-  metric: org.apache.cassandra.metrics:Table.WriteLatency, field: Max

-  metric: org.apache.cassandra.metrics:Table.WriteLatency, field: Mean

-  metric: org.apache.cassandra.metrics:Table.WriteLatency, field:
   MeanRate

-  metric: org.apache.cassandra.metrics:Table.WriteLatency, field: Min

-  metric: org.apache.cassandra.metrics:Table.WriteLatency, field:
   OneMinuteRate

-  metric: org.apache.cassandra.metrics:Table.WriteLatency, field:
   StdDev

-  metric: org.apache.cassandra.metrics:Table.WriteTotalLatency, field:
   Count

-  metric: org.apache.cassandra.metrics:ThreadPools.CompletedTasks,
   field: Value

-  metric: org.apache.cassandra.metrics:ThreadPools.MaxPoolSize, field:
   Value

-  metric: org.apache.cassandra.metrics:ThreadPools.TotalBlockedTasks,
   field: Count

.. _h_80527c055a:

Additional metrics for Aiven for PostgreSQL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  metric: postgresql.pg_stat_activity, field:
   oldest_non_autovacuum_query_age

-  metric: postgresql.pg_stat_bgwriter, field: buffers_alloc

-  metric: postgresql.pg_stat_bgwriter, field: buffers_backend

-  metric: postgresql.pg_stat_bgwriter, field: buffers_backend_fsync

-  metric: postgresql.pg_stat_bgwriter, field: buffers_checkpoint

-  metric: postgresql.pg_stat_bgwriter, field: buffers_clean

-  metric: postgresql.pg_stat_bgwriter, field: checkpoints_req

-  metric: postgresql.pg_stat_bgwriter, field: checkpoints_timed

-  metric: postgresql.pg_stat_bgwriter, field: checkpoint_sync_time

-  metric: postgresql.pg_stat_bgwriter, field: checkpoint_write_time

-  metric: postgresql.pg_stat_bgwriter, field: maxwritten_clean

-  metric: postgresql.pg_stat_replication, field: flush_diff

.. _h_913f45513a:

Additional metrics for Aiven for Redis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  metric: redis, field: active_defrag_hits

-  metric: redis, field: active_defrag_key_hits

-  metric: redis, field: active_defrag_key_misses

-  metric: redis, field: active_defrag_misses

-  metric: redis, field: active_defrag_running

-  metric: redis, field: allocator_active

-  metric: redis, field: allocator_allocated

-  metric: redis, field: allocator_frag_bytes

-  metric: redis, field: allocator_frag_ratio

-  metric: redis, field: allocator_resident

-  metric: redis, field: allocator_rss_bytes

-  metric: redis, field: allocator_rss_ratio

-  metric: redis, field: aof_current_rewrite_time_sec

-  metric: redis, field: aof_enabled

-  metric: redis, field: aof_last_bgrewrite_status

-  metric: redis, field: aof_last_cow_size

-  metric: redis, field: aof_last_rewrite_time_sec

-  metric: redis, field: aof_last_write_status

-  metric: redis, field: aof_rewrite_in_progress

-  metric: redis, field: aof_rewrite_scheduled

-  metric: redis, field: blocked_clients

-  metric: redis, field: client_recent_max_input_buffer

-  metric: redis, field: client_recent_max_output_buffer

-  metric: redis, field: clients_in_timeout_table

-  metric: redis, field: cluster_connections

-  metric: redis, field: cluster_enabled

-  metric: redis_cmdstat, field: calls

-  metric: redis_cmdstat, field: usec

-  metric: redis_cmdstat, field: usec_per_call

-  metric: redis, field: connected_slaves

-  metric: redis, field: current_cow_size

-  metric: redis, field: current_fork_perc

-  metric: redis, field: current_save_keys_processed

-  metric: redis, field: current_save_keys_total

-  metric: redis, field: dump_payload_sanitizations

-  metric: redis, field: expire_cycle_cpu_milliseconds

-  metric: redis, field: expired_stale_perc

-  metric: redis, field: expired_time_cap_reached_count

-  metric: redis, field: instantaneous_input_kbps

-  metric: redis, field: instantaneous_ops_per_sec

-  metric: redis, field: instantaneous_output_kbps

-  metric: redis, field: io_threaded_reads_processed

-  metric: redis, field: io_threaded_writes_processed

-  metric: redis, field: latest_fork_usec

-  metric: redis, field: lazyfreed_objects

-  metric: redis, field: lazyfree_pending_objects

-  metric: redis, field: loading

-  metric: redis, field: lru_clock

-  metric: redis, field: master_failover_state

-  metric: redis, field: master_repl_offset

-  metric: redis, field: maxclients

-  metric: redis, field: maxmemory_policy

-  metric: redis, field: mem_aof_buffer

-  metric: redis, field: mem_clients_normal

-  metric: redis, field: mem_clients_slaves

-  metric: redis, field: mem_fragmentation_bytes

-  metric: redis, field: mem_not_counted_for_evict

-  metric: redis, field: mem_replication_backlog

-  metric: redis, field: migrate_cached_sockets

-  metric: redis, field: module_fork_in_progress

-  metric: redis, field: module_fork_last_cow_size

-  metric: redis, field: number_of_cached_scripts

-  metric: redis, field: rdb_bgsave_in_progress

-  metric: redis, field: rdb_changes_since_last_save

-  metric: redis, field: rdb_current_bgsave_time_sec

-  metric: redis, field: rdb_last_bgsave_status

-  metric: redis, field: rdb_last_bgsave_time_sec

-  metric: redis, field: rdb_last_cow_size

-  metric: redis, field: rdb_last_save_time

-  metric: redis, field: rdb_last_save_time_elapsed

-  metric: redis, field: redis_version

-  metric: redis, field: repl_backlog_active

-  metric: redis, field: repl_backlog_first_byte_offset

-  metric: redis, field: repl_backlog_histlen

-  metric: redis, field: repl_backlog_size

-  metric: redis, field: rss_overhead_bytes

-  metric: redis, field: rss_overhead_ratio

-  metric: redis, field: second_repl_offset

-  metric: redis, field: slave_expires_tracked_keys

-  metric: redis, field: sync_full

-  metric: redis, field: sync_partial_err

-  metric: redis, field: sync_partial_ok

-  metric: redis, field: total_connections_received

-  metric: redis, field: total_error_replies

-  metric: redis, field: total_forks

-  metric: redis, field: total_net_input_bytes

-  metric: redis, field: total_net_output_bytes

-  metric: redis, field: total_reads_processed

-  metric: redis, field: total_system_memory

-  metric: redis, field: total_writes_processed

-  metric: redis, field: tracking_clients

-  metric: redis, field: tracking_total_items

-  metric: redis, field: tracking_total_keys

-  metric: redis, field: tracking_total_prefixes

-  metric: redis, field: unexpected_error_replies

-  metric: redis, field: used_cpu_sys

-  metric: redis, field: used_cpu_sys_children

-  metric: redis, field: used_cpu_sys_main_thread

-  metric: redis, field: used_cpu_user

-  metric: redis, field: used_cpu_user_children

-  metric: redis, field: used_cpu_user_main_thread

-  metric: redis, field: used_memory_dataset_perc

-  metric: redis, field: used_memory_overhead

-  metric: redis, field: used_memory_peak

-  metric: redis, field: used_memory_peak_perc

-  metric: redis, field: used_memory_rss

-  metric: redis, field: used_memory_scripts

-  metric: redis, field: used_memory_startup