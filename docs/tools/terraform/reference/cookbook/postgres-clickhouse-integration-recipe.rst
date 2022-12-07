Aiven for PostgreSQL® as a source for Aiven for ClickHouse®
===========================================================

You can use a PostgreSQL database as a data source and Aiven for ClickHouse® - to read, transform, and execute jobs using data from the PostgreSQL server. For this purpose, you need to integrate Aiven for PostgreSQL® with Aiven for ClickHouse®. Continue reading to learn how to connect these services using `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_.

Let's cook!
-----------

Imagine that you've been collecting IoT measurements from thousands of sensors and storing them in ClickHouse database ``iot_measurements``. Now, you'd like to enrich your metrics by adding the sensor's location to the measurements so that you can filter the metrics by city name. The sensor's location data is available in the ``sensors_dim`` database in PostgreSQL.

This recipe calls for the following:

1. Set up an Aiven for ClickHouse database.
2. Insert your measurements data into the Aiven for ClickHouse database.
3. Combine your measurements data in the Aiven for ClickHouse database with the related PostgreSQL dimension database.

.. mermaid::

   flowchart LR
      subgraph Aiven for PostgreSQL
      id1[(sensors_dim database)]
      end
      subgraph Aiven for ClickHouse
      id2[(iot_measurements database)]
      id3[(service_postgres-gcp-us_sensor_dims_public database)]
      end
      id1 ==> |Service integration| id3

Configure common files
''''''''''''''''''''''

.. dropdown:: Expand to check out the relevant common files needed for this recipe.

  Navigate to a new folder and add the following files:

  1. ``provider.tf`` file

    .. code-block:: terraform

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

  .. tip::

    You can set environment variable ``AIVEN_TOKEN`` for the ``api_token`` property so that you don't need to pass the ``-var-file`` flag when executing Terraform commands.

  2. ``variables.tf`` file

  Use it for defining the variables to avoid including sensitive information in source control. The ``variables.tf`` file defines the API token, the project name, and the prefix for the service name.

    .. code:: terraform

       variable "aiven_api_token" {
         description = "Aiven console API token"
         type        = string
       }
   
       variable "project_name" {
         description = "Aiven console project name"
         type        = string
       }

  3. ``*.tfvars`` file

  Use it to indicate the actual values of the variables so that they can be passed (with the ``-var-file=`` flag) to Terraform during runtime and excluded later on. Configure the ``var-values.tfvars`` file as follows:

    .. code-block:: terraform

       aiven_api_token     = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
       project_name        = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"

Configure the ``services.tf`` file
''''''''''''''''''''''''''''''''''

The following Terraform script initializes both Aiven for PostgreSQL and Aiven for ClickHouse services, creates the service integration, the source PostgreSQL database, and the Aiven for ClickHouse database.

.. code-block:: terraform

  // Postgres service based in GCP US East
  resource "aiven_pg" "postgres" {
    project                 = var.project_name
    service_name            = "postgres-gcp-us"
    cloud_name              = "google-us-east4"
    plan                    = "business-8" // Primary + read replica
    maintenance_window_dow  = "monday"
    maintenance_window_time = "10:00:00"
  }

  // Postgres sensor dimensions database
  resource "aiven_pg_database" "sensor_dims" {
    project       = var.project_name
    service_name  = aiven_pg.postgres.service_name
    database_name = "sensor_dims"
  }

  // ClickHouse service based in the same region
  resource "aiven_clickhouse" "clickhouse" {
    project                 = var.project_name
    service_name            = "clickhouse-gcp-us"
    cloud_name              = "google-us-east4"
    plan                    = "startup-beta-16"
    maintenance_window_dow  = "monday"
    maintenance_window_time = "10:00:00"
  }

  // Sample ClickHouse database that can be used to write and process raw data
  resource "aiven_clickhouse_database" "iot_measurements" {
    project      = var.project_name
    service_name = aiven_clickhouse.clickhouse.service_name
    name         = "iot_measurements"
  }

  // ClickHouse service integration for the PostgreSQL service as a source
  resource "aiven_service_integration" "clickhouse_postgres_source" {
    project                  = var.project_name
    integration_type         = "clickhouse_postgresql"
    source_service_name      = aiven_pg.postgres.service_name
    destination_service_name = aiven_clickhouse.clickhouse.service_name
    clickhouse_postgresql_user_config {
      databases {
        database = aiven_pg_database.sensor_dims.database_name
        schema = "public"
      }
    }
  }

Execute the Terraform files
'''''''''''''''''''''''''''

.. dropdown:: Expand to check out how to execute the Terraform files.

  1. Run the following command:

    .. code-block:: shell

       terraform init
  
  The ``init`` command performs initialization operations to prepare the working directory for use with Terraform. For this recipe, ``init`` automatically finds, downloads, and installs the necessary Aiven Terraform Provider plugins.

  2. Run the following command:

    .. code-block:: bash

       terraform plan -var-file=var-values.tfvars
  
  The ``plan`` command creates an execution plan and shows the resources to be created (or modified). This command doesn't actually create any resources but gives you a heads-up on what's going to happen next.

  3. If the output of ``terraform plan`` looks as expected, run the following command:

    .. code-block:: bash

       terraform apply -var-file=var-values.tfvars
  
  The ``terraform apply`` command creates (or modifies) your infrastructure resources.

Check out the results
---------------------

* ``aiven_clickhouse`` resource creates an Aiven for ClickHouse service with the parameters specified in the ``services.tf`` file (project name, cloud name, service plan and service name)
* ``aiven_clickhouse_database`` resource creates a database that can be used to store high-throughput measurement data as well as create new tables and views to process this data.
* ``aiven_pg`` resource creates a highly-available Aiven for PostgreSQL service.
* ``aiven_pg_database`` resource creates the ``sensor_dims`` database.
* ``aiven_service_integration`` resource creates the integration between the Aiven for PostgreSQL and Aiven for ClickHouse services.

This results in the creation of the ``service_postgres-gcp-us_sensor_dims_public`` database in Aiven for ClickHouse, allowing you to access the ``sensor_dims`` database for the ``postgres-gcp-us`` service.

Learn more
----------

When you use this recipe, parameters and configurations will vary from those used in this article. For Aiven for PostgreSQL and Aiven for ClickHouse advanced parameters, a related blog, and instructions on how to get started with Aiven Terraform Provider, see `Set up your first Aiven Terraform project <https://docs.aiven.io/docs/tools/terraform/get-started.html>`_.
