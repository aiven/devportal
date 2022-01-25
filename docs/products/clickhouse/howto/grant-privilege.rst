Grant privileges
==================

ClickHouse supports **Role Based Access Control** model and allows configuring access privileges by using SQL statements. You can either :doc:`use a query editor <use-query-editor>` or rely on :doc:`the command-line interface <install-cli>`.

Below you can find examples of how to create roles and grant privileges. In the ClickHouse documentation you will find  `detailed documentation for access rights <https://clickhouse.com/docs/en/operations/access-rights/>`_.

Create a new role
------------------

In order to create a new role with name `auditor` execute the following command::

    CREATE ROLE auditor;

Find more information `on role creation here <https://clickhouse.com/docs/en/sql-reference/statements/create/role/>`_.

Grant permissions
-------------------

It is possible to grant permissions both to specific roles and to particular users. The grants can be also granular, targeting specific databases, tables, columns or rows.

For example, the request below will grant permissions to select data from `transactions` database to a role named `auditor`::

    GRANT SELECT ON transactions.* TO auditor;

You can narrow the grants to a specified table::

    GRANT SELECT ON transactions.expenses TO auditor;

Or particular columns of a table::

    GRANT SELECT(date,description,amount) ON transactions.expenses TO auditor

Granting roles `auditor` and `external` to several users::

    GRANT auditor, external TO Mary.Anderson, James.Miller;

Allow creation of new users::

    GRANT CREATE USER ON transactions.* TO administrator

You can grant a variety of privileges, find `the full list in ClickHouse documentation <https://clickhouse.com/docs/en/sql-reference/statements/grant/#grant-privileges>`_.



.. note ::

    You can grant permissions to a table, which does not yet exist.

.. note ::

    User can grant permissions according to their privileges. If the user lacks permissions for requested operation, you will receive an exception `Not enough privileges.`

.. warning ::

    Privileges are not revoked when a table or a database is removed. They continue to be active for any new table/database that is created with the same name.

Find full list of supported functionality related `to grants in ClickHouse documentation <https://clickhouse.com/docs/en/sql-reference/statements/grant/>`_ .

Set role
------------------

A single user can be assigned different roles, either individually or simultaneously.

::

    SET ROLE auditor;

You can also specify a role to be activated by default when user logs in::

    SET DEFAULT ROLE auditor, external TO Mary.Anderson, James.Miller;

Delete role
-------------------

Once you don't need a role, it can be removed::

    DROP ROLE auditor;

Revoke permissions
-------------------

You can remove all or partial privileges from users or roles::

    REVOKE SELECT ON transactions.expenses FROM Mary.Anderson;

You can revoke all privileges on a table or database simultaneously::

    REVOKE ALL PRIVILEGES ON database.table FROM external;

https://clickhouse.com/docs/en/sql-reference/statements/revoke/

See current permissions
-----------------------

All available grants, users and roles can be seen by running the following commands::

    SHOW GRANTS;

::

    SHOW USERS;

::

    SHOW ROLES;


See users and roles in console
--------------------------------

You can also see the users, their roles and permissions in the  `Aiven web console <https://console.aiven.io/>`_. Find them in the *Users & Roles* tab of your service. Next to every user there is a button **View Details & Grants** which will show a list of all grants for a user.





====


