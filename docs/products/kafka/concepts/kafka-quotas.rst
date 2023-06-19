Quotas in Aiven for Apache Kafka®
====================================

Quotas ensure fair resource allocation, stability, and efficiency in your Kafka cluster. In Aiven for Apache Kafka®, you can :doc:`add quotas <../howto/manage-quotas>` to limit the data or requests exchanged by producers and consumers within a specific period, preventing issues like broker overload, network congestion, and service disruptions caused by excessive or malicious traffic. You can effectively manage resource consumption and ensure optimal user performance by implementing quotas.

Using quotas offer several benefits:

* **Resource management:** Quotas prevent individual clients from consuming excessive resources, thus ensuring fairness in resource allocation.
* **Stability:** By setting limits on network throughput and CPU usage helps maintain stability and prevent performance degradation of the Apache Kafka cluster.
* **Efficiency:** Quotas enable you to optimize resource utilization and achieve better overall efficiency within your Kafka deployment.


Supported quota types
-----------------------

Aiven for Apache Kafka service provides different quotas to help you manage resources effectively. These quotas offer benefits in controlling network bandwidth and CPU usage:

* **Consumer throttle (Network bandwidth quota):** This quota allows you to limit the amount of data a consumer can retrieve from the Kafka cluster per second. By setting a maximum network throughput, you prevent any single consumer from using excessive network bandwidth. 
* **Producer throttle (Network bandwidth quota):** Similar to the consumer throttle, this quota limits the amount of data a producer can send to the Kafka cluster per second. It ensures that producers do not overload the system by sending excessive data, thereby maintaining system stability.
* **CPU throttle:** This quota is about managing the CPU usage. You can manage CPU usage by setting a percentage of the total CPU time. Limiting the CPU resources for specific client IDs or users prevents any individual from monopolizing CPU resources, promoting fairness and efficient resource utilization.


Client ID and users in quotas
--------------------------------
**Client ID** and **User** are two types of entities that can be used to enforce quotas in Kafka.

**Client ID** 
  A Client ID is a unique identifier assigned to each client application or producer/consumer instance that connects to a Kafka cluster. It helps track the activity and resource usage of individual clients. When configuring quotas, you can set limits based on the Client ID, allowing you to control the amount of resources (such as network bandwidth or CPU) that a specific client can utilize.

**Users**
  A User represents the authenticated identity of a client connecting to a cluster. With authentication mechanisms like SASL, users are associated with specific connections. By setting quotas based on Users, resource limits can be enforced per-user. 

Quotas enforcement 
-------------------
Quotas enforcement ensures clients stay within their allocated quotas. These quotas are implemented and controlled by the brokers on an individual basis. Each client group is assigned a specific quota for every broker, and when this threshold is reached, throttling mechanisms come into action.

When a client exceeds its quota, the broker calculates the necessary delay to bring the client back within its allocated limits. Subsequently, the broker promptly responds to the client, indicating the duration of the delay. Additionally, the broker suspends communication with the client during this delay period. This cooperative approach from both sides ensures the effective enforcement of quotas.

Quota violations are swiftly detected using short measurement windows, typically 30 windows of 1 second each. This ensures timely correction and prevents bursts of traffic followed by long delays, ensuring a better user experience.

For more information, refer to the `Enforcement <https://kafka.apache.org/documentation/#design_quotasenforcement>`_ in Apache Kafka® official documentation.

.. seealso:: 
    * :doc:`How to add and manage quotas <../howto/manage-quotas>`
