Prepare a playground to experiment with OpenSearch and NodeJS
==============================================================

This tutorial will help you prepare your development environment and OpenSearch cluster to run search and aggregation queries.

Setup steps
***********

To be able to use OpenSearch and its JavaScript client we'll create an OpenSearch cluster and set up an empty NodeJS project. The final demo project can be cloned from `GitHub repository <https://github.com/aiven/demo-open-search-node-js>`_.

Step # 1: create an OpenSearch cluster
--------------------------------------

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

You should see a URL address pointing to the newly created service as a command output. Copy this value, we will need these connection details for our new cluster in a few minutes' time.

Step # 2: set up a NodeJS project
---------------------------------

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

We also need to install `OpenSearch JavaScript client  <https://github.com/opensearch-project/opensearch-js>`_. Follow its ``README`` file for instructions.

To organise our development space better we'll use several files:

- ``config.js`` to keep necessary basis to connect to the cluster,
- ``index.js`` to hold methods which manipulate the index,
- ``helpers.js`` to contain utilities for logging responses,
- ``search.js`` and ``aggregation.js`` for methods specific to search and aggregation requests.

We’ll be adding code into these files and running the methods from the command line. We'll start by adding code to ``config.js``.

Step # 3: connect to OpenSearch
-------------------------------

To connect to the cluster, use ``service_uri``, which you copied in the previous section. ``service_uri`` contains credentials, therefore should be treated with care.

We strongly recommend using environment variables for credential information. A good way to do this is to use ``dotenv``. You will find installation and usage instructions `on the library's project page <https://github.com/motdotla/dotenv>`_. In short, you need to create ``.env`` file in the project and assign ``SERVICE_URI`` to your ``service_uri`` inside of this file.

Add the require line to the top of your ``config.js`` file::

    require("dotenv").config()

Now you can refer to the value of ``service_uri`` as ``process.env.SERVICE_URI`` in the code.

Add the following lines of code to create a client and assign ``process.env.SERVICE_URI`` to the ``node`` property. This will be sufficient to connect to the cluster, because ``service_uri`` already contains credentials. Additionally, when creating a client you can also specify ``ssl configuration``, ``bearer token``, ``CA fingerprint`` and other authentication details depending on protocols you use.


.. code:: javascript

    const { Client } = require('@opensearch-project/opensearch')

    module.exports.client = new Client({
      node: process.env.SERVICE_URI,
    });

The client will perform request operations on our behalf and return the response in a consistent manner, so that we can easily parse it. To render the response, add the following helper methods to your ``helpers.js`` file.

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
        console.log(hits.map(hit => hit._source.title));
      }
    };

.. note::
    In the code snippets we'll keep error handling somewhat simple and use ``console.log`` to print information into the terminal.

Now that we have our ``config.js`` and ``helpers.js`` ready, make sure that we can indeed connect to the cluster.

We'll do this by listing the existing indices with the help of the CAT (Compact and Aligned Text) API. Open ``index.js`` and add the following code there to call ``cat.indices`` method from the client we created. Set the format to ``json`` and use the ``logBody`` as a callback to print out the response body.

.. code:: javascript

    const { client } = require("./config");
    const { logBody, logTitles } = require("./helpers");

    /**
     * Getting existing indices in the cluster.
     * run-func index getExistingIndices
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

    run-func index getExistingIndices

If you don’t want to use an additional library, you can execute the script directly with node command:

::

    node -e 'require("./index").getExistingIndices()'


``getExistingIndices`` should print out a list of indices present in our cluster. Since we just created a cluster the only index present there is ``.kibana_1`` (your name might differ), an internal index used to maintain backups when upgrading or migrating OpenSearch Dashboards.

Step # 4: ingest data into the cluster
--------------------------------------

We’ll use a dataset from `Kaggle <https://www.kaggle.com/>`_ -  Epicurious - Recipes with Rating and Nutrition. It contains over 20k recipes and is perfect for data exploration. Download `full_format_recipes.json <https://www.kaggle.com/hugodarwood/epirecipes?select=full_format_recipes.json>`_, unzip and put it into the project folder.

Add the following lines to ``config.js``

.. code-block:: javascript

    // full_format_recipes.json taken from
    // https://www.kaggle.com/hugodarwood/epirecipes?select=full_format_recipes.json
    module.exports.recipes = require("./full_format_recipes.json");

    module.exports.indexName = "recipes";


And include new dependencies into the ``index.js`` file:

.. code-block:: javascript

    const { client, indexName, recipes } = require("./config");

Before we can start searching and analyzing data, we need to index it. During indexing OpenSearch organizes documents in a compact structure which allows faster search later. It is possible to index values either one by one, or by using a bulk operation. Because we have a file containing a long list of recipes we’ll use a bulk operation.

A bulk endpoint expects a request in a format of a list where an action and an optional document are followed one after another:

* Action and metadata
* Optional document
* Action and metadata
* Optional document
* and so on...

To achieve this expected format, use a flat map to create a flat list of such pairs instructing OpenSearch to index the documents.

.. code-block:: javascript

    /**
     * Indexing data from json file with recipes.
     * run-func index indexData
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

    run-func index indexData

Let’s check that a new index was added.

::

    run-func index getExistingIndices

Now you should be able to see a newly added recipes index in the list. Depending on how soon you retrieved the list of indices, you might have seen that the newly added index has "yellow" status. This means that there is a risk of losing data if the primary shard encounters issues. Once a replica is allocated, the status will be set to green.

We didn't specify any particular structure for the recipes data when we uploaded it. Even though we could have set explicit mapping beforehand, we opted to rely on OpenSearch to derive the structure from the data and use a dynamic mapping. These obtained properties will be sufficient for our examples. To see the mapping definitions use the ``getMapping`` method and provide the index name as a parameter.

.. code-block:: javascript

    /**
     * Retrieving mapping for the index.
     * run-func index getMapping
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

    run-func index getMapping

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

These are the fields we'll be playing with. You can find information on dynamic mapping types `in the documentation <https://opensearch.org/docs/latest/opensearch/rest-api/index-apis/create-index/#dynamic-mapping-types>`_.

Resources to learn search and aggregation queries
*************************************************

Now you're ready to experiment with different types of OpenSearch queries. We prepared two tutorials for you:

- :doc:`learn how to write search queries <opensearch-and-nodejs>`
- :doc:`learn how to write aggregation queries <opensearch-aggregations-and-nodejs>`

If these are your first steps with OpenSearch, we'd recommend to start by learning how to write search queries. If you already know how to run search queries, take a look at the aggregations.

Come back to this guidance once you're done with the experiments, we'll help you to clean up the playground or temporarily pause the service.

How to pause or terminate your service
**************************************

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

We created an OpenSearch cluster, connected to it and ingested the data. Here are some resources to help you learn OpenSearch and its JavaScript client

* `Demo repository <https://github.com/aiven/demo-open-search-node-js>`_
* `OpenSearch JavaScript client  <https://github.com/opensearch-project/opensearch-js>`_
*  `Kaggle recipes dataset <https://www.kaggle.com/hugodarwood/epirecipes?select=full_format_recipes.json>`_ - great for a playground
* :doc:`How to use OpenSearch with curl <opensearch-with-curl>`
* `Official OpenSearch documentation <https://opensearch.org>`_
    *  `What clusters and nodes are in the official documentation <https://opensearch.org/docs/opensearch/index/#clusters-and-nodes>`_
    *  `How information is organised into indices and documents in the official documentation <https://opensearch.org/docs/opensearch/index/#indices-and-documents>`_
* `OpenSearch discussion forums <https://discuss.opendistrocommunity.dev/>`_ - great place to ask questions, provide feedback and get involved

