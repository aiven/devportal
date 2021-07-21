Create manual PostgreSQL backups
================================

Aiven provides :doc:`fully automated backup management for PostgreSQL <../concepts/pg-backups>`. All backups are encrypted with service-specific keys, and point-in-time recovery is supported to allow recovering the system to any point within the backup window. Aiven stores the backups to the closest available cloud storage to enhance restore speed.

To create a backup for your own use, use ``pg_dump`` and follow the steps in this article.

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

==================      =============================================================
Variable                Description
==================      =============================================================
``POSTGRESQL_URI``      URL for PostgreSQL connection, from the service overview page
==================      =============================================================

Create backups with ``pg_dump``
'''''''''''''''''''''''''''''''

Perform a backup of your database using the standard PostgreSQL ``pg_dump`` command. Full detail on the parameters can be found in the `associated documentation <https://www.postgresql.org/docs/current/app-pgdump.html>`_, but a typical command would look something like this::

     pg_dump 'POSTGRESQL_URI' \
         -f backup_folder     \
         -j 2                 \
         -F directory

This command creates a backup in ``directory`` format (ready for use with ``pg_restore``) using 2 concurrent jobs and storing the output to a folder called ``backup_folder``.

.. Tip::
    ``pg_dump`` can be run against any **standby** node, using the *Replica URI* from the Aiven web console.
    Creating more jobs via the ``-j`` option could be especially useful, since it may not be a problem to add extra load to the standby node.

