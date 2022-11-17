Cross-cluster replication with Apache Kafka® MirrorMaker 2
==========================================================

From disaster recovery to isolating data for compliance reasons, businesses need to replicate data across their Apache Kafka® clusters, and Apache Kafka® MirrorMaker 2 is a perfect tool 
to do so. 

A single MirrorMaker 2 cluster can run multiple replication flows, and it has a mechanism for preventing replication cycles. This example sets up: 

* two Aiven for Apache Kafka clusters (a source and a target)
* an Aiven for Apache Kafka MirrorMaker 2 service
* two service integrations between the Apache Kafka cluster and the MirrorMaker 2
* a replication flow to move all the topics from the source cluster to the target cluster 

The `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_ is used to create all the required resources in a declarative style. The following image shows a unidirectional flow with the Apache Kafka MirrorMaker 2 replicating all the topics from ``DC1`` (source Kafka cluster) to ``DC2`` (target Kafka cluster):

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

Here is the sample Terraform file that will spin up two Apache Kafka services, an Apache Kafka MirrorMaker 2 service and the MirrorMaker 2 service will be configured with two cluster alias pointed to the source and target Apache Kafka clusters. 

The service integrations ``source-kafka-to-mm`` and ``mm-to-target-kafka`` connect the Kafka clusters to the MirrorMaker 2 instance. The replication flow ``mm-replication-flow`` creates a unidirectional flow to populate the remote topics based on source 
topics. 

The ``".*"`` wildcard in the MirrorMaker 2 configuration means that all the topics from the source cluster will be replicated to the target cluster. However, since the flow is unidirectional, the ``topic-b`` will only be present in the target cluster (where it was originally created) and not the source cluster.

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

``services.tf`` file:

.. code:: terraform
  
  resource "aiven_kafka_mirrormaker" "mm" {
    project      = var.project_name
    cloud_name   = "google-europe-west1"
    plan         = "business-4"
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
  
  resource "aiven_service_integration" "source-kafka-to-mm" {
    project                  = var.project_name
    integration_type         = "kafka_mirrormaker"
    source_service_name      = aiven_kafka.source.service_name
    destination_service_name = aiven_kafka_mirrormaker.mm.service_name
  
    kafka_mirrormaker_user_config {
      cluster_alias = "source"
    }
  }
  
  resource "aiven_service_integration" "mm-to-target-kafka" {
    project                  = var.project_name
    integration_type         = "kafka_mirrormaker"
    source_service_name      = aiven_kafka.target.service_name
    destination_service_name = aiven_kafka_mirrormaker.mm.service_name
  
    kafka_mirrormaker_user_config {
      cluster_alias = "target"
    }
  }
  
  resource "aiven_mirrormaker_replication_flow" "mm-replication-flow" {
    project        = var.project_name
    service_name   = aiven_kafka_mirrormaker.mm.service_name
    source_cluster = aiven_service_integration.source-kafka-to-mm.kafka_mirrormaker_user_config[0].cluster_alias
    target_cluster = aiven_service_integration.mm-to-target-kafka.kafka_mirrormaker_user_config[0].cluster_alias
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
    project                 = var.project_name
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
    project      = var.project_name
    service_name = aiven_kafka.source.service_name
    topic_name   = "topic-a"
    partitions   = 3
    replication  = 2
  }
  
  resource "aiven_kafka" "target" {
    project                 = var.project_name
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
    project      = var.project_name
    service_name = aiven_kafka.target.service_name
    topic_name   = "topic-b"
    partitions   = 3
    replication  = 2
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

For Apache Kafka MirrorMaker 2 and Apache Kafka service integration, ``ip_filter`` is a specific configuration that whitelists certain ranges of IP addresses. This example of ``0.0.0.0/0`` denotes that all IP addresses are allowed.

.. Tip::

  In the target Apache Kafka cluster you will find: 
  
  * the topic named ``topic-b`` created via the resource ``"aiven_kafka_topic" "target"``
  * some internal MirrorMaker 2 topics starting with prefix ``mm2``
  * a heartbeat topic for the ``source`` Kafka cluster named ``source.heartbeats``
  * the replicated topic ``topic-a`` prefixed with the source Kafka cluster alias ``source``

More resources
--------------

Keep in mind that some parameters and configurations will vary for your case. A reference to some of the advanced Apache Kafka configurations and other related resources:

- `Configuration options for Aiven for Apache Kafka <https://docs.aiven.io/docs/products/kafka/reference/advanced-params.html>`_
- `Aiven for Apache Kafka® MirrorMaker 2 Terminology <https://docs.aiven.io/docs/products/kafka/kafka-mirrormaker/reference/terminology.html>`_
- `5 reasons why you should be using MirrorMaker 2.0 for data replication <https://aiven.io/blog/5-reasons-why-you-should-be-using-mirrormaker-2>`_
