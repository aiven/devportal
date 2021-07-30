Connect with PHP
----------------

This example connects to PostgreSQL service from PHP, making use of the built-in PDO module.

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

==================      =============================================================
Variable                Description
==================      =============================================================
``POSTGRESQL_URI``      URL for PostgreSQL connection, from the service overview page
==================      =============================================================

Code
''''

Add the following to ``index.php`` and replace the placeholder with the PostgreSQL URI:

.. literalinclude:: /code/products/postgresql/connect.php

This code creates a PostgreSQL client and opens a connection to the database. Then runs a query checking the database version and prints the response

To run the code::

    php index.php

If the script runs successfully, the outputs should be the PostgreSQL version running in your service like::

    PostgreSQL 13.3 on x86_64-pc-linux-gnu, compiled by gcc, a 68c5366192 p 6520304dc1, 64-bit
