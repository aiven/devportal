Enable reading and writing data across shards in Aiven for ClickHouse®
======================================================================

If your Aiven for ClickHouse® service uses multiple shards, the data is replicated only between nodes of the same shard. When you read from one node, you see the data from the shard of this node. In this article, you'll learn how to create a `distributed table <https://clickhouse.com/docs/en/engines/table-engines/special/distributed/>`_ on top of your replicated table, which will not only allow you to see data from all the shards but also help spread the data evenly across all the cluster nodes.

.. dropdown:: Expand to learn more on what you'll achieve following the steps in this article.

    The expected results of following the instruction are as follows: 

    * When you connect on one node and read from the distributed table, Aiven for ClickHouse® aggregates the data from all the shards and return it all.
    * When you insert data into the distributed table, Aiven for ClickHouse® decides on which node the data should be stored and write it to the correct node, which is required to ensure that a similar volume of data is written on all the nodes.

Set up a sharded service with a database
----------------------------------------

.. note::

    For Aiven for ClickHouse® services, shards are created automatically when the services are created. The number of shards that your service gets depends on the plan you select for your service. You can calculate the shards number as follows: *number of shards = number of nodes / 3*.

1. :doc:`Create an Aiven for ClickHouse® service </docs/platform/howto/create_new_service>` with multiple shards.
2. :ref:`Create database <create-a-clickhouse-database>` *test_db* in your new service.

Create a distributed table
--------------------------

1. :doc:`Connect to your database </docs/products/clickhouse/howto/connect-to-ch-service>`.

2. Create a table with the `MergeTree engine <https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree/>`_ as shown for the ``cash_flows`` table in the following example::

    CREATE TABLE test_db.cash_flows
    ( 
    EventDate DateTime,
    SourceAccount UInt64,
    TargetAccount UInt64,
    Amount Float64
    )
    ENGINE = MergeTree()
    PARTITION BY toYYYYMM(EventDate)
    ORDER BY (EventDate, SourceAccount)

3. Create distributed table ``cash_flows_distributed`` with the distributed engine::

    CREATE TABLE test_db.cash_flows_distributed AS test_db.cash_flows
    ENGINE = Distributed(test_db, test_db, cash_flows, SourceAccount)

Verify your distributed table
-----------------------------

Check if the distributed table you created is available and if you can use it to access your data from all the shards.

1. Run a read query for the number of table rows::

    SELECT count() FROM test_db.cash_flows_distributed

As a response to this query, you can expect to receive a number of rows from all the shards. This is because when you connect on one node and read from the distributed table, Aiven for ClickHouse® aggregates the data from all the shards and return it all.

2. Run a write query to insert new data into the distributed table::

    INSERT INTO test_db.cash_flows_distributed (
        EventDate, SourceAccount, TargetAccount, Amount
    ) VALUES ('2022-01-02 03:04:05', 123, 456, 100.0)

When you insert data into the distributed table, Aiven for ClickHouse® decides on which node the data should be stored and write it to the correct node making sure that a similar volume of data is written on all the nodes.
