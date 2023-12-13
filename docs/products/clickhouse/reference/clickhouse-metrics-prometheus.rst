Aiven for ClickHouse® metrics available via Prometheus
======================================================

This article provides the list of all metrics available via Prometheus for Aiven for ClickHouse® services.

You can retrieve the complete list of available metrics for your service by requesting the Prometheus endpoint as follows:

.. code-block:: bash

    curl --cacert ca.pem \
        --user '<PROMETHEUS_USER>:<PROMETHEUS_PASSWORD>' \
        'https://<CLICKHOUSE_HOSTNAME>:<PROMETHEUS_PORT>/metrics'

Where you substitute the following:

* Aiven project certificate for ``ca.pem``
* Prometheus credentials for ``<PROMETHEUS_USER>:<PROMETHEUS_PASSWORD>``
* Aiven for ClickHouse hostname for ``<CLICKHOUSE_HOSTNAME>``
* Prometheus port for ``<PROMETHEUS_PORT>``

.. Tip::

    You can check how to use Prometheus with Aiven in :doc:`Prometheus metrics </docs/platform/howto/integrations/prometheus-metrics>`.

.. code-block:: shell

   # TYPE clickhouse_asynchronous_metrics_number_of_databases untyped
   clickhouse_asynchronous_metrics_number_of_databases
   # TYPE clickhouse_asynchronous_metrics_number_of_tables untyped
   clickhouse_asynchronous_metrics_number_of_tables
   # TYPE clickhouse_asynchronous_metrics_total_parts_of_merge_tree_tables untyped
   clickhouse_asynchronous_metrics_total_parts_of_merge_tree_tables
   # TYPE clickhouse_asynchronous_metrics_total_rows_of_merge_tree_tables untyped
   clickhouse_asynchronous_metrics_total_rows_of_merge_tree_tables
   # TYPE clickhouse_events_inserted_bytes untyped
   clickhouse_events_inserted_bytes
   # TYPE clickhouse_events_inserted_rows untyped
   clickhouse_events_inserted_rows
   # TYPE clickhouse_events_merge untyped
   clickhouse_events_merge
   # TYPE clickhouse_events_merged_rows untyped
   clickhouse_events_merged_rows
   # TYPE clickhouse_events_merged_uncompressed_bytes untyped
   clickhouse_events_merged_uncompressed_bytes
   # TYPE clickhouse_events_query untyped
   clickhouse_events_query
   # TYPE clickhouse_events_read_compressed_bytes untyped
   clickhouse_events_read_compressed_bytes
   # TYPE clickhouse_events_select_query untyped
   clickhouse_events_select_query
   # TYPE clickhouse_metrics_delayed_inserts untyped
   clickhouse_metrics_delayed_inserts
   # TYPE clickhouse_metrics_ephemeral_node untyped
   clickhouse_metrics_ephemeral_node
   # TYPE clickhouse_metrics_http_connection untyped
   clickhouse_metrics_http_connection
   # TYPE clickhouse_metrics_interserver_connection untyped
   clickhouse_metrics_interserver_connection
   # TYPE clickhouse_metrics_merge untyped
   clickhouse_metrics_merge
   # TYPE clickhouse_metrics_query untyped
   clickhouse_metrics_query
   # TYPE clickhouse_metrics_query_preempted untyped
   clickhouse_metrics_query_preempted
   # TYPE clickhouse_metrics_readonly_replica untyped
   clickhouse_metrics_readonly_replica
   # TYPE clickhouse_metrics_replicated_checks untyped
   clickhouse_metrics_replicated_checks
   # TYPE clickhouse_metrics_replicated_fetch untyped
   clickhouse_metrics_replicated_fetch
   # TYPE clickhouse_metrics_rw_lock_active_readers untyped
   clickhouse_metrics_rw_lock_active_readers
   # TYPE clickhouse_metrics_rw_lock_active_writers untyped
   clickhouse_metrics_rw_lock_active_writers
   # TYPE clickhouse_metrics_rw_lock_waiting_readers untyped
   clickhouse_metrics_rw_lock_waiting_readers
   # TYPE clickhouse_metrics_rw_lock_waiting_writers untyped
   clickhouse_metrics_rw_lock_waiting_writers
   # TYPE clickhouse_metrics_tcp_connection untyped
   clickhouse_metrics_tcp_connection
   # TYPE clickhouse_metrics_zoo_keeper_request untyped
   clickhouse_metrics_zoo_keeper_request
   # TYPE clickhouse_metrics_zoo_keeper_session untyped
   clickhouse_metrics_zoo_keeper_session
   # TYPE clickhouse_metrics_zoo_keeper_watch untyped
   clickhouse_metrics_zoo_keeper_watch
   # TYPE clickhouse_replication_queue_num_attach_part untyped
   clickhouse_replication_queue_num_attach_part
   # TYPE clickhouse_replication_queue_num_get_part untyped
   clickhouse_replication_queue_num_get_part
   # TYPE clickhouse_replication_queue_num_merge_parts untyped
   clickhouse_replication_queue_num_merge_parts
   # TYPE clickhouse_replication_queue_num_merge_parts_ttl_delete untyped
   clickhouse_replication_queue_num_merge_parts_ttl_delete
   # TYPE clickhouse_replication_queue_num_merge_parts_ttl_recompress untyped
   clickhouse_replication_queue_num_merge_parts_ttl_recompress
   # TYPE clickhouse_replication_queue_num_mutate_part untyped
   clickhouse_replication_queue_num_mutate_part
   # TYPE clickhouse_replication_queue_num_total untyped
   clickhouse_replication_queue_num_total
   # TYPE clickhouse_replication_queue_num_tries_replicas untyped
   clickhouse_replication_queue_num_tries_replicas
   # TYPE clickhouse_replication_queue_too_many_tries_replicas untyped
   clickhouse_replication_queue_too_many_tries_replicas
   # TYPE cpu_usage_guest gauge
   cpu_usage_guest
   # TYPE cpu_usage_guest_nice gauge
   cpu_usage_guest_nice
   # TYPE cpu_usage_idle gauge
   cpu_usage_idle
   # TYPE cpu_usage_iowait gauge
   cpu_usage_iowait
   # TYPE cpu_usage_irq gauge
   cpu_usage_irq
   # TYPE cpu_usage_nice gauge
   cpu_usage_nice
   # TYPE cpu_usage_softirq gauge
   cpu_usage_softirq
   # TYPE cpu_usage_steal gauge
   cpu_usage_steal
   # TYPE cpu_usage_system gauge
   cpu_usage_system
   # TYPE cpu_usage_user gauge
   cpu_usage_user
   # TYPE disk_free gauge
   disk_free
   # TYPE disk_inodes_free gauge
   disk_inodes_free
   # TYPE disk_inodes_total gauge
   disk_inodes_total
   # TYPE disk_inodes_used gauge
   disk_inodes_used
   # TYPE disk_total gauge
   disk_total
   # TYPE disk_used gauge
   disk_used
   # TYPE disk_used_percent gauge
   disk_used_percent
   # TYPE diskio_io_time counter
   diskio_io_time
   # TYPE diskio_iops_in_progress counter
   diskio_iops_in_progress
   # TYPE diskio_merged_reads counter
   diskio_merged_reads
   # TYPE diskio_merged_writes counter
   diskio_merged_writes
   # TYPE diskio_read_bytes counter
   diskio_read_bytes
   # TYPE diskio_read_time counter
   diskio_read_time
   # TYPE diskio_reads counter
   diskio_reads
   # TYPE diskio_weighted_io_time counter
   diskio_weighted_io_time
   # TYPE diskio_write_bytes counter
   diskio_write_bytes
   # TYPE diskio_write_time counter
   diskio_write_time
   # TYPE diskio_writes counter
   diskio_writes
   # TYPE kernel_boot_time counter
   kernel_boot_time
   # TYPE kernel_context_switches counter
   kernel_context_switches
   # TYPE kernel_entropy_avail counter
   kernel_entropy_avail
   # TYPE kernel_interrupts counter
   kernel_interrupts
   # TYPE kernel_processes_forked counter
   kernel_processes_forked
   # TYPE mem_active gauge
   mem_active
   # TYPE mem_available gauge
   mem_available
   # TYPE mem_available_percent gauge
   mem_available_percent
   # TYPE mem_buffered gauge
   mem_buffered
   # TYPE mem_cached gauge
   mem_cached
   # TYPE mem_commit_limit gauge
   mem_commit_limit
   # TYPE mem_committed_as gauge
   mem_committed_as
   # TYPE mem_dirty gauge
   mem_dirty
   # TYPE mem_free gauge
   mem_free
   # TYPE mem_high_free gauge
   mem_high_free
   # TYPE mem_high_total gauge
   mem_high_total
   # TYPE mem_huge_page_size gauge
   mem_huge_page_size
   # TYPE mem_huge_pages_free gauge
   mem_huge_pages_free
   # TYPE mem_huge_pages_total gauge
   mem_huge_pages_total
   # TYPE mem_inactive gauge
   mem_inactive
   # TYPE mem_low_free gauge
   mem_low_free
   # TYPE mem_low_total gauge
   mem_low_total
   # TYPE mem_mapped gauge
   mem_mapped
   # TYPE mem_page_tables gauge
   mem_page_tables
   # TYPE mem_shared gauge
   mem_shared
   # TYPE mem_slab gauge
   mem_slab
   # TYPE mem_sreclaimable gauge
   mem_sreclaimable
   # TYPE mem_sunreclaim gauge
   mem_sunreclaim
   # TYPE mem_swap_cached gauge
   mem_swap_cached
   # TYPE mem_swap_free gauge
   mem_swap_free
   # TYPE mem_swap_total gauge
   mem_swap_total
   # TYPE mem_total gauge
   mem_total
   # TYPE mem_used gauge
   mem_used
   # TYPE mem_used_percent gauge
   mem_used_percent
   # TYPE mem_vmalloc_chunk gauge
   mem_vmalloc_chunk
   # TYPE mem_vmalloc_total gauge
   mem_vmalloc_total
   # TYPE mem_vmalloc_used gauge
   mem_vmalloc_used
   # TYPE mem_write_back gauge
   mem_write_back
   # TYPE mem_write_back_tmp gauge
   mem_write_back_tmp
   # TYPE net_bytes_recv counter
   net_bytes_recv
   # TYPE net_bytes_sent counter
   net_bytes_sent
   # TYPE net_drop_in counter
   net_drop_in
   # TYPE net_drop_out counter
   net_drop_out
   # TYPE net_err_in counter
   net_err_in
   # TYPE net_err_out counter
   net_err_out
   # TYPE net_icmp_inaddrmaskreps untyped
   net_icmp_inaddrmaskreps
   # TYPE net_icmp_inaddrmasks untyped
   net_icmp_inaddrmasks
   # TYPE net_icmp_incsumerrors untyped
   net_icmp_incsumerrors
   # TYPE net_icmp_indestunreachs untyped
   net_icmp_indestunreachs
   # TYPE net_icmp_inechoreps untyped
   net_icmp_inechoreps
   # TYPE net_icmp_inechos untyped
   net_icmp_inechos
   # TYPE net_icmp_inerrors untyped
   net_icmp_inerrors
   # TYPE net_icmp_inmsgs untyped
   net_icmp_inmsgs
   # TYPE net_icmp_inparmprobs untyped
   net_icmp_inparmprobs
   # TYPE net_icmp_inredirects untyped
   net_icmp_inredirects
   # TYPE net_icmp_insrcquenchs untyped
   net_icmp_insrcquenchs
   # TYPE net_icmp_intimeexcds untyped
   net_icmp_intimeexcds
   # TYPE net_icmp_intimestampreps untyped
   net_icmp_intimestampreps
   # TYPE net_icmp_intimestamps untyped
   net_icmp_intimestamps
   # TYPE net_icmp_outaddrmaskreps untyped
   net_icmp_outaddrmaskreps
   # TYPE net_icmp_outaddrmasks untyped
   net_icmp_outaddrmasks
   # TYPE net_icmp_outdestunreachs untyped
   net_icmp_outdestunreachs
   # TYPE net_icmp_outechoreps untyped
   net_icmp_outechoreps
   # TYPE net_icmp_outechos untyped
   net_icmp_outechos
   # TYPE net_icmp_outerrors untyped
   net_icmp_outerrors
   # TYPE net_icmp_outmsgs untyped
   net_icmp_outmsgs
   # TYPE net_icmp_outparmprobs untyped
   net_icmp_outparmprobs
   # TYPE net_icmp_outratelimitglobal untyped
   net_icmp_outratelimitglobal
   # TYPE net_icmp_outratelimithost untyped
   net_icmp_outratelimithost
   # TYPE net_icmp_outredirects untyped
   net_icmp_outredirects
   # TYPE net_icmp_outsrcquenchs untyped
   net_icmp_outsrcquenchs
   # TYPE net_icmp_outtimeexcds untyped
   net_icmp_outtimeexcds
   # TYPE net_icmp_outtimestampreps untyped
   net_icmp_outtimestampreps
   # TYPE net_icmp_outtimestamps untyped
   net_icmp_outtimestamps
   # TYPE net_icmpmsg_intype3 untyped
   net_icmpmsg_intype3
   # TYPE net_icmpmsg_intype8 untyped
   net_icmpmsg_intype8
   # TYPE net_icmpmsg_outtype0 untyped
   net_icmpmsg_outtype0
   # TYPE net_icmpmsg_outtype3 untyped
   net_icmpmsg_outtype3
   # TYPE net_ip_defaultttl untyped
   net_ip_defaultttl
   # TYPE net_ip_forwarding untyped
   net_ip_forwarding
   # TYPE net_ip_forwdatagrams untyped
   net_ip_forwdatagrams
   # TYPE net_ip_fragcreates untyped
   net_ip_fragcreates
   # TYPE net_ip_fragfails untyped
   net_ip_fragfails
   # TYPE net_ip_fragoks untyped
   net_ip_fragoks
   # TYPE net_ip_inaddrerrors untyped
   net_ip_inaddrerrors
   # TYPE net_ip_indelivers untyped
   net_ip_indelivers
   # TYPE net_ip_indiscards untyped
   net_ip_indiscards
   # TYPE net_ip_inhdrerrors untyped
   net_ip_inhdrerrors
   # TYPE net_ip_inreceives untyped
   net_ip_inreceives
   # TYPE net_ip_inunknownprotos untyped
   net_ip_inunknownprotos
   # TYPE net_ip_outdiscards untyped
   net_ip_outdiscards
   # TYPE net_ip_outnoroutes untyped
   net_ip_outnoroutes
   # TYPE net_ip_outrequests untyped
   net_ip_outrequests
   # TYPE net_ip_reasmfails untyped
   net_ip_reasmfails
   # TYPE net_ip_reasmoks untyped
   net_ip_reasmoks
   # TYPE net_ip_reasmreqds untyped
   net_ip_reasmreqds
   # TYPE net_ip_reasmtimeout untyped
   net_ip_reasmtimeout
   # TYPE net_packets_recv counter
   net_packets_recv
   # TYPE net_packets_sent counter
   net_packets_sent
   # TYPE net_tcp_activeopens untyped
   net_tcp_activeopens
   # TYPE net_tcp_attemptfails untyped
   net_tcp_attemptfails
   # TYPE net_tcp_currestab untyped
   net_tcp_currestab
   # TYPE net_tcp_estabresets untyped
   net_tcp_estabresets
   # TYPE net_tcp_incsumerrors untyped
   net_tcp_incsumerrors
   # TYPE net_tcp_inerrs untyped
   net_tcp_inerrs
   # TYPE net_tcp_insegs untyped
   net_tcp_insegs
   # TYPE net_tcp_maxconn untyped
   net_tcp_maxconn
   # TYPE net_tcp_outrsts untyped
   net_tcp_outrsts
   # TYPE net_tcp_outsegs untyped
   net_tcp_outsegs
   # TYPE net_tcp_passiveopens untyped
   net_tcp_passiveopens
   # TYPE net_tcp_retranssegs untyped
   net_tcp_retranssegs
   # TYPE net_tcp_rtoalgorithm untyped
   net_tcp_rtoalgorithm
   # TYPE net_tcp_rtomax untyped
   net_tcp_rtomax
   # TYPE net_tcp_rtomin untyped
   net_tcp_rtomin
   # TYPE net_udp_ignoredmulti untyped
   net_udp_ignoredmulti
   # TYPE net_udp_incsumerrors untyped
   net_udp_incsumerrors
   # TYPE net_udp_indatagrams untyped
   net_udp_indatagrams
   # TYPE net_udp_inerrors untyped
   net_udp_inerrors
   # TYPE net_udp_memerrors untyped
   net_udp_memerrors
   # TYPE net_udp_noports untyped
   net_udp_noports
   # TYPE net_udp_outdatagrams untyped
   net_udp_outdatagrams
   # TYPE net_udp_rcvbuferrors untyped
   net_udp_rcvbuferrors
   # TYPE net_udp_sndbuferrors untyped
   net_udp_sndbuferrors
   # TYPE net_udplite_ignoredmulti untyped
   net_udplite_ignoredmulti
   # TYPE net_udplite_incsumerrors untyped
   net_udplite_incsumerrors
   # TYPE net_udplite_indatagrams untyped
   net_udplite_indatagrams
   # TYPE net_udplite_inerrors untyped
   net_udplite_inerrors
   # TYPE net_udplite_memerrors untyped
   net_udplite_memerrors
   # TYPE net_udplite_noports untyped
   net_udplite_noports
   # TYPE net_udplite_outdatagrams untyped
   net_udplite_outdatagrams
   # TYPE net_udplite_rcvbuferrors untyped
   net_udplite_rcvbuferrors
   # TYPE net_udplite_sndbuferrors untyped
   net_udplite_sndbuferrors
   # TYPE netstat_tcp_close untyped
   netstat_tcp_close
   # TYPE netstat_tcp_close_wait untyped
   netstat_tcp_close_wait
   # TYPE netstat_tcp_closing untyped
   netstat_tcp_closing
   # TYPE netstat_tcp_established untyped
   netstat_tcp_established
   # TYPE netstat_tcp_fin_wait1 untyped
   netstat_tcp_fin_wait1
   # TYPE netstat_tcp_fin_wait2 untyped
   netstat_tcp_fin_wait2
   # TYPE netstat_tcp_last_ack untyped
   netstat_tcp_last_ack
   # TYPE netstat_tcp_listen untyped
   netstat_tcp_listen
   # TYPE netstat_tcp_none untyped
   netstat_tcp_none
   # TYPE netstat_tcp_syn_recv untyped
   netstat_tcp_syn_recv
   # TYPE netstat_tcp_syn_sent untyped
   netstat_tcp_syn_sent
   # TYPE netstat_tcp_time_wait untyped
   netstat_tcp_time_wait
   # TYPE netstat_udp_socket untyped
   netstat_udp_socket
   # TYPE processes_blocked gauge
   processes_blocked
   # TYPE processes_dead gauge
   processes_dead
   # TYPE processes_idle gauge
   processes_idle
   # TYPE processes_paging gauge
   processes_paging
   # TYPE processes_running gauge
   processes_running
   # TYPE processes_sleeping gauge
   processes_sleeping
   # TYPE processes_stopped gauge
   processes_stopped
   # TYPE processes_total gauge
   processes_total
   # TYPE processes_total_threads gauge
   processes_total_threads
   # TYPE processes_unknown gauge
   processes_unknown
   # TYPE processes_zombies gauge
   processes_zombies
   # TYPE service_connections_accepted untyped
   service_connections_accepted
   # TYPE service_connections_dropped untyped
   service_connections_dropped
   # TYPE service_connections_limit_avg_per_second untyped
   service_connections_limit_avg_per_second
   # TYPE service_connections_limit_burst untyped
   service_connections_limit_burst
   # TYPE swap_free gauge
   swap_free
   # TYPE swap_in counter
   swap_in
   # TYPE swap_out counter
   swap_out
   # TYPE swap_total gauge
   swap_total
   # TYPE swap_used gauge
   swap_used
   # TYPE swap_used_percent gauge
   swap_used_percent
   # TYPE system_load1 gauge
   system_load1
   # TYPE system_load15 gauge
   system_load15
   # TYPE system_load5 gauge
   system_load5
   # TYPE system_n_cpus gauge
   system_n_cpus
   # TYPE system_n_unique_users gauge
   system_n_unique_users
   # TYPE system_n_users gauge
   system_n_users
   # TYPE system_uptime counter
   system_uptime
   # TYPE zookeeper_add_dead_watcher_stall_time untyped
   zookeeper_add_dead_watcher_stall_time
   # TYPE zookeeper_approximate_data_size untyped
   zookeeper_approximate_data_size
   # TYPE zookeeper_auth_failed_count untyped
   zookeeper_auth_failed_count
   # TYPE zookeeper_bytes_received_count untyped
   zookeeper_bytes_received_count
   # TYPE zookeeper_cnt_1_ack_latency untyped
   zookeeper_cnt_1_ack_latency
   # TYPE zookeeper_cnt_action_create_service_user_done_write_per_namespace untyped
   zookeeper_cnt_action_create_service_user_done_write_per_namespace
   # TYPE zookeeper_cnt_action_grant_federated_queries_access_done_write_per_namespace untyped
   zookeeper_cnt_action_grant_federated_queries_access_done_write_per_namespace
   # TYPE zookeeper_cnt_action_grant_federated_queries_access_v2_done_write_per_namespace untyped
   zookeeper_cnt_action_grant_federated_queries_access_v2_done_write_per_namespace
   # TYPE zookeeper_cnt_action_restore_from_astacus_done_write_per_namespace untyped
   zookeeper_cnt_action_restore_from_astacus_done_write_per_namespace
   # TYPE zookeeper_cnt_action_update_service_users_privileges_done_write_per_namespace untyped
   zookeeper_cnt_action_update_service_users_privileges_done_write_per_namespace
   # TYPE zookeeper_cnt_action_update_service_users_privileges_v2_done_write_per_namespace untyped
   zookeeper_cnt_action_update_service_users_privileges_v2_done_write_per_namespace
   # TYPE zookeeper_cnt_clickhouse_read_per_namespace untyped
   zookeeper_cnt_clickhouse_read_per_namespace
   # TYPE zookeeper_cnt_clickhouse_write_per_namespace untyped
   zookeeper_cnt_clickhouse_write_per_namespace
   # TYPE zookeeper_cnt_close_session_prep_time untyped
   zookeeper_cnt_close_session_prep_time
   # TYPE zookeeper_cnt_commit_commit_proc_req_queued untyped
   zookeeper_cnt_commit_commit_proc_req_queued
   # TYPE zookeeper_cnt_commit_process_time untyped
   zookeeper_cnt_commit_process_time
   # TYPE zookeeper_cnt_commit_propagation_latency untyped
   zookeeper_cnt_commit_propagation_latency
   # TYPE zookeeper_cnt_concurrent_request_processing_in_commit_processor untyped
   zookeeper_cnt_concurrent_request_processing_in_commit_processor
   # TYPE zookeeper_cnt_connection_token_deficit untyped
   zookeeper_cnt_connection_token_deficit
   # TYPE zookeeper_cnt_dbinittime untyped
   zookeeper_cnt_dbinittime
   # TYPE zookeeper_cnt_dead_watchers_cleaner_latency untyped
   zookeeper_cnt_dead_watchers_cleaner_latency
   # TYPE zookeeper_cnt_election_leader_read_per_namespace untyped
   zookeeper_cnt_election_leader_read_per_namespace
   # TYPE zookeeper_cnt_election_leader_write_per_namespace untyped
   zookeeper_cnt_election_leader_write_per_namespace
   # TYPE zookeeper_cnt_election_time untyped
   zookeeper_cnt_election_time
   # TYPE zookeeper_cnt_follower_sync_time untyped
   zookeeper_cnt_follower_sync_time
   # TYPE zookeeper_cnt_fsynctime untyped
   zookeeper_cnt_fsynctime
   # TYPE zookeeper_cnt_health_write_per_namespace untyped
   zookeeper_cnt_health_write_per_namespace
   # TYPE zookeeper_cnt_inflight_diff_count untyped
   zookeeper_cnt_inflight_diff_count
   # TYPE zookeeper_cnt_inflight_snap_count untyped
   zookeeper_cnt_inflight_snap_count
   # TYPE zookeeper_cnt_jvm_pause_time_ms untyped
   zookeeper_cnt_jvm_pause_time_ms
   # TYPE zookeeper_cnt_local_write_committed_time_ms untyped
   zookeeper_cnt_local_write_committed_time_ms
   # TYPE zookeeper_cnt_netty_queued_buffer_capacity untyped
   zookeeper_cnt_netty_queued_buffer_capacity
   # TYPE zookeeper_cnt_node_changed_watch_count untyped
   zookeeper_cnt_node_changed_watch_count
   # TYPE zookeeper_cnt_node_children_watch_count untyped
   zookeeper_cnt_node_children_watch_count
   # TYPE zookeeper_cnt_node_created_watch_count untyped
   zookeeper_cnt_node_created_watch_count
   # TYPE zookeeper_cnt_node_deleted_watch_count untyped
   zookeeper_cnt_node_deleted_watch_count
   # TYPE zookeeper_cnt_node_slots_read_per_namespace untyped
   zookeeper_cnt_node_slots_read_per_namespace
   # TYPE zookeeper_cnt_node_slots_write_per_namespace untyped
   zookeeper_cnt_node_slots_write_per_namespace
   # TYPE zookeeper_cnt_nodes_read_per_namespace untyped
   zookeeper_cnt_nodes_read_per_namespace
   # TYPE zookeeper_cnt_nodes_write_per_namespace untyped
   zookeeper_cnt_nodes_write_per_namespace
   # TYPE zookeeper_cnt_om_commit_process_time_ms untyped
   zookeeper_cnt_om_commit_process_time_ms
   # TYPE zookeeper_cnt_om_proposal_process_time_ms untyped
   zookeeper_cnt_om_proposal_process_time_ms
   # TYPE zookeeper_cnt_pending_session_queue_size untyped
   zookeeper_cnt_pending_session_queue_size
   # TYPE zookeeper_cnt_prep_process_time untyped
   zookeeper_cnt_prep_process_time
   # TYPE zookeeper_cnt_prep_processor_queue_size untyped
   zookeeper_cnt_prep_processor_queue_size
   # TYPE zookeeper_cnt_prep_processor_queue_time_ms untyped
   zookeeper_cnt_prep_processor_queue_time_ms
   # TYPE zookeeper_cnt_propagation_latency untyped
   zookeeper_cnt_propagation_latency
   # TYPE zookeeper_cnt_proposal_ack_creation_latency untyped
   zookeeper_cnt_proposal_ack_creation_latency
   # TYPE zookeeper_cnt_proposal_latency untyped
   zookeeper_cnt_proposal_latency
   # TYPE zookeeper_cnt_quorum_ack_latency untyped
   zookeeper_cnt_quorum_ack_latency
   # TYPE zookeeper_cnt_read_commit_proc_issued untyped
   zookeeper_cnt_read_commit_proc_issued
   # TYPE zookeeper_cnt_read_commit_proc_req_queued untyped
   zookeeper_cnt_read_commit_proc_req_queued
   # TYPE zookeeper_cnt_read_commitproc_time_ms untyped
   zookeeper_cnt_read_commitproc_time_ms
   # TYPE zookeeper_cnt_read_final_proc_time_ms untyped
   zookeeper_cnt_read_final_proc_time_ms
   # TYPE zookeeper_cnt_readlatency untyped
   zookeeper_cnt_readlatency
   # TYPE zookeeper_cnt_reads_after_write_in_session_queue untyped
   zookeeper_cnt_reads_after_write_in_session_queue
   # TYPE zookeeper_cnt_reads_issued_from_session_queue untyped
   zookeeper_cnt_reads_issued_from_session_queue
   # TYPE zookeeper_cnt_requests_in_session_queue untyped
   zookeeper_cnt_requests_in_session_queue
   # TYPE zookeeper_cnt_server_write_committed_time_ms untyped
   zookeeper_cnt_server_write_committed_time_ms
   # TYPE zookeeper_cnt_session_queues_drained untyped
   zookeeper_cnt_session_queues_drained
   # TYPE zookeeper_cnt_snapshottime untyped
   zookeeper_cnt_snapshottime
   # TYPE zookeeper_cnt_startup_snap_load_time untyped
   zookeeper_cnt_startup_snap_load_time
   # TYPE zookeeper_cnt_startup_txns_load_time untyped
   zookeeper_cnt_startup_txns_load_time
   # TYPE zookeeper_cnt_startup_txns_loaded untyped
   zookeeper_cnt_startup_txns_loaded
   # TYPE zookeeper_cnt_sync_process_time untyped
   zookeeper_cnt_sync_process_time
   # TYPE zookeeper_cnt_sync_processor_batch_size untyped
   zookeeper_cnt_sync_processor_batch_size
   # TYPE zookeeper_cnt_sync_processor_queue_and_flush_time_ms untyped
   zookeeper_cnt_sync_processor_queue_and_flush_time_ms
   # TYPE zookeeper_cnt_sync_processor_queue_flush_time_ms untyped
   zookeeper_cnt_sync_processor_queue_flush_time_ms
   # TYPE zookeeper_cnt_sync_processor_queue_size untyped
   zookeeper_cnt_sync_processor_queue_size
   # TYPE zookeeper_cnt_sync_processor_queue_time_ms untyped
   zookeeper_cnt_sync_processor_queue_time_ms
   # TYPE zookeeper_cnt_time_waiting_empty_pool_in_commit_processor_read_ms untyped
   zookeeper_cnt_time_waiting_empty_pool_in_commit_processor_read_ms
   # TYPE zookeeper_cnt_updatelatency untyped
   zookeeper_cnt_updatelatency
   # TYPE zookeeper_cnt_write_batch_time_in_commit_processor untyped
   zookeeper_cnt_write_batch_time_in_commit_processor
   # TYPE zookeeper_cnt_write_commit_proc_issued untyped
   zookeeper_cnt_write_commit_proc_issued
   # TYPE zookeeper_cnt_write_commit_proc_req_queued untyped
   zookeeper_cnt_write_commit_proc_req_queued
   # TYPE zookeeper_cnt_write_commitproc_time_ms untyped
   zookeeper_cnt_write_commitproc_time_ms
   # TYPE zookeeper_cnt_write_final_proc_time_ms untyped
   zookeeper_cnt_write_final_proc_time_ms
   # TYPE zookeeper_cnt_zk_cluster_management_write_per_namespace untyped
   zookeeper_cnt_zk_cluster_management_write_per_namespace
   # TYPE zookeeper_cnt_zookeeper_read_per_namespace untyped
   zookeeper_cnt_zookeeper_read_per_namespace
   # TYPE zookeeper_cnt_zookeeper_write_per_namespace untyped
   zookeeper_cnt_zookeeper_write_per_namespace
   # TYPE zookeeper_commit_count untyped
   zookeeper_commit_count
   # TYPE zookeeper_connection_drop_count untyped
   zookeeper_connection_drop_count
   # TYPE zookeeper_connection_rejected untyped
   zookeeper_connection_rejected
   # TYPE zookeeper_connection_request_count untyped
   zookeeper_connection_request_count
   # TYPE zookeeper_connection_revalidate_count untyped
   zookeeper_connection_revalidate_count
   # TYPE zookeeper_dead_watchers_cleared untyped
   zookeeper_dead_watchers_cleared
   # TYPE zookeeper_dead_watchers_queued untyped
   zookeeper_dead_watchers_queued
   # TYPE zookeeper_diff_count untyped
   zookeeper_diff_count
   # TYPE zookeeper_digest_mismatches_count untyped
   zookeeper_digest_mismatches_count
   # TYPE zookeeper_ensemble_auth_fail untyped
   zookeeper_ensemble_auth_fail
   # TYPE zookeeper_ensemble_auth_skip untyped
   zookeeper_ensemble_auth_skip
   # TYPE zookeeper_ensemble_auth_success untyped
   zookeeper_ensemble_auth_success
   # TYPE zookeeper_ephemerals_count untyped
   zookeeper_ephemerals_count
   # TYPE zookeeper_global_sessions untyped
   zookeeper_global_sessions
   # TYPE zookeeper_large_requests_rejected untyped
   zookeeper_large_requests_rejected
   # TYPE zookeeper_last_client_response_size untyped
   zookeeper_last_client_response_size
   # TYPE zookeeper_last_proposal_size untyped
   zookeeper_last_proposal_size
   # TYPE zookeeper_leader_uptime untyped
   zookeeper_leader_uptime
   # TYPE zookeeper_learner_commit_received_count untyped
   zookeeper_learner_commit_received_count
   # TYPE zookeeper_learner_proposal_received_count untyped
   zookeeper_learner_proposal_received_count
   # TYPE zookeeper_learners untyped
   zookeeper_learners
   # TYPE zookeeper_local_sessions untyped
   zookeeper_local_sessions
   # TYPE zookeeper_looking_count untyped
   zookeeper_looking_count
   # TYPE zookeeper_max_1_ack_latency untyped
   zookeeper_max_1_ack_latency
   # TYPE zookeeper_max_action_create_service_user_done_write_per_namespace untyped
   zookeeper_max_action_create_service_user_done_write_per_namespace
   # TYPE zookeeper_max_action_grant_federated_queries_access_done_write_per_namespace untyped
   zookeeper_max_action_grant_federated_queries_access_done_write_per_namespace
   # TYPE zookeeper_max_action_grant_federated_queries_access_v2_done_write_per_namespace untyped
   zookeeper_max_action_grant_federated_queries_access_v2_done_write_per_namespace
   # TYPE zookeeper_max_action_restore_from_astacus_done_write_per_namespace untyped
   zookeeper_max_action_restore_from_astacus_done_write_per_namespace
   # TYPE zookeeper_max_action_update_service_users_privileges_done_write_per_namespace untyped
   zookeeper_max_action_update_service_users_privileges_done_write_per_namespace
   # TYPE zookeeper_max_action_update_service_users_privileges_v2_done_write_per_namespace untyped
   zookeeper_max_action_update_service_users_privileges_v2_done_write_per_namespace
   # TYPE zookeeper_max_clickhouse_read_per_namespace untyped
   zookeeper_max_clickhouse_read_per_namespace
   # TYPE zookeeper_max_clickhouse_write_per_namespace untyped
   zookeeper_max_clickhouse_write_per_namespace
   # TYPE zookeeper_max_client_response_size untyped
   zookeeper_max_client_response_size
   # TYPE zookeeper_max_close_session_prep_time untyped
   zookeeper_max_close_session_prep_time
   # TYPE zookeeper_max_commit_commit_proc_req_queued untyped
   zookeeper_max_commit_commit_proc_req_queued
   # TYPE zookeeper_max_commit_process_time untyped
   zookeeper_max_commit_process_time
   # TYPE zookeeper_max_commit_propagation_latency untyped
   zookeeper_max_commit_propagation_latency
   # TYPE zookeeper_max_concurrent_request_processing_in_commit_processor untyped
   zookeeper_max_concurrent_request_processing_in_commit_processor
   # TYPE zookeeper_max_connection_token_deficit untyped
   zookeeper_max_connection_token_deficit
   # TYPE zookeeper_max_dbinittime untyped
   zookeeper_max_dbinittime
   # TYPE zookeeper_max_dead_watchers_cleaner_latency untyped
   zookeeper_max_dead_watchers_cleaner_latency
   # TYPE zookeeper_max_election_leader_read_per_namespace untyped
   zookeeper_max_election_leader_read_per_namespace
   # TYPE zookeeper_max_election_leader_write_per_namespace untyped
   zookeeper_max_election_leader_write_per_namespace
   # TYPE zookeeper_max_election_time untyped
   zookeeper_max_election_time
   # TYPE zookeeper_max_file_descriptor_count untyped
   zookeeper_max_file_descriptor_count
   # TYPE zookeeper_max_follower_sync_time untyped
   zookeeper_max_follower_sync_time
   # TYPE zookeeper_max_fsynctime untyped
   zookeeper_max_fsynctime
   # TYPE zookeeper_max_health_write_per_namespace untyped
   zookeeper_max_health_write_per_namespace
   # TYPE zookeeper_max_inflight_diff_count untyped
   zookeeper_max_inflight_diff_count
   # TYPE zookeeper_max_inflight_snap_count untyped
   zookeeper_max_inflight_snap_count
   # TYPE zookeeper_max_jvm_pause_time_ms untyped
   zookeeper_max_jvm_pause_time_ms
   # TYPE zookeeper_max_latency untyped
   zookeeper_max_latency
   # TYPE zookeeper_max_local_write_committed_time_ms untyped
   zookeeper_max_local_write_committed_time_ms
   # TYPE zookeeper_max_netty_queued_buffer_capacity untyped
   zookeeper_max_netty_queued_buffer_capacity
   # TYPE zookeeper_max_node_changed_watch_count untyped
   zookeeper_max_node_changed_watch_count
   # TYPE zookeeper_max_node_children_watch_count untyped
   zookeeper_max_node_children_watch_count
   # TYPE zookeeper_max_node_created_watch_count untyped
   zookeeper_max_node_created_watch_count
   # TYPE zookeeper_max_node_deleted_watch_count untyped
   zookeeper_max_node_deleted_watch_count
   # TYPE zookeeper_max_node_slots_read_per_namespace untyped
   zookeeper_max_node_slots_read_per_namespace
   # TYPE zookeeper_max_node_slots_write_per_namespace untyped
   zookeeper_max_node_slots_write_per_namespace
   # TYPE zookeeper_max_nodes_read_per_namespace untyped
   zookeeper_max_nodes_read_per_namespace
   # TYPE zookeeper_max_nodes_write_per_namespace untyped
   zookeeper_max_nodes_write_per_namespace
   # TYPE zookeeper_max_om_commit_process_time_ms untyped
   zookeeper_max_om_commit_process_time_ms
   # TYPE zookeeper_max_om_proposal_process_time_ms untyped
   zookeeper_max_om_proposal_process_time_ms
   # TYPE zookeeper_max_pending_session_queue_size untyped
   zookeeper_max_pending_session_queue_size
   # TYPE zookeeper_max_prep_process_time untyped
   zookeeper_max_prep_process_time
   # TYPE zookeeper_max_prep_processor_queue_size untyped
   zookeeper_max_prep_processor_queue_size
   # TYPE zookeeper_max_prep_processor_queue_time_ms untyped
   zookeeper_max_prep_processor_queue_time_ms
   # TYPE zookeeper_max_propagation_latency untyped
   zookeeper_max_propagation_latency
   # TYPE zookeeper_max_proposal_ack_creation_latency untyped
   zookeeper_max_proposal_ack_creation_latency
   # TYPE zookeeper_max_proposal_latency untyped
   zookeeper_max_proposal_latency
   # TYPE zookeeper_max_proposal_size untyped
   zookeeper_max_proposal_size
   # TYPE zookeeper_max_quorum_ack_latency untyped
   zookeeper_max_quorum_ack_latency
   # TYPE zookeeper_max_read_commit_proc_issued untyped
   zookeeper_max_read_commit_proc_issued
   # TYPE zookeeper_max_read_commit_proc_req_queued untyped
   zookeeper_max_read_commit_proc_req_queued
   # TYPE zookeeper_max_read_commitproc_time_ms untyped
   zookeeper_max_read_commitproc_time_ms
   # TYPE zookeeper_max_read_final_proc_time_ms untyped
   zookeeper_max_read_final_proc_time_ms
   # TYPE zookeeper_max_readlatency untyped
   zookeeper_max_readlatency
   # TYPE zookeeper_max_reads_after_write_in_session_queue untyped
   zookeeper_max_reads_after_write_in_session_queue
   # TYPE zookeeper_max_reads_issued_from_session_queue untyped
   zookeeper_max_reads_issued_from_session_queue
   # TYPE zookeeper_max_requests_in_session_queue untyped
   zookeeper_max_requests_in_session_queue
   # TYPE zookeeper_max_server_write_committed_time_ms untyped
   zookeeper_max_server_write_committed_time_ms
   # TYPE zookeeper_max_session_queues_drained untyped
   zookeeper_max_session_queues_drained
   # TYPE zookeeper_max_snapshottime untyped
   zookeeper_max_snapshottime
   # TYPE zookeeper_max_startup_snap_load_time untyped
   zookeeper_max_startup_snap_load_time
   # TYPE zookeeper_max_startup_txns_load_time untyped
   zookeeper_max_startup_txns_load_time
   # TYPE zookeeper_max_startup_txns_loaded untyped
   zookeeper_max_startup_txns_loaded
   # TYPE zookeeper_max_sync_process_time untyped
   zookeeper_max_sync_process_time
   # TYPE zookeeper_max_sync_processor_batch_size untyped
   zookeeper_max_sync_processor_batch_size
   # TYPE zookeeper_max_sync_processor_queue_and_flush_time_ms untyped
   zookeeper_max_sync_processor_queue_and_flush_time_ms
   # TYPE zookeeper_max_sync_processor_queue_flush_time_ms untyped
   zookeeper_max_sync_processor_queue_flush_time_ms
   # TYPE zookeeper_max_sync_processor_queue_size untyped
   zookeeper_max_sync_processor_queue_size
   # TYPE zookeeper_max_sync_processor_queue_time_ms untyped
   zookeeper_max_sync_processor_queue_time_ms
   # TYPE zookeeper_max_time_waiting_empty_pool_in_commit_processor_read_ms untyped
   zookeeper_max_time_waiting_empty_pool_in_commit_processor_read_ms
   # TYPE zookeeper_max_updatelatency untyped
   zookeeper_max_updatelatency
   # TYPE zookeeper_max_write_batch_time_in_commit_processor untyped
   zookeeper_max_write_batch_time_in_commit_processor
   # TYPE zookeeper_max_write_commit_proc_issued untyped
   zookeeper_max_write_commit_proc_issued
   # TYPE zookeeper_max_write_commit_proc_req_queued untyped
   zookeeper_max_write_commit_proc_req_queued
   # TYPE zookeeper_max_write_commitproc_time_ms untyped
   zookeeper_max_write_commitproc_time_ms
   # TYPE zookeeper_max_write_final_proc_time_ms untyped
   zookeeper_max_write_final_proc_time_ms
   # TYPE zookeeper_max_zk_cluster_management_write_per_namespace untyped
   zookeeper_max_zk_cluster_management_write_per_namespace
   # TYPE zookeeper_max_zookeeper_read_per_namespace untyped
   zookeeper_max_zookeeper_read_per_namespace
   # TYPE zookeeper_max_zookeeper_write_per_namespace untyped
   zookeeper_max_zookeeper_write_per_namespace
   # TYPE zookeeper_min_1_ack_latency untyped
   zookeeper_min_1_ack_latency
   # TYPE zookeeper_min_action_create_service_user_done_write_per_namespace untyped
   zookeeper_min_action_create_service_user_done_write_per_namespace
   # TYPE zookeeper_min_action_grant_federated_queries_access_done_write_per_namespace untyped
   zookeeper_min_action_grant_federated_queries_access_done_write_per_namespace
   # TYPE zookeeper_min_action_grant_federated_queries_access_v2_done_write_per_namespace untyped
   zookeeper_min_action_grant_federated_queries_access_v2_done_write_per_namespace
   # TYPE zookeeper_min_action_restore_from_astacus_done_write_per_namespace untyped
   zookeeper_min_action_restore_from_astacus_done_write_per_namespace
   # TYPE zookeeper_min_action_update_service_users_privileges_done_write_per_namespace untyped
   zookeeper_min_action_update_service_users_privileges_done_write_per_namespace
   # TYPE zookeeper_min_action_update_service_users_privileges_v2_done_write_per_namespace untyped
   zookeeper_min_action_update_service_users_privileges_v2_done_write_per_namespace
   # TYPE zookeeper_min_clickhouse_read_per_namespace untyped
   zookeeper_min_clickhouse_read_per_namespace
   # TYPE zookeeper_min_clickhouse_write_per_namespace untyped
   zookeeper_min_clickhouse_write_per_namespace
   # TYPE zookeeper_min_client_response_size untyped
   zookeeper_min_client_response_size
   # TYPE zookeeper_min_close_session_prep_time untyped
   zookeeper_min_close_session_prep_time
   # TYPE zookeeper_min_commit_commit_proc_req_queued untyped
   zookeeper_min_commit_commit_proc_req_queued
   # TYPE zookeeper_min_commit_process_time untyped
   zookeeper_min_commit_process_time
   # TYPE zookeeper_min_commit_propagation_latency untyped
   zookeeper_min_commit_propagation_latency
   # TYPE zookeeper_min_concurrent_request_processing_in_commit_processor untyped
   zookeeper_min_concurrent_request_processing_in_commit_processor
   # TYPE zookeeper_min_connection_token_deficit untyped
   zookeeper_min_connection_token_deficit
   # TYPE zookeeper_min_dbinittime untyped
   zookeeper_min_dbinittime
   # TYPE zookeeper_min_dead_watchers_cleaner_latency untyped
   zookeeper_min_dead_watchers_cleaner_latency
   # TYPE zookeeper_min_election_leader_read_per_namespace untyped
   zookeeper_min_election_leader_read_per_namespace
   # TYPE zookeeper_min_election_leader_write_per_namespace untyped
   zookeeper_min_election_leader_write_per_namespace
   # TYPE zookeeper_min_election_time untyped
   zookeeper_min_election_time
   # TYPE zookeeper_min_follower_sync_time untyped
   zookeeper_min_follower_sync_time
   # TYPE zookeeper_min_fsynctime untyped
   zookeeper_min_fsynctime
   # TYPE zookeeper_min_health_write_per_namespace untyped
   zookeeper_min_health_write_per_namespace
   # TYPE zookeeper_min_inflight_diff_count untyped
   zookeeper_min_inflight_diff_count
   # TYPE zookeeper_min_inflight_snap_count untyped
   zookeeper_min_inflight_snap_count
   # TYPE zookeeper_min_jvm_pause_time_ms untyped
   zookeeper_min_jvm_pause_time_ms
   # TYPE zookeeper_min_latency untyped
   zookeeper_min_latency
   # TYPE zookeeper_min_local_write_committed_time_ms untyped
   zookeeper_min_local_write_committed_time_ms
   # TYPE zookeeper_min_netty_queued_buffer_capacity untyped
   zookeeper_min_netty_queued_buffer_capacity
   # TYPE zookeeper_min_node_changed_watch_count untyped
   zookeeper_min_node_changed_watch_count
   # TYPE zookeeper_min_node_children_watch_count untyped
   zookeeper_min_node_children_watch_count
   # TYPE zookeeper_min_node_created_watch_count untyped
   zookeeper_min_node_created_watch_count
   # TYPE zookeeper_min_node_deleted_watch_count untyped
   zookeeper_min_node_deleted_watch_count
   # TYPE zookeeper_min_node_slots_read_per_namespace untyped
   zookeeper_min_node_slots_read_per_namespace
   # TYPE zookeeper_min_node_slots_write_per_namespace untyped
   zookeeper_min_node_slots_write_per_namespace
   # TYPE zookeeper_min_nodes_read_per_namespace untyped
   zookeeper_min_nodes_read_per_namespace
   # TYPE zookeeper_min_nodes_write_per_namespace untyped
   zookeeper_min_nodes_write_per_namespace
   # TYPE zookeeper_min_om_commit_process_time_ms untyped
   zookeeper_min_om_commit_process_time_ms
   # TYPE zookeeper_min_om_proposal_process_time_ms untyped
   zookeeper_min_om_proposal_process_time_ms
   # TYPE zookeeper_min_pending_session_queue_size untyped
   zookeeper_min_pending_session_queue_size
   # TYPE zookeeper_min_prep_process_time untyped
   zookeeper_min_prep_process_time
   # TYPE zookeeper_min_prep_processor_queue_size untyped
   zookeeper_min_prep_processor_queue_size
   # TYPE zookeeper_min_prep_processor_queue_time_ms untyped
   zookeeper_min_prep_processor_queue_time_ms
   # TYPE zookeeper_min_propagation_latency untyped
   zookeeper_min_propagation_latency
   # TYPE zookeeper_min_proposal_ack_creation_latency untyped
   zookeeper_min_proposal_ack_creation_latency
   # TYPE zookeeper_min_proposal_latency untyped
   zookeeper_min_proposal_latency
   # TYPE zookeeper_min_proposal_size untyped
   zookeeper_min_proposal_size
   # TYPE zookeeper_min_quorum_ack_latency untyped
   zookeeper_min_quorum_ack_latency
   # TYPE zookeeper_min_read_commit_proc_issued untyped
   zookeeper_min_read_commit_proc_issued
   # TYPE zookeeper_min_read_commit_proc_req_queued untyped
   zookeeper_min_read_commit_proc_req_queued
   # TYPE zookeeper_min_read_commitproc_time_ms untyped
   zookeeper_min_read_commitproc_time_ms
   # TYPE zookeeper_min_read_final_proc_time_ms untyped
   zookeeper_min_read_final_proc_time_ms
   # TYPE zookeeper_min_readlatency untyped
   zookeeper_min_readlatency
   # TYPE zookeeper_min_reads_after_write_in_session_queue untyped
   zookeeper_min_reads_after_write_in_session_queue
   # TYPE zookeeper_min_reads_issued_from_session_queue untyped
   zookeeper_min_reads_issued_from_session_queue
   # TYPE zookeeper_min_requests_in_session_queue untyped
   zookeeper_min_requests_in_session_queue
   # TYPE zookeeper_min_server_write_committed_time_ms untyped
   zookeeper_min_server_write_committed_time_ms
   # TYPE zookeeper_min_session_queues_drained untyped
   zookeeper_min_session_queues_drained
   # TYPE zookeeper_min_snapshottime untyped
   zookeeper_min_snapshottime
   # TYPE zookeeper_min_startup_snap_load_time untyped
   zookeeper_min_startup_snap_load_time
   # TYPE zookeeper_min_startup_txns_load_time untyped
   zookeeper_min_startup_txns_load_time
   # TYPE zookeeper_min_startup_txns_loaded untyped
   zookeeper_min_startup_txns_loaded
   # TYPE zookeeper_min_sync_process_time untyped
   zookeeper_min_sync_process_time
   # TYPE zookeeper_min_sync_processor_batch_size untyped
   zookeeper_min_sync_processor_batch_size
   # TYPE zookeeper_min_sync_processor_queue_and_flush_time_ms untyped
   zookeeper_min_sync_processor_queue_and_flush_time_ms
   # TYPE zookeeper_min_sync_processor_queue_flush_time_ms untyped
   zookeeper_min_sync_processor_queue_flush_time_ms
   # TYPE zookeeper_min_sync_processor_queue_size untyped
   zookeeper_min_sync_processor_queue_size
   # TYPE zookeeper_min_sync_processor_queue_time_ms untyped
   zookeeper_min_sync_processor_queue_time_ms
   # TYPE zookeeper_min_time_waiting_empty_pool_in_commit_processor_read_ms untyped
   zookeeper_min_time_waiting_empty_pool_in_commit_processor_read_ms
   # TYPE zookeeper_min_updatelatency untyped
   zookeeper_min_updatelatency
   # TYPE zookeeper_min_write_batch_time_in_commit_processor untyped
   zookeeper_min_write_batch_time_in_commit_processor
   # TYPE zookeeper_min_write_commit_proc_issued untyped
   zookeeper_min_write_commit_proc_issued
   # TYPE zookeeper_min_write_commit_proc_req_queued untyped
   zookeeper_min_write_commit_proc_req_queued
   # TYPE zookeeper_min_write_commitproc_time_ms untyped
   zookeeper_min_write_commitproc_time_ms
   # TYPE zookeeper_min_write_final_proc_time_ms untyped
   zookeeper_min_write_final_proc_time_ms
   # TYPE zookeeper_min_zk_cluster_management_write_per_namespace untyped
   zookeeper_min_zk_cluster_management_write_per_namespace
   # TYPE zookeeper_min_zookeeper_read_per_namespace untyped
   zookeeper_min_zookeeper_read_per_namespace
   # TYPE zookeeper_min_zookeeper_write_per_namespace untyped
   zookeeper_min_zookeeper_write_per_namespace
   # TYPE zookeeper_non_mtls_local_conn_count untyped
   zookeeper_non_mtls_local_conn_count
   # TYPE zookeeper_non_mtls_remote_conn_count untyped
   zookeeper_non_mtls_remote_conn_count
   # TYPE zookeeper_num_alive_connections untyped
   zookeeper_num_alive_connections
   # TYPE zookeeper_open_file_descriptor_count untyped
   zookeeper_open_file_descriptor_count
   # TYPE zookeeper_outstanding_changes_queued untyped
   zookeeper_outstanding_changes_queued
   # TYPE zookeeper_outstanding_changes_removed untyped
   zookeeper_outstanding_changes_removed
   # TYPE zookeeper_outstanding_requests untyped
   zookeeper_outstanding_requests
   # TYPE zookeeper_outstanding_tls_handshake untyped
   zookeeper_outstanding_tls_handshake
   # TYPE zookeeper_p50_1_ack_latency untyped
   zookeeper_p50_1_ack_latency
   # TYPE zookeeper_p50_close_session_prep_time untyped
   zookeeper_p50_close_session_prep_time
   # TYPE zookeeper_p50_commit_propagation_latency untyped
   zookeeper_p50_commit_propagation_latency
   # TYPE zookeeper_p50_dead_watchers_cleaner_latency untyped
   zookeeper_p50_dead_watchers_cleaner_latency
   # TYPE zookeeper_p50_jvm_pause_time_ms untyped
   zookeeper_p50_jvm_pause_time_ms
   # TYPE zookeeper_p50_local_write_committed_time_ms untyped
   zookeeper_p50_local_write_committed_time_ms
   # TYPE zookeeper_p50_om_commit_process_time_ms untyped
   zookeeper_p50_om_commit_process_time_ms
   # TYPE zookeeper_p50_om_proposal_process_time_ms untyped
   zookeeper_p50_om_proposal_process_time_ms
   # TYPE zookeeper_p50_prep_processor_queue_time_ms untyped
   zookeeper_p50_prep_processor_queue_time_ms
   # TYPE zookeeper_p50_propagation_latency untyped
   zookeeper_p50_propagation_latency
   # TYPE zookeeper_p50_proposal_ack_creation_latency untyped
   zookeeper_p50_proposal_ack_creation_latency
   # TYPE zookeeper_p50_proposal_latency untyped
   zookeeper_p50_proposal_latency
   # TYPE zookeeper_p50_quorum_ack_latency untyped
   zookeeper_p50_quorum_ack_latency
   # TYPE zookeeper_p50_read_commitproc_time_ms untyped
   zookeeper_p50_read_commitproc_time_ms
   # TYPE zookeeper_p50_read_final_proc_time_ms untyped
   zookeeper_p50_read_final_proc_time_ms
   # TYPE zookeeper_p50_readlatency untyped
   zookeeper_p50_readlatency
   # TYPE zookeeper_p50_server_write_committed_time_ms untyped
   zookeeper_p50_server_write_committed_time_ms
   # TYPE zookeeper_p50_sync_processor_queue_and_flush_time_ms untyped
   zookeeper_p50_sync_processor_queue_and_flush_time_ms
   # TYPE zookeeper_p50_sync_processor_queue_flush_time_ms untyped
   zookeeper_p50_sync_processor_queue_flush_time_ms
   # TYPE zookeeper_p50_sync_processor_queue_time_ms untyped
   zookeeper_p50_sync_processor_queue_time_ms
   # TYPE zookeeper_p50_updatelatency untyped
   zookeeper_p50_updatelatency
   # TYPE zookeeper_p50_write_commitproc_time_ms untyped
   zookeeper_p50_write_commitproc_time_ms
   # TYPE zookeeper_p50_write_final_proc_time_ms untyped
   zookeeper_p50_write_final_proc_time_ms
   # TYPE zookeeper_p95_1_ack_latency untyped
   zookeeper_p95_1_ack_latency
   # TYPE zookeeper_p95_close_session_prep_time untyped
   zookeeper_p95_close_session_prep_time
   # TYPE zookeeper_p95_commit_propagation_latency untyped
   zookeeper_p95_commit_propagation_latency
   # TYPE zookeeper_p95_dead_watchers_cleaner_latency untyped
   zookeeper_p95_dead_watchers_cleaner_latency
   # TYPE zookeeper_p95_jvm_pause_time_ms untyped
   zookeeper_p95_jvm_pause_time_ms
   # TYPE zookeeper_p95_local_write_committed_time_ms untyped
   zookeeper_p95_local_write_committed_time_ms
   # TYPE zookeeper_p95_om_commit_process_time_ms untyped
   zookeeper_p95_om_commit_process_time_ms
   # TYPE zookeeper_p95_om_proposal_process_time_ms untyped
   zookeeper_p95_om_proposal_process_time_ms
   # TYPE zookeeper_p95_prep_processor_queue_time_ms untyped
   zookeeper_p95_prep_processor_queue_time_ms
   # TYPE zookeeper_p95_propagation_latency untyped
   zookeeper_p95_propagation_latency
   # TYPE zookeeper_p95_proposal_ack_creation_latency untyped
   zookeeper_p95_proposal_ack_creation_latency
   # TYPE zookeeper_p95_proposal_latency untyped
   zookeeper_p95_proposal_latency
   # TYPE zookeeper_p95_quorum_ack_latency untyped
   zookeeper_p95_quorum_ack_latency
   # TYPE zookeeper_p95_read_commitproc_time_ms untyped
   zookeeper_p95_read_commitproc_time_ms
   # TYPE zookeeper_p95_read_final_proc_time_ms untyped
   zookeeper_p95_read_final_proc_time_ms
   # TYPE zookeeper_p95_readlatency untyped
   zookeeper_p95_readlatency
   # TYPE zookeeper_p95_server_write_committed_time_ms untyped
   zookeeper_p95_server_write_committed_time_ms
   # TYPE zookeeper_p95_sync_processor_queue_and_flush_time_ms untyped
   zookeeper_p95_sync_processor_queue_and_flush_time_ms
   # TYPE zookeeper_p95_sync_processor_queue_flush_time_ms untyped
   zookeeper_p95_sync_processor_queue_flush_time_ms
   # TYPE zookeeper_p95_sync_processor_queue_time_ms untyped
   zookeeper_p95_sync_processor_queue_time_ms
   # TYPE zookeeper_p95_updatelatency untyped
   zookeeper_p95_updatelatency
   # TYPE zookeeper_p95_write_commitproc_time_ms untyped
   zookeeper_p95_write_commitproc_time_ms
   # TYPE zookeeper_p95_write_final_proc_time_ms untyped
   zookeeper_p95_write_final_proc_time_ms
   # TYPE zookeeper_p999_1_ack_latency untyped
   zookeeper_p999_1_ack_latency
   # TYPE zookeeper_p999_close_session_prep_time untyped
   zookeeper_p999_close_session_prep_time
   # TYPE zookeeper_p999_commit_propagation_latency untyped
   zookeeper_p999_commit_propagation_latency
   # TYPE zookeeper_p999_dead_watchers_cleaner_latency untyped
   zookeeper_p999_dead_watchers_cleaner_latency
   # TYPE zookeeper_p999_jvm_pause_time_ms untyped
   zookeeper_p999_jvm_pause_time_ms
   # TYPE zookeeper_p999_local_write_committed_time_ms untyped
   zookeeper_p999_local_write_committed_time_ms
   # TYPE zookeeper_p999_om_commit_process_time_ms untyped
   zookeeper_p999_om_commit_process_time_ms
   # TYPE zookeeper_p999_om_proposal_process_time_ms untyped
   zookeeper_p999_om_proposal_process_time_ms
   # TYPE zookeeper_p999_prep_processor_queue_time_ms untyped
   zookeeper_p999_prep_processor_queue_time_ms
   # TYPE zookeeper_p999_propagation_latency untyped
   zookeeper_p999_propagation_latency
   # TYPE zookeeper_p999_proposal_ack_creation_latency untyped
   zookeeper_p999_proposal_ack_creation_latency
   # TYPE zookeeper_p999_proposal_latency untyped
   zookeeper_p999_proposal_latency
   # TYPE zookeeper_p999_quorum_ack_latency untyped
   zookeeper_p999_quorum_ack_latency
   # TYPE zookeeper_p999_read_commitproc_time_ms untyped
   zookeeper_p999_read_commitproc_time_ms
   # TYPE zookeeper_p999_read_final_proc_time_ms untyped
   zookeeper_p999_read_final_proc_time_ms
   # TYPE zookeeper_p999_readlatency untyped
   zookeeper_p999_readlatency
   # TYPE zookeeper_p999_server_write_committed_time_ms untyped
   zookeeper_p999_server_write_committed_time_ms
   # TYPE zookeeper_p999_sync_processor_queue_and_flush_time_ms untyped
   zookeeper_p999_sync_processor_queue_and_flush_time_ms
   # TYPE zookeeper_p999_sync_processor_queue_flush_time_ms untyped
   zookeeper_p999_sync_processor_queue_flush_time_ms
   # TYPE zookeeper_p999_sync_processor_queue_time_ms untyped
   zookeeper_p999_sync_processor_queue_time_ms
   # TYPE zookeeper_p999_updatelatency untyped
   zookeeper_p999_updatelatency
   # TYPE zookeeper_p999_write_commitproc_time_ms untyped
   zookeeper_p999_write_commitproc_time_ms
   # TYPE zookeeper_p999_write_final_proc_time_ms untyped
   zookeeper_p999_write_final_proc_time_ms
   # TYPE zookeeper_p99_1_ack_latency untyped
   zookeeper_p99_1_ack_latency
   # TYPE zookeeper_p99_close_session_prep_time untyped
   zookeeper_p99_close_session_prep_time
   # TYPE zookeeper_p99_commit_propagation_latency untyped
   zookeeper_p99_commit_propagation_latency
   # TYPE zookeeper_p99_dead_watchers_cleaner_latency untyped
   zookeeper_p99_dead_watchers_cleaner_latency
   # TYPE zookeeper_p99_jvm_pause_time_ms untyped
   zookeeper_p99_jvm_pause_time_ms
   # TYPE zookeeper_p99_local_write_committed_time_ms untyped
   zookeeper_p99_local_write_committed_time_ms
   # TYPE zookeeper_p99_om_commit_process_time_ms untyped
   zookeeper_p99_om_commit_process_time_ms
   # TYPE zookeeper_p99_om_proposal_process_time_ms untyped
   zookeeper_p99_om_proposal_process_time_ms
   # TYPE zookeeper_p99_prep_processor_queue_time_ms untyped
   zookeeper_p99_prep_processor_queue_time_ms
   # TYPE zookeeper_p99_propagation_latency untyped
   zookeeper_p99_propagation_latency
   # TYPE zookeeper_p99_proposal_ack_creation_latency untyped
   zookeeper_p99_proposal_ack_creation_latency
   # TYPE zookeeper_p99_proposal_latency untyped
   zookeeper_p99_proposal_latency
   # TYPE zookeeper_p99_quorum_ack_latency untyped
   zookeeper_p99_quorum_ack_latency
   # TYPE zookeeper_p99_read_commitproc_time_ms untyped
   zookeeper_p99_read_commitproc_time_ms
   # TYPE zookeeper_p99_read_final_proc_time_ms untyped
   zookeeper_p99_read_final_proc_time_ms
   # TYPE zookeeper_p99_readlatency untyped
   zookeeper_p99_readlatency
   # TYPE zookeeper_p99_server_write_committed_time_ms untyped
   zookeeper_p99_server_write_committed_time_ms
   # TYPE zookeeper_p99_sync_processor_queue_and_flush_time_ms untyped
   zookeeper_p99_sync_processor_queue_and_flush_time_ms
   # TYPE zookeeper_p99_sync_processor_queue_flush_time_ms untyped
   zookeeper_p99_sync_processor_queue_flush_time_ms
   # TYPE zookeeper_p99_sync_processor_queue_time_ms untyped
   zookeeper_p99_sync_processor_queue_time_ms
   # TYPE zookeeper_p99_updatelatency untyped
   zookeeper_p99_updatelatency
   # TYPE zookeeper_p99_write_commitproc_time_ms untyped
   zookeeper_p99_write_commitproc_time_ms
   # TYPE zookeeper_p99_write_final_proc_time_ms untyped
   zookeeper_p99_write_final_proc_time_ms
   # TYPE zookeeper_packets_received untyped
   zookeeper_packets_received
   # TYPE zookeeper_packets_sent untyped
   zookeeper_packets_sent
   # TYPE zookeeper_pending_syncs untyped
   zookeeper_pending_syncs
   # TYPE zookeeper_prep_processor_request_queued untyped
   zookeeper_prep_processor_request_queued
   # TYPE zookeeper_proposal_count untyped
   zookeeper_proposal_count
   # TYPE zookeeper_quit_leading_due_to_disloyal_voter untyped
   zookeeper_quit_leading_due_to_disloyal_voter
   # TYPE zookeeper_quorum_size untyped
   zookeeper_quorum_size
   # TYPE zookeeper_request_commit_queued untyped
   zookeeper_request_commit_queued
   # TYPE zookeeper_request_throttle_wait_count untyped
   zookeeper_request_throttle_wait_count
   # TYPE zookeeper_response_packet_cache_hits untyped
   zookeeper_response_packet_cache_hits
   # TYPE zookeeper_response_packet_cache_misses untyped
   zookeeper_response_packet_cache_misses
   # TYPE zookeeper_response_packet_get_children_cache_hits untyped
   zookeeper_response_packet_get_children_cache_hits
   # TYPE zookeeper_response_packet_get_children_cache_misses untyped
   zookeeper_response_packet_get_children_cache_misses
   # TYPE zookeeper_revalidate_count untyped
   zookeeper_revalidate_count
   # TYPE zookeeper_sessionless_connections_expired untyped
   zookeeper_sessionless_connections_expired
   # TYPE zookeeper_snap_count untyped
   zookeeper_snap_count
   # TYPE zookeeper_stale_replies untyped
   zookeeper_stale_replies
   # TYPE zookeeper_stale_requests untyped
   zookeeper_stale_requests
   # TYPE zookeeper_stale_requests_dropped untyped
   zookeeper_stale_requests_dropped
   # TYPE zookeeper_stale_sessions_expired untyped
   zookeeper_stale_sessions_expired
   # TYPE zookeeper_sum_1_ack_latency untyped
   zookeeper_sum_1_ack_latency
   # TYPE zookeeper_sum_action_create_service_user_done_write_per_namespace untyped
   zookeeper_sum_action_create_service_user_done_write_per_namespace
   # TYPE zookeeper_sum_action_grant_federated_queries_access_done_write_per_namespace untyped
   zookeeper_sum_action_grant_federated_queries_access_done_write_per_namespace
   # TYPE zookeeper_sum_action_grant_federated_queries_access_v2_done_write_per_namespace untyped
   zookeeper_sum_action_grant_federated_queries_access_v2_done_write_per_namespace
   # TYPE zookeeper_sum_action_restore_from_astacus_done_write_per_namespace untyped
   zookeeper_sum_action_restore_from_astacus_done_write_per_namespace
   # TYPE zookeeper_sum_action_update_service_users_privileges_done_write_per_namespace untyped
   zookeeper_sum_action_update_service_users_privileges_done_write_per_namespace
   # TYPE zookeeper_sum_action_update_service_users_privileges_v2_done_write_per_namespace untyped
   zookeeper_sum_action_update_service_users_privileges_v2_done_write_per_namespace
   # TYPE zookeeper_sum_clickhouse_read_per_namespace untyped
   zookeeper_sum_clickhouse_read_per_namespace
   # TYPE zookeeper_sum_clickhouse_write_per_namespace untyped
   zookeeper_sum_clickhouse_write_per_namespace
   # TYPE zookeeper_sum_close_session_prep_time untyped
   zookeeper_sum_close_session_prep_time
   # TYPE zookeeper_sum_commit_commit_proc_req_queued untyped
   zookeeper_sum_commit_commit_proc_req_queued
   # TYPE zookeeper_sum_commit_process_time untyped
   zookeeper_sum_commit_process_time
   # TYPE zookeeper_sum_commit_propagation_latency untyped
   zookeeper_sum_commit_propagation_latency
   # TYPE zookeeper_sum_concurrent_request_processing_in_commit_processor untyped
   zookeeper_sum_concurrent_request_processing_in_commit_processor
   # TYPE zookeeper_sum_connection_token_deficit untyped
   zookeeper_sum_connection_token_deficit
   # TYPE zookeeper_sum_dbinittime untyped
   zookeeper_sum_dbinittime
   # TYPE zookeeper_sum_dead_watchers_cleaner_latency untyped
   zookeeper_sum_dead_watchers_cleaner_latency
   # TYPE zookeeper_sum_election_leader_read_per_namespace untyped
   zookeeper_sum_election_leader_read_per_namespace
   # TYPE zookeeper_sum_election_leader_write_per_namespace untyped
   zookeeper_sum_election_leader_write_per_namespace
   # TYPE zookeeper_sum_election_time untyped
   zookeeper_sum_election_time
   # TYPE zookeeper_sum_follower_sync_time untyped
   zookeeper_sum_follower_sync_time
   # TYPE zookeeper_sum_fsynctime untyped
   zookeeper_sum_fsynctime
   # TYPE zookeeper_sum_health_write_per_namespace untyped
   zookeeper_sum_health_write_per_namespace
   # TYPE zookeeper_sum_inflight_diff_count untyped
   zookeeper_sum_inflight_diff_count
   # TYPE zookeeper_sum_inflight_snap_count untyped
   zookeeper_sum_inflight_snap_count
   # TYPE zookeeper_sum_jvm_pause_time_ms untyped
   zookeeper_sum_jvm_pause_time_ms
   # TYPE zookeeper_sum_local_write_committed_time_ms untyped
   zookeeper_sum_local_write_committed_time_ms
   # TYPE zookeeper_sum_netty_queued_buffer_capacity untyped
   zookeeper_sum_netty_queued_buffer_capacity
   # TYPE zookeeper_sum_node_changed_watch_count untyped
   zookeeper_sum_node_changed_watch_count
   # TYPE zookeeper_sum_node_children_watch_count untyped
   zookeeper_sum_node_children_watch_count
   # TYPE zookeeper_sum_node_created_watch_count untyped
   zookeeper_sum_node_created_watch_count
   # TYPE zookeeper_sum_node_deleted_watch_count untyped
   zookeeper_sum_node_deleted_watch_count
   # TYPE zookeeper_sum_node_slots_read_per_namespace untyped
   zookeeper_sum_node_slots_read_per_namespace
   # TYPE zookeeper_sum_node_slots_write_per_namespace untyped
   zookeeper_sum_node_slots_write_per_namespace
   # TYPE zookeeper_sum_nodes_read_per_namespace untyped
   zookeeper_sum_nodes_read_per_namespace
   # TYPE zookeeper_sum_nodes_write_per_namespace untyped
   zookeeper_sum_nodes_write_per_namespace
   # TYPE zookeeper_sum_om_commit_process_time_ms untyped
   zookeeper_sum_om_commit_process_time_ms
   # TYPE zookeeper_sum_om_proposal_process_time_ms untyped
   zookeeper_sum_om_proposal_process_time_ms
   # TYPE zookeeper_sum_pending_session_queue_size untyped
   zookeeper_sum_pending_session_queue_size
   # TYPE zookeeper_sum_prep_process_time untyped
   zookeeper_sum_prep_process_time
   # TYPE zookeeper_sum_prep_processor_queue_size untyped
   zookeeper_sum_prep_processor_queue_size
   # TYPE zookeeper_sum_prep_processor_queue_time_ms untyped
   zookeeper_sum_prep_processor_queue_time_ms
   # TYPE zookeeper_sum_propagation_latency untyped
   zookeeper_sum_propagation_latency
   # TYPE zookeeper_sum_proposal_ack_creation_latency untyped
   zookeeper_sum_proposal_ack_creation_latency
   # TYPE zookeeper_sum_proposal_latency untyped
   zookeeper_sum_proposal_latency
   # TYPE zookeeper_sum_quorum_ack_latency untyped
   zookeeper_sum_quorum_ack_latency
   # TYPE zookeeper_sum_read_commit_proc_issued untyped
   zookeeper_sum_read_commit_proc_issued
   # TYPE zookeeper_sum_read_commit_proc_req_queued untyped
   zookeeper_sum_read_commit_proc_req_queued
   # TYPE zookeeper_sum_read_commitproc_time_ms untyped
   zookeeper_sum_read_commitproc_time_ms
   # TYPE zookeeper_sum_read_final_proc_time_ms untyped
   zookeeper_sum_read_final_proc_time_ms
   # TYPE zookeeper_sum_readlatency untyped
   zookeeper_sum_readlatency
   # TYPE zookeeper_sum_reads_after_write_in_session_queue untyped
   zookeeper_sum_reads_after_write_in_session_queue
   # TYPE zookeeper_sum_reads_issued_from_session_queue untyped
   zookeeper_sum_reads_issued_from_session_queue
   # TYPE zookeeper_sum_requests_in_session_queue untyped
   zookeeper_sum_requests_in_session_queue
   # TYPE zookeeper_sum_server_write_committed_time_ms untyped
   zookeeper_sum_server_write_committed_time_ms
   # TYPE zookeeper_sum_session_queues_drained untyped
   zookeeper_sum_session_queues_drained
   # TYPE zookeeper_sum_snapshottime untyped
   zookeeper_sum_snapshottime
   # TYPE zookeeper_sum_startup_snap_load_time untyped
   zookeeper_sum_startup_snap_load_time
   # TYPE zookeeper_sum_startup_txns_load_time untyped
   zookeeper_sum_startup_txns_load_time
   # TYPE zookeeper_sum_startup_txns_loaded untyped
   zookeeper_sum_startup_txns_loaded
   # TYPE zookeeper_sum_sync_process_time untyped
   zookeeper_sum_sync_process_time
   # TYPE zookeeper_sum_sync_processor_batch_size untyped
   zookeeper_sum_sync_processor_batch_size
   # TYPE zookeeper_sum_sync_processor_queue_and_flush_time_ms untyped
   zookeeper_sum_sync_processor_queue_and_flush_time_ms
   # TYPE zookeeper_sum_sync_processor_queue_flush_time_ms untyped
   zookeeper_sum_sync_processor_queue_flush_time_ms
   # TYPE zookeeper_sum_sync_processor_queue_size untyped
   zookeeper_sum_sync_processor_queue_size
   # TYPE zookeeper_sum_sync_processor_queue_time_ms untyped
   zookeeper_sum_sync_processor_queue_time_ms
   # TYPE zookeeper_sum_time_waiting_empty_pool_in_commit_processor_read_ms untyped
   zookeeper_sum_time_waiting_empty_pool_in_commit_processor_read_ms
   # TYPE zookeeper_sum_updatelatency untyped
   zookeeper_sum_updatelatency
   # TYPE zookeeper_sum_write_batch_time_in_commit_processor untyped
   zookeeper_sum_write_batch_time_in_commit_processor
   # TYPE zookeeper_sum_write_commit_proc_issued untyped
   zookeeper_sum_write_commit_proc_issued
   # TYPE zookeeper_sum_write_commit_proc_req_queued untyped
   zookeeper_sum_write_commit_proc_req_queued
   # TYPE zookeeper_sum_write_commitproc_time_ms untyped
   zookeeper_sum_write_commitproc_time_ms
   # TYPE zookeeper_sum_write_final_proc_time_ms untyped
   zookeeper_sum_write_final_proc_time_ms
   # TYPE zookeeper_sum_zk_cluster_management_write_per_namespace untyped
   zookeeper_sum_zk_cluster_management_write_per_namespace
   # TYPE zookeeper_sum_zookeeper_read_per_namespace untyped
   zookeeper_sum_zookeeper_read_per_namespace
   # TYPE zookeeper_sum_zookeeper_write_per_namespace untyped
   zookeeper_sum_zookeeper_write_per_namespace
   # TYPE zookeeper_sync_processor_request_queued untyped
   zookeeper_sync_processor_request_queued
   # TYPE zookeeper_synced_followers untyped
   zookeeper_synced_followers
   # TYPE zookeeper_synced_non_voting_followers untyped
   zookeeper_synced_non_voting_followers
   # TYPE zookeeper_synced_observers untyped
   zookeeper_synced_observers
   # TYPE zookeeper_tls_handshake_exceeded untyped
   zookeeper_tls_handshake_exceeded
   # TYPE zookeeper_unrecoverable_error_count untyped
   zookeeper_unrecoverable_error_count
   # TYPE zookeeper_uptime untyped
   zookeeper_uptime
   # TYPE zookeeper_watch_count untyped
   zookeeper_watch_count
   # TYPE zookeeper_znode_count untyped
   zookeeper_znode_count
