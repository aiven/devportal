Visualize ClickHouse® data with Grafana®
=========================================

You can visualise your ClickHouse data with the help of Grafana. Aiven can help you connect these services services.

Prerequisites
--------------
You will need:

1. Aiven for ClickHouse service, accessible by HTTPS
2. Aiven for Grafana service, see how to :doc:`get started with Aiven for Grafana </docs/products/grafana/get-started>`

Variables
--------------------
We'll use these values later in the set up. They can be found in your Aiven for ClickHouse service page, in connection information for HTTPS endpoint.

============================     ==========================================================================================================
Variable                         Description
============================     ==========================================================================================================
``CLICKHOUSE_HTTPS_URI``         HTTPS service URI of your ClickHouse service.
``CLICKHOUSE_USER``              Username to access ClickHouse service.
``CLICKHOUSE_PASSWORD``          Password to access ClickHouse service.
============================     ==========================================================================================================

Integration steps
--------------------

1. Follow :doc:`these instructions </docs/products/grafana/howto/log-in>` to log in into Aiven for Grafana.
#. In *Configuration menu* select **Data sources**.
#. Click to **Add data source**.
#. Find **Altinity plugin for ClickHouse** in the list and select it. You'll see a panel with list of settings to fill in.
#. Set *Url* to ``CLICKHOUSE_HTTPS_URI``.
#. In *Auth* section enable **Basic auth** and **With Credentials**.
#. In *Basic Auth Details* set your ``CLICKHOUSE_USER`` and ``CLICKHOUSE_PASSWORD``.
#. Press on **Save & test**.

Now you can create a dashboard and panels to work with the data from your Aiven for ClickHouse service.