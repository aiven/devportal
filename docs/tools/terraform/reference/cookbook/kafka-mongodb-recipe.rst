Apache Kafka® with MongoDB Source Connector
===========================================

The `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_ is a great choice for declaratively provisioning an Aiven for Apache Kafka® cluster with Kafka Connect enabled and the `MongoDB source connector <https://developer.aiven.io/docs/products/kafka/kafka-connect/howto/mongodb-poll-source-connector.html>`_ configured.

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

    Creating a `dedicated Aiven for Apache Kafka Connect service <https://developer.aiven.io/docs/products/kafka/kafka-connect/getting-started.html#apache-kafka-connect-dedicated-cluster>`_ is Aiven's suggested option. Having Kafka Connect running on the same nodes as Apache Kafka increases the load on the nodes possibly making the cluster more unstable. 
    
    For a better separation of concerns, a dedicated Aiven for Apache Kafka Connect cluster is therefore suggested.

Before you begin, you will require a MongoDB database and the related database connection information. You'll also need to make sure that the database is reachable from the public internet (unless it's part of a paired VPC).

.. Tip::

    Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe. For example, you'll need to declare the variables for ``project_name``, ``api_token``, ``service_name_prefix``, and ``mongodb_connection_uri``.

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
        auto_create_topics_enable    = true
      }
    }
  }
  
  resource "aiven_kafka_connector" "mongodb-source-connector" {
    project        = var.project_name
    service_name   = aiven_kafka.demo-kafka.service_name
    connector_name = "mongodb-source-connector"
    config = {
      "name" : "mongodb-source-connector"
      "connector.class" : "com.mongodb.kafka.connect.MongoSourceConnector"
      "connection.uri" = var.mongodb_connection_uri
      "database" : "sample_airbnb"
      "collection" : "listingsAndReviews"
      "copy.existing" : "true"
      "poll.await.time.ms" : "1000"
      "output.format.value" : "json"
      "output.format.key" : "json"
      "publish.full.document.only" : "true"
    }
  }

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
