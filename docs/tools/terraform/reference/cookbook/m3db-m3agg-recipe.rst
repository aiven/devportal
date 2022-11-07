Setup M3-related services using Aiven Terraform Provider
========================================================

`Aiven for M3DB <https://developer.aiven.io/docs/products/m3db>`_ is a powerful time-series database that can be used when handling very large volumes of metrics and scalability is a concern. `Aiven for M3 Aggregator <https://developer.aiven.io/docs/products/m3db/concepts/m3-components.html>`_ can store your data at various resolutions for different workloads at scale. 
Together, they are a perfect choice to aggregate, store, and query large time-series data like internet of things (IoT) sensor readings. 

This example shows how to use the `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_  to create an Aiven for M3 service, an Aiven for M3 Aggregator service, and the related service integration programmatically. 

.. mermaid::

  graph LR
      M3[(M3DB + M3 Coordinator)]
      M3Agg[M3 Aggregator]
      M3 -.-> M3Agg

In the above diagram, the M3 service contains both M3DB and M3 Coordinator. The service integration between M3DB + M3 Coordinator and M3 Aggregator brings unaggregated metrics from M3 Coordinator to M3 Aggregator. 
While you can perform aggregations without an M3 Aggregator node, a dedicated metrics aggregator can help in cases when the downsampling workload is slowing down the ingestion of metrics by the main M3DB.
For example, to aggregate all IoT metrics from the last two months into 10-minute points. 

Let's cook!
-----------

The following Terraform recipe will create an Aiven for M3 service, an Aiven for M3 Aggregator service, and the related service integration.

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

       aiven_api_token        = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
       project_name           = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"
       service_name_prefix    = "<YOUR-CHOICE-OF-A-SERVICE-NAME-PREFIX>" 

``services.tf`` file:

.. code:: terraform
  
  resource "aiven_m3db" "demo-m3db" {
    project      = var.project_name
    cloud_name   = "google-northamerica-northeast1"
    plan         = "business-8"
    service_name = join("-", [var.service_name_prefix, "m3db"])
  
    m3db_user_config {
      m3db_version = 1.5
  
      namespaces {
        name = "m3_default_unaggregated_ns"
        type = "unaggregated"
        options {
          retention_options {
            retention_period_duration = "2h"
          }
        }
      }
      namespaces {
        name       = "m3_lowRes_aggregated_ns"
        type       = "aggregated"
        resolution = "10m"
        options {
          retention_options {
            retention_period_duration = "6d"
          }
        }
      }
      namespaces {
        name       = "m3_medRes_aggregated_ns"
        type       = "aggregated"
        resolution = "2m"
        options {
          retention_options {
            retention_period_duration = "18h"
          }
        }
      }
      namespaces {
        name       = "m3_highRes_aggregated_ns"
        type       = "aggregated"
        resolution = "10s"
        options {
          retention_options {
            retention_period_duration = "4h"
          }
        }
      }
    }
  }
  
  
  // Setting up aggregation
  
  resource "aiven_m3aggregator" "demo-m3a" {
    project      = var.project_name
    cloud_name   = "google-northamerica-northeast1"
    plan         = "business-8"
    service_name = join("-", [var.service_name_prefix, "m3a"])
  
    m3aggregator_user_config {
      m3aggregator_version = 1.5
    }
  }
  
  resource "aiven_service_integration" "int-m3db-aggr" {
    project                  = var.project_name
    integration_type         = "m3aggregator"
    source_service_name      = aiven_m3db.demo-m3db.service_name
    destination_service_name = aiven_m3aggregator.demo-m3a.service_name
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

``namespaces`` in M3 is used to determine how metrics are stored and retained. There is always one unaggregated namespace which is configured under the ``demo-m3db`` resource ``namespaces`` block. There are three aggregated namespaces defined within the same block for different resolution settings.

- ``m3_default_unaggregated_ns`` keeps the unaggregated data for 2h (retention time)
- ``m3_lowRes_aggregated_ns`` aggregates the data to 10m (resolution) and keeps the data for 6d (retention time)
- ``m3_medRes_aggregated_ns`` aggregates the data to 2m (resolution) and keeps the data for 18h (retention time)
- ``m3_highRes_aggregated_ns`` aggregates the data to 10s (resolution) and keeps the data for 4h (retention time)

With high resolution (more samples per second), you'll have more data points for a given time compared to low resolution. More data points will require more storage, and that's why low resolution data is retained for a longer period of time than high resolution data. 

More resources
--------------

You might find these related resources useful too:

- `Configuration options for Aiven for M3DB <https://developer.aiven.io/docs/products/m3db/reference/advanced-params.html>`_
- `Configuration options for Aiven for M3 Aggregator <https://developer.aiven.io/docs/products/m3db/reference/advanced-params-m3aggregator.html>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
- `Metrics and graphs with M3 and Grafana® <https://aiven.io/blog/metrics-and-graphs-with-m3-and-grafana>`_
