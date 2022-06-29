Connect to MySQL with PHP
========================

This example connects to MySQL service from PHP, making use of the built-in PDO module.

Variables
---------

These are the placeholders you will need to replace in the code sample:

==================      ================================================================
Variable                Description
==================      ================================================================
``MYSQL_URI``           Service URI for MySQL connection, from the service overview page
==================      ================================================================

Pre-requisites
--------------

For this example you will need:

* :doc:`/docs/platform/howto/download-ca-cert` from the service overview page, this example assumes it is in a local file called ``ca.pem``.

.. note::
   Your PHP installation will need to include the `MySQL functions <https://www.php.net/manual/en/ref.pdo-pgsql.php>`_ (most installations will have this already).

Code
----

Add the following to ``index.php`` and replace the placeholder with the MySQL URI:

.. literalinclude:: /code/products/mysql/connect.php
   :language: php

This code creates a MySQL client and opens a connection to the database. Then runs a query checking the database version and prints the response

.. note::
   This example replaces the query string parameter to specify ``sslmode=verify-ca`` to make sure that the SSL certificate is verified, and adds the location of the cert.

To run the code::

    php index.php

If the script runs successfully, the outputs should be the MySQL version running in your service like::

    8.0.28~
