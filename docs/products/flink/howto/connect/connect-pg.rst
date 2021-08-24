Create a PostgreSQL based Flink source or sink
==============================================

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

===========================      ===============================================================================================================================
Variable                         Description
===========================      ===============================================================================================================================
``{{aiven_rest_api}}``           Aiven REST API endpoint
``{{service_name}}``             Name of the Aiven for Flink service
``{{integration_id}}``           Id of the integration created between Flink and the source/destination system
``{{source_dest_name}}``         Name of the source or destination Endpoint
``{{table_name}}``               Name of the database table to use as source or sink
``{{table_schema}}``             Definition of `table schema <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/table/sql/create/#columns>`_
``{{partition_by_clause}}``      Table partition definition
===========================      ===============================================================================================================================

Create PostgreSQL source or sink for Flink
''''''''''''''''''''''''''''''''''''''''''

The following REST-API can be called.

Endpoint::

    POST https://{{aiven_rest_api}}/v1/project/{{project_id}}/test/service/{{service_name}}/flink/table

Header: ``Authorization Bearer TOKEN``

Body::

    {
    "integration_id": "{{integration_id}}",
    "name": "{{source_dest_name}}",
    "kafka_topic": "{{topic_name}}",
    "schema_sql": "{{topic_schema}}",
    "partitioned_by": "{{partition_by_clause}}"
    }

**Example**: Define a Flink table named ``KAlert`` pointing to a Kafka topic named ``alert`` available in the Kafka cluster identified by the integration with id ``a4af7409-d167-4f31-af13-ddd4cd06564f``

::

    {
    "integration_id": "a4af7409-d167-4f31-af13-ddd4cd06564f",
    "name": "KAlert",
    "kafka_topic": "alert",
    "schema_sql": "`node` INT, `occurred_at` TIMESTAMP_LTZ(3), `cpu_in_mb` FLOAT"
    }