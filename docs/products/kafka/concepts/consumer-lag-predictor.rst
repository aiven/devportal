Consumer lag predictor for Aiven for Apache Kafka®
===================================================

The **consumer lag predictor** for Aiven for Apache Kafka estimates the delay between the time a message is produced and when it's eventually consumed by a consumer group. This information can be used to improve the performance, scalability, and cost-effectiveness of your Kafka cluster.

.. important::
    Consumer Lag Predictor for Aiven for Apache Kafka® is a limited availability feature. If you're interested in trying out this feature, contact the sales team at sales@Aiven.io.

To use the **consumer lag predictor** effectively, setting up :doc:`Prometheus integration </docs/platform/howto/integrations/prometheus-metrics>` with your Aiven for Apache Kafka® service is essential. Prometheus integration enables the extraction of key metrics necessary for lag prediction and monitoring. 

Why use consumer lag predictor?
---------------------------------

By periodically analyzing the Kafka cluster, including topic and consumer group offsets, this *Consumer Lag Predictor* provides insights crucial for scenarios like auto-scaling consumers, ensuring timely message processing.

Use case
~~~~~~~~~

- **Auto-scaling of consumers**: Leveraging the time lag metric allows users to optimize message processing by dynamically adapting their consumers.

Limitation
-----------

Using the **consumer lag predictor** can impact your Apache Kafka cluster's performance. While it offers valuable insights, it also demands more CPU and memory on each Kafka node. To optimize its use, consider the following:

- **Resource management:** Enabling the *Consumer Lag Predictor* will lead to higher CPU and memory consumption on each Kafka node. Before enabling it, review your current resource usage to ensure smooth performance.
- **Topic selection:** It is advisable to be selective when choosing topics for lag calculation. Starting with a few topics and gradually including more can effectively manage system performance impact.

Metrics
-------

Metrics offer a tangible way to measure and understand consumer lag. These metrics can be viewed and analyzed using monitoring tools like Prometheus. Here are the key metrics provided:

- ``kafka_lag_predictor_topic_produced_records``: Represents the number of records produced, categorized by topic and partition.
- ``kafka_lag_predictor_group_consumed_records``: Represents the number of records consumed, sorted by group, topic, and partition.
- ``kafka_lag_predictor_group_lag_predicted_seconds``: Provides the predicted lag time in seconds, organized by group, topic, and partition.


Next steps
-----------
- Learn how to :doc:`enable consumer lag predictor </docs/products/kafka/howto/enabled-consumer-lag-predictor>` for your Aiven for Apache Kafka® service 