Aiven for Apache Flink® features
================================
Aiven for Apache Flink® is powered by the open-source framework Apache Flink, a distributed processing engine for stateful computations over data streams. It enables you to easily get started with real-time stream processing using SQL.

Some of the key features of Aiven for Apache Flink® include:

Flink SQL
---------
Apache Flink allows you to develop streaming applications using standard SQL. Aiven for Apache Flink is a fully managed service that provides various features for developing and running streaming applications using Flink on the Aiven platform. 
One of these features is the SQL editor, which is a built-in feature of the Aiven Console. The built-in SQL editor allows you to easily create and test Flink SQL queries, explore the table schema of your data streams and tables, and deploy queries to your streaming application. This makes it easy to develop and maintain streaming applications using Flink SQL on the Aiven platform.

Build applications to process data
----------------------------------
An :doc:`Aiven for Apache Flink® Application <../concepts/flink-applications>` is an abstraction layer on top of Apache Flink SQL that includes all the elements related to a Flink job to help build your data processing pipeline. It contains all the components related to a Flink job, including the definition of source and sink tables, data processing logic, deployment parameters, and other relevant metadata.

Applications are the starting point for running an Apache Flink job within the Aiven managed service. The `Aiven Console <https://console.aiven.io/>`_ provides a user-friendly, guided wizard to help you build and deploy applications, create source and sink tables, write transformation statements, and validate and ingest data using the interactive query feature. 


Interactive queries
-------------------
The :doc:`interactive query <../concepts/supported-syntax-sql-editor>` feature in Aiven for Apache Flink grants the ability to preview the data of a Flink table or job without outputting the rows to a sink table like Apache Kafka®. This can be useful for testing and debugging purposes, as it allows you to examine the data being processed by your :doc:`Flink application <../concepts/flink-applications>`.

Built-in data flow integration with Aiven for Apache Kafka®
-----------------------------------------------------------
Aiven for Apache Flink provides built-in data flow integration with Aiven for Apache Kafka®, allowing you to easily connect your Flink streaming applications with Apache Kafka as a source or sink for your data.

- When you create data tables in Aiven for Apache Flink, the service provides auto-completion for finding existing topics in a connected Kafka service. 
- You can also choose the table format when reading data from Kafka, including JSON, Apache Avro, Confluent Avro, and Debezium CDC.
- Aiven for Apache Flink also supports upsert Kafka connectors, which allow you to produce a changelog stream where each data record represents an update or delete an event. This can be useful for maintaining data consistency in real-time streaming applications that involve complex data transformations or updates.

Built-in data flow integration with Aiven for PostgreSQL®
----------------------------------------------------------
Aiven for Apache Flink provides built-in data flow integration with Aiven for PostgreSQL, allowing you to easily connect your Flink streaming applications with PostgreSQL as a source or sink for your data.

When you create data tables in Aiven for Apache Flink, the service provides auto-completion for finding existing databases in a connected PostgreSQL service. This makes it easy to select the appropriate database and table when configuring your Flink streaming application to read or write data from PostgreSQL.

Automate workflows
------------------
Aiven for Apache Flink provides integration with the Aiven Terraform Provider, which allows you to automate workflows for managing Flink services on the Aiven platform. 
To use the Aiven Terraform Provider to automate workflows for managing Flink services, you can reference the Flink data source in your Terraform configuration files.



