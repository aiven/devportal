Migrate
=========

An external PostgreSQL database can be migrated into Aiven using the `Aiven-db-migrate <https://github.com/aiven/aiven-db-migrate>`_ tool supporting both logical replication as well as dump and restore process.


Logical replication is the default method, as once successful, this keeps the two databases synchronised until the replication is interrupted. If the preconditions for logical replication are not met for a database, the migration falls back to using ``pg_dump``.

Regardless of the migration method used, the migration tool first performs a schema dump and migration to ensure schema compatibility.

**Note**: Logical replication also works when migrating from AWS RDS PostgreSQL 10+. Google Cloud Platform's PostgreSQL for CloudSQL does not support logical replication.


Migration Requirements
----------------------

A successful migration to Aiven PostgreSQL has several requirements in terms of versioning and network access:

* Source Database being on PostgreSQL version 10 or newer
* Source server publicly available or accessible via virtual private cloud (VPC) peering connection
* User account with access to the destination cluster from an external IP, as configured in ``pg_hba.conf`` on the source cluster

Additionally, for **logical** replication the following need to be fulfilled:

* Credentials with superuser access to the source cluster or the ``aiven-extras`` extension installed on it
* An available replication slot on the destination cluster for each database migrated from the source cluster
* Set the ``wal_level`` on the source cluster to ``logical``. To check this setting, run the following command on the source cluster::

  $ show wal_level;

If necessary, run the following command in ``psql`` and then reload the PostgreSQL configuration::

  $ ALTER SYSTEM SET wal_level = logical;

**Note**: If you are migrating from an AWS RDS PostgreSQL cluster, you have to set the ``rds.logical_replication`` parameter to 1 (true) in the parameter group.


Enable ``aiven_extras`` Extension on the Target Database
----------------------------------------------------------------------------------------
The ``aiven_extras`` extension is required to perform the migration. Once the target PostgreSQL instance has `been created  <create.html>`_ we can connect via `Command Line Interface <../../tools/cli.html>`_

.. code :: bash

  $ avn service cli pg-demo

The extension can be enabled with::

  $ CREATE EXTENSION aiven_extras CASCADE;

Start the Migration
----------------------

The migration can be started with::

  $ avn service update                          \
    -c migration.host=<host>                    \
    -c migration.port=<port>                    \
    -c migration.ssl=true                       \
    -c migration.username=<user>                \
    -c migration.password=<pass>                \
    <tgt_instance_name>

Substitute the ``<host>``, ``<port>``, ``<user>>``, ``<password>`` parameters with the appropriated values pointing to your source PostgreSQL instance. Also replace the ``<tgt_instance_name>`` parameter with the Aiven PostgreSQL target instance.

Migration Parameters
``````````````````````````

The updated list of parameters available for the migration is available with the following command browsing to the ``postgres`` section ::

  $ avn service types -v


The following table contains a summary of the available parameters:


+-----------------------------+-------------------------------------------------------+--------------+
| Parameter Name              | Description                                           | Data Type    |
+-----------------------------+-------------------------------------------------------+--------------+
|``--remove-option migration``| Removes the Migration job                                            |
+-----------------------------+-------------------------------------------------------+--------------+
|``-c migration.dbname``      | Database name for bootstrapping the initial connection| string       |
+-----------------------------+-------------------------------------------------------+--------------+
|``-c migration.host``        | Hostname or IP address of the server                  | string       |
|                             | where migrating data from                             |              |
+-----------------------------+-------------------------------------------------------+--------------+
|``-c migration.port``        | Port number of the server where migrating data from   | integer      |
+-----------------------------+-------------------------------------------------------+--------------+
|``-c migration.ssl``         | The server where migrating data from is secure        |boolean       |
|                             |                                                       |(default=True)|
+-----------------------------+-------------------------------------------------------+--------------+
|``-c migration.username``    | User name for authentication with the server          | string       |
|                             | where migrating data from                             |              |
+-----------------------------+-------------------------------------------------------+--------------+
|``-c migration.password``    | Password for authentication with the server           | string       |
|                             | where migrating data from                             |              |
+-----------------------------+-------------------------------------------------------+--------------+


Check Migration Status
----------------------

The migration status can be checked with the following command::

  $ avn service migration-status pg-example-dst \
      --show-http

Remove Logical Replication
---------------------------------

The migration configuration can be removed with ::

  $ avn service update     \
      --remove-option migration \
      pg-example-dst

This removes all logical replication-related objects from both source and destination cluster, so it effectively stops the logical replication. This has no effect for the ``pg_dump`` method, since it is a one-time operation.

**Note** that removing a migration configuration can leave the destination cluster in an inconsistent state, depending on the state of the migration procedure when the removal is triggered. The states that are considered safe are ``done`` for the ``pg_dump`` method and ``syncing`` for ``logical replication``.

While running, both migration methods are still copying data from the source cluster to the destination, so stopping the process will probably leave some tables only partially moved or missing.

**Note**: Running a logical replication migration twice on the same cluster will create duplicate data. Logical replication also has some `limitations <https://www.postgresql.org/docs/12/logical-replication-restrictions.html>`_ on what it will copy.
