Getting started with Dev tools
==============================

Similarly to how you can work with the OpenSearch service :doc:`using cURL <../howto/opensearch-with-curl>` you can run the queries directly from OpenSearch Dashboards **Dev Tools**. The console contains both a request editor and a command output window.

To get you started, check out the various examples of requests that are included below. You can see that these are  same requests as in our article :doc:`on how to use cURL <../../howto/opensearch-with-curl>`, but in a pure `DSL query form <https://opensearch.org/docs/latest/opensearch/query-dsl/index/>`_. This interface is helpful when you want to quickly populate index with sample data, or run a test query.

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


You can see the command output after running the query describing created item::

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

In the output you can see the full response from OpenSearch engine::

    {
      "took" : 35,
      "timed_out" : false,
      "_shards" : {
        "total" : 9,
        "successful" : 9,
        "skipped" : 0,
        "failed" : 0
      },
      "hits" : {
        "total" : {
          "value" : 1,
          "relation" : "eq"
        },
        "max_score" : 0.6931471,
        "hits" : [
          {
            "_index" : "shopping-list",
            "_type" : "_doc",
            "_id" : "i6TdWH0BMffxqtFf7cZv",
            "_score" : 0.6931471,
            "_source" : {
              "item" : "apple",
              "quantity" : 2
            }
          }
        ]
      }
    }
Additionally, you can navigate through the history of queries and run them again.

.. note::
    **Dev Tools** supports keyboard shortcuts, to see the full list of supported commands open the help panel, which you can find as part of the menu.