MirrorMaker 2 common parameters
###############################

MirrorMaker 2 (MM2) offers a suite of parameters to help with data replication and monitoring within Apache Kafka® ecosystems. This topic outlines common parameters you can adjust, along with tips for validating MM2's performance.

1. Increase the value of ``kafka_mirrormaker.tasks_max_per_cpu`` in the advanced options. Setting this to match the number of partitions can enhance performance.
2. Ensure the interval seconds for the following settings match. You can reduce these intervals for more frequent data synchronization:

   - Advanced options:
    
     - ``kafka_mirrormaker.emit_checkpoints_interval_seconds``
     - ``kafka_mirrormaker.sync_group_offsets_interval_seconds`` 

   - Replication flow:
     
     - ``Sync interval in seconds``.

3. To exclude internal topics, add these patterns to your topic blacklist:

   - ``.*[\-\.]internal`` ``.*\.replica`` ``__.*`` ``connect.*``

4. Depending on your use case, consider adjusting these parameters:

   - ``kafka_mirrormaker.consumer_fetch_min_bytes``
   - ``kafka_mirrormaker.producer_batch_size``
   - ``kafka_mirrormaker.producer_buffer_memory``
   - ``kafka_mirrormaker.producer_linger_ms``
   - ``kafka_mirrormaker.producer_max_request_size`` 

MirrorMaker 2 validation tips
---------------------------------

To ensure MirrorMaker 2 is up-to-date with message processing, monitor these:

1. **Consumer lag metric**:
   Monitor the ``kafka.consumer_lag`` metric.

2. **Dashboard metrics**:
   If MirrorMaker 2 stops adding records to a topic, the ``jmx.kafka.connect.mirror.record_count`` metric stops increasing, showing a flat line on the dashboard.

3. **Retrieve latest messages with `kt`**:
   Use `kt <https://github.com/fgeller/kt>`_  to retrieve the latest messages from all partitions with the following command:
   
   ::
   
        kt consume -auth ./mykafka.conf \
        -brokers SERVICE-PROJECT.aivencloud.com:PORT \
        -topic topicname -offsets all=newest:newest | \
        jq -c -s 'sort_by(.partition) | .[] | \
        {partition: .partition, value: .value, timestamp: .timestamp}'