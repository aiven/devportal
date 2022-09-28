Identify lagging MySQL replication
==================================

Here are some strategies to find out MySQL replication lagging on your Aiven for MySQL service.

Query locks on the standby node
-------------------------------

A replication might face lagging when a row or table is locked. If this happens your replication will not progress. 

Run the following command to check if the table level is locked::

    show processlist

The result is a list of current processes with their statuses. If a query is causing others to lock, you should be able to identify it. The query that is causing the others queries to lock will show as waiting for another process, possibly a temporary table. The output may look like this (check the ``State`` column): 

.. code::

    +-------+-----------------+------------------------------+--------+---------+-------+---------------------------------+-----------------------------------------------------------------------------------------------------+
    | Id    | User            | Host                         | db     | Command | Time  | State                           | Info                                                                                                
    |  1800 | avnadmin        | HOST_IP:53938                | teammy | Query   | 58798 | Waiting for table metadata lock | /* ApplicationName=DataGrip 2020.3.2 */ LOCK TABLES users WRITE


If no query seems being locked, you may find other table locks by showing the open tables::

    show open tables where In_Use > 0


Or by checking the InnoDB status::

    show engine innodb status

The above command shows the locking query, and the affected rows and tables. On the output, you can check for the section ``TRANSACTION`` to find this information. 

.. Note::
    There are also cases where multiple queries and load can cause replication problems.

Long running transactions
-------------------------

Long running transactions with large binary logs can result in replication problems. To find these kind of replication problems check the time since the process is in progress. 

Once the binary log has been replicated, the standby node will be stuck processing one specific global transaction identifier  (``GTID``). If the ``GTID`` mentioned in the ``Read_Source_Log_Pos`` output is updating, the replication is progressing therefore requires no further action from your side.


No disk space on the standby
----------------------------

An alternative cause of lagging replication could be the missing space on the target standby database. You can check disk space issues with::


    show processlist;


If there is an issue with the disk space, you may find similar output:

.. code::

    +---------+-----------------+-------------------------------+-------+---------+---------+----------------------------+--------------------------------------+
    | Id      | User            | Host                          | db    | Command | Time    | State                      | Info                                 |
    +---------+-----------------+-------------------------------+-------+---------+---------+----------------------------+--------------------------------------+
    |      17 | system user     | connecting host               | NULL  | Connect | 4789695 | Waiting for disk space     | NULL                                 |


.. seealso::

    Consider reading how to :doc:`reclaim disk space </docs/products/mysql/howto/reclaim-disk-space>` if you are having issues with full disk.