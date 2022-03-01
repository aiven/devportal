Getting started
===============

To start using **Aiven for OpenSearch® Dashboards**, :doc:`create Aiven for OpenSearch® service first</docs/products/opensearch/getting-started>` and OpenSearch Dashboards service will be added alongside it. Once the Aiven for OpenSearch service is running you can find connection information to your OpenSearch Dashboards in the service overview page and use your favourite browser to access OpenSearch Dashboards service.

Load sample data
*****************

OpenSearch Dashboards come with three demonstration datasets included. To add sample data follow these steps:

#. On the OpenSearch Dashboards landing page click on **Add sample data**.
#. Choose one of the available datasets and click **Add data**.
#. Click on **View data** to open the dashboard.

Tools and pages
***************

OpenSearch Dashboards have many tools and features for working with data and running queries. Here are a few ideas to get you started in each of the different sections.

Discover
---------

**Discover** page provides an interface to work with available data fields and run search queries by using either `the OpenSearch Dashboards Query Language (DQL) <https://opensearch.org/docs/latest/dashboards/dql/>`_  or `Lucene <https://lucene.apache.org/>`_.

Additionally to search queries, you can filter the data by using either a visual interface or `OpenSearch Query DSL <https://opensearch.org/docs/latest/opensearch/query-dsl/index/>`_

.. tip::
    If the index you're looking at contains a date field, pay attention to the currently selected date range when running a query.


Visualize
----------
**Visualize** page is an interface to create and manage your visualisations. In order to create a new visualization:

#. Select visualization type you want to use.
#. Choose the source of data.
#. Follow the interface to set up metrics and buckets.

Dashboard
---------

A set of visualization can be put together on a single dashboard. Search queries and filters applied to the dashboard will refine results for every included visualisation.

Dev tools console
-----------------

Read how you can use **Dev Tools** to run the queries directly from OpenSearch Dashboards :doc:`in a separate article <howto/dev-tools-usage-example>` .

Query Workbench
---------------

Query Workbench allows you to use SQL syntax instead of DSL to query the data. For example, you can retrieve the items we just added to the shopping list with:

.. code:: sql

    select * from shopping-list

Find more on how to work `with SQL Workbench <https://opensearch.org/docs/latest/search-plugins/sql/workbench/>`_ and `how to run SQL queries <https://opensearch.org/docs/latest/search-plugins/sql/index/>`_  in the official documentation.

