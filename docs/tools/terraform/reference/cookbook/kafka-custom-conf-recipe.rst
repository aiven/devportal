Apache Kafka® with custom configurations
========================================

This example deploys an `Aiven for Apache Kafka® <https://aiven.io/kafka>`_ service with some custom configurations, as well as a Kafka topic, a Kafka user, and an access control list (ACL) to allow fine-grained permissions about which topic that user can access, using the `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_.

Before looking at the Terraform script, let's visualize the resources:

.. mermaid::

   flowchart LR
      subgraph Aiven-for-Apache-Kafka
      id4[[Aiven Kafka User]]
      id5[[Aiven Kafka User ACL]]
      end
      Producer --> Aiven-for-Apache-Kafka --> Consumer

Let's cook!
------------

Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe. For example, you'll need to declare the variables for ``project_name``, ``api_token``, and ``kafka_user_name``.

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
   
       variable "kafka_user_name" {
         description = "Username for Aiven for Apache Kafka user"
         type        = string
       } 
    
    3. The ``var-values.tfvars`` file holds the actual values and is passed to Terraform using the ``-var-file=`` flag.

    ``var-values.tfvars`` file:

    .. code:: terraform

       aiven_api_token     = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
       project_name        = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"
       kafka_user_name     = "<A-SAMPLE-USERNAME>"

Here is the sample Terraform script to stand-up Aiven for Apache Kafka and related resources. The script also performs some custom configurations on these resources.

``services.tf`` file:

.. code:: terraform
  
  resource "aiven_kafka" "demo-kafka" {
    project                 = var.project_name
    cloud_name              = "google-europe-west1"
    plan                    = "business-4"
    service_name            = "demo-kafka"
    maintenance_window_dow  = "sunday"
    maintenance_window_time = "01:00:00"
    default_acl             = false
  
    kafka_user_config {
      kafka_rest      = true
      kafka_connect   = false
      schema_registry = true
      kafka_version   = "3.2"
  
      kafka {
        auto_create_topics_enable  = true
        num_partitions             = 3
        default_replication_factor = 2
        min_insync_replicas        = 2
      }
  
      kafka_authentication_methods {
        certificate = true
      }
  
      public_access {
        kafka_rest = true
      }
    }
  }
  
  resource "aiven_kafka_topic" "demo-kafka-topic" {
    project      = var.project_name
    service_name = aiven_kafka.demo-kafka.service_name
    topic_name   = "demo-kafka-topic"
    partitions   = 5
    replication  = 3
  }
  
  resource "aiven_kafka_user" "demo-kafka-user" {
    project      = var.project_name
    service_name = aiven_kafka.demo-kafka.service_name
    username     = var.kafka_user_name
  }
  
  resource "aiven_kafka_acl" "demo-kafka-user-acl" {
    project      = var.project_name
    service_name = aiven_kafka.demo-kafka.service_name
    username     = var.kafka_user_name
    permission   = "read"
    topic        = aiven_kafka_topic.demo-kafka-topic.topic_name
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

Let's go over a few of these configurations and understand their functions:

``aiven_kafka`` resource configurations:

- ``default_acl`` parameter, when set to **true**, creates default wildcard Kafka ACL. This example sets this parameter to **false** and prevents the default wildcard ACL for resources.

- For ``kafka_user_config``, ``schema_registry`` is set to **true**, which enables the `Karapace Schema Registry <https://aiven.io/blog/what-is-karapace>`_ and ``kafka_rest`` allows you to view the messages in the topics from the Aiven web console when set to **true**.

- ``auto_create_topics_enable`` under ``kafka`` nested configurations enables the auto creation of topics when set to **true**. This means that a topic doesn't need to exist before sending a message.

- ``num_partitions`` will set the number of partitions for the automatically created topics.

- By default, the replication factor is 1. This example sets ``default_replication_factor`` to 2 and thus requires a minimum of two brokers. For production environments, a replication factor of 3 is recommended. 

- ``min_insync_replicas`` indicates that at least 2 replicas (brokers) should respond back if all replicas(brokers) are not functioning properly. When all replicas are functioning properly, this setting has no effect. 

- The ``certificate`` parameter under the ``kafka_authentication_methods`` nested configurations, when set to **true**, enables certificate/SSL authentication.

``aiven_kafka_topic`` resource configurations:

- ``partitions`` denotes the number of partitions to create in the topic, and ``replication`` sets the replication factor for the topic.

``aiven_kafka_user`` resource configurations:

- We are passing a preset username using ``var.kafka_user_name``

``aiven_kafka_acl`` resource configurations:

- This ACL allows **read** access to the ``demo-kafka-topic`` topic for the ``var.kafka_user_name`` user. 

.. Warning:: 

  By default, Aiven adds an ``avnadmin`` account to every new service and adds `admin` permission for all topics to that user. When you create your own ACLs to restrict access, you probably want to remove this ACL entry.

.. Note::

  When using the Aiven Terraform Provider, you can add the ``default_acl`` key to your ``resource`` and set it to ``false`` if you do not want to create the admin user with wildcard permissions.

More resources
--------------

Keep in mind that some parameters and configurations will vary for your case. Some related resources are provided below:

- `Configuration options for Aiven for Apache Kafka <https://docs.aiven.io/docs/products/kafka/reference/advanced-params.html>`_
- `Aiven for Apache Kafka access control lists permission mapping <https://docs.aiven.io/docs/products/kafka/concepts/acl.html>`_
- `How to Manage Aiven for Apache Kafka Parameters <https://www.youtube.com/watch?v=pXQZWI0ddLg>`_
- `Set up your first Aiven Terraform project <https://docs.aiven.io/docs/tools/terraform/get-started.html>`_
