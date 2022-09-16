MySQL replication lagging
=========================

Replication status
------------------

Find the replication by running the command on the standby node:

.. code::

    mysql> show slave statusG

With this command, you can find information about the configuration and status of the connection between the replica server and the source server. 

.. code::

    *************************** 1. row *************************** 
    Replica_IO_State: Waiting for master to send event 
    Source_Host: SOURCE_IP
    Source_User: repluser 
    Source_Port: 23343 
    Connect_Retry: 60 
    Source_Log_File: binlog.000904 
    Read_Source_Log_Pos: 1248490291 
    Relay_Log_File: relay.001821 
    Relay_Log_Pos: 405 
    Relay_Source_Log_File: binlog.000904 
    Replica_IO_Running: Yes 
    Replica_SQL_Running: Yes 
    Replicate_Do_DB: 
    Replicate_Ignore_DB: 
    Replicate_Do_Table: 
    Replicate_Ignore_Table: 
    Replicate_Wild_Do_Table: 
    Replicate_Wild_Ignore_Table: 
    Last_Errno: 0 
    Last_Error: 
    Skip_Counter: 0 
    Exec_Source_Log_Pos: 196 
    Relay_Log_Space: 1248490783 
    Until_Condition: None 
    Until_Log_File: 
    Until_Log_Pos: 0 
    Source_SSL_Allowed: Yes 
    Source_SSL_CA_File: /etc/pki/service-provider-ca-bundle.crt Source_SSL_CA_Path: 
    Source_SSL_Cert: 
    Source_SSL_Cipher: 
    Source_SSL_Key: 
    Seconds_Behind_Source: 1728 
    Source_SSL_Verify_Server_Cert: No 
    Last_IO_Errno: 0 
    Last_IO_Error: 
    Last_SQL_Errno: 0 
    Last_SQL_Error: 
    Replicate_Ignore_Server_Ids: 
    Source_Server_Id: SERVER_ID 
    Source_UUID: c6e12e9e-ac75-11eb-8cc8-42010af00009 
    Source_Info_File: mysql.slave_master_info 
    SQL_Delay: 0 
    SQL_Remaining_Delay: NULL 
    Replica_SQL_Running_State: Slave has read all relay log; waiting for more updates 
    Source_Retry_Count: 86400 
    Source_Bind: 
    Last_IO_Error_Timestamp: 
    Last_SQL_Error_Timestamp: 
    Source_SSL_Crl: 
    Source_SSL_Crlpath: 
    Retrieved_Gtid_Set: c6e12e9e-ac75-11eb-8cc8-42010af00009:28-1252 
    Executed_Gtid_Set: c6e12e9e-ac75-11eb-8cc8-42010af00009:1-1252 
    Auto_Position: 1 
    Replicate_Rewrite_DB: 
    Channel_Name: 
    Source_TLS_Version: 
    Source_public_key_path: 
    Get_Source_public_key: 0 
    Network_Namespace:


To find replication problems, you need to check for the lag ``transactions/seconds`` metric, they are calculated by connecting to the master node and comparing GTIDs, the ``Retrieved_Gtid_Set`` on the output, then you check the time between the last and the newest. This approach will give a better indication of lag, since a long running transaction on the primary when viewed from the point of the standby would seem like nothing is happening and there is no need to replicate.

``Seconds_Behind_Source`` as shown in the output is not a reliable indicator of lag for monitoring, but is still useful. Details can be found here. You can also run the following query to see if replication is currently performing any work on the standby node. For example, if there are tasks which are not progressing, this can indicate an issue.

.. code::

    SELECT * FROM performance_schema.events_stages_current WHERE EVENT_NAME LIKE 'stage/sql/Applying batch of row changes%'

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