Send metrics to Datadog
=======================

This guide will show you how to send metrics from your Aiven service to your Datadog account.

Prepare your Datadog account
----------------------------

You will need a Datadog account and the following details handy:

* Which region your Datadog account is in, US or EU.

* A Datadog API key. Generate an API key by visiting **Organization settings** under your account menu, and then choose **API Keys**. The **New Key** button will give you an API key; you should copy this as you will need it shortly.

Configure the service integration
---------------------------------

This section need only be completed once for each Datadog account you wish to use. Multiple services can then use this service integration.

1. In the Aiven web console, click **Service Integrations** in the left hand menu. Select **Datadog** and then **Add new endpoint**.

2. Configure the endpoint by adding a name for this integration, and the API key you copied earlier. Check that the correct region is selected.

.. image:: /images/integrations/configure-datadog-service-integration.png
   :alt: Screenshot of the Datadog configuration screen

3. *(optional)* Add any additional tags that should be used when sending metrics to Datadog. You can `learn more about sending tags to Datadog in our guide <https://help.aiven.io/en/articles/5372887-adding-custom-tags-to-your-datadog-integration-in-the-aiven-web-console>`_ and these can also be added or edited later.

4. Choose **Add endpoint** to save this configuration.

Add Datadog metrics integration to your Aiven service
-----------------------------------------------------

Repeat these steps for each service whose metrics should be sent to Datadog.

5. Open the service overview page, and choose **Manage integrations**. Then choose the **Datadog** integration.

6. From the list, choose which Datadog integration to use, then select **Enable**.

.. Tip::

    If you're using Aiven for Apache Kafka® you can also :doc:`customise the metrics sent to Datadog </docs/product/kafka/howto/datadog-customised-metrics>`

7. Return to your Datadog dashboard and after a few minutes, you should see the data start to arrive from your Aiven service(s).

.. seealso:: Learn more about :doc:`/docs/integrations/datadog/index`.
