Send metrics to DataDog
=======================

This guide will show you how to send metrics from your Aiven service to your DataDog account.

Prepare your DataDog account
----------------------------

You will need a DataDog account and the following details handy:

* Which region you want to use, US or EU

* An API key for this integration. Generate an API key by visiting **Organization settings** under your account menu, and then choose **API Keys**. The **New Key** button will give you an API key; you should copy this as you will need it shortly.

Configure the service integration
---------------------------------

This section need only be completed once for each DataDog account you wish to use. Multiple services can then use this service integration.

1. In the Aiven web console, click **Service Integrations** in the left hand menu. Select **DataDog** and then **Add new endpoint**.

2. Configure the endpoint by adding a name for this integration, and the API key you copied earlier. Check that the correct region is selected.

.. image:: /images/integrations/configure-datadog-service-integration.png
   :alt: Screenshot of the DataDog configuration screen

3. *(optional)* Add any additional tags that should be used when sending metrics to DataDog. You can `learn more about sending tags to DataDog in our guide <https://help.aiven.io/en/articles/5372887-adding-custom-tags-to-your-datadog-integration-in-the-aiven-web-console>`_ and these can also be added or edited later.

4. Choose **Add endpoint** to save this configuration.

Add DataDog metrics integration to your Aiven service
-----------------------------------------------------

Repeat these steps for each service whose metrics should be sent to DataDog.

5. Open the service overview page, and choose **Manage integrations**. Then choose the **DataDog** integration.

6. From the list, choose which DataDog integration to use, then select **Enable**.

7. Return to your DataDog dashboard and after a few minutes, you should see the data start to arrive from your Aiven service(s).

.. seealso:: Learn more about :doc:`/docs/integrations/concepts/datadog`.
