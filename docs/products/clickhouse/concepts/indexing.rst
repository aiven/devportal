Indexing and data processing in ClickHouse®
===========================================

This article helps you understand how ClickHouse® processes data and how it differs from the way the other database management systems (DBMS) do that. Discover spare and skipping indexes and check out what the vector computation engine is used for.

ClickHouse as a columnar database
---------------------------------

ClickHouse is a columnar database, which means that ClickHouse can read columns selectively retrieving only necessary information and omitting columns that are not needed for the request. The smaller the number of the columns you read, the faster and more efficient the performance of the request. If you have to read many or all columns, using a columnar database becomes a less effective approach.

.. seealso::
    
    Read more about characteristics of columnar databases and their features in :doc:`Columnar databases <columnar-databases>`.

Reading data in blocks
----------------------

ClickHouse is designed to process substantial chunks of information for a single request. To make this possible, it shifts the focus from reading individual lines into scanning massive blocks of data for a request. This happens by using what is called the vector computation engine, which reads data in blocks that normally consist of thousands of rows selected for a small set of columns.

ClickHouse primary index
------------------------

ClickHouse reads data in blocks. To find a specific block, ClickHouse uses its primary index, which has a few distinctive features that makes it different from primary indexes of the other systems.

Instead of indexing every row, ClickHouse indexes very 10000th row (or, to be precise, every 8192nd row when using default settings). Such type of index is descriptively called *sparse index* and the batch of rows is sometimes called *granule*.

To make sparse indexing possible, ClickHouse sorts items according to the primary key. The items are intentionally sorted physically on the disk to speed up reading and prevent jumping across the disk when processing data. Therefore, by selecting a primary key, you determine how items are sorted physically on the disk. Such an approach helps ClickHouse effectively work on regular hard drives and depend less on SSD in comparison to other DBMSs.

.. note::
    
    Even though ClickHouse sorts data by primary key, it is possible `to choose a primary key that is different from the sorting key <https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree/#choosing-a-primary-key-that-differs-from-the-sorting-key>`_.

Using sparse indexing has significant consequences for capabilities and limitations of ClickHouse. A primary key as used in ClickHouse do not ensure uniqueness for a single searched item since only every ten thousandth item is indexed. Thus, you need to iterate over thousands of items to find a specific row, which makes this approach inadequate when working with individual rows and suitable for processing millions or trillions of items.

.. topic:: Example

    When analysing error rates based on a server log analysis, you don't focus on individual lines but look at the overall picture to see trends. Such requests allow approximate calculations using only a sample of data to draw conclusions.

A good primary index should help limit the number of items you need to read to process a query.

.. tip::
    
    Learn more about ClickHouse `primary indexes in the official documentation of ClickHouse <https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree/#choosing-a-primary-key-that-differs-from-the-sorting-key>`_.

ClickHouse data skipping indexes
--------------------------------

Skipping indexes are secondary indexes in ClickHouse, but they work quite differently to the secondary indexes used in other DBMSs.

Skipping indexes help boost performance by skipping some irrelevant rows in advance, when it can be predicted that these rows do not satisfy query conditions.

.. topic:: Example

    You have numeric column *number of page visits* and run a query to select all rows where page visits are over 10000. To speed up such a query, you can add a skipping index to store extremes of the field and help ClickHouse to skip in advance values that do not satisfy the request condition.

.. tip::
    
    Learn more about `skipping indexes in the official documentation of ClickHouse <https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree/#table_engine-mergetree-data_skipping-indexes>`_.
