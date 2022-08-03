Replacing string in marshalled dashboards for Grafana®
######################################################

Sometimes, it is useful to replace all occurrences of a string in Grafana® metric expressions.
This page describes how to do that using the ``aiven-string-replaced-for-grafana`` tool

The approach described will work with your own Grafana® cluster or with an Aiven for Grafana® cluster

Install ``aiven-string-replacer-for-grafana``
---------------------------------------------

Building the tool requires a Go environment. Follow the `Go installation instructions <https://go.dev/dl/>`_.

To build the tool from its `source repository <https://github.com/aiven/aiven-string-replacer-for-grafana>`_,
run the following at the terminal prompt:

.. code:: bash

  go install github.com/aiven/aiven-string-replacer-for-grafana

Values you will need
--------------------

======================     =============================================================
Variable                   Description
======================     =============================================================
``YOUR_API_KEY``           The API key for accessing Grafana
----------------------     -------------------------------------------------------------
``YOUR_DASHBOARD_URL``     The URL for the Grafana dashboard
----------------------     -------------------------------------------------------------
``YOUR_DASHBOARD_UID``     The UID that identifies the Grafana dashboard
----------------------     -------------------------------------------------------------
``OLD_STRING``             The old string, that you want to replace
----------------------     -------------------------------------------------------------
``NEW_STRING``             The new string, that you want to use instead
======================     =============================================================

Gather authentication and authorization values
----------------------------------------------

To get your API key (``YOUR_API_KEY``):

* Go to your Grafana® UI. Select the **Configuration** icon and then select the **API keys** tab

* If you already have an appropriate API key available, save a copy of it.

* Otherwise, select **Add API key** and fill in the *Key name*, *Role* and *Time to live*. Click **Add** and then save the new API key.

   .. note:: *Role* must be either *Editor* or *Admin*. Click **Add**

To get the dashboard URL and UID (``YOUR_DASHBOARD_URL`` and ``YOUR_DASHBOARD_URI``):

* Go to the dashboard on which you want to change metric expression strings.

* Save the URL.

* Select the **Dashboard settings** icon, then select **JSON Model**. Save the dashboard *UID* from the *JSON Model* page.

Perform the replacement
-----------------------

Use a command of the following form to perform the replacement, changing the placeholder variable names to the values you collected above:

.. code:: bash

  aiven-string-replacer-for-grafana -apikey YOUR_API_KEY -url YOUR_DASHBOARD_URL \
      -from OLD_STRING -to NEW_STRING -uid YOUR_DASHBOARD_UID

Example: changing ``elasticsearch_`` to ``opensearch_``
-------------------------------------------------------

.. code:: bash

  aiven-string-replacer-for-grafana -apikey YOUR_API_KEY -url YOUR_DASHBOARD_URL \
      -from elasticsearch_ -to opensearch_ -uid YOUR_DASHBOARD_UID

Then change will be visible in the *Query* panel:

* Before running the command, a query used metrics starting with ``elasticsearch_``:

  .. image:: /images/products/grafana/query-with-elasticsearch-prefix.png
      :alt: A screenshot of the Grafana Dashboard query showing metrics prefixed with ``elasticsearch_``

* After running the command, the query uses metrics starting with ``opensearch_``:

  .. image:: /images/products/grafana/query-with-opensearch-prefix.png
      :alt: A screenshot of the Grafana Dashboard query showing metrics prefixed with ``opensearch_``

Use the version history to revert
---------------------------------
The *Dashboard changelog* can be used to revert a change, if necessary.

* Go to the your dashboard that you modified.

* Select the **Dashboard settings** icon, then select **Versions**.

* This will show *your Dashboard changelog*, and you can use this to revert to an earlier version of the dashboard.

.. image:: /images/products/grafana/grafana-version-changelog.png
    :alt: A screenshot of the Grafana Dashboard version changelog after conversion
