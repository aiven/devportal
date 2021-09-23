TLS/SSL certificates
--------------------

All traffic to Aiven services is always protected by TLS. It ensures that third-parties can't eavesdrop or modify the data while in transit between Aiven services and the clients accessing them.

Every Aiven project has its own private Certificate Authority (CA) which is used to sign certificates that are used internally by the Aiven services to communicate between different cluster nodes and to Aiven management systems.

Some service types (listed below) uses the Aiven project's CA for external connections. To access these services, you need to download the CA certificate and configure it on your browser or client.

For other services a browser-recognized CA is used, which is normally already marked as trusted in browsers and operating systems, so downloading the CA certificate is not normally required.

Certificate requirements
========================
The table below shows if you need to download the CA certificate to connect to Aiven services:

.. list-table::
  :header-rows: 1
  :align: left

  * - Service
    - Certificate download required?
  * - Aiven for PostgreSQL
    - Yes
  * - Aiven for Apache Kafka
    - Yes, it is also required to download the client certificate and key
  * - Aiven for Apache Kafka Connect
    - No
  * - Aiven Kafka-REST (Karapace)
    - No
  * - Aiven Kafka Schema Registry (Karapace)
    - No
  * - Aiven for Elasticsearch
    - No*
  * - Aiven for Grafana
    - No
  * - Aiven for InfluxDB
    - No*
  * - Aiven for Redis
    - No*

\* Old services may be using the Aiven project's CA, it can be switched to a browser-recognized certificate with a support ticket.

Download the certificates
=========================

You can download the CA certificate through the Aiven `web console <https://console.aiven.io>`_ by accessing the service page and clicking on the ``Download`` button on the ``CA Certificate`` line.

.. image:: /images/platform/ca-download.png
    :alt: A screenshot of the Aiven web console service page, showing where is the CA certificate download button.

Or, you can use the ``avn`` :doc:`command-line tool <docs/tools/cli>` with the following command::

  avn service user-creds-download --username <username> <service-name>