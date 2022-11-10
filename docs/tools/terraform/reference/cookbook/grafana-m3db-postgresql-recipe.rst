Deploy a Grafana® service to visualize PostgreSQL® metrics
==========================================================

Whether monitoring your data infrastructure or analyzing resource utilization based on metrics, `Aiven for Grafana <https://aiven.io/grafana>`_ provides powerful visualizations and easy integrations for your Aiven services.
A time-series database like M3DB can be used as backend to store PostgreSQL® database metrics to be queried by the Grafana dashboard.
This example shows how to use the `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_  to create an Aiven for PosgreSQL service, an Aiven for M3DB service, an Aiven for Grafana service, and the related service integrations programmatically. 

.. mermaid::

   flowchart LR
      PostgreSQL[Aiven for PostgreSQL]
      M3DB[Aiven for M3DB]
      Grafana[Aiven for Grafana]
      PostgreSQL ==>|si-metrics| M3DB
      Grafana ==>|si-dashboard| M3DB

In the above diagram, the PostgreSQL service metrics are pushed to M3DB which is then queried by a prebuilt Grafana dashboard. All three services are connected via Aiven Service Integrations, which lets your Aiven services talk to one another without you having to write complex integration codes.
``si-...`` in the above diagram stands for "Service Integration".

Let's cook!
-----------

Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe. For example, you'll need to declare the variables for ``project_name``, ``api_token``, and ``service_name_prefix``.

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

       variable "service_name_prefix" {
         description = "A string to prepend to the service name"
         type        = string
       }
   
   
    3. The ``var-values.tfvars`` file holds the actual values and is passed to Terraform using the ``-var-file=`` flag.

    ``var-values.tfvars`` file:

    .. code:: terraform

       aiven_api_token     = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
       project_name        = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"
       service_name_prefix = "<YOUR-CHOICE-OF-A-SERVICE-NAME-PREFIX>"

``services.tf`` file:

.. code:: terraform
  
  
  # PostgreSQL Service
  
  resource "aiven_pg" "demo-pg" {
    project                 = var.project_name
    cloud_name              = "google-northamerica-northeast1"
    plan                    = "startup-8"
    service_name            = join("-", [var.service_name_prefix, "postgres"])
    termination_protection  = false
    maintenance_window_dow  = "sunday"
    maintenance_window_time = "10:00:00"
  }
  
  # M3DB Service
  
  resource "aiven_m3db" "demo-m3db" {
    project                 = var.project_name
    cloud_name              = "google-northamerica-northeast1"
    plan                    = "startup-8"
    service_name            = join("-", [var.service_name_prefix, "m3db"])
    maintenance_window_dow  = "sunday"
    maintenance_window_time = "10:00:00"
  
    m3db_user_config {
      m3db_version = 1.1
  
      namespaces {
        name = "my_ns1"
        type = "unaggregated"
      }
    }
  }
  
  # Grafana Service
  
  resource "aiven_grafana" "demo-grafana" {
    project                 = var.project_name
    cloud_name              = "google-northamerica-northeast1"
    plan                    = "startup-8"
    service_name            = join("-", [var.service_name_prefix, "grafana"])
    maintenance_window_dow  = "sunday"
    maintenance_window_time = "10:00:00"
  
    grafana_user_config {
      alerting_enabled = true
  
      public_access {
        grafana = true
      }
    }
  }
  
  # PostgreSQL-M3DB Metrics Service Integration
  
  resource "aiven_service_integration" "postgresql_to_m3db" {
    project                  = var.project_name
    integration_type         = "metrics"
    source_service_name      = aiven_pg.demo-pg.service_name
    destination_service_name = aiven_m3db.demo-m3db.service_name
  }
  
  # M3DB-Grafana Dashboard Service Integration
  
  resource "aiven_service_integration" "m3db-to-grafana" {
    project                  = var.project_name
    integration_type         = "dashboard"
    source_service_name      = aiven_grafana.demo-grafana.service_name
    destination_service_name = aiven_m3db.demo-m3db.service_name
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

At first, ``aiven_pg``, ``aiven_m3db``, and ``aiven_grafana`` resources are created. Once these three services are running, the resources that bridge them ``aiven_service_integration`` are created.
Note the different ``integration_type`` used for each of these service integrations. 

More resources
--------------

You might find these related resources useful too:

- `Configuration options for Aiven for Grafana <https://docs.aiven.io/docs/products/grafana/reference/advanced-params.html>`_
- `Configuration options for Aiven for PostgreSQL <https://docs.aiven.io/docs/products/postgresql/reference/list-of-advanced-params.html>`_
- `Configuration options for Aiven for M3DB <https://docs.aiven.io/docs/products/m3db/reference/advanced-params.html>`_
- `Set up your first Aiven Terraform project <https://docs.aiven.io/docs/tools/terraform/get-started.html>`_
- `Metrics and graphs with M3 and Grafana <https://aiven.io/blog/metrics-and-graphs-with-m3-and-grafana>`_
