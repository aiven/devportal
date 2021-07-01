About ``aiven-db-migrate``
==========================

The ``aiven-db-migrate`` tool is the recommended approach for migrating your PostgreSQL to Aiven. It supports both logical replication and also using a dump and restore process. Find out more about the tool `on GitHub <https://github.com/aiven/aiven-db-migrate>`_.

Logical replication is the default method and once successfully set up, this keeps the two databases synchronized until the replication is interrupted. If the preconditions for logical replication are not met for a database, the migration falls back to using ``pg_dump``.

Regardless of the migration method used, the migration tool first performs a schema dump and migration to ensure schema compatibility.

.. Note::
    Logical replication also works when migrating from AWS RDS PostgreSQL 10+. Google Cloud Platform's PostgreSQL for CloudSQL does not support logical replication.

.. _aiven-db-migrate-migration-requirements:

Migration requirements
''''''''''''''''''''''

The following are the two basic requirements for a migration:

1. the source server is publicly available or there is a virtual private cloud (VPC) peering connection between the private networks
2. a user account with access to the destination cluster from an external IP, as configured in ``pg_hba.conf`` on the source cluster is present

Additionally to perform a **logical replication**, the following need to be valid:

3. PostgreSQL version 10 or newer
4. Credentials with superuser access to the source cluster or the ``aiven-extras`` extension installed (see also: `Aiven Extras on GitHub <https://github.com/aiven/aiven-extras>`_)

.. Note::
    The ``aiven_extras``  extension allows you to perform publish/subscribe-style logical replication without a superuser account, and it is preinstalled on Aiven for PostgreSQL servers.

* An available replication slot on the destination cluster for each database migrated from the source cluster.
* ``wal_level`` setting on the source cluster to ``logical``.

Migration pre-checks
''''''''''''''''''''

The ``aiven-db-migrate`` migration tool checks the following requirements before it starts the actual migration:

1. A connection can be established to both source and target servers
2. The source and target server are not the same
3. A connection can be established to all source databases, ignoring ``template0``, ``template1``, and admin databases
4. There is enough disk space on the target for 130% of the total size of the source databases (ignoring ``template0``, ``template1``, and admin databases)
5. There are at least as many free logical replication slots as there are databases to migrate
6. A connection can be established to any target database that already exists on both source and target servers
7. The target version is the same as or newer than the source version
8. All languages installed in the source are available in the target
9. All extensions in the source are installed or available in the target
10. Source extensions not installed in the target can be installed:

    - by connecting as a superuser
    - without requiring superuser access
    - by inclusion in the allowed extensions list
    - by being a trusted extension (for PostgreSQL 13 and newer)

11. In addition, for using the logical replication method:

    - The source version is PostgreSQL 10 or newer
    - The source ``wal_level`` is set to ``logical``
    - The user connecting to the source has superuser access or the ``aiven_extra`` extension is or can be installed on each database

Next steps
''''''''''

There's a detailed guide for performing the migration: :doc:`../howto/migrate-aiven-db-migrate`
