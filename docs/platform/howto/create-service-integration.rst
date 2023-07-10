Create a service integration
============================

If you're not sure what a service integration is, see :doc:`Service integration <../concepts/service-integration>` for an overview. This article will guide you on how to create service integrations between different Aiven services and move telemetry data using these integrations.

Prerequisites
-------------

To get started, you need three services:

- Service that produces the telemetry data. We're using an Aiven for Apache Kafka® service in our example, but this could be one of the other Aiven services available.
- Aiven for PostgreSQL® - Database where the telemetry data is stored and can be queried from
- Aiven for Grafana® - Dashboards for the telemetry data

Create an integration
---------------------

1. In `Aiven Console <https://console.aiven.io/>`_, :doc:`create the new services: <create_new_service>` Aiven for Apache Kafka®, Aiven for PostgreSQL®, and Aiven for Grafana®. You can choose your preferred cloud provider, region, and any plan from **startup** / **business** / **premium**.  

2. Once all three services are running in `Aiven Console <https://console.aiven.io/>`_, select the Aiven for PostgreSQL service from the **Services** page, and make sure the **Overview** page of your service is open. On the **Overview** page, go to **Service integrations** > **Manage integrations** > **Aiven solutions** > **Monitor Data in Grafana**. In the **Datasource integration** window, make sure the **Existing service** radio button is highlighted, and select the newly created Aiven for Grafana service. Select **Enable**.

3. Enable receiving metrics from the Aiven for Apache Kafka service. On the **Overview** page of your Aiven for PostgreSQL service, go to **Service integrations** > **Manage integrations** > **Aiven solutions** > **Receive Metrics**. In the **Metrics integration** window, make sure the **Existing service** radio button is highlighted, and select the newly created Aiven for Apache Kafka service. Select **Enable**.

   .. note::
   
      You have now the advanced Aiven for Apache Kafka telemetry data flowing to the Aiven for PostgreSQL service.

4. Open the Grafana dashboard to see the Aiven for Apache Kafka metrics data.

   1. In `Aiven Console <https://console.aiven.io/>`_, select your Aiven for Grafana servie from the **Services** view.
   2. In the **Overview** page of your service, navigate to the **Connection information** section.
   3. Use **Service URI** from the **Connection information** section to access the Grafana service in your browser. To log in, use the credentials available in the the **Connection information** section (the ``avnadmin`` user and the password).

.. note::
   
   If you cannot see a dashboard after logging in, search for a dashboard from the top-left corner in the Grafana console to find dashboard ``Aiven Kafka - <YOUR_KAFKA_SERVICE_NAME> - Resources``. 

   This dashboard is a predefined view that is automatically maintained by Aiven.
   
   .. note::
      
      It may take a minute to start getting data into to the dashboard view if you just enabled the integrations. The view can be refreshed by reloading in the top-right corner. You can add custom dashboards by either defining them from scratch in Grafana or by saving a copy of the predefined dashboard under a different name that does not start with *Aiven*.

.. warning::

    Any changes that you make to the predefined dashboard are eventually automatically overwritten by the system.
