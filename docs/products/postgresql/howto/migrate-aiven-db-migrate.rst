Migrate to Aiven for PostgreSQL® with ``aiven-db-migrate``
===========================================================

The ``aiven-db-migrate`` tool is an open source project available on `GitHub <https://github.com/aiven/aiven-db-migrate>`_, and it is the preferred way to perform the migration. 

``aiven-db-migrate`` performs a schema dump and migration first to ensure schema compatibility.

It supports both logical replication, and using a dump and restore process. 
Logical replication is the default method which keeps the two databases synchronized until the replication is interrupted. 
If the preconditions for logical replication are not met for a database, the migration falls back to using ``pg_dump``.

.. Note::

    You can use logical replication when migrating from AWS RDS PostgreSQL® 10+ and `Google CloudSQL PostgreSQL <https://cloud.google.com/sql/docs/release-notes#August_30_2021>`_.

Requirements
------------

To perform a migration with ``aiven-db-migrate``:
    
* The source server needs to be publicly available or accessible via a virtual private cloud (VPC) peering connection between the private networks.
* You have a user account with access to the destination cluster from an external IP, as configured in ``pg_hba.conf`` on the source cluster.

In order to use the **logical replication** method, you'll need the following:
    
* PostgreSQL® version is 10 or higher.
* Sufficient access to the source cluster (either the ``replication`` permission or the ``aiven-extras`` extension installed). The extension allows you to perform publish/subscribe-style logical replication without a superuser account, and it is preinstalled on Aiven for PostgreSQL servers. See `Aiven Extras on GitHub <https://github.com/aiven/aiven-extras>`_.
* An available replication slot on the destination cluster for each database migrated from the source cluster.

Additional migration configuration options are available, check the :ref:`pg_migration` section of the configuration reference.


Variables
'''''''''

You can use the following variables in the code samples provided:

==================      =======================================================================
Variable                Description
==================      =======================================================================
``SRC_HOSTNAME``        Hostname for source PostgreSQL connection
``SRC_PORT``            Port for source PostgreSQL connection
``SRC_DATABASE``        Database name for source PostgreSQL connection
``SRC_USERNAME``        Username for source PostgreSQL connection
``SRC_PASSWORD``        Password for source PostgreSQL connection
``SRC_SSL``             SSL setting for source PostgreSQL connection
``DEST_PG_NAME``        Name of the Aiven destination PostgreSQL service
``DEST_PG_PLAN``        Aiven plan for the Aiven destination PostgreSQL service
==================      =======================================================================
  
.. Warning::
    Running a logical replication migration twice on the same cluster will create duplicate data. Logical replication also has `limitations <https://www.postgresql.org/docs/current/logical-replication-restrictions.html>`_ on what it can copy.

Perform the migration
---------------------

1. Set the ``wal_level`` to ``logical``

To review the current ``wal_level``, run the following command on the source cluster via ``psql``::

    show wal_level;

.. _pg_migrate_wal:

If the output is not ``logical``, run the following command in ``psql`` and then reload the PostgreSQL configuration::

    ALTER SYSTEM SET wal_level = logical;

.. Note::
    If you are migrating from an AWS RDS PostgreSQL cluster, set the ``rds.logical_replication`` parameter to ``1`` (true) in the parameter group.  If you are migration from a GCP SQL PostgreSQL cluster, set the ``cloudsql.logical_decoding`` flag to ``on`` (as described in the `GCP docs <https://cloud.google.com/sql/docs/postgres/replication/configure-logical-replication>`_)


2. If you don't have an Aiven for PostgreSQL database yet, run the following command to create a couple of PostgreSQL services via :doc:`../../../tools/cli` substituting the parameters accordingly::

    avn service create -t pg -p DEST_PG_PLAN DEST_PG_NAME

3. Once logged in into the destination Aiven for PostgreSQL service, execute the following command via ``psql`` to enable the ``aiven_extras`` extension::

    CREATE EXTENSION aiven_extras CASCADE;

4. Set the migration details via :doc:`../../../tools/cli` substituting the parameters accordingly::

    avn service update -c migration.host=SRC_HOSTNAME   \
        -c migration.port=SRC_PORT                      \
        -c migration.ssl=SRC_SSL                        \
        -c migration.username=SRC_USERNAME              \
        -c migration.password=SRC_PASSWORD              \
        DEST_PG_NAME


5. Check the migration status via :doc:`../../../tools/cli`::

    avn --show-http service migration-status DEST_PG_NAME --project test

You should get the following command output which mentions that the ``pg_dump`` migration of the ``defaultdb`` database is ``done`` and the logical ``replication`` of the ``has_aiven_extras`` database is syncing``::

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


6. Remove the configuration from the destination service via :doc:`../../../tools/cli` Make sure your migration process is in one of the following state when triggering the removal: ``done`` for the ``pg_dump`` method, and ``syncing`` for logical replication. Otherwise, removing a migration configuration can leave the destination cluster in an inconsistent state. ::

    avn service update --remove-option migration DEST_PG_NAME


This command removes all logical replication-related objects from both source and destination cluster. This stops the logical replication which has no effect for the ``pg_dump`` method as it is a one-time operation.
    
.. Warning::
    Don't stop the process while running as both the logical replication and pg-dump/pg-restore methods are copying data from the source to the destination cluster.



Migrate using ``aiven-db-migrate`` directly
-------------------------------------------

The ``aiven-db-migrate`` tool migrates all the tables including extension tables such as ``spatial_ref_sys`` 
from ``postgis`` extension.

There will be a feature/fix to allow skip extension tables in the future.

At the moment the workaround is to use skip-table::

    pg_migrate -d -v -s "SRC" -t "DST" -f "_aiven" --skip-table spatial_ref_sys

