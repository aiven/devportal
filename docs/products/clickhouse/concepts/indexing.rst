Indexing and data processing
=============================

In this article we look at how ClickHouse works with data and how this differs from other database management systems (DBMS).
In particular we'll touch on such topics as **data indexing** and **a vector computation engine**.
Understanding the ClickHouse approach to data processing will help you learn why ClickHouse is perfect solution for some use cases and an awful choice for others.

ClickHouse is a columnar database. This means that ClickHouse can read columns selectively retrieving only necessary information and omitting columns that are not needed for the request. The smaller the number of the columns you read, the faster and more efficient the performance of the request. If you have to read many or all columns, then using a columnar database becomes a less effective approach.

.. note:: Read more about columnar databases :doc:`in our separate article <columnar-databases>`.

ClickHouse is designed to process substantial chunks of information for a single request. To make this possible it shifts the focus from reading individual lines into scanning massive blocks of data for a request. This happens by using what is called **a vector computation engine**, which reads data in blocks that normally consist of thousands of rows, selected for a small set of columns.

ClickHouse primary index
------------------------

To find a specific block, ClickHouse uses **a primary index**. However, unlike in other systems the primary index in ClickHouse has a couple of distinctive characteristics.

First of all, not every row is indexed. By contrast, ClickHouse indexes every 10000th row (or, to be precise, the **8192nd**, when using default settings). Such type of index is descriptively called **a sparse index** and a batch of rows is sometimes called **a granule**.

To make **sparse indexing** possible, ClickHouse sorts items according to the primary key. In fact, items are intentionally **sorted physically** on disk. This is done to speed up reading and to prevent jumping across the disk when processing data. Therefore, by selecting a primary key we determine how items are sorted physically on disk. Such an approach helps ClickHouse effectively work on regular hard drives and depend less on SSD in comparison to other DBMS.

.. note:: Even though ClickHouse sorts data by primary key, it is possible `to choose a primary key that is different than the sorting key <https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree/#choosing-a-primary-key-that-differs-from-the-sorting-key>`_.

Using sparse indexing has significant consequences for the advantages and limitations of ClickHouse, mainly because such a primary key does not ensure uniqueness for a single searched item. Seeing that we index every ten thousandth item, in order to find a specific individual row we need to iterate over thousands of items. That's why this approach is inadequate when working with individual rows and should be only used to deal when processing millions, or trillions, of items.

A good use case for it, for example, is analysing error rates based on server log analysis. In such cases we don't  center our attention on individual lines, but look at the overall picture to see trends. Such requests also allow approximate calculations, using only sample of data to make conclusions.

A good primary index should aim at helping limit number of items we need to read in order to process a query.

.. tip:: Find more about ClickHouse `primary indexes in the official documentation of ClickHouse <https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree/#choosing-a-primary-key-that-differs-from-the-sorting-key>`_.

ClickHouse data skipping indexes
--------------------------------

**Skipping indexes** are the secondary indexes in ClickHouse. However, they work quite differently to the secondary indexes we are using in other DBMS.

Such indexes help boost performance by skipping in advance some irrelevant rows, when we can predicted that these rows will not satisfy query conditions.

For example, imagining that you have a numeric column **number of page visits** and run a query to select all rows where page visits are over 10K. To speed up such query, you can add a skipping index to store extremes of the field and help ClickHouse to skip in advance values that won't satisfy the request condition.

.. tip:: Find more about `skipping indexes in the official documentation of ClickHouse <https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree/#table_engine-mergetree-data_skipping-indexes>`_.

