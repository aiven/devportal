Enable the consumer lag predictor for Aiven for Apache Kafka®
===============================================================

The :doc:`consumer lag predictor </docs/products/kafka/concepts/consumer-lag-predictor>` in Aiven for Apache Kafka® provides visibility into the time between message production and consumption, allowing for improved cluster performance and scalability.

.. important::
    Consumer Lag Predictor for Aiven for Apache Kafka® is a limited availability feature. If you're interested in trying out this feature, contact the sales team at sales@Aiven.io.


Prerequisites
-------------

Before you start, ensure you have the following:

- Aiven account.
- :doc:`Aiven for Apache Kafka® </docs/products/kafka/get-started>` service running.
- :doc:`Prometheus integration </docs/platform/howto/integrations/prometheus-metrics>` set up for your Aiven for Apache Kafka for extracting metrics.
- Necessary permissions to modify service configurations.

Enable via Aiven Console
----------------------------------------------------

1. In the `Aiven Console <https://console.aiven.io/>`_, select your project and then choose your Aiven for Apache Kafka® service.

2.  In the service page, click **Service settings** on the sidebar. 

3. Scroll to the **Advanced configuration** section, and select **Configure**.

4. In the **Advanced configuration** screen, select **Add configuration options**.

5. In the add configuration options:

   - Find and set ``kafka_lag_predictor.enabled`` to **Enabled** position. This enables the lag predictor to compute predictions for all consumer groups across all topics.
   - Find ``kafka_lag_predictor.group_filters`` and enter the desired consumer group pattern. This specifies which consumer groups to consider during lag prediction calculations.

   .. note::
    
     By default, the consumer lag predictor calculates the lag of all consumer groups. To restrict the calculation to specific groups, use the ``kafka_lag_predictor.group_filters`` option.

6. Select **Save configuration** to save your changes and enable consumer lag prediction.

Enable via Aiven CLI
------------------------------------------------

Follow these steps to enable the consumer lag predictor for your Aiven for Apache Kafka service using :doc:`Aiven CLI </docs/tools/cli>`.

1. Retrieve the project information using the following command:
   
   .. code:: 
    
        avn project details
    
   If you need details for a specific project, use:

   .. code:: 

    avn project details --project <your_project_name>

2. Get the name of the Aiven for Apache Kafka service for which you want to enable the consumer lag predictor by using the following command:

   .. code:: 
   
    avn service list

   Make a note of the ``SERVICE_NAME`` corresponding to your Aiven for Apache Kafka service.

3. Enable the consumer lag predictor for your service:
   
   .. code:: 
   
    avn service update <SERVICE_NAME> -c kafka_lag_predictor.enabled=true

   Replace <SERVICE_NAME> with your actual service name.

   .. note::
    This enables the lag predictor to compute predictions for all consumer groups across all topics.

4. If you wish to specify which consumer groups should be considered when calculating the lag prediction, you can set the ``group_filters`` configuration:

   .. code:: 
   
    avn service update <SERVICE_NAME> \
    -c kafka_lag_predictor.group_filters=\
     '["example_consumer_group_1", "example_consumer_group_2"]'




   - Replace ``<SERVICE_NAME>`` with the actual name or ID of your Aiven for Apache Kafka® service.
   - Replace ``example_consumer_group_1`` and ``example_consumer_group_2`` with your actual consumer group names.


Monitor metrics with Prometheus
-------------------------------

After enabling the consumer lag predictor, you can use Prometheus to access and monitor detailed metrics that offer insights into your Kafka cluster's performance. Here are the specific metrics and what they represent:

.. list-table::
   :widths: 25 20 60
   :header-rows: 1

   * - Metric
     - Type
     - Description
   * - ``kafka_lag_predictor_topic_produced_records_total``
     - Counter
     - Represents the total count of records produced.
   * - ``kafka_lag_predictor_group_consumed_records_total``
     - Counter
     - Represents the total count of records consumed.
   * - ``kafka_lag_predictor_group_lag_predicted_seconds``
     - Gauge
     - Represents the estimated time lag, in seconds, for a consumer group to catch up to the latest message.



