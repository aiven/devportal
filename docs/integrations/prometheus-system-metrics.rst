Prometheus system metrics
=========================

Prometheus integration allows you to monitor your Aiven services and understand the resource usage. Additionally, using this integration, you can monitor/track some non-service-specific metrics that may be worth monitoring.

To start monitoring these metrics, you need the :doc:`Prometheus integration configured and set up the Prometheus server <../platform/howto/integrations/prometheus-metrics>`.

To discover the metrics available for your services, make an HTTP ``GET`` request to your Prometheus service endpoint. Once your Prometheus integration is configured, you will find your Prometheus service details in the "Prometheus" tab of the Service Overview page. Make a note of the:

* Prometheus URL
* Username
* Password

Then make a request like the one below to get a snapshot of your metrics, replacing the placeholders with the values for your service:

.. code-block:: bash

    curl -k --user USERNAME:PASSWORD PROMETHEUS_URL/metrics

The resulting output is a full list of the metrics available for your service.

CPU usage
----------

CPU usage metrics are helpful in determining if the CPU is constantly being maxed out.
For a high-level view of CPU usage for a single CPU service, you can use

.. code-block:: bash

    100 - cpu_usage_idle{cpu="cpu-total"}

.. tip::

   A process with a ``nice`` value larger than 0 will be categorized as ``cpu_usage_nice``, which is not included in ``cpu_usage_user``.

It can be useful to monitor ``cpu_usage_iowait{cpu="cpu-total"}``. If this number is high, it indicates the service node is working on something I/O intensive. For example, 40 means 40% of CPU time is waiting for disk or network I/O.

The following table lists some important CPU-related metrics you can collect and monitor:

.. list-table::
  :header-rows: 1
  :align: left

  * - Metics
    - Description
  * - ``cpu_usage_idle``
    - The percentage of time the CPU is idle.
  * - ``cpu_usage_system``
    - The percentage of time the Kernel code is consuming the CPU.
  * - ``cpu_usage_user``
    - The percentage of time the CPU is in user-space program with ``nice`` value <= 0.
  * - ``cpu_usage_nice``
    - The percentage of time the CPU is in user-space program with ``nice`` value > 0.
  * - ``cpu_usage_iowait``
    - The percentage of time waiting for I/O operations.
  * - ``cpu_usage_steal``
    - The percentage of time waiting for the hypervisor to give CPU cycles to the VM.
  * - ``cpu_usage_irq``
    - The percentage of time the system is handling interrupts.
  * - ``cpu_usage_softirq``
    - The percentage of time the system is handling software interrupts.
  * - ``cpu_usage_guest``
    - The percentage of time the CPU is running for a guest OS.
  * - ``cpu_usage_guest_nice``
    - The percentage of time the CPU is running for a guest OS, with low priority.

These metrics are generated from the `Telegraf plugin <https://github.com/influxdata/telegraf/tree/master/plugins/inputs/cpu>`_.

Disk usage
----------

Monitoring the disk usage ensures that applications or processes don't fail due to an insufficient disk storage.

.. tip::

   Consider monitoring ``disk_used_percent`` and ``disk_free``.

The following table lists some important disk usage metrics you can collect and monitor:

.. list-table::
  :header-rows: 1
  :align: left

  * - Metics
    - Description
  * - ``disk_free``
    - Free space on the service disk
  * - ``disk_used``
    - Used space on the disk, for example, ``8.0e+9`` (8,000,000,000 bytes)
  * - ``disk_total``
    - Total space on the disk (free and used)
  * - ``disk_used_percent``
    - Percentage of the disk space used equal to ``disk_used / disk_total * 100``, for example, ``80`` (80% service disk usage)
  * - ``disk_inodes_free``
    - Number of index nodes available on the service disk
  * - ``disk_inodes_used``
    - Number of index nodes used on the service disk
  * - ``disk_inodes_total``
    - Total number of index nodes on the service disk

Memory usage
------------

Metrics for monitoring the memory consumption are essential to ensure the performance of your service.

.. tip::

   Consider monitoring ``mem_available`` (in bytes) or ``mem_available_percent``, as this is the estimated amount of memory available for application without swapping.

Network usage
-------------

Monitoring the network provides visibility of your network and an understanding of the network utilization and traffic, allowing you to act immediately in case of network issues.

.. tip::

   It may be worth monitoring the number of established TCP sessions available in the ``netstat_tcp_established`` metric.
