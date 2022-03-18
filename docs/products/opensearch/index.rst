Aiven for OpenSearch®
=====================

`OpenSearch® <https://opensearch.org>`_ is an open source search and analytics suite including search engine, NoSQL document database, and visualization interface. OpenSearch offers a distributed, full-text search engine based on `Apache Lucene® <https://lucene.apache.org/>`_ with a RESTful API interface and support for JSON documents. Aiven for OpenSearch and Aiven for OpenSearch Dashboards are available on a cloud of your choice.

.. note::
    OpenSearch and OpenSearch Dashboards projects were forked in 2021 from the formerly open source projects Elasticsearch and Kibana.

Aiven for OpenSearch comes with OpenSearch Dashboards included, giving a fully-featured user interface and visualization platform for your data.

Why OpenSearch?
---------------

OpenSearch is a very useful addition to almost any data platform. It is designed to be robust, scalable and to be able to handle a variety of data types and structures. It provides high-performance search functionality for data of any size or type, and with schemaless storage, can index a variety of sources with different data structures.

OpenSearch is widely used for log ingestion and analysis, particularly because it can handle the data volumes involved, and because OpenSearch Dashboards provides a powerful interface to the data, including search, aggregation and analysis functionality.

Get started with Aiven for OpenSearch
-------------------------------------

Try the :doc:`sample recipes dataset <howto/sample-dataset>` or browse the other articles available:

.. panels::

    📚 :doc:`concepts`

    ---

    💻 :doc:`howto`

    ---

    📖 :doc:`Reference <reference>`

    ---

    🧰 :doc:`Code <howto/opensearch-with-curl>`


Ways to use OpenSearch
----------------------

OpenSearch is ideal for working with various types of unstructured data, where you need to be able to find things quickly. The most common examples include:

* Send your **logs** to OpenSearch so that you can quickly identify and diagnose problems if they arise.

  .. tip::
    Check how to send logs from a service to your OpenSearch service :doc:`by enabling log integration <howto/opensearch-log-integration>` feature.

* Use OpenSearch to index documents, so that you can get meaningful **search results** from a large body of knowledge.

OpenSearch resources
--------------------

* Work with your OpenSearch service :doc:`using cURL <howto/opensearch-with-curl>`

* Check the `API documentation <https://opensearch.org/docs/opensearch/rest-api/index>`_ for detailed information about the HTTP endpoints.

* There's a :doc:`list of plugins <reference/plugins>` supported by Aiven for OpenSearch.

* Got a question about the OpenSearch project itself? They have an `FAQ <https://opensearch.org/faq/>`_ for that.

--------

*Apache Lucene is a registered trademark or trademark of the Apache Software Foundation in the United States and/or other countries*
*Elasticsearch is a trademark of Elasticsearch B.V., registered in the U.S. and in other countries.*
*Kibana is a trademark of Elasticsearch B.V., registered in the U.S. and in other countries.*
