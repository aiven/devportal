Configure Prometheus for Aiven for Apache Kafka® using Privatelink
====================================================================

You can integrate Prometheus with your Aiven for Apache Kafka® service using Privatelink for secure monitoring. This setup uses a Privatelink load balancer, which allows for efficient service discovery of Apache Kafka nodes and enables you to connect to your Aiven for Apache Kafka service using a private endpoint in your network or VPCs.


Prerequisites
-------------

Before you start, ensure you have the following:

- :doc:`Aiven for Apache Kafka® </docs/products/kafka/get-started>` service running.
- :doc:`Prometheus integration </docs/platform/howto/integrations/prometheus-metrics>` set up for your Aiven for Apache Kafka for extracting metrics.
- Necessary permissions to modify service configurations.


Configuration steps
--------------------

Basic configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Begin by configuring Prometheus to scrape metrics from your Aiven for Apache Kafka service. This setup involves specifying various parameters for secure data retrieval. Following is an example configuration:

.. code-block:: yaml

    scrape_configs:
      - job_name: aivenmetrics
        scheme: https
        tls_config:
          insecure_skip_verify: true
        basic_auth:
          username: <PROMETHEUS_USERNAME>
          password: <PROMETHEUS_PASSWORD>
        http_sd_configs:
          - url: <PROMETHEUS_PRIVATELINK_ACCESS_SERVICE_URI>
            refresh_interval: 120s
            tls_config:
              insecure_skip_verify: true
            basic_auth:
              username: <PROMETHEUS_USERNAME>
              password: <PROMETHEUS_PASSWORD>

**Configuration details**:

- ``job_name``: Identifies the set of targets, e.g., ``aivenmetrics``.
- ``scheme``: Specifies the protocol, typically ``https``.
- ``tls_config``: Manages TLS settings. 

  .. note::
    Setting ``insecure_skip_verify: true`` is crucial, as it permits Prometheus to disregard TLS certificate validation against host IP addresses, facilitating seamless connectivity.

- ``basic_auth``: Provides authentication credentials for Apache Kafka service access.
- ``http_sd_configs``: Configures HTTP Service Discovery. Includes:

  - ``url``: The URI for Prometheus Privatelink service access.
  - ``refresh_interval``: The frequency of target list refresh, e.g., ``120s``.
  
.. note::
    The ``basic_auth`` and ``tls_config`` are specified twice - first for scraping the HTTP SD response and then to retrieve service metrics. This duplication is necessary because the same authentication and security settings are used to retrieve the service discovery information and scrape the metrics.

(Optional) Metadata and relabeling 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your setup involves multiple Privatelink connections, you can leverage Prometheus's relabeling for better target management. This approach allows you to dynamically modify target label sets before scraping. 

To manage metrics from different Privatelink connections, include the ``__meta_privatelink_connection_id`` label in your configuration. This setup helps categorize and filter relevant metrics for each connection.

.. code-block:: yaml

    relabel_configs:
      - source_labels: [__meta_privatelink_connection_id]
        regex: 1
        action: keep


The ``regex: 1`` in the configuration is a placeholder. Make sure to replace ``1`` with the actual Privatelink connection ID that you wish to monitor.



Related pages
--------------

* :doc:`Aiven for Apache Kafka® metrics available via Prometheus </docs/products/kafka/reference/kafka-metrics-prometheus>`