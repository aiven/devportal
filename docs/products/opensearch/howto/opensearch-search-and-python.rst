Write search queries with OpenSearch® and Python
================================================

Learn how to write and run search queries on your OpenSearch cluster by using a Python OpenSearch client. We need data to interact with your cluster and make queries.

Pre-requisites
''''''''''''''

Dataset
-------
You can download the dataset `from the Kaggle recipe dataset <https://www.kaggle.com/hugodarwood/epirecipes?select=full_format_recipes.json>`_, and save the ``full_format_recipes.json`` in the current folder of the `demo <https://github.com/aiven/demo-opensearch-python>`_.


OpenSearch cluster
-------------------
For this tutorial, you'll need an OpenSearch cluster. You can create :doc:`from the Aiven Console <../getting-started>` or through the :doc:`CLI command <../../../tools/cli/service>`.


GitHub repository
------------------
The full code used here can be found at `GitHub repository <https://github.com/aiven/demo-opensearch-python>`_. 
Follow the instructions for setting up the requirements described in the ``README``.

The files are organized according to their functions:

- `config.py <https://github.com/aiven/demo-opensearch-python/blob/main/config.py>`_, basic information to connect to the cluster
- `index.py <https://github.com/aiven/demo-opensearch-python/blob/main/index.py>`_, contains methods that manipulate the index
- `search.py <https://github.com/aiven/demo-opensearch-python/blob/main/search.py>`_, contains search queries methods
- `helpers.py <https://github.com/aiven/demo-opensearch-python/blob/main/helpers.py>`_, response handler of search requests

We use ``Typer`` `Python library <ttps://typer.tiangolo.com/>`_ to create CLI commands to run from the terminal.

Connect to the OpenSearch cluster in Python
-------------------------------------------

Follow instructions on how to :doc:`connect to the cluster with a Python client <connect-with-python>`. Make sure to update the ``SERVICE_URI`` to your cluster ``SERVICE_URI`` on the ``env.`` `file <https://github.com/aiven/demo-opensearch-python/blob/main/.env>`_ as explained in the `README <https://github.com/aiven/demo-opensearch-python>`_.

.. tip::

    The ``SERVICE_URI`` value can be found in the Aiven Console dashboard.

In `config.py <https://github.com/aiven/demo-opensearch-python/blob/main/config.py>`_ you can see how the cluster configuration is created.

.. code-block:: python

    import os

    from dotenv import load_dotenv
    from opensearchpy import OpenSearch


    load_dotenv()
    INDEX_NAME = "epicurious-recipes"
    SERVICE_URI = os.getenv("SERVICE_URI")
    client = OpenSearch(SERVICE_URI, use_ssl=True)

After this, you're set to interact with our cluster.

Upload data to OpenSearch using Python
--------------------------------------

Once you're connected, the next step should be to inject data into our cluster. Follow the instructions on how to :ref:`load the sample data <load-data-with-python>` into your OpenSearch cluster. 

You can run from the demo following::

  python index.py load-data

Once the data is loaded, we can :ref:`retrieve the data mapping <get-mapping-with-python>` to explore the structure of the data, with their respective fields and types. 

From the `demo <https://github.com/aiven/demo-opensearch-python/blob/main/index.py#L50>`_, you can check the data mapping by running::

  python index.py get-mapping


All set to start writing your own search queries.

Query the data
''''''''''''''

``search()`` method
-------------------

We have an OpenSearch client and data in your cluster, so we can start writing search queries. Python OpenSearch client has a handy method called ``search()``, which we'll use to run our queries.

Checking the method's signature is a helpful way to understand the function and which parameters we'll use. Find below the method signature::

  client.search: (body=None, index=None, doc_type=None, params=None, headers=None)

All the parameters are optional in the ``search()`` method. To run the search queries, we'll use two of these parameters - ``index`` and ``body``. 

The ``index`` parameter is the name of the index we used to load the data, and therefore, it does not change. The ``body`` parameter expects a ``dict()`` object, and we'll modify the value according to the query purpose. Here is an example:

.. code-block:: python

   query_body = {
                  "query": {
                    "match_all": {}
                  }
                }

Find out how you can write the queries and call the OpenSearch client on our demo, specifically on `search.py <https://github.com/aiven/demo-opensearch-python/blob/main/search.py>`__.

Lucene query and query DSL
--------------------------

OpenSearch supports the **Lucene query syntax** to perform searches by using the ``q`` parameter. The ``q`` parameter expects a string with your query specifications, for example:

.. code-block:: python

    client.search({
        index: 'recipes',
        q: 'ingredients:broccoli AND calories:(>=100 AND <200)'
    })

For users, who prefer to work with nested objects and familiar structures like JSON (equivalent to Python dictionaries), OpenSearch supports the `query domain-specific language (DSL) <https://opensearch.org/docs/latest/opensearch/query-dsl/index/>`_.

For the **Query DSL**, the field ``body`` expects a dictionary object which can facilitate the construction of more complex queries depending on your use case, for example:

.. code-block:: python

     query_body = {
                    "query": {
                      "multi_match": {
                        "query": "Garlic-Lemon",
                        "fields": [
                          "title",
                          "ingredients"
                        ]
                      }
                    }
                  }

In this example, we are searching for "Garlic-Lemon" across ``title`` and ``ingredients`` fields. Try out yourself using our demo::
  
  python search.py multi-match title ingredients Garlic-Lemon

Check what comes out from this interesting combination 🧄 🍋 :

.. code-block:: shell
  
    [
      'Garlic-Lemon Potatoes ',
      'Lemon Garlic Mayonnaise ',
      'Lemon Garlic Mayonnaise ',
      'Garlic-Lemon Croutons ',
      'Lemon-Garlic Vinaigrette ',
      'Garlic-Lemon Potatoes ',
      'Lemon Garlic Mayonnaise ',
      'Lemon Garlic Mayonnaise ',
      'Garlic-Lemon Croutons ',
      'Lemon-Garlic Vinaigrette '
    ]

For this tutorial, we focus on the query DSL syntax to construct queries modifying the ``body`` parameter.

.. note::
  In the method ``search()``, one of the optional fields is the ``size`` field, which is defined as the number of results returned in the search. **The default value is 10.**
  

We're not adjusting the ``size`` parameter in this tutorial. Therefore, we're using the default value which is 10 results per search.


Common queries
''''''''''''''

In the next section, we cover some of the more common queries. Time to start querying 🔎 

Match query
-----------

The ``match`` query helps you to find the best matches with multiple search words and is the default option for a full-text search. For example, if you want to find matches that in the ``title`` has "Chilled Tomato".
This returns results of titles that contain "Chilled" or "Tomato" on it due to DSL defaults to the "or" operator.

.. code-block:: python

       query_body = {
                      "query": {
                        "match": {
                          "title": "Chilled Tomato"
                        }
                      }
                    }


You can run yourself the code to explore the ``match`` function. For example, if you want to find out recipes with the name "Spring" on them:

.. code-block:: shell

  python search.py match title Spring

As a result of the Spring search recipes, you'll find:

.. code-block:: shell

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

Find out more about `match queries <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#match>`_.

Multi match query
------------------
One useful query when you want to align the ``match`` query properties but expand it to search in more fields is the ``multi_match`` query. You can add several fields in the ``fields`` property, to search for the ``query`` string across all those fields included in the list.

.. code-block:: python

     query_body = {
                    "query": {
                      "multi_match": {
                        "query": query,
                        "fields": [field1, field2 ...]
                      }
                    }
                  }

Check out more results for the multi match queries creating your own. You can use our demo with ``multi-match`` keyword followed by the ``fields`` and the ``query``.

::

  python search.py multi-match title ingredients lemon


.. seealso::

  Check out more about `multi match query <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#multi-match>`_ on the OpenSearch documentation.

Match phrase query
------------------
This query can be used to match exact phrases in a field. Where the ``query`` is the phrase that is being searched in a certain field:

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
  
If you know exactly which phrases you're looking for in a recipe, you can try out our ``match-phrase`` `demo <https://github.com/aiven/demo-opensearch-python/blob/main/search.py#L39>`__. 

For example, try searching for 🍮 🍋 ``pannacotta with lemon marmalade`` in the title:

::

  python search.py match-phrase title Pannacotta with lemon marmalade

If you just have a rough idea of the phrase you're looking for, you can make your match phrase query more flexible with the ``slop`` parameter as explained in the :ref:`match phrase with slop query <match-phrase-slop>` section.

.. _match-phrase-slop:

Match phrase with slop query
----------------------------
You can use the ``slop`` parameter to create more flexible searches. Suppose you're searching for ``pannacotta marmalade`` with the ``match_phrase`` query, then no results would be returned.
You can solve this by setting the ``slop`` parameter. The ``slop`` parameter allows to control the degree where the order can be off the order, the default value is 0. The query can be constructed as:

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

If you're looking for ``pannacotta marmalade`` phrase. To find more results rather than exact phrases, you should allow a certain degree like setting the ``slop=2``, so it can find matches skipping two words between the searched ones:

.. code-block:: shell

  python search.py slop "title" "pannacotta marmalade" 2


With this flexibility, you can find titles with the desired words even if there are other words in between all thanks to the ``slop`` parameter.

.. code-block:: python

    ['Lemon Pannacotta with Lemon Marmalade ']


Try out the ``slop`` query from our `demo <https://github.com/aiven/demo-opensearch-python>`__ to allow some flexibility in your search query:

.. seealso::

  Read more about ``slop`` parameter on the `OpenSearch project specifications <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text#options>`_.


Term query
----------
If you're looking to find in a ``field`` an exact ``value``, the `term query <https://opensearch.org/docs/latest/opensearch/query-dsl/term/#term>`_ is the right choice. This query can be constructed as:

.. code-block:: python

     query_body = {
                    "query": {
                      "term": {
                        field: value
                      }
                    }
                  }


Curious about recipes low in sodium? 

You can find out more recipes with ``term`` queries by running the `demo <https://github.com/aiven/demo-opensearch-python>`__ application:

::

  python search.py term sodium 0


Range query
-----------

This query helps to find documents that the searched field's value is within a certain range. This can be handy if you're dealing with numerical values and are interested in ranges instead of specific values. The queries can be constructed as:

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

You can construct range queries with combinations of inclusive and exclusive parameters as can be seen in the table:

.. list-table::
  :header-rows: 1
  :stub-columns: 1
  :align: left

  * - Parameter
    - Behavior
  * - ``gte``
    - Greater than or equal to
  * - ``gt``
    - Greater than
  * - ``lt``
    - Less than
  * - ``lte``
    - Less than or equal to

Check out using our `demo <https://github.com/aiven/demo-opensearch-python>`__ which recipes you can find within a certain range of sodium, for example:

::

    python search.py range sodium 0 10

Fuzzy queries
-------------
You can look for fuzzy combinations where variations of the words are allowed, also called expansions, returning the exact matches for those expansions. 

The fuzzy changes can include changing a character: ``post`` → ``lost``, or removing a character: ``eggs`` → ``ggs``, and other fuzzy combinations. The queries can be constructed as:

.. code-block:: python

    query_body = {
                    "query": {
                        "fuzzy": {
                            field: {
                                "value": value
                                "fuzziness": fuzziness,
                            }
                        }
                    }
                 } 

We can try out looking for a misspelled word and allowing some ``fuzziness``, which indicates the maximum edit distance. Try to find recipes with misspelled pineapple  on the ``title`` and ``fuzziness=2`` 🍍

::

    python search.py fuzzy "title" "pinapple" 2

Notice that "Pineapple" word appears even if you've misspelled in our search:

.. code-block:: shell

    [
      'Pineapple "Lasagna" ',
      'Pineapple Bowl ',
      'Pineapple Paletas ',
      'Pineapple "Salsa" ',
      'Pineapple Sangria ',
      'Pineapple Tart ',
      'Pineapple Split ',
      'Roasted Pineapple with Star Anise Pineapple Sorbet ',
      'Pineapple-Mint Relish ',
      'Curried Pineapple Chutney '
    ]

So even if you misspelled a word, you can still find relevant results. Try out more combinations to better understand the fuzzy query.

Pause services
''''''''''''''

After following this tutorial, if you want to give a pause in your service, for the time being, see :doc:`how you can pause the service <../../../platform/howto/pause-from-cli>`. 

What's next?
''''''''''''

Want to try out OpenSearch with other clients? You can learn how to write search queries with NodeJS client, see :doc:`our tutorial <opensearch-and-nodejs>`.

Resources
'''''''''

We created an OpenSearch cluster, connected to it, and tried out different types of search queries. Now, you can explore more resources to help you learn other features of OpenSearch and its Python client.

* `Demo repository <https://github.com/aiven/demo-opensearch-python>`_, contains all code from this tutorial
* `OpenSearch Python client  <https://opensearch.org/docs/latest/clients/python/>`_
* :doc:`How to use OpenSearch with curl <opensearch-with-curl>`
* `Official OpenSearch documentation <https://opensearch.org>`_
    * `match <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#match>`_
    * `multi-match <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#match>`_
    * `match-phrase <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#match-phrase>`_
    * `fuzzy <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#options>`_
    * `term <https://opensearch.org/docs/latest/opensearch/query-dsl/term/#term>`_
    * `slop <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#options>`_
    * `range <https://opensearch.org/docs/latest/opensearch/query-dsl/term/#range>`_
    * `query-string <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#query-string>`_