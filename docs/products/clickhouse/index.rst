ClickHouse :badge:`beta,cls=badge-secondary text-black badge-pill`
==================================================================

What is Aiven for ClickHouse?
-----------------------------

Aiven for ClickHouse beta is powered by Clickhouse, an open-source database management system that uses a column-oriented structure and is best suited for the online analytical processing of queries (OLAP).

In OLAP scenarios, a column-oriented structure provides much quicker processing of queries compared to row-oriented databases, as it reduces the input/output load by minimizing the amount of data that needs to be read and by improving data compression. To optimize data compression, ClickHouse provides both general-purpose compression codecs and codecs that are tailored for specific data types. ClickHouse also includes a vector computation engine to process the columns by vectors, or parts of columns, to increase CPU efficiency and performance.

ClickHouse supports SQL syntax that is mostly identical to the ANSI SQL standard. There are however some differences in behavior, which are listed in the `ClickHouse documentation <https://clickhouse.com/docs/en/sql-reference/ansi/>`_.

The service is currently available as a beta release and is intended for **non-production use**.


Get started with Aiven for ClickHouse
-------------------------------------

Take your first steps with Aiven for ClickHouse by following our :doc:`getting-started` article, or browse through our full list of articles:


.. panels::


    📚 :doc:`Concepts <concepts>`

    ---

    💻 :doc:`howto`



ClickHouse resources
--------------------

If you are new to ClickHouse, try these resources to get you started with the platform:

* See the `main ClickHouse documentation <https://clickhouse.com/docs/en/>`_ for an introduction and a full list of features.

* Our :doc:`getting-started` guide is a good way to get hands on with your first project..
