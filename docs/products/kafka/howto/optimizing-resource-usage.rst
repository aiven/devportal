Optimizing resource usage for Aiven for Apache Kafka® 
=======================================================

Aiven for Apache Kafka® service plans with CPUs of 2 or less are optimized for lightweight operations, making them suitable for applications that handle fewer messages per second and do not require high throughput. However, you might sometimes encounter an alert showing high resource usage. These alerts typically arise when the Kafka broker memory drops too low, and the CPU idle time is less than 15%. Understanding the reasons behind these alerts and their mitigation ensures optimized Kafka usage and consistent application performance.

What triggers high resource usage?
----------------------------------

Several factors can lead to high resource usage across Aiven for Apache Kafka plans:

- **High Kafka Traffic:**
  Heavy traffic due to too many producer/consumer requests can cause an overload, leading to increased CPU and memory usage on the Kafka broker. When a Kafka cluster is overloaded, it may struggle to correctly assign leadership for a partition, potentially causing service disruptions.

- **Excessive Kafka Partitions:**
  An excessive number of Kafka partitions for the brokers to manage effectively can lead to increased memory usage and IO load.

- **Too many client connections:**
  When there are too many client connections, the memory usage can dip significantly. When your service's memory is low, it starts to use swap space, adding to the IO load. Regular use of swap space indicates your system may not have enough resources for its workload.

Additional causes of high resource usage
----------------------------------------

- **Datadog Integration:**
  Datadog offers essential monitoring, but its agent is IO-intensive. Especially on plans not designed for high IO operations, Datadog can notably increase the IO load. The load from Datadog also increases with the number of topic partitions in your Kafka service.

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
  For smaller plans such as the Startup-2, consider limiting the number of integrations to manage resource consumption effectively.

- **Upgrade Your Plan:**
  If your application demands more resources, upgrading to a larger Kafka plan can ensure stable operation.

Integration advisory for Kafka Startup-2 plan
-----------------------------------------------

Aiven for Apache Kafka service plans with CPUs of 2 or less operate on relatively small machines. Enabling integrations like Datadog or Karapace might exceed the resources these plans offer, impacting your cluster's performance. If you experience issues with your cluster or require more resources for your integrations, consider upgrading to a higher plan.