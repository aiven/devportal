Manage OpenSearch® log integration
==================================

Aiven provides a service integration that allows you to send your logs from several services, such as Aiven for Apache Kafka®, PostgreSQL®, Apache Cassandra®, OpenSearch®, Redis®*, InfluxDB®, and Grafana®, to Aiven for OpenSearch®. Making it possible for you to use OpenSearch to gain more insight and control over your logs.

In this article, you will understand how to enable, edit and disable the logs integration feature on Aiven for OpenSearch®. 

.. tip::

   Check a short `video tutorial <https://www.youtube.com/watch?v=f4y9nPadO-M>`_ for an end-to-end example of how to enable your Aiven for OpenSearch® log integration.

Enable log integration
----------------------

Here are the steps needed to enable logs integration. This allows you to send your service's logs to your Aiven for OpenSearch® from another Aiven service.

1. Log in to the `Aiven Console <https://console.aiven.io/>`_, and select the Aiven for OpenSearch service for which you want to enable log integration. 

2. Select **Logs** from the left sidebar, and select **Enable logs integration**.

3. Select an existing OpenSearch instance or create a new one, then select **Continue**.
    - When creating a new service you will need to select the cloud, region and plan to use. You should also give your service a name. The service overview page shows the nodes rebuilding, and then indicates when they are ready.
    - If you're already using OpenSearch on Aiven, you can use your running OpenSearch service as a destination for your metrics data. If you are a member of more than one Aiven project with *operator* or *admin* access rights, you need to choose the project first then your target OpenSearch service.

4. Configure your ``index prefix`` and ``index retention limit`` parameters, then select **Enable**.

.. note::
    If you want to effectively disable the ``index retention limit``, you can set it to the maximum value which is 10000 days.

Your Aiven service is now sending logs to your OpenSearch service which you can explore further.

Configure log integration
-------------------------

There are two parameters that you can adjust when integrating logs to your OpenSearch service:

* ``index prefix``, specifies the prefix part of the index name
* ``index retention limit``, number of days to preserve the daily indexes

.. warning::
    
    The service's logs are sent from the selected service to your OpenSearch cluster. When the ``index retention limit`` is reached, those indexes are deleted from the OpenSearch cluster.


You can change the configuration of the ``index prefix`` and ``index retention limit`` after the integration is enabled.

1. Log in to the `Aiven Console <https://console.aiven.io/>`_, and select the Aiven for OpenSearch service.
2. Click **Integrations** on the sidebar.
3. Identify the service you want to configure in the Integrations page.
4. Click **Actions** (**...**) menu, select **Edit** to modify the necessary parameters.
5. After making the changes, click **Edit** again to save them.


Disable logs integration
------------------------

If you no longer wish to send logs from your service to OpenSearch, follow these steps to disable the integration:

1. In your Aiven for OpenSearch service, navigate to the **Integrations** screen using the left sidebar and locate the service you want to modify.
2. From the **Actions** (**...**) menu, select **Disconnect** to proceed with disabling the integration.
3. In the confirmation window, click **Disconnect** again to confirm and save the changes.

Your log integration for OpenSearch will be disabled. 
