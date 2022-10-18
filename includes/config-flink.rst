
``additional_backup_regions``
-----------------------------
*array*

**Additional Cloud Regions for Backup Replication** 



``ip_filter``
-------------
*array*

**IP filter** Allow incoming connections from CIDR address block, e.g. '10.20.0.0/16'



``flink_version``
-----------------
*['string', 'null']*

**Flink major version** 



``number_of_task_slots``
------------------------
*integer*

**Flink taskmanager.numberOfTaskSlots** Task slots per node. For a 3 node plan, total number of task slots is 3x this value



``parallelism_default``
-----------------------
*integer*

**Flink parallelism.default** How many parallel task slots each new job is assigned. Unless you understand how Flink parallel dataflows work, please leave this at 1. Please do not set this value higher than (total number of nodes x number_of_task_slots), or every new job created will fail.



``privatelink_access``
----------------------
*object*

**Allow access to selected service components through Privatelink** 

``flink``
~~~~~~~~~
*boolean*

**Enable flink** 

``prometheus``
~~~~~~~~~~~~~~
*boolean*

**Enable prometheus** 



``restart_strategy``
--------------------
*string*

**Flink restart-strategy** failure-rate (default): Restarts the job after failure, but when failure rate (failures per time interval) is exceeded, the job eventually fails. Restart strategy waits a fixed amount of time between attempts.fixed-delay: Attempts to restart the job a given number of times before it fails. Restart strategy waits a fixed amount of time between attempts. exponential-delay: Attempts to restart the job infinitely, with increasing delay up to the maximum delay. The job never fails. none: The job fails directly and no restart is attempted.



``restart_strategy_max_failures``
---------------------------------
*integer*

**Flink restart-strategy.failure-rate.max-failures-per-interval** The number of times that Flink retries the execution before the job is declared as failed if restart-strategy has been set to fixed-delay or failure-rate.



``restart_strategy_failure_rate_interval_min``
----------------------------------------------
*integer*

**Flink restart-strategy.failure-rate.failure-rate-interval in minutes** Time interval for measuring failure rate if restart-strategy has been set to failure-rate. Specified in minutes.



``restart_strategy_delay_sec``
------------------------------
*integer*

**Flink restart-strategy.failure-rate.delay in seconds** Delay between two consecutive restart attempts if restart-strategy has been set to fixed-delay or failure-rate. Delaying the retries can be helpful when the program interacts with external systems where for example connections or pending transactions should reach a timeout before re-execution is attempted.



``execution_checkpointing_interval_ms``
---------------------------------------
*integer*

**Flink execution.checkpointing.interval in milliseconds** Checkpointing is Flink’s primary fault-tolerance mechanism, wherein a snapshot of your job’s state persisted periodically to some durable location. In the case of failure, Flink will restart from the most recent checkpoint and resume processing. A jobs checkpoint interval configures how often Flink will take these snapshots.



``execution_checkpointing_timeout_ms``
--------------------------------------
*integer*

**Flink execution.checkpointing.timeout in milliseconds** The time after which a checkpoint-in-progress is aborted, if it did not complete by then.



