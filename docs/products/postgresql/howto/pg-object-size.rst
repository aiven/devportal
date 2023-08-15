Check size of a database, a table or an index
=============================================

PostgreSQL® offers different commands and functions to get disk space usage for a database, a table, or an index. The results of executing specific commands and functions may vary, which can cause misinterpretation or confusion.

This article provides commands and functions used to check disk space usage for a database, a table, and an index. It also shows differences between the results these commands and functions return.

Get a database size
-------------------
Retrieve the database size using either the ``\l+ [ pattern ]`` command `` or the the ``pg_database_size`` function.

Use the ``\l+ [ pattern ]`` command
'''''''''''''''''''''''''''''''''''

.. code-block:: bash 

    testdb2=> \l+
                                                                     List of databases   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   |   Size    | Tablespace |            Description             
    -----------+----------+----------+-------------+-------------+-----------------------+-----------+------------+------------------------------------
     _aiven    | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =T/postgres          +| No Access | pg_default | 
    ...
     testdb2   | avnadmin | UTF8     | en_US.UTF-8 | en_US.UTF-8 |                       | 66 MB     | pg_default | 
    (6 rows)
    testdb2=> \l+ testdb2
                                                    List of databases
      Name   |  Owner   | Encoding |   Collate   |    Ctype    | Access privileges | Size  | Tablespace | Description 
    ---------+----------+----------+-------------+-------------+-------------------+-------+------------+-------------
     testdb2 | avnadmin | UTF8     | en_US.UTF-8 | en_US.UTF-8 |                   | 66 MB | pg_default | 
    (1 row)

Use the ``pg_database_size`` function
'''''''''''''''''''''''''''''''''''''

.. code-block:: bash

    testdb2=> select pg_database_size('testdb2'); 
     pg_database_size 
    ------------------
             68895523
    (1 row)
    
    testdb2=> select pg_size_pretty(pg_database_size('testdb2')); 
     pg_size_pretty 
    ----------------
     66 MB
    (1 row)

.. topic:: Compare the outputs of the ``\l+ DB_NAME`` command and the ``pg_database_size`` function
   
   The outputs for the ``testdb2`` database size are the same for both methods. Since the ``pg_database_size`` function returns the database size in bytes, we use the ``pg_size_pretty`` function to retrieve an easy-to-read output.


Get a table size
----------------
To get the table size, you can use either the ``\dt+ [ pattern ]`` command or the ``pg_table_size`` function.

Use the ``\dt+ [ pattern ]`` command
''''''''''''''''''''''''''''''''''''

.. code-block:: bash

    testdb2=> \dt+ mytable1
                                           List of relations
       Schema    |   Name   | Type  |  Owner   | Persistence | Access method | Size  | Description 
    -------------+----------+-------+----------+-------------+---------------+-------+-------------
     test_schema | mytable1 | table | myowner  | permanent   | heap          | 14 MB | 
    (1 row)


Use the ``pg_table_size`` function
''''''''''''''''''''''''''''''''''

.. code-block:: bash

    testdb2=> select pg_size_pretty(pg_table_size('mytable1')); 
     pg_size_pretty 
    ----------------
     14 MB
    (1 row)

Get an index size
-----------------
Retrieve the individual index size using either the the ``\di+ [ pattern ]`` command or the ``pg_database_size`` function.

Use the ``\di+ [ pattern ]`` command
''''''''''''''''''''''''''''''''''''

.. code-block:: bash

    testdb2=> \di+ mytable1_indx1 
                                                    List of relations
       Schema    |      Name      | Type  |  Owner   |  Table   | Persistence | Access method |  Size  | Description 
    -------------+----------------+-------+----------+----------+-------------+---------------+--------+-------------
     test_schema | mytable1_indx1 | index | myowner  | mytable1 | permanent   | btree         | 912 kB | 
    (1 row)

Use the ``pg_indexes_size`` function
''''''''''''''''''''''''''''''''''''

The ``pg_indexes_size`` function can be used to query the size for all the indexes that belong to a table.

.. code-block:: bash

    testdb2=> select pg_size_pretty(pg_indexes_size('mytable1')); 
     pg_size_pretty 
    ----------------
     912 kB  
    (1 row)  
    
Get a size for a table and its indices
--------------------------------------
To get disk space usage for a table and its indexes, you can use the ``pg_total_relation_size`` function, which computes the total disk space used by the table, all its indices, and TOAST data:

.. code-block:: bash

    testdb2=> select pg_size_pretty(pg_total_relation_size('mytable1')); 
     pg_size_pretty 
    ----------------
     15 MB
    (1 row)     

.. Warning::
    It is not recommended to use the ``pg_relation_size`` function as it computes the disk space used by only one fork of the relation. To get the total size of all the relation's forks, use higher-level functions ``pg_total_relation_size`` or ``pg_table_size``.

.. Tip::
    WAL files also contribute to the service disk usage. For more information, check :doc:`About PostgreSQL® disk usage </docs/products/postgresql/concepts/pg-disk-usage>`

.. seealso::     
    * `PostgreSQL interactive terminal <https://www.postgresql.org/docs/15/app-psql.html>`_
    * `Database Object Management Functions <https://www.postgresql.org/docs/current/functions-admin.html#FUNCTIONS-ADMIN-DBOBJECT>`_


Related reading
---------------
* :doc:`../howto`
* :doc:`list-dba-tasks`