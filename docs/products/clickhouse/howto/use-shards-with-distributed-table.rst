Work with shards in ClickHouse®
=================================

Learn why and how use shards and find out how shards get allocated to Aiven services.

About sharding
--------------

Sharding is a mechanism for splitting a database into shards across multiple servers. A shard is a horizontal partition of data consisting of one or more replicas. Each replica of the shard can handle queries sent to this shard since there's no master. Sharding enables horizontal cluster scaling, which helps spread out the load, increase processing speed, and support more traffic.

Enable shards
-------------

With Aiven services, shards are created automatically when the service is created. The number of shards that your service gets depends on the plan you select for your service. You can calculate the shards number as follows:

.. math::

  number\_of\_shards = number\_of\_nodes / 3

Use shards
----------

**Prerequisites**

Create cluster *test-cluster* with 5 shards and database *test-db*.

Create a distributed table
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. topic:: Shards vs. distributes tables

    If your service uses multiple shards, the data is replicated only between nodes of the same shard. For example, if you have six nodes and you write to one node, the data is present in the three nodes that are part of the same shard and missing from the three other nodes. Using ``http://project-name-service-name.avns.net/`` for connecting to your service, you connect to one node at random with no knowledge of which shard you read from or write to. When you read from one node, you see the data from the shard of this node but cannot see the data from the other shards. To be able to see all the data, you need to create a `distributed table <https://clickhouse.com/docs/en/engines/table-engines/special/distributed/>`_ on top of your replicated table. As a result, when you connect on one node and read from the distributed table, ClickHouse® aggregates the data from all the shards and return it all. Similarly, if you insert data into the distributed table, ClickHouse decides on which node the data should be stored and write it to the correct node. This is required to ensure that a similar volume of data is written on all the nodes.

1. :doc:`Connect to your database </docs/products/clickhouse/howto/connect-to-ch-service>`.

2. Create a table with the `MergeTree engine <https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree/>`_ as shown for the ``cash-flows`` table in the following example:

    .. code:: sql

        CREATE TABLE test-db.cash-flows
        ( 
        `<table structure>` 
        )
        ENGINE = MergeTree()
        PARTITION BY toYYYYMM(EventDate)
        ORDER BY (CounterID, EventDate)

.. note::

    ``<table structure>`` is for describing columns and their data types as per the `ClickHouse documentation <https://clickhouse.com/docs/en/tutorial/>`_.

3. Create distributed table ``cash-flows_distributed`` with the distributed engine.

.. code:: sql

    CREATE TABLE test-db.cash-flows_distributed AS test-db.data_table1
    ENGINE = Distributed(test-db, cash-flows, rand())

.. tip::
    
    You can use ``AS test-db.cash-flows`` to copy the structure of the initial table created earlier instead of explicitly describing the table structure. 

Verify your distributed table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To check that the distributed table you created is available, run a query for the number of table rows.

.. code:: sql

    SELECT count() FROM test-db.cash-flows_distributed

.. Topic:: Result
    
     As a response to this query, you can expect to receive a number.
