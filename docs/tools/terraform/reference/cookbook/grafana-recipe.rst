Deploy a Grafana® service to visualize PostgreSQL® metrics
==========================================================

Whether monitoring your data infrastructure or analyzing the resource utilization based on metrics, `Aiven for Grafana <https://aiven.io/grafana>`_ provides powerful visualizations and easy integrations for your Aiven services.
This example shows how to use the `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_  to create an Aiven for PosgreSQL service, an Aiven for Grafana service and the service integration programmatically. 

.. mermaid::

   flowchart LR
      PostgreSQL[Aiven for PostgreSQL]
      Grafana[Aiven for Grafana]
      PostgreSQL ==>|metrics| Grafana
      PostgreSQL <-- Service Integration --> Grafana

In the above diagram, the Grafana dashboard is able to display the metrics for the PostgreSQL service because a service integration is established between these two services. 

Let's cook!
-----------

Here is the sample Terraform file to deploy two services and a service integration. Keep in mind that some parameters and configurations will vary for your case. A reference to some of the advanced Grafana configurations is added at the end of this document.

.. Tip::

    Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe. For example, you'll need to declare the variables for ``project_name`` and ``api_token``.

``services.tf`` file:

.. code:: terraform

    # Postgres Service

    resource "aiven_pg" "demo-pg" {
      project                = var.project_name
      cloud_name             = "google-northamerica-northeast1" 
      plan                   = "startup-4"                      
      service_name           = join("-", [var.service_name_prefix, "postgres"])
      termination_protection = false
    }

    # Grafana Service

    resource "aiven_grafana" "demo-grafana" {
      project                 = var.project_name
      cloud_name              = "google-northamerica-northeast1"
      plan                    = "startup-4"
      service_name            = join("-", [var.service_name_prefix, "grafana"])
      maintenance_window_dow  = "monday"
      maintenance_window_time = "10:00:00"

      grafana_user_config {
        alerting_enabled = true

        public_access {
          grafana = true
        }
      }
    }

    # PG-Grafana Service Integration

    resource "aiven_service_integration" "postgresql_to_grafana" {
      project                  = var.project_name
      integration_type         = "dashboard"
      source_service_name      = aiven_grafana.demo-grafana.service_name
      destination_service_name = aiven_pg.demo-pg.service_name
    }

At first, the **aiven_pg** and **aiven_grafana** resources are created. Once the services are running, the third Terraform resource **aiven_service_integration** is created which establishes the service integration between the Aiven for PostgreSQL and Aiven for Grafana services.
For **aiven_grafana**, you have to choose the `integration_type` as ``dashboard``. 

More resources
--------------

You might find these related resources useful too:

- `Configuration options for Aiven for Grafana <https://developer.aiven.io/docs/products/grafana/reference/advanced-params.html>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
- `Metrics and graphs with M3 and Grafana <https://aiven.io/blog/metrics-and-graphs-with-m3-and-grafana>`_
