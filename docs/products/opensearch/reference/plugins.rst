Plugins available with Aiven for OpenSearch
===========================================

Aiven for OpenSearch includes by default a standard a set of plugins. We also provide
support for enabling a further set of plugins should you need them. The exact plugins are listed in the sections further down this page.

.. tip::

    If you 
    are upgrading from Aiven for Elasticsearch, all the existing `supported 
    plugins <https://help.aiven.io/en/articles/511872-elasticsearch-plugins>`__
    are included. 

Included plugins
----------------

These plugins are enabled on all Aiven for OpenSearch services by default:

* ICU Analysis
* Phonetic Analysis
* kuromoji (Japanese Analysis)
* Mapper Size
* `Open Distro for Elasticsearch SQL plugin <https://opendistro.github.io/for-elasticsearch/features/SQL%20Support.html>`_
* `Open Distro for Elasticsearch Alerting plugin <https://opendistro.github.io/for-elasticsearch/features/alerting.html>`_

Additional plugins
------------------

To enable additional plugins in an OpenSearch service:

1. Select your service in the Aiven web console.
2. On the service overview page, scroll down to **Additional plugins** and
   switch on the feature.

The additional plugins collection includes the following:

-  `Anomaly detection <https://opensearch.org/docs/monitoring-plugins/ad/index/>`__
-  `Asynchronous search <https://opensearch.org/docs/search-plugins/async/index/>`__
-  `Index Management <https://opensearch.org/docs/im-plugin/index/>`__
-  Job scheduler
-  `k-NN <https://opensearch.org/docs/search-plugins/knn/index/>`__
-  `Notebooks <https://opensearch.org/docs/dashboards/notebooks/>`__
-  `Performance Analyzer <https://opensearch.org/docs/monitoring-plugins/pa/index/>`__
-  Reports Scheduler
