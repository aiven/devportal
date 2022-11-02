Connect Apache Kafka® to OpenSearch® with Terraform
===================================================

This example shows how to use a Kafka® Connector to take data from Apache Kafka® and ingest it into OpenSearch® using :doc:`Apache Kafka Connect </docs/products/kafka/kafka-connect>`. As a use case, the data here is application logs going onto a Kafka topic, and being put into OpenSearch for short term storage and easy inspection, if needed.
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
------------------

Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe. For example, you'll need to declare the variables for ``project_name`` and ``api_token``.

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

Here is the sample Terraform file to stand-up and connect all the services. Keep in mind that some parameters and configurations will vary for your case. A reference to the Kafka and OpenSearch configurations are added at the end of this document.

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
    resource "aiven_kafka_connector" "kafka-os-con1" {
      project        = var.project_name
      service_name   = aiven_kafka.application-logs.service_name
      connector_name = "kafka-os-con1"
      config = {
        "topics" = aiven_kafka_topic.topic-logs-app-1.topic_name
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
    
    # Opensearch service
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
           
This file creates three Aiven services - a Kafka service, a Kafka Connect service, and an OpenSearch service. Two service integrations among these three services and a Kafka topic within the Kafka service will also be created from this Terraform file.
To validate, produce some messages on the Kafka topic and you should be seeing those appear on OpenSearch indices.

More resources
--------------

You might find these related resources useful too:

- `Configuration options for Kafka <https://developer.aiven.io/docs/products/kafka/reference/advanced-params.html>`_
- `Configuration options for OpenSearch <https://developer.aiven.io/docs/products/opensearch/reference/advanced-params.html>`_

