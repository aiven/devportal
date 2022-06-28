Monitor PostgreSQL® metrics using M3-related services
=====================================================

Aiven for M3DB is a powerful metrics engine that can be used to monitor your Aiven services on a very large scale. Aiven for M3 Aggregator can store your data at various resolutions for different workloads at scale. You can monitor a relational database like PostgreSQL by sending its metrics to M3DB with M3 Aggregator integration and then visualizing the metrics data on an Aiven for Grafana® dashboard.
This example shows how to use the `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_  to create an Aiven for M3 service, an Aiven for M3 Aggregator service, an Aiven for Grafana service, an Aiven for PostgreSQL service, and the related service integrations programmatically. 

.. mermaid::

  graph LR
    PG[(PostgreSQL)] ---> |metrics| M3[(M3DB + M3 Coordinator)]
    Gr((Grafana)) ---> |dashboard| M3
    M3 -.-> Agg(M3 Aggregator)

In the above diagram, a service integration between the **PostgreSQL** service and the M3DB + M3 Coordinator service ensures that PostgreSQL metrics are sent to M3. If you're planning for longer retentions, the M3 aggregator can help reduce the volume of time series data stored by using variable data point resolutions. 
The M3 service contains both M3DB and M3 Coordinator. The service integration between **M3** and M3 Aggregator brings unaggregated metrics from M3 Coordinator to M3 Aggregator. Finally, the third service integration shows M3 data points in the form of graphs on a Grafana dashboard.

Let's cook!
-----------

The following Terraform recipe will create an Aiven for PostgreSQL service, an Aiven for M3 service, an Aiven for M3 Aggregator service, an Aiven for Grafana service, and the related service integrations.

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
        name = "m3_ns"
        type = "unaggregated"
      }
    }
  }

  resource "aiven_pg" "demo-pg" {
    project      = var.project_name
    cloud_name   = "google-northamerica-northeast1"
    service_name = join("-", [var.service_name_prefix, "postgresql"])
    plan         = "startup-4"

    pg_user_config {
      pg_version = 14
    }
  }

  resource "aiven_service_integration" "int-m3db-pg" {
    project                  = var.project_name
    integration_type         = "metrics"
    source_service_name      = aiven_pg.demo-pg.service_name
    destination_service_name = aiven_m3db.demo-m3db.service_name
  }

  resource "aiven_grafana" "demo-grafana" {
    project      = var.project_name
    cloud_name   = "google-northamerica-northeast1"
    plan         = "startup-4"
    service_name = join("-", [var.service_name_prefix, "grafana"])

    grafana_user_config {
      alerting_enabled = true

      public_access {
        grafana = true
      }
    }
  }

  resource "aiven_service_integration" "int-grafana-m3db" {
    project                  = var.project_name
    integration_type         = "dashboard"
    source_service_name      = aiven_grafana.demo-grafana.service_name
    destination_service_name = aiven_m3db.demo-m3db.service_name
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

Namespaces in M3 are used to determine how metrics are stored and retained. There is always one unaggregated namespace which is configured under the ``demo-m3db`` resource ``namespaces`` block. 
The ``grafana_user_config`` setting under the ``demo-grafana`` resource will ensure that you receive alerts based on metrics' threshold level. Make a note of the different ``integration_type`` for each of the service integrations. 

More resources
--------------

You might find these related resources useful too:

- `Configuration options for Aiven for M3DB <https://developer.aiven.io/docs/products/m3db/reference/advanced-params.html>`_
- `Configuration options for Aiven for M3 Aggregator <https://developer.aiven.io/docs/products/m3db/reference/advanced-params-m3aggregator.html>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
- `Metrics and graphs with M3 and Grafana <https://aiven.io/blog/metrics-and-graphs-with-m3-and-grafana>`_
