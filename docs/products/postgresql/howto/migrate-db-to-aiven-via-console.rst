Migrate PostgreSQL® databases to Aiven using the console 
========================================================

You can migrate PostgreSQL® databases to Aiven using either CLI (``aiven-db-migrate``) or the Aiven web console. This article addresses the latter scenario by providing guidelines on how to use the Aiven console to migrate PostgreSQL databases to the Aiven platform.

.. seealso::

    For the other migration method (using ``aiven-db-migrate``), see :doc:`Migrate to Aiven for PostgreSQL® with aiven-db-migrate </docs/products/postgresql/howto/migrate-aiven-db-migrate>`.

About migrating via console
---------------------------

* With the console migration tool, you can migrate existing on-premise or cloud-hosted PostgreSQL databases to clusters in your Aiven account.

  .. note:: 
    
     The console migration tool doesn't support migrating managed database clusters on Aiven to other managed database clusters on Aiven.

* Console migration tool uses `logical replication <https://www.postgresql.org/docs/current/logical-replication.html>`_ by default.

* With the console migration tool, you can migrate PostgreSQL® databases either using the continuous migration method, which is the one recommended and detailed in this guide, or using the dump method (``pg_dump``).

  * Continuous migration keeps the source database operational during the migration but requires superuser permissions.
  * Dump is a point-in-time snapshot and requires the source database to be offline or in the maintenance mode during the migration process since any data it gets after initiating the dump are not migrated to the target database.

.. dropdown:: Expand to check out how to verify that you have superuser permissions.

    Use ``psql`` to run the ``\du`` command:

    .. code-block:: bash

       \du

    .. code-block:: bash
       :caption: Expected output

       Role name |                      Attributes                            |                 Member of
       ----------+------------------------------------------------------------+-----------------------------------------
       _dodb     | Superuser, Replication                                     | {}
       example   | Create role, Create DB, Replication, Bypass RLS            | {pg_read_all_stats,pg_stat_scan_tables,pg_signal_backend}
       postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

    Identify your role name in the ``Role name`` column and check if it has the ``Superuser`` attribute assigned in the ``Attributes`` column. If not, request it from your system administrator.

.. topic:: No superuser permissions? Migrate using the dump method.

   If you don't have superuser permissions required for the continuous migration, you can still migrate your database using the dump method if you have the following permissions:

   * Connect
   * Select on all tables in the database
   * Select on all the sequences in the database

   To perform the dump, make sure your source database is offline or under maintenance and skip to the final part of this guide for the instruction on how to set up the migration in the console.

Prerequisites
-------------

* Logical replication is enabled on the source database.
* You have superuser permissions on the source database.
* Source database's hostname or IP address are :doc:`accessible from the public Internet </docs/platform/howto/public-access-in-vpc>`.
* You have the source database's credentials and reference data
  
  * Public hostname or connection string, or IP address used to connect to the database
  * Port used to connect to the database
  * Username (for a user with superuser permissions)
  * Password

* Firewalls protecting the source database and the target databases are open to allow the traffic and connection between the databases (update or disable the firewalls temporarily if needed).

Pre-configure the source
------------------------

* Allow remote connections.

  Check that your database allows all remote connections, use ``psql`` to run the following query:

  .. code-block:: bash

     SHOW listen_addresses;

  If enabled, you can expect the following output (with ``listen_addresses`` set to ``*``):

  .. code-block:: bash

      listen_addresses
      -----------
      *
      (1 row)

  If the command line returns something different, enable remote connections for your database with the following query:

  .. code-block:: bash

     ALTER SYSTEM SET listen_addresses = '*';

* Change your IPv4 local connection to ``0.0.0.0/0`` to allow all incoming IP addresses.

  Find the ``pg_hba.conf`` configuration file using the following query:

  .. code-block:: bash

     SHOW hba_file;

  Open ``pg_hba.conf`` in a text editor of your choice, for example, Visual Studio Code:

  .. code-block:: bash

     code pg_hba.conf

  Under ``IPv4 local connections``, find and replace the IP address with ``0.0.0.0/0``.

  .. code-block:: bash

     # TYPE  DATABASE        USER            ADDRESS                 METHOD
     
     # IPv4 local connections:
     host    all             all             0.0.0.0/0               md5
     # IPv6 local connections:
     host    all             all             ::/0                    md5 

  .. seealso::
   
     For more details on the configuration file's syntax, see `The pg_hba.conf File <https://www.postgresql.org/docs/14/auth-pg-hba-conf.html>`_.

* Enable logical replication.

  For cloud-hosted databases, the logical replication is usually enabled by default, while databases hosted on-premises can have the logical replication not enabled.

  Check that the logical replication is enabled, use ``psql`` to run the following query:

  .. code-block:: bash

     SHOW wal_level;

  .. code-block:: bash
     :caption: Expected output if enabled

     wal_level
     -----------
     logical
     (1 row)

  If the command prompt returns something different, enable the logical replication in your database by setting ``wal_level`` to ``logical``:

  .. code-block:: bash

     ALTER SYSTEM SET wal_level = logical;

* Set the maximum number of replication slots to a value that is equal to or greater than the number of databases in the PostgreSQL server.

  Check the current status using the following query:
  
  .. code-block:: bash

     SHOW max_replication_slots;

  You can expect the following output:

  .. code-block:: bash

     max_replication_slots
     -----------
     <number of slots, e.g. 8>
     (1 row)

  If ``number of slots`` is smaller than the number of databases in your PostgreSQL server, modify it.

  .. code-block:: bash

     ALTER SYSTEM SET max_replication_slots = use_your_number;

  where ``use_your_number`` is the number of databases in your server.

* Restart your PostgreSQL server.
  
  .. code-block:: bash

     sudo service postgresql stop
     sudo service postgresql start

Migrate a database
------------------

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. From the **Current services** list, select the service where your target database is located.
3. In the **Overview** tab of the selected service, navigate to the **Migrate database** section and select **Set up migration**.

   .. image:: /images/products/postgresql/set-up-migration.png
      :width: 700px
      :alt: Set up migration

4. Guided by the **PostgreSQL migration configuration guide** wizard, go through all the migration steps.

Step 1 - configure
''''''''''''''''''

Get familiar with the guidelines provided in the migration wizard and select **Get started**.

.. image:: /images/products/postgresql/start-migration.png
   :width: 700px
   :alt: Set up migration

Step 2 - connect
''''''''''''''''

1. To establish a connection to your source database, enter required database details into the wizard:

   * Hostname
   * Port
   * Database name
   * Username
   * Password

   .. image:: /images/products/postgresql/connect-source.png
      :width: 700px
      :alt: Set up migration

2. Select the **SSL encryption (recommended)** checkbox.

3. If you prefer to use the dump method for the migration, select the **Start the migration using a one-time snapshot (dump method)** checkbox.

4. Select **Test connection**.

.. topic:: Unable to use logical replication?

   If your connection test returns such a warning, either resolve the issues or give up the continuous migration and opt for the dump method by selecting **Start the migration using a one-time snapshot (dump method)** > **Run check** > **Start migration**.

Step 3 - migrate
''''''''''''''''

If all the checks pass with no error messages, you can trigger the migration by selecting **Start migration**.

.. image:: /images/products/postgresql/ready-to-migrate.png
   :width: 700px
   :alt: Set up migration

Step 5 - close
''''''''''''''

While the migration is in progress, you can

* Let it proceed until completed by selecting **Close window**, which closes the wizard. You come back to check the status at any time.
* Write to the target database.
* Discontinue the migration by selecting **Cancel migration**, which retains the data already migrated. You cannot restart the stopped process and can only start a new migration.

.. image:: /images/products/postgresql/migration-in-progress.png
   :width: 700px
   :alt: Set up migration

.. warning::

   To avoid conflicts and replication issues while the migration is ongoing

   * Do not write to any tables in the target database that are being processed by the migration tool.
   * Do not change the replication configuration of the source database manually. Do not modify ``wal_level`` or reduce ``max_replication_slots``.
   * Do not make database changes that could disrupt or prevent the connection between the source database and the target database. Do not change the listen address of the source database and do not modify or enable firewalls on the databases.

.. topic:: Migration attempt failed?

   If you happen to get such a notification, investigate potential causes of the failure and try to fix the issues. When you are ready, trigger the migration again by selecting **Start over**.

When the wizard communicates the completion of the migration, select one of the following:

* **Close connection** if there is no replication in progress.
* **Keep replicating** if the replication is still ongoing.

.. topic:: Replication mode active?

   Your data has been transferred to Aiven but some new data is still continuously being synced between the connected databases.

Related reading
---------------

- :doc:`About aiven-db-migrate </docs/products/postgresql/concepts/aiven-db-migrate>`
- :doc:`Migrate to Aiven for PostgreSQL® with aiven-db-migrate </docs/products/postgresql/howto/migrate-aiven-db-migrate>`
- :doc:`Migrate to Aiven for PostgreSQL® with pg_dump and pg_restore </docs/products/postgresql/howto/migrate-pg-dump-restore>`
- :doc:`Migrate between PostgreSQL® instances using aiven-db-migrate in Python </docs/products/postgresql/howto/run-aiven-db-migrate-python>`
- :doc:`Migrate to Aiven for MySQL from an external MySQL </docs/products/mysql/howto/migrate-from-external-mysql>`
