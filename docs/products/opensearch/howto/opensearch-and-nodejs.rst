Write search queries with OpenSearch and NodeJS
================================================

Learn how the OpenSearch JavaScript client gives a clear and useful interface to communicate with an OpenSearch cluster and run search queries. To make it more delicious we’ll be using a recipe dataset from Kaggle 🍕.

Prepare the playground
**********************

You can create an OpenSearch cluster either with the visual interface or with the command line. Depending on your preference follow the instructions for :doc:`getting started with the console for Aiven for Opensearch <../getting-started>` or see :doc:`how to create a service with the help of Aiven command line interface <../../../tools/cli/service>`.

.. note::

    You can also clone the final demo project from `GitHub repository <https://github.com/aiven/demo-open-search-node-js>`_.

File structure and GitHub repository
------------------------------------

To organise our development space we'll use these files:

- ``config.js`` to keep necessary basis to connect to the cluster,
- ``index.js`` to hold methods which manipulate the index,
- ``helpers.js`` to contain utilities for logging responses,
- ``search.js`` for methods specific to search requests.

We’ll be adding code into these files and running the methods from the command line.

Connect to the cluster and load data
------------------------------------

Follow instructions on how to :doc:`connect to the cluster with a NodeJS client <connect-with-nodejs>` and add the necessary code to ``config.js``. Once you're connected :ref:`load a sample data set <load-data-with-nodejs>` and :ref:`retrieve the data mapping <get-mapping-with-nodejs>` to understand the structure of the created index.

Extra helpers
-------------

To render the response, add the following helper method to your ``helpers.js`` file.

.. code:: javascript

    /**
     * Parsing and logging list of titles from the result, used in callbacks.
     */
    const logTitles = (error, result) => {
      if (error) {
        console.error(error);
      } else {
        const hits = result.body.hits.hits;
        console.log(`Number of returned results is ${hits.length}`);
        console.log(hits.map(hit => hit._source.title));
      }
    };

.. note::
    In the code snippets we'll keep error handling somewhat simple and use ``console.log`` to print information into the terminal.

Now you're ready to start querying the data.

Query the data
**************

Now that we have data in the OpenSearch cluster, we're ready to construct and run search queries. We will use ``search`` method which is provided by the OpenSearch JavaScript client. The following code goes into ``search.js``, you'll need connection configuration and helpers methods. Therefore, include them at the top of your ``search.js`` file with

.. code-block:: javascript

    const { client, indexName } = require("./config");
    const { logTitles } = require("./helpers");


The ``search`` method expects three optional parameters: ``params``, ``options`` and ``callback``.

The query details are placed into the ``params`` object. Here we can specify a variety of parameters, such as the name of the index (``index``), the maximum number of results to be returned (``size``), if the response is paginated (``size`` and ``from``), by which fields to sort the data (``sort``) and others.


We'll pay a closer attention to two of these parameters - ``q`` - a query defined in the Lucene query string syntax and ``body`` - a query based on  Query DSL (Domain Specific Language). These are two main methods to construct a query.

The query string syntax is a powerful tool which can be used for a variety of requests. It is especially convenient for cURL requests, since it is a very compact string. However, as the complexity of a request grows, it becomes more difficult to read and maintain these types of queries.

.. code-block:: javascript

    //example of using a query syntax
    client.search({
        index: 'recipes',
        q: 'ingredients:broccoli AND calories:(>=100 AND <200)'
    })

A query with a request ``body`` might look bulky at first glance, but its structure makes it easier to read, understand and modify the content. Unlike ``q``, which expects a string, ``body`` is an object allowing a variety of granular parameters.

.. code-block:: javascript

   //example of using a request body
    client.search({
        index: indexName,
        body: {
            query: {
                match: { property: 'value' }
            }
        }
    })

In this tutorial we'll focus on Query DSL and its three main groups of requests: term-level, full-text and boolean. You will also see how to use the Lucene query string syntax inside Query DSL.

* Term-level queries are handy when we need to find **exact matches** for numbers, dates or tags and don't need to sort the results by relevance. Term-level queries use search terms as they are without additional analysis.

* Full-text queries allow a smarter search for matches in analysed text fields and return results sorted by relevance.

* Boolean queries are useful to combine multiple queries together. It supports boolean clauses such as ``must``, ``filter``, ``should`` and ``must_not``.


Find matching field values
--------------------------

One of the examples of a term-level query is searching for all entries containing a particular value in a field. To construct a body request we use ``term`` property which defines an object, where the name is a field and the value is a term we're searching in this field.

.. code-block:: javascript

    /**
     * Searching for exact matches of a value in a field.
     * run-func search term sodium 0
     */
    module.exports.term = (field, value) => {
      console.log(`Searching for values in the field ${field} equal to ${value}`);
      const body = {
        query: {
          term: {
            [field]: value,
          },
        },
      };
      client.search(
        {
          index: indexName,
          body,
        },
        logTitles
      );
    };

::

    run-func search term sodium 0

Try to replace "sodium" with other fields we have, such as "calories" or "fat".

Find fields with a value within a range
---------------------------------------

When dealing with numeric values, naturally we want to be able to search for certain ranges of values. To find all documents that contain terms  in a specific field within a given range, use ``range`` property. It expects an object, where the name is set to the field name and the body defines the upper and lower bounds: ``gt`` (greater than), ``gte`` (greater than or equal to), ``lt`` (less than) and ``lte`` (less than or equal to).

.. code-block:: javascript

    /**
     * Searching for a range of values in a field.
     * run-func search range sodium 0 10
     */
    module.exports.range = (field, gte, lte) => {
      console.log(
        `Searching for values in the ${field} ranging from ${gte} to ${lte}`
      );
      const body = {
        query: {
          range: {
            [field]: {
              gte,
              lte,
            },
          },
        },
      };
      client.search(
        {
          index: indexName,
          body,
        },
        logTitles
      );
    };

::

    run-func search range sodium 0 10

Try your own term query. How about a search for food with a particular rating value, or finding all meals with zero calories?

Find fields with fuzzy text matching
------------------------------------

When searching for terms inside text fields, we can take into account typos and misspellings. We measure such "deviations" by a minimum number of single-character edits necessary to convert one word into another. Such types of queries are called ``fuzzy`` and the property ``fuzziness`` specifies the maximum edit distance.

.. code-block:: javascript

    /**
     * Specifying fuzziness to account for typos and misspelling.
     * run-func search fuzzy title pinapple 2
     */
    module.exports.fuzzy = (field, value, fuzziness) => {
      console.log(
        `Search for ${value} in the ${field} with fuzziness set to ${fuzziness}`
      );
      const query = {
        query: {
          fuzzy: {
            [field]: {
              value,
              fuzziness,
            },
          },
        },
      };
      client.search(
        {
          index: indexName,
          body: query,
        },
        logTitles
      );
    };

See if you can find recipes with misspelled pineapple 🍍

::

    run-func search fuzzy title pinapple 2

Even though there is a typo in the word "pineapple", you still got relevant results. Try other search terms and different values for ``fuzziness`` to understand better how fuzzy queries work. What is your favourite food ingredient typo?

Find best match with multiple search words
------------------------------------------

A standard way to perform a full-text query is to use ``match`` property inside a request. ``match`` expects an object, the name of which is set to a specific field, and its body contains a search query in a form of a string.

To see ``match`` in action use the method below to search for "Tomato garlic soup with dill".

.. code-block:: javascript

    /**
     * Finding matches sorted by relevance.
     * run-func search match title 'Tomato-garlic soup with dill'
     */
    module.exports.match = (field, query) => {
      console.log(`Searching for ${query} in the field ${field}`);
      const body = {
        query: {
          match: {
            [field]: {
              query,
            },
          },
        },
      };
      client.search(
        {
          index: indexName,
          body,
        },
        logTitles
      );
    };

::

    run-func search match title 'Tomato-garlic soup with dill'

In the response you should see different recipes of soups sorted by how close they are to "Tomato-garlic soup with dill" according to OpenSearch engine.

What are your favourite recipes? Try searching for them and see if you find some new and unusual recipe combinations.

Find matching phrases
---------------------

When the order of the words is important, use ``match_phrase`` instead of ``match``. An additional power of ``match_phrase`` is that it allows to define how far search words can be from each other to still be considered a match. This parameter is called ``slop`` and its default value is ``0``. The format of ``match_phrase`` is almost identical to ``match``:

.. code-block:: javascript

    /**
     * Specifying a slop - a distance between search words.
     * run-func search slop directions "pizza pineapple" 10
     */
    module.exports.slop = (field, query, slop) => {
      console.log(
        `Searching for ${query} with slop value ${slop} in the field ${field}`
      );
      const body = {
        query: {
          match_phrase: {
            [field]: {
              query,
              slop,
            },
          },
        },
      };
      client.search(
        {
          index: indexName,
          body,
        },
        logTitles
      );
    };


We can use this method to find some recipes for pizza with pineapple. I learned from my Italian colleague that this considered a combination only for tourists, not a true pizza recipe. We'll do it by searching the ``directions`` field for words "pizza" and "pineapple" with top-most distance of 10 words in between.

::

    run-func search slop directions "pizza pineapple" 10

Oh look: "Pan-Fried Hawaiian Pizza" (don't tell my colleague).

So far all the requests we tried returned us at most 10 results. Why 10? Because it is a default ``size`` value. It can be increased by setting ``size`` property to a higher number when making the request. We'll include this in the next example.

Search with query string syntax
-------------------------------

Remember the Lucene query string syntax we talked about earlier, in relation to ``q`` parameter? We can also use it inside of Query DSL by defining ``query_string`` object. It requires its own ``query`` parameter and, optionally, we can specify ``default_field`` or ``fields`` properties to indicate the search fields.

This example also sets ``size`` to demonstrate how we can get more than 10 results.

.. code-block:: javascript

    /**
     * Using special operators within a query string and a size parameter.
     * run-func search query ingredients "(salmon|tuna) +tomato -onion" 100
     */
    module.exports.query = (field, query, size) => {
      console.log(
        `Searching for ${query} in the field ${field} and returning maximum ${size} results`
      );
      const body = {
        query: {
          query_string: {
            default_field: field,
            query,
          },
        },
      };
      client.search(
        {
          index: indexName,
          body,
          size,
        },
        logTitles
      );
    };

To find recipes with tomato, salmon or tuna and no onion run this query:

::

    run-func search query ingredients "(salmon|tuna) +tomato -onion" 100

Now, experiment with your recipe search by including and excluding different ingredients.

Combine queries to improve results
----------------------------------

The boolean clause types each affect the document relevance score differently. Both ``must`` and ``should`` positively contribute to the score, affecting the relevance of matches; ``must_not`` sets the score to 0, ensuring that the document won't appear in the results. ``filter`` clause is similar to ``must``, however it has no effect on the relevance score.

In the next method we combine what we learned so far, using both term-level and full-search queries to find recipes to make a quick and easy dish, with no garlic, low sodium and high protein.

.. code-block:: javascript

    /**
     * Combining several queries together
     * run-func search boolean
     */
    module.exports.boolean = () => {
      console.log(
        `Searching for quick and easy recipes without garlic with low sodium and high protein`
      );
      const body = {
        query: {
          bool: {
            must: { match: { categories: "Quick & Easy" } },
            must_not: { match: { ingredients: "garlic" } },
            filter: [
              { range: { sodium: { lte: 50 } } },
              { range: { protein: { gte: 5 } } },
            ],
          },
        },
      };
      client.search(
        {
          index: indexName,
          body,
        },
        logTitles
      );
    };

::

    run-func search boolean

Now it's your turn to experiment! Create your own boolean query, using what we learned to find recipes with particular nutritional values and ingredients. Experiment using different clauses to see how they affects the results.

What's next?
************

Now that you learned how to work with search queries, have a look at :doc:`our tutorial for aggregations <opensearch-aggregations-and-nodejs>`. Or, if you're done for a day, see :doc:`how you can pause the service <../../../platform/howto/pause-from-cli>`.

Resources
*********

We created an OpenSearch cluster, connected to it and tried out different types of search queries. But this is just a tip of the iceberg. Here are some resources to help you learn other features of OpenSearch and its JavaScript client

* `Demo repository <https://github.com/aiven/demo-open-search-node-js>`_ - All the examples we run in this tutorial can be found in
* `OpenSearch JavaScript client  <https://github.com/opensearch-project/opensearch-js>`_
* :doc:`How to use OpenSearch with curl <opensearch-with-curl>`
* `Official OpenSearch documentation <https://opensearch.org>`_
    *  `Term-level queries <https://opensearch.org/docs/latest/opensearch/query-dsl/term/>`_
    *  `Full-text queries <https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/>`_
    *  `Boolean queries <https://opensearch.org/docs/latest/opensearch/query-dsl/bool/>`_

