Flink REST API examples cheatsheet
==================================

This page contains an overview of the REST API calls examples useful to create Aiven for Apache Flink table and job definitions.

Create PostgreSQL based Flink table
-------------------------------------------------

Define a Flink table named ``node_info``

* pointing to a PostgreSQL table named ``public.node_definition`` available in the PostgreSQL database identified by the integration with the ID ``a4af7409-d167-4f31-af13-ddd4cd06564f``. 
* using the Aiven for Flink service named ``my-flink-service`` in the ``my-test-project`` project.

Endpoint::

    POST https://api.aiven.io/v1/project/my-test-project/test/service/my-flink-service/flink/table

Header: ``Authorization Bearer TOKEN``

Body::

    {
    "integration_id": "a4af7409-d167-4f31-af13-ddd4cd06564f",
    "name": "node_info",
    "jdbc_table": "public.node_definition",
    "schema_sql": "`node` INT, `node_description` VARCHAR"
    }

Create Kafka based Flink table
-------------------------------------------------

Define a Flink table named ``KAlert`` 

* pointing to a Kafka topic named ``alert`` available in the Kafka cluster identified by the integration with the ID ``a4af7409-d167-4f31-af13-ddd4cd06564f``
* using the Aiven for Flink service named ``my-flink-service`` in the ``my-test-project`` project.

Endpoint::

    POST https://api.aiven.io/v1/project/my-test-project/test/service/my-flink-service/flink/table

Header: ``Authorization Bearer TOKEN``

Body::

    {
    "integration_id": "a4af7409-d167-4f31-af13-ddd4cd06564f",
    "name": "KAlert",
    "kafka_topic": "alert",
    "schema_sql": "`node` INT, `occurred_at` TIMESTAMP_LTZ(3), `cpu_in_mb` FLOAT"
    }


Create a Flink job
--------------------------------

Define a Flink job named ``JobExample`` 

* transforming data from the ``KCpuIn`` table and inserting data in the ``KAlert`` table.
* using the Aiven for Flink service named ``my-flink-service`` in the ``my-test-project`` project.

Request:: 
    
    POST https://api.aiven.io/v1/project/my-test-project/test/service/my-flink-service/flink/job

Headers: ``Authorization Bearer TOKEN``

Body::

    {
    "statement": "INSERT INTO KAlert SELECT * FROM KCpuIn WHERE `cpu` > 70",
    "tables": ["KCpuIn", "KAlert"],
    "job_name": "JobExample"
    }