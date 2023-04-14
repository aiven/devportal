Upgrade the Aiven Terraform Provider from v3 to v4
===================================================

The Aiven Terraform Provider version 4.0.0 was released in February 2023. If you previously upgraded the Terraform provider from version 2 to version 3, then no other actions are needed. Otherwise, this article has information on how to upgrade to version 4. 

Major changes in v4
''''''''''''''''''''

Aiven Terraform Provider has a `detailed changelog <https://github.com/aiven/terraform-provider-aiven/blob/main/CHANGELOG.md>`_ but the main changes in v4 are:

- schema fields use strict types instead of string
- support for strict types in diff functions

These deprecated resources have also been removed:

- ``aiven_database``
- ``aiven_service_user``
- ``aiven_vpc_peering_connection``
- ``aiven_flink_table``
- ``aiven_flink_job``

Upgrade Aiven Terraform provider
''''''''''''''''''''''''''''''''

You update the Aiven Terraform Provider by editing the providers block of your script. If the version was already set to ``>= 3.0.0`` then the upgrade is automatic.

.. code:: terraform
    
    terraform {
      required_providers {
        aiven = {
          source  = "aiven/aiven"
          version = ">= 4.0.0"
        }
      }
    }

.. tip::
    You might need to run ``terraform init -upgrade`` for the provider version upgrade to take place.
    
Update resource syntax
''''''''''''''''''''''''

The deprecated fields listed in the major changes were removed. The following example shows how to migrate these fields safely without destroying existing resources.

.. tip::
    Backup your Terraform state file ``terraform.tfstate`` (if available), just in case of potential rollback.


In this example, the ``aiven_database`` field is updated to the service-specific ``aiven_pg_database`` field for an Aiven for PostgreSQL® service. A list of all resources is available in the `Aiven Operator for Terraform documentation <https://registry.terraform.io/providers/aiven/aiven/latest/docs/resources/>`_.

1. Update ``aiven_database`` references to ``aiven_pg_database`` as in this example file:

.. code::

    - resource "aiven_database" "mydatabase" {
        project       = aiven_project.myproject.project
        service_name  = aiven_pg.mypg.service_name
        database_name = "<DATABASE_NAME>"
    }


    + resource "aiven_pg_database" "mydatabase" {
        project       = aiven_project.myproject.project
        service_name  = aiven_pg.mypg.service_name
        database_name = "<DATABASE_NAME>"
    }

2. View a list of all resources in the state file::

    terraform state list | grep azure

3. Remove the resource from the control of Terraform::

    terraform state rm aiven_database

.. tip::
    Use the ``-dry-run`` flag to preview the changes without applying them.

4. Add the resource back to Terraform by importing it as a new resource::

    terraform import aiven_pg_database project_name/ ???

5. Check that the import is going to run as you expect::

    terraform plan

6. Apply the new configuration::

    terraform apply

You can follow these steps to update the other resources that were deprecated in version 3 of the provider.
