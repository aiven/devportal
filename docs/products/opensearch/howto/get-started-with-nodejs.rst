Use OpenSearch with NodeJS
==========================

Learn how the OpenSearch JavaScript client gives a clear and useful interface to communicate with an OpenSearch cluster. To make it more delicious we’ll be using a recipe dataset from Kaggle 🍕.

Prerequisites
*************

To be able to use OpenSearch and its JavaScript client together we'll create an OpenSearch cluster and set up an empty NodeJS project. Feel free to skip this section if you're only interested in the code samples. The final demo project can be cloned from `GitHub repository <https://github.com/aiven/demo-open-search-node-js>`_.

Create an OpenSearch cluster
----------------------------

Start by creating an OpenSearch cluster. You can either `set up OpenSearch manually <https://opensearch.org/docs/opensearch/install/index/>`_ or use a fully managed OpenSearch service from Aiven. We’ll do the latter and use Aiven for OpenSearch to quickly create a cluster. If you don’t have an Aiven account yet, `register for a free 30 day trial <https://console.aiven.io/signup>`_.

To create an OpenSearch cluster we’ll use the `Aiven command line interface <https://github.com/aiven/aiven-client>`_ . To install and set it up follow the instructions in `its GitHub page <https://github.com/aiven/aiven-client/>`_. However, if you prefer a visual interface, we also have a `web-based console <https://console.aiven.io/>`_ which you can use instead. Read the :doc:`getting started guide <../getting-started>` for more information.

Run the command below to create an OpenSearch cluster named ``demo-open-search``, hosted in **Google Europe (Warsaw) Region**. A single-node setup is sufficient for this tutorial, that's why we'll use **hobbyist** plan.

::

    avn service create demo-open-search     \
        --service-type opensearch           \
        --cloud google-europe-central2      \
        --plan hobbyist;                    \
    avn service wait demo-open-search

The command ``avn service wait`` will regularly check the status of your service until it is fully up. Once the service is running, we can start interacting with it.

While you're waiting for the service to start, obtain the connection details of your new service.

::

    avn service get demo-open-search --format {service_uri}

You should see a URL address pointing to the newly created service as a command output. Copy this value, we will need these connection details for our new clust in a few minutes' time.

Set up a NodeJS project
-----------------------

Make sure that you have both NodeJS and `npm <https://www.npmjs.com/>`_ installed by checking the installed versions.

::

    node -v
    npm -v

If you don’t have NodeJS or npm installed, follow `these instructions <https://docs.npmjs.com/downloading-and-installing-node-js-and-npm>`_.

To set up a new NodeJS project run the following command in a place where you’d like to create a project and follow the instructions (you can accept default options).

::

    mkdir demo-open-search
    cd demo-open-search
    npm init

We also need to also install `OpenSearch JavaScript client  <https://github.com/opensearch-project/opensearch-js>`_. Follow its ``README`` file for instructions.

Next add an empty ``index.js`` file into the project and open it with your favourite editor. We’ll be adding code into this file and running the methods from the command line.

Connect to OpenSearch
*********************

To connect to the cluster, you'll use ``service_uri``, which you copied in the previous section. ``service_uri`` contains credentials, therefore should be treated with care.

We strongly recommend using environment variables for credential information. A good way to do this is to use ``dotenv``. You will find installation and usage instructions `on the library's project page <https://github.com/motdotla/dotenv>`_. In short, you need to create ``.env`` file in the project and assign ``SERVICE_URI`` to your ``service_uri`` inside of this file.

Add the require line to the top of your ``index.js`` file::

    require("dotenv").config()

Now you can refer to the value of ``service_uri`` as ``process.env.SERVICE_URI`` in the code.

Add the following lines of code to create a client and assign ``process.env.SERVICE_URI`` to the ``node`` property. This will be sufficient to connect to the cluster, because ``service_uri`` already contains credentials. Additionally, when creating a client you can also specify ``ssl configuration``, ``bearer token``, ``CA fingerprint`` and other authentication details depending on protocols you use.


.. code:: javascript

    const { Client } = require('@opensearch-project/opensearch')

    const client = new Client({
      node: process.env.SERVICE_URI,
    });

The client will perform request operations on our behalf and return the response in a consistent manner, so that we can easily parse it. To render the response, add the following helper methods to your ``index.js`` file.

.. code:: javascript

    /**
     * Logging result body, used in callbacks.
     */
    const logBody = (error, result) => {
      if (error) {
        console.error(error);
      } else {
        console.log(result.body);
      }
    };

    /**
     * Parsing and logging list of titles from the result, used in callbacks.
     */
    const logTitles = (error, result) => {
      if (error) {
        console.error(error);
      } else {
        const hits = result.body.hits.hits;
        console.log(`Number of returned results is ${hits.length}`);
        console.log(hits.map((hit) => hit._source.title));
      }
    };

.. note::
    In the code snippets we'll keep error handling somewhat simple and use ``console.log`` to print information into the terminal.

To make sure that we can indeed connect to the cluster, list the existing indices with the help of the CAT (Compact and Aligned Text) API. Call the method ``indices`` and set the format to ``json`` and use the ``logBody`` as a callback to print out the response body.

.. code:: javascript

    /**
     * Getting existing indices in the cluster.
     */
    module.exports.getExistingIndices = () => {
      console.log(`Getting existing indices:`);
      client.cat.indices({ format: "json" }, logBody);
    };

We'll be calling a few functions inside our code from the terminal and the `run-func utility <https://github.com/DVLP/run-func#readme>`_ makes this much more pleasant. Install it with

::

    npm i -g run-func

To use ``run-func`` specify name of file, name of function and parameters separated with spaces.

::

    run-func index.js getExistingIndices

If you don’t want to use an additional library, you can execute the script directly with node command:

::

    node -e 'require("./index").getExistingIndices()'


``getExistingIndices`` should print out a list of indices present in our cluster. Since we've just created a cluster the only index present there is ``.kibana_1`` (your name might differ), an internal index used to maintain backups when upgrading or migrating OpenSearch Dashboards.

Load example recipe data and ingest it into the cluster
*******************************************************

We’ll use a dataset from `Kaggle <https://www.kaggle.com/>`_ -  Epicurious - Recipes with Rating and Nutrition. It contains over 20k recipes and is perfect for data exploration. Download `full_format_recipes.json <https://www.kaggle.com/hugodarwood/epirecipes?select=full_format_recipes.json>`_, unzip and put it into the project folder.

Before we can start searching and analyzing data, we need to index it. During indexing OpenSearch organizes documents in a compact structure which allows faster search later. It is possible to index values either one by one, or by using a bulk operation. Because we have a file containing a long list of recipes we’ll use a bulk operation.

A bulk endpoint expects a request in a format of a list where an action and an optional document are followed one after another:

* Action and metadata
* Optional document
* Action and metadata
* Optional document
* and so on...

To achieve this expected format, use a flat map to create a flat list of such pairs instructing OpenSearch to index the documents.

.. code-block:: javascript

    // full_format_recipes.json taken from
    // https://www.kaggle.com/hugodarwood/epirecipes?select=full_format_recipes.json
    const recipes = require('./full_format_recipes.json')

    const indexName = 'recipes';
    /**
     * Indexing data from json file with recipes.
     */
    module.exports.indexData = () => {
      console.log(`Ingesting data: ${recipes.length} recipes`);
      const body = recipes.flatMap((doc) => [
        { index: { _index: indexName } },
        doc,
      ]);

      client.bulk({ refresh: true, body }, logBody);
    };

Run a command to load the data and wait till it's done. We’re injecting over 20k recipes, so it can take 10-15 seconds.

::

    run-func index.js indexData

Let’s check that a new index was added.

::

    run-func index.js getExistingIndices

Now you should be able to see a newly added recipes index in the list. Depending on how soon you retrieved the list of indices, you might have seen that the newly added index has "yellow" status. This means that there is a risk of losing data if the primary shard encounters issues. Once a replica is allocated, the status will be set to green.

We didn't specify any particular structure for the recipes data when we uploaded it. Even though we could have set explicit mapping beforehand, we opted to rely on OpenSearch to derive the structure from the data and use a dynamic mapping. These obtained properties will be sufficient for our examples. To see the mapping definitions use the ``getMapping`` method and provide the index name as a parameter.

.. code-block:: javascript

    /**
     * Retrieving mapping for the index.
     */
    module.exports.getMapping = () => {
      console.log(`Retrieving mapping for the index with name ${indexName}`);

      client.indices.getMapping({ index: indexName }, (error, result) => {
        if (error) {
          console.error(error);
        } else {
          console.log(result.body.recipes.mappings.properties);
        }
      });
    };

Now run this new method::

    run-func index.js getMapping

You should be able to see the following structure:

.. code-block:: javascript

    {
      calories: { type: 'long' },
      categories: { type: 'text', fields: { keyword: [Object] } },
      date: { type: 'date' },
      desc: { type: 'text', fields: { keyword: [Object] } },
      directions: { type: 'text', fields: { keyword: [Object] } },
      fat: { type: 'long' },
      ingredients: { type: 'text', fields: { keyword: [Object] } },
      protein: { type: 'long' },
      rating: { type: 'float' },
      sodium: { type: 'long' },
      title: { type: 'text', fields: { keyword: [Object] } }
    }

These are the fields we'll be playing with. You can find information on dynamic mapping types `in the documentation <https://opensearch.org/docs/opensearch/rest-api/create-index/#dynamic-mapping-types>`_.

Query the data
**************

Now that we have data in the OpenSearch cluster, we're ready to construct and run search queries. We will use ``search`` method which is provided by the OpenSearch JavaScript client.

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
     */
    module.exports.termSearch = (field, value) => {
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

    run-func index.js termSearch sodium 0

Try to replace "sodium" with other fields we have, such as "calories" or "fat".

Find fields with a value within a range
---------------------------------------

When dealing with numeric values, naturally we want to be able to search for certain ranges of values. To find all documents that contain terms  in a specific field within a given range, use ``range`` property. It expects an object, where the name is set to the field name and the body defines the upper and lower bounds: ``gt`` (greater than), ``gte`` (greater than or equal to), ``lt`` (less than) and ``lte`` (less than or equal to).

.. code-block:: javascript

    /**
     * Searching for a range of values in a field.
     */
    module.exports.rangeSearch = (field, gte, lte) => {
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

    run-func index.js rangeSearch sodium 0 10

Try your own term query. How about a search for food with a particular rating value, or finding all meals with zero calories?

Find fields with fuzzy text matching
------------------------------------

When searching for terms inside text fields, we can take into account typos and misspellings. We measure such "deviations" by a minimum number of single-character edits necessary to convert one word into another. Such types of queries are called ``fuzzy`` and the property ``fuzziness`` specifies the maximum edit distance.

.. code-block:: javascript

    /**
     * Specifying fuzziness to account for typos and misspelling.
     */
    module.exports.fuzzySearch = (field, value, fuzziness) => {
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

    run-func index.js fuzzySearch title pinapple 2

Even though there is a typo in the word "pineapple", you still got relevant results. Try other search terms and different values for ``fuzziness`` to understand better how fuzzy queries work. What is your favourite food ingredient typo?

Find best match with multiple search words
------------------------------------------

A standard way to perform a full-text query is to use ``match`` property inside a request. ``match`` expects an object, the name of which is set to a specific field, and its body contains a search query in a form of a string.

To see ``match`` in action use the method below to search for "Tomato garlic soup with dill".

.. code-block:: javascript

    /**
     * Finding matches sorted by relevance.
     */
    module.exports.matchSearch = (field, query) => {
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

    run-func index.js matchSearch title 'Tomato-garlic soup with dill'

In the response you should see different recipes of soups sorted by how close they are to "Tomato-garlic soup with dill" according to OpenSearch engine.

What are your favourite recipes? Try searching for them and see if you find some new and unusual recipe combinations.

Find matching phrases
---------------------

When the order of the words is important, use ``match_phrase`` instead of ``match``. An additional power of ``match_phrase`` is that it allows to define how far search words can be from each other to still be considered a match. This parameter is called ``slop`` and its default value is ``0``. The format of ``match_phrase`` is almost identical to ``match``:

.. code-block:: javascript

    /**
     * Specifying a slop - a distance between search words.
     */
    module.exports.slopSearch = (field, query, slop) => {
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


We can use this method to find some recipes for pizza with pineapple. I've learned from my Italian colleague that this considered a combination only for tourists, not a true pizza recipe. We'll do it by searching the ``directions`` field for words "pizza" and "pineapple" with top-most distance of 10 words in between.

::

    run-func index.js slopSearch directions "pizza pineapple" 10

Oh look: "Pan-Fried Hawaiian Pizza" (don't tell my colleague).

So far all the requests we've tried returned us at most 10 results. Why 10? Because it is a default ``size`` value. It can be increased by setting ``size`` property to a higher number when making the request. We'll include this in the next example.

Search with query string syntax
-------------------------------

Remember the Lucene query string syntax we talked about earlier, in relation to ``q`` parameter? We can also use it inside of Query DSL by defining ``query_string`` object. It requires its own ``query`` parameter and, optionally, we can specify ``default_field`` or ``fields`` properties to indicate the search fields.

This example also sets ``size`` to demonstrate how we can get more than 10 results.

.. code-block:: javascript

    /**
     * Using special operators within a query string and a size parameter.
     */
    module.exports.querySearch = (field, query, size) => {
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

    run-func index.js querySearch ingredients "(salmon|tuna) +tomato -onion" 100

Now, experiment with your recipe search by including and excluding different ingredients.

Combine queries to improve results
----------------------------------

The boolean clause types each affect the document relevance score differently. Both ``must`` and ``should`` positively contribute to the score, affecting the relevance of matches; ``must_not`` sets the score to 0, ensuring that the document won't appear in the results. ``filter`` clause is similar to ``must``, however it has no effect on the relevance score.

In the next method we combine what we've learned so far, using both term-level and full-search queries to find recipes to make a quick and easy dish, with no garlic, low sodium and high protein.

.. code-block:: javascript

    /**
     * Combining several queries together
     */
    module.exports.booleanSearch = () => {
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

    run-func index.js booleanSearch

Now it's your turn to experiment! Create your own boolean query, using what we've learned to find recipes with particular nutritional values and ingredients. Experiment using different clauses to see how they affects the results.

Finish up
*********

One of the nice things about cloud services is that they can be created and destroyed easily, or just paused while you aren't using them so that you aren't being charged (or using up your trial credits).

One option is to power the service off temporarily. This way you can come back and play with the cluster later without wasting your credits while the service is idle.

::

    avn service update demo-open-search --power-off


When you're ready to continue using the service run the command to power it on. Use ``wait`` command to easily see when the service is up and running.

::

    avn service update demo-open-search --power-on
    avn service wait demo-open-search


If you have finished exploring your OpenSearch service, you can destroy or "terminate" the service. To terminate the service completely use the following command:

::

    avn service terminate demo-open-search

You will be prompted to re-enter the service name to confirm that you want to complete the termination.


Resources
*********

We've created an OpenSearch cluster, connected to it and tried out different types of search queries. But this is just a tip of the iceberg. Here are some resources to help you learn other features of OpenSearch and its JavaScript client

* `Demo repository <https://github.com/aiven/demo-open-search-node-js>`_ - All the examples we've run in this tutorial can be found in
* `OpenSearch JavaScript client  <https://github.com/opensearch-project/opensearch-js>`_
*  `Kaggle recipes dataset <https://www.kaggle.com/hugodarwood/epirecipes?select=full_format_recipes.json>`_ - great for a playground
* :doc:`How to use OpenSearch with curl <opensearch-with-curl>`
* `Official OpenSearch documentation <https://opensearch.org>`_
    *  `What clusters and nodes are in the official documentation <https://opensearch.org/docs/opensearch/index/#clusters-and-nodes>`_
    *  `How information is organised into indices and documents in the official documentation <https://opensearch.org/docs/opensearch/index/#indices-and-documents>`_
* `OpenSearch discussion forums <https://discuss.opendistrocommunity.dev/>`_ - great place to ask questions, provide feedback and get involved

