Enable slow queries 
===================

You can identify inefficient or time-consuming queries by enabling `slow queries <https://dev.mysql.com/doc/refman/5.7/en/slow-query-log.html>` in your MySQL service. In this tutorial, you can find how can you enable slow queries in your Aiven for MySQL service.

Prerequisites
-------------

* An Aiven account with an Aiven for MySQL service running.

Configure slow queries
----------------------

Follow the steps to enable your slow queries in your Aiven for MySQL service:

1. On the **Overview** page, scroll down to the **Advanced configuration** section and click **Add configuration option**.
2. Click **Add configuration option** and choose the ``slow_query_log``. 
3. Enable ``slow_query_log`` by toggling it to On. By default, ``slow_query_log`` is disabled.
4. Click **Add configuration option** and choose the ``long_query_time``. 
5. Set ``long_query_time`` according to your use case. By default, the value is 10 seconds.
6. Click **Save advanced configuration**

Your Aiven for MySQL can now log slow queries. If you want to simulate slow queries to check this feature, check the next section for that.

Simulate slow queries
---------------------

Connect to your Aiven for MySQL using your favorite tool. Make sure to have ``slow_query_log`` enabled and set ``long_query_time``, in seconds, for ``2``. Now, you can run the following query to simulate a slow query of 3 seconds.

.. code::

    select sleep(3);

You should see this as output:

.. code::

    +----------+
    | sleep(3) |
    +----------+
    | 0        |
    +----------+
    1 row in set (3.03 sec)

Now, you can check the logs of your slow query:

.. code::

    select convert(sql_text using utf8) as slow_query, query_time from mysql.slow_log;

You can see the logs in the output:

.. code::

    +-----------------+-----------------+
    | slow_query      | query_time      |
    +-----------------+-----------------+
    | select sleep(3) | 00:00:03.000450 |
    +-----------------+-----------------+
    1 row in set, 1 warning (0.03 sec)

.. warning::

   Disabling the ``slow_query_logging`` setting will truncate ``mysql.slow_log table``. Make sure to back up the data from ``mysql.slow_log`` table in case you need it for further analysis.
