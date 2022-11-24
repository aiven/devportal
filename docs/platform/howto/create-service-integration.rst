Create a service integration
============================

If you're not sure what a service integration is, follow :doc:`this guide <../concepts/service-integration>` for an overview. This article will guide you on how to create service integrations between different Aiven services and move telemetry data using these integrations. To get started, you will need three services:

- Aiven for Apache Kafka® - The service that produces the telemetry data
- Aiven for PostgreSQL® - Database where the telemetry data is stored and can be queried from
- Aiven for Grafana® - Dashboards for the telemetry data

.. note::

    Currently these services need to be running in the same Aiven project, but this limitation will be removed in the future and you will be able to, for example, connect multiple Aiven for Apache Kafka® services from different projects to the same PostgreSQL® and Grafana® instances.

Steps:

1. From the Aiven console, follow :doc:`this guide <create_new_service>` to create three new services - Aiven for Apache Kafka®, Aiven for PostgreSQL®, and Aiven for Grafana®. You can choose your preferred cloud provider, region, and any plan from **startup** / **business** / **premium**.  

2. Once all three services are running, navigate to the PostgreSQL service on the Aiven console and click on **Service integrations** from the **Overview** page. Click **Use integration** button for the *Grafana Metrics Dashboard* card. The **Existing service** radio button should be highlighted next and you can choose the newly create Grafana service.

   Next, click **Enable**.

3. Now, let's enable receiving metrics from the Kafka service. While still on the same PostgreSQL service integration screen, click **Use integration** button for *Metrics*. 

4. That is all that is needed to get the advanced Kafka telemetry data flowing to the PostgreSQL service! Close the service integrations dialog by pressing the **Close** button.

5. Open the Grafana dashboard to see the Kafka metrics data. In order to do that, navigate to the Grafana service overview page and look under *Connection information*. Use the ``avnadmin`` user and the password to access the Grafana service found in the **Service URI**. If you don't see a dashboard after logging in, search for a dashboard from the top-left corner on the Grafana console and you'll find a dashboard named ``Aiven Kafka - <YOUR_KAFKA_SERVICE_NAME> - Resources``. 

   This dashboard is a predefined view that is automatically maintained by Aiven. Note that it may take a minute to start getting data into to the dashboard view if you just enabled the integrations. The view can be refreshed by pressing the reload button at the top-right corner. You can add custom dashboards by either defining them from scratch in Grafana or by saving a copy of the predefined dashboard under a different name that does not start with "Aiven".

.. warning::

    Any changes that you make to the predefined dashboard will eventually be automatically overwritten by the system.
