Get database, table and index disk space usage
===============================================

PostgreSQL® offers different commands and functions to get the database and object disk space usage, which could cause some confusion as the result may vary depending on the function used. 
This article will show some of the available commands and functions that can be used and the difference among them.  

Get database size
-----------------
The database size can be retrieved using the following psql command ``\l+ [ pattern ]``:: 

    testdb2=> \l+
                                                                     List of databases   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   |   Size    | Tablespace |            Description             
    -----------+----------+----------+-------------+-------------+-----------------------+-----------+------------+------------------------------------
     _aiven    | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =T/postgres          +| No Access | pg_default | 
    .....
     testdb2   | avnadmin | UTF8     | en_US.UTF-8 | en_US.UTF-8 |                       | 66 MB     | pg_default | 
    (6 rows)
    
    testdb2=> \l+ testdb2
                                                    List of databases
      Name   |  Owner   | Encoding |   Collate   |    Ctype    | Access privileges | Size  | Tablespace | Description 
    ---------+----------+----------+-------------+-------------+-------------------+-------+------------+-------------
     testdb2 | avnadmin | UTF8     | en_US.UTF-8 | en_US.UTF-8 |                   | 66 MB | pg_default | 
    (1 row)

An alternative to get the database size is to use the ``pg_database_size`` function::

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

As shown on the examples above the output for the database **testdb2** size is the same, though the ``pg_database_size`` function will return the database size in bytes, so we used the ``pg_size_pretty`` function to return an easy to read output, we will keep using it in the coming examples. 

Get table size
--------------
In order to get the table size the ``\dt+ [ pattern ]`` command can be used::

    testdb2=> \dt+ mytable1
                                           List of relations
       Schema    |   Name   | Type  |  Owner   | Persistence | Access method | Size  | Description 
    -------------+----------+-------+----------+-------------+---------------+-------+-------------
     test_schema | mytable1 | table | myowner  | permanent   | heap          | 14 MB | 
    (1 row)


The function ``pg_table_size`` can be used to get the table size::

    testdb2=> select pg_size_pretty(pg_table_size('mytable1')); 
     pg_size_pretty 
    ----------------
     14 MB
    (1 row)

Get index size
--------------
Individual index size can be retrieved using the command ``\di+ [ pattern ]``::

    testdb2=> \di+ mytable1_indx1 
                                                    List of relations
       Schema    |      Name      | Type  |  Owner   |  Table   | Persistence | Access method |  Size  | Description 
    -------------+----------------+-------+----------+----------+-------------+---------------+--------+-------------
     test_schema | mytable1_indx1 | index | myowner  | mytable1 | permanent   | btree         | 912 kB | 
    (1 row)

The function ``pg_indexes_size`` can be used to query the size for **all the indexes** that belong to a table::

    testdb2=> select pg_size_pretty(pg_indexes_size('mytable1')); 
     pg_size_pretty 
    ----------------
     912 kB  
    (1 row)  
    
Get table and its indexes size
--------------------------------
It is possible to get the disk usage for a table and its corresponding indexes, the function ``pg_total_relation_size`` computes the total disk space used by the specified table, including all indexes and TOAST data::

    testdb2=> select pg_size_pretty(pg_total_relation_size('mytable1')); 
     pg_size_pretty 
    ----------------
     15 MB
    (1 row)     

.. Warning:: 
    It is not recommended to use the ``pg_relation_size`` function as it computes the disk space used by one “fork” of the specified relation. (Note that for most purposes it is more convenient to use the higher-level functions pg_total_relation_size or pg_table_size, which sum the sizes of all forks.)
.. Tip::
    WAL files will also contribute to the service disk usage for additional information see: :doc:`../concepts/pg-disk-usage`.
    
    Relevant documentation is available on following links:  
    `PostgreSQL interactive terminal <https://www.postgresql.org/docs/15/app-psql.html>`_ and
    `Database Object Management Functions <https://www.postgresql.org/docs/current/functions-admin.html#FUNCTIONS-ADMIN-DBOBJECT/>`_
