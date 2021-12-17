OpenSearch alerting
===================

OpenSearch alerting feature sends notifications when data from one or more indices meets certain conditions that can be customized.
Use case examples are such as monitoring for HTTP status code 503, CPU load average above certain percentage or watch for counts of a specific keyword in logs for a specific amount of interval,
notification to be configured to be sent via email, slack or webhooks and other destination.

In the following example, we are using a ``sample-host-health`` index as datasource to create a simple alert to check cpu load, action will be triggered when average of ``cpu_usage_percentage`` over ``3`` minutes is above ``75%``

You can define an alert either by using visual interface or programmatically.

Create using Dashboards UI
**************************

In order to create an alert via OpenSearch Dashboards interface, follow these steps:

1. Log in to the `Aiven web console <https://console.aiven.io>`_ and select your OpenSearch service.

2. Click the **Overview** tab -> **OpenSearch Dashboards** under `Connection Information`

   This opens the OpenSearch Dashboard

3. In OpenSearch Dashboard Click  on top left to open the left side panel -> Under `OpenSearch Plugins` -> **Alerting**

.. note::
    To configure each alert there are ``Monitor``, ``Data source``, ``Query``, ``Trigger`` and ``Destination`` needs to be created.

4. Click the **Destination** tab -> **Add destination**
   
   **Name** -> ``slack-test``

   **Type** -> ``Slack``

   **Settings** **Webhook URL:** -> ``https://your_slack_webhook_URL``

.. note::
   Destination Type can be: ``Amazon Chime``, ``Slack``, ``Custom webhook`` or ``Email``

.. important::
   When using email you need to have a SMTP server configured for a valid domain to deliver email notifications

5. Click the **Monitors** tab -> **Create monitor**

6. **Monitor details**
   
   **Monitor name** -> ``High CPU Monitor``

   **Monitor name** -> ``Per query monitor``
   
   **Monitor defining method** -> ``Visual editor`` 

   **Schedule** **Frequency** -> ``By interval``

   **Run every** -> ``1`` ``Minutes``

.. note::
   Schedule Frequency can be `By internal`, `Daily`, `Weekly`, `Monthly`, `Custom CRON expression`


7. **Data source** 
 
   **index** -> ``sample-host-health``

   **Time field** -> ``timestamp``

8. **Query**

   **Metrics** -> **Add metric** 

   **Aggregation** ``avrerage()`` **Field** ``cpu_usage_percentage``

   **Time range for the last** ``3`` ``minutes``

9. **Add trigger**

   **Trigger name** -> ``high_cpu``

   **Severity level** -> ``1 (Highest)``

   **Trigger condition** ``IS ABOVE`` ``75``

.. note::
   You can see a visual graph below trigger with the index data and the trigger condition you have defined as a red line

10. **Actions**
     
**Action name** -> ``slack``

**Destination** -> ``slack-test``

**Message subject** -> ``High CPU Test Alert``

.. note::
   Multiple Actions can be defined, in this example we will define one action to send notification to destination we have defined in step 4

**Message** can be adjusted as needed, check **Message Preview** to see the sample and use **Send test message** to validate notification delivery

Click on **Create** and your monitor is ready!

* For further details on `alerting monitors configuration <https://opensearch.org/docs/latest/monitoring-plugins/alerting/monitors/>`_

.. _Code:

Create programmatically
***********************

Monitors can be created by ``POST`` a JSON to OpenSearch API 

``https://username:password@os-name-myproject.aivencloud.com:24947/_plugins/_alerting/monitors``

The required JSON request format can be found in `OpenSearch Alerting API documentation <https://opensearch.org/docs/latest/monitoring-plugins/alerting/api/#create-query-level-monitor>`_


The following example code is for creating the same CPU alert monitor above programmatically.

Save the JSON below into ``cpu_alert.json`` 

.. literalinclude:: /code/products/opensearch/cpu_alert.json
  :language: JSON

Use ``curl`` to create the alert

.. code-block::

   curl -XPOST \
   https://username:password@os-name-myproject.aivencloud.com:24947/_plugins/_alerting/monitors \
   -H 'Content-type: application/json' -T cpu_alert.json

