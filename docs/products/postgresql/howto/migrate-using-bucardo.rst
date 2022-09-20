Migrating to Aiven for PostgreSQL® using Bucardo
================================================

The preferred approach to migrating a database to Aiven for PostgreSQL®
is to use Aiven's open source migration tool (:doc:`../concepts/aiven-db-migrate`). However, if you
are running PostgreSQL 9.6 (or earlier) or do not have ``superuser`` access to your
database to add replication slots, you can use the open source
`Bucardo <https://bucardo.org>`__ tool to allow replication to Aiven.

**Requirements:**

-  An Aiven for PostgreSQL database

-  Your current database

-  A computer with Bucardo installed

-  Connectivity between Bucardo and the source and target databases

Moving existing data
~~~~~~~~~~~~~~~~~~~~

To move existing data, you can follow the steps below and
`update <https://bucardo.org/Bucardo/operations/onetimecopy>`__ your
``sync`` job to use the ``onetimecopy`` and move existing data across.
You can also use the standard ``pg_dump`` and ``pg_restore`` commands to
fill the Aiven database and use Bucardo for syncing any changes to the
source database and ensuring it remains up-to-date.

Replicating changes
~~~~~~~~~~~~~~~~~~~

To migrate your data using Bucardo:

#. | Install Bucardo using `the installation
     instructions <https://bucardo.org/Bucardo/installation/>`__ on the
     Bucardo site.

#. | Install the ``aiven_extras`` `extension <https://developer.aiven.io/docs/products/postgresql/concepts/dba-tasks-pg.html#aiven-extras-extension>`_ to your current database.
   | Bucardo requires the superuser role to set the
     ``session_replication_role`` parameter. Aiven uses the open source
     ``aiven_extras`` extension to allow you to run ``superuser``
     commands as a different user, as direct ``superuser`` access is not
     provided for security reasons.

#. | Open and edit the ``Bucardo.pm`` file with administrator
     privileges.
   | The location of the file can vary according to your operating
     system, but you might find it in
     ``/usr/local/share/perl5/5.32/Bucardo.pm`` , for example.

   a. Scroll down until you see a ``disable_triggers`` function, on line
      `5324 <https://github.com/bucardo/bucardo/blob/1ff4d32d1924f3437af3fbcc1a50c1a5b21d5f5c/Bucardo.pm#L5324>`__.

   b. On line `5359 <https://github.com/bucardo/bucardo/blob/1ff4d32d1924f3437af3fbcc1a50c1a5b21d5f5c/Bucardo.pm#L5359>`__, change ``SET session_replication_role = default`` to
      the following:

      ::

         $dbh->do(q{select aiven_extras.session_replication_role('replica');});

   c. Scroll down to the ``enable_triggers`` function at line `5395 <https://github.com/bucardo/bucardo/blob/1ff4d32d1924f3437af3fbcc1a50c1a5b21d5f5c/Bucardo.pm#L5395>`__.

   d. On line 5428, change ``SET session_replication_role = default`` to
      the following:

      ::

         $dbh->do(q{select aiven_extras.session_replication_role('origin');});

   e. | Save your changes and close the file.

#. | Add your source and destination databases.
   | For example:

   ::

      bucardo add db srcdb dbhost=0.0.0.0 dbport=5432 dbname=all_your_base dbuser=$DBUSER dbpass=$DBPASS

      bucardo add db destdb dbhost=cg-pg-dev-sandbox.aivencloud.com dbport=21691 dbname=all_your_base dbuser=$DBUSER dbpass=$DBPASS

#. Add the tables that you want to replicate:

   ::

      bucardo add table belong to us herd=$HERD db=srcdb

   .. note:: You can set ``$HERD`` to any name you choose for the herd, which is used to set up the synchronization.

#. Dump and restore the database from your source to your Aiven service:

   ::

      pg_dump --schema-only --no-owner all_your_base > base.sql
      psql "$AIVEN_DB_URL" < base.sql

   | You can restore the source data or provide only the schema,
     depending on the size of your current database.

#. Create the ``dbgroup`` for Bucardo:

   ::

      bucardo add dbgroup src_to_dest srcdb:source destdb:target
      bucardo add sync sync_src_to_dest relgroup=$HERD db=srcdb,destdb
      (sudo) bucardo start
      bucardo status sync_src_to_dest

#. | Start Bucardo and run the ``status`` command. When ``Current state`` is ``Good`` , the data is flowing to your
     Aiven database.

#. | Log in to the `Aiven web console <https://console.aiven.io>`_ and go to the **Current Queries** tab for your Aiven for PostgreSQL service. This shows you that the ``bucardo`` process is inserting data.

#. Once all your data is synchronized, switch the database connection
   for your applications to Aiven for PostgreSQL.
