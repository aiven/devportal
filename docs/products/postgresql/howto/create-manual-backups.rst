Create manual PostgreSQL backups
================================

Aiven provides :doc:`fully automated backup management for PostgreSQL <../concepts/pg-backups>`. All backups are encrypted with service-specific keys, and point-in-time recovery is supported to allow recovering the system to any point within the backup window. Aiven stores the backups to the closest available cloud storage. The raw backups automatically created by Aiven are not accessible by customers.

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

If an additional set of backups is needed, it can be performed using the standard PostgreSQL ``pg_dump`` command. Typical parameters for the command include the following::

    pg_dump 'POSTGRESQL_URI'   \
        -f <target_file/dir>   \
        -j <number_of_jobs>    \
        -F <backup_format>

More information about ``pg_dump`` parameters can be found in the `associated documentation <https://www.postgresql.org/docs/current/app-pgdump.html>`_.

.. Tip::
    ``pg_dump`` can be run against any **standby** node, using the *Replica URI* from the Aiven web console.
    Creating more jobs via the ``-j`` option could be especially useful, since extra load on the standby node might not be an issue.

For example, to create a backup in ``directory`` format (which can be used directly with ``pg_restore``) using two concurrent jobs and storing the results to a folder called ``backup_folder`` run the following command::

     pg_dump 'POSTGRESQL_URI' \
         -f backup_folder     \
         -j 2                 \
         -F directory
