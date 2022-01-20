Using Aiven with Prometheus
===========================

.. _h_6a84674413:

Background
----------

Prometheus is an open-source systems monitoring and alerting toolkit. It
implements in-memory and persistent storage model for metrics as well as
a query language for accessing the metrics.

The metrics delivery model of Prometheus is a somewhat atypical pull
model where the Prometheus server connects to HTTP servers running on
the nodes being monitored and pulls the metrics from them. While this
makes the service discovery more of an issue than with the more common
push approach, it does have the benefit of making the metrics available
not just for Prometheus but for any app that can read the Prometheus
format from the HTTP server running on Aiven nodes.

Enabling Prometheus support in Aiven
------------------------------------

To enable the metrics endpoints that Prometheus can query you need to
follow the steps below:

#. | Navigate to the project ``Service Integrations`` section from the
     side menu

#. | Add a ``Prometheus`` integration endpoint if one does not already
     exist.

   | Usually you only need one of these per project (as it can be used
     for all services in the same project) so if you can see one has
     already been created then you can skip this step.

#. | Navigate to your service that you
     would like to monitor and click ``Manage integrations``

#. | Choose the ``Prometheus`` service integration by clicking
     ``Use integration``

#. | Confirm you have selected the Prometheus endpoint configured
     earlier in Step 2 and click ``Enable``

   .. image:: /images/platform/integrations/prometheus-endpoint-select.png
      :alt: Dialog box to select already configured Prometheus endpoints

#. | Check the service overview page to see that the integration has
     been successfully enabled and is now ``Active``

#. | Copy the Prometheus connection information found from the top of
     the service overview page under the new ``Prometheus`` tab

   .. image:: /images/platform/integrations/prometheus-service-info.png
      :alt: Screenshot of Prometheus connection information in service overview page



After finishing these steps, the system will start an HTTP server on all
nodes of the service that provide access to the metrics. Note that there
can be roughly one minute delay until the metrics are available.

Often the users have VPC enabled in their projects. If this was the
case, the property **public_access.prometheus** needs to be enabled in
the Advanced Configurations of the service. In this way it becomes
possible to access metrics by using the public hostname.

Configuring your Prometheus server
-----------------------------

To make Prometheus fetch metrics from Aiven servers you'll need to add a
new scrape configuration with appropriate basic auth parameters (as seen on the
Service Integrations page) and identify the servers to pull data from.

For Services with multiple nodes
'''''''''''''''''''''''''''''''''''''''''

For any services that consist of multiple nodes and each node doesn't
have its own unique DNS name, you need to use the ``dns_sd_configs``
option for defining the servers with DNS type set to ``A`` . This causes
Prometheus to resolve all the IP addresses associated with the DNS name
and query all of those IP addresses directly. A side effect of using
this IP resolution is that Prometheus expects the TLS certificate to be
bound to the IP address of the hosts, not to the DNS name, so to make
the connection work you must enable the ``insecure_skip_verify``
setting. See the below snippet for an example configuration.

::

   scrape_configs:
     - job_name: aivenmetrics
       scheme: https
       basic_auth:
         username: <PROMETHEUS_USERNAME>
         password: <PROMETHEUS_PASSWORD>
       dns_sd_configs:
         - names:
             - <SERVICE_URI>
           type: A
           port: 9273
       tls_config:
         insecure_skip_verify: true


For services with a single node
'''''''''''''''''''''''''''''''''''

For services where a DNS name resolves to only single node using
``static_configs`` instead of ``dns_sd_configs`` may be preferable as it
allows doing all the regular certificate checks. Do note, however, that
the certificate provided by the Aiven servers is signed by the
Aiven project CA instead of a generally trusted CA and you must set the
``ca_file`` setting under ``tls_config`` to point to that file. For most
services it can be downloaded from the service overview page in Aiven
web console or alternatively the `Aiven command line
client <https://github.com/aiven/aiven-client/>`_ can be used (
``avn project ca-get --target-filepath TARGET_FILEPATH`` ). The file is
identical for all services in the same project.

View full list of metrics
''''''''''''''''''''''''''

Aiven provides the Prometheus client via the Telegraf plugin so all the same
metrics that are available via the Aiven InfluxDB metrics integration are also
available via the Prometheus integration. You can see the full list of metrics `here
<https://help.aiven.io/en/articles/5144867-aiven-service-metrics>`_.

.. note:: Note that for some services the metrics provided by different hosts may vary depending on the host role. Most notably for Kafka only one of the nodes provides metrics related to consumer group offsets.

Accessing Prometheus in a VPC
''''''''''''''''''''''''''''''

Often the users have VPC enabled in their projects. If this was the case, the
property ``public_access.prometheus`` needs to be enabled in the Advanced
Configurations of the service.

.. image:: /images/platform/integrations/prometheus-advanced-configurations.png
    :alt: Advanced configuration for accessing Prometheus in a VPC

Further Reading:
----------------------------------------

* `Aiven M3DB & Grafana integration <https://help.aiven.io/services/integrations/getting-started-with-service-integrations>`_

* `Datadog integration <https://help.aiven.io/services/integrations/getting-started-with-datadog>`_