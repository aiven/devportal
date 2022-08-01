Use PostgreSQL® provider with Aiven's PostgreSQL service
#####################################################

`Aiven Terraform provider <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_ can be used to create and manage Aiven for PostgreSQL® service, PostgreSQL® databases, and users. If you need to perform additional configurations such as setting PostgreSQL default privileges, configure PostgreSQL publication, or reuse a PostgreSQL-based sub-module between different vendors to make the Terraform code homogeneous, you can consider using the `PostgreSQL® provider <https://registry.terraform.io/providers/cyrilgdn/postgresql/latest/docs>`_.
This article shows how to use the PostgreSQL provider along with the Aiven Terraform Provider to create a PostgreSQL role.   


Configure the required providers
--------------------------------

The new provider must be added to the ``required_providers`` block in the Terraform code.

1. This example shows how to add the PostgreSQL provider (source: ``cyrilgdn/postgresql``) along with the Aiven Terraform Provider (source: ``aiven/aiven``).

.. code:: terraform

    terraform {
      required_providers {
        aiven = {
          source  = "aiven/aiven"
          version = ">= 3.1"
        }
        postgresql = {
          source  = "cyrilgdn/postgresql"
          version = "1.16.0"
        }        
      }
    }

2. If the PostgreSQL provider is used on its own, you can provide the Aiven for PostgreSQL service connection details as follows: 

.. code:: terraform

    provider "postgresql" {
      host            = "pg-serivicename-projectname.aivencloud.com"
      port            = 12691
      database        = "defaultdb"
      username        = "avnadmin"
      password        = "postgres_password"
      sslmode         = "require"
      connect_timeout = 15
    }

Optionally, when the Aiven for PostgreSQL service is created within the same Terraform project, the values required to configure the PostgreSQL provider can be passed using references to the resource, as shown in the code below:

.. code:: terraform

    resource "aiven_pg" "demo-pg" {
      project                 = var.project_name
      cloud_name              = "google-asia-southeast1"
      plan                    = "business-8"
      service_name            = "demo-pg"
      termination_protection  = true
    }

    # PostgreSQL provider is configured with references to the aiven_pg.demo-pg resource.
    provider "postgresql" {
      host            = aiven_pg.demo-pg.service_host
      port            = aiven_pg.demo-pg.service_port
      database        = "defaultdb"
      username        = aiven_pg.demo-pg.service_username
      password        = aiven_pg.demo-pg.service_password
      sslmode         = "require"
      connect_timeout = 15
    }

3. Create a PostgreSQL role called **test_role** using the Terraform resource ``postgresql_role.my_role``. 

.. code:: terraform

    resource "postgresql_role" "my_role" {
      name     = "test_role"
    }

.. note::

  For the full documentation of the ``Aiven Terraform Provider`` refer to `Aiven provider documentation <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_.

  For the full list of resources available in ``PostgreSQL provider`` refer to `PostgreSQL provider documentation <https://registry.terraform.io/providers/cyrilgdn/postgresql/latest/docs>`_.

