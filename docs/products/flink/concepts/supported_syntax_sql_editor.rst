Using the Aiven SQL editor
==========================

The Aiven web console includes an SQL editor for data tables and jobs in Aiven for Apache Flink services. This editor gives you access to creating the SQL schema for data tables and the job statements directly in the console.

The SQL editor in the Aiven web console highlights the content that you enter according to standard SQL syntax validation, but it does not indicate syntax that the Aiven backend systems do not currently support. This means that the operation may fail when you submit the content, even though what you see in the editor is technically valid SQL syntax.

At the moment, Aiven for Apache Flink services do not support the following SQL syntax:

* SQL comments
* empty lines
* line changes
* tabs
* whitespace characters (except for single spaces in command lines)
* special characters

All other valid SQL syntax is supported.

