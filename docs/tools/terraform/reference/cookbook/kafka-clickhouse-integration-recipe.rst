Apache Kafka® as source for Aiven for ClickHouse®
=================================================

This article shows by way of example how to integrate Aiven for Apache Kafka® with Aiven for ClickHouse® using `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_.

An Apache Kafka® source topic is used as a data source and Aiven for ClickHouse® can process the data to do filtering or transformation with a materialized view before writing it to a regular table.

Let's cook!
-----------

Imagine that you are collecting CPU usage for hundreds of machines in your data centre and these metrics are populated in an Apache Kafka topic called ``cpu_measurements``. But you're interested in learning about those machines with CPU usages higher than 85%.

For this, you'd like to setup a Aiven ClickHouse database and write the filtered messages into a table called ``cpu_high_usage``. The following Terraform script initializes up both Apache Kafka and Aiven ClickHouse services, creates the service integration, the source Apache Kafka topic and an Aiven ClickHouse database.

.. dropdown:: Expand to check out the relevant common files needed for this recipe.

    Navigate to a new folder and add the following files.

    1. Add the following to a new ``provider.tf`` file:

    .. code:: terraform

       terraform {
	 required_providers {
	   aiven = {
	     source  = "aiven/aiven"
	     version = ">= 3.8"
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

``services.tf`` file
''''''''''''''''''''

.. code:: terraform

  resource "aiven_kafka" "kafka" {
    project                 = var.project_name
    cloud_name              = "google-europe-west1"
    plan                    = "business-4"
    service_name            = "kafka-gcp-eu"
    maintenance_window_dow  = "monday"
    maintenance_window_time = "10:00:00"
  }

  resource "aiven_kafka_topic" "source" {
    project      = var.project_name
    service_name = aiven_kafka.kafka.service_name
    partitions   = 2
    replication  = 3
    topic_name   = "iot_measurements"
  }

  resource "aiven_clickhouse" "clickhouse" {
    project                 = var.project_name
    cloud_name              = "google-europe-west1"
    plan                    = "startup-4"
    service_name            = "clickhouse-gcp-eu"
    maintenance_window_dow  = "monday"
    maintenance_window_time = "10:00:00"
  }

  resource "aiven_service_integration" "clickhouse_kafka_source" {
    project                  = var.project_name
    integration_type         = "clickhouse_kafka"
    source_service_name      = aiven_kafka.kafka.service_name
    destination_service_name = aiven_clickhouse.clickhouse.service_name
  }

  resource "aiven_clickhouse_database" "measurements" {
    project                 = var.project_name
    service_name            = aiven_clickhouse.clickhouse.service_name
    name                    = "measurements"
  }

  resource "aiven_clickhouse_user" "ch-user" {
    project      = var.project_name
    service_name = aiven_clickhouse.clickhouse.service_name
    username     = "etl"
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

Results
'''''''

The resource ``"aiven_clickhouse"`` creates an Aiven ClickHouse resource with the project name, choice of cloud, an Aiven service plan, and a specified service name. The ``"aiven_clickhouse_database"`` resources creates a database which can be used to write raw kafka messages and create new tables and view processing them.
``"aiven_kafka"`` resource creates an Apache Kafka cluster and a Apache Kafka topic ``iot_measurements`` is created using the ``"aiven_kafka_topic"`` resource.
Similarly, the ``"aiven_service_integration"`` resource creates the integration between Apache Kafka and the Aiven ClickHouse service.

More resources
--------------

The parameters and configurations will vary for your case. Please refer below for Apache Kafka and Aiven ClickHouse advanced parameters, a related blog, and how to get started with Aiven Terraform Provider:

- `Set up your first Aiven Terraform project <https://docs.aiven.io/docs/tools/terraform/get-started.html>`_

Follow up
---------

* Now you can proceed to `creating databases and tables <https://docs.aiven.io/docs/products/clickhouse/howto/integrate-kafka.html#update-apache-kafka-integration-settings>`_ so that you can `read and store your data <https://docs.aiven.io/docs/products/clickhouse/howto/integrate-kafka.html#read-and-store-data>`_.
* You can also `create a materialized view <https://docs.aiven.io/docs/products/clickhouse/howto/materialized-views.html>`_ to store the Kafka® messages in Aiven for ClickHouse.
