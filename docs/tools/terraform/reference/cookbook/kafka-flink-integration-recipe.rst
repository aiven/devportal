Add the power of Apache Flink® to Apache Kafka® for stateful stream processing
==============================================================================

Whether it's an event-driven application or a data pipeline, Apache Flink® is an excellent choice due to its ability to perform computations at in-memory speed and at any scale. 
We can use Apache Kafka® as a highly-available, fault-tolerant platform and leverage the power of Flink's stateful data transformations alongside. This example shows how to set up an Aiven for Apache Kafka
with an Aiven for Apache Flink integration using the `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_.

Describe the setup
------------------

The following Terraform script stands up both Apache Kafka and Apache Flink services, creates the service integration and  related resources. The parameters and configurations will vary for your case and you can find
links to the advanced parameters as a reference at the end of this document.


``services.tf`` file:

.. code:: bash

  resource "aiven_flink" "flink" {
   project      = data.aiven_project.dev-advocates.project
   cloud_name   = "google-europe-west1"
   plan         = "business-8"
   service_name = "demo-flink"
  }

  resource "aiven_kafka" "kafka" {
   project      = data.aiven_project.dev-advocates.project
   cloud_name   = "google-europe-west1"
   plan         = "business-8"
   service_name = "demo-kafka"
  }

  resource "aiven_service_integration" "flink_to_kafka" {
   project                  = data.aiven_project.dev-advocates.project
   integration_type         = "flink"
   destination_service_name = aiven_flink.flink.service_name
   source_service_name      = aiven_kafka.kafka.service_name
  }

  resource "aiven_kafka_topic" "source" {
   project      = data.aiven_project.dev-advocates.project
   service_name = aiven_kafka.kafka.service_name
   partitions   = 2
   replication  = 3
   topic_name   = "source_topic"
  }

  resource "aiven_kafka_topic" "sink" {
   project      = data.aiven_project.dev-advocates.project
   service_name = aiven_kafka.kafka.service_name
   partitions   = 2
   replication  = 3
   topic_name   = "sink_topic"
  }

  resource "aiven_flink_table" "source" {
   project        = data.aiven_project.dev-advocates.project
   service_name   = aiven_flink.flink.service_name
   integration_id = aiven_service_integration.flink_to_kafka.integration_id
   table_name     = "source_table"
   kafka_topic    = aiven_kafka_topic.source.topic_name
   schema_sql     = <<EOF
    `cpu` INT,
    `node` INT,
    `occurred_at` TIMESTAMP(3) METADATA FROM 'timestamp',
    WATERMARK FOR `occurred_at` AS `occurred_at` - INTERVAL '5' SECOND
   EOF
  }

  resource "aiven_flink_table" "sink" {
   project        = data.aiven_project.dev-advocates.project
   service_name   = aiven_flink.flink.service_name
   integration_id = aiven_service_integration.flink_to_kafka.integration_id
   table_name     = "sink_table"
   kafka_topic    = aiven_kafka_topic.sink.topic_name
   schema_sql     = <<EOF
     `cpu` INT,
     `node` INT,
     `occurred_at` TIMESTAMP(3)
   EOF
  }

  resource "aiven_flink_job" "flink_job" {
   project      = data.aiven_project.dev-advocates.project
   service_name = aiven_flink.flink.service_name
   job_name     = "my_job"
   table_ids = [
     aiven_flink_table.source.table_id,
     aiven_flink_table.sink.table_id
   ]
   statement = <<EOF
     INSERT INTO ${aiven_flink_table.sink.table_name}
     SELECT * FROM ${aiven_flink_table.source.table_name}
     WHERE `cpu` > 70
   EOF
  }


The resource names are self-descriptive in terms of what they're doing. The resource ``"aiven_flink"`` creates an Aiven for Apache Flink resource with the project name, choice of cloud, an Aiven service plan, and
a specified service name. Similarly, the ``"aiven_service_integration"`` resource creates the integration between Apache Kafka and the Apache Flink service. Two ``"aiven_flink_table"``
resources are created - a **source** and a **sink** with a specified schema. Once the Terraform script is run, an Apache Flink job is started that copies data from the **source** Flink table to the **sink** Flink 
table where the **cpu** threshold is over a certain limit. The data originates at the resource ``"aiven_kafka_topic"`` called **source** and the processed data is put into another resource ``"aiven_kafka_topic"`` 
called **sink**.

More resources
--------------

You might find these related resources useful too:

- `Build a Streaming SQL Pipeline with Apache Flink® and Apache Kafka® <https://aiven.io/blog/build-a-streaming-sql-pipeline-with-flink-and-kafka>`_
- `Advanced parameters for Aiven for Apache Kafka® <https://developer.aiven.io/docs/products/kafka/reference/advanced-params.html>`_
- `Advanced parameters for Aiven for Apache Flink® <https://developer.aiven.io/docs/products/flink/reference/advanced-params.html>`_