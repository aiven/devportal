Read Only User for PostgreSQL
=============================
In the interest of having users with the least permissions to complete their tasks, one may need a user with read only access to the whole database or a handful of tables. In some cases, we may want this to happen automatically, below are two approaches to complete this task.

All new objects shall have a role with read-only permissions
------------------------------------------------------------
1. Alter the default permissions for the role for the given schema: ``ALTER DEFAULT PRIVILEGES FOR ROLE <target role> IN SCHEMA <schema name> abbreviated_grant_or_revoke``

2.  To update any existing database objects, run the following: ``GRANT SELECT ON ALL TABLES IN SCHEMA <schema name> to <myreadonlyrole>;``

Only certain databases should be read-only for users in a particular role:
==========================================================================
1. Create a new database which will be used as a template ``CREATE DATABASE ro_<name>_template...``
2. Update the standardizable information of the database
3. When creating a new database, use ``CREATE DATABASE <name> WITH TEMPLATE = 'ro_<name>_template'``