Manage OpenSearch log integration
==================================

Aiven provides a service integration that allows you to send your logs from several services, such as Aiven for Kafka, PostgreSQL, Cassandra, OpenSearch, Redis, InfluxDB, and Grafana, to Aiven for OpenSearch. Making it possible for you to use OpenSearch to gain more insight and control over your logs. 

In this article, you will understand how to enable, edit and disable the logs integration feature on Aiven for OpenSearch.

Enable logs integration
-----------------------

Here are the steps needed to enable logs integration. This allows you to send logs to your Aiven for OpenSearch from another Aiven service.

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. On the **Services** page, scroll down and choose **Service integrations**.

3. On the **Logs** tab, click on **Use Integration**. 

4. Select an existing OpenSearch instance or create a new one, then select **Continue**.

5. Configure your ``index prefix`` and ``index retention limit`` parameters, then select **Enable**

.. note::
    If you want to effectively disable the ``index retention limit``, you can set it to the maximum value which is 10000 days.

Your Aiven service is now sending logs to your OpenSearch service which you can explore further.

Logs integration configuration
------------------------------
There are two parameters that you can adjust when integrating logs to your OpenSearch service:

* ``index prefix``, specifies the prefix part.
* ``index retention limit``, number of days to preserve the daily indexes.

.. warning::
    
    The logs are sent once per day from the selected service to your OpenSearch cluster. When the ``index retention limit`` is reached, those indexes are deleted from the OpenSearch cluster.


Change logs integration configuration
'''''''''''''''''''''''''''''''''''''

You can change the configuration of the ``index prefix`` and ``index retention limit`` after the integration is enabled.

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. On the **Overview** page, scroll down to the **Service integrations**.

3. Click on **Manage integrations**.

4. On the **Enabled service integrations** list, find the service to disable the integration.

5. Click on **Edit** button, and edit the parameters.

6. Once the parameters are chosen, click in **Edit**

Your logs parameters should be updated after those steps.

Disable logs integration
------------------------

In case, you are no longer interested in sending the logs from your service to OpenSearch, follow those steps to disable the integration:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. On the *Overview* page, scroll down to the **Service integrations**.

3. Click on **Manage integrations**.

4. On the **Enabled service integrations** list, find the service to disable the integration.

5. Click on **Delete** button.

Your log integration for OpenSearch should be successfully disabled after those steps.