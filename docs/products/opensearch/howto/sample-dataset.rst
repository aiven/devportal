Sample dataset
--------------
Here you will find different sample datasets for OpenSearch and how to interact with them.

Before exploring the available datasets, we need an OpenSearch server to load the data on. A quick and easy way to get a server is through `Aiven for OpenSearch <https://aiven.io>`_. If don't have an Aiven account yet, `sign up <https://console.aiven.io/signup?utm_source=github&amp;utm_medium=organic&amp;utm_campaign=devportal&amp;utm_content=repo>`_ and enjoy our free trial!

After logging in the Aiven Console, chose the OpenSearch version, select the cloud and plan of your choice, give the service a name and hit the "Create Service" button. In a couple of minutes, you will have an OpenSearch server up and running.

Epicurious recipes
==================
A dataset from `Kaggle <https://www.kaggle.com/hugodarwood/epirecipes>`_ with recipes, rating and nutrition information from `Epicurious <https://www.epicurious.com>`_.

Let's take a look at the a sample document:

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
'''''''''''''
Follow the steps below to load the sample data into your OpenSearch service:

1. Download and unzip the `full_format_recipes.json <https://www.kaggle.com/hugodarwood/epirecipes?select=full_format_recipes.json>`_ file from the dataset in your current directory.

2. Create and activate a Python virtual environment:

.. Tip::
    If you don't have Python installed, follow the `official installation documentation <https://www.python.org/downloads/>`_.

.. code:: shell

    python -m venv venv
    source venv/bin/activate

3. Install the Python dependencies:

.. code:: shell

    pip install elasticsearch==7.13.4

4. Create a file named ``epicurious_recipes_import.py`` and add the following code:

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


5. Run it with the following command – it might take a few seconds:

.. code:: bash

    python epicurious_recipes_import.py

Sample queries
''''''''''''''

After loading the data, let's play with a couple of queries:

.. Tip::

    We will use `httpie <https://github.com/httpie/httpie>`_ for the HTTP requests.

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
''''''''''''''''''''''
After playing around with the sample queries, can you use OpenSearch queries to answer some these questions?

1. Find all vegan recipes and order them by ``calories``.
2. Find all recipes with ``vegan`` on the title but without the words ``cheese``, ``meat`` or ``egs`` on any other field.
3. Use one query to count how many ``vegan`` and ``vegetarian`` recipes there are.

Clean up
''''''''
To clean up the environment and, run the following commands:

.. code:: bash

    http DELETE "$SERVICE_URI"
