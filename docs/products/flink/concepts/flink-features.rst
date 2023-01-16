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
Applications in the Aiven for Apache Flink service are containers that hold everything related to a Flink job, including the source and sink connectors and the data processing logic. They serve as the entry point for executing a Flink job within the Aiven for Apache Flink service. The Aiven console provides an intuitive interface and workflow to build applications. You can select the source and sink connectors and create statements for processing the data within your application. Additionally, you can create multiple versions of an application. Applications in Aiven for Apache Flink significantly improve the developer experience and make it easier to build and deploy Flink applications.

Interactive queries
-------------------
The interactive query feature in Aiven for Apache Flink allows you to preview the data of a Flink table or job without outputting the rows to a sink table such as Apache Kafka®. This can be useful for testing and debugging purposes, as it allows you to quickly and easily see the data that is being processed by your Flink application.

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



