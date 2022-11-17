Connect to the Aiven for ClickHouse® service with PHP
=====================================================

Learn how to connect to your Aiven for ClickHouse® service with PHP using the PHP ClickHouse client and the HTTPS port.

Pre-requisites
--------------

* `PHP 7.4 or later <https://www.php.net/downloads>`_
* ``smi2/phpclickhouse`` library

.. tip::

    You can install ``smi2/phpclickhouse`` with the following command:

    .. code:: php

        composer require smi2/phpclickhouse

Identify connection information
-------------------------------

To run the code for connecting to your service, first identify values of the following variables:

===========================     =======================================================================================
Variable                        Description
===========================     =======================================================================================
``https``                       Required to be set to ``true``
``host``                        ``Host`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
``port``                        ``Port`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
``username``                    ``User`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
``password``                    ``Password`` for the ClickHouse connection available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
``database``                    ``Database Name`` in the ClickHouse service available in the Aiven console: Service **Overview** > **Connection information** > **ClickHouse HTTPS & JDBC**
``setTimeout``                  Supports only integer values, measured in seconds
``setConnectTimeout``           Supports only integer values, measured in seconds
``ping``                        Set to ``true`` to enable throwing an exception if a connection cannot be established
===========================     =======================================================================================

Connect to the service
----------------------

1. Start the PHP ClickHouse client with the following command:

.. code:: php

    $db = new ClickHouseDB\Client(['config_array']);
    if (!$db->ping()) echo 'Error connect';

2. Replace the placeholders in the code with meaningful information on your service connection and run the code.

.. code:: php

    $config = [
        'https' => true,
        'host' => '0.1.2.3',
        'port' => '1234',
        'username' => 'default',
        'password' => ''
    ];
    $db = new ClickHouseDB\Client($config);
    $db->database('default');
    $db->setTimeout(10);
    $db->setConnectTimeOut(5);
    $db->ping(true);

.. topic:: Expected result

    Now you have your service connection set up and you can proceed to :doc:`uploading data into your database <load-dataset>`.

.. seealso::

    For information on how to connect to the Aiven for Clickhouse service with the ClickHouse client, see :doc:`Connect with the ClickHouse client </docs/products/clickhouse/howto/connect-with-clickhouse-cli>`.

