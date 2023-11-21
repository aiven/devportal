Aiven for Apache Cassandra® metrics available via Prometheus
============================================================

This article provides the list of all metrics available via Prometheus for Aiven for Apache Cassandra® services.

You can retrieve the complete list of available metrics for your service by requesting the Prometheus endpoint as follows:

.. code-block:: bash

    curl --cacert ca.pem \
        --user '<PROMETHEUS_USER>:<PROMETHEUS_PASSWORD>' \
        'https://<CASSANDRA_HOSTNAME>:<PROMETHEUS_PORT>/metrics'

Where you substitute the following:

* Aiven project certificate for ``ca.pem``
* Prometheus credentials for ``<PROMETHEUS_USER>:<PROMETHEUS_PASSWORD>``
* Aiven for Apache Cassandra hostname for ``<CASSANDRA_HOSTNAME>``
* Prometheus port for ``<PROMETHEUS_PORT>``

.. Tip::

    You can check how to use Prometheus with Aiven in :doc:`Prometheus metrics </docs/platform/howto/integrations/prometheus-metrics>`.

.. code-block:: shell

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
    # TYPE java_lang_GarbageCollector_G1_Old_Generation_CollectionCount untyped
    java_lang_GarbageCollector_G1_Old_Generation_CollectionCount
    # TYPE java_lang_GarbageCollector_G1_Old_Generation_CollectionTime untyped
    java_lang_GarbageCollector_G1_Old_Generation_CollectionTime
    # TYPE java_lang_GarbageCollector_G1_Young_Generation_CollectionCount untyped
    java_lang_GarbageCollector_G1_Young_Generation_CollectionCount
    # TYPE java_lang_GarbageCollector_G1_Young_Generation_CollectionTime untyped
    java_lang_GarbageCollector_G1_Young_Generation_CollectionTime
    # TYPE java_lang_Memory_ObjectPendingFinalizationCount untyped
    java_lang_Memory_ObjectPendingFinalizationCount
    # TYPE java_lang_Memory_committed untyped
    java_lang_Memory_committed
    # TYPE java_lang_Memory_init untyped
    java_lang_Memory_init
    # TYPE java_lang_Memory_max untyped
    java_lang_Memory_max
    # TYPE java_lang_Memory_used untyped
    java_lang_Memory_used
    # TYPE java_lang_OperatingSystem_OpenFileDescriptorCount untyped
    java_lang_OperatingSystem_OpenFileDescriptorCount
    # TYPE kafka_jolokia_collector_collect_time untyped
    kafka_jolokia_collector_collect_time
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
    # TYPE net_icmpmsg_intype0 untyped
    net_icmpmsg_intype0
    # TYPE net_icmpmsg_intype11 untyped
    net_icmpmsg_intype11
    # TYPE net_icmpmsg_intype3 untyped
    net_icmpmsg_intype3
    # TYPE net_icmpmsg_intype5 untyped
    net_icmpmsg_intype5
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
    # TYPE org_apache_cassandra_metrics_CQL_PreparedStatementsCount_Value untyped
    org_apache_cassandra_metrics_CQL_PreparedStatementsCount_Value
    # TYPE org_apache_cassandra_metrics_CQL_PreparedStatementsEvicted_Count untyped
    org_apache_cassandra_metrics_CQL_PreparedStatementsEvicted_Count
    # TYPE org_apache_cassandra_metrics_CQL_PreparedStatementsExecuted_Count untyped
    org_apache_cassandra_metrics_CQL_PreparedStatementsExecuted_Count
    # TYPE org_apache_cassandra_metrics_CQL_PreparedStatementsRatio_Value untyped
    org_apache_cassandra_metrics_CQL_PreparedStatementsRatio_Value
    # TYPE org_apache_cassandra_metrics_CQL_RegularStatementsExecuted_Count untyped
    org_apache_cassandra_metrics_CQL_RegularStatementsExecuted_Count
    # TYPE org_apache_cassandra_metrics_Cache_Capacity_Value untyped
    org_apache_cassandra_metrics_Cache_Capacity_Value
    # TYPE org_apache_cassandra_metrics_Cache_Entries_Value untyped
    org_apache_cassandra_metrics_Cache_Entries_Value
    # TYPE org_apache_cassandra_metrics_Cache_FifteenMinuteHitRate_Value untyped
    org_apache_cassandra_metrics_Cache_FifteenMinuteHitRate_Value
    # TYPE org_apache_cassandra_metrics_Cache_FiveMinuteHitRate_Value untyped
    org_apache_cassandra_metrics_Cache_FiveMinuteHitRate_Value
    # TYPE org_apache_cassandra_metrics_Cache_HitRate_Value untyped
    org_apache_cassandra_metrics_Cache_HitRate_Value
    # TYPE org_apache_cassandra_metrics_Cache_Hits_Count untyped
    org_apache_cassandra_metrics_Cache_Hits_Count
    # TYPE org_apache_cassandra_metrics_Cache_Hits_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Cache_Hits_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Cache_Hits_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Cache_Hits_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Cache_Hits_MeanRate untyped
    org_apache_cassandra_metrics_Cache_Hits_MeanRate
    # TYPE org_apache_cassandra_metrics_Cache_Hits_OneMinuteRate untyped
    org_apache_cassandra_metrics_Cache_Hits_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Cache_Misses_Count untyped
    org_apache_cassandra_metrics_Cache_Misses_Count
    # TYPE org_apache_cassandra_metrics_Cache_Misses_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Cache_Misses_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Cache_Misses_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Cache_Misses_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Cache_Misses_MeanRate untyped
    org_apache_cassandra_metrics_Cache_Misses_MeanRate
    # TYPE org_apache_cassandra_metrics_Cache_Misses_OneMinuteRate untyped
    org_apache_cassandra_metrics_Cache_Misses_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Cache_OneMinuteHitRate_Value untyped
    org_apache_cassandra_metrics_Cache_OneMinuteHitRate_Value
    # TYPE org_apache_cassandra_metrics_Cache_Requests_Count untyped
    org_apache_cassandra_metrics_Cache_Requests_Count
    # TYPE org_apache_cassandra_metrics_Cache_Requests_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Cache_Requests_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Cache_Requests_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Cache_Requests_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Cache_Requests_MeanRate untyped
    org_apache_cassandra_metrics_Cache_Requests_MeanRate
    # TYPE org_apache_cassandra_metrics_Cache_Requests_OneMinuteRate untyped
    org_apache_cassandra_metrics_Cache_Requests_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Cache_Size_Value untyped
    org_apache_cassandra_metrics_Cache_Size_Value
    # TYPE org_apache_cassandra_metrics_ClientRequest_ConditionNotMet_Count untyped
    org_apache_cassandra_metrics_ClientRequest_ConditionNotMet_Count
    # TYPE org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_50thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_50thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_75thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_75thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_95thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_95thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_98thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_98thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_999thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_999thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_99thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_99thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_Count untyped
    org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_Count
    # TYPE org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_Max untyped
    org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_Max
    # TYPE org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_Min untyped
    org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_Min
    # TYPE org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_StdDev untyped
    org_apache_cassandra_metrics_ClientRequest_ContentionHistogram_StdDev
    # TYPE org_apache_cassandra_metrics_ClientRequest_Failures_Count untyped
    org_apache_cassandra_metrics_ClientRequest_Failures_Count
    # TYPE org_apache_cassandra_metrics_ClientRequest_Failures_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_Failures_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_Failures_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_Failures_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_Failures_MeanRate untyped
    org_apache_cassandra_metrics_ClientRequest_Failures_MeanRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_Failures_OneMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_Failures_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_Latency_50thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_Latency_50thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_Latency_75thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_Latency_75thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_Latency_95thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_Latency_95thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_Latency_98thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_Latency_98thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_Latency_999thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_Latency_999thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_Latency_99thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_Latency_99thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_Latency_Count untyped
    org_apache_cassandra_metrics_ClientRequest_Latency_Count
    # TYPE org_apache_cassandra_metrics_ClientRequest_Latency_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_Latency_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_Latency_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_Latency_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_Latency_Max untyped
    org_apache_cassandra_metrics_ClientRequest_Latency_Max
    # TYPE org_apache_cassandra_metrics_ClientRequest_Latency_Mean untyped
    org_apache_cassandra_metrics_ClientRequest_Latency_Mean
    # TYPE org_apache_cassandra_metrics_ClientRequest_Latency_MeanRate untyped
    org_apache_cassandra_metrics_ClientRequest_Latency_MeanRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_Latency_Min untyped
    org_apache_cassandra_metrics_ClientRequest_Latency_Min
    # TYPE org_apache_cassandra_metrics_ClientRequest_Latency_OneMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_Latency_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_Latency_StdDev untyped
    org_apache_cassandra_metrics_ClientRequest_Latency_StdDev
    # TYPE org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_50thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_50thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_75thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_75thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_95thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_95thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_98thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_98thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_999thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_999thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_99thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_99thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_Count untyped
    org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_Count
    # TYPE org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_Max untyped
    org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_Max
    # TYPE org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_Mean untyped
    org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_Mean
    # TYPE org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_Min untyped
    org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_Min
    # TYPE org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_StdDev untyped
    org_apache_cassandra_metrics_ClientRequest_MutationSizeHistogram_StdDev
    # TYPE org_apache_cassandra_metrics_ClientRequest_Timeouts_Count untyped
    org_apache_cassandra_metrics_ClientRequest_Timeouts_Count
    # TYPE org_apache_cassandra_metrics_ClientRequest_Timeouts_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_Timeouts_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_Timeouts_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_Timeouts_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_Timeouts_MeanRate untyped
    org_apache_cassandra_metrics_ClientRequest_Timeouts_MeanRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_Timeouts_OneMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_Timeouts_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_TotalLatency_Count untyped
    org_apache_cassandra_metrics_ClientRequest_TotalLatency_Count
    # TYPE org_apache_cassandra_metrics_ClientRequest_Unavailables_Count untyped
    org_apache_cassandra_metrics_ClientRequest_Unavailables_Count
    # TYPE org_apache_cassandra_metrics_ClientRequest_Unavailables_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_Unavailables_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_Unavailables_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_Unavailables_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_Unavailables_MeanRate untyped
    org_apache_cassandra_metrics_ClientRequest_Unavailables_MeanRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_Unavailables_OneMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_Unavailables_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_UnfinishedCommit_Count untyped
    org_apache_cassandra_metrics_ClientRequest_UnfinishedCommit_Count
    # TYPE org_apache_cassandra_metrics_ClientRequest_UnknownResult_Count untyped
    org_apache_cassandra_metrics_ClientRequest_UnknownResult_Count
    # TYPE org_apache_cassandra_metrics_ClientRequest_UnknownResult_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_UnknownResult_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_UnknownResult_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_UnknownResult_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_UnknownResult_MeanRate untyped
    org_apache_cassandra_metrics_ClientRequest_UnknownResult_MeanRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_UnknownResult_OneMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_UnknownResult_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewPendingMutations_Value untyped
    org_apache_cassandra_metrics_ClientRequest_ViewPendingMutations_Value
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewReplicasAttempted_Count untyped
    org_apache_cassandra_metrics_ClientRequest_ViewReplicasAttempted_Count
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewReplicasSuccess_Count untyped
    org_apache_cassandra_metrics_ClientRequest_ViewReplicasSuccess_Count
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_50thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_50thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_75thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_75thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_95thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_95thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_98thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_98thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_999thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_999thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_99thPercentile untyped
    org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_99thPercentile
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_Count untyped
    org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_Count
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_Max untyped
    org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_Max
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_MeanRate untyped
    org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_MeanRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_Min untyped
    org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_Min
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_OneMinuteRate untyped
    org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_StdDev untyped
    org_apache_cassandra_metrics_ClientRequest_ViewWriteLatency_StdDev
    # TYPE org_apache_cassandra_metrics_Client_AuthFailure_Count untyped
    org_apache_cassandra_metrics_Client_AuthFailure_Count
    # TYPE org_apache_cassandra_metrics_Client_AuthFailure_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Client_AuthFailure_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Client_AuthFailure_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Client_AuthFailure_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Client_AuthFailure_MeanRate untyped
    org_apache_cassandra_metrics_Client_AuthFailure_MeanRate
    # TYPE org_apache_cassandra_metrics_Client_AuthFailure_OneMinuteRate untyped
    org_apache_cassandra_metrics_Client_AuthFailure_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Client_AuthSuccess_Count untyped
    org_apache_cassandra_metrics_Client_AuthSuccess_Count
    # TYPE org_apache_cassandra_metrics_Client_AuthSuccess_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Client_AuthSuccess_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Client_AuthSuccess_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Client_AuthSuccess_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Client_AuthSuccess_MeanRate untyped
    org_apache_cassandra_metrics_Client_AuthSuccess_MeanRate
    # TYPE org_apache_cassandra_metrics_Client_AuthSuccess_OneMinuteRate untyped
    org_apache_cassandra_metrics_Client_AuthSuccess_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Client_ConnectedNativeClientsByUser_Value_aiven untyped
    org_apache_cassandra_metrics_Client_ConnectedNativeClientsByUser_Value_aiven
    # TYPE org_apache_cassandra_metrics_Client_ConnectedNativeClientsByUser_Value_avnadmin untyped
    org_apache_cassandra_metrics_Client_ConnectedNativeClientsByUser_Value_avnadmin
    # TYPE org_apache_cassandra_metrics_Client_ConnectedNativeClients_Value untyped
    org_apache_cassandra_metrics_Client_ConnectedNativeClients_Value
    # TYPE org_apache_cassandra_metrics_Client_PausedConnections_Value untyped
    org_apache_cassandra_metrics_Client_PausedConnections_Value
    # TYPE org_apache_cassandra_metrics_Client_ProtocolException_Count untyped
    org_apache_cassandra_metrics_Client_ProtocolException_Count
    # TYPE org_apache_cassandra_metrics_Client_ProtocolException_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Client_ProtocolException_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Client_ProtocolException_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Client_ProtocolException_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Client_ProtocolException_MeanRate untyped
    org_apache_cassandra_metrics_Client_ProtocolException_MeanRate
    # TYPE org_apache_cassandra_metrics_Client_ProtocolException_OneMinuteRate untyped
    org_apache_cassandra_metrics_Client_ProtocolException_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Client_RequestDiscarded_Count untyped
    org_apache_cassandra_metrics_Client_RequestDiscarded_Count
    # TYPE org_apache_cassandra_metrics_Client_RequestDiscarded_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Client_RequestDiscarded_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Client_RequestDiscarded_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Client_RequestDiscarded_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Client_RequestDiscarded_MeanRate untyped
    org_apache_cassandra_metrics_Client_RequestDiscarded_MeanRate
    # TYPE org_apache_cassandra_metrics_Client_RequestDiscarded_OneMinuteRate untyped
    org_apache_cassandra_metrics_Client_RequestDiscarded_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_50thPercentile untyped
    org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_50thPercentile
    # TYPE org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_75thPercentile untyped
    org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_75thPercentile
    # TYPE org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_95thPercentile untyped
    org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_95thPercentile
    # TYPE org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_98thPercentile untyped
    org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_98thPercentile
    # TYPE org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_999thPercentile untyped
    org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_999thPercentile
    # TYPE org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_99thPercentile untyped
    org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_99thPercentile
    # TYPE org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_Count untyped
    org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_Count
    # TYPE org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_Max untyped
    org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_Max
    # TYPE org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_Mean untyped
    org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_Mean
    # TYPE org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_Min untyped
    org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_Min
    # TYPE org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_StdDev untyped
    org_apache_cassandra_metrics_Client_RequestsSizeByIpDistribution_StdDev
    # TYPE org_apache_cassandra_metrics_Client_RequestsSize_Value untyped
    org_apache_cassandra_metrics_Client_RequestsSize_Value
    # TYPE org_apache_cassandra_metrics_Client_UnknownException_Count untyped
    org_apache_cassandra_metrics_Client_UnknownException_Count
    # TYPE org_apache_cassandra_metrics_Client_UnknownException_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Client_UnknownException_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Client_UnknownException_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Client_UnknownException_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Client_UnknownException_MeanRate untyped
    org_apache_cassandra_metrics_Client_UnknownException_MeanRate
    # TYPE org_apache_cassandra_metrics_Client_UnknownException_OneMinuteRate untyped
    org_apache_cassandra_metrics_Client_UnknownException_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Client_connectedNativeClientsByUser_Value_aiven untyped
    org_apache_cassandra_metrics_Client_connectedNativeClientsByUser_Value_aiven
    # TYPE org_apache_cassandra_metrics_Client_connectedNativeClientsByUser_Value_avnadmin untyped
    org_apache_cassandra_metrics_Client_connectedNativeClientsByUser_Value_avnadmin
    # TYPE org_apache_cassandra_metrics_Client_connectedNativeClients_Value untyped
    org_apache_cassandra_metrics_Client_connectedNativeClients_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AdditionalWriteLatencyNanos_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_AdditionalWriteLatencyNanos_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AdditionalWrites_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_AdditionalWrites_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AllMemtablesHeapSize_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_AllMemtablesHeapSize_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AllMemtablesLiveDataSize_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_AllMemtablesLiveDataSize_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AllMemtablesOffHeapDataSize_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_AllMemtablesOffHeapDataSize_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AllMemtablesOffHeapSize_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_AllMemtablesOffHeapSize_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AllMemtablesOnHeapDataSize_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_AllMemtablesOnHeapDataSize_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_MeanRate untyped
    org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_MeanRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_OneMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_AnticompactionTime_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BloomFilterDiskSpaceUsed_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_BloomFilterDiskSpaceUsed_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BloomFilterFalsePositives_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_BloomFilterFalsePositives_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BloomFilterFalseRatio_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_BloomFilterFalseRatio_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BloomFilterOffHeapMemoryUsed_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_BloomFilterOffHeapMemoryUsed_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesAnticompacted_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesAnticompacted_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesFlushed_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesFlushed_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesMutatedAnticompaction_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesMutatedAnticompaction_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesPendingRepair_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesPendingRepair_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesRepaired_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesRepaired_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesUnrepaired_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesUnrepaired_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesValidated_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesValidated_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesValidated_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesValidated_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesValidated_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesValidated_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesValidated_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesValidated_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesValidated_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesValidated_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesValidated_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesValidated_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesValidated_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesValidated_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesValidated_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesValidated_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesValidated_Mean untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesValidated_Mean
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesValidated_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesValidated_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_BytesValidated_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_BytesValidated_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_Mean untyped
    org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_Mean
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_ColUpdateTimeDeltaHistogram_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CompactionBytesWritten_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_CompactionBytesWritten_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CompressionMetadataOffHeapMemoryUsed_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_CompressionMetadataOffHeapMemoryUsed_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CompressionRatio_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_CompressionRatio_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_Mean untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_Mean
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_MeanRate untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_MeanRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_OneMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorReadLatency_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_Mean untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_Mean
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_MeanRate untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_MeanRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_OneMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorScanLatency_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_Mean untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_Mean
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_MeanRate untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_MeanRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_OneMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_CoordinatorWriteLatency_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_DroppedMutations_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_DroppedMutations_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_EstimatedRowCount_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_EstimatedRowCount_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_IndexSummaryOffHeapMemoryUsed_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_IndexSummaryOffHeapMemoryUsed_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_KeyCacheHitRate_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_KeyCacheHitRate_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_LiveDiskSpaceUsed_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_LiveDiskSpaceUsed_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_LiveSSTableCount_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_LiveSSTableCount_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_Mean untyped
    org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_Mean
    # TYPE org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_LiveScannedHistogram_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_MaxRowSize_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_MaxRowSize_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_MeanRowSize_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_MeanRowSize_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_MemtableColumnsCount_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_MemtableColumnsCount_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_MemtableLiveDataSize_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_MemtableLiveDataSize_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_MemtableOffHeapDataSize_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_MemtableOffHeapDataSize_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_MemtableOffHeapSize_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_MemtableOffHeapSize_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_MemtableOnHeapDataSize_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_MemtableOnHeapDataSize_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_MemtableOnHeapSize_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_MemtableOnHeapSize_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_MemtableSwitchCount_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_MemtableSwitchCount_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_MinRowSize_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_MinRowSize_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_MutatedAnticompactionGauge_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_MutatedAnticompactionGauge_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_OldVersionSSTableCount_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_OldVersionSSTableCount_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_Mean untyped
    org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_Mean
    # TYPE org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_PartitionsValidated_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_PendingCompactions_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_PendingCompactions_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_PendingFlushes_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_PendingFlushes_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_PercentRepaired_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_PercentRepaired_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReadRepairRequests_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_ReadRepairRequests_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReadRepairRequests_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ReadRepairRequests_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReadRepairRequests_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ReadRepairRequests_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReadRepairRequests_MeanRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ReadRepairRequests_MeanRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReadRepairRequests_OneMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ReadRepairRequests_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RecentBloomFilterFalsePositives_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_RecentBloomFilterFalsePositives_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RecentBloomFilterFalseRatio_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_RecentBloomFilterFalseRatio_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairJobsCompleted_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairJobsCompleted_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairJobsStarted_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairJobsStarted_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_MeanRate untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_MeanRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_OneMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairSyncTime_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesConfirmed_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesConfirmed_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesConfirmed_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesConfirmed_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesConfirmed_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesConfirmed_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesConfirmed_MeanRate untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesConfirmed_MeanRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesConfirmed_OneMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesConfirmed_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesUnconfirmed_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesUnconfirmed_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesUnconfirmed_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesUnconfirmed_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesUnconfirmed_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesUnconfirmed_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesUnconfirmed_MeanRate untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesUnconfirmed_MeanRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesUnconfirmed_OneMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataInconsistenciesUnconfirmed_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadRows_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_MeanRate untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_MeanRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_OneMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_RepairedDataTrackingOverreadTime_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRequests_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRequests_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRequests_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRequests_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRequests_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRequests_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRequests_MeanRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRequests_MeanRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRequests_OneMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRequests_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_ReplicaFilteringProtectionRowsCachedPerQuery_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RowCacheHitOutOfRange_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_RowCacheHitOutOfRange_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RowCacheHit_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_RowCacheHit_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_RowCacheMiss_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_RowCacheMiss_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_Mean untyped
    org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_Mean
    # TYPE org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_SSTablesPerReadHistogram_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ShortReadProtectionRequests_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_ShortReadProtectionRequests_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ShortReadProtectionRequests_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ShortReadProtectionRequests_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ShortReadProtectionRequests_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ShortReadProtectionRequests_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ShortReadProtectionRequests_MeanRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ShortReadProtectionRequests_MeanRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ShortReadProtectionRequests_OneMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ShortReadProtectionRequests_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_SnapshotsSize_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_SnapshotsSize_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_SpeculativeFailedRetries_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_SpeculativeFailedRetries_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_SpeculativeInsufficientReplicas_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_SpeculativeInsufficientReplicas_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_SpeculativeRetries_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_SpeculativeRetries_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_SpeculativeSampleLatencyNanos_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_SpeculativeSampleLatencyNanos_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_TombstoneFailures_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_TombstoneFailures_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_Mean untyped
    org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_Mean
    # TYPE org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_TombstoneScannedHistogram_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_TombstoneWarnings_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_TombstoneWarnings_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_TotalDiskSpaceUsed_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_TotalDiskSpaceUsed_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_UnleveledSSTables_Value untyped
    org_apache_cassandra_metrics_ColumnFamily_UnleveledSSTables_Value
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ValidationTime_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ValidationTime_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ValidationTime_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ValidationTime_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ValidationTime_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ValidationTime_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ValidationTime_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ValidationTime_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ValidationTime_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ValidationTime_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ValidationTime_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ValidationTime_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ValidationTime_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_ValidationTime_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ValidationTime_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ValidationTime_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ValidationTime_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ValidationTime_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ValidationTime_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_ValidationTime_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ValidationTime_Mean untyped
    org_apache_cassandra_metrics_ColumnFamily_ValidationTime_Mean
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ValidationTime_MeanRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ValidationTime_MeanRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ValidationTime_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_ValidationTime_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ValidationTime_OneMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ValidationTime_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ValidationTime_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_ValidationTime_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_MeanRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_MeanRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_OneMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewLockAcquireTime_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_MeanRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_MeanRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_OneMinuteRate untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_ViewReadTime_StdDev
    # TYPE org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_50thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_50thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_75thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_75thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_95thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_95thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_98thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_98thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_999thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_999thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_99thPercentile untyped
    org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_99thPercentile
    # TYPE org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_Count untyped
    org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_Count
    # TYPE org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_Max untyped
    org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_Max
    # TYPE org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_Min untyped
    org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_Min
    # TYPE org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_StdDev untyped
    org_apache_cassandra_metrics_ColumnFamily_WaitingOnFreeMemtableSpace_StdDev
    # TYPE org_apache_cassandra_metrics_CommitLog_CompletedTasks_Value untyped
    org_apache_cassandra_metrics_CommitLog_CompletedTasks_Value
    # TYPE org_apache_cassandra_metrics_CommitLog_OverSizedMutations_Count untyped
    org_apache_cassandra_metrics_CommitLog_OverSizedMutations_Count
    # TYPE org_apache_cassandra_metrics_CommitLog_OverSizedMutations_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_CommitLog_OverSizedMutations_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_CommitLog_OverSizedMutations_FiveMinuteRate untyped
    org_apache_cassandra_metrics_CommitLog_OverSizedMutations_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_CommitLog_OverSizedMutations_MeanRate untyped
    org_apache_cassandra_metrics_CommitLog_OverSizedMutations_MeanRate
    # TYPE org_apache_cassandra_metrics_CommitLog_OverSizedMutations_OneMinuteRate untyped
    org_apache_cassandra_metrics_CommitLog_OverSizedMutations_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_CommitLog_PendingTasks_Value untyped
    org_apache_cassandra_metrics_CommitLog_PendingTasks_Value
    # TYPE org_apache_cassandra_metrics_CommitLog_TotalCommitLogSize_Value untyped
    org_apache_cassandra_metrics_CommitLog_TotalCommitLogSize_Value
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_50thPercentile untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_50thPercentile
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_75thPercentile untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_75thPercentile
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_95thPercentile untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_95thPercentile
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_98thPercentile untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_98thPercentile
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_999thPercentile untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_999thPercentile
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_99thPercentile untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_99thPercentile
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_Count untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_Count
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_FiveMinuteRate untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_Max untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_Max
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_MeanRate untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_MeanRate
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_Min untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_Min
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_OneMinuteRate untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_StdDev untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnCommit_StdDev
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_50thPercentile untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_50thPercentile
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_75thPercentile untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_75thPercentile
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_95thPercentile untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_95thPercentile
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_98thPercentile untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_98thPercentile
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_999thPercentile untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_999thPercentile
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_99thPercentile untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_99thPercentile
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_Count untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_Count
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_FiveMinuteRate untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_Max untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_Max
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_MeanRate untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_MeanRate
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_Min untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_Min
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_OneMinuteRate untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_StdDev untyped
    org_apache_cassandra_metrics_CommitLog_WaitingOnSegmentAllocation_StdDev
    # TYPE org_apache_cassandra_metrics_Compaction_BytesCompacted_Count untyped
    org_apache_cassandra_metrics_Compaction_BytesCompacted_Count
    # TYPE org_apache_cassandra_metrics_Compaction_CompactionsAborted_Count untyped
    org_apache_cassandra_metrics_Compaction_CompactionsAborted_Count
    # TYPE org_apache_cassandra_metrics_Compaction_CompactionsReduced_Count untyped
    org_apache_cassandra_metrics_Compaction_CompactionsReduced_Count
    # TYPE org_apache_cassandra_metrics_Compaction_CompletedTasks_Value untyped
    org_apache_cassandra_metrics_Compaction_CompletedTasks_Value
    # TYPE org_apache_cassandra_metrics_Compaction_PendingTasksByTableName_Value_effect_clicks_by_dist_id_v2 untyped
    org_apache_cassandra_metrics_Compaction_PendingTasksByTableName_Value_effect_clicks_by_dist_id_v2
    # TYPE org_apache_cassandra_metrics_Compaction_PendingTasks_Value untyped
    org_apache_cassandra_metrics_Compaction_PendingTasks_Value
    # TYPE org_apache_cassandra_metrics_Compaction_SSTablesDroppedFromCompaction_Count untyped
    org_apache_cassandra_metrics_Compaction_SSTablesDroppedFromCompaction_Count
    # TYPE org_apache_cassandra_metrics_Compaction_TotalCompactionsCompleted_Count untyped
    org_apache_cassandra_metrics_Compaction_TotalCompactionsCompleted_Count
    # TYPE org_apache_cassandra_metrics_Compaction_TotalCompactionsCompleted_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Compaction_TotalCompactionsCompleted_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Compaction_TotalCompactionsCompleted_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Compaction_TotalCompactionsCompleted_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Compaction_TotalCompactionsCompleted_MeanRate untyped
    org_apache_cassandra_metrics_Compaction_TotalCompactionsCompleted_MeanRate
    # TYPE org_apache_cassandra_metrics_Compaction_TotalCompactionsCompleted_OneMinuteRate untyped
    org_apache_cassandra_metrics_Compaction_TotalCompactionsCompleted_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Connection_TotalTimeouts_OneMinuteRate untyped
    org_apache_cassandra_metrics_Connection_TotalTimeouts_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_50thPercentile untyped
    org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_50thPercentile
    # TYPE org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_75thPercentile untyped
    org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_75thPercentile
    # TYPE org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_95thPercentile untyped
    org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_95thPercentile
    # TYPE org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_98thPercentile untyped
    org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_98thPercentile
    # TYPE org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_999thPercentile untyped
    org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_999thPercentile
    # TYPE org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_99thPercentile untyped
    org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_99thPercentile
    # TYPE org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_Count untyped
    org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_Count
    # TYPE org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_FiveMinuteRate untyped
    org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_Max untyped
    org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_Max
    # TYPE org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_MeanRate untyped
    org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_MeanRate
    # TYPE org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_Min untyped
    org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_Min
    # TYPE org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_OneMinuteRate untyped
    org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_StdDev untyped
    org_apache_cassandra_metrics_DroppedMessage_CrossNodeDroppedLatency_StdDev
    # TYPE org_apache_cassandra_metrics_DroppedMessage_Dropped_Count untyped
    org_apache_cassandra_metrics_DroppedMessage_Dropped_Count
    # TYPE org_apache_cassandra_metrics_DroppedMessage_Dropped_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_DroppedMessage_Dropped_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_DroppedMessage_Dropped_FiveMinuteRate untyped
    org_apache_cassandra_metrics_DroppedMessage_Dropped_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_DroppedMessage_Dropped_MeanRate untyped
    org_apache_cassandra_metrics_DroppedMessage_Dropped_MeanRate
    # TYPE org_apache_cassandra_metrics_DroppedMessage_Dropped_OneMinuteRate untyped
    org_apache_cassandra_metrics_DroppedMessage_Dropped_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_50thPercentile untyped
    org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_50thPercentile
    # TYPE org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_75thPercentile untyped
    org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_75thPercentile
    # TYPE org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_95thPercentile untyped
    org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_95thPercentile
    # TYPE org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_98thPercentile untyped
    org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_98thPercentile
    # TYPE org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_999thPercentile untyped
    org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_999thPercentile
    # TYPE org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_99thPercentile untyped
    org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_99thPercentile
    # TYPE org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_Count untyped
    org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_Count
    # TYPE org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_FiveMinuteRate untyped
    org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_Max untyped
    org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_Max
    # TYPE org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_MeanRate untyped
    org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_MeanRate
    # TYPE org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_Min untyped
    org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_Min
    # TYPE org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_OneMinuteRate untyped
    org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_StdDev untyped
    org_apache_cassandra_metrics_DroppedMessage_InternalDroppedLatency_StdDev
    # TYPE org_apache_cassandra_metrics_Keyspace_SSTablesPerReadHistogram_95thPercentile untyped
    org_apache_cassandra_metrics_Keyspace_SSTablesPerReadHistogram_95thPercentile
    # TYPE org_apache_cassandra_metrics_Keyspace_SSTablesPerReadHistogram_99thPercentile untyped
    org_apache_cassandra_metrics_Keyspace_SSTablesPerReadHistogram_99thPercentile
    # TYPE org_apache_cassandra_metrics_Keyspace_SSTablesPerReadHistogram_Mean untyped
    org_apache_cassandra_metrics_Keyspace_SSTablesPerReadHistogram_Mean
    # TYPE org_apache_cassandra_metrics_ReadRepair_Attempted_Count untyped
    org_apache_cassandra_metrics_ReadRepair_Attempted_Count
    # TYPE org_apache_cassandra_metrics_ReadRepair_Attempted_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_Attempted_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_Attempted_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_Attempted_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_Attempted_MeanRate untyped
    org_apache_cassandra_metrics_ReadRepair_Attempted_MeanRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_Attempted_OneMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_Attempted_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_ReconcileRead_Count untyped
    org_apache_cassandra_metrics_ReadRepair_ReconcileRead_Count
    # TYPE org_apache_cassandra_metrics_ReadRepair_ReconcileRead_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_ReconcileRead_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_ReconcileRead_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_ReconcileRead_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_ReconcileRead_MeanRate untyped
    org_apache_cassandra_metrics_ReadRepair_ReconcileRead_MeanRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_ReconcileRead_OneMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_ReconcileRead_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_RepairedBackground_Count untyped
    org_apache_cassandra_metrics_ReadRepair_RepairedBackground_Count
    # TYPE org_apache_cassandra_metrics_ReadRepair_RepairedBackground_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_RepairedBackground_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_RepairedBackground_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_RepairedBackground_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_RepairedBackground_MeanRate untyped
    org_apache_cassandra_metrics_ReadRepair_RepairedBackground_MeanRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_RepairedBackground_OneMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_RepairedBackground_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_RepairedBlocking_Count untyped
    org_apache_cassandra_metrics_ReadRepair_RepairedBlocking_Count
    # TYPE org_apache_cassandra_metrics_ReadRepair_RepairedBlocking_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_RepairedBlocking_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_RepairedBlocking_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_RepairedBlocking_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_RepairedBlocking_MeanRate untyped
    org_apache_cassandra_metrics_ReadRepair_RepairedBlocking_MeanRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_RepairedBlocking_OneMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_RepairedBlocking_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_SpeculatedRead_Count untyped
    org_apache_cassandra_metrics_ReadRepair_SpeculatedRead_Count
    # TYPE org_apache_cassandra_metrics_ReadRepair_SpeculatedRead_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_SpeculatedRead_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_SpeculatedRead_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_SpeculatedRead_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_SpeculatedRead_MeanRate untyped
    org_apache_cassandra_metrics_ReadRepair_SpeculatedRead_MeanRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_SpeculatedRead_OneMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_SpeculatedRead_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_SpeculatedWrite_Count untyped
    org_apache_cassandra_metrics_ReadRepair_SpeculatedWrite_Count
    # TYPE org_apache_cassandra_metrics_ReadRepair_SpeculatedWrite_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_SpeculatedWrite_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_SpeculatedWrite_FiveMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_SpeculatedWrite_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_SpeculatedWrite_MeanRate untyped
    org_apache_cassandra_metrics_ReadRepair_SpeculatedWrite_MeanRate
    # TYPE org_apache_cassandra_metrics_ReadRepair_SpeculatedWrite_OneMinuteRate untyped
    org_apache_cassandra_metrics_ReadRepair_SpeculatedWrite_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Storage_Exceptions_Count untyped
    org_apache_cassandra_metrics_Storage_Exceptions_Count
    # TYPE org_apache_cassandra_metrics_Storage_Load_Count untyped
    org_apache_cassandra_metrics_Storage_Load_Count
    # TYPE org_apache_cassandra_metrics_Storage_RepairExceptions_Count untyped
    org_apache_cassandra_metrics_Storage_RepairExceptions_Count
    # TYPE org_apache_cassandra_metrics_Storage_TotalHintsInProgress_Count untyped
    org_apache_cassandra_metrics_Storage_TotalHintsInProgress_Count
    # TYPE org_apache_cassandra_metrics_Storage_TotalHints_Count untyped
    org_apache_cassandra_metrics_Storage_TotalHints_Count
    # TYPE org_apache_cassandra_metrics_Table_AdditionalWriteLatencyNanos_Value untyped
    org_apache_cassandra_metrics_Table_AdditionalWriteLatencyNanos_Value
    # TYPE org_apache_cassandra_metrics_Table_AdditionalWrites_Count untyped
    org_apache_cassandra_metrics_Table_AdditionalWrites_Count
    # TYPE org_apache_cassandra_metrics_Table_AllMemtablesHeapSize_Value untyped
    org_apache_cassandra_metrics_Table_AllMemtablesHeapSize_Value
    # TYPE org_apache_cassandra_metrics_Table_AllMemtablesLiveDataSize_Value untyped
    org_apache_cassandra_metrics_Table_AllMemtablesLiveDataSize_Value
    # TYPE org_apache_cassandra_metrics_Table_AllMemtablesOffHeapDataSize_Value untyped
    org_apache_cassandra_metrics_Table_AllMemtablesOffHeapDataSize_Value
    # TYPE org_apache_cassandra_metrics_Table_AllMemtablesOffHeapSize_Value untyped
    org_apache_cassandra_metrics_Table_AllMemtablesOffHeapSize_Value
    # TYPE org_apache_cassandra_metrics_Table_AllMemtablesOnHeapDataSize_Value untyped
    org_apache_cassandra_metrics_Table_AllMemtablesOnHeapDataSize_Value
    # TYPE org_apache_cassandra_metrics_Table_AnticompactionTime_50thPercentile untyped
    org_apache_cassandra_metrics_Table_AnticompactionTime_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_AnticompactionTime_75thPercentile untyped
    org_apache_cassandra_metrics_Table_AnticompactionTime_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_AnticompactionTime_95thPercentile untyped
    org_apache_cassandra_metrics_Table_AnticompactionTime_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_AnticompactionTime_98thPercentile untyped
    org_apache_cassandra_metrics_Table_AnticompactionTime_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_AnticompactionTime_999thPercentile untyped
    org_apache_cassandra_metrics_Table_AnticompactionTime_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_AnticompactionTime_99thPercentile untyped
    org_apache_cassandra_metrics_Table_AnticompactionTime_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_AnticompactionTime_Count untyped
    org_apache_cassandra_metrics_Table_AnticompactionTime_Count
    # TYPE org_apache_cassandra_metrics_Table_AnticompactionTime_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_AnticompactionTime_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_AnticompactionTime_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_AnticompactionTime_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_AnticompactionTime_Max untyped
    org_apache_cassandra_metrics_Table_AnticompactionTime_Max
    # TYPE org_apache_cassandra_metrics_Table_AnticompactionTime_MeanRate untyped
    org_apache_cassandra_metrics_Table_AnticompactionTime_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_AnticompactionTime_Min untyped
    org_apache_cassandra_metrics_Table_AnticompactionTime_Min
    # TYPE org_apache_cassandra_metrics_Table_AnticompactionTime_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_AnticompactionTime_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_AnticompactionTime_StdDev untyped
    org_apache_cassandra_metrics_Table_AnticompactionTime_StdDev
    # TYPE org_apache_cassandra_metrics_Table_BloomFilterDiskSpaceUsed_Value untyped
    org_apache_cassandra_metrics_Table_BloomFilterDiskSpaceUsed_Value
    # TYPE org_apache_cassandra_metrics_Table_BloomFilterFalsePositives_Value untyped
    org_apache_cassandra_metrics_Table_BloomFilterFalsePositives_Value
    # TYPE org_apache_cassandra_metrics_Table_BloomFilterFalseRatio_Value untyped
    org_apache_cassandra_metrics_Table_BloomFilterFalseRatio_Value
    # TYPE org_apache_cassandra_metrics_Table_BloomFilterOffHeapMemoryUsed_Value untyped
    org_apache_cassandra_metrics_Table_BloomFilterOffHeapMemoryUsed_Value
    # TYPE org_apache_cassandra_metrics_Table_BytesAnticompacted_Count untyped
    org_apache_cassandra_metrics_Table_BytesAnticompacted_Count
    # TYPE org_apache_cassandra_metrics_Table_BytesFlushed_Count untyped
    org_apache_cassandra_metrics_Table_BytesFlushed_Count
    # TYPE org_apache_cassandra_metrics_Table_BytesMutatedAnticompaction_Count untyped
    org_apache_cassandra_metrics_Table_BytesMutatedAnticompaction_Count
    # TYPE org_apache_cassandra_metrics_Table_BytesPendingRepair_Value untyped
    org_apache_cassandra_metrics_Table_BytesPendingRepair_Value
    # TYPE org_apache_cassandra_metrics_Table_BytesRepaired_Value untyped
    org_apache_cassandra_metrics_Table_BytesRepaired_Value
    # TYPE org_apache_cassandra_metrics_Table_BytesUnrepaired_Value untyped
    org_apache_cassandra_metrics_Table_BytesUnrepaired_Value
    # TYPE org_apache_cassandra_metrics_Table_BytesValidated_50thPercentile untyped
    org_apache_cassandra_metrics_Table_BytesValidated_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_BytesValidated_75thPercentile untyped
    org_apache_cassandra_metrics_Table_BytesValidated_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_BytesValidated_95thPercentile untyped
    org_apache_cassandra_metrics_Table_BytesValidated_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_BytesValidated_98thPercentile untyped
    org_apache_cassandra_metrics_Table_BytesValidated_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_BytesValidated_999thPercentile untyped
    org_apache_cassandra_metrics_Table_BytesValidated_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_BytesValidated_99thPercentile untyped
    org_apache_cassandra_metrics_Table_BytesValidated_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_BytesValidated_Count untyped
    org_apache_cassandra_metrics_Table_BytesValidated_Count
    # TYPE org_apache_cassandra_metrics_Table_BytesValidated_Max untyped
    org_apache_cassandra_metrics_Table_BytesValidated_Max
    # TYPE org_apache_cassandra_metrics_Table_BytesValidated_Mean untyped
    org_apache_cassandra_metrics_Table_BytesValidated_Mean
    # TYPE org_apache_cassandra_metrics_Table_BytesValidated_Min untyped
    org_apache_cassandra_metrics_Table_BytesValidated_Min
    # TYPE org_apache_cassandra_metrics_Table_BytesValidated_StdDev untyped
    org_apache_cassandra_metrics_Table_BytesValidated_StdDev
    # TYPE org_apache_cassandra_metrics_Table_CasCommitLatency_50thPercentile untyped
    org_apache_cassandra_metrics_Table_CasCommitLatency_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasCommitLatency_75thPercentile untyped
    org_apache_cassandra_metrics_Table_CasCommitLatency_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasCommitLatency_95thPercentile untyped
    org_apache_cassandra_metrics_Table_CasCommitLatency_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasCommitLatency_98thPercentile untyped
    org_apache_cassandra_metrics_Table_CasCommitLatency_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasCommitLatency_999thPercentile untyped
    org_apache_cassandra_metrics_Table_CasCommitLatency_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasCommitLatency_99thPercentile untyped
    org_apache_cassandra_metrics_Table_CasCommitLatency_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasCommitLatency_Count untyped
    org_apache_cassandra_metrics_Table_CasCommitLatency_Count
    # TYPE org_apache_cassandra_metrics_Table_CasCommitLatency_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_CasCommitLatency_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CasCommitLatency_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_CasCommitLatency_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CasCommitLatency_Max untyped
    org_apache_cassandra_metrics_Table_CasCommitLatency_Max
    # TYPE org_apache_cassandra_metrics_Table_CasCommitLatency_MeanRate untyped
    org_apache_cassandra_metrics_Table_CasCommitLatency_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_CasCommitLatency_Min untyped
    org_apache_cassandra_metrics_Table_CasCommitLatency_Min
    # TYPE org_apache_cassandra_metrics_Table_CasCommitLatency_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_CasCommitLatency_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CasCommitLatency_StdDev untyped
    org_apache_cassandra_metrics_Table_CasCommitLatency_StdDev
    # TYPE org_apache_cassandra_metrics_Table_CasCommitTotalLatency_Count untyped
    org_apache_cassandra_metrics_Table_CasCommitTotalLatency_Count
    # TYPE org_apache_cassandra_metrics_Table_CasPrepareLatency_50thPercentile untyped
    org_apache_cassandra_metrics_Table_CasPrepareLatency_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasPrepareLatency_75thPercentile untyped
    org_apache_cassandra_metrics_Table_CasPrepareLatency_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasPrepareLatency_95thPercentile untyped
    org_apache_cassandra_metrics_Table_CasPrepareLatency_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasPrepareLatency_98thPercentile untyped
    org_apache_cassandra_metrics_Table_CasPrepareLatency_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasPrepareLatency_999thPercentile untyped
    org_apache_cassandra_metrics_Table_CasPrepareLatency_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasPrepareLatency_99thPercentile untyped
    org_apache_cassandra_metrics_Table_CasPrepareLatency_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasPrepareLatency_Count untyped
    org_apache_cassandra_metrics_Table_CasPrepareLatency_Count
    # TYPE org_apache_cassandra_metrics_Table_CasPrepareLatency_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_CasPrepareLatency_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CasPrepareLatency_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_CasPrepareLatency_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CasPrepareLatency_Max untyped
    org_apache_cassandra_metrics_Table_CasPrepareLatency_Max
    # TYPE org_apache_cassandra_metrics_Table_CasPrepareLatency_MeanRate untyped
    org_apache_cassandra_metrics_Table_CasPrepareLatency_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_CasPrepareLatency_Min untyped
    org_apache_cassandra_metrics_Table_CasPrepareLatency_Min
    # TYPE org_apache_cassandra_metrics_Table_CasPrepareLatency_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_CasPrepareLatency_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CasPrepareLatency_StdDev untyped
    org_apache_cassandra_metrics_Table_CasPrepareLatency_StdDev
    # TYPE org_apache_cassandra_metrics_Table_CasPrepareTotalLatency_Count untyped
    org_apache_cassandra_metrics_Table_CasPrepareTotalLatency_Count
    # TYPE org_apache_cassandra_metrics_Table_CasProposeLatency_50thPercentile untyped
    org_apache_cassandra_metrics_Table_CasProposeLatency_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasProposeLatency_75thPercentile untyped
    org_apache_cassandra_metrics_Table_CasProposeLatency_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasProposeLatency_95thPercentile untyped
    org_apache_cassandra_metrics_Table_CasProposeLatency_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasProposeLatency_98thPercentile untyped
    org_apache_cassandra_metrics_Table_CasProposeLatency_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasProposeLatency_999thPercentile untyped
    org_apache_cassandra_metrics_Table_CasProposeLatency_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasProposeLatency_99thPercentile untyped
    org_apache_cassandra_metrics_Table_CasProposeLatency_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CasProposeLatency_Count untyped
    org_apache_cassandra_metrics_Table_CasProposeLatency_Count
    # TYPE org_apache_cassandra_metrics_Table_CasProposeLatency_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_CasProposeLatency_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CasProposeLatency_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_CasProposeLatency_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CasProposeLatency_Max untyped
    org_apache_cassandra_metrics_Table_CasProposeLatency_Max
    # TYPE org_apache_cassandra_metrics_Table_CasProposeLatency_MeanRate untyped
    org_apache_cassandra_metrics_Table_CasProposeLatency_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_CasProposeLatency_Min untyped
    org_apache_cassandra_metrics_Table_CasProposeLatency_Min
    # TYPE org_apache_cassandra_metrics_Table_CasProposeLatency_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_CasProposeLatency_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CasProposeLatency_StdDev untyped
    org_apache_cassandra_metrics_Table_CasProposeLatency_StdDev
    # TYPE org_apache_cassandra_metrics_Table_CasProposeTotalLatency_Count untyped
    org_apache_cassandra_metrics_Table_CasProposeTotalLatency_Count
    # TYPE org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_50thPercentile untyped
    org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_75thPercentile untyped
    org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_95thPercentile untyped
    org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_98thPercentile untyped
    org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_999thPercentile untyped
    org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_99thPercentile untyped
    org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_Count untyped
    org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_Count
    # TYPE org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_Max untyped
    org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_Max
    # TYPE org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_Mean untyped
    org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_Mean
    # TYPE org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_Min untyped
    org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_Min
    # TYPE org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_StdDev untyped
    org_apache_cassandra_metrics_Table_ColUpdateTimeDeltaHistogram_StdDev
    # TYPE org_apache_cassandra_metrics_Table_CompactionBytesWritten_Count untyped
    org_apache_cassandra_metrics_Table_CompactionBytesWritten_Count
    # TYPE org_apache_cassandra_metrics_Table_CompressionMetadataOffHeapMemoryUsed_Value untyped
    org_apache_cassandra_metrics_Table_CompressionMetadataOffHeapMemoryUsed_Value
    # TYPE org_apache_cassandra_metrics_Table_CompressionRatio_Value untyped
    org_apache_cassandra_metrics_Table_CompressionRatio_Value
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorReadLatency_50thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorReadLatency_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorReadLatency_75thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorReadLatency_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorReadLatency_95thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorReadLatency_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorReadLatency_98thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorReadLatency_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorReadLatency_999thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorReadLatency_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorReadLatency_99thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorReadLatency_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorReadLatency_Count untyped
    org_apache_cassandra_metrics_Table_CoordinatorReadLatency_Count
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorReadLatency_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_CoordinatorReadLatency_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorReadLatency_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_CoordinatorReadLatency_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorReadLatency_Max untyped
    org_apache_cassandra_metrics_Table_CoordinatorReadLatency_Max
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorReadLatency_Mean untyped
    org_apache_cassandra_metrics_Table_CoordinatorReadLatency_Mean
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorReadLatency_MeanRate untyped
    org_apache_cassandra_metrics_Table_CoordinatorReadLatency_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorReadLatency_Min untyped
    org_apache_cassandra_metrics_Table_CoordinatorReadLatency_Min
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorReadLatency_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_CoordinatorReadLatency_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorReadLatency_StdDev untyped
    org_apache_cassandra_metrics_Table_CoordinatorReadLatency_StdDev
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorScanLatency_50thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorScanLatency_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorScanLatency_75thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorScanLatency_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorScanLatency_95thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorScanLatency_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorScanLatency_98thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorScanLatency_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorScanLatency_999thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorScanLatency_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorScanLatency_99thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorScanLatency_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorScanLatency_Count untyped
    org_apache_cassandra_metrics_Table_CoordinatorScanLatency_Count
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorScanLatency_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_CoordinatorScanLatency_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorScanLatency_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_CoordinatorScanLatency_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorScanLatency_Max untyped
    org_apache_cassandra_metrics_Table_CoordinatorScanLatency_Max
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorScanLatency_Mean untyped
    org_apache_cassandra_metrics_Table_CoordinatorScanLatency_Mean
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorScanLatency_MeanRate untyped
    org_apache_cassandra_metrics_Table_CoordinatorScanLatency_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorScanLatency_Min untyped
    org_apache_cassandra_metrics_Table_CoordinatorScanLatency_Min
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorScanLatency_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_CoordinatorScanLatency_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorScanLatency_StdDev untyped
    org_apache_cassandra_metrics_Table_CoordinatorScanLatency_StdDev
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_50thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_75thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_95thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_98thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_999thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_99thPercentile untyped
    org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_Count untyped
    org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_Count
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_Max untyped
    org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_Max
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_Mean untyped
    org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_Mean
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_MeanRate untyped
    org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_Min untyped
    org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_Min
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_StdDev untyped
    org_apache_cassandra_metrics_Table_CoordinatorWriteLatency_StdDev
    # TYPE org_apache_cassandra_metrics_Table_DroppedMutations_Count untyped
    org_apache_cassandra_metrics_Table_DroppedMutations_Count
    # TYPE org_apache_cassandra_metrics_Table_EstimatedPartitionCount_Value untyped
    org_apache_cassandra_metrics_Table_EstimatedPartitionCount_Value
    # TYPE org_apache_cassandra_metrics_Table_IndexSummaryOffHeapMemoryUsed_Value untyped
    org_apache_cassandra_metrics_Table_IndexSummaryOffHeapMemoryUsed_Value
    # TYPE org_apache_cassandra_metrics_Table_KeyCacheHitRate_Value untyped
    org_apache_cassandra_metrics_Table_KeyCacheHitRate_Value
    # TYPE org_apache_cassandra_metrics_Table_LiveDiskSpaceUsed_Count untyped
    org_apache_cassandra_metrics_Table_LiveDiskSpaceUsed_Count
    # TYPE org_apache_cassandra_metrics_Table_LiveSSTableCount_Value untyped
    org_apache_cassandra_metrics_Table_LiveSSTableCount_Value
    # TYPE org_apache_cassandra_metrics_Table_LiveScannedHistogram_50thPercentile untyped
    org_apache_cassandra_metrics_Table_LiveScannedHistogram_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_LiveScannedHistogram_75thPercentile untyped
    org_apache_cassandra_metrics_Table_LiveScannedHistogram_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_LiveScannedHistogram_95thPercentile untyped
    org_apache_cassandra_metrics_Table_LiveScannedHistogram_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_LiveScannedHistogram_98thPercentile untyped
    org_apache_cassandra_metrics_Table_LiveScannedHistogram_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_LiveScannedHistogram_999thPercentile untyped
    org_apache_cassandra_metrics_Table_LiveScannedHistogram_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_LiveScannedHistogram_99thPercentile untyped
    org_apache_cassandra_metrics_Table_LiveScannedHistogram_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_LiveScannedHistogram_Count untyped
    org_apache_cassandra_metrics_Table_LiveScannedHistogram_Count
    # TYPE org_apache_cassandra_metrics_Table_LiveScannedHistogram_Max untyped
    org_apache_cassandra_metrics_Table_LiveScannedHistogram_Max
    # TYPE org_apache_cassandra_metrics_Table_LiveScannedHistogram_Mean untyped
    org_apache_cassandra_metrics_Table_LiveScannedHistogram_Mean
    # TYPE org_apache_cassandra_metrics_Table_LiveScannedHistogram_Min untyped
    org_apache_cassandra_metrics_Table_LiveScannedHistogram_Min
    # TYPE org_apache_cassandra_metrics_Table_LiveScannedHistogram_StdDev untyped
    org_apache_cassandra_metrics_Table_LiveScannedHistogram_StdDev
    # TYPE org_apache_cassandra_metrics_Table_MaxPartitionSize_Value untyped
    org_apache_cassandra_metrics_Table_MaxPartitionSize_Value
    # TYPE org_apache_cassandra_metrics_Table_MeanPartitionSize_Value untyped
    org_apache_cassandra_metrics_Table_MeanPartitionSize_Value
    # TYPE org_apache_cassandra_metrics_Table_MemtableColumnsCount_Value untyped
    org_apache_cassandra_metrics_Table_MemtableColumnsCount_Value
    # TYPE org_apache_cassandra_metrics_Table_MemtableLiveDataSize_Value untyped
    org_apache_cassandra_metrics_Table_MemtableLiveDataSize_Value
    # TYPE org_apache_cassandra_metrics_Table_MemtableOffHeapDataSize_Value untyped
    org_apache_cassandra_metrics_Table_MemtableOffHeapDataSize_Value
    # TYPE org_apache_cassandra_metrics_Table_MemtableOffHeapSize_Value untyped
    org_apache_cassandra_metrics_Table_MemtableOffHeapSize_Value
    # TYPE org_apache_cassandra_metrics_Table_MemtableOnHeapDataSize_Value untyped
    org_apache_cassandra_metrics_Table_MemtableOnHeapDataSize_Value
    # TYPE org_apache_cassandra_metrics_Table_MemtableOnHeapSize_Value untyped
    org_apache_cassandra_metrics_Table_MemtableOnHeapSize_Value
    # TYPE org_apache_cassandra_metrics_Table_MemtableSwitchCount_Count untyped
    org_apache_cassandra_metrics_Table_MemtableSwitchCount_Count
    # TYPE org_apache_cassandra_metrics_Table_MinPartitionSize_Value untyped
    org_apache_cassandra_metrics_Table_MinPartitionSize_Value
    # TYPE org_apache_cassandra_metrics_Table_MutatedAnticompactionGauge_Value untyped
    org_apache_cassandra_metrics_Table_MutatedAnticompactionGauge_Value
    # TYPE org_apache_cassandra_metrics_Table_OldVersionSSTableCount_Value untyped
    org_apache_cassandra_metrics_Table_OldVersionSSTableCount_Value
    # TYPE org_apache_cassandra_metrics_Table_PartitionsValidated_50thPercentile untyped
    org_apache_cassandra_metrics_Table_PartitionsValidated_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_PartitionsValidated_75thPercentile untyped
    org_apache_cassandra_metrics_Table_PartitionsValidated_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_PartitionsValidated_95thPercentile untyped
    org_apache_cassandra_metrics_Table_PartitionsValidated_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_PartitionsValidated_98thPercentile untyped
    org_apache_cassandra_metrics_Table_PartitionsValidated_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_PartitionsValidated_999thPercentile untyped
    org_apache_cassandra_metrics_Table_PartitionsValidated_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_PartitionsValidated_99thPercentile untyped
    org_apache_cassandra_metrics_Table_PartitionsValidated_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_PartitionsValidated_Count untyped
    org_apache_cassandra_metrics_Table_PartitionsValidated_Count
    # TYPE org_apache_cassandra_metrics_Table_PartitionsValidated_Max untyped
    org_apache_cassandra_metrics_Table_PartitionsValidated_Max
    # TYPE org_apache_cassandra_metrics_Table_PartitionsValidated_Mean untyped
    org_apache_cassandra_metrics_Table_PartitionsValidated_Mean
    # TYPE org_apache_cassandra_metrics_Table_PartitionsValidated_Min untyped
    org_apache_cassandra_metrics_Table_PartitionsValidated_Min
    # TYPE org_apache_cassandra_metrics_Table_PartitionsValidated_StdDev untyped
    org_apache_cassandra_metrics_Table_PartitionsValidated_StdDev
    # TYPE org_apache_cassandra_metrics_Table_PendingCompactions_Value untyped
    org_apache_cassandra_metrics_Table_PendingCompactions_Value
    # TYPE org_apache_cassandra_metrics_Table_PendingFlushes_Count untyped
    org_apache_cassandra_metrics_Table_PendingFlushes_Count
    # TYPE org_apache_cassandra_metrics_Table_PercentRepaired_Value untyped
    org_apache_cassandra_metrics_Table_PercentRepaired_Value
    # TYPE org_apache_cassandra_metrics_Table_RangeLatency_50thPercentile untyped
    org_apache_cassandra_metrics_Table_RangeLatency_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RangeLatency_75thPercentile untyped
    org_apache_cassandra_metrics_Table_RangeLatency_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RangeLatency_95thPercentile untyped
    org_apache_cassandra_metrics_Table_RangeLatency_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RangeLatency_98thPercentile untyped
    org_apache_cassandra_metrics_Table_RangeLatency_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RangeLatency_999thPercentile untyped
    org_apache_cassandra_metrics_Table_RangeLatency_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RangeLatency_99thPercentile untyped
    org_apache_cassandra_metrics_Table_RangeLatency_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RangeLatency_Count untyped
    org_apache_cassandra_metrics_Table_RangeLatency_Count
    # TYPE org_apache_cassandra_metrics_Table_RangeLatency_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_RangeLatency_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_RangeLatency_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_RangeLatency_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_RangeLatency_Max untyped
    org_apache_cassandra_metrics_Table_RangeLatency_Max
    # TYPE org_apache_cassandra_metrics_Table_RangeLatency_Mean untyped
    org_apache_cassandra_metrics_Table_RangeLatency_Mean
    # TYPE org_apache_cassandra_metrics_Table_RangeLatency_MeanRate untyped
    org_apache_cassandra_metrics_Table_RangeLatency_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_RangeLatency_Min untyped
    org_apache_cassandra_metrics_Table_RangeLatency_Min
    # TYPE org_apache_cassandra_metrics_Table_RangeLatency_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_RangeLatency_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_RangeLatency_StdDev untyped
    org_apache_cassandra_metrics_Table_RangeLatency_StdDev
    # TYPE org_apache_cassandra_metrics_Table_RangeTotalLatency_Count untyped
    org_apache_cassandra_metrics_Table_RangeTotalLatency_Count
    # TYPE org_apache_cassandra_metrics_Table_ReadLatency_50thPercentile untyped
    org_apache_cassandra_metrics_Table_ReadLatency_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ReadLatency_75thPercentile untyped
    org_apache_cassandra_metrics_Table_ReadLatency_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ReadLatency_95thPercentile untyped
    org_apache_cassandra_metrics_Table_ReadLatency_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ReadLatency_98thPercentile untyped
    org_apache_cassandra_metrics_Table_ReadLatency_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ReadLatency_999thPercentile untyped
    org_apache_cassandra_metrics_Table_ReadLatency_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ReadLatency_99thPercentile untyped
    org_apache_cassandra_metrics_Table_ReadLatency_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ReadLatency_Count untyped
    org_apache_cassandra_metrics_Table_ReadLatency_Count
    # TYPE org_apache_cassandra_metrics_Table_ReadLatency_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_ReadLatency_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ReadLatency_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_ReadLatency_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ReadLatency_Max untyped
    org_apache_cassandra_metrics_Table_ReadLatency_Max
    # TYPE org_apache_cassandra_metrics_Table_ReadLatency_Mean untyped
    org_apache_cassandra_metrics_Table_ReadLatency_Mean
    # TYPE org_apache_cassandra_metrics_Table_ReadLatency_MeanRate untyped
    org_apache_cassandra_metrics_Table_ReadLatency_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_ReadLatency_Min untyped
    org_apache_cassandra_metrics_Table_ReadLatency_Min
    # TYPE org_apache_cassandra_metrics_Table_ReadLatency_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_ReadLatency_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ReadLatency_StdDev untyped
    org_apache_cassandra_metrics_Table_ReadLatency_StdDev
    # TYPE org_apache_cassandra_metrics_Table_ReadRepairRequests_Count untyped
    org_apache_cassandra_metrics_Table_ReadRepairRequests_Count
    # TYPE org_apache_cassandra_metrics_Table_ReadRepairRequests_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_ReadRepairRequests_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ReadRepairRequests_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_ReadRepairRequests_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ReadRepairRequests_MeanRate untyped
    org_apache_cassandra_metrics_Table_ReadRepairRequests_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_ReadRepairRequests_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_ReadRepairRequests_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ReadTotalLatency_Count untyped
    org_apache_cassandra_metrics_Table_ReadTotalLatency_Count
    # TYPE org_apache_cassandra_metrics_Table_RecentBloomFilterFalsePositives_Value untyped
    org_apache_cassandra_metrics_Table_RecentBloomFilterFalsePositives_Value
    # TYPE org_apache_cassandra_metrics_Table_RecentBloomFilterFalseRatio_Value untyped
    org_apache_cassandra_metrics_Table_RecentBloomFilterFalseRatio_Value
    # TYPE org_apache_cassandra_metrics_Table_RepairJobsCompleted_Count untyped
    org_apache_cassandra_metrics_Table_RepairJobsCompleted_Count
    # TYPE org_apache_cassandra_metrics_Table_RepairJobsStarted_Count untyped
    org_apache_cassandra_metrics_Table_RepairJobsStarted_Count
    # TYPE org_apache_cassandra_metrics_Table_RepairSyncTime_50thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairSyncTime_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairSyncTime_75thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairSyncTime_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairSyncTime_95thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairSyncTime_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairSyncTime_98thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairSyncTime_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairSyncTime_999thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairSyncTime_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairSyncTime_99thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairSyncTime_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairSyncTime_Count untyped
    org_apache_cassandra_metrics_Table_RepairSyncTime_Count
    # TYPE org_apache_cassandra_metrics_Table_RepairSyncTime_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_RepairSyncTime_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_RepairSyncTime_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_RepairSyncTime_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_RepairSyncTime_Max untyped
    org_apache_cassandra_metrics_Table_RepairSyncTime_Max
    # TYPE org_apache_cassandra_metrics_Table_RepairSyncTime_MeanRate untyped
    org_apache_cassandra_metrics_Table_RepairSyncTime_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_RepairSyncTime_Min untyped
    org_apache_cassandra_metrics_Table_RepairSyncTime_Min
    # TYPE org_apache_cassandra_metrics_Table_RepairSyncTime_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_RepairSyncTime_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_RepairSyncTime_StdDev untyped
    org_apache_cassandra_metrics_Table_RepairSyncTime_StdDev
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesConfirmed_Count untyped
    org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesConfirmed_Count
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesConfirmed_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesConfirmed_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesConfirmed_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesConfirmed_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesConfirmed_MeanRate untyped
    org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesConfirmed_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesConfirmed_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesConfirmed_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesUnconfirmed_Count untyped
    org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesUnconfirmed_Count
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesUnconfirmed_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesUnconfirmed_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesUnconfirmed_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesUnconfirmed_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesUnconfirmed_MeanRate untyped
    org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesUnconfirmed_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesUnconfirmed_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_RepairedDataInconsistenciesUnconfirmed_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_50thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_75thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_95thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_98thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_999thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_99thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_Count untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_Count
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_Max untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_Max
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_Min untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_Min
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_StdDev untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadRows_StdDev
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_50thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_75thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_95thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_98thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_999thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_99thPercentile untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_Count untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_Count
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_Max untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_Max
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_MeanRate untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_Min untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_Min
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_StdDev untyped
    org_apache_cassandra_metrics_Table_RepairedDataTrackingOverreadTime_StdDev
    # TYPE org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRequests_Count untyped
    org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRequests_Count
    # TYPE org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRequests_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRequests_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRequests_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRequests_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRequests_MeanRate untyped
    org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRequests_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRequests_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRequests_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_50thPercentile untyped
    org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_75thPercentile untyped
    org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_95thPercentile untyped
    org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_98thPercentile untyped
    org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_999thPercentile untyped
    org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_99thPercentile untyped
    org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_Count untyped
    org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_Count
    # TYPE org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_Max untyped
    org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_Max
    # TYPE org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_Min untyped
    org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_Min
    # TYPE org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_StdDev untyped
    org_apache_cassandra_metrics_Table_ReplicaFilteringProtectionRowsCachedPerQuery_StdDev
    # TYPE org_apache_cassandra_metrics_Table_RowCacheHitOutOfRange_Count untyped
    org_apache_cassandra_metrics_Table_RowCacheHitOutOfRange_Count
    # TYPE org_apache_cassandra_metrics_Table_RowCacheHit_Count untyped
    org_apache_cassandra_metrics_Table_RowCacheHit_Count
    # TYPE org_apache_cassandra_metrics_Table_RowCacheMiss_Count untyped
    org_apache_cassandra_metrics_Table_RowCacheMiss_Count
    # TYPE org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_50thPercentile untyped
    org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_75thPercentile untyped
    org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_95thPercentile untyped
    org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_98thPercentile untyped
    org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_999thPercentile untyped
    org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_99thPercentile untyped
    org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_Count untyped
    org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_Count
    # TYPE org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_Max untyped
    org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_Max
    # TYPE org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_Mean untyped
    org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_Mean
    # TYPE org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_Min untyped
    org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_Min
    # TYPE org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_StdDev untyped
    org_apache_cassandra_metrics_Table_SSTablesPerReadHistogram_StdDev
    # TYPE org_apache_cassandra_metrics_Table_ShortReadProtectionRequests_Count untyped
    org_apache_cassandra_metrics_Table_ShortReadProtectionRequests_Count
    # TYPE org_apache_cassandra_metrics_Table_ShortReadProtectionRequests_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_ShortReadProtectionRequests_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ShortReadProtectionRequests_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_ShortReadProtectionRequests_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ShortReadProtectionRequests_MeanRate untyped
    org_apache_cassandra_metrics_Table_ShortReadProtectionRequests_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_ShortReadProtectionRequests_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_ShortReadProtectionRequests_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_SnapshotsSize_Value untyped
    org_apache_cassandra_metrics_Table_SnapshotsSize_Value
    # TYPE org_apache_cassandra_metrics_Table_SpeculativeFailedRetries_Count untyped
    org_apache_cassandra_metrics_Table_SpeculativeFailedRetries_Count
    # TYPE org_apache_cassandra_metrics_Table_SpeculativeInsufficientReplicas_Count untyped
    org_apache_cassandra_metrics_Table_SpeculativeInsufficientReplicas_Count
    # TYPE org_apache_cassandra_metrics_Table_SpeculativeRetries_Count untyped
    org_apache_cassandra_metrics_Table_SpeculativeRetries_Count
    # TYPE org_apache_cassandra_metrics_Table_SpeculativeSampleLatencyNanos_Value untyped
    org_apache_cassandra_metrics_Table_SpeculativeSampleLatencyNanos_Value
    # TYPE org_apache_cassandra_metrics_Table_TombstoneFailures_Count untyped
    org_apache_cassandra_metrics_Table_TombstoneFailures_Count
    # TYPE org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_50thPercentile untyped
    org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_75thPercentile untyped
    org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_95thPercentile untyped
    org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_98thPercentile untyped
    org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_999thPercentile untyped
    org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_99thPercentile untyped
    org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_Count untyped
    org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_Count
    # TYPE org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_Max untyped
    org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_Max
    # TYPE org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_Mean untyped
    org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_Mean
    # TYPE org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_Min untyped
    org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_Min
    # TYPE org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_StdDev untyped
    org_apache_cassandra_metrics_Table_TombstoneScannedHistogram_StdDev
    # TYPE org_apache_cassandra_metrics_Table_TombstoneWarnings_Count untyped
    org_apache_cassandra_metrics_Table_TombstoneWarnings_Count
    # TYPE org_apache_cassandra_metrics_Table_TotalDiskSpaceUsed_Count untyped
    org_apache_cassandra_metrics_Table_TotalDiskSpaceUsed_Count
    # TYPE org_apache_cassandra_metrics_Table_UnleveledSSTables_Value untyped
    org_apache_cassandra_metrics_Table_UnleveledSSTables_Value
    # TYPE org_apache_cassandra_metrics_Table_ValidationTime_50thPercentile untyped
    org_apache_cassandra_metrics_Table_ValidationTime_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ValidationTime_75thPercentile untyped
    org_apache_cassandra_metrics_Table_ValidationTime_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ValidationTime_95thPercentile untyped
    org_apache_cassandra_metrics_Table_ValidationTime_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ValidationTime_98thPercentile untyped
    org_apache_cassandra_metrics_Table_ValidationTime_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ValidationTime_999thPercentile untyped
    org_apache_cassandra_metrics_Table_ValidationTime_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ValidationTime_99thPercentile untyped
    org_apache_cassandra_metrics_Table_ValidationTime_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ValidationTime_Count untyped
    org_apache_cassandra_metrics_Table_ValidationTime_Count
    # TYPE org_apache_cassandra_metrics_Table_ValidationTime_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_ValidationTime_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ValidationTime_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_ValidationTime_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ValidationTime_Max untyped
    org_apache_cassandra_metrics_Table_ValidationTime_Max
    # TYPE org_apache_cassandra_metrics_Table_ValidationTime_Mean untyped
    org_apache_cassandra_metrics_Table_ValidationTime_Mean
    # TYPE org_apache_cassandra_metrics_Table_ValidationTime_MeanRate untyped
    org_apache_cassandra_metrics_Table_ValidationTime_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_ValidationTime_Min untyped
    org_apache_cassandra_metrics_Table_ValidationTime_Min
    # TYPE org_apache_cassandra_metrics_Table_ValidationTime_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_ValidationTime_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ValidationTime_StdDev untyped
    org_apache_cassandra_metrics_Table_ValidationTime_StdDev
    # TYPE org_apache_cassandra_metrics_Table_ViewLockAcquireTime_50thPercentile untyped
    org_apache_cassandra_metrics_Table_ViewLockAcquireTime_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ViewLockAcquireTime_75thPercentile untyped
    org_apache_cassandra_metrics_Table_ViewLockAcquireTime_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ViewLockAcquireTime_95thPercentile untyped
    org_apache_cassandra_metrics_Table_ViewLockAcquireTime_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ViewLockAcquireTime_98thPercentile untyped
    org_apache_cassandra_metrics_Table_ViewLockAcquireTime_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ViewLockAcquireTime_999thPercentile untyped
    org_apache_cassandra_metrics_Table_ViewLockAcquireTime_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ViewLockAcquireTime_99thPercentile untyped
    org_apache_cassandra_metrics_Table_ViewLockAcquireTime_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ViewLockAcquireTime_Count untyped
    org_apache_cassandra_metrics_Table_ViewLockAcquireTime_Count
    # TYPE org_apache_cassandra_metrics_Table_ViewLockAcquireTime_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_ViewLockAcquireTime_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ViewLockAcquireTime_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_ViewLockAcquireTime_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ViewLockAcquireTime_Max untyped
    org_apache_cassandra_metrics_Table_ViewLockAcquireTime_Max
    # TYPE org_apache_cassandra_metrics_Table_ViewLockAcquireTime_MeanRate untyped
    org_apache_cassandra_metrics_Table_ViewLockAcquireTime_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_ViewLockAcquireTime_Min untyped
    org_apache_cassandra_metrics_Table_ViewLockAcquireTime_Min
    # TYPE org_apache_cassandra_metrics_Table_ViewLockAcquireTime_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_ViewLockAcquireTime_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ViewLockAcquireTime_StdDev untyped
    org_apache_cassandra_metrics_Table_ViewLockAcquireTime_StdDev
    # TYPE org_apache_cassandra_metrics_Table_ViewReadTime_50thPercentile untyped
    org_apache_cassandra_metrics_Table_ViewReadTime_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ViewReadTime_75thPercentile untyped
    org_apache_cassandra_metrics_Table_ViewReadTime_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ViewReadTime_95thPercentile untyped
    org_apache_cassandra_metrics_Table_ViewReadTime_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ViewReadTime_98thPercentile untyped
    org_apache_cassandra_metrics_Table_ViewReadTime_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ViewReadTime_999thPercentile untyped
    org_apache_cassandra_metrics_Table_ViewReadTime_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ViewReadTime_99thPercentile untyped
    org_apache_cassandra_metrics_Table_ViewReadTime_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_ViewReadTime_Count untyped
    org_apache_cassandra_metrics_Table_ViewReadTime_Count
    # TYPE org_apache_cassandra_metrics_Table_ViewReadTime_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_ViewReadTime_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ViewReadTime_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_ViewReadTime_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ViewReadTime_Max untyped
    org_apache_cassandra_metrics_Table_ViewReadTime_Max
    # TYPE org_apache_cassandra_metrics_Table_ViewReadTime_MeanRate untyped
    org_apache_cassandra_metrics_Table_ViewReadTime_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_ViewReadTime_Min untyped
    org_apache_cassandra_metrics_Table_ViewReadTime_Min
    # TYPE org_apache_cassandra_metrics_Table_ViewReadTime_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_ViewReadTime_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_ViewReadTime_StdDev untyped
    org_apache_cassandra_metrics_Table_ViewReadTime_StdDev
    # TYPE org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_50thPercentile untyped
    org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_75thPercentile untyped
    org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_95thPercentile untyped
    org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_98thPercentile untyped
    org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_999thPercentile untyped
    org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_99thPercentile untyped
    org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_Count untyped
    org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_Count
    # TYPE org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_Max untyped
    org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_Max
    # TYPE org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_Min untyped
    org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_Min
    # TYPE org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_StdDev untyped
    org_apache_cassandra_metrics_Table_WaitingOnFreeMemtableSpace_StdDev
    # TYPE org_apache_cassandra_metrics_Table_WriteLatency_50thPercentile untyped
    org_apache_cassandra_metrics_Table_WriteLatency_50thPercentile
    # TYPE org_apache_cassandra_metrics_Table_WriteLatency_75thPercentile untyped
    org_apache_cassandra_metrics_Table_WriteLatency_75thPercentile
    # TYPE org_apache_cassandra_metrics_Table_WriteLatency_95thPercentile untyped
    org_apache_cassandra_metrics_Table_WriteLatency_95thPercentile
    # TYPE org_apache_cassandra_metrics_Table_WriteLatency_98thPercentile untyped
    org_apache_cassandra_metrics_Table_WriteLatency_98thPercentile
    # TYPE org_apache_cassandra_metrics_Table_WriteLatency_999thPercentile untyped
    org_apache_cassandra_metrics_Table_WriteLatency_999thPercentile
    # TYPE org_apache_cassandra_metrics_Table_WriteLatency_99thPercentile untyped
    org_apache_cassandra_metrics_Table_WriteLatency_99thPercentile
    # TYPE org_apache_cassandra_metrics_Table_WriteLatency_Count untyped
    org_apache_cassandra_metrics_Table_WriteLatency_Count
    # TYPE org_apache_cassandra_metrics_Table_WriteLatency_FifteenMinuteRate untyped
    org_apache_cassandra_metrics_Table_WriteLatency_FifteenMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_WriteLatency_FiveMinuteRate untyped
    org_apache_cassandra_metrics_Table_WriteLatency_FiveMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_WriteLatency_Max untyped
    org_apache_cassandra_metrics_Table_WriteLatency_Max
    # TYPE org_apache_cassandra_metrics_Table_WriteLatency_Mean untyped
    org_apache_cassandra_metrics_Table_WriteLatency_Mean
    # TYPE org_apache_cassandra_metrics_Table_WriteLatency_MeanRate untyped
    org_apache_cassandra_metrics_Table_WriteLatency_MeanRate
    # TYPE org_apache_cassandra_metrics_Table_WriteLatency_Min untyped
    org_apache_cassandra_metrics_Table_WriteLatency_Min
    # TYPE org_apache_cassandra_metrics_Table_WriteLatency_OneMinuteRate untyped
    org_apache_cassandra_metrics_Table_WriteLatency_OneMinuteRate
    # TYPE org_apache_cassandra_metrics_Table_WriteLatency_StdDev untyped
    org_apache_cassandra_metrics_Table_WriteLatency_StdDev
    # TYPE org_apache_cassandra_metrics_Table_WriteTotalLatency_Count untyped
    org_apache_cassandra_metrics_Table_WriteTotalLatency_Count
    # TYPE org_apache_cassandra_metrics_ThreadPools_ActiveTasks_Value untyped
    org_apache_cassandra_metrics_ThreadPools_ActiveTasks_Value
    # TYPE org_apache_cassandra_metrics_ThreadPools_CompletedTasks_Value untyped
    org_apache_cassandra_metrics_ThreadPools_CompletedTasks_Value
    # TYPE org_apache_cassandra_metrics_ThreadPools_CurrentlyBlockedTasks_Count untyped
    org_apache_cassandra_metrics_ThreadPools_CurrentlyBlockedTasks_Count
    # TYPE org_apache_cassandra_metrics_ThreadPools_MaxPoolSize_Value untyped
    org_apache_cassandra_metrics_ThreadPools_MaxPoolSize_Value
    # TYPE org_apache_cassandra_metrics_ThreadPools_MaxTasksQueued_Value untyped
    org_apache_cassandra_metrics_ThreadPools_MaxTasksQueued_Value
    # TYPE org_apache_cassandra_metrics_ThreadPools_PendingTasks_Value untyped
    org_apache_cassandra_metrics_ThreadPools_PendingTasks_Value
    # TYPE org_apache_cassandra_metrics_ThreadPools_TotalBlockedTasks_Count untyped
    org_apache_cassandra_metrics_ThreadPools_TotalBlockedTasks_Count
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
