Kafka with Kafka Connect services with custom configurations
============================================================

This example shows how to create an Apache Kafka service integrates with Kafka Connect with some custom configurations. 

Aiven has a concept of service integrations to manage the relationships between components. `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_
has a specific resource type in Terraform for service integration. 

Describe the setup
------------------

Here is the sample Terraform file to stand-up and connect all the services. Keep in mind that some parameters and configurations will vary for your case. A reference to the Kafka and Kafka Connect configurations are added at the end of this document.

``kafka.tf`` file:

.. code:: bash

 ##Create the source Kafka
 resource "aiven_kafka" "kafka1" {
 project = var.project_name
 cloud_name = "google-europe-west1"
 plan = "business-4"   ###kafka-connect will not able to run on startup-2
 service_name = "kafka-dev-tf"
 maintenance_window_dow  = "sunday"
 maintenance_window_time = "01:00:00"

 kafka_user_config {
    kafka_rest      = true
    kafka_connect   = true
    schema_registry = true
    kafka_version   = "3.1"
    #ip_filter       = ["0.0.0.0/0", "8.8.8.8", "9.9.9.9"]

    kafka {
      auto_create_topics_enable    = true
      num_partitions               = 3
      default_replication_factor   = 2
      min_insync_replicas          = 2
      message_max_bytes            = 131072
      group_max_session_timeout_ms = 70000
      log_retention_bytes          = 1000000000
    }

    kafka_authentication_methods {
      certificate = true
    }

    public_access {
      kafka_rest    = true
      kafka_connect = true
      }
     }
 }

 output "kafka1_value" {
 value = aiven_kafka.kafka1
 sensitive = true
 }

 resource "aiven_service_user" "kafka_user" {
   project      = var.project_name
   service_name = aiven_kafka.kafka1.service_name
   username     = var.kafka_user_name
 }

 resource "aiven_kafka_acl" "kafka_user_acl" {
   project      = var.project_name
   service_name = aiven_kafka.kafka1.service_name
   ##username     = "kafka_*"
   username   = var.kafka_user_name
   permission = "read"
   topic      = "*"
 }


 #create Kafka connector
 resource "aiven_kafka_connect" "kafka_connect1" {
   project = var.project_name
   cloud_name = "google-europe-west1"
   plan = "startup-4"
   service_name = "kafka-connect-tf"
   maintenance_window_dow  = "sunday"
   maintenance_window_time = "01:00:00"

 kafka_connect_user_config {
 kafka_connect {
     consumer_isolation_level = "read_committed"
     }

 public_access {
     kafka_connect = true
     }
   }
 }

 output "kafka_connect1_value" {
 value = aiven_kafka_connect.kafka_connect1
 sensitive = true
 }

 #Source kafka and Kafka connector integration
 resource "aiven_service_integration" "si1" {
   project = var.project_name
   integration_type = "kafka_connect"
   source_service_name = aiven_kafka.kafka1.service_name
   destination_service_name = aiven_kafka_connect.kafka_connect1.service_name

 kafka_connect_user_config {
   kafka_connect {
   group_id = "connect"
   status_storage_topic = "__connect_status"
   offset_storage_topic = "__connect_offsets"
   config_storage_topic = "__connect_configs"
    }
  }
 }

 output "si1_value" {
  value = aiven_service_integration.si1
  sensitive = true
 }


This file creates two Aiven services - a Kafka service and a Kafka Connect service. One service integrations among these two services, an additional kafka user and a kafka ACL entry with the defined username and defined permission will also be created from this terraform file.

Additonal setup file
--------------------

Below is the example of the variables.tf for this example

``variables.tf`` file:

.. code:: bash

 variable "aiven_api_token" {
   description = "Aiven console API token"
   type = string
 }

 variable "project_name" {
   description = "Aiven console project name"
   type        = string
 }

 variable "kafka_user_name" {
   description = "Aiven kafka user name"
   type        = string
 }


More resources
--------------

You might find these related resources useful too:

- `Configuration options for Kafka <https://developer.aiven.io/docs/products/kafka/reference/advanced-params.html>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
