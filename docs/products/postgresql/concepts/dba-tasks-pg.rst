Perform DBA-type tasks in Aiven for PostgreSQL
==============================================

Aiven doesn't allow superuser access to Aiven PostgreSQL services. However, most DBA-type actions can still be achieved using a different method.

``avnadmin`` user privileges
----------------------------

By default, in every PostgreSQL instance, an ``avnadmin`` database user is created, with permissions to perform most of the usual DB management operations, for example it can manage:

* Databases (``CREATE DATABASE``, ``DROP DATABASE``)
* Database users (``CREATE USER/ROLE``,`` DROP USER/ROLE``)
* Extensions (``CREATE EXTENSION``), check out the list of :doc:`available extensions <../reference/list-of-extensions>`
* Access permissions (``GRANT``, ``REVOKE``)
* Logical replication with the ``REPLICATION`` privilege

.. Tip::
    You can also manage databases and users in the Aiven web console or though our :doc:`REST API <../../../tools/api/index>`.

``aiven_extras`` extension
--------------------------

The ``aiven_extras`` extension, developed and maintained by Aiven, enables the ``avnadmin`` to perform superuser-like functionalities like:

* Manage `substriptions <https://www.postgresql.org/docs/current/catalog-pg-subscription.html>`_
* Manage ``auto_explain`` `functionality <https://www.postgresql.org/docs/current/auto-explain.html>`_
* Manage `publications <https://www.postgresql.org/docs/current/sql-createpublication.html>`_
* :doc:`Claim public schema ownership <../howto/claim-public-schema-ownership>`

You can install the ``aiven_extras`` extension executing the following command with the ``avnadmin`` user::

    CREATE EXTENSION aiven_extras CASCADE;

For more information about ``aiven_extras`` check the dedicated `github repository <https://github.com/aiven/aiven-extras>`_
