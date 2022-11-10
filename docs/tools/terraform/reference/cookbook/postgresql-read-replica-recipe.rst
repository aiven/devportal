PostgreSQL® read replica using Terraform
========================================================

A PostgreSQL® read replica can be used to offload read requests like the analytics traffic from the primary instance. In this example, you'll create two Aiven for PostgreSQL® services - a primary service and the other one as its read replica. 
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

Be sure to check out the :doc:`getting started guide <../../get-started>` to learn about the common files required to execute the following recipe. For example, you'll need to declare the variables for ``project_name`` and ``api_token``.

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

    3. The ``var-values.tfvars`` file holds the actual values and is passed to Terraform using the ``-var-file=`` flag.

    ``var-values.tfvars`` file:

    .. code:: terraform

       aiven_api_token     = "<YOUR-AIVEN-AUTHENTICATION-TOKEN-GOES-HERE>"
       project_name        = "<YOUR-AIVEN-CONSOLE-PROJECT-NAME-GOES-HERE>"

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

When you run ``terraform apply`` command, ``demo-postgresql-primary`` gets created first since ``demo-postgresql-read-replica`` service depends on it. 
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
- `Configuration options for PostgreSQL <https://docs.aiven.io/docs/products/postgresql/reference/list-of-advanced-params.html>`_
- `Create and use read-only replicas <https://docs.aiven.io/docs/products/postgresql/howto/create-read-replica>`_
- `Set up your first Aiven Terraform project <https://docs.aiven.io/docs/tools/terraform/get-started.html>`_
