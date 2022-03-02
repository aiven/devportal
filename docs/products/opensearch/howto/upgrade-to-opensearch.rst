Upgrade to OpenSearch
=====================

For current Aiven for Elasticsearch customers, we recommend you upgrade as soon as possible so that we can continue to support your database requirements. Depending on your needs, the various options for testing and upgrading the service are detailed here. The upgrade does not require downtime, and any Kibana service alongside Elasticsearch will be upgraded to OpenSearch Dashboards at the same time.

.. warning::
    We strongly recommend that you avoid upgrading any library dependencies as part of this upgrade process. Keep your current dependencies at their current versions.

There are three approaches that you can use to upgrade an existing service:

* Create a :doc:`fork </docs/platform/concepts/database-forking>` of Aiven for OpenSearch from your existing Aiven for Elasticsearch service. This is a good way to get a fast preview of how Aiven for OpenSearch will work for you.
* Create a fork of Aiven for Elasticsearch from your existing Aiven for Elasticsearch service. This gives you the opportunity to test the process of upgrading an existing Elasticsearch service to OpenSearch without experimenting on your live database.
* Upgrade from Aiven for Elasticsearch to Aiven for OpenSearch to move either a test or production database to the upgraded state.

The steps for each of these options are detailed in this article.

Fork an existing Elasticsearch to OpenSearch
--------------------------------------------

1. In the service overview of the web console, choose the **New database fork** button to create a new service from a backup.
2. When forking Aiven for Elasticsearch services, there in an additional option to specify the **Service type** as either Elasticsearch or OpenSearch. Choose OpenSearch and give your new service a name.

Use the new OpenSearch service to test your application against before performing an upgrade. We recommend upgrading any dependencies at the same time.

Fork an existing Elasticsearch to Elasticsearch
-----------------------------------------------

The database fork acts as a clone of your existing Elasticsearch service, but allows you to test that an upgrade will run smoothly.

1. In the service overview of the web console, choose the **New database fork** button to create a new service from a backup.
2. Check that the **Service type** field is set to Elasticsearch and give your new service a name.

You can use this service to test the upgrade to OpenSearch (instructions in the next section).

Upgrade from Elasticsearch to OpenSearch
----------------------------------------

To perform the upgrade, visit the service overview page and choose the button labelled **Upgrade Elasticsearch**. This operation cannot be reversed.

When the operation completes, your Aiven for OpenSearch service should continue to operate much as your Elasticsearch service did.

More resources
--------------

Here are some related resources that may help you with your upgrade process

* :doc:`Understand how OpenSearch relates to Elasticsearch <../concepts/opensearch-vs-elasticsearch>`
* :doc:`Upgrade your application client libraries for OpenSearch <upgrade-clients-to-opensearch>`
* :doc:`Plugins available on for Aiven for OpenSearch <../reference/plugins>`
* :doc:`OpenSearch Dashboards <../dashboards/index>` replaces Kibana
