Connect to MySQL from command line
==================================

There are multiple ways you can try out your new MySQL service. From the
command line, including the ``mysqlsh`` tool provided
by Oracle, which can directly accept the service URL shown on the
Service Overview page:

::

   mysqlsh --sql mysql://avnadmin:giufg3yd1b89sqjb@mysql-demo-dev-advocates.aivencloud.com:12691/defaultdb?ssl-mode=REQUIRED

   MySQL ssl defaultdb SQL> select 1 + 2 as three;
   +-------+
   | three |
   +-------+
   |     3 |
   +-------+
   1 row in set (0.0539 sec)

The basic ``mysql`` command line tool is another option, this requires you 
to manually specify individual parameters. 

::

   mysql --user avnadmin --password=giufg3yd1b89sqjb --host mysql-demo-dev-advocates.aivencloud.com --port 12691 defaultdb

.. note::
   If you are providing the password via the command line, you must pass it as shown; putting a space between the parameter name and value does not work like it does for other parameters.



