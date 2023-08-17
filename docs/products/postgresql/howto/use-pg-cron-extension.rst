Use the PostgreSQL® ``pg_cron`` extension
===========================================

``pg_cron`` is a simple cron-based job scheduler for PostgreSQL (10 or higher) that runs inside the database as an extension. It uses the same syntax as regular cron, but it allows you to schedule PostgreSQL commands directly from the database. You can also use '[1-59] seconds' to schedule a job based on an interval.

.. note:: 
	``pg_cron`` can run multiple jobs in parallel, but it runs at most one instance of a job at a time. If a second run is supposed to start before the first one finishes, then the second run is queued and started as soon as the first run completes.

The schedule uses the standard cron syntax, where an asterisk (*) signifies "execute at every time interval", and a specific number indicates "execute exclusively at this specific time":

::

       	┌───────────── min (0 - 59)
	│ ┌────────────── hour (0 - 23)
	│ │ ┌─────────────── day of month (1 - 31)
	│ │ │ ┌──────────────── month (1 - 12)
	│ │ │ │ ┌───────────────── day of week (0 - 6) (0 to 6 are Sunday to
	│ │ │ │ │                  Saturday, or use names; 7 is also Sunday)
	│ │ │ │ │
	│ │ │ │ │
	* * * * *

Enable ``pg_cron`` for specific users
--------------------------------------------

To use the ``pg_cron`` extension: 

1. Connect to the database as ``avnadmin`` user and make sure to use the ``defaultdb`` database
:: 

	CREATE EXTENSION pg_cron;

2. As a optional step, you can grant usage permission to regular users
::	
	
	GRANT USAGE ON SCHEMA cron TO janedoe;




Setup the cron job
------------------

List all the jobs
```````````````````
To view the full list of existing jobs, you can run the following query:

::

	postgres=> SELECT * FROM cron.job;
	jobid | schedule    | command                        | nodename  | nodeport | database | username  | active | jobname
	------+-------------+--------------------------------+-----------+----------+----------+-----------+--------+-------------------------
	106   | 29 03 * * * | vacuum freeze test_table       | localhost | 8192     | database1| adminuser | t      | database1 manual vacuum
	  1   | 59 23 * * * | vacuum freeze pgbench_accounts | localhost | 8192     | postgres | adminuser | t      | manual vacuum
	(2 rows)  


Schedule a job
```````````````
You can schedule a new job with the following command. In this example, the job is set to vacuum daily at 10:00am (GMT):

::

	###Vacuum every day at 10:00am (GMT)
	SELECT cron.schedule('nightly-vacuum', '0 10 * * *', 'VACUUM');


Unschedule a job
``````````````````
To stop scheduling a job, you have two options:

1. By using the ``jobname``:

::

	###Stop scheduling jobs using jobname
	SELECT cron.unschedule('nightly-vacuum' );

2. By using the ``jobid``:

::

	###Stop scheduling jobs using jobid
	SELECT cron.unschedule(1);

  
View completed jobs
```````````````````````
To view a list of all completed job runs, you can use the following query:

::

	select * from cron.job_run_details order by start_time desc limit 5;
	+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	¦ jobid ¦ runid ¦ job_pid ¦ database ¦ username ¦      command      ¦  status   ¦  return_message  ¦          start_time           ¦           end_time            ¦
	+-------+-------+---------+----------+----------+-------------------+-----------+------------------+-------------------------------+-------------------------------¦
	¦    10 ¦  4328 ¦    2610 ¦ postgres ¦ marco    ¦ select process()  ¦ succeeded ¦ SELECT 1         ¦ 2023-02-07 09:30:00.098164+01 ¦ 2023-02-07 09:30:00.130729+01 ¦
	¦    10 ¦  4327 ¦    2609 ¦ postgres ¦ marco    ¦ select process()  ¦ succeeded ¦ SELECT 1         ¦ 2023-02-07 09:29:00.015168+01 ¦ 2023-02-07 09:29:00.832308+01 ¦
	¦    10 ¦  4321 ¦    2603 ¦ postgres ¦ marco    ¦ select process()  ¦ succeeded ¦ SELECT 1         ¦ 2023-02-07 09:28:00.011965+01 ¦ 2023-02-07 09:28:01.420901+01 ¦
	¦    10 ¦  4320 ¦    2602 ¦ postgres ¦ marco    ¦ select process()  ¦ failed    ¦ server restarted ¦ 2023-02-07 09:27:00.011833+01 ¦ 2023-02-07 09:27:00.72121+01  ¦
	¦     9 ¦  4320 ¦    2602 ¦ postgres ¦ marco    ¦ select do_stuff() ¦ failed    ¦ job canceled     ¦ 2023-02-07 09:26:00.011833+01 ¦ 2023-02-07 09:26:00.22121+01  ¦
	+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	(10 rows)

