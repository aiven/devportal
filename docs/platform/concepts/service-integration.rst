Service integration
===================

Service integrations provide additional functionality and features by connecting different Aiven services together. 
This includes metrics integration which enables Aiven users to send advanced telemetry data to an `Aiven for PostgreSQL <https://aiven.io/postgresql>`_ database for metrics and visualize it in `Aiven for Grafana® <https://aiven.io/grafana>`_.
In addition to the metrics integration, log integration is supported that allows sending logs from any Aiven service to `Aiven for OpenSearch® <https://aiven.io/opensearch>`_.


Benefits of integrated telemetry 
--------------------------------

Aiven automatically provides basic host-level resource metrics (CPU, memory, disk and network) for every service under the **Metrics** tab on the Aiven web console. 

The advanced telemetry feature brings much more detailed, service-specific metrics to the Aiven user, who can then drill down into the service behavior and identify issues and performance bottlenecks.

Frequently asked questions on Aiven service integration
-------------------------------------------------------

**How are the service integrations billed? Does it cost something extra?**

The advanced telemetry data and predefined dashboards do not cost anything extra, but they require you to have an Aiven for PostgreSQL® and an Aiven for Grafana® service, which will be billed hourly as regular Aiven services.

**Can I define my own metrics dashboards?**

Yes. You can use the predefined dashboards as a starting point and save them under a different name or you can build one from scratch. Dashboards whose title starts with the word "Aiven" are automatically managed, so it is better to name the dashboards differently from that.

**Can I access the telemetry data directly in PostgreSQL?**

Yes. The PostgreSQL service is a normal PostgreSQL database service that can be accessed via any PostgreSQL client software or your own application or script. You can perform complex queries over the data and so on.

**Can I add alerts in Grafana for the telemetry data?**

Yes. You can add alert thresholds for individual graphs and attach different alerting mechanisms to them for sending out alerts. Please refer to the :doc:`Grafana documentation <../../products/grafana>` for more information.

Create a service integration
-----------------------------

Follow :doc:`this guide <../howto/create-service-integration>` to create service integration between multiple Aiven services.

