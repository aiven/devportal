Optimizing resource usage for Kafka® Startup-2 Plan
===================================================

The Kafka Startup-2 Plan has been optimized for lightweight operations, making it ideal for applications that handle fewer messages per second and don't demand high throughput. But sometimes, you might encounter an alert showing high resource usage. This alert is generally triggered when the Kafka broker memory drops too low and CPU idle time is less than 15%. Understanding the reasons behind these alerts and their mitigation ensures optimized Kafka usage and consistent application performance.

What triggers high resource usage?
----------------------------------

There are a few things that can trigger high resource usage on the Kafka Startup-2 plan:

- **High Kafka Traffic:**
  Heavy traffic due to too many producer/consumer requests can cause an overload, leading to increased CPU and memory usage on the Kafka broker. When a Kafka cluster is overloaded, it may struggle to correctly assign leadership for a partition, potentially causing service disruptions.

- **Excessive Kafka Partitions:**
  An excessive number of Kafka partitions for the brokers to manage effectively can lead to increased memory usage and IO load.

- **Too many client connections:**
  When there are too many client connections, the memory usage can dip significantly. When your service's memory is low, it starts to use swap space, adding to the IO load. Regular use of swap space indicates your system may not have enough resources for its workload.

Additional causes of high resource usage
----------------------------------------

- **Datadog Integration:**
  While Datadog provides valuable monitoring, its agent is IO-heavy. On a Startup-2 Plan not designed for high IO operations, Datadog can significantly increase the IO load. Moreover, Datadog load increases with the number of topic partitions in your Kafka service.

- **Karapace Integration:**
  Karapace provides a REST API for Kafka, but this can consume a substantial amount of memory and contribute to a high load when REST API is used in high demand.

Strategies to minimize resource usage
-------------------------------------

- **Reduce Topic Partition Limit:**
  Decreasing the number of topic partitions reduces the load on the Kafka service.

- **Disable Datadog Integration:**
  If Datadog sends too many metrics, it could affect the reliability of the service and hinder the backup of topic configurations. It is recommended to turn off the integration of the Datadog service.

- **Enable Quotas:**
  Quotas can manage the resources consumed by clients, preventing any single client from using too much of the broker's resources.

- **Limit the Number of Integrations:**
  For smaller plans like the Startup-2, consider limiting the number of integrations to manage resource consumption effectively.

- **Upgrade Your Plan:**
  If your application demands more resources, upgrading to a larger Kafka plan can ensure stable operation.

Integration advisory for Kafka Startup-2 plan
-----------------------------------------------

The Kafka Startup-2 plan runs on relatively small machines. Enabling integrations like Datadog or Karapace may consume more resources than this plan can handle, affecting your cluster's performance. If you notice any issues with your cluster or need more resources for your integrations, consider upgrading to a higher plan.