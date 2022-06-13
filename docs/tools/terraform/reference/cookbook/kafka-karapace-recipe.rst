Apache Kafka® with Karapace Schema Registry
===========================================

This example shows how to setup [Karapace](https://github.com/aiven/karapace) - an open source HTTP API interface and schema registry, with Aiven for Apache Kafka using `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_.
You'll also enable the auto creation of Apache Kafka topics which will allow you to send message to topics that didn't exist already on the Apache Kafka cluster. In order to work directly with Kafka by producing and consuming messages over HTTTP, the REST API feature will be enabled. 

.. mermaid::

   flowchart LR
      producer[Producer]
      consumer[Consumer]
      SchemaRegistry{{Schema Registry:<br /> Karapace}}
      producer --> Kafka --> consumer
      producer --> SchemaRegistry --> consumer

Describe the setup
------------------

Here is the sample Terraform file to stand-up a single Apache Kafka server and configure Karapace, Kafka REST, and auto creation of topics.

``services.tf`` file:

.. code:: bash

   resource "aiven_kafka" "demo-kafka" {
     project                 = var.project_name
     cloud_name              = "google-northamerica-northeast1"
     plan                    = "business-4"
     service_name            = "demo-kafka"
     maintenance_window_dow  = "monday"
     maintenance_window_time = "10:00:00"
     kafka_user_config {
       kafka_version = "3.1"
       // Enables Kafka Schemas
       schema_registry = true
       kafka_rest    = true
       kafka {
         group_max_session_timeout_ms = 70000
         log_retention_bytes          = 1000000000
         auto_create_topics_enable = false
       }
     }
   }

   resource "aiven_kafka_topic" "source" {
     project      = var.project_name
     service_name = aiven_kafka.dewan-kafka.service_name
     topic_name   = "topic-a"
     partitions   = 3
     replication  = 2
   }


Let's test that each of these configurations are setup by Terraform. Once the Aiven for Apache Kafka service is running, from the *Overview* tab, ensure that *Apache Kafka REST API (Karapace)* and *Schema Registry (Karapace)* are toggled on.
For documentation on how to use Karapace, refer to the `Karapace GitHub repository <https://github.com/aiven/karapace>`_. 
Without the REST API option enabled, you won't be able to view the topics from the Aiven web console. If you navigate to the *Topics* tab on Aiven console and are able to view the topics, that confirms that the REST API setting has been enabled. 

Finally, you can send messages to a non-existing topic (for example, **topic-b**) on your Apache Kafka cluster and the message will be delivered thanks to the ``auto_create_topics_enable`` parameter being set to **true**.
However, simply removing this parameter won't prevent Apacha Kafka from automatically creating non-existing topics since this is the default behavior. Set ``auto_create_topics_enable`` parameter to **false** and run the ``terraform apply`` again. 
This time, you won't be able to send messages to a non-existing topic.

More resources
--------------

To find more information on Karapace and Apache Kafka:

- `What is Apache Kafka <https://aiven.io/blog/what-is-apache-kafka>`_
- `What is Karapace <https://aiven.io/blog/what-is-karapace>`_
- `Karapace strengthens schema management <https://aiven.io/blog/karapace-strengthens-schema-management>`_

