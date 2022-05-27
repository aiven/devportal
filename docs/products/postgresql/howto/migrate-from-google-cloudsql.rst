Migrate from google cloud SQL PostgreSQL® to Aiven for PostgreSQL® with ``aiven-db-migrate``
============================================================================================

``avn`` Aiven CLI simplifies PostgreSQL® database migration with ``aiven-db-migrate`` without down time.
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

1. If you don't have an Aiven for PostgreSQL database yet, run the following command to create a couple of PostgreSQL services via :doc:`../../../tools/cli` substituting the parameters accordingly::

    avn service create -t pg -p DEST_PG_PLAN DEST_PG_NAME

2. Once logged in into the destination Aiven for PostgreSQL service, execute the following command via ``psql`` to enable the ``aiven_extras`` extension::
 
    psql postgres://avnadmin:PASSWORD@HOSTNAME:PORT/defaultdb?sslmode=require
    CREATE EXTENSION aiven_extras CASCADE;

.. Note::
    Aiven PostgreSQL has ``wal_level`` set to ``logical`` by default

3. Set the ``wal_level`` to ``logical`` on source database.

To review the current ``wal_level``, run the following command on the source cluster via ``psql``::

    show wal_level;

.. _pg_migrate_wal_cloudsql:

1. If you have not enabled logical replication on Cloud SQL PostgreSQL already, the following instructions shows how to set the ``cloudsql.logical_decoding`` parameter to ``On``.

   Set logical replication parameter for your Cloud SQL PostgreSQL database.

    .. image:: /images/products/postgresql/migrate-cloudsql-flags.png
        :alt: Cloud SQL PostgreSQL flags

2. Authorize Aiven PostgresSQL IP to Cloud SQL's allowed network CIDR.

    .. image:: /images/products/postgresql/migrate-cloudsql-network.png
        :alt: Cloud SQL PostgreSQL network


3. Set replication role to PostgreSQL user (or the user will be used for migration) in Cloud SQL PostgreSQL::

    ALTER ROLE postgres REPLICATION;


.. include:: aiven-db-migrate.rst