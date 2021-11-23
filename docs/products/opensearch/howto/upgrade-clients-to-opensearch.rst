Upgrade Elasticsearch clients to OpenSearch
===========================================

This article outlines the changes required for upgrading Elasticsearch clients to OpenSearch, migration strategy and what to do if you can't upgrade immediately.

What if you can't upgrade immediately?
--------------------------------------

OpenSearch documentation suggests version locking the client libraries
to **7.10.2** for the corresponding language or framework in order
to prevent many of the breaking changes that were introduced into
Elasticsearch client libraries as early as **7.13.\***. This is true for
application libraries as well as the supporting ecosystem of tooling
like File Beats and Logstash.

Migration strategy and upgrade order
------------------------------------

OpenSearch project was forked from the last open source version of Elasticsearch,
namely **7.10.2**, therefore locking **Elasticsearch to 7.10.2** and
**OpenSearch to 1.0.0** provides compatibility between client libraries and
deployed servers.

.. image:: /images/products/opensearch/client-and-node-compatibility-es-to-os.png

Because of this compatibility, it does not matter the order that you
migrate your cluster, or application clients. However, as always, please follow
best practices:

- thoroughly test lower environments
- test against a fork of your production database
- have a fallback plan in place should anything go wrong with your production upgrade.

Migration examples
------------------

Similarly to forking the Elasticsearch application code for deploying
nodes, the OpenSearch project forked the open source client
libraries. This means that you can simply switch the libraries without modifying your data
model, or application logic.

Please refer to `OpenSearch compatibility documentation <https://opensearch.org/docs/latest/clients/index/>`_ as
the source of truth.

To help you with migration, we provided some `code migration examples <https://github.com/aiven/opensearch-migration-examples>`_ in our repository.

Java and Spring Boot
~~~~~~~~~~~~~~~~~~~~

`Java clients <https://opensearch.org/docs/latest/clients/java-rest-high-level/>`_ are forks of the Elasticsearch libraries. To migrate change the Maven or Gradle dependencies, and update the import statements for the DOA layer. You can find an `example code change <https://github.com/aiven/opensearch-migration-examples/commit/7453d659c06b234ae7f28f801a074e459c2f31c8>`_ in our repository.

NodeJS
~~~~~~

`Node libraries <https://opensearch.org/docs/latest/clients/javascript/>`_ are forks of the Elasticsearch libraries. The only required change should be the dependency in ``package.json`` and your
``require`` or ``import`` statements. You can see an `example migration code <https://github.com/aiven/opensearch-migration-examples/tree/main/node-client-migration>`_ in our repository.
