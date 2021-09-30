Create a Flink job
=================================

Prerequisites
'''''''''''''

To build data pipelines, Apache Flink requires source or target data structures to :doc:`be mapped as Flink tables <connect>`.

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

===========================      ===============================================================================================================================
Variable                         Description
===========================      ===============================================================================================================================
``{{aiven_rest_api}}``           Aiven REST API endpoint
``{{service_name}}``             Name of the Aiven for Flink service
``{{sql_statement}}``            SQL statement defining the data transformation
``{{list_of_tables}}``           Full list of all the Flink-defined tables included in the SQL statement as source or sink
``{{job_name}}``                 Flink Job name
===========================      ===============================================================================================================================

Create a Flink job via REST APIs
'''''''''''''''''''''''''''''''''''''

To create a new data pipeline defined by a Flink job, the following REST-API can be called.

Request:: 
    
    POST https://{{aiven_rest_api}}/v1/project/{{project_id}}/test/service/{{service_name}}/flink/job

Headers: ``Authorization Bearer TOKEN``

Body::

    {
    "statement": "{{sql_statement}}",
    "tables": {{list_of_tables}},
    "job_name": "{{job_name}}"
    }

**Example**: Define a Flink job named ``JobExample`` transforming data from the ``KCpuIn`` table and inserting data in the ``KAlert`` table.

::

    {
    "statement": "INSERT INTO KAlert SELECT * FROM KCpuIn WHERE `cpu` > 70",
    "tables": ["KCpuIn", "KAlert"],
    "job_name": "JobExample"
    }


Create a Flink job via Aiven Console
'''''''''''''''''''''''''''''''''''''

To create a new data pipeline defined by a Flink job via the Aiven Console:

1. Navigate to the Aiven for Apache Flink service page, and open the **Jobs and Data** tab

2. Select the **Create SQL job** sub-tab

3. Define the Flink **Job Name**, the list of Flink source and target **tables** and data pipeline SQL **Statement** 

**Example**: Define a Flink job named ``JobExample`` transforming data from the ``KCpuIn`` table and inserting data in the ``KAlert`` table.

Settings:

* ``JobExample`` as **Job Name**
* ``KCpuIn, KAlert`` as **Tables**
* ``INSERT INTO KAlert SELECT * FROM KCpuIn WHERE `cpu` > 70`` as **Statement**

The image below shows the Aiven console page with the filled details.

.. image:: /images/products/flink/create-job.png
  :scale: 50 %
  :alt: Image of the Aiven for Apache Flink Jobs and Data tab when creating a Flink job