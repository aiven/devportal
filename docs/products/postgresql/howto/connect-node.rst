Connect with NodeJS
-------------------

This example connects to PostgreSQL® service from NodeJS, making use of the ``pg`` package.

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

==================      =============================================================
Variable                Description
==================      =============================================================
``POSTGRESQL_URI``      URL for PostgreSQL connection, from the service overview page
==================      =============================================================

Pre-requisites
''''''''''''''

For this example you will need:

* The npm ``pg`` package::

    npm install pg --save

* :doc:`/docs/platform/howto/download-ca-cert` from the service overview page, this example assumes it is in a local file called ``ca.pem``.

Code
''''

Add the following to ``index.js`` and replace the placeholder with the PostgreSQL URI:

.. literalinclude:: /code/products/postgresql/connect.js
   :language: javascript

This code creates a PostgreSQL client and opens a connection to the database. Then runs a query checking the database version and prints the response.

.. note::
    This example removes ``?sslmode=require`` from the URL string to avoid running into `this bug <https://github.com/brianc/node-postgres/issues/2558>`_. Adding the ``rejectUnauthorized: true`` configuration ensures that the certificate is checked.

To run the code::

    node index.js

If the script runs successfully, the outputs should be the PostgreSQL version running in your service like::

    PostgreSQL 13.3 on x86_64-pc-linux-gnu, compiled by gcc, a 68c5366192 p 6520304dc1, 64-bit
