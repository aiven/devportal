Connect Apache Kafka® to OpenSearch with Terraform
==========================================================

This example shows how to use a Kafka Connector to take data from Apache Kafka and ingest it into OpenSearch using `Apache Kafka Connect <https://developer.aiven.io/docs/products/kafka/kafka-connect/index.html>`_. As a use case, the data here is application logs going onto a Kafka topic, and being put into OpenSearch for short term storage and easy inspection, if needed.
Aiven has a concept of service integrations to manage the relationships between components. `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_
has a specific resource type in Terraform for service integration. 

Before looking at the Terraform script, let's visually realize how the services will be connected:

.. mermaid::

   flowchart LR
      kafka[Kafka]
      sikafka{{Service Integration}}
      kconn[Kafka Connect]
      kcopensearch{{Kafka Connector:<br /> OpenSearch Sink}}
      opensearch[OpenSearch]
      kafka --> sikafka --> kconn --> kcopensearch --> opensearch

In the above diagram, *KafkaConnect* is the service that you create for connecting Kafka with external systems. The Kafka Connectors, *OpenSearch Sink Connector* for example, are ready-to-use components to send/receive data to common data sources/sinks. 

Describe the setup
==================

Here is the sample Terraform file to stand-up and connect all the services. Keep in mind that some parameters and configurations will vary for your case. A reference to the Kafka and OpenSearch configurations are added at the end of this document.

``services.tf`` file:

.. code:: bash

   # Kafka service
   resource "aiven_kafka" "application-logs" {
   project                 = var.project_name
   cloud_name              = "google-northamerica-northeast1"
   plan                    = "business-4"
   service_name            = "kafka-application-logs"
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

   # Kafka topic
   resource "aiven_kafka_topic" "topic-logs-app-1" {
   project = var.project_name
   service_name = aiven_kafka.application-logs.service_name
   topic_name = "logs-app-1"
   partitions = 3
   replication = 2
   }

   # Kafka connect service
   resource "aiven_kafka_connect" "logs-connector" {
   project = var.project_name
   cloud_name = "google-northamerica-northeast1"
   plan = "business-4"
   service_name = "kafka-connect-logs-connector"
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
   resource "aiven_service_integration" "kafka-to-logs-connector" {
   project = var.project_name
   integration_type = "kafka_connect"
   source_service_name = aiven_kafka.application-logs.service_name
   destination_service_name = aiven_kafka_connect.logs-connector.service_name
   kafka_connect_user_config {
      kafka_connect {
         group_id = "connect"
         status_storage_topic = "__connect_status"
         offset_storage_topic = "__connect_offsets"
      }
   }
   }

   # Kafka connector
   resource "aiven_kafka_connector" "kafka-os-con1" {
   project = var.project_name
   service_name = aiven_kafka.application-logs.service_name
   connector_name = "kafka-os-con1"
   config = {
      "topics" = aiven_kafka_topic.topic-logs-app-1.topic_name
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

This file creates three Aiven services - a Kafka service, a Kafka Connect service, and an OpenSearch service. Two service integrations among these three services and a Kafka topic within the Kafka service will also be created from this Terraform file.
To validate, produce some messages on the Kafka topic and you should be seeing those appear on OpenSearch indices.

More resources
==============

You might find these related resources useful too:

- `Configuration options for Kafka <https://developer.aiven.io/docs/products/kafka/reference/advanced-params.html>`_
- `Configuration options for OpenSearch <https://developer.aiven.io/docs/products/opensearch/reference/advanced-params.html>`_

If you liked this recipe, try out some of the other recipes within the Aiven Terraform cookbook. 
