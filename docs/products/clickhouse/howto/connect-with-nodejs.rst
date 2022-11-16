Connect to the Aiven for ClickHouse® service with Node.js
=========================================================

Learn how to connect to your Aiven for ClickHouse® service with Node.js using the official Node.js client for connecting to ClickHouse and the HTTPS port.

Pre-requisites
--------------

* `Node.js <https://nodejs.org/en/download/>`_ in your environment
* `Node.js client for connecting to ClickHouse <https://clickhouse.com/docs/en/integrations/language-clients/nodejs/>`_

.. tip::

    You can install the Node.js client for connecting to ClickHouse using

    .. code:: java

        npm i @clickhouse/client

Create a client instance
------------------------

Use the ``createClient`` factory to initiate a client instance.

.. code:: javascript

    import { createClient } from '@clickhouse/client'

    const client = createClient({
    /* configuration */
    })

In the process of initiating the client instance, you can configure the following settings:

========================    =================================================   =========================================================================================================================   =========================
Setting                     Data type                                           Description                                                                                                                 Default value
========================    =================================================   =========================================================================================================================   =========================
``host``                    string                                              ClickHouse instance URL                                                                                                     ``http://localhost:8123``
``connect_timeout``         number                                              Timeout to set up a connection in milliseconds                                                                              10_000
``request_timeout``         number                                              Request timeout in milliseconds                                                                                             30_000
``max_open_connections``    number                                              Maximum number of sockets to allow per host                                                                                 Infinity
``compression``             { response?: boolean; request?: boolean }           `Enables compression <https://clickhouse.com/docs/en/integrations/language-clients/nodejs/#compression>`_                   --
``username``                string                                              Name of the user on whose behalf requests are made                                                                          default
``password``                string                                              User password                                                                                                               ``''``
``application``             string                                              Name of the application using the Node.js client                                                                            clickhouse-js
``database``                string                                              Database name to use                                                                                                        default
``clickhouse_settings``     ClickHouseSettings                                  ClickHouse settings to apply to all requests                                                                                {}
``log``                     { enable?: boolean, LoggerClass?: Logger }          `Configure logging <https://clickhouse.com/docs/en/integrations/language-clients/nodejs/#logging>`_                         -- 
``tls``                     { ca_cert: Buffer, cert?: Buffer, key?: Buffer }    `Configure TLS certificates <https://clickhouse.com/docs/en/integrations/language-clients/nodejs/#tls-certificates>`_       --
``session_id``              string                                              Optional ClickHouse Session ID to send with every request                                                                   --
========================    =================================================   =========================================================================================================================   =========================

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

.. code:: javascript

    import { createClient } from '@clickhouse/client'

    const client = createClient({
    host: process.env.CLICKHOUSE_HOST ?? 'http://localhost:8123',
    user: process.env.CLICKHOUSE_USER ?? 'default',
    password: process.env.CLICKHOUSE_PASSWORD ?? '',
    })

.. topic:: Expected result

    Now you have your service connection set up and you can proceed to :doc: `uploading data into your database <load-dataset>`.

.. seealso::

    For information on how to connect to the Aiven for Clickhouse service with the ClickHouse client, see :doc:`Connect with the ClickHouse client </docs/products/clickhouse/howto/connect-with-clickhouse-cli>`.

