``NOT_LEADER_FOR_PARTITION`` errors
===================================

Aiven continuously monitors services to ensure they are healthy; if problems arise, nodes could be recycled: new nodes are created to substitute old, malfunctioning ones. During nodes replacement in your Aiven for Apache Kafka® cluster, you may find several ``NOT_LEADER_FOR_PARTITION`` warnings or errors in the logs of your producer.

The exact error message depends on your client library and log formatting, but should be similar to the following:

::

    [2021-02-04 09:01:20,118] WARN [Producer clientId=test-producer] Received invalid metadata error in produce request on partition topic1-25 due to org.apache.kafka.common.errors.NotLeaderForPartitionException: This server is not the leader for that topic-partition.. Going to request metadata update now (org.apache.kafka.clients.producer.internals.Sender)

This is an expected behavior as part of the failover from old to new nodes. 

Each producer contains a metadata cache that identifies which broker is the leader of each partition. When your code produces a message, it tries to send it to the broker that is the partition leader according to the producer's metadata cache.

When nodes are replaced, the partition leaders are expected to change. Every partition leader changes at least once, but it can be more, depending on the number of nodes and how many nodes are replaced at a time. 

.. Note::

    If a service has 3000 active partitions, then you can expect at least one of these error messages for each partition in each producer. 

Producers usually update their metadata cache immediately. After that, they continue producing messages without issue. However, high load on the broker side or unfortunate timing in parallel requests can sometimes trigger several updates. This might cause a very large number of these warnings in the producer logs, which can look worrying but is in fact harmless.