Aiven for Apache Flink
=======================

What is Aiven for Apache Flink?
-------------------------------

Aiven for Apache Flink is a fully managed **distributed processing engine for stateful computations over data streams**, deployable in the cloud of your choice enabling the creation of streaming data pipelines on top of your datasets.


Why Flink?
-----------------

Flink is a processing engine enabling the definition of streaming data pipelines with SQL statements. It can work in batch or streaming mode, it's distributed by default and performs computation at in-memory speed at any scale.

A major benefit of Apache Flink is its versatility. You can use it to implement batch data processing, but also for handling real-time processing for data streams. More conventional database solutions might only have automation to process the accumulated data at certain intervals. Working with data streams, on the other hand, allows you to analyze and process the data in real time. This means that you can use Apache Flink to configure solutions for real-time alerting or triggering operations instead of using less efficient solutions.

A key part of data stream processing is the ability to filter and transform incoming data in real time. As an example, compliance requirements might mean that you have to ensure limited visibility and access to certain data. In such cases, the capability to process incoming data directly can add significant value and efficiency. Using Apache Flink, you can configure data pipelines to handle the incoming data and store or deliver it differently according to the type of the data or content. You can also transform the data according to your needs, or combine sources to enrich the data.

While the optimal solution depends largely on your use case and goals, the versatility of Apache Flink makes it a good option for many situations. As it uses SQL as a key part of constructing data pipelines, it is quite an approachable option for people who are already familiar with databases and batch processing. However, there are some relevant concepts (such as :doc:`windows <concepts/windows>`, :doc:`watermarks <concepts/watermarks>`, and :doc:`checkpoints <concepts/checkpoints>`) that are worth knowing if you are new to data stream processing.


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
