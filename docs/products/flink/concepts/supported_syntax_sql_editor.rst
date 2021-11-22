Using the Aiven SQL editor
==========================

The Aiven web console includes an SQL editor for data tables and jobs in Aiven for Apache Flink services. This editor gives you access to creating the SQL schema for data tables and the job statements directly in the console.

.. image:: /images/products/flink/flink_sql_editor.png
  :alt: Image of the SQL editor in the Aiven for Apache Flink data table view

The SQL editor in the Aiven web console uses standards-compliant SQL validation. However, this means that the editor does not recognize cases where valid SQL is not currently supported by Apache Flink. At the moment, Aiven for Apache Flink services do not support the following SQL syntax:

* SQL comments
* empty lines
* line changes
* tabs
* whitespace characters (except for single spaces in command lines)
* special characters

All other valid SQL syntax is supported.

