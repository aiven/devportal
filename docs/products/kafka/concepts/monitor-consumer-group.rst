Monitoring consumer groups in Aiven for Apache Kafka®
======================================================

With Aiven for Apache Kafka® dashboards and telemetry, you can monitor the performance and system resources of your Aiven for Apache Kafka service. Aiven provides pre-built dashboards and telemetry for your service, allowing you to collect and visualize telemetry data using InfluxDB® and Grafana®. Aiven streamlines the process by automatically configuring the dashboards for each of your Aiven for Apache Kafka instances.

This section builds on the :doc:`service integrations </docs/platform/concepts/service-integration>` documentation and provides an in-depth look at consumer group graphs and related key terminology in Aiven for Apache Kafka®. Consumer group graphs offer valuable insights into the behavior of Apache Kafka consumers, which is crucial for maintaining a continuously running production Kafka system.


Topics 
---------
In Apache Kafka®, a topic serves as a unique channel for discussions. Producers send messages to the topic while consumers read those messages. For instance, in a topic named ``soccer``, you can read what others say about soccer (acting as a consumer) or post messages about soccer (acting as a producer).

Topic partitions 
-----------------
The storage of messages for an Apache Kafka® topic can be spread across one or more topic partitions. For instance, in a topic that has 100 messages and is set up to have 5 partitions, 20 messages would be assigned to each partition.

Consumer groups
----------------

Apache Kafka® allows multiple consumers to read messages from a Kafka topic. This improves the message consumption rate and overall performance. Organizing consumers into consumer groups identified by a group ID is common practice. Consumer groups consume messages from a topic with messages spread across multiple partitions. Apache Kafka ensures that each message is consumed by only one consumer, which is essential for certain classes of business applications.

For example, with a topic having 100 messages across five partitions and five consumers in a consumer group, each consumer will be allocated a distinct partition, consuming 20 messages each.

If the number of consumers exceeds the number of partitions, extra consumers remain idle until an active consumer exits. Also, a consumer cannot read from a partition not assigned to it.


Consumer group telemetry
-------------------------
Aiven for Apache Kafka provides built-in consumer group graphs that offer valuable telemetry to monitor and manage consumer groups effectively.

Consumer group graph: consumer group replication lag
```````````````````````````````````````````````````````
Consumer group lag is an important metric in your Apache Kafka dashboard. It shows how far behind the consumers in a group are in consuming messages on the topic. A significant lag could indicate one of two scenarios - terminated consumers or consumers who are alive but unable to keep up with the rate of incoming messages. Persistent lag for long durations may indicate that the system is not behaving according to plan, requiring investigation and follow-up actions to resolve the issue.

The terms ``Consumer group lag`` and ``Consumer group replication lag`` can be used interchangeably. Consumer Group Lag is typically a metric provided by the client side, while Aiven computes its metric known as Consumer Group Replication Lag (``kafka_consumer_group_rep_lag``) by fetching information about partitions and consumer groups from broker side. This metric captures the difference between the latest published offset (high watermark) and the consumer group offset for the same partition.

The consumer group graph below, which is enabled by default, provides valuable insights into consumer behavior. It displays the consumer group replication lag, indicating how far behind the consumers are in consuming messages from a topic. This graph provides information about consumer behavior, enabling you to take appropriate action if necessary.


.. image:: /images/products/kafka/consumer-group-graphs-for-kafka-dashboards.png
  :alt: Image of consumer group replication lag


Consumer group offset telemetry
`````````````````````````````````
In Apache Kafka, messages are written into a partition as append-only logs and each message is assigned a unique incremental number called the offset. These offsets indicate the exact position of messages within the partition.

Aiven for Apache Kafka provides offset telemetry, which can help understand message consumption patterns and troubleshoot issues. The ``kafka_consumer_group_offset`` metric identifies the consumer group's most recent committed offset, which can be used to determine its relative position within the assigned partitions.







