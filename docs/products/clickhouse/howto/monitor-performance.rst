Monitor Aiven for ClickHouse® metrics with Grafana®
===================================================

As well as offering ClickHouse®-as-a-service, the Aiven platform gives you access to monitor the database. The metrics/dashboard integration in the Aiven console allows you to create an integration and monitoring dashboards in Aiven for Grafana®. For more information on the metrics, see :doc:`Aiven for ClickHouse® metrics exposed in Aiven for Grafana® <../reference/metrics-list>`.

Push ClickHouse® metrics to InfluxDB®, M3DB, or PostgreSQL
----------------------------------------------------------

To collect metrics about your ClickHouse® service, you will need to configure a metrics integration and nominate somewhere to store the collected metrics.

1. On the service **Overview** page for your ClickHouse® service, go to **Manage Integrations** and choose the **Metrics** option with *Send service metrics to InfluxDB, M3DB or PostgreSQL service* as its description.

2. Choose either a new or existing InfluxDB®, M3DB, or PostgreSQL service.

   - If you choose to use a new service, follow instructions on :doc:`how to create a service </docs/platform/howto/create_new_service>`.
   - If you're already using InfluxDB, M3DB, or PostgreSQL on Aiven, you can submit your ClickHouse® metrics to the existing service.

Provision and configure Grafana®
--------------------------------

1. Select the target InfluxDB, M3DB, or PostgreSQL database service and go to its service page. Under **Manage Integrations**, select **Dashboard** to make the metrics available on that platform.

2. Choose either a new or existing Grafana® service.

   - If you choose to use a new service, follow instructions on :doc:`how to create a service </docs/platform/howto/create_new_service>`.
   - If you're already using Grafana® on Aiven, you can integrate your M3DB as an additional data source for that existing Grafana.

3. On the service **Overview** page for your Grafana® service, select the **Service URI** link. The username and password for your Grafana® service is also available on the same page.

Now your Grafana® service is connected to InfluxDB, M3DB, or PostgreSQL as a data source and you can go ahead and visualize your ClickHouse® metrics.

Open ClickHouse® metrics dashboard
----------------------------------

1. In Grafana®, go to **Dashboards** > **Manage**.
2. Double click on the dashboard that bears the name of the metrics database.
3. Browse the prebuilt dashboard or create your own monitoring views.
