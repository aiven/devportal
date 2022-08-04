Replacing a string in Grafana® dashboards
#########################################

Sometimes, it is useful to replace all occurrences of a string in Grafana® metric expressions.
This page describes how to do that using the ``aiven-string-replacer-for-grafana`` tool, which is on `GitHub <https://github.com/aiven/aiven-string-replacer-for-grafana>`_.

The approach described will work with your own Grafana® cluster or with an Aiven for Grafana® cluster

Prerequisites
-------------

Building the tool requires a Go environment. Follow the `Go installation instructions <https://go.dev/dl/>`_.

To build the tool from its `source repository <https://github.com/aiven/aiven-string-replacer-for-grafana>`_,
run the following at the terminal prompt:

.. code:: bash

  go install github.com/aiven/aiven-string-replacer-for-grafana

Values you will need
--------------------

=========================    =============================================================
Variable                     Description
=========================    =============================================================
``GRAFANA_API_KEY``          The API key for accessing Grafana
-------------------------    -------------------------------------------------------------
``GRAFANA_DASHBOARD_URL``    The URL for the Grafana dashboard
-------------------------    -------------------------------------------------------------
``GRAFANA_DASHBOARD_UID``    The UID that identifies the Grafana dashboard
-------------------------    -------------------------------------------------------------
``OLD_STRING``               The old string, that you want to replace
-------------------------    -------------------------------------------------------------
``NEW_STRING``               The new string, that you want to use instead
=========================    =============================================================

Get the Grafana API key
~~~~~~~~~~~~~~~~~~~~~~~

The key needs the Grafana API key to be able to edit the Grafana dashboards.

To get your API key (``GRAFANA_API_KEY``):

* Go to your Grafana® UI. Select the **Configuration** icon and then select the **API keys** tab

* If you already have an appropriate API key available, save a copy of it.

* Otherwise, select **Add API key** and fill in the *Key name*, *Role* and *Time to live*. Click **Add** and then save the new API key.

   .. tip:: *Role* must be either *Editor* or *Admin*.

To get the Grafana dashboard URL and UID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get the dashboard URL and UID (``GRAFANA_DASHBOARD_URL`` and ``GRAFANA_DASHBOARD_UID``):

* Go to the dashboard on which you want to change metric expression strings.

* Save the dashboard URL (``GRAFANA_DASHBOARD_URL``).

* Select the **Dashboard settings** icon, then select **JSON Model**. Save the dashboard *UID* from the *JSON Model* page (``GRAFANA_DASHBOARD_UID``).

Perform the replacement
-----------------------

Use a command like the following to perform the replacement, changing the placeholder variable names to the values you collected above:

.. code:: bash

  aiven-string-replacer-for-grafana \
      -apikey GRAFANA_API_KEY \
      -url GRAFANA_DASHBOARD_URL \
      -from OLD_STRING \
      -to NEW_STRING \
      -uid GRAFANA_DASHBOARD_UID

Example: changing ``elasticsearch_`` to ``opensearch_``
-------------------------------------------------------

For instance, use the following command to change all metric expressions that start with ``elasticsearch_`` to instead start with ``opensearch_``:

.. code:: bash

  aiven-string-replacer-for-grafana \
      -apikey GRAFANA_API_KEY \
      -url YOUR_DASHBOARD_URL \
      -from elasticsearch_ \
      -to opensearch_ \
      -uid YOUR_DASHBOARD_UID

The change will be visible in the *Query* panel:

* Before running the command, metrics start with ``elasticsearch_``:

  .. image:: /images/products/grafana/query-with-elasticsearch-prefix.png
      :alt: A screenshot of the Grafana Dashboard query showing metrics prefixed with ``elasticsearch_``

* After running the command, metrics start with ``opensearch_``:

  .. image:: /images/products/grafana/query-with-opensearch-prefix.png
      :alt: A screenshot of the Grafana Dashboard query showing metrics prefixed with ``opensearch_``

Use the version history to revert
---------------------------------
If necessary, the *Dashboard changelog* page can be used to revert a change to a specific version.

* Go to the dashboard that you modified.

* Select the **Dashboard settings** icon, then select **Versions**.

* This will show your Dashboard changelog, and you can use this to revert to an earlier version of the dashboard.

.. image:: /images/products/grafana/grafana-version-changelog.png
    :alt: A screenshot of the Grafana Dashboard version changelog after conversion
