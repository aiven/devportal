PostgreSQL® as source for Aiven for ClickHouse®
===============================================

This article shows by way of example how to integrate PostgreSQL® with Aiven for ClickHouse® using `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_.

A PostgreSQL database is used as a data source and Aiven for ClickHouse can be used to read, transform, and execute jobs using data from the PostgreSQL server.

Let's cook!
-----------

Imagine that you are collecting IoT measurements from thousands of sensors and these metrics are stored in ClickHouse table ``iot_measurements``.

You may want to enrich the measurements using the sensor's location found in the ``sensors_dim`` table in PostgreSQL and filter by city names.

For this, you'd like to set up an Aiven for ClickHouse database and insert your measurements data. Then, you'd like to
join it with the related PostgreSQL dimension tables. The following Terraform script initializes both PostgreSQL
and Aiven for ClickHouse services, creates the service integration, the source PostgreSQL table and the Aiven for ClickHouse database.

Configure common files
''''''''''''''''''''''

.. dropdown:: Expand to check out the relevant common files needed for this recipe.

    Navigate to a new folder and add the following files.

    1. Add the following to a new ``provider.tf`` file:

    .. code-block:: terraform

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

    .. code-block:: terraform

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

    .. code-block:: terraform

       aiven_api_token     = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
       project_name        = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"

Configure the ``services.tf`` file
''''''''''''''''''''''''''''''''''

.. code-block:: terraform


  // Postgres service based in GCP US East
  resource "aiven_pg" "postgres" {
    project                 = var.project_name
    service_name            = "postgres-gcp-us"
    cloud_name              = "google-us-east-4"
    plan                    = "business-8" // Primary + read replica
    maintenance_window_dow  = "monday"
    maintenance_window_time = "10:00:00"
  }

  // Postgres sensors database
  resource "aiven_pg_database" "mydatabase" {
    project       = var.project_name
    service_name  = aiven_pg.postgres.service_name
    database_name = "sensors"
  }

  // ClickHouse service based in the same region
  resource "aiven_clickhouse" "clickhouse" {
    project                 = var.project_name
    service_name            = "clickhouse-gcp-us"
    cloud_name              = "google-us-east-4"
    plan                    = "startup-4"
    maintenance_window_dow  = "monday"
    maintenance_window_time = "10:00:00"
  }

  // Sample ClickHouse database that can be used to write and process raw data
  resource "aiven_clickhouse_database" "iot_measurements" {
    project      = var.project_name
    service_name = aiven_clickhouse.clickhouse.service_name
    name         = "iot_measurements"
  }

  // ClickHouse service integration for the PostgreSQL service as source
  resource "aiven_service_integration" "clickhouse_postgres_source" {
    project                  = var.project_name
    integration_type         = "clickhouse_postgresql"
    source_service_name      = aiven_pg.postgres.service_name
    destination_service_name = aiven_clickhouse.clickhouse.service_name
  }

Execute the Terraform files
'''''''''''''''''''''''''''

.. dropdown:: Expand to check out how to execute the Terraform files.

    The ``init`` command performs several different initialization steps in order to prepare the current working directory for use with Terraform. In our case, this command automatically finds, downloads, and installs the necessary Aiven Terraform provider plugins.

    .. code-block:: shell

       terraform init

    The ``plan`` command creates an execution plan and shows you the resources that will be created (or modified) for you. This command does not actually create any resource; this is more like a preview.

    .. code-block:: shell

       terraform plan -var-file=var-values.tfvars

    If you're satisfied with the output of ``terraform plan``, go ahead and run the ``terraform apply`` command which actually does the task or creating (or modifying) your infrastructure resources.

    .. code-block:: shell

       terraform apply -var-file=var-values.tfvars

Check out the results
---------------------

The resource ``"aiven_clickhouse"`` creates an Aiven for ClickHouse resource with the project name, choice of a cloud provider, an Aiven service plan, and a specified service name. The ``"aiven_clickhouse_database"`` resources creates a database which can be used to write high-thoughput measurement data, create new tables and views to process them.
The ``"aiven_pg"`` resource creates an PostgreSQL service and a database ``sensors`` is created using the ``"aiven_pg_database"`` resource.
The ``"aiven_service_integration"`` resource creates the integration between PostgreSQL and the Aiven for ClickHouse service.

Learn more
----------

The parameters and configurations will vary for your case. Please refer below for PostgreSQL and Aiven for ClickHouse advanced parameters, a related blog, and how to get started with Aiven Terraform Provider:

- `Set up your first Aiven Terraform project <https://docs.aiven.io/docs/tools/terraform/get-started.html>`_

Follow up
---------
