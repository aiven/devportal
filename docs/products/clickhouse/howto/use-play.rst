Use play UI
============

ClickHouse® includes a built-in user interface for running SQL queries. You can access it from a web browser over the HTTPS protocol. Follow these steps to use it:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_, choose the right project, and select your Aiven for ClickHouse service.
#. In the *Overview* tab, find *Connection information* and select **ClickHouse HTTPS**.
#. Copy the Service URI and navigate to ``SERVICE_URI/play`` from a web browser.
#. Set the *name* and the *password* of the user on whose behalf you want to run the queries.
#. Enter the body of the query.
#. Click **Run**.

.. note::
    The play interface is only available if you can connect directly to ClickHouse from your browser. If the service is `restricted by IP addresses <https://developer.aiven.io/docs/platform/howto/restrict-access.html>`_ or in a `VPC without public access <https://developer.aiven.io/docs/platform/howto/public-access-in-vpc.html>`_, you can use the :doc:`query editor <use-query-editor>` instead.
    The query editor can be accessed directly from the console to run requests on behalf of the default user.