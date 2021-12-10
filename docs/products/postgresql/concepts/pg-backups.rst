PostgreSQL backups
==================

Aiven for PostgreSQL databases are automatically backed up, with **full backups** made daily, and **write-ahead logs (WAL)** copied at 5 minute intervals, or for every new file generated. All backups are encrypted using ``pghoard``, an open source tool developed and maintained by Aiven, that you can find `on GitHub <https://github.com/aiven/pghoard>`_.

The time of day when the daily backups are made is initially randomly selected, but can be customised by setting the ``backup_hour`` and ``backup_minute`` advanced parameters, see :doc:`../reference/list-of-advanced-params`.

Backup retention time by plan
-----------------------------

The number of stored backups and the backup retention time depends on the service plan that you have selected.

.. list-table::
    :header-rows: 1

    * - Plan Type
      - Backup Retention Time
    * - Hobbyist
      - None
    * - Startup
      - 2 days
    * - Business
      - 14 days
    * - Premium
      - 30 days


Differences between logical and full backups
----------------------------------------------

**Full backups** are version-specific binary backups that, when combined with WAL, allow consistent recovery to a point in time (PITR). **Logical backups** contain the SQL statements used to create the database schema and fill it with data, and are not tied to a specific version.

.. list-table::
    :header-rows: 1

    * - Feature
      - Full backup
      - Logical backup
    * - Version-specific
      - Full backups can be restored with the same PostgreSQL version as the backup was created from
      - Cross-version compatibility
    * - Database selection
      - The entire PostgreSQL instance is backed up. No option to backup (or restore) as single database
      - Single database objects can be backed up. Easy to backup and restore any item down to a single table
    * - Data
      - Contains uncommitted transactions and deleted and updated rows that have not been cleaned up by the PostgreSQL ``VACUUM`` process
      - Contains only the current committed content of the tables
    * - Indexes
      - Contains all data from indexes
      - Contains the queries needed to recreate indexes
    * - PITR capabilities
      - Previous database status can be restored using the WAL
      - Only "as-of-backup" status can be restored
    * - Restore time
      - Almost instantaneous, restore backup and replay delta WAL files
      - Long restoration process, replay of all SQL statements is needed to generate schema object and insert data

.. Tip::
    The size of backups and the Aiven backup size shown on the Aiven web console differ, in some cases significantly. The backup sizes shown in the Aiven web console are for daily backups, before encryption and compression.

To restore a backup, see :doc:`../howto/restore-backup`.
