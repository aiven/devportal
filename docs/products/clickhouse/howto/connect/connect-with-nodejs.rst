Connect to the Aiven for ClickHouse® service with Node.js
=========================================================

Learn how to connect to your Aiven for ClickHouse® service with Node.js using the official Node.js client for connecting to ClickHouse and the HTTPS port.

Pre-requisites
--------------

* `Node.js <https://nodejs.org/en/download/>`_ in your environment
* `Node.js client for connecting to ClickHouse <https://clickhouse.com/docs/en/integrations/language-clients/nodejs/>`_

.. tip::

    You can install the Node.js client for connecting to ClickHouse using

    .. code-block:: shell

        npm i @clickhouse/client

Identify connection information
-------------------------------

To run the code for connecting to your service, first identify values of the following variables:

===========================     ======================================================================================
Variable                        Description
===========================     ======================================================================================
``CLICKHOUSE_HOST``             ``https://HOST:HTTPS_PORT``, where ``Host`` and ``Port`` for the ClickHouse connection are available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
``CLICKHOUSE_USER``             ``User`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
``CLICKHOUSE_PASSWORD``         ``Password`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
===========================     ======================================================================================

Connect to the service
----------------------

Replace the placeholders in the code with meaningful information on your service connection and run the code.

.. code-block:: javascript

    import { createClient } from '@clickhouse/client'
    const client = createClient({
        host: "CLICKHOUSE_HOST",
        username: "CLICKHOUSE_USER",
        password: "CLICKHOUSE_PASSWORD",
        database: "default",
    })
    const response = await client.query({
        query : "SELECT 1",
        format: "JSONEachRow",
        wait_end_of_query: 1,
    })
    const data = await response.json()
    console.log(data)

.. topic:: Expected result

    Now you have your service connection set up and you can proceed to :doc: `uploading data into your database <load-dataset>`.

.. seealso::

    For information on how to connect to the Aiven for Clickhouse service with the ClickHouse client, see :doc:`Connect with the ClickHouse client </docs/products/clickhouse/howto/connect-with-clickhouse-cli>`.
