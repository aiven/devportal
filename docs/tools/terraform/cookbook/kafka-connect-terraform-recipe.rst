Cooking with Terraform - Apache Kafka® Connect Integration
==========================================================

`Kafka Connect <https://aiven.io/kafka-connect>`_ helps simplify getting data in and out of Kafka. Kafka Connectors can either be source (for pulling data from other systems into Kafka) or sink connectors (for pushing data into other systems from Kafka).
This recipe for the Terraform cookbook includes an Aiven for Kafka service, an Aiven for Apache Kafka® Connect, an Aiven for OpenSearch® service, and the integrations among these services.

Setup
=====

The problem that we're trying to solve is to get data out of Kafka and into OpenSeach. We're using a Kafka Connect service to make this happen. Because these services are created programmatically, we'll also need to link the services together.
Before looking at the Terraform script, let's visually realize how the services will be connected:

.. mermaid::

    flowchart LR
        Kafka --> |Kafka Connect Service Integration| KafkaConnect
        KafkaConnect --> | Kafka Connector OpenSearch Sink | OpenSearch

Let's cook
==========

There are four different Terraform files - each serving a specific purpose. Let's go over each of these files.

1. ``provider.tf`` file:

.. code:: bash

   terraform {
      required_providers {
         aiven = {
            source  = "aiven/aiven"
            version = ">= 2.6.0, < 3.0.0"
         }
      }
   }

   provider "aiven" {
      api_token = var.aiven_api_token
   }


Consider this code block similar to declaring a dependency; the **Aiven Terraform Provider** in this case. We mention the source of the provider and specify a certain version to be used.
Following `Aiven Terraform Provider doc <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_, ``api_token`` is the only parameter for the provider configuration.
Make sure the owner of the API Authentication Token has admin permissions in Aiven.

2. ``variables.tf`` file:

.. code:: bash

   variable "aiven_api_token" {
      description = "Aiven console API token"
      type = string
   }

   variable "project_name" {
      description = "Aiven console project name"
      type        = string
   }

This file relates to the Terraform best practices since you don't want to hardcode certain values within the main Terraform file.

3. ``var-values.tfvars`` file:

.. code:: bash

   aiven_api_token = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
   project_name = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"

This is where you put the actual values for Aiven API token and Aiven console project name. This file is passed to Terraform using the ``-var-file=`` flag.

4. ``services.tf`` file:

.. code:: bash

   # Kafka service
   resource "aiven_kafka" "dewans-tf-kafka" {
   project                 = var.project_name
   cloud_name              = "google-northamerica-northeast1"
   plan                    = "business-4"
   service_name            = "dewans-tf-kafka"
   maintenance_window_dow  = "monday"
   maintenance_window_time = "10:00:00"
   kafka_user_config {
      kafka_connect = true
      kafka_rest    = true
      kafka_version = "3.0"
      kafka {
         group_max_session_timeout_ms = 70000
         log_retention_bytes          = 1000000000
      }
   }
   }

   # Kafka connect service
   resource "aiven_kafka_connect" "dewans-tf-kafka-connect" {
   project = var.project_name
   cloud_name = "google-northamerica-northeast1"
   plan = "business-4"
   service_name = "dewans-tf-kafka-connect"
   maintenance_window_dow = "monday"
   maintenance_window_time = "10:00:00"
   kafka_connect_user_config {
      kafka_connect {
         consumer_isolation_level = "read_committed"
      }
      public_access {
         kafka_connect = true
      }
   }
   }

   # Kafka connect service integration
   resource "aiven_service_integration" "dewan_tf_integration" {
   project = var.project_name
   integration_type = "kafka_connect"
   source_service_name = aiven_kafka.dewans-tf-kafka.service_name
   destination_service_name = aiven_kafka_connect.dewans-tf-kafka-connect.service_name
   kafka_connect_user_config {
      kafka_connect {
         group_id = "connect"
         status_storage_topic = "__connect_status"
         offset_storage_topic = "__connect_offsets"
      }
   }
   }

   # Kafka topic
   resource "aiven_kafka_topic" "kafka-topic1" {
   project = var.project_name
   service_name = aiven_kafka.dewans-tf-kafka.service_name
   topic_name = "dewans-tf-kafka-topic1"
   partitions = 3
   replication = 2
   }

   # Kafka connector
   resource "aiven_kafka_connector" "kafka-os-con1" {
   project = var.project_name
   service_name = aiven_kafka.dewans-tf-kafka.service_name
   connector_name = "kafka-os-con1"
   config = {
      "topics" = aiven_kafka_topic.kafka-topic1.topic_name
      "connector.class" : "io.aiven.kafka.connect.opensearch.OpensearchSinkConnector"
      "type.name" = "os-connector"
      "name" = "kafka-os-con1"
      "connection.url" = "https://${aiven_opensearch.os-service1.service_host}:${aiven_opensearch.os-service1.service_port}"
      "connection.username" = aiven_opensearch.os-service1.service_username
      "connection.password" = aiven_opensearch.os-service1.service_password
      "key.converter" = "org.apache.kafka.connect.storage.StringConverter"
      "value.converter" = "org.apache.kafka.connect.json.JsonConverter"
      "tasks.max" = 1
      "schema.ignore" = true
      "value.converter.schemas.enable" = false
   }
   }

   # Opensearch service
   resource "aiven_opensearch" "os-service1" {
   project = var.project_name
   cloud_name = "google-northamerica-northeast1"
   plan = "business-4"
   service_name = "os-service1"
   maintenance_window_dow = "monday"
   maintenance_window_time = "10:00:00"
   opensearch_user_config {
      opensearch_version = "1"
   }
   }

This file is where all the magic (a.k.a cooking) happens. Three services and two integrations are defined in separate blocks. ``resource`` indicates the type of Aiven resource and each project identifies a specific project (this value is passed from the ``variables.tf`` file.
For the three services, we need to specify the type of `Aiven plan <https://aiven.io/pricing>`_ and some product specific configurations. For the integrations, we specify the service name where the integration is happening and the integration configurations.
Apart from that, we also define a Kafka topic that Terraform will create as part of the plan. 

Assuming that you have `Terraform installed <https://www.terraform.io/downloads>`_, create an empty folder and add the above files to that folder. Then execute the following commands in order:

.. code:: bash

   terraform init 

This command performs several different initialization steps in order to prepare the current working directory for use with Terraform. In our case, this command automatically finds, downloads, and installs the necessary Aiven Terraform Provider plugins.

.. code:: bash

   terraform plan -var-file=var-values.tfvars

This command creates an execution plan and shows you the resources that will be created (or modified) for you. This command does not actually create any resource; this is more like a preview.

.. code:: bash

   terraform apply -var-file=var-values.tfvars

If you're satisfied with ``terraform plan``, you execute ``terraform apply`` command which actually does the task or creating (or modifying) your infrastructure resources. 

Optional
--------

If this was a test environment, be sure to delete the resources once you're done to avoid consuming unwanted bills. 

.. warning::

   Use this command with caution. This will actually delete resources that might have important data.

.. code:: bash

   terraform destroy -var-file=var-values.tfvars


Wrap up
=======

If you liked this recipe, try out some of the other recipes within the Aiven Terraform cookbook.