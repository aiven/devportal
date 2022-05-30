Create alerts with OpenSearch® API
==================================

OpenSearch® alerting feature sends notifications when data from one or more indices meets certain conditions that can be customized.
Use case examples are such as monitoring for HTTP status code 503, CPU load average above certain percentage or watch for counts of a specific keyword in logs for a specific amount of interval,
notification to be configured to be sent via email, slack or custom webhooks and other destination, in this example we are using slack as the destination.

In the following example, we are creating an alert programmatically by using OpenSearch Alerting API.
We are using a ``sample-host-health`` index as datasource to create a simple alert to check cpu load, action will be triggered when average of ``cpu_usage_percentage`` over ``3`` minutes is above ``75%``

OpenSearch API Alerting API URL can be copied from Aiven console:

Click the **Overview** tab -> **OpenSearch** under `Connection Information` -> **Service URI**
append ``_plugins/_alerting/monitors`` to the **Service URI**

Example:

``https://username:password@os-name-myproject.aivencloud.com:24947/_plugins/_alerting/monitors``

Save the JSON below into ``cpu_alert.json`` 

.. literalinclude:: /code/products/opensearch/cpu_alert.json
  :language: JSON

Use ``curl`` to create the alert

.. code-block::

   curl -XPOST \
   https://username:password@os-name-myproject.aivencloud.com:24947/_plugins/_alerting/monitors \
   -H 'Content-type: application/json' -T cpu_alert.json

* The required JSON request format can be found in `OpenSearch Alerting API documentation <https://opensearch.org/docs/latest/monitoring-plugins/alerting/api/#sample-request>`_

