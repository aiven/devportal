Use Prometheus with Aiven
=========================

About Prometheus
----------------

Prometheus is an open-source systems monitoring and alerting toolkit. It
implements an in-memory and persistent storage model for metrics as well as
a query language for accessing the metrics.

The metrics delivery model of Prometheus is a pull model where the Prometheus
server connects to HTTP servers running on the nodes being monitored and pulls
the metrics from them. While this makes the service discovery more of a
challenge than using the more common push approach, it does have the benefit of
making the metrics available not just for Prometheus but for any application that can
read the Prometheus format from the HTTP server running on Aiven nodes.

Check Prometheus support on your service
----------------------------------------

Usually one Prometheus integration endpoint can be used for all services in the same project. To check if Prometheus is supported on your service, you need to verify if the project for this service has a Prometheus integration endpoint created. For this purpose, take the following steps:

#. | Log in to `Aiven Console <https://console.aiven.io/>`_, go to **Projects** in the top navigation bar, and select your project from the dropdown list.
#. | On the **Services** page, select **Integration endpoints** from the left sidebar.
#. | On the **Integration endpoints** page, select **Prometheus** from the list available integration endpoints, and check if there is any endpoint available under **Endpoint Name**.

If there is a Prometheus endpoint available, your service supports Prometheus. If there's no Prometheus endpoint available, proceed to :ref:`Enable Prometheus on your Aiven project <enable-prometheus>` to set up Prometheus for your service (project).

.. _enable-prometheus:

Enable Prometheus on your Aiven project
---------------------------------------

Aiven offers Prometheus endpoints for your services. To enable this feature, take the following steps:

#. | Log in to `Aiven Console <https://console.aiven.io/>`_, go to **Projects** in the top navigation bar, and select your project from the dropdown list.
#. | On the **Services** page, select **Integration endpoints** from the left sidebar.
#. | On the **Integration endpoints** page, select **Prometheus** from the list available integration endpoints, and select **Add new endpoint**.
#. | In the **Create new Prometheus endpoint** window, enter the details for the endpoint, and select **Create**. 
#. | Select **Services** from the sidebar, and navigate to the service that you would like to monitor.
#. On the **Overview** page of your service, go to the **Service integrations** section, and select **Manage integrations**.
#. | On the **Integrations** page, select **Prometheus**. 
#. | In the **Prometheus integration** window, select the endpoint name you created from the dropdown list, and select **Enable**.

   .. note::
      
      At the top of the **Integrations** page, you will see the Prometheus integration listed and status ``active``. 

#. | From the **Integrations** page, go to the **Overview** page > the **Connection information** section > the **Prometheus** tab.
#. | Copy **Service URI**, and use it in your browser to access the Prometheus dashboard.

.. topic:: Result

   The system initiates an HTTP server on all service nodes, granting access to the metrics. Aiven is exposing endpoints for your services.
   
.. note::
  
   There might be a slight delay of approximately one minute before the metrics become available.

Accessing Prometheus in a VPC
''''''''''''''''''''''''''''''

If you use a VPC in your project, to access Prometheus, you need to go to `Aiven Console <https://console.aiven.io/>`_ > your project > the service you want to monitor using Prometheus > the **Overview** page > the **Advanced configuration** section and enable property ``public_access.prometheus``.

Configure Prometheus
--------------------

After enabling Prometheus on your project, add a scrape configuration to Prometheus for the servers you want to pull data from. The examples in this section show how to set up the scrape configuration for both single-node and multi-node services.

Single-node services
''''''''''''''''''''

For single-node services, configure the following in your ``scrape_config`` job entry in ``prometheus.yml``:

* ``basic_auth`` details: Check your service's the **Overview** page > the **Connection information** section > the **Prometheus** tab).

* ``PROMETHEUS_SERVICE_URI``: Check **Service URI** on your service's the **Overview** page > the **Connection information** section > the **Prometheus** tab).

* ``ca_file``: Download the CA certificate from your service's the **Overview** page, and specify its location (the certificates are signed by the Aiven project CA).

  .. note::

     You can download the CA certificate using the `Aiven command line client <https://github.com/aiven/aiven-client/>`_ and command ``avn project ca-get --target-filepath ca.pem``.

.. topic:: Sample configuration

    .. code-block:: bash

        scrape_configs:
          - job_name: aivenmetrics
            scheme: https
            basic_auth:
              username: <PROMETHEUS_USERNAME>
              password: <PROMETHEUS_PASSWORD>
            tls_config:
              ca_file: ca.pem
            static_configs:
              - targets: ["<PROMETHEUS_SERVICE_URI>:<PROMETHEUS_SERVICE_PORT"]

.. topic:: Result

   With the configuration in place, Prometheus starts pulling metrics from your service.


Multi-node services
'''''''''''''''''''

1. For any service that consist of multiple nodes without a DNS name for each node, use the ``dns_sd_configs`` option to define the servers with DNS type set to ``A``.

.. topic:: Result
  
   Prometheus resolves all the IP addresses associated with the DNS name and query all of those IP addresses directly. A side effect of using this IP resolution is that Prometheus expects the TLS certificate to be bound to the IP addresses of the hosts, not to the DNS name.
   
2. Enable the ``insecure_skip_verify`` setting so that Prometheus wouldn't verify if the TLS certificate is bound to the IP addresses of the hosts.

   .. code-block:: bash

      scrape_configs:
        - job_name: aivenmetrics
          scheme: https
          basic_auth:
            username: <PROMETHEUS_USERNAME>
            password: <PROMETHEUS_PASSWORD>
          dns_sd_configs:
            - names:
                - <PROMETHEUS_SERVICE_URI>
              type: A
              port: <PROMETHEUS_SERVICE_PORT>
          tls_config:
            insecure_skip_verify: true

.. note::
  
   For Aiven for PostgreSQL® services with multiple nodes, the primary DNS name does not include standby IP addresses. To track those, make sure to include the replica DNS names in the list. If your ``<PROMETHEUS_SERVICE_URI>`` is ``example.aivencloud.com``, you need to add ``replica-example.aivencloud.com``.

View full list of metrics
''''''''''''''''''''''''''

Aiven provides the Prometheus client via the Telegraf plugin so all the same
metrics that are available via the Aiven for InfluxDB® metrics integration are also
available via the Prometheus integration.

You can preview the full list of metrics in :doc:`Prometheus system metrics </docs/integrations/prometheus-system-metrics>`.

.. note::
  
   For some services the metrics provided by different hosts may vary depending on the host role. Most notably for Kafka® only one of the nodes provides metrics related to consumer group offsets.

More integrations
-----------------

Learn more about integrations with Aiven:

* :doc:`Aiven integrations </docs/platform/concepts/service-integration>`
* :doc:`Datadog integration </docs/integrations/datadog>`
