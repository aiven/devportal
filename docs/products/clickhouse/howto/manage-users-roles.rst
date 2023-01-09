Manage ClickHouse® service users and roles
==========================================

This article shows you how to create new user accounts for your service and how to manage user roles and permissions for efficiently access control.

Add a new user
--------------

To create a new user account for your service,

1. Log in to the `Aiven web console <https://console.aiven.io/>`_ and select your ClickHouse® service.

#. Select **Users & Roles**.

   This page shows you a list of all the users that are currently available in your service. The default ``avnadmin`` user has all available access grants to the service.

   .. tip::
      To view the roles and grants for any of the listed users, click **View Details & Grants** for that user.

#. Enter a name for the new user and select a role.

   The role that you select defines the access grants that are assigned to the user. For more information on roles, see :ref:`Manage roles and permissions <manage-roles-and-permissions>`.

#. Select **Add User**.

   This creates the new user and shows you a summary of the information.

#. Copy the password on screen to a safe place. It can't be accessed again in future, however it can be reset if needed.

.. _manage-roles-and-permissions:

Manage roles and permissions
----------------------------

ClickHouse® supports a **Role Based Access Control** model and allows you to configure access privileges by using SQL statements. You can either :doc:`use the query editor <query-databases>` or rely on :doc:`the command-line interface <connect-with-clickhouse-cli>`.

This article shows you examples of how to create roles and grant privileges. The ClickHouse documentation includes  `detailed documentation for access rights <https://clickhouse.com/docs/en/operations/access-rights/>`_.

Create a new role
^^^^^^^^^^^^^^^^^

To create a new role named `auditor`, run the following command::

    CREATE ROLE auditor;

You can find more information `on role creation here <https://clickhouse.com/docs/en/sql-reference/statements/create/role/>`_.

Grant permissions
^^^^^^^^^^^^^^^^^

You can grant permissions both to specific roles and to individual users. The grants can be also granular, targeting specific databases, tables, columns, or rows.

For example, the following request grants the `auditor` role permissions to select data from the `transactions` database::

    GRANT SELECT ON transactions.* TO auditor;

You can limit the grant to a specified table::

    GRANT SELECT ON transactions.expenses TO auditor;

Or to particular columns of a table::

    GRANT SELECT(date,description,amount) ON transactions.expenses TO auditor

To grant the `auditor` and `external` roles to several users, run::

    GRANT auditor, external TO Mary.Anderson, James.Miller;

To allow the creation of new users::

    GRANT CREATE USER ON transactions.* TO administrator

There are a variety of privileges that you can grant, and you can find `the full list in the ClickHouse documentation <https://clickhouse.com/docs/en/sql-reference/statements/grant/#privileges>`_.

.. note ::

    You can grant permissions to a table that does not yet exist.

.. note ::

    Users can grant permissions according to their privileges. If the user lacks the required permissions for a requested operation, they receive a `Not enough privileges` exception.

.. warning ::

    Privileges are not revoked when a table or database is removed. They continue to be active for any new table or database that is created with the same name.

You can find the full list of supported functionality related `to grants in the ClickHouse documentation <https://clickhouse.com/docs/en/sql-reference/statements/grant/>`_.

Set roles
^^^^^^^^^

A single user can be assigned different roles, either individually or simultaneously.

::

    SET ROLE auditor;

You can also specify a role to be activated by default when the user logs in::

    SET DEFAULT ROLE auditor, external TO Mary.Anderson, James.Miller;

Delete a role
^^^^^^^^^^^^^

If you no longer need a role, you can remove it::

    DROP ROLE auditor;

Revoke permissions
^^^^^^^^^^^^^^^^^^

Remove all or specific privileges from users or roles::

    REVOKE SELECT ON transactions.expenses FROM Mary.Anderson;

Revoke all privileges to a table or database simultaneously::

    REVOKE ALL PRIVILEGES ON database.table FROM external;

See the ClickHouse documentation `for more information on revoking privileges <https://clickhouse.com/docs/en/sql-reference/statements/revoke/>`_.

Check permissions
^^^^^^^^^^^^^^^^^

Run the following commands to see all available grants, users, and roles::

    SHOW GRANTS;

::

    SHOW USERS;

::

    SHOW ROLES;


Preview users and roles in the console
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also see the users, their roles and permissions in the  `Aiven web console <https://console.aiven.io/>`_. You will find these on the *Users & Roles* tab of your service. Next to every user there is a **View Details & Grants** button that shows you a list of all grants for that user.
