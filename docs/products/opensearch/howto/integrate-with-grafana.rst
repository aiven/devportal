Integrate with Grafana®
=======================

You can monitor and set up alerts for the data in your Aiven for OpenSearch® service with Grafana. This feature is especially powerful if you're sending your Aiven service logs to an OpenSearch instance using :doc:`log integration <opensearch-log-integration>`.

Prerequisites
--------------
You will need:

1. Aiven for OpenSearch service.
2. Aiven for Grafana service, see how to :doc:`get started with Aiven for Grafana </docs/products/grafana/get-started>`.


Variables
--------------------
We'll use these values later in the set up. They can be found in your Aiven for OpenSearch service page, in the connection information.

========================================     ==========================================================================================================
Variable                                     Description
========================================     ==========================================================================================================
``OPENSEARCH_URI``                           Service URI of your OpenSearch service.
``OPENSEARCH_USER``                          Username to access OpenSearch service.
``OPENSEARCH_PASSWORD``                      Password to access OpenSearch service.
========================================     ==========================================================================================================

Integration steps
--------------------

1. Follow :doc:`these instructions </docs/products/grafana/howto/log-in>` to log in into Aiven for Grafana.
#. In *Configuration menu* select **Data sources**.
#. Click to **Add data source**.
#. Find **OpenSearch** in the list and select it. You'll see a panel with list of settings to fill in.
#. Use your preferred in the *Name* field. You'll use it later for creating dashboards and alerts.
#. Set *URL* to ``OPENSEARCH_URI``.
#. In *Auth* section enable **Basic auth** and **With Credentials**.
#. In *Basic Auth Details* set your ``OPENSEARCH_USER`` and ``OPENSEARCH_PASSWORD``.
#. Scroll down to *OpenSearch details* and set the index name or an index pattern (for example, ``logs-*``).
#. Set the time field name (in case you use :doc:`the log integration <opensearch-log-integration>` it will be ``timestamp``).
#. Press on **Save & test**. In case of errors, verify that the data source information is set correctly.


Create dashboards and alerts
-------------------------------
Using the interface of Grafana you can now create dashboards and alerts.

Select **Create** from the menu on the left and select to create either a dashboard or an alert rule. Follow the instructions to set them up.
