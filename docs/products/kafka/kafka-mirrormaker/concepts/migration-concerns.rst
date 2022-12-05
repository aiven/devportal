Migration concerns
###################

MirrorMaker 2 is translating the offsets incorrectly if LAG shows negative on the target cluster and these are know issues which are expected to be resolved in 3.3.0 and tuning can be done to minimize hitting this issue.

Known bugs:
--------------

* https://issues.apache.org/jira/browse/KAFKA-12635 
* https://github.com/apache/kafka/pull/11748
* https://issues.apache.org/jira/browse/KAFKA-13452 
* https://github.com/apache/kafka/pull/11492
* MirrorMaker 2 always set ``min.insync.replicas = 1`` in destination cluster topics

MirrorMaker 2 tuning:
-----------------------

1. Using startup-32 as an example, change increase task workers in advanced options: ``kafka_mirrormaker.tasks_max_per_cpu = 4``
2. Reduce the seconds for these settings and make sure they are exactly the same everywhere:

  Advanced options:
    * ``kafka_mirrormaker.emit_checkpoints_interval_seconds``
    * ``kafka_mirrormaker.sync_group_offsets_interval_seconds`` 
    * Replication flow:
        * Sync interval in seconds

3. add `*[\-\.]` internal to the topic black list:
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
3. With kt the following might be helpful to get the latest messages from all partitions:
    * ``kt consume -auth ./mykafka.conf -brokers service-project.aivencloud.com:24949 -topic topicname -offsets all=newest:newest | jq -c -s 'sort_by(.partition) | .[] | {partition: .partition, value: .value, timestamp: .timestamp}'``

MirrorMaker 2 always set ``min.insync.replicas = 1`` in destination cluster topics
--------------------------------------------------------------------------------

**Description**

If a topic on destination cluster is updated or pre-created with ``min.insync.replicas > 1`` , MirrorMaker 2 would always be overwritten with ``min.insync.replicas = 1`` in target topics. 
The replication factor of target topics does not match the replication factor of source topics either when they are newly-created by MM2, or when they exist beforehand.

Steps to reproduce:

Create the following topics on destination kafka:

* topic04 -  partitions: 3 replicas: 3 min.insync.replicas: 3
* topic05 - partitions: 6 replicas: 3 min.insync.replicas: 3

Create the following topics on source kafka:

* topic04 -  partitions: 6 replicas: 2 min.insync.replicas: 1
* topic05 - partitions: 6 replicas: 3 min.insync.replicas: 3

Start MirrorMaker 2 with the following settings:

* 4. after > 15 minutes

topic configuration on destination kafka got updated as the following:

* topic04 -  partitions: 6 replicas: 3 min.insync.replicas: 1
* topic05 - partitions: 6 replicas: 3 min.insync.replicas: 1

Findings:

* replicas does not get updated by MM2
* min.insync.replicas would be overwritten as 1 by MM2



