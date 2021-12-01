
``custom_domain``  *['string', 'null']*
  - **Custom domain** Serve the web frontend using a custom CNAME pointing to the Aiven DNS name



``ip_filter``  *array*
  - **IP filter** Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'



``static_ips``  *boolean*
  - **Static IP addresses** Use static public IP addresses



``private_access``  *object*
  - **Allow access to selected service ports from private networks** 

  ``prometheus``  *boolean*
    - **Allow clients to connect to prometheus with a DNS name that always resolves to the service's private IP addresses. Only available in certain network locations** None



``public_access``  *object*
  - **Allow access to selected service ports from the public Internet** 

  ``kafka``  *boolean*
    - **Allow clients to connect to kafka from the public internet for service nodes that are in a project VPC or another type of private network** None

  ``kafka_connect``  *boolean*
    - **Allow clients to connect to kafka_connect from the public internet for service nodes that are in a project VPC or another type of private network** None

  ``kafka_rest``  *boolean*
    - **Allow clients to connect to kafka_rest from the public internet for service nodes that are in a project VPC or another type of private network** None

  ``prometheus``  *boolean*
    - **Allow clients to connect to prometheus from the public internet for service nodes that are in a project VPC or another type of private network** None

  ``schema_registry``  *boolean*
    - **Allow clients to connect to schema_registry from the public internet for service nodes that are in a project VPC or another type of private network** None



``privatelink_access``  *object*
  - **Allow access to selected service components through Privatelink** 

  ``kafka``  *boolean*
    - **Enable kafka** None

  ``kafka_connect``  *boolean*
    - **Enable kafka_connect** None

  ``kafka_rest``  *boolean*
    - **Enable kafka_rest** None

  ``schema_registry``  *boolean*
    - **Enable schema_registry** None



``kafka``  *object*
  - **Kafka broker configuration values** 

  ``compression_type``  *string*
    - **compression.type** Specify the final compression type for a given topic. This configuration accepts the standard compression codecs ('gzip', 'snappy', 'lz4', 'zstd'). It additionally accepts 'uncompressed' which is equivalent to no compression; and 'producer' which means retain the original compression codec set by the producer.

  ``group_initial_rebalance_delay_ms``  *integer*
    - **group.initial.rebalance.delay.ms** The amount of time, in milliseconds, the group coordinator will wait for more consumers to join a new group before performing the first rebalance. A longer delay means potentially fewer rebalances, but increases the time until processing begins. The default value for this is 3 seconds. During development and testing it might be desirable to set this to 0 in order to not delay test execution time.

  ``group_min_session_timeout_ms``  *integer*
    - **group.min.session.timeout.ms** The minimum allowed session timeout for registered consumers. Longer timeouts give consumers more time to process messages in between heartbeats at the cost of a longer time to detect failures.

  ``group_max_session_timeout_ms``  *integer*
    - **group.max.session.timeout.ms** The maximum allowed session timeout for registered consumers. Longer timeouts give consumers more time to process messages in between heartbeats at the cost of a longer time to detect failures.

  ``connections_max_idle_ms``  *integer*
    - **connections.max.idle.ms** Idle connections timeout: the server socket processor threads close the connections that idle for longer than this.

  ``max_incremental_fetch_session_cache_slots``  *integer*
    - **max.incremental.fetch.session.cache.slots** The maximum number of incremental fetch sessions that the broker will maintain.

  ``message_max_bytes``  *integer*
    - **message.max.bytes** The maximum size of message that the server can receive.

  ``offsets_retention_minutes``  *integer*
    - **offsets.retention.minutes** Log retention window in minutes for offsets topic

  ``log_cleaner_delete_retention_ms``  *integer*
    - **log.cleaner.delete.retention.ms** How long are delete records retained?

  ``log_cleaner_min_cleanable_ratio``  *number*
    - **log.cleaner.min.cleanable.ratio** Controls log compactor frequency. Larger value means more frequent compactions but also more space wasted for logs. Consider setting log.cleaner.max.compaction.lag.ms to enforce compactions sooner, instead of setting a very high value for this option.

  ``log_cleaner_max_compaction_lag_ms``  *integer*
    - **log.cleaner.max.compaction.lag.ms** The maximum amount of time message will remain uncompacted. Only applicable for logs that are being compacted

  ``log_cleaner_min_compaction_lag_ms``  *integer*
    - **log.cleaner.min.compaction.lag.ms** The minimum time a message will remain uncompacted in the log. Only applicable for logs that are being compacted.

  ``log_cleanup_policy``  *string*
    - **log.cleanup.policy** The default cleanup policy for segments beyond the retention window

  ``log_flush_interval_messages``  *integer*
    - **log.flush.interval.messages** The number of messages accumulated on a log partition before messages are flushed to disk

  ``log_flush_interval_ms``  *integer*
    - **log.flush.interval.ms** The maximum time in ms that a message in any topic is kept in memory before flushed to disk. If not set, the value in log.flush.scheduler.interval.ms is used

  ``log_index_interval_bytes``  *integer*
    - **log.index.interval.bytes** The interval with which Kafka adds an entry to the offset index

  ``log_index_size_max_bytes``  *integer*
    - **log.index.size.max.bytes** The maximum size in bytes of the offset index

  ``log_message_downconversion_enable``  *boolean*
    - **log.message.downconversion.enable** This configuration controls whether down-conversion of message formats is enabled to satisfy consume requests. 

  ``log_message_timestamp_type``  *string*
    - **log.message.timestamp.type** Define whether the timestamp in the message is message create time or log append time.

  ``log_message_timestamp_difference_max_ms``  *integer*
    - **log.message.timestamp.difference.max.ms** The maximum difference allowed between the timestamp when a broker receives a message and the timestamp specified in the message

  ``log_preallocate``  *boolean*
    - **log.preallocate** Should pre allocate file when create new segment?

  ``log_retention_bytes``  *integer*
    - **log.retention.bytes** The maximum size of the log before deleting messages

  ``log_retention_hours``  *integer*
    - **log.retention.hours** The number of hours to keep a log file before deleting it

  ``log_retention_ms``  *integer*
    - **log.retention.ms** The number of milliseconds to keep a log file before deleting it (in milliseconds), If not set, the value in log.retention.minutes is used. If set to -1, no time limit is applied.

  ``log_roll_jitter_ms``  *integer*
    - **log.roll.jitter.ms** The maximum jitter to subtract from logRollTimeMillis (in milliseconds). If not set, the value in log.roll.jitter.hours is used

  ``log_roll_ms``  *integer*
    - **log.roll.ms** The maximum time before a new log segment is rolled out (in milliseconds).

  ``log_segment_bytes``  *integer*
    - **log.segment.bytes** The maximum size of a single log file

  ``log_segment_delete_delay_ms``  *integer*
    - **log.segment.delete.delay.ms** The amount of time to wait before deleting a file from the filesystem

  ``auto_create_topics_enable``  *boolean*
    - **auto.create.topics.enable** Enable auto creation of topics

  ``min_insync_replicas``  *integer*
    - **min.insync.replicas** When a producer sets acks to 'all' (or '-1'), min.insync.replicas specifies the minimum number of replicas that must acknowledge a write for the write to be considered successful.

  ``num_partitions``  *integer*
    - **num.partitions** Number of partitions for autocreated topics

  ``default_replication_factor``  *integer*
    - **default.replication.factor** Replication factor for autocreated topics

  ``replica_fetch_max_bytes``  *integer*
    - **replica.fetch.max.bytes** The number of bytes of messages to attempt to fetch for each partition (defaults to 1048576). This is not an absolute maximum, if the first record batch in the first non-empty partition of the fetch is larger than this value, the record batch will still be returned to ensure that progress can be made.

  ``replica_fetch_response_max_bytes``  *integer*
    - **replica.fetch.response.max.bytes** Maximum bytes expected for the entire fetch response (defaults to 10485760). Records are fetched in batches, and if the first record batch in the first non-empty partition of the fetch is larger than this value, the record batch will still be returned to ensure that progress can be made. As such, this is not an absolute maximum.

  ``max_connections_per_ip``  *integer*
    - **max.connections.per.ip** The maximum number of connections allowed from each ip address (defaults to 2147483647).

  ``producer_purgatory_purge_interval_requests``  *integer*
    - **producer.purgatory.purge.interval.requests** The purge interval (in number of requests) of the producer request purgatory(defaults to 1000).

  ``socket_request_max_bytes``  *integer*
    - **socket.request.max.bytes** The maximum number of bytes in a socket request (defaults to 104857600).

  ``transaction_state_log_segment_bytes``  *integer*
    - **transaction.state.log.segment.bytes** The transaction topic segment bytes should be kept relatively small in order to facilitate faster log compaction and cache loads (defaults to 104857600 (100 mebibytes)).

  ``transaction_remove_expired_transaction_cleanup_interval_ms``  *integer*
    - **transaction.remove.expired.transaction.cleanup.interval.ms** The interval at which to remove transactions that have expired due to transactional.id.expiration.ms passing (defaults to 3600000 (1 hour)).



``kafka_authentication_methods``  *object*
  - **Kafka authentication methods** 

  ``certificate``  *boolean*
    - **Enable certificate/SSL authentication** None

  ``sasl``  *boolean*
    - **Enable SASL authentication** None



``kafka_connect``  *boolean*
  - **Enable Kafka Connect service** 



``kafka_connect_config``  *object*
  - **Kafka Connect configuration values** 

  ``connector_client_config_override_policy``  *string*
    - **Client config override policy** Defines what client configurations can be overridden by the connector. Default is None

  ``consumer_auto_offset_reset``  *string*
    - **Consumer auto offset reset** What to do when there is no initial offset in Kafka or if the current offset does not exist any more on the server. Default is earliest

  ``consumer_fetch_max_bytes``  *integer*
    - **The maximum amount of data the server should return for a fetch request** Records are fetched in batches by the consumer, and if the first record batch in the first non-empty partition of the fetch is larger than this value, the record batch will still be returned to ensure that the consumer can make progress. As such, this is not a absolute maximum.

  ``consumer_isolation_level``  *string*
    - **Consumer isolation level** Transaction read isolation level. read_uncommitted is the default, but read_committed can be used if consume-exactly-once behavior is desired.

  ``consumer_max_partition_fetch_bytes``  *integer*
    - **The maximum amount of data per-partition the server will return.** Records are fetched in batches by the consumer.If the first record batch in the first non-empty partition of the fetch is larger than this limit, the batch will still be returned to ensure that the consumer can make progress. 

  ``consumer_max_poll_interval_ms``  *integer*
    - **The maximum delay between polls when using consumer group management** The maximum delay in milliseconds between invocations of poll() when using consumer group management (defaults to 300000).

  ``consumer_max_poll_records``  *integer*
    - **The maximum number of records returned by a single poll** The maximum number of records returned in a single call to poll() (defaults to 500).

  ``offset_flush_interval_ms``  *integer*
    - **The interval at which to try committing offsets for tasks** The interval at which to try committing offsets for tasks (defaults to 60000).

  ``offset_flush_timeout_ms``  *integer*
    - **Offset flush timeout** Maximum number of milliseconds to wait for records to flush and partition offset data to be committed to offset storage before cancelling the process and restoring the offset data to be committed in a future attempt (defaults to 5000).

  ``producer_max_request_size``  *integer*
    - **The maximum size of a request in bytes** This setting will limit the number of record batches the producer will send in a single request to avoid sending huge requests.

  ``session_timeout_ms``  *integer*
    - **The timeout used to detect failures when using Kafka’s group management facilities** The timeout in milliseconds used to detect failures when using Kafka’s group management facilities (defaults to 10000).



``kafka_rest``  *boolean*
  - **Enable Kafka-REST service** 



``kafka_version``  *['string', 'null']*
  - **Kafka major version** 



``schema_registry``  *boolean*
  - **Enable Schema-Registry service** 



``kafka_rest_config``  *object*
  - **Kafka REST configuration** 

  ``producer_acks``  *string*
    - **producer.acks** The number of acknowledgments the producer requires the leader to have received before considering a request complete. If set to 'all' or '-1', the leader will wait for the full set of in-sync replicas to acknowledge the record.

  ``producer_linger_ms``  *integer*
    - **producer.linger.ms** Wait for up to the given delay to allow batching records together

  ``consumer_enable_auto_commit``  *boolean*
    - **consumer.enable.auto.commit** If true the consumer's offset will be periodically committed to Kafka in the background

  ``consumer_request_max_bytes``  *integer*
    - **consumer.request.max.bytes** Maximum number of bytes in unencoded message keys and values by a single request

  ``consumer_request_timeout_ms``  *integer*
    - **consumer.request.timeout.ms** The maximum total time to wait for messages for a request if the maximum number of messages has not yet been reached

  ``simpleconsumer_pool_size_max``  *integer*
    - **simpleconsumer.pool.size.max** Maximum number of SimpleConsumers that can be instantiated per broker



``schema_registry_config``  *object*
  - **Schema Registry configuration** 

  ``topic_name``  *string*
    - **topic_name** The durable single partition topic that acts as the durable log for the data. This topic must be compacted to avoid losing data due to retention policy. Please note that changing this configuration in an existing Schema Registry / Karapace setup leads to previous schemas being inaccessible, data encoded with them potentially unreadable and schema ID sequence put out of order. It's only possible to do the switch while Schema Registry / Karapace is disabled. Defaults to `_schemas`.

  ``leader_eligibility``  *boolean*
    - **leader_eligibility** If true, Karapace / Schema Registry on the service nodes can participate in leader election. It might be needed to disable this when the schemas topic is replicated to a secondary cluster and Karapace / Schema Registry there must not participate in leader election. Defaults to `true`.




