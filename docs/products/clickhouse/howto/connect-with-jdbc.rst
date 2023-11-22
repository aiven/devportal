Connect Aiven for ClickHouse® to external databases via JDBC
===============================================================

You can use `ClickHouse JDBC driver <https://github.com/ClickHouse/clickhouse-jdbc/tree/master/clickhouse-jdbc>`_ to connect external sources to your Aiven for ClickHouse database.

You will need Aiven for ClickHouse® service, accessible by HTTPS. The connection values you need can be found in `Aiven Console <https://console.aiven.io/>`_ > your service's page > **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**.

============================     ==========================================================================================================
Variable                         Description
============================     ==========================================================================================================
``CLICKHOUSE_HTTPS_HOST``        HTTPS service host of your ClickHouse service.
``CLICKHOUSE_HTTPS_PORT``        HTTPS service port of your ClickHouse service.
``CLICKHOUSE_USER``              Username to access ClickHouse service.
``CLICKHOUSE_PASSWORD``          Password to access ClickHouse service.
============================     ==========================================================================================================

Connection string
--------------------

Replace ``CLICKHOUSE_HTTPS_HOST`` and ``CLICKHOUSE_HTTPS_PORT`` with your connection values:

.. code::
 
   jdbc:ch://CLICKHOUSE_HTTPS_HOST:CLICKHOUSE_HTTPS_PORT?ssl=true&sslmode=STRICT


You'll also need to provide user name and password to establish the connection. For example, if you use Java:

.. code::
  
   Connection connection = dataSource.getConnection("CLICKHOUSE_USER", "CLICKHOUSE_PASSWORD");
