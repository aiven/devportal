Query Data to PostgreSQL with Go
--------------------------------

This example queries some data in a PostgreSQL service from Go, making use of the ``pg`` library.

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

1. The Go ``pq`` library::

    go get github.com/lib/pq



Code
''''

Add the following to ``main.go`` and replace the placeholder with the PostgreSQL URI:

.. literalinclude:: /code/products/postgresql/query.go

This code creates an PostgreSQL client and opens a connection to the database. Then runs a query checking the database version and prints the response

To run the code::

    go run main.go

If the script runs successfully, the outputs should be the PostgreSQL version running in your service like::

    Version: PostgreSQL 13.3 on x86_64-pc-linux-gnu, compiled by gcc, a 68c5366192 p 6520304dc1, 64-bit
