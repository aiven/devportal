Replacing string in marshalled dashboards for Grafana®
######################################################

This tutorial helps you to quickly replace metric expression that occurs more than once in Grafana® dashboard.

What you need
-------------
* GO envinronment installed. Please follow this `instructions <https://go.dev/dl/>`_ to install GO.
* This tool can work with your own Grafana® cluster or your Aiven for Grafana® cluster

Replacing string in marshalled dashboard
----------------------------------------
1. Run this command to `download <https://github.com/aiven/aiven-string-replacer-for-grafana>`_ and install ``aiven-string-replacer-for-grafana`` 

.. code:: bash

  go install github.com/aiven/aiven-string-replacer-for-grafana

2. Go to your Grafana® UI. Click **Configuration** icon and then click **API keys** tab

3. If you already have your API Key set up and you have saved your API Key, you can skip to step 5.

4. Click **Add API key** and fill in *Key name*, *Role* must be either *Editor* or *Admin*, *Time to live*. Click **Add**

5. Save your newly created API Key

6. Go to the your dashboard that you want to convert. Click on the **Dashboard settings** icon, then click **JSON Model**.

7. Save the *UID* of your dashboard under *JSON Model* page.

8. When you have your API Key of your Grafana® cluster, UID, and URL of your dashboard ready, you can run this command.

.. code:: bash

  aiven-string-replacer-for-grafana -apikey YOUR_API_KEY -url YOUR_DASHBOARD_URL -from OLD_STRING -to NEW_STRING -uid YOUR_DASHBOARD_UID

======================     =============================================================
Variable                   Description
======================     =============================================================
``YOUR_API_KEY``             The API key from step 4
----------------------     -------------------------------------------------------------
``YOUR_DASHBOARD_URL``       The dashboard URL
----------------------     -------------------------------------------------------------
``OLD_STRING``               The name of your service
----------------------     -------------------------------------------------------------
``NEW_STRING``               The name of your service
----------------------     -------------------------------------------------------------
``YOUR_DASHBOARD_UID``       The dashboard UID from step 7.
======================     =============================================================

Example of query that replaces ``elasticsearch_`` prefix metrics to ``opensearch_`` prefix

.. code:: bash

  aiven-string-replacer-for-grafana -apikey YOUR_API_KEY -url YOUR_DASHBOARD_URL -from elasticsearch_ -to opensearch_ -uid YOUR_DASHBOARD_UID

9. Check if your dashboard is now converted.

Example of a query using ``elasticsearch_`` prefix metrics before conversion.

.. image:: /images/products/grafana/query-with-elasticsearch-prefix.png
    :alt: A screenshot of the Grafana Dashboard query with elasticsearch_ prefix metrics

Example of that same query after conversion. It should use ``opensearch_`` prefix metrics.

.. image:: /images/products/grafana/query-with-opensearch-prefix.png
    :alt: A screenshot of the Grafana Dashboard query with opensearch_ prefix metrics
