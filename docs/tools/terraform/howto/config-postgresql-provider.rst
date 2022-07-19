Use PostgreSQL provider with Aiven's Postgres service
#####################################################

Aiven's Terraform provider is aimed for provisioning and performing basic service configuration, if additional configuration on the service is required ther are other providers that can be used to perform the task. 
This article shows how to use the `PostgreSQL provider <https://registry.terraform.io/providers/cyrilgdn/postgresql/latest/docs>`_ along the ``Aiven Postgres service``.   


Configure the required providers
--------------------------------

The new provider must be added to the ``required providers`` block in the Terraform code.

1. This example shows how to add the ``PostgreSQL`` provider along with the ``Aiven`` provider

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

2. Then configure the provider with the corresponding information from the ``Aiven Postgres service``. 

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

Optionally, when the Aiven PG service is created in the same Terraform project the values required to configure the ``PostgreSQL`` provider can be passed using references to the resource, as shown in the code below:

.. code:: terraform

    # A new Aiven PG service is created.
    resource "aiven_pg" "pg-service" {
      project                 = "my_project"
      cloud_name              = "cloud_name"
      plan                    = "plan"
      service_name            = "pg-myservice"
    }

    # References to the aiven_pg.pg-service are used for configuring the provider.
    provider "postgresql" {
      host            = aiven_pg.pg-service.service_host
      port            = aiven_pg.pg-service.service_port
      database        = "defaultdb"
      username        = aiven_pg.pg-service.service_username
      password        = aiven_pg.pg-service.service_password
      sslmode         = "require"
      connect_timeout = 15
    }

3. Start using the resources available for the ``PostgreSQL`` provider. The following example shows how to create a role. 

.. code:: terraform

    resource "postgresql_role" "my_role" {
      name     = "test_role"
    }

.. note::

  For the full documentation of the ``Aiven provider`` refer to `Aiven provider documentation <https://registry.terraform.io/providers/aiven/aiven/latest/docs>`_.

  For the full list of resources availabe in ``PostgreSQL provider`` refer to `PostgreSQL provider documentation <https://registry.terraform.io/providers/cyrilgdn/postgresql/latest/docs>`_.

