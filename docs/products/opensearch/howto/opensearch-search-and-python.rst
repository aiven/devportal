Write search queries with OpenSearch® and Python
================================================

Learn how to write and run search queries on your OpenSearch cluster by using your Python OpenSearch client. We need data to interact with your cluster and make queries. We will be using the recipe dataset from Kaggle. 


Pre-requisites
''''''''''''''

OpenSearch cluster
-------------------
For this tutorial, we will need an OpenSearch cluster that can be created :doc:`from the Aiven Console <../getting-started>` or through the :doc:`CLI command <../../../tools/cli/service>`.


GitHub repository
------------------
The full code used in this tutorial can be found at `GitHub repository <https://github.com/aiven/demo-opensearch-python>`_. 
Follow the instructions for setting up the requirements described in the ``README``.

The files are organized according to their functions:

- `config.py <https://github.com/aiven/demo-opensearch-python/blob/main/config.py>`_, basic information to connect to the cluster
- `index.py <https://github.com/aiven/demo-opensearch-python/blob/main/index.py>`_, contains methods that manipulate the index
- `search.py <https://github.com/aiven/demo-opensearch-python/blob/main/search.py>`_, contains search queries methods
- `helpers.js <https://github.com/aiven/demo-opensearch-python/blob/main/helpers.py>`_, response handler of search requests

We will be using ``Typer`` `Python library <ttps://typer.tiangolo.com/>`_ to create CLI commands to run from the terminal.

Connect to the OpenSearch cluster in Python
-------------------------------------------

Follow instructions on how to :doc:`connect to the cluster with a Python client <connect-with-python>` and add the necessary code to ``config.py``.
In this ``config.py``, the cluster configuration is created. After this, we're set to interact with our cluster.

.. code:: python

    import os

    from dotenv import load_dotenv
    from opensearchpy import OpenSearch


    load_dotenv()
    INDEX_NAME = "epicurious-recipes"
    SERVICE_URI = os.getenv("SERVICE_URI")
    client = OpenSearch(SERVICE_URI, use_ssl=True)


.. tip::

    The ``SERVICE_URI`` value can be found in the Aiven Console dashboard.

Upload data to OpenSearch using Python
--------------------------------------

Once you're connected, the next step should be to inject data into our cluster. Follow the instructions in how to :ref:`load the sample data <load-data-with-python>` into your OpenSearch cluster. 

You can run from the demo following::

  python index.py send-data

Once the data is sent, we can :ref:`retrieve the data mapping <get-mapping-with-python>` to explore the structure of the data, with their respective fields and types. 

From the `demo <https://github.com/aiven/demo-opensearch-python/blob/main/index.py#L50>`_, you can check the data mapping running::

  python index.py get-mapping


All set to start writing your own search queries.

Query the data
''''''''''''''

``search()`` method
-------------------

We have an OpenSearch client and data in your cluster, so we can start writing search queries. The method ``search()`` provided by the Python OpenSearch client library will be used to perform the queries. 

Find below the method signature's::

  client.search: (body=None, index=None, doc_type=None, params=None, headers=None)

All the parameters are optional in the ``search()`` method. We will define Python ``dict()`` objects for the ``body`` parameter and use. Here is an example:

.. code:: python

    query_body = {
                  "query": {
                    "match_all": {}
                  }
                }


The parameters that we will be using to configure our search queries are the ``index`` and ``body``. The ``index`` will not be changing, but we will be modifying the ``body`` parameter value according to the query purpose.

Search lite API and query DSL
-----------------------------
There are two ways of performing search queries in OpenSearch: `Search Lite API <https://opensearch.org/docs/1.2/opensearch/rest-api/search/>`_ and `OpenSearch query domain-specific language (DSL) <https://opensearch.org/docs/latest/opensearch/query-dsl/index/>`_.
In the Search Lite API, it is used the ``q`` parameter to run a query parameter search. But those kinds of queries do not support the Query DSL, and they work better for simple searches because it is expected a string as a parameter, for example:

.. code-block:: python

    client.search({
        index: 'recipes',
        q: 'ingredients:broccoli AND calories:(>=100 AND <200)'
    })


With Query DSL, the field ``body`` expects a dictionary object which makes it easier to construct more complex search queries. As an example:

.. code-block:: python

    query_body = {
                  "query": {
                      "multi_match": {
                          "query": "Garlic-Lemon",
                          "fields": ["title", "ingredients"]
                      }
                  }
              }
    resp = client.search(index=INDEX_NAME, body=query_body)
    log_titles(resp)

In this example, we are searching for "Garlic-Lemon" across ``title`` and ``ingredients`` fields.

.. note::
  In the method ``search()``. One of the optional fields is the ``size`` field, which is defined as the number of results returned in the search. The default value is 10.
  

We are not adjusting the ``size`` parameter in this tutorial. Therefore, we are using the default value which is 10 results per search.


Common queries
''''''''''''''

In the next section, we will cover some of the more common queries. Let's start querying 🔎 

Match query
-----------

The ``match`` query helps you to find the best matches with multiple search word and is the default option for full-text search. For example, if you want to find matches that in the ``title`` has "Chilled Tomato".
This will return results of titles that contain "Chilled" or "Tomato" on it due to DSL defaults to the "or" operator.

.. code-block:: python

      query_body = {
                    "query": {
                      "match": {
                        "title": "Chilled Tomato"
                      }
                    }
                  }
      resp = client.search(index=INDEX_NAME, body=query_body)
      log_titles(resp)

If you want to find exact matches for fields in the ``title`` as "Chilled Tomato", you can specify the operator "and".

.. code-block:: python

      query_body = {
                    "query": {
                      "match": {
                        "title": {"query": "Chilled Tomato", "operator": "and"}
                      }
                    }
                  }
      resp = client.search(index=INDEX_NAME, body=query_body)
      log_titles(resp)

You can run yourself the code to explore the ``match`` function. For example, if you want to find spring recipes in the title:

.. code-block:: shell

  python search.py match "title" "Spring"
  [
    'Spring Fever ',
    'Spring Rolls ',
    'Spring Feeling ',
    'Spring Fever ',
    'Spring Rolls ',
    'Spring Feeling ',
    'Spring Vegetable Sauté ',
    'Spring-Onion Cocktail ',
    'Braised Spring Legumes ',
    'Asian Spring Rolls '
  ]

Find out more about `Match query <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#match>`_.

Multi match query
------------------
One useful query when you want to align the ``match`` query properties but expand it to search in more fields is the ``multi_match`` query. You can add several fields in the ``fields`` property, so we will be searching the ``query`` string across all those fields included in the list.

.. code::python

    query_body = {
                  "query": {
                    "multi_match": {
                      "query": query,
                      "fields": [field1, field2 ...]
                    }
                  }
                }

In the next query we are looking across the ``title`` and ``ingredients`` fields for recipes with "Summer" on them. 

.. code-block:: python

    query_body = {
                  "query": {
                      "multi_match": {
                          "query": "Summer",
                          "fields": ["title", "ingredients"]
                      }
                  }
              }
    resp = client.search(index=INDEX_NAME, body=query_body)
    log_titles(resp)

Check out more results for the ``multi_match`` queries creating your own ``multi_match`` query, for example

::

  python search.py multi_match title ingredients lemon


Check out more about `multi match query <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#multi-match>`_.

Match phrase query
------------------
This query can be used to match phrases in a field. Where the ``query`` is the phrase that is being searched in a certain field:

.. code-block:: python

    query_body = {
                  "query": {
                    "match_phrase": {
                      field: {
                        "query": query
                      }
                    }
                  }
                }

If we are looking for a certain phrase, for example, ``pannacotta with lemon marmalade`` in the title, we may use a query like:

.. code-block:: python

    query_body = {
                  "query": {
                    "match_phrase": {
                      "title": {
                        "query": "pannacotta with lemon marmalade"
                      }
                    }
                  }
                }
    resp = client.search(index=INDEX_NAME, body=query_body)
    log_titles(resp)

If you know exactly which phrases you are looking for in a recipe, you can try out our ``match_phrase`` demo:

::

  python search.py match_phrase "title" "Pannacotta with lemon marmalade"

If you just have a rough idea of the phrase you are looking for, you can make your match phrase query more flexible with the ``slop`` parameter in the next section.

Match phrase with slop query
----------------------------
A useful feature we can make use of in the match_phrase query is the “slop” parameter which allows us to create more flexible searches. If we are searching for ``pannacotta marmalade`` with the ``match_phrase`` query, no results would be returned.
We can solve this by setting the ``slop`` parameter. The ``slop`` parameter allows to control the degree where the order can be off the order, the default value is 0. The query can be constructed as:

.. code-block:: python

    query_body = {
                  "query": {
                    "match_phrase": {
                      title: {
                        "query": query
                        "slop": slop
                      }
                    }
                  }
                }

Suppose we are looking for ``pannacotta marmalade`` phrase. In order to find more results rather than exact phrases, we should allow a certain degree like setting the ``slop=2``, so it can find matches skipping two words between the searched ones.

.. code-block:: python

    query_body = {
                  "query": {
                    "match_phrase": {
                      "title": {
                        "query": "pannacotta marmalade"
                        "slop": 2
                      }
                    }
                  }
                }

With this flexibility, we can find titles with the desired words even if there are other words in between all thanks to the ``slop`` parameter.

.. code-block:: python

    ['Lemon Pannacotta with Lemon Marmalade ',
    'Lemon Pannacotta with Lemon Marmalade ']


If you actually do not know exactly which phrases you are looking, you can try out using the ``slop`` query from our demo:

::

  python search.py slop "title" "pannacotta marmalade" 2

.. seealso::

  Read more about ``slop`` parameter on the `OpenSearch project specifications <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text#options>`_.


Term query
----------
If you are looking to find in a ``field`` an exact ``value``, the `term query <https://opensearch.org/docs/latest/opensearch/query-dsl/term/#term>`_ is the right choice. This query can be constructed as:

.. code-block:: python

    query_body = {
                  "query": {
                    "term": {
                      field: value
                    }
                  }
                }

Let's suppose you're looking for recipes exactly with 0 fat on them:

.. code-block:: python

    query_body = {
                  "query": {
                    "term": {
                      "fat": 0
                    }
                  }
                }
    resp = client.search(index=INDEX_NAME, body=query_body)
    log_titles(resp)

Curious about recipes low in sodium? You can use find out more recipes with ``term`` queries by running the demo application:

::

  python search.py term sodium 0


Range query
-----------

This query helps to find documents that the searched field's value is within a certain range. This can be handy if you are dealing with numerical values and are interested in ranges instead of specific values. The queries can be constructed as:

.. code-block:: python

    query_body = {
                  "query": {
                    "range": {
                      field: {
                        "gte": gte,
                        "lte": lte
                      }
                    }
                  }
                }
    resp = client.search(index=INDEX_NAME, body=query_body)
    log_titles(resp)

You can construct range queries with combinations of inclusive and exclusive parameters as can be seen in the table:

.. list-table::
  :header-rows: 1
  :stub-columns: 1
  :align: left

  * - Parameter
    - Behavior
  * - 3
    - Greater than or equal to.
  * - 4
    - Greater than.
  * - 6
    - 1001
  * - 8
    - Less than or equal to.

Check out which recipes you can find within a certain range of sodium, for example:

::

    python search.py range sodium 0 10

Fuzzy queries
-------------
You can look for fuzzy combinations where variations of the words are allowed, also called expansions, returning the exact matches for those expansions. The fuzzy changes can include changing a character: post → lost, or removing character: ``eggs`` → ``ggs``, and other fuzzy combinations. The queries can be constructed as:

.. code-block:: python

    query_body = {
          "query": {
              "fuzzy": {
                  "title": {
                      "value": 2
                      "fuzziness": 2,
                  }
              }
          }
      } 

We can try out looking for a misspelled word and allowing some ``fuzziness``, which indicates the maximum edit distance.

.. code-block:: python

    query_body = {
          "query": {
              "fuzzy": {
                  "title": {
                      "value": "pinapple",
                      "fuzziness": 2,
                  }
              }
          }
      }
    resp = client.search(index=INDEX_NAME, body=query_body)
    log_titles(resp)


Try yourself to find recipes with misspelled pineapple 🍍

::

    python search.py fuzzy "title" "pinapple" 2

So even if your misspelled a word, you can still find relevant results. Try out more combinations to better understand the fuzzy query.

Pause services
''''''''''''''

After following this tutorial, if you want to give a pause in your service for the time being, see :doc:`how you can pause the service <../../../platform/howto/pause-from-cli>`. 

What's next?
''''''''''''

Want to try out OpenSearch with other clients? You can learn how to write search queries with NodeJS client, see :doc:`our tutorial how to connect OpenSearch with NodeJS client <connect-with-nodejs>`.

Resources
'''''''''

We created an OpenSearch cluster, connected to it, and tried out different types of search queries. Now, you can and explore more resources to help you learn other features of OpenSearch and its Python client.

* `Demo repository <https://github.com/aiven/demo-opensearch-python>`_, contains all code from this tutorial
* `OpenSearch Python client  <https://opensearch.org/docs/latest/clients/python/>`_
* :doc:`How to use OpenSearch with curl <opensearch-with-curl>`
* `Official OpenSearch documentation <https://opensearch.org>`_
    *  `Term-level queries <https://opensearch.org/docs/latest/opensearch/query-dsl/term/>`_
    *  `Full-text queries <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/>`_
    *  `Boolean queries <https://opensearch.org/docs/latest/opensearch/query-dsl/bool/>`_