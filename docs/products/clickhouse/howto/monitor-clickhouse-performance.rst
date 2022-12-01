Monitor ClickHouse® metrics with Grafana®
=========================================

As well as offering ClickHouse®-as-a-service, the Aiven platform gives you access to monitor the database. The metrics/dashboard integration in the Aiven console lets you send ClickHouse® metrics to an external endpoint like Datadog or to create an integration and a :doc:`prebuilt dashboard <../reference/ch-metrics>` in Aiven for Grafana®. Get detailed information about the metrics and dashboard sections in :doc:`../reference/ch-metrics`.


Push ClickHouse® metrics to InfluxDB®, M3DB or ClickHouse®
----------------------------------------------------------

To collect metrics about your ClickHouse® service, you will need to configure a metrics integration and nominate somewhere to store the collected metrics.

1. On the service **Overview** page for your ClickHouse® service, go to **Manage Integrations** and choose the **Metrics** option with *Send service metrics to InfluxDB, M3DB or ClickHouse® service* as its description.

2. Choose either a new or existing InfluxDB®, M3DB or ClickHouse® service.

   - New service asks you to select the cloud, region and plan to use. Give your service a name. The service **Overview** page shows the nodes rebuilding and indicates when they are ready.
   - If you're already using InfluxDB, M3DB or ClickHouse® on Aiven, you can submit your ClickHouse® metrics to the existing service.

.. Warning::
    You can send your ClickHouse® service metrics to the same instance. This is not recommended since it increases the load on the monitored system and could also be affected in the event of problems with the database.

Provision and configure Grafana®
--------------------------------

1. Select the target InfluxDB, M3DB or ClickHouse® database service and go to its service page. Under **Manage Integrations**, choose the **Dashboard** option to make the metrics available on that platform.

2. Choose either a new or existing Grafana® service.
    - New service asks you to select the cloud, region and plan to use. Give your service a name. The service **Overview** page shows the nodes rebuilding and indicates when they are ready.
    - If you're already using Grafana® on Aiven, you can integrate your M3DB as an additional data source for that existing Grafana.

3. On the service **Overview** page for your Grafana® service, select the **Service URI** link. The username and password for your Grafana® service is also available on the service **Overview** page.

.. topic::

    Now your Grafana® service is connected to M3DB as a data source and you can go ahead and visualize your ClickHouse® metrics.

Open ClickHouse® metrics prebuilt dashboard
-------------------------------------------

1. In Grafana®, go to **Dashboards** > **Manage**.
2. Double click on the dashboard that bears the name of the metrics database.
3. Browse the prebuilt dashboard or create your own monitoring views.

.. seealso::

    For more information about the dashboard and pushed metrics, see :doc:`../reference/clickhouse-metrics`.

