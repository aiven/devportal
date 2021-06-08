Migrate Databases with ``pg_dump`` and ``pg_restore``
=====================================================

The preferred approach for migrating a PostgreSQL database to Aiven is to use :doc:`migration-aiven-db-migrate`. However, Aiven for PostgreSQL supports the same tools as a regular PostgreSQL database, which allows you to use those same tools for migrating to Aiven for PostgreSQL.

``pg_dump`` tool can be used to extract the data from your existing PostgreSQL database and ``pg_restore`` then can insert that data to your Aiven for PostgreSQL database. The duration of the process depends on the size of your existing database.

While the migration is in progress, no new data written to the database is included, so we recommend turning off all write operations to your source database server before you run ``pg_dump``.

.. Tip::
    You can also use these steps to do a trial run without turning off write operations for your current database server before you perform the actual migration. This gives you a better idea of how much time to reserve for the migration, and to make sure that the process works without causing any downtime.


Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

====================      =======================================================================================
Variable                  Description
====================      =======================================================================================
``SRC_SERVICE_URI``       Service URI for the source PostgreSQL connection
``DUMP_FOLDER``           Local Folder used to store the source database dump files
``DEST_PG_NAME``          Name of the destination Aiven PostgreSQL service
``DEST_PG_PLAN``          Aiven Plan for the destination Aiven PostgreSQL service
``DEST_SERVICE_URI``      Service URI for the destination PostgreSQL connection, available from the Aiven Console
====================      =======================================================================================

Perform the Migration
'''''''''''''''''''''

To following is the series of steps required to migrate your database to Aiven for PostgreSQL

1. If you don't have a PostgreSQL database already, run the following commands to create a couple of PostgreSQL services via :doc:`../../../tools/cli` substituting the parameters accordingly::

    avn service create -t pg -p DEST_PG_PLAN DEST_PG_NAME

.. Tip::
    Aiven for PostgreSQL allows you to switch between different service plans, but at least for the duration of the initial migration process when using ``pg_dump``, we recommend that you choose a service plan that is large enough for the task. This allows you to limit downtime during the migration process.

Aiven automatically creates a ``defaultdb`` database and ``avnadmin`` user account, which are used by default. If necessary, you can create additional databases and related users in the Aiven web console, on the **Databases** and **Users** tabs of your Aiven for PostgreSQL service.


2. Run the ``pg_dump`` command substituting the ``SRC_SERVICE_URI`` with the service URI of your source PostgreSQL service and ``DUMP_FOLDER`` with the folder where you want to store the dump in::

    pg_dump -d 'SRC_SERVICE_URI' --jobs 4 --format directory -f DUMP_FOLDER

The ``--jobs`` option in this command instructs the operation to use 4 CPUs to dump the database. Depending on the number of CPUs that you have available, you can use this option to adjust the performance to better suit your server.

.. Tip::
    If you have issues with restoring your previous object ownerships to users that do not exist in your Aiven database, use the ``--no-owner`` option in the ``pg_dump`` command. You can then create the ownership hierarchy after the data is migrated.


3. Run pg_restore to load the data into the new database::

     pg_restore -d 'DEST_SERVICE_URI' --jobs 4 DUMP_FOLDER

4. If you have more than one database to migrate, repeat the ``pg_dump`` and ``pg_restore`` steps for each database.


5. Switch the connection settings in your applications to use the new Aiven database once you have migrated all of your data.

.. Warning::
    The user passwords are different from those on the server that you migrated from. Go to the **Users** tab for your service in the Aiven web console to check the new passwords.

7. Connected to the target database via ``psql``::

    psql 'DEST_SERVICE_URI'

6. Run the ``ANALYZE`` command to apply proper database statistics for the newly loaded data::

    newdb=> ANALYZE;
