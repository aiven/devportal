Connect to the Aiven for ClickHouse® service with Python
========================================================

To connect to your Aiven for ClickHouse® service with Python, you can use either the native protocol or the HTTPS protocol. This article provides you with instructions for both scenarios.

Connect with the native protocol
--------------------------------

Pre-requisites
''''''''''''''

* `Python 3.5 or later <https://www.python.org/downloads/>`_

* `ClickHouse Python Driver <https://pypi.org/project/clickhouse-driver/>`_

Identify connection information
'''''''''''''''''''''''''''''''

To run the code for connecting to your service, first identify values of the following variables:

==================      =====================================================================
Variable                Description
==================      =====================================================================
``USERNAME``            ``User`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse native**
``PASSOWRD``            ``Password`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse native**
``HOST``                ``Host`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse native**
``NATIVE_PORT``         ``Port`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse native**
``query``               Query you want to run, for example ``SELECT 1``
==================      =====================================================================

Connect to the service
''''''''''''''''''''''

Replace the placeholders in the code with meaningful information on your service connection and run the code.

.. code:: python

    from clickhouse_driver import Client
    client = Client(user="USERNAME", password="PASSWORD", host="HOST", port=NATIVE_PORT, secure=True)
    print(client.execute("SELECT 1"))

Connect with HTTPS
------------------

Pre-requisites
''''''''''''''

* `Python 3.7 or later <https://www.python.org/downloads/>`_

* `Requests HTTP library <https://pypi.org/project/requests/>`_

Identify connection information
'''''''''''''''''''''''''''''''

To run the code for connecting to your service, first identify values of the following variables:

===========================     ======================================================================================
Variable                        Description
===========================     ======================================================================================
``https://HOST:HTTPS_PORT``     ``Host`` and ``Port`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
``query``                       Query you want to run, for example ``SELECT 1``
``X-ClickHouse-Database``       ``Database Name`` available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**, for example ``system``
``X-ClickHouse-User``           ``User`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
``X-ClickHouse-Key``            ``Password`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
``X-ClickHouse-Format``         Format for the output from your query, for example ``JSONCompact``
===========================     ======================================================================================

Connect to the service
''''''''''''''''''''''

Replace the placeholders in the code with meaningful information on your service connection and run the code.

.. code:: python

    import requests
    response = requests.post(
        "https://HOST:HTTPS_PORT",
        params={"query": "SELECT 1"},
        headers={
            "X-ClickHouse-Database": "system",
            "X-ClickHouse-User": "USERNAME",
            "X-ClickHouse-Key": "PASSWORD",
            "X-ClickHouse-Format": "JSONCompact",
        })
    print(response.text)

.. topic:: Expected result

    Now you have your service connection set up and you can proceed to :doc: `uploading data into your database <load-dataset>`.

.. seealso::

    For information on how to connect to the Aiven for Clickhouse service with the ClickHouse client, see :doc:`Connect with the ClickHouse client </docs/products/clickhouse/howto/connect-with-clickhouse-cli>`.


