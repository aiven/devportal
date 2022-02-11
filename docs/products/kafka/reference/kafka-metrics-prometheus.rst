List of metrics available via Prometheus integration
==================================================================

Below you can find a summary of every metric available via Prometheus for an Aiven for Apache Kafka service.

CPU utilization
---------------

* ``cpu_usage_guest``
* ``cpu_usage_guest_nice``
* ``cpu_usage_idle``
* ``cpu_usage_iowait``
* ``cpu_usage_irq``
* ``cpu_usage_nice``
* ``cpu_usage_softirq``
* ``cpu_usage_steal``
* ``cpu_usage_system``
* ``cpu_usage_user``
* ``system_load1``
* ``system_load15``
* ``system_load5``
* ``system_n_cpus``
* ``system_n_users``
* ``system_uptime``

Disk space utilization
----------------------

* ``disk_free``
* ``disk_inodes_free``
* ``disk_inodes_total``
* ``disk_inodes_used``
* ``disk_total``
* ``disk_used``
* ``disk_used_percent``

Disk input and output
---------------------

* ``diskio_iops_in_progress``
* ``diskio_io_time``
* ``diskio_read_bytes``
* ``diskio_reads``
* ``diskio_read_time``
* ``diskio_weighted_io_time``
* ``diskio_write_bytes``
* ``diskio_writes``
* ``diskio_write_time``

Garbage collector MXBean
------------------------

* ``java_lang_GarbageCollector_G1_Young_Generation_CollectionCount``: returns the total number of collections that have occurred
* ``java_lang_GarbageCollector_G1_Young_Generation_CollectionTime``: returns the approximate accumulated collection elapsed time in milliseconds
* ``java_lang_GarbageCollector_G1_Young_Generation_duration``

Memory usage
------------

* ``java_lang_Memory_committed``: returns the amount of memory in bytes that is committed for the Java virtual machine to use
* ``java_lang_Memory_init``: returns the amount of memory in bytes that the Java virtual machine initially requests from the operating system for memory management
* ``java_lang_Memory_max``: returns the maximum amount of memory in bytes that can be used for memory management 
* ``java_lang_Memory_used``: returns the amount of used memory in bytes
* ``java_lang_Memory_ObjectPendingFinalizationCount``

Apache Kafka Connect
--------------------

The list of Apache Kafka Connect metrics is available in the :doc:`dedicated page <../kafka-connect/reference/connect-metrics-prometheus>`.

Apache Kafka broker
-------------------

The descriptions for the below metrics are available in the `Monitoring section of the Apache Kafka documentation <http://kafka.apache.org/documentation/#monitoring>`_. 

.. Note:: 

    The metrics with a ``_Count`` suffix are cumulative counters for the given metric.
    
    E.g. ``kafka_server_BrokerTopicMetrics_MessagesInPerSec_Count`` is a cumulative count of incoming messages despite the ``PerSec`` suffix in the metric name. To see the rate of change of these ``_Count`` metrics, a function can be applied e.g. the ``rate()`` function in PromQL.

Apache Kafka controller
'''''''''''''''''''''''

* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_50thPercentile``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_75thPercentile``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_95thPercentile``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_98thPercentile``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_999thPercentile``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_99thPercentile``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_Count``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_FifteenMinuteRate``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_FiveMinuteRate``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_Max``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_Mean``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_MeanRate``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_Min``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_OneMinuteRate``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_StdDev``
* ``kafka_controller_ControllerStats_UncleanLeaderElectionsPerSec_Count``
* ``kafka_controller_KafkaController_ActiveControllerCount_Value``
* ``kafka_controller_KafkaController_OfflinePartitionsCount_Value``

Jolokia collector collect time
''''''''''''''''''''''''''''''

* ``kafka_jolokia_collector_collect_time``

Apache Kafka log 
''''''''''''''''

* ``kafka_log_LogCleaner_cleaner_recopy_percent_Value``
* ``kafka_log_LogCleanerManager_time_since_last_run_ms_Value``
* ``kafka_log_LogCleaner_max_clean_time_secs_Value``
* ``kafka_log_LogFlushStats_LogFlushRateAndTimeMs_50thPercentile``
* ``kafka_log_LogFlushStats_LogFlushRateAndTimeMs_75thPercentile``
* ``kafka_log_LogFlushStats_LogFlushRateAndTimeMs_95thPercentile``
* ``kafka_log_LogFlushStats_LogFlushRateAndTimeMs_98thPercentile``
* ``kafka_log_LogFlushStats_LogFlushRateAndTimeMs_999thPercentile``
* ``kafka_log_LogFlushStats_LogFlushRateAndTimeMs_99thPercentile``
* ``kafka_log_LogFlushStats_LogFlushRateAndTimeMs_Count``
* ``kafka_log_LogFlushStats_LogFlushRateAndTimeMs_FifteenMinuteRate``
* ``kafka_log_LogFlushStats_LogFlushRateAndTimeMs_FiveMinuteRate``
* ``kafka_log_LogFlushStats_LogFlushRateAndTimeMs_Max``
* ``kafka_log_LogFlushStats_LogFlushRateAndTimeMs_Mean``
* ``kafka_log_LogFlushStats_LogFlushRateAndTimeMs_MeanRate``
* ``kafka_log_LogFlushStats_LogFlushRateAndTimeMs_Min``
* ``kafka_log_LogFlushStats_LogFlushRateAndTimeMs_OneMinuteRate``
* ``kafka_log_LogFlushStats_LogFlushRateAndTimeMs_StdDev``
* ``kafka_log_Log_LogEndOffset_Value``
* ``kafka_log_Log_LogStartOffset_Value``
* ``kafka_log_Log_Size_Value``

Apache Kafka network
''''''''''''''''''''

* ``kafka_network_RequestMetrics_TotalTimeMs_95thPercentile``
* ``kafka_network_RequestMetrics_TotalTimeMs_Count``
* ``kafka_network_RequestMetrics_TotalTimeMs_Mean``
* ``kafka_network_SocketServer_NetworkProcessorAvgIdlePercent_Value``

Apache Kafka server
'''''''''''''''''''

* ``kafka_server_BrokerTopicMetrics_BytesInPerSec_Count``
* ``kafka_server_BrokerTopicMetrics_BytesOutPerSec_Count``
* ``kafka_server_BrokerTopicMetrics_BytesRejectedPerSec_Count``
* ``kafka_server_BrokerTopicMetrics_FailedFetchRequestsPerSec_Count``
* ``kafka_server_BrokerTopicMetrics_FailedProduceRequestsPerSec_Count``
* ``kafka_server_BrokerTopicMetrics_FetchMessageConversionsPerSec_Count``
* ``kafka_server_BrokerTopicMetrics_MessagesInPerSec_Count``
* ``kafka_server_BrokerTopicMetrics_TotalFetchRequestsPerSec_Count``
* ``kafka_server_BrokerTopicMetrics_TotalProduceRequestsPerSec_Count``
* ``kafka_server_DelayedOperationPurgatory_NumDelayedOperations_Value``
* ``kafka_server_DelayedOperationPurgatory_PurgatorySize_Value``
* ``kafka_server_KafkaRequestHandlerPool_RequestHandlerAvgIdlePercent_OneMinuteRate``
* ``kafka_server_KafkaServer_BrokerState_Value``
* ``kafka_server_ReplicaManager_IsrExpandsPerSec_Count``
* ``kafka_server_ReplicaManager_IsrShrinksPerSec_Count``
* ``kafka_server_ReplicaManager_LeaderCount_Value``
* ``kafka_server_ReplicaManager_PartitionCount_Value``
* ``kafka_server_ReplicaManager_UnderMinIsrPartitionCount_Value``
* ``kafka_server_ReplicaManager_UnderReplicatedPartitions_Value``

Kernel
''''''

* ``kernel_boot_time``
* ``kernel_context_switches``
* ``kernel_entropy_avail``
* ``kernel_interrupts``
* ``kernel_processes_forked``

Generic memory
''''''''''''''

* ``mem_active``
* ``mem_available``
* ``mem_available_percent``
* ``mem_buffered``
* ``mem_cached``
* ``mem_commit_limit``
* ``mem_committed_as``
* ``mem_dirty``
* ``mem_free``
* ``mem_high_free``
* ``mem_high_total``
* ``mem_huge_pages_free``
* ``mem_huge_page_size``
* ``mem_huge_pages_total``
* ``mem_inactive``
* ``mem_low_free``
* ``mem_low_total``
* ``mem_mapped``
* ``mem_page_tables``
* ``mem_shared``
* ``mem_slab``
* ``mem_swap_cached``
* ``mem_swap_free``
* ``mem_swap_total``
* ``mem_total``
* ``mem_used``
* ``mem_used_percent``
* ``mem_vmalloc_chunk``
* ``mem_vmalloc_total``
* ``mem_vmalloc_used``
* ``mem_wired``
* ``mem_write_back``
* ``mem_write_back_tmp``

Network
'''''''

* ``net_bytes_recv``
* ``net_bytes_sent``
* ``net_drop_in``
* ``net_drop_out``
* ``net_err_in``
* ``net_err_out``
* ``net_icmp_inaddrmaskreps``
* ``net_icmp_inaddrmasks``
* ``net_icmp_incsumerrors``
* ``net_icmp_indestunreachs``
* ``net_icmp_inechoreps``
* ``net_icmp_inechos``
* ``net_icmp_inerrors``
* ``net_icmp_inmsgs``
* ``net_icmp_inparmprobs``
* ``net_icmp_inredirects``
* ``net_icmp_insrcquenchs``
* ``net_icmp_intimeexcds``
* ``net_icmp_intimestampreps``
* ``net_icmp_intimestamps``
* ``net_icmpmsg_intype3``
* ``net_icmpmsg_intype8``
* ``net_icmpmsg_outtype0``
* ``net_icmpmsg_outtype3``
* ``net_icmp_outaddrmaskreps``
* ``net_icmp_outaddrmasks``
* ``net_icmp_outdestunreachs``
* ``net_icmp_outechoreps``
* ``net_icmp_outechos``
* ``net_icmp_outerrors``
* ``net_icmp_outmsgs``
* ``net_icmp_outparmprobs``
* ``net_icmp_outredirects``
* ``net_icmp_outsrcquenchs``
* ``net_icmp_outtimeexcds``
* ``net_icmp_outtimestampreps``
* ``net_icmp_outtimestamps``
* ``net_ip_defaultttl``
* ``net_ip_forwarding``
* ``net_ip_forwdatagrams``
* ``net_ip_fragcreates``
* ``net_ip_fragfails``
* ``net_ip_fragoks``
* ``net_ip_inaddrerrors``
* ``net_ip_indelivers``
* ``net_ip_indiscards``
* ``net_ip_inhdrerrors``
* ``net_ip_inreceives``
* ``net_ip_inunknownprotos``
* ``net_ip_outdiscards``
* ``net_ip_outnoroutes``
* ``net_ip_outrequests``
* ``net_ip_reasmfails``
* ``net_ip_reasmoks``
* ``net_ip_reasmreqds``
* ``net_ip_reasmtimeout``
* ``net_packets_recv``
* ``net_packets_sent``
* ``netstat_tcp_close``
* ``netstat_tcp_close_wait``
* ``netstat_tcp_closing``
* ``netstat_tcp_established``
* ``netstat_tcp_fin_wait1``
* ``netstat_tcp_fin_wait2``
* ``netstat_tcp_last_ack``
* ``netstat_tcp_listen``
* ``netstat_tcp_none``
* ``netstat_tcp_syn_recv``
* ``netstat_tcp_syn_sent``
* ``netstat_tcp_time_wait``
* ``netstat_udp_socket``
* ``net_tcp_activeopens``
* ``net_tcp_attemptfails``
* ``net_tcp_currestab``
* ``net_tcp_estabresets``
* ``net_tcp_incsumerrors``
* ``net_tcp_inerrs``
* ``net_tcp_insegs``
* ``net_tcp_maxconn``
* ``net_tcp_outrsts``
* ``net_tcp_outsegs``
* ``net_tcp_passiveopens``
* ``net_tcp_retranssegs``
* ``net_tcp_rtoalgorithm``
* ``net_tcp_rtomax``
* ``net_tcp_rtomin``
* ``net_udp_ignoredmulti``
* ``net_udp_incsumerrors``
* ``net_udp_indatagrams``
* ``net_udp_inerrors``
* ``net_udplite_ignoredmulti``
* ``net_udplite_incsumerrors``
* ``net_udplite_indatagrams``
* ``net_udplite_inerrors``
* ``net_udplite_noports``
* ``net_udplite_outdatagrams``
* ``net_udplite_rcvbuferrors``
* ``net_udplite_sndbuferrors``
* ``net_udp_noports``
* ``net_udp_outdatagrams``
* ``net_udp_rcvbuferrors``
* ``net_udp_sndbuferrors``

Processes
'''''''''

* ``processes_blocked``
* ``processes_dead``
* ``processes_idle``
* ``processes_paging``
* ``processes_running``
* ``processes_sleeping``
* ``processes_stopped``
* ``processes_total``
* ``processes_total_threads``
* ``processes_unknown``
* ``processes_zombies``

Swap usage
''''''''''

* ``swap_free``
* ``swap_in``
* ``swap_out``
* ``swap_total``
* ``swap_used``
* ``swap_used_percent``