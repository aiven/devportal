Configure Aiven for Apache Kafka®-Prometheus via Privatelink
============================================================

Ensure secure and efficient monitoring of your Aiven for Apache Kafka® multi-node service with Privatelink Prometheus integration. Privatelink establishes a secure connection between your network and Aiven to keep your Apache Kafka data private and secure.


Prerequisites
-------------

Before you start, ensure you have the following:

- :doc:`Aiven for Apache Kafka® </docs/products/kafka/getting-started>` service running.
- :doc:`Prometheus integration </docs/platform/howto/integrations/prometheus-metrics>` set up for your Aiven for Apache Kafka for extracting metrics.
- Necessary permissions to modify service configurations.


Configuration steps
--------------------

Step 1: Basic configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Begin by configuring Prometheus to scrape metrics from your Aiven for Apache Kafka service. This setup involves specifying various parameters for secure and accurate data retrieval. Folowing is an example configuration:

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
    Setting ``insecure_skip_verify: true`` is crucial for Privatelink connections, as it permits Prometheus to disregard TLS certificate validation against host IP addresses, facilitating seamless connectivity.

- ``basic_auth``: Provides authentication credentials for Kafka service access.
- ``http_sd_configs``: Configures HTTP service discovery. Includes:
- ``url``: The URI for Prometheus Privatelink service access.
- ``refresh_interval``: The frequency of target list refresh, e.g., ``120s``.
  
.. note::
    The ``basic_auth`` and ``tls_config`` are specified twice - first for fetching the HTTP SD response and then for the metrics. This duplication is necessary because the same authentication and security settings are used to retrieve the service discovery information and scrape the metrics.

Step 2: (Optional) Metadata and relabeling 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your setup involves multiple Privatelink connections, this optional step allows for more precise target management. Use the ``__meta_privatelink_connection_id`` label to filter and distinguish metrics from different Privatelink connections. This approach is beneficial in scenarios requiring separate monitoring of distinct data streams.

.. code-block:: yaml

    relabel_configs:
      - source_labels: [__meta_privatelink_connection_id]
        regex: 1
        action: keep


Related pages
--------------

* :doc:`Aiven for Apache Kafka® metrics available via Prometheus </docs/products/kafka/reference/kafka-metrics-prometheus>`