Deploy a Grafana® service to visualize PostgreSQL® metrics
==========================================================

Whether monitoring your data infrastructure or analyzing resource utilization based on metrics, `Aiven for Grafana <https://aiven.io/grafana>`_ provides powerful visualizations and easy integrations for your Aiven services.
A time-series database like M3DB can be used as a data source to send the relational database metrics to the Grafana dashboard.
This example shows how to use the `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_  to create an Aiven for PosgreSQL service, an Aiven for M3DB service, an Aiven for Grafana service, and the related service integrations programmatically. 

.. mermaid::

   flowchart LR
      PostgreSQL[Aiven for PostgreSQL]
      M3DB[Aiven for M3DB]
      Grafana[Aiven for Grafana]
      PostgreSQL ==>|si-metrics| M3DB
      M3DB ==>|si-datasource| Grafana
      Grafana ==>|si-dashboard| PostgreSQL

In the above diagram, the Grafana dashboard is able to display the metrics for the PostgreSQL service because M3DB is acting as a datasource in the middle. All three services are connected via Aiven Service Integrations, which lets your Aiven services talk to one another without you having to write complex integration codes.
``si-...`` in the above diagram stands for "Service Integration".

Let's cook!
-----------

Here is the sample Terraform file to deploy the three services and three service integrations. Keep in mind that some parameters and configurations will vary for your case. A reference to some of the advanced configurations is added at the end of this document.

.. Tip::

    Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe. For example, you'll need to declare the variables for ``project_name``, ``api_token``, and ``service_name_prefix``.

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

  # PostgreSQL-M3DB Service Integration

  resource "aiven_service_integration" "postgresql_to_m3db" {
    project                  = var.project_name
    integration_type         = "metrics"
    source_service_name      = aiven_pg.demo-pg.service_name
    destination_service_name = aiven_m3db.demo-m3db.service_name
  }

  # M3DB-Grafana Service Integration

  resource "aiven_service_integration" "m3db-to-grafana" {
    project                  = var.project_name
    integration_type         = "datasource"
    source_service_name      = aiven_grafana.demo-grafana.service_name
    destination_service_name = aiven_m3db.demo-m3db.service_name
  }

  # PostgreSQL-Grafana Service Integration

  resource "aiven_service_integration" "postgresql-to-grafana" {
    project                  = var.project_name
    integration_type         = "dashboard"
    source_service_name      = aiven_grafana.demo-grafana.service_name
    destination_service_name = aiven_pg.demo-pg.service_name
  }

At first, ``aiven_pg``, ``aiven_m3db``, and ``aiven_grafana`` resources are created. Once these three services are running, the resources that bridge them ``aiven_service_integration`` are created.
Note the different ``integration_type`` used for each of these service integrations. 

More resources
--------------

You might find these related resources useful too:

- `Configuration options for Aiven for Grafana <https://developer.aiven.io/docs/products/grafana/reference/advanced-params.html>`_
- `Configuration options for Aiven for PostgreSQL <https://developer.aiven.io/docs/products/postgresql/reference/list-of-advanced-params.html>`_
- `Configuration options for Aiven for M3DB <https://developer.aiven.io/docs/products/m3db/reference/advanced-params.html>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
- `Metrics and graphs with M3 and Grafana <https://aiven.io/blog/metrics-and-graphs-with-m3-and-grafana>`_
