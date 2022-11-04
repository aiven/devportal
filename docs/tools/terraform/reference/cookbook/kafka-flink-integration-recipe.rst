Apache Kafka® as source and sink for Apache Flink® job
======================================================

This example shows how to set up an Aiven for Apache Kafka with an Aiven for Apache Flink integration using the `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_.
An Apache Kafka source topic is used as a data source, and Apache Flink processes the data to do filtering or transformation, and finally write the transformed output to a sink topic.

Let's cook!
-----------

Before looking at the Terraform script, let's visually realize how the services will be connected:

.. mermaid::

   flowchart LR
      subgraph Apache Kafka
      SourceTopic
      end
      subgraph Apache Flink
      SourceTopic-->|FlinkTableMapping|FlinkSourceTable
      FlinkSourceTable-->|Filter/Transform|FlinkTargetTable
      end
      subgraph Apache Kafka
      FlinkTargetTable-->|FlinkTableMapping|SinkTopic
      end

If you relate the above diagram to the following example, both source and target Apache Kafka topics are part of the same Apache Kafka cluster.

Imagine that you are collecting CPU usage for hundreds of machines in your data centre and these metrics are populated in an Apache Kafka topic called ``cpu_measurements``. But you're interested in learning about those machines with CPU usages higher than 85%.
For this, you'd like to run an Apache Flink job and write the filtered messages into a topic called ``cpu_high_usage``. The following Terraform script stands up both Apache Kafka and Apache Flink services, creates the service integration, source and target Apache Kafka topics, an Apache Flink job, and two Apache Flink tables. 

.. dropdown:: Expand to check out the relevant common files needed for this recipe.

    Navigate to a new folder and add the following files.

    1. Add the following to a new ``provider.tf`` file:

    .. code:: terraform

       terraform {
         required_providers {
           aiven = {
             source  = "aiven/aiven"
             version = ">= 3.7"
           }
         }
       }
   
       provider "aiven" {
         api_token = var.aiven_api_token
       }
   
    You can also set the environment variable ``AIVEN_TOKEN`` for the ``api_token`` property. With this, you don't need to pass the ``-var-file`` flag when executing Terraform commands.
 
    2. To avoid including sensitive information in source control, the variables are defined here in the ``variables.tf`` file. You can then use a ``*.tfvars`` file with the actual values so that Terraform receives the values during runtime, and exclude it.

    The ``variables.tf`` file defines the API token, the project name to use, and the prefix for the service name:

    .. code:: terraform

       variable "aiven_api_token" {
         description = "Aiven console API token"
         type        = string
       }
   
       variable "project_name" {
         description = "Aiven console project name"
         type        = string
       }
      
    3. The ``var-values.tfvars`` file holds the actual values and is passed to Terraform using the ``-var-file=`` flag.

    ``var-values.tfvars`` file:

    .. code:: terraform

       aiven_api_token     = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
       project_name        = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"

``services.tf`` file:

.. code:: terraform

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
    topic_name   = "iot_measurements"
  }
  
  resource "aiven_kafka_topic" "sink" {
    project      = var.project_name
    service_name = aiven_kafka.kafka.service_name
    partitions   = 2
    replication  = 3
    topic_name   = "cpu_high_usage"
  }
  
  resource "aiven_flink_table" "source" {
    project        = var.project_name
    service_name   = aiven_flink.flink.service_name
    integration_id = aiven_service_integration.flink_to_kafka.integration_id
    table_name     = "iot_measurements_table"
    kafka_topic    = aiven_kafka_topic.source.topic_name
    schema_sql     = <<-EOF
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
    table_name     = "cpu_high_usage_table"
    kafka_topic    = aiven_kafka_topic.sink.topic_name
    schema_sql     = <<-EOF
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
    statement = <<-EOF
          INSERT INTO ${aiven_flink_table.sink.table_name}
          SELECT
            time_ltz,
            hostname,
            cpu,
            usage
          FROM ${aiven_flink_table.source.table_name}
          WHERE usage > 85
    EOF
  }

.. dropdown:: Expand to check out how to execute the Terraform files.

    The ``init`` command performs several different initialization steps in order to prepare the current working directory for use with Terraform. In our case, this command automatically finds, downloads, and installs the necessary Aiven Terraform provider plugins.
    
    .. code:: shell

       terraform init

    The ``plan`` command creates an execution plan and shows you the resources that will be created (or modified) for you. This command does not actually create any resource; this is more like a preview.

    .. code:: bash

       terraform plan -var-file=var-values.tfvars

    If you're satisfied with the output of ``terraform plan``, go ahead and run the ``terraform apply`` command which actually does the task or creating (or modifying) your infrastructure resources. 

    .. code:: bash

       terraform apply -var-file=var-values.tfvars

The resource ``"aiven_flink"`` creates an Aiven for Apache Flink resource with the project name, choice of cloud, an Aiven service plan, and a specified service name. 
``"aiven_kafka"`` resource creates an Apache Kafka cluster and two Apache Kafka topics (``cpu_measurements`` and a ``cpu_high_usage``) are created using the ``"aiven_kafka_topic"`` resource.
Similarly, the ``"aiven_service_integration"`` resource creates the integration between Apache Kafka and the Apache Flink service. Two ``"aiven_flink_table"``
resources are created - a **source** and a **sink** with a specified schema. Once the Terraform script is run, an Apache Flink job is started that copies data from the **source** Flink table to the **sink** Flink 
table where the ``usage`` threshold is over a certain limit. The data originates at the resource ``"aiven_kafka_topic"`` called **source** and the processed data is put into another resource ``"aiven_kafka_topic"`` 
called **sink**.

To test the data streaming pipeline, you can use the `fake data producer for Apache Kafka on Docker <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_ making sure that in the ``conf/env.conf`` file you specify ``TOPIC="cpu_measurements"`` (same topic name defined in the resource ``"aiven_kafka_topic" "source"``) and ``SUBJECT="metric"`` together with the appropriate project name, service name and required credentials.
In the destination topic, defined in the resource ``"aiven_kafka_topic" "sink"``, you should see only data samples having ``usage`` above 85. A note that the fake data generates CPU usages higher than 70.

More resources
--------------

The parameters and configurations will vary for your case. Please refer below for Apache Kafka and Apache Flink advanced parameters, a related blog, and how to get started with Aiven Terraform Provider:

- `Build a Streaming SQL Pipeline with Apache Flink® and Apache Kafka® <https://aiven.io/blog/build-a-streaming-sql-pipeline-with-flink-and-kafka>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
- `Advanced parameters for Aiven for Apache Kafka® <https://developer.aiven.io/docs/products/kafka/reference/advanced-params.html>`_
- `Advanced parameters for Aiven for Apache Flink® <https://developer.aiven.io/docs/products/flink/reference/advanced-params.html>`_
