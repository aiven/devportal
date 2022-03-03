Increase metrics limit setting for Datadog
==========================================

Monitoring of services, applications is essential to know wether programs work as expected, here is the article_ on getting started with Aiven and Datadog integration.
For large service cluster, sometimes, we can not find the metrics we expected or some value missing on dashboards. 
This is the guide for how to lift the limitation, get more metrics from the integration.

Identify that metrics are been dropped
--------------------------------------
Following example is a large Kafka where some metrics can not be found in Datadog dashboards after service integration.
A number of metrics have been dropped by user Telegraf.

::
 
  2022-02-15T22:47:30.601220+0000 scoober-kafka-3c1132a3-82 user-telegraf: 2022-02-15T22:47:30Z W! [outputs.prometheus_client] Metric buffer overflow; 3378 metrics have been dropped
  2022-02-15T22:47:30.625696+0000 scoober-kafka-3c1132a3-86 user-telegraf: 2022-02-15T22:47:30Z W! [outputs.prometheus_client] Metric buffer overflow; 1197 metrics have been dropped

Follow steps below can help you tackle this problem.

Configure the maximum metric limit
----------------------------------

We allow setting the maximum metric limit for services where Datadog agent gathers the metrics via ``JMX`` using the ``max_jmx_metrics`` option in the Datadog integration configuration. This can be set to any value between 10 and 100000 with a default value: 2000.

.. note:: Datadog may also limit the number of custom metrics that can be received, based on your pricing plan_ . 

The ``max_jmx_metrics`` is not exposed in our console yet, but you should be able to change it with the Aiven command line client_, using the following procedure:

1. Find the SERVICE_INTEGRATION_ID for your Datadog integration with

::

  avn service integration-list --project=PROJECT_NAME SERVICE_NAME

2. Change the value of ``max_jmx_metrics`` to the new LIMIT:

::

  avn service integration-update SERVICE_INTEGRATION_ID --project PROJECT_NAME -c max_jmx_metrics=LIMIT

.. note:: Please gradually increase the value, and monitor the memory usage on the cluster.

.. _article: https://help.aiven.io/en/articles/1759208-getting-started-with-datadog

.. _plan: https://docs.datadoghq.com/account_management/billing/custom_metrics/?tab=countrate#allocation

.. _client: https://github.com/aiven/aiven-client/
