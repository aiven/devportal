<script type='text/javascript' async src='https://play.vidyard.com/embed/v4.js' data-playbackurl='play.vidyard.com'></script><img style='margin: auto; display: block; width: 100%; 'class='vidyard-player-embed' src='https://play.vidyard.com/2cQUuV7pxtSWabGMmwkGYJ.jpg' data-height='540' data-width='960' data-width='auto' data-controller='hubs' data-action='show' data-hub_path='hub' data-uuid='2cQUuV7pxtSWabGMmwkGYJ' data-type='inline' />

Visualize ClickHouse® data with Grafana®
=========================================

You can visualise your ClickHouse® data using Grafana® and Aiven can help you connect the two services.

Prerequisites
--------------

1. Aiven for ClickHouse® service accessible by HTTPS
2. Aiven for Grafana® service (see how to :doc:`get started with Aiven for Grafana® </docs/products/grafana/get-started>`)

Variables
--------------------
You'll need a few variables for the setup. To get their values, go to the Aiven console and navigate to **Overview** of your Aiven for ClickHouse® service (connection information for the HTTPS endpoint).

============================     ==========================================================================================================
Variable                         Description
============================     ==========================================================================================================
``CLICKHOUSE_HTTPS_URI``         HTTPS service URI of your ClickHouse service.
``CLICKHOUSE_USER``              Username to access ClickHouse service.
``CLICKHOUSE_PASSWORD``          Password to access ClickHouse service.
============================     ==========================================================================================================

Integrate ClickHouse® with Grafana®
----------------------------------

1. Log in to Aiven for Grafana® following :doc:`the instructions </docs/products/grafana/howto/log-in>`.
#. From the **Configuration** menu, select **Data sources** > **Add data source**.
#. Find **Altinity plugin for ClickHouse** in the list and select it.
#. Set *URL* to ``CLICKHOUSE_HTTPS_URI``.
#. In *Auth* section, enable **Basic auth** and **With Credentials**.
#. In *Basic Auth Details*, set your ``CLICKHOUSE_USER`` and ``CLICKHOUSE_PASSWORD``.
#. Selec **Save & test**.

Now you can create a dashboard and panels to work with the data from your Aiven for ClickHouse® service.
