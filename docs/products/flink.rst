Apache Flink® :badge:`beta,cls=badge-secondary text-black badge-pill`
=====================================================================

What is Aiven for Apache Flink®?
--------------------------------

Aiven for Apache Flink® beta is powered by the open-source framework Apache Flink®, a **distributed processing engine for stateful computations over data streams**. It enables you to easily get started with real-time stream processing using SQL.

The service is currently available as a beta release and is intended for **non-production use**.


Why Apache Flink?
-----------------

Apache Flink is a processing engine enabling the definition of streaming data pipelines with SQL statements. It can work in batch or streaming mode, it's distributed by default, and performs computation at in-memory speed at any scale.

You can use Flink to implement **batch data processing**, but also for handling **real-time processing for data streams**. More conventional database solutions might only have automation to process the accumulated data at certain intervals. Working with data streams, on the other hand, allows you to analyze and process the data in real time. This means that you can use Apache Flink to configure solutions for real-time alerting or triggering operations instead of using less efficient solutions.

Real time filtering
'''''''''''''''''''

A key part of data stream processing is the ability to filter and transform incoming data in real time. As an example, compliance requirements might mean that you have to ensure limited visibility and access to certain data. In such cases, the capability to process incoming data directly can add significant value and efficiency. Using Apache Flink, you can configure data pipelines to handle the incoming data and store or deliver it differently according to the type of the data or content. You can also transform the data according to your needs, or combine sources to enrich the data.

Use familiar SQL
''''''''''''''''

As Apache Flink uses SQL as a key part of constructing data pipelines, it is quite an approachable option for people who are already familiar with databases and batch processing. However, there are some relevant concepts (such as :doc:`windows </docs/products/flink/concepts/windows>`, :doc:`watermarks </docs/products/flink/concepts/watermarks>`, and :doc:`checkpoints </docs/products/flink/concepts/checkpoints>`) that are worth knowing if you are new to data stream processing.


Get started with Aiven for Apache Flink
---------------------------------------

Take your first steps with Aiven for Apache Flink by following our :doc:`/docs/products/flink/getting-started` article, or browse through our full list of articles:


.. panels::


    📚 :doc:`Concepts </docs/products/flink/concepts>`

    ---

    💻 :doc:`/docs/products/flink/howto`

    ---

    📖 :doc:`/docs/products/flink/reference`


Apache Flink features
---------------------

**Flink SQL**
  Apache Flink enables you to develop streaming applications using standard SQL. The :doc:`Aiven web console provides an SQL editor </docs/products/flink/concepts/supported-syntax-sql-editor>` to explore the table schema and create SQL queries to process streaming data.

**Built-in data flow integration with Aiven for Apache Kafka®**
  Connect with Aiven for Apache Kafka® as a source or sink for your data.

  * Autocompletion for finding existing topics in a connected Kafka service when you create data tables.
  * Choose the table format when reading data from Kafka - JSON, Apache Avro, Confluent Avro, Debezium CDC.
  * Supports :doc:`upsert Kafka connectors </docs/products/flink/concepts/kafka-connectors>`, which allow you to produce a changelog stream, where each data record represents an update or delete event.

**Built-in data flow integration with Aiven for PostgreSQL®**
  Connect with Aiven for PostgreSQL® as a source or sink for your data. The Aiven web console features autocompletion for finding existing databases in a connected PostgreSQL service when you create data tables.

**Automate workflows**
  Automate workflows for managing Flink services with :doc:`Aiven Terraform Provider </docs/tools/terraform>`. See the `Flink data source <https://registry.terraform.io/providers/aiven/aiven/latest/docs/data-sources/flink>`_ for details.


Apache Flink resources
----------------------

If you are new to Flink, try these resources to get you started with the platform:

* Read about the `overview of the Flink and its architecture <https://flink.apache.org/flink-architecture.html>`_ on the main Apache Flink project documentation.

* Our :doc:`/docs/products/flink/getting-started` guide is a good way to get hands on with your first project..

* Read more about `Flink SQL capabilities <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/table/sql/overview/>`_.
