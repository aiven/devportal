Deploy PostgreSQL® service to a single cloud and region
=======================================================

This example shows how to use Terraform script to create a single PostgreSQL service in a single cloud and region with some basic configurations applied to the service.

The following image shows that the Aiven Terraform Provider calls the Aiven API under the hood to create a single service PostgreSQL services on AWS (Europe):

.. mermaid::

   graph TD
      B[(Aiven for PostgreSQL - AWS EU)]


Describe the setup
'''''''''''''''''''''''''''''''''''

The contents of the ``postgresql.tf`` file should look like this:

.. code:: bash

  # A single-node PostgreSQL service
  
  resource "aiven_pg" "pg" {
    project                 = var.project_name
    cloud_name              = "google-europe-west1"
    plan                    = "startup-4"
    service_name            = "my-pg1-gcp-eu"
    maintenance_window_dow  = "monday"
    maintenance_window_time = "10:00:00"
    termination_protection  = true  

    pg_user_config {
      pg_version = 14
      backup_hour           = 01
      backup_minute         = 30
      shared_buffers_percentage = 40

      ##project_to_fork_from  = "dev-sandbox"        ### You can create read-replica
      ##service_to_fork_from  = "pg-31c3595b-simon"  ### PostgreSQL service by using
      ##pg_read_replica          = true              ### these three line configurations

      ##ip_filter           = ["0.0.0.0/0", "8.8.8.8", "9.9.9.9"]
      ##admin_username      = "customadminusername"
      ##admin_password      = "addyourownpassword"

    public_access {
      pg         = false
      prometheus = false
    }

    pg {
      idle_in_transaction_session_timeout = 900
      log_min_duration_statement          = -1
      jit                                 = false
      deadlock_timeout                    = 2000
      } 

    pgbouncer {
      min_pool_size = 20
      autodb_max_db_connections = 100
      }
    }

    timeouts {
      create = "20m"
      update = "15m"
    }
  }

This file create one Aiven for PostgreSQL service in the region that has been defined in the file. You can set this new service as a read-replica service by defining the ``project_to_fork_from``, ``service_to_fork_from`` and set the value of ``pg_read_replica``

You can specify the ``admin_username`` and ``admin_password`` for this service. This option will not be available if ``pg_read_replica`` is set to true. 

More resources
'''''''''''''''''

You might find these related resources useful too:

- `Configuration options for PostgreSQL <https://developer.aiven.io/docs/products/postgresql/reference/list-of-advanced-params.html>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
