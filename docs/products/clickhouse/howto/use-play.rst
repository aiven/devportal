Use ClickHouse® play UI
========================

ClickHouse® includes a built-in user interface for running SQL queries. You can access it through HTTPS protocol. Follow these steps to use it:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_ and select your ClickHouse service.
#. In the *Overview* tab find *Connection information* and select **ClickHouse HTTPS**
#. Copy Service URI and use it to open a page in the browser with the URL ``your-full-service-uri/play``.
#. Set the *name* and the *password* of the user of whose behalf you want to run the queries.
#. Enter the body of the query.
#. Click **Run**.

.. note::
    `/play` is an alternative to the :doc:`query editor <use-query-editor>`. The query editor can be accessed directly from console to run requests on behalf of the default user.