Create a PostgreSQL based Flink table
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

Create PostgreSQL based Flink table via REST-APIs
'''''''''''''''''''''''''''''''''''''''''''''''''

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

Create PostgreSQL based Flink table via Aiven console
'''''''''''''''''''''''''''''''''''''''''''''''''''''

To create a Flink table based on Aiven for PostgreSQL via Aiven console:

1. Navigate to the Aiven for Apache Flink service page, and open the **Jobs and Data** tab

2. Select the **Data Tables** sub-tab and select the Aiven for PostgreSQL integration to use

3. Define the Flink table **Name**, the source **JDBC table** name and **Schema SQL** 

**Example**: Define a Flink table named ``node_info`` pointing to a PostgreSQL table named ``public.node_definition`` available in the Aiven for PostgreSQL service named ``pg-devportal-example``

Settings:

* ``pg-devportal-example`` as the selected service 
* ``node_info`` as **Name**
* ``public.node_definition`` as **JDBC table**
* ``node INT, node_description VARCHAR`` as **SQL schema**

The image below shows the Aiven console page with the filled details.

.. image:: /images/products/flink/create-table-pg.png
  :scale: 50 %
  :alt: Image of the Aiven for Apache Flink Jobs and Data tab when creating a Flink table on top of an Aiven for PostgreSQL table