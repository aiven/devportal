Aiven for Apache Kafka® metrics available via Prometheus
========================================================

The following list only contains the most common metrics available via Prometheus for an Aiven for Apache Kafka® service.

You can retrieve the complete list of available metrics for your specific service by requesting the Prometheus endpoint, substituting:

* the Aiven project certificate (``ca.pem``)
* the Prometheus credentials (``<PROMETHEUS_USER>:<PROMETHEUS_PASSWORD>``)
* the Aiven for Apache Kafka hostname (``<KAFKA_HOSTNAME>``)
* the Prometheus port (``<PROMETHEUS_PORT>``)

.. code-block:: bash

    curl --cacert ca.pem \
        --user '<PROMETHEUS_USER>:<PROMETHEUS_PASSWORD>' \
        'https://<KAFKA_HOSTNAME>:<PROMETHEUS_PORT>/metrics'

.. Tip::

    You can check how to use Prometheus with Aiven in the :doc:`dedicated document </docs/platform/howto/integrations/prometheus-metrics>`.

CPU utilization
---------------

* ``cpu_usage_guest``: CPU time spent running a virtual CPU for guest operating systems.
* ``cpu_usage_guest_nice``: The amount of time the CPU runs a virtual CPU for a guest operating system, which is low-priority and can be interrupted by other processes. This metric is measured in hundredths of a second.
* ``cpu_usage_idle``: Time the CPU spends doing nothing.
* ``cpu_usage_iowait``: Time waiting for I/O to complete.
* ``cpu_usage_irq``: Time servicing interrupts.
* ``cpu_usage_nice``: Time running user-niced processes.
* ``cpu_usage_softirq``: Time servicing softirqs.
* ``cpu_usage_steal``: Time spent in other operating systems when running in a virtualized environment.
* ``cpu_usage_system``: Time spent running system processes.
* ``cpu_usage_user``: Time spent running user processes.
* ``system_load1``: System load average for the last minute.
* ``system_load15``: System load average for the last 15 minutes.
* ``system_load5``: System load average for the last 5 minutes.
* ``system_n_cpus``: Number of CPU cores available.
* ``system_n_users``: Number of users logged in.
* ``system_uptime``: Time for which the system has been up and running.

Disk space utilization
----------------------

* ``disk_free``: Amount of free disk space.
* ``disk_inodes_free``: Number of free inodes.
* ``disk_inodes_total``: Total number of inodes.
* ``disk_inodes_used``: Number of used inodes.
* ``disk_total``: Total disk space.
* ``disk_used``: Amount of used disk space.
* ``disk_used_percent``: Percentage of disk space used.

Disk input and output
---------------------
Metrics such as diskio_io_time, diskio_iops_in_progress, etc., offer valuable insights into disk I/O operations. These metrics encompass read/write operations, the duration of these operations, bytes read/written, and more.


* ``diskio_io_time``
* ``diskio_iops_in_progress``
* ``diskio_merged_reads``
* ``diskio_merged_writes``
* ``diskio_read_bytes``
* ``diskio_read_time``
* ``diskio_reads``
* ``diskio_weighted_io_time``
* ``diskio_write_bytes``
* ``diskio_write_time``
* ``diskio_writes``

Garbage collector ``MXBean``
----------------------------
Metrics associated with the java_lang_GarbageCollector provide insights into the JVM's garbage collection process. These metrics encompass details such as the collection count, duration of collections, and more.

* ``java_lang_GarbageCollector_G1_Young_Generation_CollectionCount``: returns the total number of collections that have occurred
* ``java_lang_GarbageCollector_G1_Young_Generation_CollectionTime``: returns the approximate accumulated collection elapsed time in milliseconds
* ``java_lang_GarbageCollector_G1_Young_Generation_duration``

Memory usage
------------
Metrics starting with java_lang_Memory provide insights into the JVM's memory usage, such as committed memory, initial memory, max memory, used memory, etc.

* ``java_lang_Memory_committed``: returns the amount of memory in bytes that is committed for the Java virtual machine to use
* ``java_lang_Memory_init``: returns the amount of memory in bytes that the Java virtual machine initially requests from the operating system for memory management
* ``java_lang_Memory_max``: returns the maximum amount of memory in bytes that can be used for memory management
* ``java_lang_Memory_used``: returns the amount of used memory in bytes
* ``java_lang_Memory_ObjectPendingFinalizationCount``

Apache Kafka Connect
--------------------

The Apache Kafka Connect metrics list is available in the :doc:`dedicated page <../kafka-connect/reference/connect-metrics-prometheus>`.

Apache Kafka broker
-------------------

The descriptions for the below metrics are available in the `Monitoring section of the Apache Kafka documentation <https://kafka.apache.org/documentation/#monitoring>`_.

.. Note::

    The metrics with a ``_Count`` suffix are cumulative counters for the given metric, e.g. ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_Count``.

    Note that a metric like ``kafka_server_BrokerTopicMetrics_MessagesInPerSec_Count`` is a cumulative count of incoming messages despite the ``PerSec`` suffix in the metric name.

    To see the rate of change of these ``_Count`` metrics, you can apply a function such as the ``rate()`` function in PromQL.

Apache Kafka controller
'''''''''''''''''''''''

.. Note::
    These metrics with ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_XthPercentile`` (where X can be 50th, 75th, 95th, etc.) represent the time taken for leader elections to complete at various percentiles. It helps in understanding the distribution of leader election times.

    Metrics below with ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_`` (FifteenMinuteRate, FiveMinuteRate, etc.) represent the rate of leader elections over different time intervals.

    Metrics below with ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_`` (Max/Mean/Min/StdDev) provide statistical measures about the leader election times.

    Metrics below with ``kafka_controller_KafkaController_Metrics`` provide insights into the state of the Kafka controller, like the number of active brokers, offline partitions, replicas to delete, etc.

* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_50thPercentile``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_75thPercentile``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_95thPercentile``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_98thPercentile``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_999thPercentile``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_99thPercentile``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_Count``: The total number of leader elections.
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_FifteenMinuteRate``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_FiveMinuteRate``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_Max``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_Mean``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_MeanRate``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_Min``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_OneMinuteRate``
* ``kafka_controller_ControllerStats_LeaderElectionRateAndTimeMs_StdDev``
* ``kafka_controller_ControllerStats_UncleanLeaderElectionsPerSec_Count``: Number of times an unclean leader election occurs. Unclean leader elections can lead to data loss.
* ``kafka_controller_KafkaController_ActiveBrokerCount_Value``
* ``kafka_controller_KafkaController_ActiveControllerCount_Value``
* ``kafka_controller_KafkaController_FencedBrokerCount_Value``
* ``kafka_controller_KafkaController_OfflinePartitionsCount_Value``
* ``kafka_controller_KafkaController_PreferredReplicaImbalanceCount_Value``
* ``kafka_controller_KafkaController_ReplicasIneligibleToDeleteCount_Value``
* ``kafka_controller_KafkaController_ReplicasToDeleteCount_Value``
* ``kafka_controller_KafkaController_TopicsIneligibleToDeleteCount_Value``
* ``kafka_controller_KafkaController_TopicsToDeleteCount_Value``

``Jolokia`` collector collect time
''''''''''''''''''''''''''''''''''

* ``kafka_jolokia_collector_collect_time``: Represents the time taken by the Jolokia collector to collect metrics. Jolokia is a JMX-HTTP bridge, giving an alternative to native JMX access.


Apache Kafka log
''''''''''''''''

.. Note::

    Metrics like ``kafka_log_LogCleaner_cleaner_recopy_percent_Value`` and ``kafka_log_LogCleanerManager_time_since_last_run_ms_Value`` provide insights into the log cleaner's operation, which helps in compacting the Kafka logs.
    
    ``Log Flush Rate Metrics`` give insights into the log flush operations. Flushing ensures that data is written from memory to disk. Metrics like kafka_log_LogFlushStats_LogFlushRateAndTimeMs_XthPercentile provide the time taken to flush logs at various percentiles.

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

.. Note::

    Metrics below like ``kafka_network_RequestMetrics_RequestsPerSec_Count`` and ``kafka_network_RequestMetrics_TotalTimeMs_Mean`` provide insights into the network requests made to the Kafka brokers.

* ``kafka_network_RequestChannel_RequestQueueSize_Value``
* ``kafka_network_RequestChannel_ResponseQueueSize_Value``
* ``kafka_network_RequestMetrics_RequestsPerSec_Count``
* ``kafka_network_RequestMetrics_TotalTimeMs_95thPercentile``
* ``kafka_network_RequestMetrics_TotalTimeMs_Count``
* ``kafka_network_RequestMetrics_TotalTimeMs_Mean``
* ``kafka_network_SocketServer_NetworkProcessorAvgIdlePercent_Value``

Apache Kafka server
'''''''''''''''''''

.. Note::

    The metrics below like ``BrokerTopicMetrics`` provide insights into various operations related to topics, like bytes in/out, failed fetch/produce requests, etc.

    Metrics ``ReplicaManager`` like ``kafka_server_ReplicaManager_LeaderCount_Value`` provide insights into the state of replicas in the Kafka cluster.

    If you do not specify the ``topic`` tag, it displays the combined rate for all topics as well as the rate for each individual topic. To view rates for specific topics, use the ``topic`` tag. To exclude the combined rate for all topics and only list metrics for individual topics, filter with ``topic!=""``

* ``kafka_server_BrokerTopicMetrics_BytesInPerSec_Count``: Byte in (from the clients) rate per topic. Omitting 'topic=(...)' will yield the all-topic rate.
* ``kafka_server_BrokerTopicMetrics_BytesOutPerSec_Count``: Byte out (to the clients) rate per topic. Omitting 'topic=(...)' will yield the all-topic rate.
* ``kafka_server_BrokerTopicMetrics_BytesRejectedPerSec_Count``: Rejected byte rate per topic due to the record batch size being greater than max.message.bytes configuration. Omitting 'topic=(...)' will yield the all-topic rate.
* ``kafka_server_BrokerTopicMetrics_FailedFetchRequestsPerSec_Count``: Failed Fetch request (from clients or followers) rate per topic. Omitting 'topic=(...)' will yield the all-topic rate.
* ``kafka_server_BrokerTopicMetrics_FailedProduceRequestsPerSec_Count``: Failed Produce request rate per topic. Omitting 'topic=(...)' will yield the all-topic rate.
* ``kafka_server_BrokerTopicMetrics_FetchMessageConversionsPerSec_Count``: Message format conversion rate, for Produce or Fetch requests, per topic. Omitting 'topic=(...)' will yield the all-topic rate.
* ``kafka_server_BrokerTopicMetrics_MessagesInPerSec_Count``: Incoming message rate per topic. Omitting 'topic=(...)' will yield the all-topic rate.
* ``kafka_server_BrokerTopicMetrics_ProduceMessageConversionsPerSec_Count``: Message format conversion rate, for Produce or Fetch requests, per topic. Omitting 'topic=(...)' will yield the all-topic rate.
* ``kafka_server_BrokerTopicMetrics_ReassignmentBytesInPerSec_Count``: Incoming byte rate of reassignment traffic
* ``kafka_server_BrokerTopicMetrics_ReassignmentBytesOutPerSec_Count``: Outgoing byte rate of reassignment traffic
* ``kafka_server_BrokerTopicMetrics_ReplicationBytesInPerSec_Count``: Byte in (from the other brokers) rate per topic. Omitting 'topic=(...)' will yield the all-topic rate.
* ``kafka_server_BrokerTopicMetrics_ReplicationBytesOutPerSec_Count``: Byte out (to the other brokers) rate per topic. Omitting 'topic=(...)' will yield the all-topic rate.
* ``kafka_server_BrokerTopicMetrics_TotalFetchRequestsPerSec_Count``: Fetch request (from clients or followers) rate per topic. Omitting 'topic=(...)' will yield the all-topic rate.
* ``kafka_server_BrokerTopicMetrics_TotalProduceRequestsPerSec_Count``: Produce request rate per topic. Omitting 'topic=(...)' will yield the all-topic rate.
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
* ``kafka_server_group_coordinator_metrics_group_completed_rebalance_count``
* ``kafka_server_group_coordinator_metrics_group_completed_rebalance_rate``
* ``kafka_server_group_coordinator_metrics_offset_commit_count``
* ``kafka_server_group_coordinator_metrics_offset_commit_rate``
* ``kafka_server_group_coordinator_metrics_offset_deletion_count``
* ``kafka_server_group_coordinator_metrics_offset_deletion_rate``
* ``kafka_server_group_coordinator_metrics_offset_expiration_count``
* ``kafka_server_group_coordinator_metrics_offset_expiration_rate``

Kernel
''''''

.. Note::

    Metrics below, like ``kernel_boot_time``, ``kernel_context_switches``, etc., provide insights into the underlying system's kernel operations.

* ``kernel_boot_time``
* ``kernel_context_switches``
* ``kernel_entropy_avail``
* ``kernel_interrupts``
* ``kernel_processes_forked``

Generic memory
''''''''''''''

.. Note::

    Metrics like ``mem_active``, ``mem_available``, etc., provide insights into the system's memory usage.

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

.. Note::

    Metrics like ``net_bytes_recv``, ``net_packets_sent``, etc., provide insights into the system's network operations.

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

.. Note::

    Metrics like ``processes_running``, ``processes_zombies``, etc., provide insights into the system's process management.

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

.. Note::

    Metrics like ``swap_free``, ``swap_used``, etc., provide insights into the system's swap memory usage.

* ``swap_free``
* ``swap_in``
* ``swap_out``
* ``swap_total``
* ``swap_used``
* ``swap_used_percent``
