Create a Flink job via REST-APIs
=================================


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

Create Kafka source or sink for Flink
'''''''''''''''''''''''''''''''''''''

The following REST-API can be called.

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