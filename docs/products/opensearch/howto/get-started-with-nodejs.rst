Get started with OpenSearch and Node.js
=======================================

Do you want to use OpenSearch with Node.js, but don’t know where to start? Then this tutorial is for you! Together we'll setup necessary building blocks from scratch and demonstrate usage of different search queries. To make it more delicious we’ll be using a recipe dataset from Kaggle 🍕.

In short, here is what we’ll do in this tutorial:

1. Create an OpenSearch cluster.
2. Set up a Node.js project.
3. Get data.
4. Index data.
5. Search data using different types of queries: term-level, full-text and boolean.
6. Clean up.
7. Share references and farther reading.

Note, we won’t dive deep into the concepts of OpenSearch, but you can check the official documentation to learn `what are clusters and nodes <https://opensearch.org/docs/opensearch/index/#clusters-and-nodes>`_ and `how information is organised into indices and documents <https://opensearch.org/docs/opensearch/index/#indices-and-documents>`_.

Creating an OpenSearch cluster
------------------------------

Let’s start by creating an OpenSearch cluster. You can either `set it up manually <https://opensearch.org/docs/opensearch/install/index/>`_  or use a fully managed OpenSearch service built for you. We’ll be doing the latter and using Aiven for OpenSearch to create a cluster in a fast and simple way. If you don’t have an Aiven account yet, register at `<https://console.aiven.io/signup>`_ for a free 30 day trial.

To create an OpenSearch cluster we’ll be using the `Aiven command line interface <https://github.com/aiven/aiven-client>`_ . However, if you prefer a visual interface, we also have a friendly `Aiven console <https://console.aiven.io/>`_ which you can use instead of the command line.

The easiest way to install `Aiven command line interface <https://github.com/aiven/aiven-client>`_ is to use Pypi:

::

    python3 -m pip install aiven-client

Once installed, check that you see usage help output by running

::

    avn

Next, authenticate to have access to your projects. The simplest way is to use the username and password you used to register for Aiven account.

::

    avn user login <your.email@example.com>

To verify that you have been authenticated run the following command

::

    avn user info

The output will display your current user information. If you can see it, you're ready to create Aiven services. For more information on how to set up and use Aiven CLI check `its github page <https://github.com/aiven/aiven-client>`_

Now let’s create an OpenSearch cluster named *demo-open-search*, hosted in *Google Europe (Warsaw) Region*. A single-node setup will be sufficient for this tutorial, that's why we'll use *hobbyist* plan.

::

    avn service create demo-open-search     \
        --service-type opensearch           \
        --cloud google-europe-central2      \
        --plan hobbyist;                    \
    avn service wait demo-open-search

Wait till the service reaches running state. At this point you’ll get a message in the terminal

::

    INFO	Service 'demo-open-search' state is now 'RUNNING'

Next, we should find where the cluster is located in order to be able to connect. The parameter with the address is ``service_uri`` and can be requested through the command line.

::

    avn service get demo-open-search --format "The service is located at {service_uri}"

You should see a URL as a command output.

Great! Now we have the cluster set up and running. We’ll be using ``service_uri`` in just a couple of minutes.

Setting up a Node.js project
----------------------------

Make sure that you have both Node.js and npm installed. You can do it by checking the installed versions.

::

    node -v;    /
    npm -v

If you you don’t have Node.js or npm installed, follow `these instructions <https://docs.npmjs.com/downloading-and-installing-node-js-and-npm>`_.

To set up a new Node.js project run the following command in a place where you’d like to create a project and follow the instructions (you can accept default options).

::

    mkdir demo-open-search; /
    cd demo-open-search;    /
    npm init

While we’re at it let’s also install `opensearch-js <https://github.com/opensearch-project/opensearch-js>`_. At the moment of writing this tutorial the opensearch-js module is still not in the npm registry and we will install it directly from github:

::

    npm install https://github.com/opensearch-project/opensearch-js

Next add an empty ``index.js`` file into the project and open it with your favourite editor. We’ll be adding code into this file and running the methods from the command line.

Start by adding the following lines of code to connect to the cluster. Use the ``service_uri`` you’ve got in the previous section.

.. code:: javascript

    const { Client } = require('@opensearch-project/opensearch')

    const client = new Client({
       node: "your-open-search-service-uri"
    })

Next let's add a couple of helper methods to parse and log response body. In the code snippets we'll keep error handling somewhat simple and will use console.logs to print information into the terminal.

.. code:: javascript

    const logBody = (error, result) => {
        if (error) {
            console.error(error);
        } else {
            console.log(result.body);
        }
    }

    const logTitles = (error, result) => {
        if (error) {
            console.error(error);
        } else {
            const hits = result.body.hits.hits;
            console.log(`Number of returned results is ${hits.length}`)
            console.log(hits.map(hit => hit._source.title));
        }
    }

Let’s verify that we can connect to the cluster by getting all indices.
Add the following method to index.js.

.. code:: javascript

    /**
     * Retrieves and logs all present indices in the cluster.
     */
    module.exports.getExistingIndices = () => {
        console.log(`Retrieving existing indices:`)
        client.cat.indices({format: 'json'}, logResultBody)
    };

Let’s call this method from the command line. To keep commands shorter I’ll be using `run-func <https://github.com/DVLP/run-func#readme>`_, which you can install with

::

    npm i -g run-func

To use run-func specify name of file, name of function and parameters separated with spaces.

::

    run-func index.js getExistingIndices

If you don’t want to use an additional library, you can execute the script directly with node command:

::

    node -e 'require("./index").getExistingIndices()'


`getExistingIndices` prints out a list of indices present in our cluster. Since we've just created a cluster the only index present there is ``.kibana_1`` (your name might differ), an internal index used to maintain backups when upgrading or migrating Dashboards.

Getting Data
------------

Now that we have our cluster running, it is time to get some data for our experiments!

We’ll use a dataset from `Kaggle <https://www.kaggle.com/>`_ -  *Epicurious - Recipes with Rating and Nutrition*. It contains over 20k recipes and is perfect for data exploration! Download `full_format_recipes.json <https://www.kaggle.com/hugodarwood/epirecipes?select=full_format_recipes.json>`_  , unzip and put it into the project folder.

Indexing data
--------------

Before we can start searching and analyzing data, we need to index it. During indexing OpenSearch organizes documents in a compact structure which allows faster search and aggregations later.

It is possible to index values either one by one, or by using a bulk operation. Because we have a file containing a long list of recipes we’ll use a bulk operation.

A bulk endpoint expects a request in a format of a list where an action and an optional document are followed one after another:

* Action and metadata
* Optional document
* Action and metadata
* Optional document
* and so on...

That’s why we use a flat map to create a flat list of such pairs instructing OpenSearch to index the documents.

.. code-block:: javascript

    // full_format_recipes.json taken from https://www.kaggle.com/hugodarwood/epirecipes?select=full_format_recipes.json
    const recipes = require('./full_format_recipes.json')

    const indexName = 'recipes';
    /**
     * Indexes data from json file with recipes.
     */
    module.exports.indexData = () => {
       console.log(`Ingesting data: ${recipes.length} recipes`);
       const body = recipes.flatMap(doc => [{ index: { _index: indexName } }, doc]);

       client.bulk({ refresh: true, body }, logBody);
    };

Run a command to load the data and wait till it's done. We’re injecting over 20k recipes, so it can take 10-15 seconds.

::

    run-func index.js indexData

Let’s check that a new index was added

::

    run-func index.js getExistingIndices

Now, you should be able to see a newly added recipes index in the list. Depending on how soon you retrieved the list of indices, you might have seen that the newly added index has yellow status. It means that there is a risk of loosing data if the primary shard encounters issues. Once a a replica is allocated the status will be set to green.

You probably noticed that we haven’t specified any structure for the documents. Even though we could have set explicit mapping beforehand, we opted to rely on OpenSearch to derive the structure from the data and use dynamic mapping. The derived properties will be sufficient for our examples. You can find `more information on mapping in the documentation <full_format_recipes.json>`_ Let’s see what properties were defined by OpenSearch when indexing the data.

.. code-block:: javascript

    /**
     * Retrieves mapping for the index.
     */
    module.exports.getMapping = () => {
        console.log(`Retrieving mapping for ${indexName}`)

        client.indices.getMapping({index: indexName}, (error, result) => {
            if (error) {
                console.error(error);
            } else {
                console.log(result.body.recipes.mappings.properties);
            }
        })
    };

::

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

Searching queries
-----------------

Now that we have data in the OpenSearch cluster, it is time to run some search queries.
We can separate possible search queries into three groups: term-level, full-text and boolean. Let's look at each one in more details.


Term-level queries
^^^^^^^^^^^^^^^^^^

Term-level queries are handy when we need to find exact matches for numbers, dates or tags and when we don't need to sort results by relevance.

One of the examples for term-level query is searching for all entries with sodium value equal to 0.

.. code-block:: javascript

    /**
     * Searches for exact matches of a value in a field.
     */
    module.exports.termSearch = (field, value) => {
        console.log(`Searching for recipes with ${field} equal to ${value}`);
        const body = {
            'query': {
                'term': {
                    [field]: value
                }
            }
        }
        client.search({
            index: indexName,
            body
        }, logTitles)
    };

::

    run-func index.js termSearch sodium 0


Full-text queries
^^^^^^^^^^^^^^^^^^

Full-text queries returns results sorted by relevance. It allows higher flexibility to find most relevant results. For example, lets search for "Tomato garlic soup with dill" and look at the list of results.

.. code-block:: javascript

    /**
     * Returns matches sorted by relevance.
     */
    module.exports.matchSearch = (field, query) => {
        const body = {
            'query': {
                'match': {
                    [field] : {
                        query
                    }
                }
            }
        }
        client.search({
            index: indexName,
            body
        }, logTitles)
    };

::

    run-func index.js matchSearch title 'Tomato-garlic soup with dill'

These are results which I got from the dataset:

.. code-block:: text

    [
      'Mussel Soup with Avocado, Tomato, and Dill ',
      'Garlic Soup ',
      'Cucumber-Dill Soup with Scallions ',
      'Cold Tomato-Thyme Soup with Grilled Garlic Croutons ',
      'Chilled Tomato, Roasted Garlic, and Basil Soup ',
      'Fast Favorite Garlic Dill Pickles ',
      'Fast Favorite Garlic Dill Pickles ',
      'Asparagus and Dill Avgolemono Soup ',
      'Garlic Tomato Sauce ',
      'Creamy Tomato Soup '
    ]

OpenSearch engine returned 10 most relevant results. Why 10? Because it is a default value. It can be increased by setting size property to a higher number.

Next, lets use some special operators in a search query with *a query string*. Let's also increase the number of returned results to 100 to demonstrate how we can get more than 10 values.

.. code-block:: javascript

    /**
     * Allows using special operators within a query string.
     */
    module.exports.querySearch = (query, size) => {
        const body = {
            'query': {
                'query_string': {
                    "fields" : ["ingredients"],
                    query
                }
            }
        }
        client.search({
            index: indexName,
            body,
            size
        }, logTitles)
    };

The full list of operators and their shortcuts can be found `in the documentation <https://opensearch.org/docs/opensearch/query-dsl/full-text/#simple-query-string>`_.

To find recipes with tomato, salmon or tuna and no onion run the next query:

::

    run-func index.js querySearch "(salmon|tuna) +tomato -onion" 100


Another useful feature of free-text query is defining how far search words can be from each other to still be considered a match. This parameter is called ``slop``.

.. code-block:: javascript

    /**
     * Allows specifying a slop - a distance between search words.
     */
    module.exports.slopSearch = (field, query, slop) => {
        console.log(`search for ${query} within distance of ${slop} in the field ${field}`);
        const body = {
            'query': {
                'match_phrase': {
                    [field]: {
                        query,
                        slop
                    }
                }
            }
        }
        client.search({
            index: indexName,
            body
        }, logTitles)
    };


Let's use this method to find recipes for pizza with pineapple. I've learned from my italian colleagues that it is an illegal combination! Let's see if we have any recipes where words pizza and pineapple are located within the distance of maximum 10 words.

::

    run-func index.js slopSearch directions "pizza pineapple" 10

And we've found "Pan-Fried Hawaiian Pizza" ;)

Another useful feature of full-text search are fuzzy queries, which are used to take into account typos and misspellings.

.. code-block:: javascript

    /**
     * Allows  specifying fuzziness - to account of typos and misspelling.
     */
    module.exports.fuzzySearch = (value, fuzziness) => {
        console.log(`search for ${value}`);
        const query = {
            'query': {
                'fuzzy': {
                    "title": {
                        value,
                        fuzziness
                    }
                }
            }
        }
        client.search({
            index: indexName,
            body: query
        }, logTitles)
    };

::

    run-func index.js fuzzySearch "pinapple" 2

And though there is a typo in the word Pineapple, we still got relevant results.

Boolean queries
^^^^^^^^^^^^^^^

The last type of queries is the boolean one, useful when we want to combine multiple queries together.
Let's find recipes to make a quick and easy dish, with no garlic, low sodium and high protein.

.. code-block:: javascript

    /**
     * Combining several queries together
     */
    module.exports.booleanSearch = () => {
        console.log(`Searching for food withing Salmon
            category without onion with low sodium and high protein`);
        const body = {
            'query': {
                'bool': {
                    "must": { "match":{"categories": "Quick & Easy"}},
                    "must_not": {"match":{"ingredients": "garlic"}},
                    "filter": [ {"range": {"sodium": {lt: 50}}},
                        {"range": {"protein": {gte: 5}}}],
                }
            }
        }
        client.search({
            index: indexName,
            body
        }, logTitles)
    };

::

    run-func index.js booleanSearch


Cleaning up
-----------

Once you're done, delete the index and the cluster

.. code-block:: javascript

    /**
     * Deleting the index
     */
    module.exports.deleteIndex = () => {
        client.indices.delete({
            index: indexName
        }, logBody)
    };

::

    run-func index.js deleteIndex

::

    avn service terminate demo-open-search

To terminate the service you will be prompted to re-enter the service name.


Resources
---------

The best source to continue learning OpenSearch is its `documentation <https://opensearch.org/>`_ and `discussion forums <https://discuss.opendistrocommunity.dev/>`_.









