Apache Kafka® as source and sink for Apache Flink® job
======================================================

This example shows how to set up an Aiven for Apache Kafka with an Aiven for Apache Flink integration using the `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_.
An Apache Kafka source topic is used as a data source, and Apache Flink processes the data to do filtering or transformation, and finally write the transformed output to a different target topic.

Let's cook!
-----------

Before looking at the Terraform script, let's visually realize how the services will be connected:

.. mermaid::

   flowchart LR
      subgraph Apache Kafka
      SourceTopic
      end
      subgraph Apache Flink
      SourceTopic-->|FlinkJob|FlinkSourceTable
      FlinkSourceTable-->|Filter/Transform|FlinkTargetTable
      end
      subgraph Apache Kafka
      FlinkTargetTable-->|FlinkJob|TargetTopic
      end

If you relate the above diagram to the following example, both source and target Apache Kafka topics are part of the same Apache Kafka cluster.

The following Terraform script stands up both Apache Kafka and Apache Flink services, creates the service integration, source and target Apache Kafka topics, an Apache Flink job and two Apache Flink tables. 

``services.tf`` file:

.. code:: bash

  resource "aiven_flink" "flink" {
    project      = var.project_name
    cloud_name   = "google-europe-west1"
    plan         = "business-8"
    service_name = "demo-flink"
  }

  resource "aiven_kafka" "kafka" {
    project      = var.project_name
    cloud_name   = "google-europe-west1"
    plan         = "business-8"
    service_name = "demo-kafka"
  }

  resource "aiven_service_integration" "flink_to_kafka" {
    project                  = var.project_name
    integration_type         = "flink"
    destination_service_name = aiven_flink.flink.service_name
    source_service_name      = aiven_kafka.kafka.service_name
  }

  resource "aiven_kafka_topic" "source" {
    project      = var.project_name
    service_name = aiven_kafka.kafka.service_name
    partitions   = 2
    replication  = 3
    topic_name   = "source_topic"
  }

  resource "aiven_kafka_topic" "sink" {
    project      = var.project_name
    service_name = aiven_kafka.kafka.service_name
    partitions   = 2
    replication  = 3
    topic_name   = "sink_topic"
  }

  resource "aiven_flink_table" "source" {
    project        = var.project_name
    service_name   = aiven_flink.flink.service_name
    integration_id = aiven_service_integration.flink_to_kafka.integration_id
    table_name     = "source_table"
    kafka_topic    = aiven_kafka_topic.source.topic_name
    schema_sql = <<EOF
      hostname STRING,
      cpu STRING,
      usage DOUBLE,
      occurred_at BIGINT,
      time_ltz AS TO_TIMESTAMP_LTZ(occurred_at, 3),
      WATERMARK FOR time_ltz AS time_ltz - INTERVAL '10' SECOND
    EOF
  }

  resource "aiven_flink_table" "sink" {
    project        = var.project_name
    service_name   = aiven_flink.flink.service_name
    integration_id = aiven_service_integration.flink_to_kafka.integration_id
    table_name     = "sink_table"
    kafka_topic    = aiven_kafka_topic.sink.topic_name
    schema_sql     = <<EOF
      time_ltz TIMESTAMP(3),
      hostname STRING,
      cpu STRING,
      usage DOUBLE
    EOF
  }

  resource "aiven_flink_job" "flink_job" {
    project      = var.project_name
    service_name = aiven_flink.flink.service_name
    job_name     = "my_job"
    table_ids = [
      aiven_flink_table.source.table_id,
      aiven_flink_table.sink.table_id
    ]
    statement = <<EOF
      INSERT INTO ${aiven_flink_table.sink.table_name}
      SELECT
        time_ltz,
        hostname,
        cpu,
        usage
      FROM ${aiven_flink_table.source.table_name}
      WHERE usage > 70
    EOF
  }

The resource ``"aiven_flink"`` creates an Aiven for Apache Flink resource with the project name, choice of cloud, an Aiven service plan, and a specified service name. 
``"aiven_kafka"`` resource creates an Apache Kafka cluster and two Apache Kafka topics (**source** and a **sink**) are created using the ``"aiven_kafka_topic"`` resource.
Similarly, the ``"aiven_service_integration"`` resource creates the integration between Apache Kafka and the Apache Flink service. Two ``"aiven_flink_table"``
resources are created - a **source** and a **sink** with a specified schema. Once the Terraform script is run, an Apache Flink job is started that copies data from the **source** Flink table to the **sink** Flink 
table where the ``usage`` threshold is over a certain limit. The data originates at the resource ``"aiven_kafka_topic"`` called **source** and the processed data is put into another resource ``"aiven_kafka_topic"`` 
called **sink**.

To test the data streaming pipeline, you can use the `fake data producer for Apache Kafka on Docker <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_ making sure that in the ``conf/env.conf`` file you specify ``TOPIC="source-topic"`` (same topic name defined in the resource ``"aiven_kafka_topic"``) and ``SUBJECT="metric"`` together with the appropriate project name, service name and required credentials.

More resources
--------------

The parameters and configurations will vary for your case. Please refer below for Apache Kafka and Apache Flink advanced parameters, a related blog, and how to get started with Aiven Terraform Provider:

- `Build a Streaming SQL Pipeline with Apache Flink® and Apache Kafka® <https://aiven.io/blog/build-a-streaming-sql-pipeline-with-flink-and-kafka>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
- `Advanced parameters for Aiven for Apache Kafka® <https://developer.aiven.io/docs/products/kafka/reference/advanced-params.html>`_
- `Advanced parameters for Aiven for Apache Flink® <https://developer.aiven.io/docs/products/flink/reference/advanced-params.html>`_