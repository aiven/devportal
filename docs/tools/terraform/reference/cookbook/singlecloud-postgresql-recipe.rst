Deploy PostgreSQL® service to a single cloud and region
=========================================

This example shows the setup for a Terraform project containing a single PostgreSQL service. The following setup shows that the Aiven Terraform Provider calls the Aiven API under the hood to create a PostgreSQL service with startup-4 plan on Google Cloud Platform (Europe).


Describe the setup
'''''''''''''''''''''''''''''''''''

Your Terraform files declare the structure of your infrastructure as well as required dependencies and configuration. While you can stuff these together in one file, it's ideal to keep those as separate files.

The following Terraform script deploys a single-node PostgreSQL service. This is a minimal example which you can swap out with your own Terraform scripts or other advanced recipes from :doc:`the Terraform cookbook <reference/cookbook>`.

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

    public_access {
      pg         = false
      prometheus = false
    }

    pg {
      idle_in_transaction_session_timeout = 900
      log_min_duration_statement          = -1
      } 
    }

    timeouts {
      create = "20m"
      update = "15m"
    }
  }

This file create one Aiven for PostgreSQL service in the region that has been defined in the file. The ``termination_protection = true`` property ensures that these databases are protected against accidental or unauthorized deletion.

With termination protection enabled, a ``terraform destroy`` command will result in a 403 response and an error message "Service is protected against termination and shutdown. Remove termination protection first.".

To destroy resources with termination protection, you need to update the script with ``termination_protection = false`` and then execute a ``terraform apply`` followed by a ``terraform destroy``.


More resources
'''''''''''''''''

You might find these related resources useful too:

- `Configuration options for PostgreSQL <https://developer.aiven.io/docs/products/postgresql/reference/list-of-advanced-params.html>`_
- `Set up your first Aiven Terraform project <https://developer.aiven.io/docs/tools/terraform/get-started.html>`_
