Sample dataset: recipes
=======================

Databases are more fun with data, so to get you started on your OpenSearch journey we picked this open data set of recipes as a great example you can try out yourself.

Epicurious recipes
------------------

A dataset from `Kaggle <https://www.kaggle.com/hugodarwood/epirecipes>`_ with recipes, rating and nutrition information from `Epicurious <https://www.epicurious.com>`_.

Let's take a look at a sample recipe document:

.. code:: json

    {
        "title": "A very nice Vegan dish",
        "desc": "A beautiful description of the recipe",
        "date": "2015-05-01T04:00:00.000Z",
        "categories": [
            "Vegan",
            "Tree Nut Free",
            "Soy Free",
            "No Sugar Added"
        ],
        "ingredients": [
            "list",
            "of",
            "ingredients"
        ],
        "directions": [
            "list",
            "of",
            "steps",
            "to prepare the dish"
        ],
        "calories": 32.0,
        "fat": 1.0,
        "protein": 1.0,
        "rating": 5.0,
        "sodium": 959.0,
    }

Sample queries with HTTP client
-------------------------------

With the data in place, we can start trying some queries against your OpenSearch service. Since it has a simple HTTP interface, you can use your favorite HTTP client. In these examples, we will use `httpie <https://github.com/httpie/httpie>`_ because it's one of our favorites.

First, export the ``SERVICE_URI`` variable with your OpenSearch service URI address and index name from the previous script:

.. code:: bash

    export SERVICE_URI="YOUR_SERVICE_URI_HERE/epicurious-recipes"

1. Execute a basic search for the word ``vegan`` across all documents and fields:

.. code:: bash

    http "$SERVICE_URI/_search?q=vegan"

2. Search for ``vegan`` in the ``desc`` or ``title`` fields only: 

.. code:: bash

    http POST "$SERVICE_URI/_search" <<< '
    {
        "query": {
            "multi_match": {
                "query": "vegan",
                "fields": ["desc", "title"]
            }
        }
    }
    '

3. Search for recipes published only in 2013:

.. code:: bash

    http POST "$SERVICE_URI/_search" <<< '
    {
        "query": {
            "range" : {
                "date": {
                "gte": "2013-01-01",
                "lte": "2013-12-31"
                }
            }
        }
    }
    '

.. _load-data-with-python:

Load the data with Python
-------------------------

Follow the steps below to obtain the dataset and then load the sample data into your OpenSearch service using Python:

1. Download and unzip the `full_format_recipes.json <https://www.kaggle.com/hugodarwood/epirecipes?select=full_format_recipes.json>`_ file from the dataset in your current directory.

3. Install the Python dependencies:

.. code:: shell

    pip install opensearch-py==1.0.0

4. In this step you will create the script that reads the data file you downloaded and puts the records into the OpenSearch service. Create a file named ``epicurious_recipes_import.py``, and add the following code; you will need to edit it to add the connection details for your OpenSearch service.

.. Tip::
    You can find the ``SERVICE_URI`` on Aiven's dashboard.

.. code:: python

    import json
    from opensearchpy import helpers, OpenSearch


    SERVICE_URI = 'YOUR_SERVICE_URI_HERE'
    INDEX_NAME = 'epicurious-recipes'

    os_client = OpenSearch(hosts=SERVICE_URI, ssl_enable=True)


    def load_data():
        with open('full_format_recipes.json', 'r') as f:
            data = json.load(f)
            for recipe in data:
                yield {'_index': INDEX_NAME, '_source': recipe}

OpenSearch Python client offers a helper called bulk() which allows us to send multiple documents in one API call.

.. code:: python

    helpers.bulk(os_client, load_data())

5. Run the script with the following command, and wait for it to complete:

.. code:: bash

    python epicurious_recipes_import.py


.. _get-mapping-with-python:

Get data mapping with Python
----------------------------
When the data has been sent to OpenSearch cluster on :ref:`load the data with Python <load-data-with-python>`, no data structure was specified.
This is possible because OpenSearch has `dynamic mapping feature <https://opensearch.org/docs/latest/opensearch/rest-api/index-apis/create-index/#mappings>`_ that automatically add the fields to their type mapping.

To check the mapping definition, we will use ``get_mapping`` method with the index name as argument.

.. code:: python

    from pprint import pprint

    INDEX_NAME = 'epicurious-recipes'
    mapping_data = os_client.indices.get_mapping(INDEX_NAME)

    # Find index doc_type
    doc_type = list(mapping_data[INDEX_NAME]["mappings"].keys())[0]

    schema = mapping_data[INDEX_NAME]["mappings"][doc_type]
    print(f"Fields: {list(schema.keys())} \n")
    pprint(schema, width=80, indent=0)


.. seealso::

    More about `OpenSearch mapping <https://opensearch.org/docs/latest/opensearch/rest-api/index-apis/create-index/#mappings>`_ 


.. _load-data-with-nodejs:

Load the data with NodeJS
-------------------------

To load data with NodeJS we'll use `OpenSearch JavaScript client  <https://github.com/opensearch-project/opensearch-js>`_

Download `full_format_recipes.json <https://www.kaggle.com/hugodarwood/epirecipes?select=full_format_recipes.json>`_, unzip and put it into the project folder.

It is possible to index values either one by one or by using a bulk operation. Because we have a file containing a long list of recipes we’ll use a bulk operation. A bulk endpoint expects a request in a format of a list where an action and an optional document are followed one after another:

* Action and metadata
* Optional document
* Action and metadata
* Optional document
* and so on...

To achieve this expected format, use a flat map to create a flat list of such pairs instructing OpenSearch to index the documents.

.. code-block:: javascript

    module.exports.recipes = require("./full_format_recipes.json");

    /**
     * Indexing data from json file with recipes.
     */
    module.exports.indexData = () => {
      console.log(`Ingesting data: ${recipes.length} recipes`);
      const body = recipes.flatMap((doc) => [
        { index: { _index: indexName } },
        doc,
      ]);

      client.bulk({ refresh: true, body }, console.log(result.body));
    };

Run this method to load the data and wait till it's done. We’re injecting over 20k recipes, so it can take 10-15 seconds.

.. _get-mapping-with-nodejs:

Get data mapping with NodeJS
----------------------------

We didn't specify any particular structure for the recipes data when we uploaded it. Even though we could have set explicit mapping beforehand, we opted to rely on OpenSearch to derive the structure from the data and use dynamic mapping. To see the mapping definitions use the ``getMapping`` method and provide the index name as a parameter.

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

These are the fields you can play with. You can find information on dynamic mapping types `in the documentation <https://opensearch.org/docs/latest/opensearch/rest-api/index-apis/create-index/#dynamic-mapping-types>`_.

Ready for a challenge?
----------------------

After playing around with the sample queries, can you use OpenSearch queries to answer some of these questions?

1. Find all vegan recipes and order them by ``calories``.
2. Find all recipes with ``vegan`` on the title but without the words ``cheese``, ``meat`` or ``eggs`` on any other field.
3. Use one query to count how many ``vegan`` and ``vegetarian`` recipes there are.

