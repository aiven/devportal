Converting Elasticsearch Grafana® dashboards to OpenSearch® Grafana® dashboards
###############################################################################

After August 23 2022, all of Aiven for OpenSearch® metrics only contains ``opensearch_`` prefixes. As a refresher on the context, please refer to :doc:`this article <../../opensearch/reference/sunsetting-backward-compatible-aiven-for-opensearch.html>`. 

This tutorial helps you to quickly convert all of your non-default Aiven for Grafana® dashboard that uses ``elasticsearch_`` prefixes metrics to ``opensearch_`` prefixes metrics.

What you need
-------------
* GO envinronment installed. Please follow this `instructions <https://go.dev/dl/>`_ to install GO.
* Grafana® dashboard using ``elasticsearch_`` prefixes. This tool can work with your own Grafana® cluster or your Aiven for Grafana® cluster

Converting dashboard using ``elasticsearch_`` prefixes to ``opensearch_`` prefixes
----------------------------------------------------------------------------------
1. `Download <github.com/aiven/aiven-string-replacer-for-grafana>`_ and install ``aiven-string-replacer-for-grafana``

.. code:: json

  go install github.com/aiven/aiven-string-replacer-for-grafana

2. Go to your Grafana® UI. Click **Configuration** icon and then click **API keys** tab

3. If you already have your API Key set up and you have saved your API Key, you can skip to step 5.

4. Click **Add API key** and fill in *Key name*, *Role* must be either *Editor* or *Admin*, *Time to live*. Click **Add**

5. Save your newly created API Key

6. Go to the your dashboard that you want to convert. Click on the **Dashboard settings** icon, then click **JSON Model**.

7. Save the *UID* of your dashboard under *JSON Model* page.

8. When you have your API Key of your Grafana® cluster, UID, and URL of your dashboard ready, you can run this command.

.. code:: json

  aiven-string-replacer-for-grafana -apikey YOUR_API_KEY -url YOUR_DASHBOARD_URL -from elasticsearch_ -to opensearch_ -uid YOUR_DASHBOARD_UID

9. Check if your dashboard is now converted.

Example of a query using ``elasticsearch_`` prefix metrics before conversion.

.. image:: /images/products/grafana/query-with-elasticsearch-prefix.png
    :alt: A screenshot of the Grafana Dashboard query with elasticsearch_ prefix metrics

Example of that same query after conversion. It should use ``opensearch_`` prefix metrics.

.. image:: /images/products/grafana/query-with-opensearch-prefix.png
    :alt: A screenshot of the Grafana Dashboard query with opensearch_ prefix metrics