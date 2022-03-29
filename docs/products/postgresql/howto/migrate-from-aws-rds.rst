Migrate from RDS PostgreSQL® to Aiven PostgreSQL® with Aiven CLI and ``aiven-db-migrate``
===========================================================================================

``avn`` Aiven CLI simplifies PostgreSQL database migration with ``aiven-db-migrate`` without down time.
The ``aiven-db-migrate`` tool is an open source project available on `GitHub <https://github.com/aiven/aiven-db-migrate>`_, and it is the preferred way to perform the migration. 

``aiven-db-migrate`` performs a schema dump and migration first to ensure schema compatibility.

It supports both logical replication, and using a dump and restore process. 
Logical replication is the default method which keeps the two databases synchronized until the replication is interrupted. 
If the preconditions for logical replication are not met for a database, the migration falls back to using ``pg_dump``.


Requirements
------------

To perform a migration with ``aiven-db-migrate``:
    
* The source server needs to be publicly available or accessible via a virtual private cloud (VPC) peering connection between the private networks.

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
``SRC_USERNAME``        Username for source PostgreSQL connection
``SRC_PASSWORD``        Password for source PostgreSQL connection
``DEST_PG_NAME``        Name of the Aiven destination PostgreSQL service
``DEST_PG_PLAN``        Aiven plan for the Aiven destination PostgreSQL service
==================      =======================================================================
  
.. Warning::
    Running a logical replication migration twice on the same cluster will create duplicate data. Logical replication also has `limitations <https://www.postgresql.org/docs/current/logical-replication-restrictions.html>`_ on what it can copy.

Perform the migration
---------------------

1. Set the ``wal_level`` to ``logical`` on source database.

To review the current ``wal_level``, run the following command on the source cluster via ``psql``::

    show wal_level;

.. _pg_migrate_wal:

If you have not enabled logical replication on RDS already, the following instructions shows how to set the ``rds.logical_replication`` parameter to ``1`` (true) in the parameter group.

    Create a parameter group for your RDS database.

    .. image:: /images/products/postgresql/migrate-rds-pg-parameter-group.png
        :alt: RDS PostgreSQL parameter group

    Set the ``rds.logical_replication`` parameter to ``1`` (true) in the parameter group

    .. image:: /images/products/postgresql/migrate-rds-pg-parameter-value.png
        :alt: RDS PostgreSQL parameter value

    Modify Database options to use the new DB parameter group - ``RDS`` -> ``Databases`` -> ``Modify``

    .. image:: /images/products/postgresql/migrate-rds-pg-parameter-modify.png
        :alt: RDS PostgreSQL parameter modify

.. Warning::
    Apply immediately or reboot is required to see configuration change reflected to ``wal_level``

    

2. If you don't have an Aiven for PostgreSQL database yet, run the following command to create a couple of PostgreSQL services via :doc:`../../../tools/cli` substituting the parameters accordingly::

    avn service create -t pg -p DEST_PG_PLAN DEST_PG_NAME

3. Once logged in into the destination Aiven for PostgreSQL service, execute the following command via ``psql`` to enable the ``aiven_extras`` extension::
 
    psql postgres://avnadmin:PASSWORD@HOSTNAME:PORT/defaultdb?sslmode=require
    CREATE EXTENSION aiven_extras CASCADE;

.. Note::
    Aiven PostgreSQL has ``wal_level`` set to ``logical`` by default


4. Set the migration details via :doc:`../../../tools/cli` substituting the parameters accordingly::

    avn service update -c migration.host=SRC_HOSTNAME \
    -c migration.port=SRC_PORT \
    -c migration.ssl=true \
    -c migration.username=SRC_USERNAME \
    -c migration.password=SRC_PASSWORD \
    -c migration.dbname=postgres \
    -c migration.ignore_dbs=postgres,rdsadmin \
    DEST_PG_NAME

5. Check the migration status via :doc:`../../../tools/cli`::

    avn --show-http service migration-status DEST_PG_NAME --project PROJECT_NAME

.. Note::
    Please note you may not see migration status updated immediately, run this command multiple times to see status changes.


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
    Once migration is completed successfully, unused replications should be removed.



Migrate using ``aiven-db-migrate`` directly
-------------------------------------------

You can run ``aiven-db-migrate`` directly to see verbose logging of the migration process by running::

    pg_migrate -s "postgres://SRC_USERNAME:SRC_PASSWORD@SRC_HOSTNAME/postgres?sslmode=require" -t "postgres://avnadmin:DST_PASSWORD@DST_HOSTNAME:DST_PORT/defaultdb?sslmode=require" -f rdsadmin,postgres

After migration completed successfully, you should `remove unused replications <https://developer.aiven.io/docs/products/postgresql/howto/setup-logical-replication.html#remove-unused-replication-setup>`_.

By default, the ``aiven-db-migrate`` tool migrates all the tables including extension tables such as ``spatial_ref_sys`` 
from ``postgis`` extension.

There will be a feature/fix to allow skip extension tables in the future.

At the moment the workaround is to use skip-table::

    pg_migrate -d -v -s "postgres://SRC_USERNAME:SRC_PASSWORD@SRC_HOSTNAME/postgres?sslmode=require" -t "postgres://avnadmin:DST_PASSWORD@DST_HOSTNAME:DST_PORT/defaultdb?sslmode=require" -f "rdsadmin,postgres" --skip-table spatial_ref_sys