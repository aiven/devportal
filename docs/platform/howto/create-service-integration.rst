Create service integrations
============================

If you're not sure what a service integration is, see :doc:`Service integration </docs/platform/concepts/service-integration>` for an overview. This article will guide you on how to create service integrations between different Aiven services and move telemetry data using these integrations.

Prerequisites
-------------

To get started, you need three services:

- Service that produces the telemetry data. We're using an Aiven for Apache Kafka® service in our example, but this could be one of the other Aiven services available.
- Aiven for PostgreSQL® - Database where the telemetry data is stored and can be queried from
- Aiven for Grafana® - Dashboards for the telemetry data

Create an integration
---------------------

1. In the `Aiven Console <https://console.aiven.io/>`_, :doc:`create new services <create_new_service>` including Aiven for Apache Kafka®, Aiven for PostgreSQL®, and Aiven for Grafana®. Choose your preferred cloud provider, region, and a plan from **startup**, **business**, or **premium**.

2. Once all three services are running in the `Aiven Console <https://console.aiven.io/>`, select the Aiven for PostgreSQL service from the **Services** page. Ensure you are on the **Overview** page of your service. 
   
   a. Select to **Integrations**  from the sidebar. 
   b. Under  **Aiven solutions**, click **Monitor Data in Grafana**. 
   c. In the **Datasource integration** window, select the **Existing service** radio button and choose the Aiven for Grafana service you created.
   d. Click **Enable**.

3. To enable metrics from the Aiven for Apache Kafka service, go to the **Overview** page of your Aiven for PostgreSQL service. 
   
   a. Select **Service integrations** from the sidebar. 
   b. Under **Aiven solutions**, select **Receive Metrics**. 
   c. In the **Metrics integration** window, ensure the **Existing service** radio button is selected and choose the Aiven for Apache Kafka service.
   d. Click **Enable**.

   .. note::
   
      This step allows advanced Aiven for Apache Kafka telemetry data to flow into the Aiven for PostgreSQL service.

4. To view the Aiven for Apache Kafka metrics data in Grafana:

   a. In the `Aiven Console <https://console.aiven.io/>`_, select your Aiven for Grafana service from the **Services** page.
   b. In the **Connection information** section on the service **Overview** page, copy the **Service URI** from the **Connection information** to access the Grafana service in your browser. 
   c. Log in using the credentials provided in the **Connection information** section (the ``avnadmin`` user and the password).

.. note::
   
   If you don't see a dashboard after logging in, search for ``Aiven Kafka - <YOUR_KAFKA_SERVICE_NAME> - Resources`` from the top-left corner in the Grafana console. This is a predefined dashboard automatically maintained by Aiven.
   
.. note::
      
   Data may take a minute to appear on the dashboard if you've just enabled the integrations. Refresh the view by reloading the page from the top-right corner. You can create custom dashboards either from scratch in Grafana or by saving a copy of the predefined dashboard under a different name that does not start with *Aiven*.

.. warning::

   Any modifications to the predefined dashboard will be automatically overwritten by the system in time.
