Apache Kafka® with MongoDB source connector
===========================================

The `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_ is a great choice for provisioning an Aiven for Apache Kafka® cluster with Kafka Connect enabled and the `MongoDB source connector <https://developer.aiven.io/docs/products/kafka/kafka-connect/howto/mongodb-poll-source-connector.html>`_ configured.

Let's check out the following diagram to understand the setup.

.. mermaid::

   flowchart LR
      id1[(MongoDB Database)]
      subgraph Kafka Connect
      MongoDB-Source-Connector
      end
      subgraph Apache Kafka
      Topic
      end
      id1 --->|polls changes| MongoDB-Source-Connector -->|publishes changes| Topic

Describe the setup
------------------

Here is the Terraform recipe that will spin up an Aiven for Apache Kafka service with Kafka Connect enabled. This recipe will also create and configure a MongoDB source connector. 

.. Warning::

    Aiven provides the option to run Kafka Connect on the same nodes as your Kafka cluster, sharing the resources. This is a low-cost way to get started with Kafka Connect. A standalone Aiven for Apache Kafka® Connect allows you to scale independently, offers more CPU time and memory for the Kafka Connect service and reduces load on nodes, making the cluster more stable.

Before you begin, you will require a MongoDB database and the related database connection information. You'll also need to make sure that the database is reachable from the public internet (unless it's part of a paired VPC).

Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe. For example, you'll need to declare the variables for ``project_name``, ``api_token``, ``service_name_prefix``, and ``mongodb_connection_uri``.

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

       variable "service_name_prefix" {
         description = "A string to prepend to the service name"
         type        = string
       }

       variable "mongodb_connection_uri" {
         description = "MongoDB connection URI used to connect to your MongoDB deployment"
         type        = string
       }

    3. The ``var-values.tfvars`` file holds the actual values and is passed to Terraform using the ``-var-file=`` flag.

    ``var-values.tfvars`` file:

    .. code:: terraform

       aiven_api_token        = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
       project_name           = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"
       service_name_prefix    = "<YOUR-CHOICE-OF-A-SERVICE-NAME-PREFIX>" 
       mongodb_connection_uri = "<YOUR-MONGODB-SERVICE-CONNECTION-URI>"

``services.tf`` file:

.. code:: terraform
  
  resource "aiven_kafka" "demo-kafka" {
    project                 = var.project_name
    cloud_name              = "google-northamerica-northeast1"
    plan                    = "business-4"
    service_name            = join("-", [var.service_name_prefix, "kafka"])
    maintenance_window_dow  = "sunday"
    maintenance_window_time = "10:00:00"
    kafka_user_config {
      kafka_connect = true
      kafka_rest    = true
      kafka_version = "3.1"
      kafka {
        auto_create_topics_enable = true
      }
    }
  }
  
  resource "aiven_kafka_connector" "mongodb-source-connector" {
    project        = var.project_name
    service_name   = aiven_kafka.demo-kafka.service_name
    connector_name = "mongodb-source-connector"
    config = {
      "name"                       = "mongodb-source-connector"
      "connector.class"            = "com.mongodb.kafka.connect.MongoSourceConnector"
      "connection.uri"             = var.mongodb_connection_uri
      "database"                   = "sample_airbnb"
      "collection"                 = "listingsAndReviews"
      "copy.existing"              = "true"
      "poll.await.time.ms"         = "1000"
      "output.format.value"        = "json"
      "output.format.key"          = "json"
      "publish.full.document.only" = "true"
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

- Since you have ``kafka_connect`` set to ``true`` under the ``kafka_user_config``, you don't need a standalone Aiven for Apache Kafka Connect service.
- The ``auto_create_topics_enable`` flag is enabled, therefore the connector is able to create the topic on the Apache Kafka cluster by pushing the first message, without having to create the topic first.
- The automatically created topic name will be the concatenation of ``database`` and ``collection`` parameters - ``sample_airbnb.listingsAndReviews`` in this example.
- ``poll.await.time.ms`` can be configured to set the amount of wait time before the MongoDB source connector pulls the new changes from a collection.
- ``publish.full.document.only``, when set to ``true``, only publishes the actual document rather than the full change stream document. The default value of the parameter is ``false``.

More resources
--------------

Keep in mind that some parameters and configurations will vary for your case. A reference to some of the advanced Apache Kafka configurations and other related resources:

- `List of advanced Apache Kafka configurations <https://developer.aiven.io/docs/products/kafka/kafka-connect/reference/advanced-params.html>`_
- `Create a MongoDB source connector <https://developer.aiven.io/docs/products/kafka/kafka-connect/howto/mongodb-poll-source-connector.html>`_
- `List of available Apache Kafka® Connect connectors <https://developer.aiven.io/docs/products/kafka/kafka-connect/concepts/list-of-connector-plugins.html>`_
