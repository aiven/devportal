Migrate PostgreSQL® databases to Aiven using the console 
========================================================

You can migrate PostgreSQL® databases to Aiven using either :doc:`CLI </docs/products/postgresql/howto/migrate-aiven-db-migrate>` (``aiven-db-migrate``) or `Aiven Console <https://console.aiven.io/>`_. This article addresses the latter scenario by providing guidelines on how to use `Aiven Console <https://console.aiven.io/>`_ to migrate PostgreSQL databases to the Aiven platform.

.. seealso::

    For the other migration method (using ``aiven-db-migrate``), see :doc:`Migrate to Aiven for PostgreSQL® with aiven-db-migrate </docs/products/postgresql/howto/migrate-aiven-db-migrate>`.

About migrating via console
---------------------------

The console migration tool enables you to migrate PostgreSQL databases to managed PostgreSQL clusters in your Aiven organization. You can migrate the following:

* Existing on-premise PostgreSQL databases
* Cloud-hosted PostgreSQL databases
* Managed PostgreSQL database clusters on Aiven.

With the console migration tool, you can migrate your data using either the :ref:`continuous migration method <pg-continuous-migration>` (default and recommended) or the :ref:`one-time snapshot method <pg-dump-migration>` (``pg_dump``).

.. _pg-continuous-migration:

Continuous migration
''''''''''''''''''''

The continuous migration method is used by default in the console and taken as a method to follow in this guide. The continuous migration keeps the source database operational during the migration. This method uses `logical replication <https://www.postgresql.org/docs/current/logical-replication.html>`_, which enables data transfer not only for the data that has already been there in the source database when triggering the migration but also for any data written to the source database during the migration.

.. important::

   Before you use the logical replication, make sure you know and understand all the restrictions it has. For details, check out `Logical replication restrictions <https://www.postgresql.org/docs/current/logical-replication-restrictions.html>`_.

Using the continuous migration requires either superuser permissions or the ``aiven_extras`` extension installed on the source database.

.. dropdown:: Expand to check out how to verify that you have superuser permissions.

    Use ``psql`` to run the ``\du`` command:

    .. code-block:: bash

       \du

    .. code-block:: bash
       :caption: Expected output

       Role name |                      Attributes                            |                 Member of
       ----------+------------------------------------------------------------+-----------------------------------------
       _source_db     | Superuser, Replication                                     | {}
       example   | Create role, Create DB, Replication, Bypass RLS            | {pg_read_all_stats,pg_stat_scan_tables,pg_signal_backend}
       postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

    Identify your role name in the ``Role name`` column and check if it has the ``Superuser`` attribute assigned in the ``Attributes`` column. If not, request it from your system administrator.

.. topic:: No superuser permissions? Install ``aiven_extras``.

   If you don't have superuser permissions, but you still want to use the continuous migration, you can install the ``aiven_extras`` extension on the source database using the following command:

   .. code-block:: bash

      CREATE EXTENSION `aiven_extras` CASCADE;

.. _pg-dump-migration:

Dump migration
''''''''''''''

``pg_dump`` is a point-in-time snapshot. The data written to the source database during the migration process (after initiating the dump) is not migrated to the target database. When you start a dump migration, make sure no data is written to the source database by the time the dumping process is over.

When you trigger the migration setup in the console and initial checks detect that your source database does not support the logical replication, you are notified about it via wizard. To continue with the migration, you can select the alternative ``pg_dump`` migration method in the wizard.

.. topic:: No superuser permissions and no ``aiven_extras``? Migrate using the dump method.

   Without superuser permissions or ``aiven_extras`` installed, you cannot use the logical replication and migrate in a continuous manner. In that case, you can migrate your database using the dump method if you have the following permissions:

   * Connect
   * Select on all tables in the database
   * Select on all the sequences in the database

For the instruction on how to perform a dump, skip a few sections that follow and go straight to :ref:`Migrate a database <migrate-in-console>`.

Prerequisites
-------------

* To use the default continuous migration method in the console, you need to have the logical replication enabled on your source database either with superuser permissions or the ``aiven_extras`` extension.
* Source database's hostname or IP address needs to be :doc:`accessible from the public Internet </docs/platform/howto/public-access-in-vpc>`.
* You need to have the following source database's credentials and reference data:
  
  * Public hostname or connection string, or IP address used to connect to the database
  * Port used to connect to the database
  * Username (for a user with superuser permissions)
  * Password.

* Firewalls protecting the source database and the target databases need to be open to allow the traffic and connection between the databases (update or disable the firewalls temporarily if needed).

Pre-configure the source
------------------------

* Allow remote connections on the source database.

  Check that your database allows all remote connections by using ``psql`` to run the following query:

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

  Open ``pg_hba.conf`` in a text editor of your choice, for example, Visual Studio Code.

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

* Enable the logical replication.

  For cloud-hosted databases, the logical replication is usually enabled by default, while databases hosted on-premises can have the logical replication not enabled.

  Check that the logical replication is enabled using ``psql`` to run the following query:

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

  If ``number of slots`` is smaller than the number of databases in your PostgreSQL server, modify it using the following query:

  .. code-block:: bash

     ALTER SYSTEM SET max_replication_slots = use_your_number;

  where ``use_your_number`` stands for the number of databases in your server.

* Restart your PostgreSQL server using the following command:
  
  .. code-block:: bash

     sudo service postgresql restart

.. _migrate-in-console:

Migrate a database
------------------

1. Log in to the `Aiven Console <https://console.aiven.io/>`_.
2. On the **Services** page, select the service where your target database is located.
3. From the sidebar on your service's page, select **Service settings**.
4. On the **Service settings** page, navigate to the **Service management** section, and select **Import database**.
5. Guided by the migration wizard, go through all the migration steps.

Step 1: Configure
'''''''''''''''''

Get familiar with the guidelines provided in the **PostgreSQL migration configuration guide** window, make sure your configuration is in line with them, and select **Get started**.

Step 2: Validation
''''''''''''''''''

1. To establish a connection to your source database, enter required database details in the **Database connection and validation** window:

   * Hostname
   * Port
   * Database name
   * Username
   * Password

2. Select the **SSL encryption (recommended)** checkbox.

3. Optionally, exclude specific databases from the migration by entering their names (separated with spaces) into the **Exclude databases** field.

4. Select **Run check**.

.. topic:: Cannot migrate the database using logical replication?

   If your connection test returns information that you cannot migrate the database using the logical replication due to the missing superuser permissions or ``aiven_extras`` extension, you can still migrate your data using the dump method.

   To start a dump, select checkbox **Start the migration using a one-time snapshot (dump method)**.

Step 3: Migration
'''''''''''''''''

If all the checks pass with no error messages, you are ready to start the migration. Before you do that, make sure you understand its limitations and consequences.

.. topic:: Impact on target databases

   It's recommended to migrate into an empty database. If you migrate into a populated database, colliding tables with primary keys are not affected, but tables without primary keys are appended. Check other limitations in `Logical replication restrictions <https://www.postgresql.org/docs/current/logical-replication-restrictions.html>`_.

Trigger the migration by selecting **Start migration** in the **Database migration** window.

While the migration is in progress, you can take the following actions:

* Let it proceed until completed by selecting **Close window**, which closes the wizard. You can come back to check the status at any time on the **Service settings** page > the **Service management** section > **Import database**.
* Write to the target database.
* Discontinue the migration by selecting **Stop migration**. Although the data already migrated is retained, you cannot restart the stopped process. To continue with the migration, you need to start a new migration process from scratch.

.. warning::

   To avoid conflicts and replication issues while the migration is ongoing, take the following precautions:

   * Do not write to any tables in the target database that are being processed by the migration tool.
   * Do not change the replication configuration of the source database manually. Do not modify ``wal_level`` or reduce ``max_replication_slots``.
   * Do not make database changes that could disrupt or prevent the connection between the source database and the target database. Do not change the listen address of the source database and do not modify or enable firewalls on the databases.

.. topic:: Migration attempt failed?

   If you happen to get such a notification, investigate potential causes of the failure and try to fix the issues. When you are ready, trigger the migration again by selecting **Start over**.

Step 4: Close
'''''''''''''

As soon as the wizard communicates the completion of the migration, check if there's also information about the replication mode being active.

.. topic:: Replication mode active

   This information in the wizard means that your data has been transferred to Aiven, but some new data is still continuously being synced between the connected databases.

* If there is no replication in progress, select **Close connection** in the migration wizard to finalize the migration process. As a result, on the **Service settings** page > the **Service management** section > **Import database**, you'll see the **Ready** tag.
* If the replication mode is active, you can select **Keep replicating**. As a result, on the **Service settings** page > the **Service management** section > **Import database**, you'll see the **Syncing** tag, and you'll be able to check the status of the migration process by selecting **Status update**.

.. topic:: Result

   You have successfully migrated your PostgreSQL database into you Aiven for PostgreSQL service.

Related pages
---------------

- :doc:`About aiven-db-migrate </docs/products/postgresql/concepts/aiven-db-migrate>`
- :doc:`Migrate to Aiven for PostgreSQL® with aiven-db-migrate </docs/products/postgresql/howto/migrate-aiven-db-migrate>`
- :doc:`Migrate to Aiven for PostgreSQL® with pg_dump and pg_restore </docs/products/postgresql/howto/migrate-pg-dump-restore>`
- :doc:`Migrate between PostgreSQL® instances using aiven-db-migrate in Python </docs/products/postgresql/howto/run-aiven-db-migrate-python>`
- :doc:`Migrate to Aiven for MySQL from an external MySQL </docs/products/mysql/howto/migrate-from-external-mysql>`
