Debezium source connector - PostgreSQL® to Apache Kafka® across clouds
==========================================================

The `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_ is a great choice for provisioning an Aiven for Apache Kafka® cluster with Kafka Connect enabled and the `Debezium source connector for PostgreSQL® <https://developer.aiven.io/docs/products/kafka/kafka-connect/howto/debezium-source-connector-pg.html>`_ configured.

Let's check out the following diagram to understand the setup.

.. mermaid::

   flowchart LR
      id1[(PostgreSQL Database)]
      subgraph Kafka Connect
      Debezium-Source-Connector-PG
      end
      subgraph Apache Kafka
      Topic
      end
      id1 --->|wal2json plugin| Debezium-Source-Connector-PG -->|publishes changes| Topic

Describe the setup
------------------

This terraform recipe will provision one Aiven PostgreSQL database service, one Aiven for Apache Kafka service, a separate Aiven for Apache Kafka Connect 
service with a Debezium source connector for PostgreSQL enabled and configured to connect to the PostgreSQL database and capture any change in tables.
As soon as any of the monitored tables is inserted or updated with new data, the Debezium connector will capture the data change and convert table data into
json payload and produce messages to the relevant Kafka topic. 
Some of these services are created in one cloud provider and some in another cloud provider, to demonstrate how easy it is with Aiven to integrate services across 
multiple cloud vendors.

.. Warning::

    Aiven provides the option to run Kafka Connect on the same nodes as your Kafka cluster, sharing the resources. This is a low-cost way to get started with Kafka Connect but it is not recommended for Production environments, or scenarios where the deployed Connect cluster needs to be in a different cloud provider/region to the Kafka cluster. For these situations, Aiven recommends the use of a dedicated Aiven for Apache Kafka Connect service


.. Tip::

    Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe.
    For example, you'll need to declare the variables for ``project``, ``api_token``.
    These global variables that allow terraform to access the Aiven console and instruct deployments, are normally configured in a separate file called ``secret.tfvars`` and called 
    in the terraform command line using the option ``--var-file=<path/to/tfvars file>``.

The content of the ``secret.tfvars`` file, looks like this:

.. code::

  project = "my-aiven-project"
  aiven_api_token = "<AIVEN_TOKEN>"
  prefix = "anytext"

The ``service.tf`` file for the provisioning of these 3 services and integrations is this:

.. code:: terraform

    terraform {
      required_providers {
        aiven = {
          source  = "aiven/aiven"
          version = ">=3.2.1"
    #      version = ">= 2.0.0, < 3.0.0"
        }
      }
    }

    provider "aiven" {
      api_token = var.aiven_api_token
    }

    data "aiven_project" "prj" {
      project = var.project
    }

    resource "aiven_pg" "demo" {
      project      = var.project
      service_name = "demo-postgres"
      cloud_name   = "google-europe-north1"
      plan         = "business-4"
    }

    resource "aiven_kafka" "kf" {
      project                 = var.project
      cloud_name              = "azure-norway-west"
      plan                    = "startup-2"
    #  service_name            = "${var.prefix}kf"
      service_name            = "kf"
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

    resource "aiven_kafka_connect" "kc" {
      project                 = var.project
      cloud_name              = "google-europe-north1"
      project_vpc_id          = "francesco-demo/01a413b4-36df-4b1b-a697-fd7f87833494"
      plan                    = "startup-4"
    #  service_name            = "${var.prefix}kc"
      service_name            = "kc"
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
      project                  = var.project
      integration_type         = "kafka_connect"
      source_service_name      = aiven_kafka.kf.service_name
      destination_service_name = aiven_kafka_connect.kc.service_name

      kafka_connect_user_config {
        kafka_connect {
          group_id             = "connect"
          status_storage_topic = "__connect_status"
          offset_storage_topic = "__connect_offsets"
        }
      }

      depends_on = [aiven_kafka_connect.kc,aiven_pg.demo]
    }

    resource "aiven_kafka_connector" "cdc-connector" {
      project        = var.project
      service_name   = aiven_kafka_connect.kc.service_name
      connector_name = "kafka-pg-source"

      config = {
        "name"            = "kafka-pg-source"
        "connector.class" = "io.debezium.connector.postgresql.PostgresConnector",
        "snapshot.mode"   = "initial"
        "database.hostname" : aiven_pg.demo.service_host
        "database.port" : aiven_pg.demo.service_port
        "database.password" : aiven_pg.demo.service_password
        "database.user" : aiven_pg.demo.service_username
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
      depends_on = [aiven_service_integration.i1,aiven_kafka_connect.kc,aiven_pg.demo]
    }

Let's see the different resources we are going to create:

- Version 3.2.1 of the Aiven Terraform provider will be used
- The PostgreSQL database will be created in "google-europe-north1" cloud provider with a business-4 plan
- The Aiven Apache Kafka service will be created in "azure-norway-west" cloud and will be preconfigured with a number of properties:
  
  - The ``auto_create_topics_enable = true`` property is crucial as it allows the Debezium connector to create the Kafka topics directly.
  - The ``kafka_connect = false`` property is needed because we want to create a separate Aiven Apache Kafka Connect service.


- One Aiven Apache Kafka Connect service is configured with public access
- Then a service integration is created within Kafka Connect service. This integration will use 2 internal topics for storing status and offset.
- The last Aiven service that will be provisioned is the actual Debezium source connector for PostgreSQL, which is specified by the "connector.class" and is configured with the connection strings to access the PostgreSQL database and listen for all data changes on one or more tables. In our case, it will be "tab1" in "defaultdb", "public" schema. The plugin used is "wal2json" that converts WAL events (WAL stands for Write Ahead Logging) into json payload that is sent to the Kafka topic. The Kafka topic that the Debezium connector creates has the name "replicator.public.tab1", where "replicator" is the logical database used by Debezium connector to monitor for data changes and "public" and "tab1" are the name of the schema and the table name respectively. One important thing to otice is the "depends_on" property that establishes a dependency between the services creation in order to avoid failures.


More resources
--------------

Keep in mind that some parameters and configurations will vary for your case. A reference to some of the advanced Apache Kafka configurations and other related resources:

- `List of advanced Apache Kafka configurations <https://developer.aiven.io/docs/products/kafka/kafka-connect/reference/advanced-params.html>`_
- `Create a Debezium source connector <https://developer.aiven.io/docs/products/kafka/kafka-connect/howto/debezium-source-connector-pg.html>`_
- `List of available Apache Kafka® Connect connectors <https://developer.aiven.io/docs/products/kafka/kafka-connect/concepts/list-of-connector-plugins.html>`_