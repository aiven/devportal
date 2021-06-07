Query Data to PostgreSQL with Python
------------------------------------

This example queries some data in a PostgreSQL service from Python, making use of the ``psycopg2`` library.

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

1. Python 3.6 or later

2. The Python ``psycopg2`` library. You can install this with ``pip``::

    pip install psycopg2


Code
''''

Add the following to ``main.py`` and replace the placeholders with values for your project:

.. literalinclude:: /code/products/m3db/write.py


This code creates an PostgreSQL client and connects to the database. Then runs a query checking the database version and prints the response

To run the code::

    python main.py

If the script runs successfully, the outputs should be the PostgreSQL version running in your service like::

    PostgreSQL 13.3 on x86_64-pc-linux-gnu, compiled by gcc, a 68c5366192 p 6520304dc1, 64-bit
