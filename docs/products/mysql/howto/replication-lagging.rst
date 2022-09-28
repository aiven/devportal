Identify lagging MySQL replication
==================================

Here are some strategies to find out MySQL replication lagging on your Aiven for MySQL service.

Query locks on the standby node
-------------------------------

Another reason you may face replication lagging is when a row or table is locked. If this happens your replication will not progress. 

Run the following command to check if the table level is locked::

    mysql> show processlist

The result is a list of current processes with their statuses. If a query is causing others to lock, you should be able to identify it. The query that is causing the others queries to lock will show as waiting for another process, possibly a temporary table. The output may look like this: 

.. code::

    +-------+-----------------+------------------------------+--------+---------+-------+---------------------------------+-----------------------------------------------------------------------------------------------------+
    | Id    | User            | Host                         | db     | Command | Time  | State                           | Info                                                                                                
    |  1800 | avnadmin        | HOST_IP:53938                | teammy | Query   | 58798 | Waiting for table metadata lock | /* ApplicationName=DataGrip 2020.3.2 */ LOCK TABLES users WRITE


If nothing shows up there, you may find them by showing the open tables::

    show open tables where In_Use > 0


Another way is to check the InnoDB status by running::

    show engine innodb status

This will show you the locking query, and the affected rows and tables. On the output, you can check for the section ``TRANSACTION`` to find this information. There are also cases where multiple queries and load can cause replication problems.

Long running transactions
-------------------------

Long running transactions with large binlogs can result in replication problems. You can find replication problems in this case by checking the time since the process is in progress. Once the binlog has been replicated, the standby node will be stuck processing one massive ``GTID``. If ``Read_Source_Log_Pos`` in the output is updating, this requires no further action from your side. You should leave the replication process to continue without interferring in the service.


No disk space on the standby
----------------------------

You can run the command ``show processlist`` to find if there is a disk space issue::


    mysql> show processlist;


If there is an issue with the disk space, you may find similar output:

.. code::

    +---------+-----------------+-------------------------------+-------+---------+---------+----------------------------+--------------------------------------+
    | Id      | User            | Host                          | db    | Command | Time    | State                      | Info                                 |
    +---------+-----------------+-------------------------------+-------+---------+---------+----------------------------+--------------------------------------+
    |      17 | system user     | connecting host               | NULL  | Connect | 4789695 | Waiting for disk space     | NULL                                 |


.. seealso::

    Consider reading how to :doc:`reclaim disk space </docs/products/mysql/howto/reclaim-disk-space>` if you are having issues with full disk.