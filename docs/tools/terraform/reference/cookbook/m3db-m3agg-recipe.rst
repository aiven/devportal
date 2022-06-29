Setup M3-related services using Aiven Terraform Provider
========================================================

`Aiven for M3DB <https://aiven.io/m3>`_ is a powerful time-series database that can be used when handling very large volumes of metrics and scalability is a concern. `Aiven for M3 Aggregator <https://aiven.io/m3-aggregator>`_ can store your data at various resolutions for different workloads at scale. 
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

``namespaces`` in M3 is used to determine how metrics are stored and retained. There is always one unaggregated namespace which is configured under the ``demo-m3db`` resource ``namespaces`` block. There are three aggregated namespaces defined within the same block for different resolution settings.

- ``m3_default_unaggregated_ns`` keeps the unaggregated data for 2h (retention time)
- ``m3_lowRes_aggregated_ns`` downsamples the data to 10m (resolution) and keeps the data for 6d (retention time)
- ``m3_medRes_aggregated_ns`` downsamples the data to 2m (resolution) and keeps the data for 18h (retention time)
- ``m3_highRes_aggregated_ns`` downsamples the data to 10s (resolution) and keeps the data for 4h (retention time)

With high resolution (more samples per second), you'll have more data points for a given time compared to low resolution. More data points will require more storage, and that's why low resolution data is retained for a longer period of time than high resolution data. 

More resources
--------------

You might find these related resources useful too:

- `Configuration options for Aiven for M3DB <https://developer.aiven.io/docs/products/m3db/reference/advanced-params.html>`_
- `Configuration options for Aiven for M3 Aggregator <https://developer.aiven.io/docs/products/m3db/reference/advanced-params-m3aggregator.html>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
- `Metrics and graphs with M3 and Grafana® <https://aiven.io/blog/metrics-and-graphs-with-m3-and-grafana>`_
