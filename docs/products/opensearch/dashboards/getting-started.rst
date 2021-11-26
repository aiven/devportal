Getting started
===============

To start using Aiven for OpenSearch Dashboards, you should :doc:`create Aiven for OpenSearch service first</docs/products/opensearch/getting-started>` and OpenSearch Dashboards service will be created alongside it. Once the Aiven for OpenSearch service is running you can find connection information to your OpenSearch Dashboards in the service overview page.

.. note::
    If you are using Chrome, you need to enter **user name** and **password** manually. :doc:`Read more <howto/access-from-chrome>` for details.

Load sample data
************

OpenSearch Dashboards come with three demonstration datasets included. To add sample data follow these steps:

#. On the OpenSearch Dashboards landing page click on **Add sample data**.
#. Choose one of the available datasets and click **Add data**.
#. Click on **View data** to open the dashboard.

Tools and pages
************

OpenSearch Dashboards includes various tools to work with data and run queries in different ways. Below you can find ideas what you can do at different pages.

Discover
---------

**Discover** page provides an interface to work with available data fields and run search queries by using either `the OpenSearch Dashboards Query Language (DQL) <https://opensearch.org/docs/latest/dashboards/dql/>`_  or Lucene.

Additionally to search queries, you can filter the data by using either a visual interface or `OpenSearch Query DSL <https://opensearch.org/docs/latest/opensearch/query-dsl/index/>`_

.. note::
    If the index you're looking at contains a date field, pay attention to currently selected date range when running a query.


Visualize
----------
**Visualize** page contains tools to manage your visualisations. In order to create a new visualization:

#. Select visualization type you want to use.
#. Choose the source of data.
#. Follow the interface to set up metrics and buckets.

Dashboard
---------

A set of visualization can be put together on a single dashboard. Search queries and filters applied to the dashboard will refine results for every included visualisation.

Dev tools console
-----------------

Similarly to how you can work with the OpenSearch service :doc:`using cURL <../howto/opensearch-with-curl>` you can run the queries directly from OpenSearch Dashboards **Dev Tools**. The console contains both a request editor and a command output window.

To get you started find below examples of several requests. You can see that these are  same requests as in our article :doc:`on how to use cURL <../howto/opensearch-with-curl>`, but in a pure `DSL query form <https://opensearch.org/docs/latest/opensearch/query-dsl/index/>`_. This interface is helpful when you want to quickly populate index with sample data, or run a test query.

Use **POST** method to add a new item to an index called ``shopping-list``. If the index doesn't exist yet, it will be created::

    POST shopping-list/_doc
    {
        "item": "apple",
        "quantity": 2
    }

Follow by adding another item with a different set of fields::

    POST shopping-list/_doc
    {
        "item": "bucket",
        "color": "blue",
        "quantity": 5,
        "notes": "the one with the metal handle"
    }


You can see the command output after running each of the queries::

    {
      "_index" : "shopping-list",
      "_type" : "_doc",
      "_id" : "jKTeWH0BMffxqtFft8Zv",
      "_version" : 1,
      "result" : "created",
      "_shards" : {
        "total" : 2,
        "successful" : 1,
        "failed" : 0
      },
      "_seq_no" : 1,
      "_primary_term" : 1
    }


Use **GET** method to send a query to find items with an apple::

    GET _search
    {
        "query": {
            "multi_match" : {
                "query" : "apple",
                "fields" : ["item", "notes"]
            }
        }
    }

Additionally, you can navigate through the history of queries and run them again.

.. note::
    **Dev Tools** supports keyboard shortcuts, to see the full list of supported commands open the help panel.


Query Workbench
---------------

Query Workbench allows to use SQL syntax instead of DSL to query the data. For example, you can retrieve the items we just added to the shopping list with:

.. code:: sql

    select * from shopping-list

Find more on how to work `with SQL Workbench <https://opensearch.org/docs/latest/search-plugins/sql/workbench/>`_ and `how to run SQL queries <https://opensearch.org/docs/latest/search-plugins/sql/index/>`_  in the official documentation.

