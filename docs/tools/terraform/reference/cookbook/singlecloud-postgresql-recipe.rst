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
  
      ## project_to_fork_from  = "source-project-name" 
      ## service_to_fork_from  = "source-pg-service"   
      ## pg_read_replica       = true                  
  
      ip_filter           = ["0.0.0.0/0", "8.8.8.8", "9.9.9.9"]
      admin_username      = var.admin_username
      admin_password      = var.admin_password
  
      public_access {
        pg         = false
        prometheus = false
      }
  
      pg {
        idle_in_transaction_session_timeout = 900
        log_min_duration_statement          = 1000
        deadlock_timeout                    = 2000
      }
    }
  
    timeouts {
      create = "20m"
      update = "15m"
    }
  }
  
.. Tip::

  Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe. For example, you'll need to declare the variables for ``project_name``, ``api_token``, ``admin_username``, and ``admin_password``.

This file create one Aiven for PostgreSQL service in the region that has been defined in the file. You can set this new service as a read-replica service by defining the ``project_to_fork_from``, ``service_to_fork_from`` and set the value of ``pg_read_replica``. Currently the configuration is commented out.

If you choose to set ``pg_read_replica`` to true, then the custom ``admin_username`` and ``admin_password`` will no longer work as it will follow the master configuration.


Below are some explanation for each ingredients
'''''''''''''''''''''''''''''''''''''''''''''''

``idle_in_transaction_session_timeout`` 
If a transaction is working, it is there for a reason. But if it just hangs around, why not just kill it? This is exactly what idle_in_transaction_session_timeout will do for you. Transactions cannot stay open accidentally anymore as PostgreSQL will clean things out for you.

``log_min_duration_statement``
Once you have some idea of how long a typical query statement should take to execute, this setting allows you to log only the ones that exceed some threshold you set. And then, you'll only see statements that take longer than one second to run. This can be extremely handy for finding out the source of outlier statements that take much longer than most to execute.

``deadlock_timeout``
The deadlock timeout is the amount of time that PostgreSQL waits on a lock before it checks for a deadlock. The deadlock check is an expensive operation so it is not run every time a lock needs to wait. Deadlocks should not be common in production environments and PostgreSQL will wait for a while before running the expensive deadlock check. The default timeout value in PostgreSQL is 1 second, and this is probably the smallest time interval you would want to set in practice. If your database is heavily loaded, you might want to raise this value to reduce the overhead on your database servers.




More resources
'''''''''''''''''

To learn how to get started with Aiven Terraform Provider and specific PostgreSQL configurations for you use case, check out the following resources:

- `Configuration options for PostgreSQL <https://developer.aiven.io/docs/products/postgresql/reference/list-of-advanced-params.html>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
