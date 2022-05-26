Cross-cluster replication with Apache Kafka® Mirrormaker2
=========================================================

From disaster recovery to isolating data for compliance reasons, businesses need to replicate data across their Apache Kafka® clusters, and Apache Kafka® Mirrormaker2 is a perfect tool 
to do so. A single Mirrormaker2 cluster can run multiple replication flows, and it has a mechanism for preventing replication cycles. This example sets up two Aiven for Apache Kafka clusters (a source and a target),
a Mirrormaker2 service, two service integrations between the Apache Kafka cluster and the Mirrormaker2, and a replication flow for data to move from all the topics from the source cluster to the target cluster. The 
`Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_ is used to create all the required resources declaratively. 

The following image shows a unidirectional flow with the Apache Kafka Mirrormaker2 replicating all the topics from DC1 (source Kafka cluster) to DC2 (target Kafka cluster):

.. mermaid::

   flowchart LR
    
    subgraph DC2
    DC1.TopicA
    DC1.TopicB
    DC1.TopicC
    end
    subgraph MM
    replication-flow-->DC1.TopicA
    replication-flow-->DC1.TopicB
    replication-flow-->DC1.TopicC
    end
    subgraph DC1
    TopicA-->replication-flow
    TopicB-->replication-flow
    TopicC-->replication-flow
    end

Describe the setup
------------------

Here is the sample Terraform file to deploy all the related services. Keep in mind that some parameters and configurations will vary for your case. A reference to some of the advanced Apache Kafka configurations is added at the end of this document.

``services.tf`` file:

.. code:: bash

   resource "aiven_kafka_mirrormaker" "mm" {
    project      = data.aiven_project.kafka-mm-project1.project
    cloud_name   = "google-europe-west1"
    plan         = "startup-4"
    service_name = "mm"

    kafka_mirrormaker_user_config {
      ip_filter = [
        "0.0.0.0/0"
      ]

    kafka_mirrormaker {
      refresh_groups_interval_seconds = 600
      refresh_topics_enabled          = true
      refresh_topics_interval_seconds = 600
    }
   }
  }

  resource "aiven_service_integration" "i1" {
   project                  = data.aiven_project.kafka-mm-project1.project
   integration_type         = "kafka_mirrormaker"
   source_service_name      = aiven_kafka.source.service_name
   destination_service_name = aiven_kafka_mirrormaker.mm.service_name

    kafka_mirrormaker_user_config {
     cluster_alias = "source"
    }
  }

  resource "aiven_service_integration" "i2" {
   project                  = data.aiven_project.kafka-mm-project1.project
   integration_type         = "kafka_mirrormaker"
   source_service_name      = aiven_kafka.target.service_name
   destination_service_name = aiven_kafka_mirrormaker.mm.service_name

    kafka_mirrormaker_user_config {
     cluster_alias = "target"
    }
  }

  resource "aiven_mirrormaker_replication_flow" "f1" {
   project        = data.aiven_project.kafka-mm-project1.project
   service_name   = aiven_kafka_mirrormaker.mm.service_name
   source_cluster = aiven_kafka.source.service_name
   target_cluster = aiven_kafka.target.service_name
   enable         = true

   topics = [
     ".*",
   ]

   topics_blacklist = [
     ".*[\\-\\.]internal",
     ".*\\.replica",
     "__.*"
   ]
  }

  resource "aiven_kafka" "source" {
   project                 = data.aiven_project.kafka-mm-project1.project
   cloud_name              = "google-europe-west1"
   plan                    = "business-4"
   service_name            = "source"
   maintenance_window_dow  = "monday"
   maintenance_window_time = "10:00:00"

   kafka_user_config {
     kafka_version = "3.1"
     kafka {
       group_max_session_timeout_ms = 70000
       log_retention_bytes          = 1000000000
     }
   }
  }

  resource "aiven_kafka_topic" "source" {
   project      = data.aiven_project.kafka-mm-project1.project
   service_name = aiven_kafka.source.service_name
   topic_name   = "topic-a"
   partitions   = 3
   replication  = 2
  }

  resource "aiven_kafka" "target" {
   project                 = data.aiven_project.kafka-mm-project1.project
   cloud_name              = "google-europe-west1"
   plan                    = "business-4"
   service_name            = "target"
   maintenance_window_dow  = "monday"
   maintenance_window_time = "10:00:00"

   kafka_user_config {
     kafka_version = "3.1"
     kafka {
       group_max_session_timeout_ms = 70000
       log_retention_bytes          = 1000000000
     }
    }
  }

  resource "aiven_kafka_topic" "target" {
   project      = data.aiven_project.kafka-mm-project1.project
   service_name = aiven_kafka.target.service_name
   topic_name   = "topic-b"
   partitions   = 3
   replication  = 2
  }

Once you run the Terraform script, an Apache Kafka Mirrormaker2 service is created and configured with two cluster alias pointed to the source and target Apache Kafka clusters. The service 
integrations **i1** and **i2** connect the Kafka clusters to the Mirrormaker2 instance. The replication flow **f1** creates a unidirectional flow to populate the remote topics based on source 
topics. The `".*"` wildcard in the Mirrormaker2 configuration means that all the topics from the source cluster will be replicated to the target cluster. However, since the flow is unidirectional, 
the `topic-b` will only be present in the target cluster and not the source cluster.


More resources
--------------

You might find these related resources useful too:

- `Configuration options for Aiven for Apache Kafka <https://developer.aiven.io/docs/products/kafka/reference/advanced-params.html>`_
- `Aiven for Apache Kafka® Mirrormaker2 Terminology <https://developer.aiven.io/docs/products/kafka/kafka-mirrormaker/reference/terminology.html>`_
- `5 reasons why you should be using MirrorMaker 2.0 for data replication <https://aiven.io/blog/5-reasons-why-you-should-be-using-mirrormaker-2>`_
