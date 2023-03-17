Aiven for OpenSearch® overview
===============================

Aiven for OpenSearch® is a fully managed distributed search and analytics suite, deployable in the cloud of your choice. Ideal for logs management, application and website search, analytical aggregations and more. OpenSearch is an open source fork derived from Elasticsearch.


`OpenSearch® <https://opensearch.org>`_ is an open-source search and analytics suite including a search engine, NoSQL document database, and visualization interface. OpenSearch offers a distributed, full-text search engine based on `Apache Lucene® <https://lucene.apache.org/>`_ with a RESTful API interface and support for JSON documents. Aiven for OpenSearch and Aiven for OpenSearch Dashboards are available on a cloud of your choice.

.. note::
    OpenSearch and OpenSearch Dashboards projects were forked in 2021 from the formerly open source projects Elasticsearch and Kibana.

Aiven for OpenSearch includes OpenSearch Dashboards, giving a fully-featured user interface and visualization platform for your data.

Why OpenSearch?
---------------

OpenSearch is designed to be robust and scalable, capable of handling various data types and structures. It provides high-performance search functionality for data of any size or type, and with schemaless storage, it can index various sources with different data structures.

OpenSearch is widely used for log ingestion and analysis, mainly because it can handle large data volumes, and OpenSearch Dashboards provide a powerful interface to the data, including search, aggregation, and analysis functionality.


Ways to use OpenSearch
----------------------

OpenSearch is ideal for working with various types of unstructured data, where you need to be able to find things quickly. The most common examples include the following:

* **Log ingestion and analysis:** Send your **logs** to OpenSearch so that you can quickly identify and diagnose problems if they arise.

  .. tip::
    You must :doc:`enable the log integration </docs/products/opensearch/howto/opensearch-log-integration>` to send logs from a service to your OpenSearch service.

* **Document indexing:** Use OpenSearch to index documents to get meaningful **search results** from a large body of knowledge.

Benefits of using Aiven for OpenSearch®
----------------------------------------
Aiven for OpenSearch service has many benefits, such as:

* **Easy setup:** With Aiven, you can set up clusters, deploy new nodes, migrate clouds, and fork databases in a single mouse click. 
* **Open-source alternative:** Aiven for OpenSearch is an open-source alternative to Elasticsearch.
* **Search analytics:** OpenSearch has a lot of search analytics capabilities that you can use with Aiven's other services.
* **High uptime:** Aiven ensures that you get 99.99% uptime.
* **Scalability:** You can scale up or down as needed. Increase your storage, get more nodes, create new clusters, or expand to new regions.
* **Rich set of extensions:** Aiven provides a powerful set of default extensions, including SQL support, anomaly detection, and phonetic analysis.


OpenSearch resources
--------------------
Below are a few resources that can help you learn more about OpenSearch and working with your OpenSearch service:

* Work with your OpenSearch service :doc:`using cURL </docs/products/opensearch/howto/opensearch-with-curl>`

* Check the `API documentation <https://opensearch.org/docs/opensearch/rest-api/index>`_ for detailed information about the HTTP endpoints.

* There's a :doc:`list of plugins </docs/products/opensearch/reference/plugins>` supported by Aiven for OpenSearch.

* Got a question about the OpenSearch project itself? They have an `FAQ <https://opensearch.org/faq/>`_ for that.

--------

*Apache Lucene is a registered trademark or trademark of the Apache Software Foundation in the United States and/or other countries*
*Elasticsearch is a trademark of Elasticsearch B.V., registered in the U.S. and in other countries.*
*Kibana is a trademark of Elasticsearch B.V., registered in the U.S. and in other countries.*
