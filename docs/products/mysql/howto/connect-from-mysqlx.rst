Connect to MySQL using MySQLx with Python
=========================================

Enabling MySQLx protocol support allows customers to use their MySQL instance as a document store. This example shows how to connect to your Aiven for MySQL instance using MySQLx protocol.

.. note::

    MySQL initially provided support for X-DevAPI (MySQLx) in v5.7.12 as an optional extension that can be installed by the user. On the MySQL v8.0+, the X-DevAPI is supported by default.

Variables
'''''''''

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Variable
     - Description
   * - ``SERVICE_URI``
     - Connection information about your Aiven for MySQLx service.
   * - ``MYSQLX_PASSWORD``
     - Password for ``avnadmin`` user

Prerequisites
'''''''''''''

* Python 3.7 or later
  
* A ``mysqlx`` python library installed::
     
     pip install mysql-connector-python

* An Aiven account with a service running. Click on **MySQLx** tab under **Connection information**, and copy ``SERVICE_URI`` and ``Port`` information.

* Set ``PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python`` on your terminal to avoid issues described on `Protocol buffers docs <https://developers.google.com/protocol-buffers/docs/news/2022-05-06>`_. 
  
  .. code:: shell

    export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

Code
''''

Add the following to ``main.py`` and replace the placeholders with values for your project:

.. literalinclude:: /code/products/mysql/connect.py
   :language: python


This code creates a MySQL client and connects to the database via the MySQLx protocol. It creates a schema, a collection, inserts some entries, fetches them, and prints the output.

If the script runs successfully, the output will be the values that were inserted into the document::

    Found document: {"_id": "000062c55a6b0000000000000001", "type": "pizza", "price": "10e"}
    Found document: {"_id": "000062c55a6b0000000000000002", "type": "burger", "price": "5e"}


Now that your application is connected, you are all set to use Python with Aiven for MySQL using MySQLx protocol.

