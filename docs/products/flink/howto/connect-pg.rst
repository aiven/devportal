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
``{{jdbc_table}}``               Name of the database table to use as source or sink
``{{table_schema}}``             Definition of `table schema <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/table/sql/create/#columns>`_
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
    "jdbc_table": "{{jdbc_table}}",
    "schema_sql": "{{table_schema}}"
    }

**Example**: Define a Flink table named ``node_info`` pointing to a PostgreSQL table named ``public.node_definition`` available in the PostgreSQL database identified by the integration with id ``a4af7409-d167-4f31-af13-ddd4cd06564f``

::

    {
    "integration_id": "a4af7409-d167-4f31-af13-ddd4cd06564f",
    "name": "node_info",
    "jdbc_table": "public.node_definition",
    "schema_sql": "`node` INT, `node_description` VARCHAR"
    }
