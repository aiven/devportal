Create alerts with OpenSearch Dashboards
========================================

OpenSearch alerting feature sends notifications when data from one or more indices meets certain conditions that can be customized.
Use case examples are such as monitoring for HTTP status code 503, CPU load average above certain percentage or watch for counts of a specific keyword in logs for a specific amount of interval,
notification to be configured to be sent via email, slack or custom webhooks and other destination.

In the following example we are using Slack as the destination and a ``sample-host-health`` index as datasource to create a simple alert to check cpu load. An action will be triggered when average of ``cpu_usage_percentage`` over ``3`` minutes is above ``75%``.

Create using Dashboards UI
**************************

In order to create an alert via OpenSearch Dashboards interface, follow these steps:

1. Log in to the `Aiven web console <https://console.aiven.io>`_ and select your OpenSearch service.

2. Click the **Overview** tab and under `Connection Information` click on **OpenSearch Dashboards** tab.

   This opens the OpenSearch Dashboard

3. In OpenSearch Dashboard open the left side panel and under `OpenSearch Plugins` click on **Alerting**.


To configure each alert the following needs to be created, we will walk-through configuration of each section.

- ``Destination``
- ``Monitor``
- ``Data source``
- ``Query``
- ``Trigger``

Create a destination
********************
Destination is a location for notifications to be delivered when an action is triggered.

1. Open the **Destination** tab and click on **Add destination**
   
2. **Name** -> ``slack-test``



.. note::
   Destination Type can be: ``Amazon Chime``, ``Slack``, ``Custom webhook`` or ``Email``

.. important::
   When using email you need to have a SMTP server configured for a valid domain to deliver email notifications

Create a monitor
****************
Monitor is a job that runs on a defined schedule and queries OpenSearch indices. 

1. Open the **Monitors** tab and click on **Create monitor**

2. **Monitor details**
   
   **Monitor name** -> ``High CPU Monitor``

   **Monitor name** -> ``Per query monitor``
   
   **Monitor defining method** -> ``Visual editor`` 

   **Schedule** **Frequency** -> ``By interval``

   **Run every** -> ``1`` ``Minutes``

.. note::
   Schedule Frequency can be `By internal`, `Daily`, `Weekly`, `Monthly`, `Custom CRON expression`

3. **Data source** 
   
   Data source is the OpenSearch indices to query.
 
   **index** -> ``sample-host-health``

   **Time field** -> ``timestamp``

4. **Query**

   Query defines the fields to query from indices and how to evaluate the results.

   **Metrics** -> **Add metric** 

   **Aggregation** ``average()`` **Field** ``cpu_usage_percentage``

   **Time range for the last** ``3`` ``minutes``

Create a trigger
****************
Triggers is a defined conditions from the queries results from monitor.  If conditions are met, alerts are generated.

1. **Add trigger**

   **Trigger name** -> ``high_cpu``

   **Severity level** -> ``1 (Highest)``

   **Trigger condition** ``IS ABOVE`` ``75``

.. note::
   You can see a visual graph below trigger with the index data and the trigger condition you have defined as a red line

2. **Actions**

   Actions defines the destination for notification alerts when trigger conditions are met.
     
   **Action name** -> ``slack``

   **Destination** -> ``slack-test``

   **Message subject** -> ``High CPU Test Alert``

.. note::
   Multiple Actions can be defined, in this example we will define one action to send notification to destination we have defined in step 4

Alert Message
*************

**Message** can be adjusted as needed, check **Message Preview** to see the sample and use **Send test message** to validate notification delivery

Click on **Create** and your monitor is ready!

* For further details on `alerting monitors configuration <https://opensearch.org/docs/latest/monitoring-plugins/alerting/monitors/>`_