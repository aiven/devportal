Integration of logs into Apache Kafka topic
============================================

You can send logs from your services into a specified Apache Kafka topic. The setup can be done through `Aiven console <https://console.aiven.io>`_.

.. note::

    Note, the integration can be used for both Aiven for Apache Kafka, as well as external Kafka clusters registered in the project's service integrations page.

In this example we'll show how to send the logs from an Aiven for PostgreSQL service to a topic in your Aiven for Apache
Kafka service. For this example you need:

-  a created and running Aiven for PostgreSQL service (we'll refer to it as *a source*)
-  a created and running Aiven for Apache Kafka service (we'll refer as *a destination*)

Prepare the destination to receive the logs
-------------------------------------------

In the Aiven for Apache Kafka overview page enable Kafka REST API and create a Kafka topic where you want to receive the logs.

Add a new integration to the source
-----------------------------------

Go to the overview page of your PostgreSQL service, scroll the list of actions till you see **Service integrations** and click on **Manage Integrations**. A new pop up window will be displayed showing a list of available integrations for your service. Select **Kafka Logs** from this list.

Follow the steps to select the destination service and the topic where you want to push the logs.

Test the integration
--------------------

Go to the destination service overview page. Open the destination topic you specified to send logs. Navigate to the page with messages and press **Fetch Messages** to see the log entries that were sent from your source service. Select **Decode from base64** to see messages in JSON format.

Edit or remove the integration
------------------------------

If you want to edit or remove the integration, use **Manage Integrations** in the source service. You'll see the created destination service in the list of **Enabled service integrations**, you can edit or remove it from here.
