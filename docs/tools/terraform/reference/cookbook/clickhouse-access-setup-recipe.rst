Manage user's access for Terraform-deployed ClickHouse® services
================================================================

This article shows by way of example how to set up user's permissions for a Terraform project containing a managed ClickHouse® service. It details how to grant the administrator's (read and write) access and the analyst's (read) access.

Prerequisites
-------------

* `Download and install Terraform <https://www.terraform.io/downloads>`_.
* `Sign up <https://console.aiven.io/signup?utm_source=github&utm_medium=organic&utm_campaign=devportal&utm_content=repo>`_ for Aiven if you haven't already.
* `Generate an authentication token <https://docs.aiven.io/docs/platform/howto/create_authentication_token.html>`_.

.. seealso::

    For information on what types of access you can grant to your project, see `Project members and roles <https://docs.aiven.io/docs/platform/concepts/projects_accounts_access.html#project-members-and-roles>`_.

Let's cook!
-----------

Imagine that you are collecting IoT measurements from thousands of sensors and these metrics are populated in Apache Kafka® topic ``iot_measurements``.

You may wish to create an Aiven for ClickHouse® service along with a database containing IoT sensor measurements and
correct permissions for two roles: the writer role (allowed to insert data) and the analyst role (allowed to query data).

Configure common files
''''''''''''''''''''''

.. dropdown:: Expand to check out the relevant common files needed for this recipe.

  Navigate to a new folder and add the following files:

  1. ``provider.tf`` file

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

  .. tip::
    
    You can set environment variable ``AIVEN_TOKEN`` for the ``api_token`` property so that you don't need to pass the ``-var-file`` flag when executing Terraform commands.

  2. ``variables.tf`` file

  Use it for defining the variables to avoid including sensitive information in source control. The ``variables.tf`` file defines the API token, the project name to use, and the prefix for the service name:

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

  Use it to indicate the actual values of variables so that they can be passed (with the ``-var-file=`` flag) to Terraform during runtime and excluded later on. Configure the ``var-values.tfvars`` file as follows:

    .. code:: terraform

       aiven_api_token     = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
       project_name        = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"

Set up service and database
'''''''''''''''''''''''''''

Configure the ``services.tf`` file as follows:

.. code:: terraform

  resource "aiven_clickhouse" "clickhouse" {
    project                 = var.project_name
    cloud_name              = "google-europe-west1"
    plan                    = "startup-16"
    service_name            = "clickhouse-gcp-eu"
    maintenance_window_dow  = "monday"
    maintenance_window_time = "10:00:00"
  }

  resource "aiven_clickhouse_database" "measurements" {
    project                 = var.project_name
    service_name            = aiven_clickhouse.clickhouse.service_name
    name                    = "iot_measurements"
  }

.. topic:: Expected result

  * ``"aiven_clickhouse"`` resource creates an Aiven for ClickHouse service with the project name, choice of a cloud provider, an Aiven service plan, and a specified service name.
  * ``"aiven_clickhouse_database"`` resource creates the measurements database.

Grant user's permissions
''''''''''''''''''''''''

Administrator role - read & write access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the ``access-writer.tf`` file as follows:

.. code-block:: terraform

  // ETL user with write permissions to the IoT measurements DB
  resource "aiven_clickhouse_user" "etl" {
    project      = var.project_name
    service_name = aiven_clickhouse.clickhouse.service_name
    username     = "etl"
  }

  // Writer role that will be granted insert privilege to the measurements DB
  resource "aiven_clickhouse_role" "writer" {
    project      = var.project_name
    service_name = aiven_clickhouse.clickhouse.service_name
    role         = "writer"
  }

  // Writer role's privileges
  resource "aiven_clickhouse_grant" "writer_role" {
    project      = aiven_clickhouse.clickhouse.project
    service_name = aiven_clickhouse.clickhouse.service_name
    role         = aiven_clickhouse_role.writer.role

    privilege_grant {
      privilege = "INSERT"
      database  = aiven_clickhouse_database.measurements.name
      table     = "*"
    }

    privilege_grant {
      privilege = "SELECT"
      database  = aiven_clickhouse_database.measurements.name
      table     = "*"
    }
  }

  // Grant the writer role to the ETL user
  resource "aiven_clickhouse_grant" "etl_user" {
    project      = aiven_clickhouse.clickhouse.project
    service_name = aiven_clickhouse.clickhouse.service_name
    user         = aiven_clickhouse_user.etl.username

    role_grant {
      role = aiven_clickhouse_role.writer.role
    }
  }

.. topic:: Expected result

  * ``"aiven_clickhouse_user"`` resource creates a user that can connect to the cluster.
  * ``"aiven_clickhouse_role"`` resources creates a role that can be granted fine-grained privileges at the table level.
  * ``"aiven_clickhouse_grant"."writer_role"`` resource specifies the privileges and the scope of their application
  using the ``privilege_grant`` nested configuration.
  * ``"aiven_clickhouse_grant"."etl_user"`` assigns the ``writer`` role to the ``etl`` user.

Analyst role - read access
~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the ``access-analyst.tf`` file as follows:

.. code-block:: terraform

  // Analyst user with read-only access to the IoT measurements DB
  resource "aiven_clickhouse_user" "analyst" {
    project      = var.project_name
    service_name = aiven_clickhouse.clickhouse.service_name
    username     = "analyst"
  }

  // Reader role that will be granted insert privilege to the measurements DB
  resource "aiven_clickhouse_role" "reader" {
    project      = var.project_name
    service_name = aiven_clickhouse.clickhouse.service_name
    role         = "reader"
  }

  // Reader role's privileges
  resource "aiven_clickhouse_grant" "reader_role" {
    project      = aiven_clickhouse.clickhouse.project
    service_name = aiven_clickhouse.clickhouse.service_name
    role         = aiven_clickhouse_role.reader.role

    privilege_grant {
      privilege = "SELECT"
      database  = aiven_clickhouse_database.measurements.name
      table     = "*"
    }
  }

  // Grant the reader role to the Analyst user
  resource "aiven_clickhouse_grant" "analyst_user" {
    project      = aiven_clickhouse.clickhouse.project
    service_name = aiven_clickhouse.clickhouse.service_name
    user         = aiven_clickhouse_user.analyst.username

    role_grant {
      role = aiven_clickhouse_role.reader.role
    }
  }

Execute the Terraform files
'''''''''''''''''''''''''''

.. dropdown:: Expand to check out how to execute the Terraform files.

  1. Run the following command:

    .. code:: shell

       terraform init

  The ``init`` command performs several different initialization operations to prepare the current working directory for use with Terraform. For this recipe, ``init`` automatically finds, downloads, and installs the necessary Aiven Terraform Provider plugins.

  2. Run the following command:

    .. code:: bash

       terraform plan -var-file=var-values.tfvars

  The ``plan`` command creates an execution plan and shows the resources that will be created (or modified). This command doesn't actually create any resource but gives you a heads-up on what's going to happen.

  3. If the output of ``terraform plan`` looks as expected, run the following command:

    .. code:: bash

       terraform apply -var-file=var-values.tfvars

  The ``terraform apply`` command creates (or modifies) your infrastructure resources.
