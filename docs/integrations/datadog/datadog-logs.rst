Send logs to Datadog
====================

This article will show you how to use the Aiven Rsyslog integration to send the logs from your Aiven services to Datadog.

You will need:

* A Datadog account, and which region it is in.

* A Datadog API key. Generate an API key by visiting **Organization settings** under your account menu, and then choose **API Keys**. The **New Key** button will give you an API key; you should copy this as you will need it shortly.

* An Aiven account with a project set up. You'll need the name of the project.


Configure the integration
-------------------------

Start by configuring the link between Aiven and Datadog for logs. This setup only needs to be done once.

1. Click **Integration endpoints** in the web console, then **Syslog** and **Add a new endpoint**.

2. Configure the settings for the new endpoint:

   * **Endpoint name** is how you will refer to this logs integration when linking it to other Aiven services

   * **Server** and **Port** (leave TLS enabled):

     - For region USA use ``intake.logs.datadoghq.com`` and ``10516``
     - For region EU use ``tcp-intake.logs.datadoghq.eu`` and ``443``

   * **Format** set to "custom"

3. Configure the **Log Template** field. You will need to replace the following values:

.. list-table::
  :header-rows: 1

  * - Variable
    - Description
  * - ``DATADOG_API_KEY``
    - From your Datadog account settings
  * - ``AIVEN_PROJECT_NAME``
    - Found in the web console

This is the format to use, replacing the variables listed. Don't edit the values surrounded by ``%`` signs, such as ``%msg%`` as these are used in constructing the log line::

   DATADOG_API_KEY <%pri%>1 %timestamp:::date-rfc3339% %HOSTNAME%.AIVEN_PROJECT_NAME %app-name% - - - %msg%

An example of the correct format, using an example API key and "my_project" as the project name:

``01234567890123456789abcdefabcdef <%pri%>1 %timestamp:::date-rfc3339% %HOSTNAME%.my_project %app-name% - - - %msg%``

.. note::  Metrics and logs are correlated in Datadog by hostname. The metrics integration is currently configured to append the project name to the hostname in order to disambiguate between services that have the same name in different projects. Adding the project name to the hostname in the syslog integration to Datadog assures that they can be correlated again in the Datadog dashboard. Not doing so will not result in missing logs, but the logs that appear in Datadog will miss tags that come from this correlation with the metrics. See https://docs.datadoghq.com/integrations/rsyslog.


4. Save the settings.

Send logs from an Aiven service to Datadog
------------------------------------------

Follow the steps in this section for each of the services whose logs should be sent to Datadog.

4. From the **Service Overview** page, select **Manage integrations** and choose the **Rsyslog** option.

.. image:: /images/integrations/rsyslog-service-integration.png
   :alt: Screenshot of system integrations including rsyslog

5. Pick the log integration you created earlier from the dropdown and choose **Enable**.

6. Visit Datadog and look under "Logs" to see the data flowing within a few minutes.

.. seealso:: Learn more about :doc:`/docs/integrations/datadog`.

