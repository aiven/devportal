Setup M3-related services using Aiven Terraform Provider
========================================================

`Aiven for M3DB <https://aiven.io/m3>`_ is a powerful time-series database that can be used to monitor your Aiven services on a very large scale. `Aiven for M3 Aggregator <https://aiven.io/m3-aggregator>`_ can store your data at various resolutions for different workloads at scale. You can monitor a relational database like PostgreSQL® by sending its metrics to M3DB with M3 Aggregator integration and then visualizing the metrics data on an Aiven for Grafana® dashboard.
This example shows how to use the `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_  to create an Aiven for M3 service, an Aiven for M3 Aggregator service, and the related service integration programmatically. 

.. mermaid::

  graph LR
      M3[(M3DB + M3 Coordinator)]
      M3Agg[M3 Aggregator]
      M3 -.-> M3Agg

In the above diagram, the M3 service contains both M3DB and M3 Coordinator. If you're planning for longer retentions, the M3 aggregator can help reduce the volume of time series data stored by using variable data point resolutions. 
The service integration between M3DB + M3 Coordinator and M3 Aggregator brings unaggregated metrics from M3 Coordinator to M3 Aggregator.

Let's cook!
-----------

The following Terraform recipe will create an Aiven for M3 service, an Aiven for M3 Aggregator service, and the related service integration.

.. Tip::

    Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe. For example, you'll need to declare the variables for ``project_name``, ``api_token``, and ``service_name_prefix``.

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
      }
      namespaces {
        name       = "m3_lowRes_aggregated_ns"
        type       = "aggregated"
        resolution = "10m"
        options {
          retention_options {
            retention_period_duration = "1d"
          }
        }
      }
      namespaces {
        name       = "m3_medRes_ns"
        type       = "aggregated"
        resolution = "2m"
        options {
          retention_options {
            retention_period_duration = "6h"
          }
        }
      }
      namespaces {
        name       = "m3_highRes_ns"
        type       = "aggregated"
        resolution = "10s"
        options {
          retention_options {
            retention_period_duration = "1h"
          }
        }
      }
    }
  }

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

``namespaces`` in M3 is used to determine how metrics are stored and retained. There is always one unaggregated namespace which is configured under the ``demo-m3db`` resource ``namespaces`` block. There are three aggregated namespaces defined within the same block for different resolution settings.
Typically, a low resolution data is retained for a longer period of time than a high resolution data. 

More resources
--------------

You might find these related resources useful too:

- `Configuration options for Aiven for M3DB <https://developer.aiven.io/docs/products/m3db/reference/advanced-params.html>`_
- `Configuration options for Aiven for M3 Aggregator <https://developer.aiven.io/docs/products/m3db/reference/advanced-params-m3aggregator.html>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
- `Metrics and graphs with M3 and Grafana <https://aiven.io/blog/metrics-and-graphs-with-m3-and-grafana>`_
