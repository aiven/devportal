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


Load the data
-------------

Follow the steps below to obtain the dataset and then load the sample data into your OpenSearch service using Python:

1. Download and unzip the `full_format_recipes.json <https://www.kaggle.com/hugodarwood/epirecipes?select=full_format_recipes.json>`_ file from the dataset in your current directory.

3. Install the Python dependencies:

.. code:: shell

    pip install elasticsearch==7.13.4

4. In this step you will create the script that reads the data file you downloaded and puts the records into the OpenSearch service. Create a file named ``epicurious_recipes_import.py``, and add the following code; you will need to edit it to add the connection details for your OpenSearch service.

.. Tip::
    You can find the ``SERVICE_URI`` on Aiven's dashboard.

.. code:: python

    from elasticsearch.helpers import bulk
    from elasticsearch import Elasticsearch

    import json

    SERVICE_URI = 'YOUR_SERVICE_URI_HERE'
    INDEX_NAME = 'epicurious-recipes'

    es = Elasticsearch([SERVICE_URI])


    def load_data():
        with open('full_format_recipes.json', 'r') as f:
            data = json.load(f)
            for recipe in data:
                yield {'_index': INDEX_NAME, '_source': recipe}


    bulk(es, load_data())

5. Run the script with the following command, and wait for it to complete:

.. code:: bash

    python epicurious_recipes_import.py

Sample queries
--------------

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

Ready for a challenge?
----------------------

After playing around with the sample queries, can you use OpenSearch queries to answer some these questions?

1. Find all vegan recipes and order them by ``calories``.
2. Find all recipes with ``vegan`` on the title but without the words ``cheese``, ``meat`` or ``egs`` on any other field.
3. Use one query to count how many ``vegan`` and ``vegetarian`` recipes there are.

