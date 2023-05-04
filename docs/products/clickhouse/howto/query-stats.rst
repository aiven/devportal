Query Statistics in ClickHouse®
================================

Usually, Query statistics in ClickHouse can be obtained using the ``system.query_log`` table, which stores statistics of each executed query, including memory usage and duration. Aiven for ClickHouse® currently do not give access to the table ``system.query_log`` table, in order to directly query the table for the required statistics.

Instead,use one of the two approach to view *Query Statistics* for Aiven for ClickHouse®

With Aiven console
---------------------

1. Log in to the `Aiven web console <https://console.aiven.io/>`_, choose the right project, and select your Aiven for ClickHouse service.
2. Navigate to the **Query Statstics** tab, and you can visulize the content in the dashboard.

With Aiven API
----------------------

Alternatively, you can access *Query Statistics* via `Query statistics endpoint <https://api.aiven.io/doc/#tag/Service:_ClickHouse/operation/ServiceClickHouseQueryStats>`_. Example endpoint skeloton:

    .. code:: bash

        GET /project/<project>/service/<service_name>/clickhouse/query/stats

Learn more about API usage in the :doc:`Aiven API overview </docs/tools/api>`.