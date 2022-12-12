ClickHouse® |beta|
==================

.. note::
   The Aiven for ClickHouse® service is currently available as a beta release and is intended for **non-production use**.

What is Aiven for ClickHouse®?
------------------------------

Aiven for ClickHouse® beta is powered by `ClickHouse <https://clickhouse.com/>`_, a highly scalable, open source database that uses a column-oriented structure. ClickHouse is designed for online analytical processing (OLAP) applications, and is an ideal tool for applications such as web analytics, or complex data reporting.

In OLAP scenarios, a column-oriented structure provides much quicker processing of queries compared to row-oriented databases, as it reduces the input/output load by minimizing the amount of data that needs to be read and by improving data compression. To optimize data compression, ClickHouse provides both general-purpose compression codecs and codecs that are tailored for specific data types. ClickHouse also includes a vector computation engine to process the columns by vectors, or parts of columns, to increase CPU efficiency and performance.


Why ClickHouse?
---------------

ClickHouse is ideal for performing detailed analytics on large datasets. If your data is high volume, usually inserted in batches, and then rarely updated or deleted, then ClickHouse could be an excellent choice. Tables can be configured with a TTL (Time To Live) so that data will be deleted after a defined interval, this stops the tables growing in an unconstrained way.

ClickHouse is designed for analytics, so if your data is used in many different reports, including very large or complex ones that use multiple data dimensions then it could be a good fit. It isn't optimised for reports that join between source tables; much like other data warehouse solutions, data may be transformed before being inserted, to prepare for the reports that will be run.

ClickHouse supports a familiar SQL syntax that resembles the ANSI SQL standard. There are however some differences in behavior, which are listed in the `ClickHouse documentation <https://clickhouse.com/docs/en/sql-reference/ansi/>`_.


Get started with Aiven for ClickHouse
-------------------------------------

Take your first steps with Aiven for ClickHouse by following our :doc:`getting started </docs/products/clickhouse/getting-started>` article, or browse through our full list of articles:


.. grid:: 1 2 2 2

    .. grid-item-card::
        :shadow: md
        :margin: 2 2 0 0

        📚 :doc:`Concepts </docs/products/clickhouse/concepts>`

    .. grid-item-card::
        :shadow: md
        :margin: 2 2 0 0

        💻 :doc:`/docs/products/clickhouse/howto`

    .. grid-item-card::
        :shadow: md
        :margin: 2 2 0 0

        📖 :doc:`/docs/products/clickhouse/reference`


ClickHouse resources
--------------------

If you are new to ClickHouse, try these resources to get you started with the platform:

* See the `main ClickHouse documentation <https://clickhouse.com/docs/en/>`_ for an introduction and a full list of features.

* Our :doc:`/docs/products/clickhouse/getting-started` guide is a good way to get hands on with your first project.

* Follow :doc:`a guide to add a sample dataset </docs/products/clickhouse/sample-dataset>` to your service.

* Find out :doc:`how to use the web-based query editor </docs/products/clickhouse/howto/query-databases>`, that comes as part of the ClickHouse service.
