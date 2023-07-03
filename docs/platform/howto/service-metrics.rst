Access service metrics
=======================

Service metrics are essential for monitoring and evaluating how well your services perform. They provide valuable information about how your services utilize resources, their efficiency, and their overall health. By tracking and analyzing service metrics, you can make data-driven decisions, identify potential issues, and optimize the performance of your services.

Available service metrics
--------------------------

The service metrics available in the Aiven Console include:

* **CPU usage:** Shows the percentage of CPU resources consumed by the service.
* **Disk space usage:** Represents the percentage of disk space utilized by the service.
* **Disk iops (reads):** Indicates the input/output operations per second (IOPS) for disk reads.
* **Disk iops (writes):** Indicates the input/output operations per second (IOPS) for disk writes.
* **Load average:** Shows the 5-minute average CPU load, indicating the system's computational load.
* **Memory usage:** Represents the percentage of memory resources utilized by the service.
* **Network received:** Indicates the amount of network traffic received by the service, measured in bytes per second.
* **Network transmitted:** Indicates the amount of network traffic transmitted by the service, also measured in bytes per second.

View service metrics
---------------------

The  `Aiven Console <https://console.aiven.io/>`_ provides a user-friendly interface for accessing service metrics. Follow these steps to retrieve the metrics:

1. Go to your **Services**, and open the service you want to review.
2. Navigate to the **Metrics** tab. 
3. Choose the desired period for which you want to retrieve the metrics. The available options are:

   * **Hour:** Last hour metrics, updated every 30 seconds.
   * **Day:** Last day metrics, updated every 5 minutes.
   * **Week:** Last week metrics, updated every 30 minutes.
   * **Month:** Last month metrics, updated every 3 hours.
   * **Year:** Last year metrics, updated daily.

.. note:: 
    The selected period is relative to the current date and time. For instance, when you select the **Hour** option, it retrieves metrics for the last hour.


To further enhance your :doc:`monitoring capabilities </docs/platform/howto/monitoring-services>`, you can **Enable metrics integration** and establish a connection to push service metrics to an M3, InfluxDB®, or PostgreSQL® service within the Aiven platform. This integration allows you to conveniently send your service metrics to an existing service or create a new one dedicated to receiving and storing the metrics. 
