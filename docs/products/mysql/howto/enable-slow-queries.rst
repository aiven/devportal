Enable slow query logging
=========================

You can identify inefficient or time-consuming queries by enabling `slow query log <https://dev.mysql.com/doc/refman/5.7/en/slow-query-log.html>`_ in your Aiven for MySQL® service. In this article, you'll find out how to enable slow queries in your Aiven for MySQL service.

Prerequisites
-------------

You need an Aiven organization with an Aiven for MySQL service running.

Configure slow queries in Aiven Console
---------------------------------------


Follow these steps to enable your slow queries in your Aiven for MySQL service via `Aiven Console <https://console.aiven.io/>`_:

1. Log in to `Aiven Console <https://console.aiven.io/>`_.
2. In the **Services** page, select your Aiven for MySQL service.
3. In the **Overview** page of your service, scroll down to the **Advanced configuration** section and select **Change**.
4. In the **Edit advanced configuration** window

   1. Select **Add configuration option**. From the unfolded list, choose ``mysql.slow_query_log``. Enable ``mysql.slow_query_log`` by toggling it to ``On``. By default, ``mysql.slow_query_log`` is disabled.
   2. Select **Add configuration option**. From the unfolded list, choose ``mysql.long_query_time``. Set ``mysql.long_query_time`` according to your specific need.
   3. Select **Save advanced configuration**.

Your Aiven for MySQL service can now log slow queries. If you want to simulate slow queries to check this feature, check the next section.

.. warning::

    Aiven managed MySQL services use table output for the slow query log.
    This means that the slow query log will not function on a read-only replica.

Simulate slow queries
---------------------

Connect to your Aiven for MySQL using your favorite tool. Make sure you have ``mysql.slow_query_log`` enabled and set ``mysql.long_query_time`` to ``2`` seconds. Now, you can run the following query to simulate a slow query of 3 seconds.

.. code-block:: shell

    select sleep(3);

You should see the following output:

.. code-block:: shell

    +----------+
    | sleep(3) |
    +----------+
    | 0        |
    +----------+
    1 row in set (3.03 sec)

Now, you can check the logs of your slow query:

.. code-block:: shell

    select convert(sql_text using utf8) as slow_query, query_time from mysql.slow_log;

You can expect to receive an output similar to the following:

.. code-block:: shell

    +-----------------+-----------------+
    | slow_query      | query_time      |
    +-----------------+-----------------+
    | select sleep(3) | 00:00:03.000450 |
    +-----------------+-----------------+
    1 row in set, 1 warning (0.03 sec)

.. warning::

   Disabling the ``mysql.slow_query_log`` setting truncates the ``mysql.slow_query_log`` table. Make sure to back up the data from the ``mysql.slow_query_log`` table in case you need it for further analysis.


