Migrate to Aiven for PostgreSQL with ``pg_dump`` and ``pg_restore``
===================================================================

.. Tip::
    We recommend to migrate your PostgreSQL database to Aiven by using :doc:`aiven-db-migrate <migrate-aiven-db-migrate>`.

Aiven for PostgreSQL supports the same tools as a regular PostgreSQL database, so you can migrate using the standard ``pg_dump`` and ``pg_restore`` tools.

The `pg_dump <https://www.postgresql.org/docs/current/app-pgdump.html>`_ tool can be used to extract the data from your existing PostgreSQL database and `pg_restore <https://www.postgresql.org/docs/current/app-pgrestore.html>`_ can then insert that data into your Aiven for PostgreSQL database.
The duration of the process depends on the size of your existing database.

During the migration no new data written to the database is included. You should turn off all write operations to your source database server before you run the ``pg_dump``.

.. Tip::
    You can keep the write operations enabled, and use the steps to try out the migration process first before the actual migration. This way, you will find out about the duration, and check everything works without downtime.

Variables
'''''''''

You can use the following variables in the code samples provided:

====================      =======================================================================================
Variable                  Description
====================      =======================================================================================
``SRC_SERVICE_URI``       Service URI for the source PostgreSQL connection
``DUMP_FOLDER``           Local Folder used to store the source database dump files
``DEST_PG_NAME``          Name of the destination Aiven PostgreSQL service
``DEST_PG_PLAN``          Aiven plan for the destination Aiven PostgreSQL service
``DEST_SERVICE_URI``      Service URI for the destination PostgreSQL connection, available from the Aiven Console
====================      =======================================================================================

Perform the migration
'''''''''''''''''''''

1. If you don't have an Aiven for PostgreSQL database yet, run the following command to create a couple of PostgreSQL services via :doc:`../../../tools/cli` substituting the parameters accordingly::

    avn service create -t pg -p DEST_PG_PLAN DEST_PG_NAME

.. Tip::
    Aiven for PostgreSQL allows you to easily switch between different service plans, but for the duration of the initial migration process using ``pg_dump``, we recommend that you choose a service plan that is large enough for the task. This allows you to limit downtime during the migration process. Once migrated, you can scale the plan size up or down as needed.

Aiven automatically creates a ``defaultdb`` database and ``avnadmin`` user account, which are used by default.


2. Run the ``pg_dump`` command substituting the ``SRC_SERVICE_URI`` with the service URI of your source PostgreSQL service, and ``DUMP_FOLDER`` with the folder where you want to store the dump in::

    pg_dump -d 'SRC_SERVICE_URI' --jobs 4 --format directory -f DUMP_FOLDER

The ``--jobs`` option in this command instructs the operation to use 4 CPUs to dump the database. Depending on the number of CPUs you have available, you can use this option to adjust the performance to better suit your server.

.. Tip::
    If you encounter problems with restoring your previous object ownerships to users that do not exist in your Aiven database, use the ``--no-owner`` option in the ``pg_dump`` command. You can create the ownership hierarchy after the data is migrated.


3. Run ``pg_restore`` to load the data into the new database::

     pg_restore -d 'DEST_SERVICE_URI' --jobs 4 DUMP_FOLDER

.. Note::
    If you have more than one database to migrate, repeat the ``pg_dump`` and ``pg_restore`` steps for each database.


5. Switch the connection settings in your applications to use the new Aiven database once you have migrated all of your data.

.. Warning::
    The user passwords are different from those on the server that you migrated from. Go to the **Users** tab for your service in the Aiven web console to check the new passwords.

7. Connect to the target database via ``psql``::

    psql 'DEST_SERVICE_URI'

6. Run the ``ANALYZE`` command to apply proper database statistics for the newly loaded data::

    newdb=> ANALYZE;

If you got this far, then all went well and your Aiven for PostgreSQL database is now ready to use.

Handle ``pg_restore`` errors
''''''''''''''''''''''''''''

When migrating PostgreSQL databases to Aiven via ``pg_restore`` you could encounter errors like::

    could not execute query: ERROR: must be owner of extension <extension>

For example, the following ``pg_restore`` error appears quite commonly::

  pg_restore: [archiver (db)] could not execute query: ERROR: must be owner of extension <some_extension>

This type of error is often related to the lack of superuser-level privileges blocking non-essential queries.

A typical example is due to failing ``COMMENT ON EXTENSION`` queries trying to replace the documented comment string for an extension. In such cases, the errors are harmless and can be ignored. Alternatively, use the ``--no-comments`` parameter in ``pg_restore`` to skip these queries.

.. Tip::
    ``pg_restore`` offers similar ``--no-XXX`` options to switch off other, often unnecessary restore queries. More information are avaialble at the `dedicated documentation page <https://www.postgresql.org/docs/current/app-pgrestore.html>`_.
