Create an Apache Flink® job
=================================

Prerequisites
'''''''''''''

To build data pipelines, Apache Flink® requires source or target data structures to be mapped as Flink tables. 
Currently Apache Flink® tables can be defined over:

* :doc:`Aiven for Apache Kafka® topics <connect-kafka>` 
* :doc:`Aiven for PostgreSQL® tables <connect-pg>`.
* :doc:`Aiven for OpenSearch® tables <connect-pg>`.

Create a Flink job via Aiven Console
'''''''''''''''''''''''''''''''''''''

To create a new data pipeline defined by an Apache Flink® job via the Aiven Console:

1. Navigate to the Aiven for Apache Flink® service page, and open the **Jobs and Data** tab

2. Select the **Create SQL job** sub-tab

3. Define the Apache Flink® **Job Name**, the job name is the main reference to the data pipeline and can be used to manage the job and to view its details in the Apache Flink® console

4. Select the list of Apache Flink® source and target **tables**. 

.. Note::

  Even if the list of tables could be parsed from the SQL statement, it can be cumbersome and slow, especially on complex SQL statements. Defining the list of tables upfront provides a faster method to check if all the mentioned tables exists and if they have any connectivity or definition issue.

5. Define the data pipeline SQL **Statement**

.. Tip::

  Apache Flink® SQL is ANSI-SQL 2011 compliant, the following are few links with further SQL reading from the Flink documentation:

  * the available `functions and expected parameters <https://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/functions/systemfunctions/>`_
  * the `Windowing functions <https://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/window-tvf/>`_ and `windowing aggregation <https://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/window-agg/>`_
  * the `Joins <https://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/joins/>`_ and `time window joins <https://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/window-join/>`_
  * the `with clause <https://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/sql/queries/with/>`_ helpful to divide a statement in sub-statements

6. Run the job and check the results in the Aiven for Apache Kafka® topic or Aiven for PostgreSQL® table pointed by the target Apache Flink® table.

Example: Define and Apache Flink® job for basic data filtering
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

In this example we'll define an Apache Flink® streaming job, named ``JobExample``, performing a basic filtering of the data available in the Apache Flink® table named ``KCpuIn``, and insert the results into the ``KAlert`` table. 

.. Note::

  When defining Apache Flink® jobs, the input and output objects are Apache Flink® table, enabling to decouple the data pipeline definition from the source or sink technologies. If a change in the backend technology is needed, it can be handled by redefining the Apache Flink® table, without needing to change the job.

We can define the Apache Flink® job named ``JobExample`` with:

* ``JobExample`` as **Job Name**
* ``KCpuIn, KAlert`` as **Tables**
* ``INSERT INTO KAlert SELECT * FROM KCpuIn WHERE `cpu` > 70`` as **Statement**

The image below shows the Aiven console page with the filled details.

.. image:: /images/products/flink/create-job.png
  :scale: 80 %
  :alt: Image of the Aiven for Apache Flink® Jobs and Data tab when creating a Flink job

The result of the data pipeline is the target table ``KAlert`` being populated with data exceeding the ``70`` threshold. 
Depending on the Apache Flink® table definition the data could either be written to an Apache Kafka topic or a PostgreSQL table where the data pipeline results can be verified.
