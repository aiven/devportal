Restrict access to databases or tables in Aiven for PostgreSQL®
===============================================================
This article shows how you can restrict access to Aiven for PostgreSQL® databases and tables by setting up read-only permissions for specific user's roles.

Set read-only access in a schema
--------------------------------
1. Modify default permissions for a user's role in a particular schema.

.. code-block:: bash

   alter default privileges for role name_of_role in schema name_of_schema YOUR_GRANT_OR_REVOKE_PERMISSIONS

2.  Apply the new read-only access setting to your existing database objects that uses the affected schema.

.. code-block:: bash

   grant select on all tables in schema name_of_schema to NAME_OF_READ_ONLY_ROLE

Set read-only access in a database
----------------------------------
You can set up the read-only access for a specific user's role in a particular database.

1. Create a new database which will be used as a template ``create database ro_<name>_template...``
2. For the new template database, set permissions and roles that you want as default ones in the template.
3. When creating a new database, use ``create database NAME with template = 'ro_<name>_template'``
