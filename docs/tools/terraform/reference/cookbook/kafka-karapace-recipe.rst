Apache Kafka® with Karapace Schema Registry
===========================================

This example shows how to setup `Karapace <https://github.com/aiven/karapace>`_ - an open source HTTP API interface and schema registry, with Aiven for Apache Kafka® using `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_.

You'll also enable the auto creation of Apache Kafka topics which will allow you to send message to topics that didn't exist already on the Apache Kafka cluster. In order to work directly with Kafka by producing and consuming messages over HTTP, the REST API feature will be enabled.
To learn more, check out `Create Apache Kafka® topics automatically <https://developer.aiven.io/docs/products/kafka/howto/create-topics-automatically.html>`_ page.  

.. mermaid::

   flowchart LR
      producer[Producer]
      consumer[Consumer]
      SchemaRegistry{{Schema Registry:<br /> Karapace}}
      producer --> Kafka --> consumer
      producer --> SchemaRegistry --> consumer

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

Here is the sample Terraform file to stand-up a single Apache Kafka server and configure Karapace, Kafka REST, and auto creation of topics.

``services.tf`` file:

.. code:: terraform
   
   resource "aiven_kafka" "demo-kafka" {
     project                 = var.project_name
     cloud_name              = "google-northamerica-northeast1"
     plan                    = "business-4"
     service_name            = "demo-kafka"
     maintenance_window_dow  = "monday"
     maintenance_window_time = "10:00:00"
     kafka_user_config {
       kafka_version = "3.1"
       // Enables Karapace Schema Registry and REST
       schema_registry = true
       kafka_rest      = true
       kafka {
         auto_create_topics_enable = true
       }
     }
   }
   
   resource "aiven_kafka_topic" "source" {
     project      = var.project_name
     service_name = aiven_kafka.demo-kafka.service_name
     topic_name   = "topic-a"
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
   
Let's test that each of these configurations are setup by Terraform. Once the Aiven for Apache Kafka service is running, from the *Overview* tab, ensure that *Apache Kafka REST API (Karapace)* and *Schema Registry (Karapace)* are toggled on.
For documentation on how to use Karapace, refer to the `Karapace GitHub repository <https://github.com/aiven/karapace>`_. 
Without the REST API option enabled, you won't be able to view the messages in the topics from the Aiven web console. If you navigate to the *Topics* tab on Aiven console and are able to browse the messages for a particular topic (the *Messages* button is enabled), that confirms that the REST API setting has been enabled. 

Finally, you can send messages to a non-existing topic (for example, ``topic-b``) on your Apache Kafka cluster and the message will be delivered thanks to the ``auto_create_topics_enable`` parameter being set to ``true``.
By default, in Aiven for Apache Kafka this features is turned off as safeguard against accidental topic creation. Either remove this parameter from the Terraform code or set ``auto_create_topics_enable`` parameter to ``false`` and run the ``terraform apply`` again. 
This time, you won't be able to send messages to a non-existing topic.

More resources
--------------

To find more information on Karapace and Apache Kafka:

- `What is Apache Kafka <https://aiven.io/blog/what-is-apache-kafka>`_
- `What is Karapace <https://aiven.io/blog/what-is-karapace>`_
- `Karapace strengthens schema management <https://aiven.io/blog/karapace-strengthens-schema-management>`_

