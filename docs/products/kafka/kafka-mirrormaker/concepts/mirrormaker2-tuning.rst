MirrorMaker 2 common parameters
###############################

1. ``kafka_mirrormaker.tasks_max_per_cpu`` in advanced options can be increased, set it to match the number of partitions may improve performance.
2. Interval seconds for the following settings should match, intervals can be decreased to sync data more frequently:

  Advanced options:
    * ``kafka_mirrormaker.emit_checkpoints_interval_seconds``
    * ``kafka_mirrormaker.sync_group_offsets_interval_seconds`` 
    * Replication flow:
        * Sync interval in seconds

3. Add `*[\-\.]` internal to the topic black list:
    * connect.* __.*, crowdcontrol.public.events, .*[\-\.]internal
    * The following parameters can be tuned depending on use case:
        * ``kafka_mirrormaker.consumer_fetch_min_bytes``
        * ``kafka_mirrormaker.producer_batch_size``
        * ``kafka_mirrormaker.producer_buffer_memory``
        * ``kafka_mirrormaker.producer_linger_ms``
        * ``kafka_mirrormaker.producer_max_request_size``

To validate MM2 is caught up on the messages, the following can be monitored:
------------------------------------------------------------------------------

1. ``Metric kafka.consumer_lag``
2. ``jmx.kafka.connect.mirror.record_count``:
    * When MirrorMaker 2 stops producing records to a topic then the value of this metric stops increasing and therefore a flat line is visible in the dashboard
3. With kt the following command helps to to retrieve the latest messages from all partitions:
    * ``kt consume -auth ./mykafka.conf -brokers service-project.aivencloud.com:24949 -topic topicname -offsets all=newest:newest | jq -c -s 'sort_by(.partition) | .[] | {partition: .partition, value: .value, timestamp: .timestamp}'``