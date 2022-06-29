Connect Apache Kafka® to Google Cloud Storage with Terraform
============================================================

This example shows how to use a Kafka® Connector to take data from Apache Kafka® and ingest it into Google Cloud Storage® using `Apache Kafka Connect <https://developer.aiven.io/docs/products/kafka/kafka-connect/index.html>`_. As a use case, the data here is application logs going onto a Kafka topic, and being put into Google Cloud Storage for short term storage and easy inspection, if needed.
Aiven has a concept of service integrations to manage the relationships between components. `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_
has a specific resource type in Terraform for service integration. 

Before looking at the Terraform script, let's visually realize how the services will be connected:

.. mermaid::

   flowchart LR
      kafka[Kafka]
      sikafka{{Service Integration}}
      kconn[Kafka Connect]
      kcgcs{{Kafka Connector:<br /> GCS Sink}}
      gcs[GCS]
      kafka --> sikafka --> kconn --> kcgcs --> gcs

In the above diagram, *KafkaConnect* is the service that you create for connecting Kafka with external systems. The Kafka Connectors, *GCS Sink Connector* for example, are ready-to-use components to send/receive data to common data sources/sinks. 

Describe the setup
------------------

Here is the sample Terraform file to stand-up and connect all the services. Keep in mind that some parameters and configurations will vary for your case. A reference to the Kafka and GCS configurations are added at the end of this document.

``services.tf`` file:

.. code:: terraform

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
      project      = var.project_name
      service_name = aiven_kafka.application-logs.service_name
      topic_name   = "logs-app-1"
      partitions   = 3
      replication  = 2
    }
    
    # Kafka connect service
    resource "aiven_kafka_connect" "logs-connector" {
      project                 = var.project_name
      cloud_name              = "google-northamerica-northeast1"
      plan                    = "business-4"
      service_name            = "kafka-connect-logs-connector"
      maintenance_window_dow  = "monday"
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
      project                  = var.project_name
      integration_type         = "kafka_connect"
      source_service_name      = aiven_kafka.application-logs.service_name
      destination_service_name = aiven_kafka_connect.logs-connector.service_name
      kafka_connect_user_config {
        kafka_connect {
          group_id             = "connect"
          status_storage_topic = "__connect_status"
          offset_storage_topic = "__connect_offsets"
        }
      }
    }
    
    # Kafka connector
    resource "aiven_kafka_connector" "kafka-gcs-con1" {
      project        = var.project_name
      service_name   = aiven_kafka.kafka1.service_name
      connector_name = "gcs-connector"
      config = {
        "value.converter"= "org.apache.kafka.connect.json.JsonConverter"
        "file.name.prefix"= "my-custom-prefix/"
        "topics"= "logs-app-1"
        "tasks.max"= "1"
        "file.max.records"= "1"
        "name"= "gcs-connector"
        "format.output.fields"= "value,offset"
        "format.output.type"= "jsonl"
        "key.converter"= "org.apache.kafka.connect.storage.StringConverter"
        "gcs.credentials.json"= var.gcs_credentials
        "file.compression.type"= "gzip"
        "connector.class"= "io.aiven.kafka.connect.gcs.GcsSinkConnector"
        "gcs.bucket.name"= "the-bucket-list"
        "value.converter.schemas.enable"= "false"
        "key.converter.schemas.enable"= "false"
        }
    }
    
    
This file creates two Aiven services - a Kafka service and a Kafka Connect service. 
A service integration is created between the above two services and a Kafka topic is also created from this Terraform file.
To validate, produce some messages on the Kafka topic and you should be seeing those appear on GCS indices.
  

More resources
--------------

You might find these related resources useful too:

- `Configuration options for Kafka <https://developer.aiven.io/docs/products/kafka/reference/advanced-params.html>`_
- `Configuration options for GCS Sink <https://developer.aiven.io/docs/products/kafka/kafka-connect/howto/gcs-sink.html>`_

