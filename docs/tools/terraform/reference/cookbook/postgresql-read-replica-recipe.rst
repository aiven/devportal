Create a MySQL/PostgreSQL® Read Replica using Terraform
========================================================

A MySQL/PostgreSQL® read replica can be used to offload read requests or analytics traffic from the primary instance. In this example, you'll create two Aiven for PostgreSQL® services - a primary service and the other one as its read replica. 
Both services will be provisioned programmatically using the `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_. The same process can be followed for setting up MySQL read replica as well. 
The following diagram shows the typical client interaction when a read replica is in place.

.. mermaid::

   flowchart LR
      id6[Client]
      
      id5>WAL record]

      subgraph Aiven for PostgreSQL
      id1[(Primary)]
      id2[[WAL sender]]
      id1 --> id2
      end
      
      subgraph Aiven for PostgreSQL
      id4[(Read-Replica)]
      id3[[WAL receiver]]
      id3 --> id4
      end

      id2 --> id5 --> id3

      id6-->|Data Modification|id1
      id6-->|Data Read|id4

Let's cook!
'''''''''''''''''''''''''''''''''''

The following sample Terraform script stands up the primary PostgreSQL service and a read replica for that service using service integration. 

.. Tip::

  Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe. For example, you'll need to declare the variables for ``project_name``, ``api_token``, ``admin_username``, and ``admin_password``.

``services.tf`` file:

.. code:: terraform
  
  resource "aiven_pg" "demo-postgresql-primary" {
    project                 = var.project_name
    service_name            = "demo-postgresql-primary"
    cloud_name              = "google-northamerica-northeast1"
    plan                    = "startup-4"
    maintenance_window_dow  = "sunday"
    maintenance_window_time = "10:00:00"
    termination_protection  = false
  }
  
  resource "aiven_pg" "demo-postgresql-read-replica" {
    project                 = var.project_name
    cloud_name              = "google-northamerica-northeast1"
    service_name            = "demo-postgresql-read-replica"
    plan                    = "startup-4"
    maintenance_window_dow  = "sunday"
    maintenance_window_time = "10:00:00"
    termination_protection  = false
  
    service_integrations {
      integration_type    = "read_replica"
      source_service_name = aiven_pg.demo-postgresql-primary.service_name
    }
  
    pg_user_config {
      service_to_fork_from = aiven_pg.demo-postgresql-primary.service_name
  
      pg {
        idle_in_transaction_session_timeout = 900
      }
      pgbouncer {
        server_reset_query_always = false
      }
      pglookout {
        max_failover_replication_time_lag = 60
      }
    }
  
    depends_on = [
      aiven_pg.demo-postgresql-primary,
    ]
  }
  
Once you run ``terraform apply`` command, **demo-postgresql-primary** gets created first since **demo-postgresql-read-replica** service depends on it. 
Terraform knows it from the ``depends_on`` block. Here are some configurations that are used in this setup:

- ``service_to_fork_from``: This is the source Aiven for PostgreSQL service.
- ``idle_in_transaction_session_timeout``: Kills an idle session after specified number of seconds.
- ``server_reset_query_always``: This PgBouncer configuration, when set to ``false``, causes the ``server_reset_query`` to not take effect for transaction pooling.
According to the PostgreSQL documentation, when transaction pooling is used, the ``server_reset_query`` should be empty, as clients should not use any session features.
- ``max_failover_replication_time_lag``: In case of a failover, this is the replication time lag after which ``failover_command`` will be executed and a ``failover_has_happened`` file will be created.

More resources
'''''''''''''''''

To learn how to get started with Aiven Terraform Provider and specific PostgreSQL configurations for you use case, check out the following resources:

- `What is PostgreSQL®? <https://aiven.io/blog/an-introduction-to-postgresql>`_
- `Configuration options for PostgreSQL <https://developer.aiven.io/docs/products/postgresql/reference/list-of-advanced-params.html>`_
- `Create and use read-only replicas <https://developer.aiven.io/docs/products/postgresql/howto/create-read-replica>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
