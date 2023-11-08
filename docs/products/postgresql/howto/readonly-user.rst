Restrict access to databases or tables in Aiven for PostgreSQL®
===============================================================
This article shows how you can restrict access to Aiven for PostgreSQL® databases and tables by setting up read-only permissions for specific user's roles.

Set read-only access in a schema
--------------------------------
1. Modify default permissions for a user's role in a particular schema.

.. code-block:: bash

   ALTER DEFAULT PRIVILEGES FOR ROLE NAME_OF_ROLE IN SCHEMA NAME_OF_SCHEMA abbreviated_grant_or_revoke

2.  Apply the new read-only access setting to your existing database objects that uses the affected schema.

.. code-block:: bash

   GRANT SELECT ON ALL TABLES IN SCHEMA NAME_OF_SCHEMA to NAME_OF_READ_ONLY_ROLE

Set read-only access in a database
----------------------------------
You can set up the read-only access for a specific user's role in a particular database.

1. Create a new database which will be used as a template ``CREATE DATABASE ro_<name>_template...``
2. Update the standardizable information of the database
3. When creating a new database, use ``CREATE DATABASE <name> WITH TEMPLATE = 'ro_<name>_template'``