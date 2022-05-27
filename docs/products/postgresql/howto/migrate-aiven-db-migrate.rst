
Migrate to Aiven for PostgreSQL® with ``aiven-db-migrate``
===============================================================

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


1. If you don't have an Aiven for PostgreSQL database yet, run the following command to create a couple of PostgreSQL services via :doc:`../../../tools/cli` substituting the parameters accordingly::

    avn service create -t pg -p DEST_PG_PLAN DEST_PG_NAME

2. Once logged in into the destination Aiven for PostgreSQL service, execute the following command via ``psql`` to enable the ``aiven_extras`` extension::
 
    psql postgres://avnadmin:PASSWORD@HOSTNAME:PORT/defaultdb?sslmode=require
    CREATE EXTENSION aiven_extras CASCADE;

.. Note::
    Aiven for PostgreSQL has ``wal_level`` set to ``logical`` by default

3. Set the ``wal_level`` to ``logical`` on source database.

:doc:`./logical-replication-aws-aurora`

:doc:`./logical-replication-aws-rds`

:doc:`./logical-replication-gcp-cloudsql`

To review the current ``wal_level``, run the following command on the source cluster via ``psql``::

    show wal_level;

.. _pg_migrate_wal:


Perform the migration
---------------------
.. Warning::
    Running a logical replication migration twice on the same cluster will create duplicate data. Logical replication also has `limitations <https://www.postgresql.org/docs/current/logical-replication-restrictions.html>`_ on what it can copy.

Run ``aiven-db-migrate`` library module directly
''''''''''''''''''''''''''''''''''''''''''''''''
::

    python3 -m aiven_db_migrate.migrate pg -d \
    -s postgres://SRC_USERNAME:SRC_PASSWORD@SRC_HOSTNAME:SRC_PORT \
    -t postgres://DST_USERNAME:DST_PASSWORD@DST_HOSTNAME:DST_PORT/DST_DBNAME?sslmode=require \
    --max-replication-lag 1 --stop-replication -f DB_TO_SKIP

**Variables**

==================      =======================================================================
Variable                Description
==================      =======================================================================
``SRC_USERNAME``        Username for source PostgreSQL connection
``SRC_PASSWORD``        Password for source PostgreSQL connection
``SRC_HOSTNAME``        Hostname for source PostgreSQL connection
``SRC_PORT``            Port for source PostgreSQL connection
``DST_USERNAME``        Username for destination PostgreSQL connection
``DST_PASSWORD``        Password for destination PostgreSQL connection
``DST_HOSTNAME``        Hostname for destination PostgreSQL connection
``DST_PORT``            Port for destination PostgreSQL connection
``DST_DBNAME``          Bootstrap database name for destination PostgreSQL connection
==================      =======================================================================

**Flags**

=========================================   =======================================================================
Flag                                        Description
=========================================   =======================================================================
``-d, --debug``                             Enable debug logging 
``-f, --filtered-db``                       Password for source PostgreSQL connection
``--stop-replication``                      By default logical replication will be left running on both source and target database
``--max-replication-lag``                   Max replication lag in bytes to wait for, by default no wait, this parameter is required when using --stop-replication
=========================================   =======================================================================

* ``-d`` is highly recommended when running migration to see details of the migration process.

* For live migration ``--stop-replication`` and ``--max-replication-lag`` flags are not needed to keep logical replication running.
 
* The ``aiven-db-migrate`` tool migrates all the tables including extension tables such as ``spatial_ref_sys`` from ``postgis`` extension.  There will be a feature/fix to allow skip extension tables in the future.  At the moment the workaround is to use ``--skip-table`` flag::

    --skip-table spatial_ref_sys


OR
''

Run ``aiven-db-migrate`` using ``avn`` CLI  
''''''''''''''''''''''''''''''''''''''''''

* Set the migration details via :doc:`../../../tools/cli` substituting the parameters accordingly::

    avn service update -c migration.host=SRC_HOSTNAME   \
        -c migration.port=SRC_PORT                      \
        -c migration.ssl=true                           \
        -c migration.username=SRC_USERNAME              \
        -c migration.password=SRC_PASSWORD              \
        -c migration.dbname=DST_DBNAME                  \
        -c migration.ignore_dbs=DB_TO_SKIP              \
        DEST_PG_NAME

.. Note::
    Using avn CLI shows limited status output, to troubleshoot failures please run ``aiven-db-migrate`` directly from the above instructions.

**Variables**

==================      =======================================================================
Variable                Description
==================      =======================================================================
``DEST_PG_PLAN``        Aiven plan for the Aiven destination PostgreSQL service
``PROJECT_NAME``        Aiven project for the Aiven destination PostgreSQL service
==================      =======================================================================

* Check the migration status via :doc:`../../../tools/cli`::

    avn --show-http service migration-status DEST_PG_NAME --project PROJECT_NAME


.. Note::
    There maybe delay for migration status to update the current progress, keep running this command to see the most up-to-date status.


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


* Remove the configuration from the destination service via :doc:`../../../tools/cli` Make sure your migration process is in one of the following state when triggering the removal: ``done`` for the ``pg_dump`` method, and ``syncing`` for logical replication. Otherwise, removing a migration configuration can leave the destination cluster in an inconsistent state. ::

    avn service update --remove-option migration DEST_PG_NAME


This command removes all logical replication-related objects from both source and destination cluster. This stops the logical replication which has no effect for the ``pg_dump`` method as it is a one-time operation.
    
.. Warning::
    Don't stop the process while running as both the logical replication and pg-dump/pg-restore methods are copying data from the source to the destination cluster.
    Once migration is completed successfully, unused replications should be removed.