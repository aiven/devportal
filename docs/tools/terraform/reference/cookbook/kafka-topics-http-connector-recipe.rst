Configure Apache Kafka® with topics and an HTTP sink connector using Terraform
==============================================================================

This article shows the Terraform configuration for setting up an Aiven for
Apache Kafka®, configuring a topic, and adding a Kafka Connector to send the
data from the topic over HTTP using the :doc:`HTTP sink connector
</docs/products/kafka/kafka-connect/howto/http-sink>`. This is a great way to
use webhooks or HTTP requests as a generic connector to send the data to
another platform.

The setup needs the Aiven for Apache Kafka service and the Kafka Connect
service, plus a service integration to connect the two. The overall setup looks
something like the diagram below:


.. mermaid::

    flowchart LR
        subgraph k1 [Kafka cluster]
        topic[Topic]
        end
        sikafka{{Service Integration}}
        subgraph kc1 [Kafka Connect]
        connector[HTTP sink connector]
        end
        webhook([HTTP destination])
        topic-->sikafka-->connector-->webhook

The Aiven for Apache Kafka and Kafka Connect services are connected with a
service integration. The Kafka Connect service has the HTTP sink configured and
this connects the topic to the HTTP destination. The HTTP destination is an
external location defined by `http.url` in the HTTP sink connector
configuration.

Define the setup
----------------

Be sure to check out the :doc:`getting started guide <../../get-started>` to
learn about the common files required to execute the following recipe. For
example, you'll need to declare the variables for ``project_name`` and
``api_token``.

.. dropdown:: Expand to see the common files needed for this recipe.

    Navigate to a new folder and add the following files.

    1. Add the following to a new ``provider.tf`` file:

    .. code:: terraform

       terraform {
         required_providers {
           aiven = {
             source  = "aiven/aiven"
             version = "~> 3.9.0"
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



The sample Terraform file to create and connect all the services is shown
below. This file uses sample data; comments are added to indicate settings that
are likely to need changing to suit your use case.

``services.tf`` file:

.. code:: terraform
    
    # Kafka service
    resource "aiven_kafka" "project_kafka" {
      project                 = var.project_name # from variables.tf and supplied at run time
      cloud_name              = "google-europe-west1"
      plan                    = "business-4"
      service_name            = "my-kafka-demo"
      kafka_user_config {
        kafka_version = "3.2"
        kafka_rest      = true
        kafka {
          auto_create_topics_enable = true
        }
      }
    }

    # Kafka topic, in the cluster defined above
    resource "aiven_kafka_topic" "user_activity" {
      project      = var.project_name
      service_name = aiven_kafka.project_kafka.service_name
      topic_name   = "user_activity"
      partitions   = 3
      replication  = 2
    }

    # Kafka Connect service
    resource "aiven_kafka_connect" "data_connector" {
      project                 = var.project_name
      cloud_name              = "google-europe-west1"
      plan                    = "business-4"
      service_name            = "my-kafka-demo-connector"
    }

    # Integration between kafka and kafka connect
    resource "aiven_service_integration" "kafka_to_data_connector" {
      project                  = var.project_name
      integration_type         = "kafka_connect"
      source_service_name      = aiven_kafka.project_kafka.service_name
      destination_service_name = aiven_kafka_connect.data_connector.service_name
    }

    # Kafka connector: this one is an HTTP sink
    resource "aiven_kafka_connector" "kafka_webhook_sink" {
      project        = var.project_name
      service_name   = aiven_kafka_connect.data_connector.service_name
      connector_name = "my-http-sink"
      config = {
        # Which topic (or topics) should the data come from?
        "topics"                         = aiven_kafka_topic.user_activity.topic_name
        "connector.class"                = "io.aiven.kafka.connect.http.HttpSinkConnector"
        "name"                           = "my-http-sink"
        # Edit where the HTTP data should be sent
        "http.url"                       = "https://example.com/endpoint"
        "http.authorization.type"        = "none"
        "http.headers.content.type"      = "application/json"
        "key.converter"                  = "org.apache.kafka.connect.storage.StringConverter"
        "value.converter"                = "org.apache.kafka.connect.storage.StringConverter"
      }

      # Make sure that the connect service is ready before creating this
      depends_on = [
        aiven_kafka_connect.data_connector,
        aiven_service_integration.kafka_to_data_connector
      ]
    }

This example creates two Aiven services: one Aiven for Apache Kafka service,
and a Kafka Connect service. It adds a service integration so that the the
connectors can access the data in the Kafka cluster. There is a topic defined
`user_activity`, and this is referred to by the Kafka connector configuration
as the source of the data to send over HTTP. The connector also defines where
the HTTP requests should be sent to, using the `http.url` setting.

To avoid any race conditions in this setup, the `depends_on` clause makes sure
that the connector will only be configured when both the Kafka Connect service
and its integration to Kafka are in place.

Go ahead and plan and then apply the Terraform configuration.

.. dropdown:: Expand for how to execute the Terraform files

    The ``init`` command performs several different initialization steps in order to prepare the current working directory for use with Terraform. In our case, this command automatically finds, downloads, and installs the necessary Aiven Terraform provider plugins.
    
    .. code:: shell

       terraform init

    The ``plan`` command creates an execution plan and shows you the resources that will be created (or modified) for you. This command does not actually create any resource; this is more like a preview.

    .. code:: bash

       terraform plan -var-file=var-values.tfvars

    If you're satisfied with the output of ``terraform plan``, go ahead and run the ``terraform apply`` command which actually does the task or creating (or modifying) your infrastructure resources. 

    .. code:: bash

       terraform apply -var-file=var-values.tfvars
           
Try out this recipe by defining an HTTP endpoint where you can receive and
acknowledge HTTP requests in the connector configuration. Then produce some
data to the `user_activity` topic (any JSON data is fine), and observe that
this is then sent over HTTP.

You could use this setup for relaying payloads to platforms that don't have specific connectors available. The HTTP sink connector is also an excellent tool for integrating with webhook-ready platforms like functions-as-a-service ([Amazon Lambda](https://aws.amazon.com/lambda/), [Cloudflare Workers](https://workers.cloudflare.com/)) or [Zapier](https://zapier.com/).


Further resources
-----------------

Here are some resources with additional information, examples and documentation for working with the technologies in this recipe:

- :doc:`Configuration options for Kafka </docs/products/kafka/reference/advanced-params>`
- :doc:`HTTP sink documentation and examples </docs/products/kafka/kafka-connect/howto/http-sink>`
