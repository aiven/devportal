Indexing and data processing
=============================

In this article we look at how ClickHouse works with data and how this differs from other database management systems.
In particular we'll touch on such topics as **data indexing** and **a vector computation engine**.

Understanding ClickHouse approach to data processing will help you learn why ClickHouse is perfect solution for some use cases and an awful choice for others.

ClickHouse is :doc:`a columnar database <columnar-databases>`, this means that ClickHouse can read columns selectively retrieving only necessary information and omitting columns that are not needed for the request. The smaller the number of the columns you read, the faster and more efficient is the performance of the request. If you have to read many or all columns, then using columnar database becomes highly ineffective and we recommend reconsidering this solution.

ClickHouse is designed to process massive chunks of information for a single request. To make this possible it shifts the focus from reading individual lines into scanning massive blocks of data for a request. This happens by using what is called **a vector computation engine**, which reads data in blocks that normally consist of thousands of rows, selected for a small set of columns.

To find a specific block, ClickHouse uses **a primary index**. However, unlike in other systems the primary index in ClickHouse has a couple of distinctive characteristics.

First of all, not every row is indexed. By contrast, indexing happens at every ten thousandth's row (to be precise, **8192nd** is the default suggested value). Such type of index is descriptively called **a sparse index**.

Using sparse indexing has a significant consequence on advantages and limitations of ClickHouse, mainly because such primary key does not ensure uniqueness for a single searched item. Seeing that we index every ten thousandth's item, in order to find a specific individual row we need to iterating over thousands of items. That's why this approach is inadequate when working with individual rows and should be only used to deal when processing millions, or trillions of items.

Another special characteristic of ClickHouse, is that the items are intentionally **physically sorted** on disk. This is done to speed up reading and to prevent jumping across the disk when processing data. However, because you can only use one way to physically sort the items, you can have only one such key per table.

A good index should aim at helping limit number of items we need to read in order to process a query.