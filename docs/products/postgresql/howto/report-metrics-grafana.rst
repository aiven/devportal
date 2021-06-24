Monitor PostgreSQL Metrics with Grafana
=======================================

As well as offering PostgreSQL-as-a-service, the Aiven platform gives you access to monitor the database. The metrics/dashboard integration in the Aiven console lets you send PostgreSQL metrics to an external endpoint like DataDog or to create an integration and a :doc:`prebuilt dashboard <../reference/pg-metrics>` in Aiven for Grafana. Get detailed information about the metrics and dashboard sections in :doc:`../reference/pg-metrics`.


Push PostgreSQL Metrics to InfluxDB, M3DB or PostgreSQL
-------------------------------------------------------

To collect metrics about your PostgreSQL service you will need to configure a metrics integration and nominate somewhere to store the collected metrics.

1. On the service overview page for your PostgreSQL service, go to "Manage Integrations" and choose the "Metrics" option with "**Send** service metrics to InfluxDB, M3DB or PostgreSQL service" as its description.

2. Choose either a new or existing InfluxDB, M3DB or PostgreSQL service.

   - A new service will ask you to select the cloud, region and plan to use. You should also give your service a name. The service overview page shows the nodes rebuilding, and then indicates when they are ready.
   - If you're already using InfluxDB, M3DB or PostgreSQL on Aiven, you can submit your PostgreSQL metrics to the existing service.

.. Warning::
    You can send your PostgreSQL service metrics to the same instance. This is not recommended since it increases the load on the monitored system and could also be affected in the event of problems with the database.

Provision and Configure Grafana
-------------------------------

3. Select the target InfluxDB, M3DB or PostgreSQL database service and go to its service page. Under "Manage Integrations", choose the "Dashboard" option to make the metrics available on that platform.

4. Choose either a new or existing Grafana service.
    - A new service will ask you to select the cloud, region and plan to use. You should also give your service a name. The service overview page shows the nodes rebuilding, and then indicates when they are ready.
    - If you're already using Grafana on Aiven, you can integrate your M3DB as an additional data source for that existing Grafana.

5. On the service overview page for your Grafana service, click the "Service URI" link. The username and password for your Grafana service is also available on the service overview page.

Now your Grafana service is connected to M3DB as a data source and you can go ahead and visualize your PostgreSQL metrics.

Open Aiven PostgreSQL Metrics Prebuilt Dashboard
------------------------------------------------

In Grafana, go to "Dashboards" and "Manage" and double click on the Aiven PostgreSQL Resources dashboard that bears name of the metrics database.

.. image:: /images/products/postgresql/metrics-dashboard-manage.png
   :alt: Screenshot of a Grafana Manage Dashboards panel

Browse the prebuilt dashboard or create your own monitoring views. More info about the dashboard and pushed metrics can be found at :doc:`../reference/pg-metrics`

.. image:: /images/products/postgresql/metrics-dashboard-global.png
   :alt: Screenshot of the PostgreSQL Metrics Dashboard for Grafana
