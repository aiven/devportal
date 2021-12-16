Connect to MySQL with Python
============================

This example connects your Python application to a MySQL service, using the `PyMySQL <https://github.com/PyMySQL/PyMySQL>`__ library.

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

==================      =============================================================
Variable                Description
==================      =============================================================
``MYSQL_HOST``          Host name for the connection, from the service overview page
------------------      -------------------------------------------------------------
``MYSQL_PORT``          Port number to use, from the service overview page
------------------      -------------------------------------------------------------
``MYSQL_USERNAME``      User to connect with
------------------      -------------------------------------------------------------
``MYSQL_PASSWORD``      Password for this user
==================      =============================================================

Pre-requisites
''''''''''''''

For this example you will need:

* Python 3.7 or later

* The Python ``PyMySQL`` library. You can install this with ``pip``::

    pip install pymysql


Code
''''

Add the following to ``main.py`` and replace the placeholders with values for your project:

.. literalinclude:: /code/products/mysql/connect.py


This code creates a PostgreSQL client and connects to the database. It creates a table, inserts some values, fetches them and prints the output.

To run the code::

    python main.py

If the script runs successfully, the output will be the values that were inserted into the table::

    [{'id': 1}, {'id': 2}]    

Now that your application is connected, you are all set to use Python with Aiven for MySQL.

