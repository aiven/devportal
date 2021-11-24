Integration of logs into Apache Kafka topic
============================================

You can send logs from your Aiven services into a specified Apache Kafka topic. The setup can be done through `Aiven console <https://console.aiven.io>`_.

.. note::

    Note, the integration can be used for both Aiven for Apache Kafka, as well as external Kafka clusters registered in the project's service integrations page. Read more on :doc:`how to manage Aiven internal and external integrations </docs/tools/cli/service/integration>`.

In this example we'll show how to send the logs from an Aiven for PostgreSQL service to a topic in your Aiven for Apache
Kafka service. For this example you need:

-  a running Aiven for PostgreSQL service (we'll refer to it as *a source*)
-  a running Aiven for Apache Kafka service (we'll refer as *a destination*)

Setup Apache Kafka to receive the logs
---------------------------------------

Verify that Kafka REST API is enabled and create a Kafka topic where you want to receive the logs.

Add a new integration to the source service
-------------------------------------------

1. Navigate to the Aiven console overview page of the source PostgreSQL service.
2. Scroll the list of actions till you see **Service integrations**.
3. Click on **Manage Integrations**. A new pop up window will be displayed showing a list of available integrations for your service.
4. Select **Kafka Logs** from this list.
5. Select the destination Kafka service (or external Kafka integration) and the topic where the logs should be pushed.

Test the integration
--------------------

1. Go to the destination service overview page.
2. Open the destination topic you specified to send logs.
3. Navigate to the page with messages and press **Fetch Messages** to see the log entries that were sent from your source service.
4. Select **Decode from base64** to see messages in JSON format.

Edit or remove the integration
------------------------------

If you want to edit or remove the integration, use **Manage Integrations** in the source service. The created integration is listed in the **Enabled service integrations** section, from where you can edit or remove it.
