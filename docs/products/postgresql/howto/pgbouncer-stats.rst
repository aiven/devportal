Accessing PGBouncer statistics
==============================

PGBouncer is used at Aiven for :doc:`../concepts/pg-connection-pooling`.

Get PGBouncer URL
------------------

PGBouncer URL can be extracted via Aiven Command Line interface with the following command replacing the ``INSTANCE_NAME`` parameter with the name of your instance::

    avn service get INSTANCE_NAME --json | jq -r '.connection_info.pgbouncer'

The output will be similar to the below::

    postgres://avnadmin:xxxxxxxxxxx@demo-pg-dev-advocates.aivencloud.com:13040/pgbouncer?sslmode=require

Connect to PGBouncer
--------------------

Once retrieved the PGBouncer URL, connect to it with the following::

    psql postgres://avnadmin:xxxxxxxxxxx@demo-pg-dev-advocates.aivencloud.com:13040/pgbouncer?sslmode=require

Finally show PGBouncer statistics::

    pgbouncer=# SHOW STATS;

Depending on the load of your database, the output will be similar to::

    database  | total_xact_count | total_query_count | total_received | total_sent | total_xact_time | total_query_time | total_wait_time | avg_xact_count | avg_query_count | avg_recv | avg_sent | avg_xact_time | avg_query_time | avg_wait_time
    -----------+------------------+-------------------+----------------+------------+-----------------+------------------+-----------------+----------------+-----------------+----------+----------+---------------+----------------+---------------
    pgbouncer |                1 |                 1 |              0 |          0 |               0 |                0 |               0 |              0 |               0 |        0 |        0 |             0 |              0 |             0
    (1 row)


.. Tip::
    Run ``SHOW HELP`` to see all available commands. Only read-only access is available, as PGBouncer pools are automatically managed by Aiven.
