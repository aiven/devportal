Connect to Aiven for MySQL® with PHP
====================================

This example connects to an Aiven for MySQL® service from PHP, making use of the built-in PDO module.

Variables
---------

These are the placeholders you need to replace in the code sample:

==================      ============================================================================================================================
Variable                Description
==================      ============================================================================================================================
``MYSQL_URI``           Service URI for MySQL connection, from `Aiven Console <https://console.aiven.io/>`__ > the **Overview** page of your service
==================      ============================================================================================================================

Pre-requisites
--------------

* :doc:`/docs/platform/howto/download-ca-cert` from `Aiven Console <https://console.aiven.io/>`__ > the **Overview** page of your service. This example assumes it is in a local file called ``ca.pem``.

.. note::
   Your PHP installation needs to include the `MySQL functions <https://www.php.net/manual/en/ref.pdo-pgsql.php>`_ (most installations have this already).

Code
----

Add the following to ``index.php`` and replace the placeholder with the MySQL URI:

.. literalinclude:: /code/products/mysql/connect.php
   :language: php

This code creates a MySQL client and opens a connection to the database. It then runs a query checking the database version and prints the response.

.. note::
   This example replaces the query string parameter to specify ``sslmode=verify-ca`` to make sure that the SSL certificate is verified, and adds the location of the cert.

Run the following code::

    php index.php

If the script runs successfully, the output is the MySQL version running in your service like::

    8.0.28
