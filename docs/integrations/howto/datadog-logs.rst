Send logs to DataDog
====================

This article will show you how to use the Aiven Rsyslog integration to send the logs from your Aiven services to DataDog.

You will need:

* A DataDog account.

* The region to use, US or EU

* A DataDog API key. Generate an API key by visiting **Organization settings** under your account menu, and then choose **API Keys**. The **New Key** button will give you an API key; you should copy this as you will need it shortly.


Configure the integration
-------------------------

Start by configuring the link between Aiven and DataDog for logs. This setup only needs to be done once.

1. Choose **Service integrations** in the left hand menu of the web console, then choose **Syslog** and **Add a new endpoint**.

.. image:: /images/integrations/configure-rsyslog-integration-datadog.png
   :alt: Screenshot of configuration screen for rsyslog

2. Configure the settings for the new endpoint:

   * **Endpoint name** is how you will refer to this logs integration when linking it to other Aiven services

   * **Server** and **Port** (leave TLS enabled):

     - For region USA use ``intake.logs.datadoghq.com`` and ``10516``
     - For region EU use ``tcp-intake.logs.datadoghq.eu`` and ``443``

   * **Format** set to "custom"

   * **Log Template** should be set as follows, but edited to include your actual ``DATADOG_API_KEY`` and ``AIVEN_PROJECT_NAME``:

::

   DATADOG_API_KEY <%pri%>1 %timestamp:::date-rfc3339% %HOSTNAME%.AIVEN_PROJECT_NAME %app-name% - - - %msg%

3. Save the settings.

Send logs from an Aiven service to DataDog
------------------------------------------

Follow the steps in this section for each of the services whose logs should be sent to DataDog.

4. From the **Service Overview** page, select **Manage integrations** and choose the **Rsyslog** option.

.. image:: /images/integrations/rsyslog-service-integration.png
   :alt: Screenshot of system integrations including rsyslog

5. Pick the log integration you created earlier from the dropdown and choose **Enable**.

6. Visit DataDog and look under "Logs" to see the data flowing within a few minutes.

.. seealso:: Learn more about :doc:`/docs/integrations/concepts/datadog`.

