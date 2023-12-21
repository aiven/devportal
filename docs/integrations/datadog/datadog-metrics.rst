Send metrics to Datadog
=======================

This guide will show you how to send metrics from your Aiven service to your Datadog account.

Prepare your Datadog account
----------------------------

Before you begin, ensure that you have the following details ready:

* Determine whether your Datadog account is located in the US or EU region.

* A Datadog API key. Generate an API key for your Datadog account by visiting the **Organization settings** in your account menu. Select **API Keys** and then select **New Key** to obtain the API key. Make sure to copy this key, as you will need it shortly.


Configure the service integration endpoint
-------------------------------------------

This section needs to be completed only once for each Datadog account you intend to use. Afterward, multiple services can use this service integration endpoint.

1. Log in to the `Aiven Console <https://console.aiven.io/>`_. 
2. In the **Services** screen, select **Integration endpoints** on the left sidebar. 
3. Select **Datadog** and then select **Add new endpoint** or **Create new**.
4. Configure the endpoint by providing a name for this integration and entering the API key you copied earlier. Ensure that the correct region is selected.

.. image:: /images/integrations/configure-datadog-service-integration.png
   :alt: Screenshot of the Datadog configuration screen

5. Optionally, include additional tags that will be used when sending metrics to Datadog. Refer to :doc:`Add custom tags Datadog integration </docs/integrations/datadog/add-custom-tags-to-datadog>` to learn more about adding tags to the Datadog integration. You can always add or edit tags later.
6. Select **Add endpoint** to save this configuration.

Add Datadog metrics integration to your Aiven service
-----------------------------------------------------

To enable the Datadog metrics integration for each service that requires metric tracking in Datadog, follow these steps:

1. In the `Aiven Console <https://console.aiven.io/>`_, select your service. 
2. From the **Overview** page of your service, scroll to **Service integrations** and select **Manage integrations**. 
3. In the **Integrations** screen, select **Datadog Metrics**.

4. Select the Datadog endpoint you want to use from the drop-down list and select **Enable**.

.. Tip::

    If you're using Aiven for Apache Kafka® you can also :doc:`customise the metrics sent to Datadog </docs/products/kafka/howto/datadog-customised-metrics>`.

5. Return to your Datadog dashboard and after a few minutes, you should see the data start to arrive from your Aiven service(s).

.. seealso:: 
    - Learn more about :doc:`/docs/integrations/datadog`.
    - For information on how to enable `Datadog Deep Database Monitoring <https://www.datadoghq.com/product/database-monitoring/>`_ for specific Datadog Metrics integration, see :doc:`Database monitoring with Datadog </docs/products/postgresql/howto/monitor-database-with-datadog>`. 
