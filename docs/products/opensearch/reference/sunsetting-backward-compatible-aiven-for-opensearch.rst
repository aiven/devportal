Sunsetting backward compatibility with Aiven for Elasticsearch
==============================================================

In September 2021, Aiven `introduced Aiven for OpenSearch® <https://aiven.io/blog/announcing-aiven-for-opensearch>`_ service and provided a migration path from Aiven for Elasticsearch service to Aiven for OpenSearch service that has backward capability to Aiven for Elasticsearch.

On 23 August 2022, in order to complete the migration, Aiven will sunset the backward compatible capability to all migrated Aiven for OpenSearch cluster. In this article, we will explain what are the changes after performing the update.

Aiven REST API
--------------
This section covers changes related to the REST API when the backward compatibility with Aiven for Elasticsearch is discontinued.

Aiven for OpenSearch® ACL API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After 23 August 2022, we recommend you to switch to use `Aiven for OpenSearch® API <https://api.aiven.io/doc/#tag/Service:_OpenSearch>`_ instead of Aiven for Elasticsearch API. This includes using:

* GET ``https://api.aiven.io/v1/project/{project}/service/{service_name}/opensearch/acl``
* POST ``https://api.aiven.io/v1/project/{project}/service/{service_name}/opensearch/acl``
* PUT ``https://api.aiven.io/v1/project/{project}/service/{service_name}/opensearch/acl``

Instead of:

* GET ``https://api.aiven.io/v1/project/{project}/service/{service_name}/elasticsearch/acl``
* POST ``https://api.aiven.io/v1/project/{project}/service/{service_name}/elasticsearch/acl``
* PUT ``https://api.aiven.io/v1/project/{project}/service/{service_name}/elasticsearch/acl``

  
.. seealso::

	You can check the usage of Aiven API for Aiven for OpenSearch `in the API reference <https://api.aiven.io/doc/#tag/Service:_OpenSearch>`_.

Aiven API to access service information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sunsetting the backwards compatibility with Aiven for Elasticsearch will bring changes in how to access service information using the Aiven API. You can find below the changes when you make a request to ``https://api.aiven.io/v1/project/{project}/service/{service_name}``:

================     =============================================================
Variable             Description
================     =============================================================
``project``             The name of your project on Aiven
----------------     -------------------------------------------------------------
``service_name``        The name of your service
================     =============================================================


* ``elasticsearch`` and ``kibana`` will no longer be returned under ``components`` field
* ``elasticsearch``, ``elasticsearch_username``, ``elasticsearch_password``, ``kibana_uri`` will no longer be returned under ``connection_info``
* ``elasticsearch_version`` will no longer be returned under ``user_config``
* ``service_type`` will return ``opensearch`` instead of ``elasticsearch``

Example of JSON response to your **backward compatible with Aiven for Elasticsearch** Aiven for OpenSearch® service:

.. code:: json

	{
	 "service_type": "elasticsearch",
	 "components": [
	  {
	   "component": "elasticsearch",
   	   "host": "ELASTICSEARCH_HOST",
	   "port": 12691,
   	   "privatelink_connection_id": null,
   	   "route": "dynamic",
   	   "usage": "primary"
  	  }
  	  {
   	   "component": "kibana",
   	   "host": "ELASTICSEARCH_HOST",
   	   "port": 443,
   	   "privatelink_connection_id": null,
   	   "route": "dynamic",
   	   "usage": "primary"
  	  },
	  {
	   "component": "opensearch",
   	   "host": "OPENSEARCH_HOST",
	   "port": 12691,
   	   "privatelink_connection_id": null,
   	   "route": "dynamic",
   	   "usage": "primary"
  	  }
  	  {
   	   "component": "opensearch_dashboards",
   	   "host": "OPENSEARCH_HOST",
   	   "port": 443,
   	   "privatelink_connection_id": null,
   	   "route": "dynamic",
   	   "usage": "primary"
  	  }
	 ]
	 "connection_info":{
	  "elasticsearch": [],
	  "kibana_uri": "ELASTICSEARCH_URI",
	  "elasticsearch_password":"PASSWORD",
	  "elasticsearch_username":"USERNAME",
	  "opensearch": [],
	  "opensearch_dashboards_uri": "OPENSEARCH_URI",
	  "opensearch_password":"PASSWORD",
	  "opensearch_username":"USERNAME"
	 },
	 "user_config": {
	  "elasticsearch_version": 1.3.3
	 }
	}

Example of JSON response to your Aiven for OpenSearch® service after **turning off backward compatibility with Elasticsearch**:

.. code:: json

	{
	 "service_type": "opensearch",
	 "components": [
	  {
	   "component": "opensearch",
   	   "host": "OPENSEARCH_HOST",
	   "port": 12691,
   	   "privatelink_connection_id": null,
   	   "route": "dynamic",
   	   "usage": "primary"
  	  }
  	  {
   	   "component": "opensearch_dashboards",
   	   "host": "OPENSEARCH_HOST",
   	   "port": 443,
   	   "privatelink_connection_id": null,
   	   "route": "dynamic",
   	   "usage": "primary"
  	  }
	 ]
	 "connection_info":{
	  "opensearch": [],
	  "opensearch_dashboards_uri": "OPENSEARCH_URI",
	  "opensearch_password":"PASSWORD",
	  "opensearch_username":"USERNAME"
	 },
	 "user_config": {
	  "opensearch_version": 1.3.3
	 }
	}

Aiven Console
-------------

Once we turn off the backward compatibility, you will be able to spot the differences from your OpenSearch® service page in Aiven Console. ``Elasticsearch version`` becomes ``OpenSearch version``.

Service page for Backward compatible Aiven for OpenSearch®:
  .. image:: /images/products/opensearch/console-backward-compatible-opensearch.png
    :alt: A screenshot of the OpenSearch® Service page for Backward Compatible OpenSearch®

Service page for Aiven for OpenSearch® after turning off backward compatibility:
  .. image:: /images/products/opensearch/console-pure-opensearch.png
    :alt: A screenshot of the OpenSearch® Service page for Pure OpenSearch®

Metrics integrations
--------------------

Aiven provides metrics via the Telegraf plugin so metrics that are available across Aiven for InfluxDB®, Aiven for M3 metrics integration, external Prometheus integration, and external AWS CloudWatch metrics integration are the same. You can see the full list of `detail metrics <https://help.aiven.io/en/articles/5144867-aiven-service-metrics>`_ and `additional metrics <https://help.aiven.io/en/articles/5144953-additional-service-metrics>`_.

Once we turn off the backward compatibility, Aiven for OpenSearch® will not produce any ``elasticsearch_`` prefixes metrics to **all types of metric integrations** apart from external Datadog integration. Therefore, the metrics from your Aiven for OpenSearch® cluster only contains ``opensearch_`` prefixes from the above lists.

Datadog metrics integrations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aiven does not have controls over Datadog agents, therefore, all metrics sent to external Datadog metrics integration currently still have ``elasticsearch.`` prefixes.

Grafana®
~~~~~~~~

If you have a default Aiven for Grafana® dashboard, Aiven automatically converts all queries using ``elasticsearch_`` prefixes to ``opensearch_`` prefixes.

If you have a non-default Aiven for Grafana® dashboard. Aiven provides a `tool <https://github.com/aiven/aiven-string-replacer-for-grafana>`_ and an :doc:`instruction <../../grafana/howto/aiven-string-replacer-for-grafana>` to help you converting your dashboard that uses ``elasticsearch_`` to ``opensearch_``.

