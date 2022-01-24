ClickHouse :badge:`beta,cls=badge-secondary text-black badge-pill`
==================================================================

What is Aiven for ClickHouse?
-----------------------------

Aiven for ClickHouse beta is powered by ClickHouse, an open-source database management system that uses a column-oriented structure and is best suited for the online analytical processing of queries (OLAP).

In OLAP scenarios, a column-oriented structure provides much quicker processing of queries compared to row-oriented databases, as it reduces the input/output load by minimizing the amount of data that needs to be read and by improving data compression. To optimize data compression, ClickHouse provides both general-purpose compression codecs and codecs that are tailored for specific data types. ClickHouse also includes a vector computation engine to process the columns by vectors, or parts of columns, to increase CPU efficiency and performance.

As a truly columnar database, ClickHouse also stores the values of the same column physically next to each other. This further increases the speed of retrieving the values of a column. However, it also makes it slower to retrieve complete rows, as the values of a single row are stored across different physical locations.

ClickHouse supports SQL syntax that resembles the ANSI SQL standard. There are however some differences in behavior, which are listed in the `ClickHouse documentation <https://clickhouse.com/docs/en/sql-reference/ansi/>`_.

.. note::
   The service is currently available as a beta release and is intended for **non-production use**.


Get started with Aiven for ClickHouse
-------------------------------------

Take your first steps with Aiven for ClickHouse by following our :doc:`getting-started` article, or browse through our full list of articles:


.. panels::


    📚 :doc:`Concepts <concepts>`

    ---

    💻 :doc:`howto`

    ---

    📖 :doc:`reference`



ClickHouse resources
--------------------

If you are new to ClickHouse, try these resources to get you started with the platform:

* See the `main ClickHouse documentation <https://clickhouse.com/docs/en/>`_ for an introduction and a full list of features.

* Our :doc:`getting-started` guide is a good way to get hands on with your first project.
