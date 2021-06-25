Restore PostgreSQL from a backup
================================

Aiven for PostgreSQL databases can be restored from a backup at any point in time within the **backup retention period**, different per :doc:`plan <../concepts/pg-backups>`. The restore is created via "Forking": a new PostgreSQL instance is created and content from the original database is restored into it.

.. Note::
    Aiven for PostgreSQL doesn't allow a service to be rolled back to a backup in-place since it creates alternative timelines for the database, adding complexity for the user.

To restore a PostgreSQL database:

1. Access the service detail page of the PostgreSQL database to restore
2. Click on the "New database fork"
3. Select the new PostgreSQL service name, project name, database version, cloud region and plan for the new instance
4. Select the "Source service state" defining the backup point in time, available options are
    * Latest transaction
    * Another point in time - the date selector allows to chose a precise point in time within the available backup retention period.

.. Note::
    The Hobbyist service plan does not support database forking, so you have to use an external tool, such as ``pg_dump``, to perform a backup.

Once the new service is running, you can change your application’s connection settings to point to it.

Manual restoration should only be necessary when data is accidentally corrupted by the pointing applications. Aiven handles automatically outages and software failures by replacing broken nodes with new ones that resume correctly from the point of failure.

.. Tip::
    Forked services can also be very useful for testing purposes, allowing you to create a completely realistic, separate copy of the actual production database with its data.
