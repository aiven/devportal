Apache Kafka® Connect Services with Custom Configurations
=========================================================

Apache Kafka® Connect is an open-source component that allows Apache Kafka® to connect with various data systems via connectors. You can think of connectors as the translators between Apache Kafka topics and external systems.
This example uses `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_ to deploy Apache Kafka, Apache Kafka Connect, and the service integration between them, as well as related resources and configurations.

Before looking at the Terraform script, let's visually realize how the services will be connected:

.. mermaid::

   flowchart LR
      subgraph Aiven-for-Apache-Kafka
      id4[[Aiven Kafka User]]
      id5[[Aiven Kafka User ACL]]
      end
      Aiven-for-Apache-Kafka <--> Aiven-for-Apache-Kafka-Connect --> OpenSearch
      Producer --> Aiven-for-Apache-Kafka --> Consumer

Let's cook!
------------

Here is the sample Terraform file to stand-up and connect all the services. Terraform also performs some custom configurations on these resources.

.. Tip::

    Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe. For example, you'll need to declare the variables for ``project_name``, ``api_token``, and ``kafka_user_name``.

``services.tf`` file:

.. code:: terraform

  resource "aiven_kafka" "kafka" {
    project                 = var.project_name
    cloud_name              = "google-europe-west1"
    plan                    = "business-4"
    service_name            = "demo-kafka"
    maintenance_window_dow  = "sunday"
    maintenance_window_time = "01:00:00"
  
    kafka_user_config {
      kafka_rest      = true
      kafka_connect   = true
      schema_registry = true
      kafka_version   = "3.1"
  
      kafka {
        auto_create_topics_enable    = true
        num_partitions               = 3
        default_replication_factor   = 2
        min_insync_replicas          = 2
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

  resource "aiven_kafka_topic" "kafka_topic" {
  project                = var.project_name
  service_name           = aiven_kafka.kafka.service_name
  topic_name             = "logs-app-1"
  partitions             = 5
  replication            = 3

  config {
    flush_ms                       = 10
    unclean_leader_election_enable = true
    cleanup_policy                 = "compact,delete"
    }
  }
  
  resource "aiven_kafka_user" "kafka_user" {
    project      = var.project_name
    service_name = aiven_kafka.kafka.service_name
    username     = var.kafka_user_name
  }
  
  resource "aiven_kafka_acl" "kafka_user_acl" {
    project      = var.project_name
    service_name = aiven_kafka.kafka.service_name
    username     = var.kafka_user_name
    permission   = "read"
    topic        = aiven_kafka_topic.kafka_topic.topic_name
  }
  
  resource "aiven_kafka_connect" "kafka_connect" {
    project                 = var.project_name
    cloud_name              = "google-europe-west1"
    plan                    = "startup-4"
    service_name            = "demo-kafka-connect"
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
  
  resource "aiven_service_integration" "kafka-to-connect" {
    project                  = var.project_name
    integration_type         = "kafka_connect"
    source_service_name      = aiven_kafka.kafka.service_name
    destination_service_name = aiven_kafka_connect.kafka_connect.service_name
  
    kafka_connect_user_config {
      kafka_connect {
        group_id             = "connect"
        status_storage_topic = "__connect_status"
        offset_storage_topic = "__connect_offsets"
        config_storage_topic = "__connect_configs"
      }
    }
  }

  resource "aiven_kafka_connector" "kafka-os-con1" {
  project        = var.project_name
  service_name   = aiven_kafka.kafka.service_name
  connector_name = "kafka-os-con1"
  config = {
    "topics" = aiven_kafka_topic.kafka_topic.topic_name
    "connector.class" : "io.aiven.kafka.connect.opensearch.OpensearchSinkConnector"
    "type.name"                      = "os-connector"
    "name"                           = "kafka-os-con1"
    "connection.url"                 = "https://${aiven_opensearch.os-service1.service_host}:${aiven_opensearch.os-service1.service_port}"
    "connection.username"            = aiven_opensearch.os-service1.service_username
    "connection.password"            = aiven_opensearch.os-service1.service_password
    "key.converter"                  = "org.apache.kafka.connect.storage.StringConverter"
    "value.converter"                = "org.apache.kafka.connect.json.JsonConverter"
    "tasks.max"                      = 1
    "schema.ignore"                  = true
    "value.converter.schemas.enable" = false
    }
  }

  resource "aiven_opensearch" "os-service1" {
  project                 = var.project_name
  cloud_name              = "google-northamerica-northeast1"
  plan                    = "business-4"
  service_name            = "os-service1"
  maintenance_window_dow  = "monday"
  maintenance_window_time = "10:00:00"
  opensearch_user_config {
  opensearch_version = "1"
    }
  }

  
  
This file creates three Aiven services - a Kafka service, a Kafka Connect service and an OpenSearch service. A service integration is created between Kafka service and Kafka Connect service. A sink connector is also created between the kafka connect service to the Opensearch service. An additional ``kafka_user``, ``kafka_user_acl``, and ``kafka_topic`` with the defined username and defined permission will also be created from this terraform file. 

More resources
--------------

Keep in mind that some parameters and configurations will vary for your case. A reference to the Aiven for Apache Kafka and Aiven for Apache Kafka Connect connectors are provided below:

- `Configuration options for Aiven for Apache Kafka <https://developer.aiven.io/docs/products/kafka/reference/advanced-params.html>`_
- `List of available Apache Kafka Connect connectors <https://developer.aiven.io/docs/products/kafka/kafka-connect/concepts/list-of-connector-plugins.html>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
