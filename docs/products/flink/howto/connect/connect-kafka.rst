Create a Kafka based Flink table
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
``{{topic_name}}``               Name of the Kafka Topic to use as source or sink
``{{topic_schema}}``             Definition of `topic schema <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/table/sql/create/#columns>`_
``{{partition_by_clause}}``      Topic partition definition
===========================      ===============================================================================================================================

Create Kafka based Flink table via REST-APIs
''''''''''''''''''''''''''''''''''''''''''''

To create an Aiven for Apache Kafka based Flink table, use the following REST-API.

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

More information on the table definition supported syntax can be found in the :doc:`dedicated page</docs/products/concepts/supported_syntax_sql_editor>`.

Create Kafka based Flink table via Aiven console
''''''''''''''''''''''''''''''''''''''''''''''''

To create a Flink table based on Aiven for Apache Kafka via Aiven console:

1. Navigate to the Aiven for Apache Flink service page, and open the **Jobs and Data** tab

2. Select the **Data Tables** sub-tab and select the Aiven for Apache Kafka integration to use

3. Define the Flink table **Name**, the source **Kafka topic** and **Schema SQL** 

**Example**: Define a Flink table named ``KAlert`` pointing to a Kafka topic named ``alert`` available in the Aiven for Apache Kafka service named ``kafka-devportal-example``

Settings:

* ``kafka-devportal-example`` as the selected service 
* ``Kalert`` as **Name**
* ``alert`` as **Kafka topic**
* ``node INT, occurred_at TIMESTAMP_LTZ(3), cpu_in_mb FLOAT`` as **SQL schema**

The image below shows the Aiven console page with the filled details.

.. image:: /images/products/flink/create-table-topic.png
  :scale: 50 %
  :alt: Image of the Aiven for Apache Flink Jobs and Data tab when creating a Flink table on top of an Aiven for Apache Kafka topic