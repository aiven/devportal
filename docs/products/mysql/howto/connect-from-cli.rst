Connect to MySQL from the command line
--------------------------------------

Here, you can find how to connect to your MySQL via the command line with a choice of tools:

* :ref:`mysqlsh shell <connect-mysqlsh>`
* :ref:`mysql client <connect-mysql>`

.. _connect-mysqlsh:

Using ``mysqlsh``
-----------------

Variables
~~~~~~~~~

These are the placeholders you will need to replace in the code sample:

.. list-table::
  :header-rows: 1
  :widths: 15 60
  :align: left

  * - Variable
    - Description
  * - ``SERVICE_URI``
    - URL for MySQL connection, from the service overview page

Prerequisites
~~~~~~~~~~~~~

For this example you will need:

1. The ``mysqlsh`` client installed. You can install this by following the `MySQL documentation <https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-install.html>`_.


Code
~~~~

Execute the following from a terminal window to connect to the MySQL database:

::

    mysqlsh --sql SERVICE_URI

You can execute this query to test:

::

   MySQL ssl defaultdb SQL> select 1 + 2 as three;
   +-------+
   | three |
   +-------+
   |     3 |
   +-------+
   1 row in set (0.0539 sec)



Using ``mysql``
---------------

Variables
~~~~~~~~~

These are the placeholders you will need to replace in the code sample:

.. list-table::
  :header-rows: 1
  :widths: 15 60
  :align: left

  * - Variable
    - Description
  * - ``USER_HOST``
    - Hostname for MySQL connection
  * - ``USER_PORT``
    - Port for MySQL connection
  * - ``USER_PASSWORD``
    - Password of your Aiven for MySQL connection

.. _connect-mysql:

Prerequisites
~~~~~~~~~~~~~

For this example you will need:

1. The ``mysql`` client installed. You can install it by following the `MySQL documentation <https://dev.mysql.com/doc/refman/8.0/en/mysql.html>`_.

Code
~~~~

This step requires to manually specify individual parameters. You can find those parameters in the `Aiven Console <https://console.aiven.io>`_ for your service. 

Once you have these parameters, execute the following from a terminal window to connect to the MySQL database:

::

   mysql --user avnadmin --password=USER_PASSWORD --host USER_HOST --port USER_PORT defaultdb

.. warning::
   If you are providing the password via the command line, you must pass it as shown; putting a space between the parameter name and value will cause the password to be parsed incorrectly.
