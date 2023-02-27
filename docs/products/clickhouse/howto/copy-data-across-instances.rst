Copy data from one Aiven for ClickHouse® server to another
==========================================================

This article details how to copy data from one Aiven for ClickHouse® server to another using the `remoteSecure()` function.

Prerequisites
-------------

* Aiven account
* IP of the source (remote) ClickHouse server

Copy data
---------

1. From your target server(s), use the `remoteSecure()` function to select data from the source server.

   .. code-block:: shell

      SELECT * FROM remote('127.0.0.1', db.remote_engine_table) LIMIT 3;

2. Insert the selected data into the target server.

   .. code-block:: shell

      INSERT INTO [db.]table [(c1, c2, c3)] SELECT ...

   .. seealso::

      For details on how to configure and use the INSERT query, see `Inserting the Results of SELECT <https://clickhouse.com/docs/en/sql-reference/statements/insert-into/#inserting-the-results-of-select>`_.

.. topic:: Results

    Your data has been copied from the remote (source) server to the new (target) servier.
