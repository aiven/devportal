Apache Kafka® as source and sink with Apache Flink® to process streaming data
=============================================================================

This example shows how to set up an Aiven for Apache Kafka with an Aiven for Apache Flink integration using the `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_.
An Apache Kafka source topic is used as a data source, and Apache Flink processes the data to do filtering or transformation, and finally write the transformed output to a sink topic.
Please get yourself familiar with :doc:`Aiven for Apache Flink concepts <../../../../products/flink/concepts>` before you start cooking.

Let's cook!
-----------

Before looking at the Terraform script, let's visually realize how the services will be connected:

.. mermaid::

   flowchart LR
      subgraph Aiven for Apache Kafka
      SourceTopic
      end
      subgraph Aiven for Apache Flink Application
      SourceTopic-->|FlinkTableMapping|FlinkSourceTable
      FlinkSourceTable-->|Filter/Transform|FlinkTargetTable
      end
      subgraph Aiven for Apache Kafka
      FlinkTargetTable-->|FlinkTableMapping|SinkTopic
      end

Imagine that you are collecting CPU usage for hundreds of machines in your data centre and these metrics are populated in an Apache Kafka topic called ``cpu_measurements``. But you're interested in learning about those machines with CPU usages higher than 85% and write the filtered messages into a topic called ``cpu_high_usage``.
If you relate the above diagram to this example, both source and target Apache Kafka topics are part of the same Apache Kafka cluster. To do the processing on the data, you'll be using an Aiven for Apache Flink Application which is an abstraction layer on top of Apache Flink SQL that includes all the elements related to a Flink job to help build your data processing pipeline. 

The following Terraform script stands up both Apache Kafka and Apache Flink services, creates the service integration, source and target Apache Kafka topics, an Aiven for Apache Flink application, and the Aiven for Apache Flink application version. By design, you cannot manage the deployment resource using Aiven Terraform Provider. 
In order to do so, you'll need to use Aiven console or Aiven CLI.

.. dropdown:: Expand to check out the relevant common files needed for this recipe.

    Navigate to a new folder and add the following files.

    1. Add the following to a new ``provider.tf`` file:

    .. code:: terraform

       terraform {
         required_providers {
           aiven = {
             source  = "aiven/aiven"
             version = "~> 3.12.0"
           }
         }
       }
   
       provider "aiven" {
         api_token = var.aiven_api_token
       }
   
    You can also set the environment variable ``TF_VAR_aiven_api_token`` for the ``api_token`` property and ``TF_VAR_project_name`` for the ``project_name`` property. With this, you don't need to pass the ``-var-file`` flag when executing Terraform commands.
 
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
  
   # Flink service
  
   resource "aiven_flink" "demo-flink" {
      project      = var.project_name
      cloud_name   = "google-northamerica-northeast1"
      plan         = "business-8"
      service_name = "demo-flink"
   }

   # Kafka service

   resource "aiven_kafka" "demo-kafka" {
     project      = var.project_name
     cloud_name   = "google-northamerica-northeast1"
     plan         = "business-8"
     service_name = "demo-kafka"
   }

   # Flink-Kafka integration

   resource "aiven_service_integration" "flink_to_kafka" {
     project                  = var.project_name
     integration_type         = "flink"
     destination_service_name = aiven_flink.demo-flink.service_name
     source_service_name      = aiven_kafka.demo-kafka.service_name
   }

   # Flink application

   resource "aiven_flink_application" "demo-flink-app" {
     project      = var.project_name
     service_name = aiven_flink.demo-flink.service_name
     name         = "demo-flink-app"
   }

   # Flink application version (includes Flink table creation)

   resource "aiven_flink_application_version" "demo-flink-app-version" {
     project        = var.project_name
     service_name   = aiven_flink.demo-flink.service_name
     application_id = aiven_flink_application.demo-flink-app.application_id
     statement      = <<EOT
     INSERT INTO cpu_high_usage_table SELECT * FROM iot_measurements_table WHERE usage > 85
     EOT
     sinks {
       create_table   = <<EOT
       CREATE TABLE cpu_high_usage_table (
         time_ltz TIMESTAMP(3),
         hostname STRING,
         cpu STRING,
         usage DOUBLE
       ) WITH (
         'connector' = 'kafka',
         'properties.bootstrap.servers' = '',
         'scan.startup.mode' = 'earliest-offset',
         'topic' = 'cpu_high_usage',
         'value.format' = 'json'
       )
     EOT
       integration_id = aiven_service_integration.flink_to_kafka.integration_id
     }
     sources {
       create_table   = <<EOT
       CREATE TABLE iot_measurements_table (
         time_ltz TIMESTAMP(3),
         hostname STRING,
         cpu STRING,
         usage DOUBLE
       ) WITH (
         'connector' = 'kafka',
         'properties.bootstrap.servers' = '',
         'scan.startup.mode' = 'earliest-offset',
         'topic' = 'iot_measurements',
         'value.format' = 'json'
       )
       EOT
       integration_id = aiven_service_integration.flink_to_kafka.integration_id
     }
   }

   # Kafka source topic

   resource "aiven_kafka_topic" "source" {
     project      = var.project_name
     service_name = aiven_kafka.demo-kafka.service_name
     partitions   = 2
     replication  = 3
     topic_name   = "iot_measurements"
   }

   # Kafka sink topic

   resource "aiven_kafka_topic" "sink" {
     project      = var.project_name
     service_name = aiven_kafka.demo-kafka.service_name
     partitions   = 2
     replication  = 3
     topic_name   = "cpu_high_usage"
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
Similarly, the ``"aiven_service_integration"`` resource creates the integration between Apache Kafka and the Apache Flink service.
``aiven_flink_application`` resource ``demo-flink-app`` creates the Aiven for Apache Flink application whereas ``aiven_flink_application_version`` resource ``demo-flink-app-version`` contains all the necessary specifications.
For example, the application version resource creates two Flink tables, ``iot_measurements_table`` as the source table and ``cpu_high_usage_table`` as the sink table with the specified schema.

Once the Terraform script is run, all of the resources from the manifest are created but you'll need to create the deployment. From the Aiven console, go to the ``Application`` tab under the newly created Aiven for Apache Flink service. Click on ``demo-flink-app`` and click **Create deployment**. If this is your first deployment, you won't have an option for :doc:`savepoint <../../../../products/flink/concepts/savepoints>`.
Accept the default setting or make necessary selection and then deploy. 

To test the data streaming pipeline, you can use the `fake data producer for Apache Kafka on Docker <https://github.com/aiven/fake-data-producer-for-apache-kafka-docker>`_ making sure that in the ``conf/env.conf`` file you specify ``TOPIC="cpu_measurements"`` (same topic name defined in the resource ``"aiven_kafka_topic" "source"``) and ``SUBJECT="metric"`` together with the appropriate project name, service name and required credentials.
In the destination topic, defined in the resource ``"aiven_kafka_topic" "sink"``, you should see only data samples having ``usage`` above 85. A note that the fake data generates CPU usages higher than 70.

More resources
--------------

The parameters and configurations will vary for your case. Please refer below for Apache Kafka and Apache Flink advanced parameters, a related blog, and how to get started with Aiven Terraform Provider:

- `Build a Streaming SQL Pipeline with Apache Flink® and Apache Kafka® <https://aiven.io/blog/build-a-streaming-sql-pipeline-with-flink-and-kafka>`_
- `Set up your first Aiven Terraform project <https://docs.aiven.io/docs/tools/terraform/get-started.html>`_
- `Advanced parameters for Aiven for Apache Kafka® <https://docs.aiven.io/docs/products/kafka/reference/advanced-params.html>`_
- `Advanced parameters for Aiven for Apache Flink® <https://docs.aiven.io/docs/products/flink/reference/advanced-params.html>`_
