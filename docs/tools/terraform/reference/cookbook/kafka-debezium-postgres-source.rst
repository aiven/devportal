Debezium source connector - PostgreSQL® to Apache Kafka® across clouds
==========================================================

The `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_ is a great choice for provisioning an Aiven for Apache Kafka® cluster with Kafka Connect enabled and the `Debezium source connector for PostgreSQL® <https://developer.aiven.io/docs/products/kafka/kafka-connect/howto/debezium-source-connector-pg.html>`_ configured.

Let's check out the following diagram to understand the setup.

.. mermaid::

   flowchart LR
      id1[(PostgreSQL service on GCP)]
      subgraph Kafka Connect
      Debezium-Source-Connector-PG
      end
      subgraph Apache Kafka on Azure
      Topic
      end
      id1 --->|wal2json plugin| Debezium-Source-Connector-PG --->|publishes changes| Topic

Describe the setup
------------------

This terraform recipe will provision one Aiven for PostgreSQL database service, one Aiven for Apache Kafka service, and a separate Aiven for Apache Kafka Connect  
service with a Debezium source connector for PostgreSQL enabled and configured to connect to the PostgreSQL database and capture any changes in tables. The Aiven for Apache Kafka service is deployed in the Azure cloud, whereas the PostgreSQL database, like the Aiven for Apache Kafka Connector service, is deployed in the Google Cloud.
Aiven makes it very easy to configure services in different clouds that integrate seamlessly. As soon as any of the monitored tables is inserted or updated with new data, the Debezium connector will capture the data change and convert table data into
JSON payload and produce messages to the relevant Kafka topic. Some of these services are created on one cloud provider and some on another cloud provider, to demonstrate how easy it is with Aiven to integrate services across multiple cloud vendors.

.. Warning::

    Aiven provides the option to run Kafka Connect on the same nodes as your Kafka cluster, sharing the resources. This is a low-cost way to get started with Kafka Connect. A standalone Aiven for Apache Kafka® Connect allows you to scale independently, offers more CPU time and memory for the Kafka Connect service and reduces load on nodes, making the cluster more stable.


.. Tip::

    Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe.
    For example, you'll need to declare the variables for ``project`` and ``api_token``.

The ``services.tf`` file for the provisioning of these three services, service integration, and related resource is this:

.. code:: terraform

    resource "aiven_pg" "demo-pg" {
      project      = var.project_name
      service_name = "demo-postgres"
      cloud_name   = "google-europe-north1"
      plan         = "business-4"
    }

    resource "aiven_kafka" "demo-kafka" {
      project                 = var.project_name
      cloud_name              = "azure-norway-west"
      plan                    = "startup-2"
      service_name            = "demo-kafka"
      maintenance_window_dow  = "saturday"
      maintenance_window_time = "10:00:00"
      kafka_user_config {
        kafka_rest      = true
        kafka_connect   = false
        schema_registry = true
        kafka_version   = "3.1"

        kafka {
          auto_create_topics_enable    = true
          num_partitions               = 3
          default_replication_factor   = 2
          min_insync_replicas          = 2
        }

        kafka_authentication_methods {
          certificate = true
        }

      }
    }

    resource "aiven_kafka_connect" "demo-kafka-connect" {
      project                 = var.project_name
      cloud_name              = "google-europe-north1"
      project_vpc_id          = "proj1-demo/01a413b4-36df-4b1b-a697-fd7f87833494"
      plan                    = "startup-4"
      service_name            = "demo-kafka-connect"
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

    resource "aiven_service_integration" "i1" {
      project                  = var.project_name
      integration_type         = "kafka_connect"
      source_service_name      = aiven_kafka.demo-kafka.service_name
      destination_service_name = aiven_kafka_connect.demo-kafka-connect.service_name

      kafka_connect_user_config {
        kafka_connect {
          group_id             = "connect"
          status_storage_topic = "__connect_status"
          offset_storage_topic = "__connect_offsets"
        }
      }
    }

    resource "aiven_kafka_connector" "kafka-pg-source" {
      project        = var.project_name
      service_name   = aiven_kafka_connect.demo-kafka-connect.service_name
      connector_name = "kafka-pg-source"

      config = {
        "name"            = "kafka-pg-source"
        "connector.class" = "io.debezium.connector.postgresql.PostgresConnector"
        "snapshot.mode"   = "initial"
        "database.hostname" = aiven_pg.demo-pg.service_host
        "database.port" = aiven_pg.demo-pg.service_port
        "database.password" = aiven_pg.demo-pg.service_password
        "database.user" = aiven_pg.demo-pg.service_username
        "database.dbname"           = "defaultdb"
        "database.server.name"      = "replicator"
        "database.ssl.mode"         = "require"
        "include.schema.changes"    = true
        "include.query"             = true
        "table.include.list"        = "public.tab1"
        "plugin.name"               = "wal2json"
        "decimal.handling.mode"     = "double"
        "_aiven.restart.on.failure" = "true"
        "heartbeat.interval.ms"     = 30000
        "heartbeat.action.query"    = "INSERT INTO heartbeat (status) VALUES (1)"
      }
      depends_on = [aiven_service_integration.i1]
    }

.. Warning::

  ``wal2json`` will be deprecated in Debezium 2.0. A future revision of the recipe will use another decoding plug-in like ``pgoutput``.

Let's go over a few of these configurations and understand their functions:

- The ``auto_create_topics_enable = true`` property allows the Debezium connector to send messages to a non-existing topic.
- The ``kafka_connect = false`` property is used because we want to create a separate Aiven for Apache Kafka Connect service.
- The Aiven for Apache Kafka Connect service is configured with ``public_access`` set to TRUE to allow the service to be accessed through a VPC since we are setting up services in different clouds.
- The resource ``aiven_service_integration.i1`` configures the integration between the Aiven for Apache Kafka service and the Aiven for Apache Kafka Connect service. This integration uses two internal topics for storing status and offset.
- ``group_id`` under ``kafka_connect_user_config`` is a unique ID that identifies the Kafka Connect cluster.
- ``status_storage_topic`` and ``offset_storage_topic`` identify the name of the internal Kafka topics that store the connector status and the connector offsets respectively.
- The Debezium source connector for PostgreSQL listens for all data changes on one or more tables, including schema changes. In our case, the table that is monitored for any data change is "tab1" in ``defaultdb`` database under ``public`` schema. The plugin used to capture changes is ``wal2json`` that converts WAL events (WAL stands for Write Ahead Logging) into JSON payload that is sent to the Kafka topic via the Kafka connect service. The Kafka topic that the Debezium connector creates has the name ``replicator.public.tab1``, where "replicator" is the logical database used by Debezium connector to monitor for data changes and "public" and "tab1" are the name of the PostgreSQL schema and table name respectively. 
- The "depends_on" property establishes a dependency between the services creation in order to avoid failures.

More resources
--------------

Keep in mind that some parameters and configurations will vary for your case. A reference to some of the advanced Apache Kafka configurations and other related resources:

- `List of advanced Apache Kafka configurations <https://developer.aiven.io/docs/products/kafka/kafka-connect/reference/advanced-params.html>`_
- `Create a Debezium source connector <https://developer.aiven.io/docs/products/kafka/kafka-connect/howto/debezium-source-connector-pg.html>`_
- `List of available Apache Kafka® Connect connectors <https://developer.aiven.io/docs/products/kafka/kafka-connect/concepts/list-of-connector-plugins.html>`_