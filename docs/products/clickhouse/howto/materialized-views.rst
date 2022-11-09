Create materialized views in ClickHouse®
========================================

About materialized views
------------------------

One way of integrating your ClickHouse® service with Kafka® is using the Kafka® table engine, which enables, for example, inserting data into ClickHouse® from Kafka.

In such a scenario, ClickHouse can read from a Kafka® topic directly. This is, however, one-time retrieval so the data cannot be re-read. When a new block of data is inserted in a table (whether the table is backed by a MergeTree or Kafka® engine), the table expression defined by the materialized view is triggered with the block of data. With Kafka®, the block of data lives in a buffer in memory and the trigger *flushes* the buffer. For this reason, the data consumed from the topic by the Kafka® engine cannot be read twice.

Persisting the data from the Kafka ®table engine read requires capturing and inserting it into a different table. Here's where materialized views come in. A materialized view triggers a read on the table engine. The destination of the data (for example, a Merge Tree family table) is defined by the TO clause. This process is illustrated in the following diagram:

.. mermaid::

   flowchart LR
      a[Kafka topic]
      b{{Kafka table engine}}
      c[Materialized view]
      d{{Merge Tree<br /> family table}}
      a --> b --> c --> d

Create a materialized view
--------------------------

To store the Kafka® messages by creating a materialized view on top of the Kafka® table, you need to run the following query:

.. code:: sql

    CREATE MATERIALIZED VIEW default.my_view TO destination_name
    ENGINE = ReplicatedMergeTree
    ORDER BY x AS SELECT x,y FROM service_kaf.table_name

.. note::

    All ClickHouse® nodes share the same consumer group: Each message is consumed and stored by a single node. However, since materialized views use the ReplicatedMergeTree engine, the stored messages are exchanged and replicated across all the nodes.

.. seealso::

    For more information on how to integrate Aiven for ClickHouse® with Apache Kafka®, see :doc:`Connect Apache Kafka® to Aiven for ClickHouse® </docs/products/clickhouse/howto/integrate-kafka>`.
