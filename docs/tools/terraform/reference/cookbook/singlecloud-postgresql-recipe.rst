Deploy PostgreSQL® service to a single cloud and region
=======================================================

PostgreSQL® has been a popular choice for decades as an open source, relational database to run in production. This example shows how to use Terraform script to create a single PostgreSQL service in a single cloud and region with some basic configurations applied to the service.

The following image shows that the `Aiven Terraform Provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_ calls the Aiven API under the hood to create a single Aiven for PostgreSQL® services on Google Cloud Platform (Europe):

.. mermaid::

   flowchart LR
      id1[[Terraform]]
      id2>Aiven Terraform Provider]
      subgraph Aiven Platform
      id3[(Aiven for PostgreSQL)]
      end
      id1 --> id2 --> id3

Let's cook!
'''''''''''''''''''''''''''''''''''

The following sample Terraform script stands up the single PostgreSQL service with some configurations. 

``services.tf`` file:

.. code:: terraform

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
      pg_version                = 14
      backup_hour               = 01
      backup_minute             = 30
      shared_buffers_percentage = 40
  
      ## project_to_fork_from  = "source-project-name" ### You can create read-replica
      ## service_to_fork_from  = "source-pg-service"   ### PostgreSQL service by using
      ## pg_read_replica       = true                  ### these three line configurations
  
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
        min_pool_size             = 20
        autodb_max_db_connections = 100
      }
    }
  
    timeouts {
      create = "20m"
      update = "15m"
    }
  }
  
.. Tip::

  Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe. For example, you'll need to declare the variables for ``project_name`` and ``api_token``.

This file create one Aiven for PostgreSQL service in the region that has been defined in the file. You can set this new service as a read-replica service by defining the ``project_to_fork_from``, ``service_to_fork_from`` and set the value of ``pg_read_replica``

You can specify the ``admin_username`` and ``admin_password`` for this service. This option will not be available if ``pg_read_replica`` is set to true. 

More resources
'''''''''''''''''

To learn how to get started with Aiven Terraform Provider and specific PostgreSQL configurations for you use case, check out the following resources:

- `Configuration options for PostgreSQL <https://developer.aiven.io/docs/products/postgresql/reference/list-of-advanced-params.html>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
