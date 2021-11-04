Aiven for Apache Flink
=======================

What is Aiven for Apache Flink?
-------------------------------

Aiven for Apache Flink is a fully managed **distributed processing engine for stateful computations over data streams**, deployable in the cloud of your choice enabling the creation of streaming data pipelines on top of your datasets.


Why Flink?
-----------------

Flink is a processing engine enabling the definition of streaming data pipelines with SQL statements. It can work in batch or streaming mode, it's distributed by default and performs computation at in-memory speed at any scale.

A major benefit of Apache Flink lies in the differences between data streams and databases. Compared to databases, where you might have automation to process the accumulated data at certain intervals, working with data streams allows you to analyze and process the data in real time. This means that you can use Apache Flink to configure solutions for real-time alerting or triggering operations instead of using less efficient solutions.

Another benefit is the ability to filter and transform incoming data in real time. For example, in cases where compliance requirements necessitate that you can ensure limited visibility and access to certain data, the capability to process incoming data directly can be a significant factor. Using Apache Flink, you can configure data pipelines to handle the incoming data and store or deliver it differently according to the type of the data or content. You can also transform the data according to your needs, or combine sources to enrich the data.

While the choice between data streams and databases depends largely on your use case and goals, SQL is a key part of constructing data pipelines in Apache Flink, making it quite an approachable data stream processing option for people who are already familiar with databases.


Get started with Aiven for Apache Flink
---------------------------------------

Take your first steps with Aiven for Apache Flink by following our :doc:`getting-started` article, or browse through our full list of articles:


.. panels::

    📙 :doc:`concepts`

    ---

    💻 :doc:`howto`


Integrates with your existing tools
------------------------------------

Flink is highly compatible with other Aiven products for the following tasks:

- Parse, transform, calculate streaming data from Aiven for Apache Kafka.

- Ingest changes on relational PostgreSQL or MySQL tables.

- Join data coming from various sources listed above to create complex data pipelines.
  
- Stream the data pipeline result back to Apache Kafka or any of the supported sinks.

Flink resources
---------------

If you are new to Flink, we recommend the following resources to get you started with the platform:

* Read about the `overview of the Flink and its architecture <https://flink.apache.org/flink-architecture.html>`_ on the main Apache Flink project documentation.

* Read more about `Flink SQL capabilities <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/table/sql/overview/>`_.
