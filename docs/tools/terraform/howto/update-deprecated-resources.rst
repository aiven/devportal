Update deprecated resources 
============================

Use the following steps to migrate from resources that have been deprecated or renamed without destroying existing resources.

.. tip::
    Backup your Terraform state file ``terraform.tfstate`` to use in the case of a rollback.

In the following example, the ``aiven_database`` field is migrated to the new ``aiven_pg_database`` field for an Aiven for PostgreSQL® service. 

1. Replace references to the deprecated field with the new field. In the following file ``aiven_database`` was replaced with ``aiven_pg_database``:
   
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

2. View a list of all resources in the state file:

   .. code::

      terraform state list

3. Remove the resource from the control of Terraform:

   .. code::

      terraform state rm <DEPRECATED_RESOURCE>

   .. tip::
     
      Use the ``-dry-run`` flag to preview the changes without applying them.

4. Add the resource back to Terraform by importing it as a new resource:

   .. code::
   
     terraform import <NEW_RESOURCE> project_name/service_name/db_name

5. Check that the import is going to run as you expect:

   .. code::

      terraform plan

6. Apply the new configuration:

   .. code::
     
      terraform apply
