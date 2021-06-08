Migrate data to Aiven for PostgreSQL with ``aiven-db-migrate``
==============================================================

This article describes how to migrate a PostgreSQL cluster from an external source to an Aiven for PostgreSQL service using the `aiven-db-migrate <https://github.com/aiven/aiven-db-migrate>`_ tool. To know more about how the tool works, please check :doc:`../concepts/aiven-db-migrate`

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

==================      =======================================================================
Variable                Description
==================      =======================================================================
``SRC_HOSTNAME``        Hostname for source PostgreSQL connection
``SRC_PORT``            Port for source PostgreSQL connection
``SRC_DATABASE``        Database Name for source PostgreSQL connection
``SRC_USERNAME``        Username for source PostgreSQL connection
``SRC_PASSWORD``        Password for source PostgreSQL connection
``SRC_SSL``             SSL setting for source PostgreSQL connection
``DEST_PG_NAME``        Name of the destination Aiven PostgreSQL service
``DEST_PG_PLAN``        Aiven Plan for the destination Aiven PostgreSQL service
==================      =======================================================================

Check ``wal_level`` setting
'''''''''''''''''''''''''''

As per :doc:`Migration Requirements<../concepts/aiven-db-migrate>`, to perform a migration using ``aiven-db-migrate``, the ``wal_level`` needs to be set to ``logical``. To review the current ``wal_level`` run the following command on the source cluster via ``psql``::

    show wal_level;

If the output is not ``logical``, run the following command in ``psql`` and then reload the PostgreSQL configuration::

    ALTER SYSTEM SET wal_level = logical;

.. Note::
    If you are migrating from an AWS RDS PostgreSQL cluster, you have to set the ``rds.logical_replication`` parameter to ``1`` (true) in the parameter group.

Check the Migration Configuration Options
'''''''''''''''''''''''''''''''''''''''''

The following command using the :doc:`../../../tools/cli` to see the available configuration options for migration::

    avn service types -v

The output includes::

  ----
  Service type 'pg' options:

    Remove migration

       => --remove-option migration

    Database name for bootstrapping the initial connection

       => -c migration.dbname=<string>

    Hostname or IP address of the server where to migrate data from

       => -c migration.host=<string>

    Password for authentication with the server where to migrate data from

       => -c migration.password=<string>

    Port number of the server where to migrate data from

       => -c migration.port=<integer>

    The server where to migrate data from is secured with SSL

       => -c migration.ssl=<boolean> (default=True)

    User name for authentication with the server where to migrate data from

       => -c migration.username=<string>

  ----



Perform the Migration
'''''''''''''''''''''

The following is the migration process:

1. If you don't have a PostgreSQL database already, run the following commands to create a couple of PostgreSQL services via :doc:`../../../tools/cli` substituting the parameters accordingly::

    avn service create -t pg -p DEST_PG_PLAN DEST_PG_NAME

2. Once logged on the destination Aiven PostgreSQL service execute the following command via ``psql`` to enable the ``aiven_extras`` extension::

    CREATE EXTENSION aiven_extras CASCADE;

3. Configure the migration details via :doc:`../../../tools/cli` substituting the parameters accordingly::

    avn service update -c migration.host=SRC_HOSTNAME   \
        -c migration.port=SRC_PORT                      \
        -c migration.ssl=SRC_SSL                        \
        -c migration.username=SRC_USERNAME              \
        -c migration.password=SRC_PASSWORD              \
        DEST_PG_NAME



4. Check the migration status via :doc:`../../../tools/cli`::

    avn --show-http service migration-status DEST_PG_NAME --project test

The command output should be similar to the following stating that the ``pg_dump`` migration of the ``defaultdb`` database is ``done`` and the logical ``replication`` of the ``has_aiven_extras`` database is sincing``::

    -----Response Begin-----
    {
        "migration": {
            "error": null,
            "method": "",
            "status": "done"
        },
        "migration_detail": [
            {
            "dbname": "has_aiven_extras",
            "error": null,
            "method": "replication",
            "status": "syncing"
            },
            {
            "dbname": "defaultdb",
            "error": null,
            "method": "pg_dump",
            "status": "done"
            }
        ]
    }
    -----Response End-----
    STATUS  METHOD  ERROR
    ======  ======  =====
    done            null



.. Note::
    The overall ``method`` field is left empty due to the mixed methods used to migrate each database.


5. Remove the configuration from the destination service via :doc:`../../../tools/cli`::

    avn service update --remove-option migration DEST_PG_NAME


This command removes all logical replication-related objects from both source and destination cluster, so it effectively stops the logical replication. This has no effect for the ``pg_dump`` method, since it is a one-time operation.

.. Warning::
    Removing a migration configuration can leave the destination cluster in an inconsistent state, depending on the state of the migration procedure when the removal is triggered. The states that are considered safe are ``done`` for the ``pg_dump`` method and ``syncing`` for logical replication.

While running, both migration methods are still copying data from the source cluster to the destination. Thus stopping the process will probably leave some tables only partially moved or missing.

.. Note::
    Running a logical replication migration twice on the same cluster will create duplicate data. Logical replication also has some `limitations <https://www.postgresql.org/docs/current/logical-replication-restrictions.html>`_ on what it will copy.
