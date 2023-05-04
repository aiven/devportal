Query Statstics in ClickHouse®
================================

Usually, Query stats in ClickHouse can be obtained using the ``system.query_log`` table, which stores statistics of each executed query, including memory usage and duration. Aiven for ClickHouse® currently do not give access to the table ``system.query_log`` table, in order to directly query the table for the required statistics.

Instead, we currently display the contents of the table on the service dashboard in Aiven Console. It can be viewed under the tab *Query Statstics* .
Alternatively, we also provide access to *Query Statstics* via `Aiven API<https://docs.aiven.io/docs/tools/api>`_. The following is the endpoint for the same:

    .. code:: bash

        GET /project/<project>/service/<service_name>/clickhouse/query/stats

The detalied usage of API can be found `here<https://api.aiven.io/doc/#tag/Service:_ClickHouse/operation/ServiceClickHouseQueryStats>_`.