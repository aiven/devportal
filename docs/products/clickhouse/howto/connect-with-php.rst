Connect to the Aiven for ClickHouse® service with PHP
=====================================================

Learn how to connect to your Aiven for ClickHouse® service with PHP using the PHP ClickHouse client and the HTTPS port.

Pre-requisites
--------------

* `PHP 7.4 or later <https://www.php.net/downloads>`_
* ``smi2/phpclickhouse`` library
* `Composer <https://getcomposer.org/>`_

.. tip::

    You can install ``smi2/phpclickhouse`` with the following command:

    .. code-block:: php

        composer require smi2/phpclickhouse

    or

    .. code-block:: php

        php composer.phar require smi2/phpclickhouse

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

Replace the placeholders in the code with meaningful information on your service connection and run the code.

.. code-block:: php

    <?php
        require_once 'vendor/autoload.php';
        $db = new ClickHouseDB\Client([
            'https' => true,
            'host' => 'HOSTNAME',
            'port' => 'HTTPS_PORT',
            'username' => 'USERNAME',
            'password' => 'PASSWORD'
        ]);
        $response = $db->select('SELECT 1');
        print_r($response->rows());

.. topic:: Expected result

    Now you have your service connection set up and you can proceed to :doc:`uploading data into your database <load-dataset>`.

.. seealso::

    For information on how to connect to the Aiven for Clickhouse service with the ClickHouse client, see :doc:`Connect with the ClickHouse client </docs/products/clickhouse/howto/connect-with-clickhouse-cli>`.
