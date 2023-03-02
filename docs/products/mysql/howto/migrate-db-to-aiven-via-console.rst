Migrate MySQL® databases to Aiven using the console 
===================================================

You can migrate MySQL® databases to Aiven using either :doc:`CLI </docs/products/mysql/howto/migrate-from-external-mysql>` or the `Aiven web console <https://console.aiven.io/>`_. This article addresses the latter scenario by providing guidelines on how to use the Aiven console to migrate MySQL databases to the Aiven platform.

.. seealso::

    For the other migration method (CLI), see :doc:`Migrate to Aiven for MySQL from an external MySQL </docs/products/mysql/howto/migrate-from-external-mysql>`.

About migrating via console
---------------------------

* Console migration tool enables you to migrate MySQL databases to managed MySQL clusters in your Aiven account. You can migrate

  * Existing on-premise MySQL databases
  * Cloud-hosted MySQL databases
  * Managed MySQL database clusters on Aiven.

* Console migration tool can use either logical replication or physical replication.

  * Logical replication allows the continuous migration, which is recommended and used by default in the tool, hence, also detailed in this guide. With this method, data transfer is possible not only for the data that has already been there in the source database when triggering the migration but also for any data written to the source database during the migration.

  * Physical replication allows the other migration method supported in the migration tool, ``mysqldump``. With this method, current contents of the database are copied into a file and transferred to the target database. Any changes written to the source database during the migration are not transferred. When you trigger the migration setup in the console and initial checks detect that your source database does not support the logical replication, you are notified about it via wizard. To continue with the migration, you can select the alternative ``mysqldump`` migration method in the wizard.

Prerequisites
-------------

* To use the default migration method in the console tool, you have the logical replication enabled on your source database.
* Source database's hostname or IP address are :doc:`accessible from the public Internet </docs/platform/howto/public-access-in-vpc>`.
* You have the source database's credentials and reference data
  
  * Public hostname or connection string, or IP address used to connect to the database
  * Port used to connect to the database
  * Username (for a user with superuser permissions)
  * Password

* Firewalls protecting the source database and the target databases are open to allow the traffic and connection between the databases (update or disable the firewalls temporarily if needed).

Pre-configure the source
------------------------

* Allow remote connections on the source database.

  Log in to the server hosting your database and the MySQL installation. Next, open the network configuration of MySQL with the following command:

  .. code-block:: bash

     sudo code /etc/mysql/mysql.conf.d/mysqld.cnf

  .. code-block:: bash
     :caption: Expected output

      . . .
      lc-messages-dir = /usr/share/mysql
      skip-external-locking
      #
      # Instead of skip-networking the default is now to listen only on
      # localhost which is more compatible and is not less secure.
      bind-address            = 127.0.0.1
      . . . 

  Change the value of ``bind-address`` to a wildcard IP address,``*`` or ``0.0.0.0``.

  .. code-block:: bash
     :caption: Expected output

      . . .
      lc-messages-dir = /usr/share/mysql
      skip-external-locking
      #
      # Instead of skip-networking the default is now to listen only on
      # localhost which is more compatible and is not less secure.
      bind-address            = *
      . . . 

  Save the changes and exit the file. Restart MySQL to apply the changes.

  .. code-block:: bash

     sudo systemctl restart mysql

  .. note::

     After completing the migration, make sure you revert those changes so that the MySQL database no longer accept remote connections.

* Enable GTID.

  Set up GTID on your database so that it can create a unique identifier for each transaction on the source database. See `Enabling GTID Transactions Online <https://dev.mysql.com/doc/refman/5.7/en/replication-mode-change-online-enable-gtids.html>`_ for the guidelines.

  To make sure you have GTID enabled, open your ``my.cnf`` file in ``/etc/my.cnf`` or ``/etc/mysql/my.cnf`` (if no luck finding the file, check out `more potential locations in the table corresponding to your OS in the MySQL documentation <https://dev.mysql.com/doc/refman/8.0/en/option-files.html>`_).

  Check that the ``my.cnf`` file has the ``[mysqld]`` header.

  .. code-block:: bash

      [mysqld]
      gtid_mode=ON
      enforce_gtid_consistency=ON
 
  After enabling GTID, restart MySQL.

  .. code-block:: bash

     sudo systemctl restart mysql

* Enable logical replication.

  Grant logical replication privileges to the user that you intend to connect to the source database with during the migration.

  Log in to the database as an administrator and grant the following permission to the user:

  .. code-block:: bash

     GRANT ALL ON <database-name>.* TO ‘username’@‘%’;

  Reload the grant tables to apply the changes to the permissions.

  .. code-block:: bash

     FLUSH PRIVILEGES;

  .. note::

     After completing the migration, make sure you revert those changes so that the user no longer has logical replication privileges.

Migrate a database
------------------

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. From the **Current services** list, select the service where your target database is located.
3. In the **Overview** tab of the selected service, navigate to the **Migrate database** section and select **Set up migration**.

   .. image:: /images/products/mysql/set-up-migration-mysql.png
      :width: 700px
      :alt: Set up migration

4. Guided by the **MySQL migration configuration guide** wizard, go through all the migration steps.

Step 1 - configure
''''''''''''''''''

Make sure your configuration is in line with **Guidelines for successful database migration** provided in the migration wizard and select **Get started**.

.. image:: /images/products/mysql/start-migration-mysql.png
   :width: 700px
   :alt: Start the setup

Step 2 - validation
'''''''''''''''''''

1. To establish a connection to your source database, enter required source database details into the wizard:

   * Hostname
   * Port
   * Database name
   * Username
   * Password

   .. image:: /images/products/mysql/connect-source-mysql.png
      :width: 700px
      :alt: Connect to database

2. Select the **SSL encryption (recommended)** checkbox.

3. Select **Run checks** to have the connection validated.

.. topic:: Unable to use logical replication?

   If your connection check returns the **Unable to use logical replication** warning, either resolve the issues or give up using the logical replication and opt for the dump method by selecting **Start the migration using a one-time snapshot (dump method)** > **Run check** > **Start migration**.

Step 3 - migration
''''''''''''''''''

If all the checks pass with no error messages, you can trigger the migration by selecting **Start migration**.

.. image:: /images/products/mysql/ready-to-migrate-mysql.png
   :width: 700px
   :alt: Start migration

Step 4 - replicating
''''''''''''''''''''

.. _stop-migration-mysql:

1. While the migration is in progress, you can

   * Let it proceed until completed by selecting **Close window**, which closes the wizard. You come back to check the status at any time.

   * Discontinue the migration by selecting **Stop migration**, which retains the data already migrated. For information on how to follow up on a stopped migration process, see :ref:`Start over <start-over-mysql>`.

   .. image:: /images/products/mysql/migration-in-progress-mysql.png
      :width: 700px
      :alt: Set up migration

   .. warning::

      To avoid conflicts and replication issues while the migration is ongoing

      * Do not write to any tables in the target database that are being processed by the migration tool.
      * Do not change the replication configuration of the source database manually. Don't modify ``wal_level`` or reduce ``max_replication_slots``.
      * Do not make database changes that could disrupt or prevent the connection between the source database and the target database. Do not change the source database's listen address and do not modify or enable firewalls on the databases.

.. topic:: Migration attempt failed?

   If you happen to get such a notification, investigate potential causes of the failure and try to fix the issues. When you're ready, trigger the migration again by selecting **Start over**.

1. When the wizard communicates the completion of the migration, select one of the following:

   * **Close connection** to disconnect the databases and stop the replication process if still active.
   * **Keep replicating** if the replication is still ongoing and you want to keep the connection open for data synchronization.

.. topic:: Replication mode active?

   Your data has been transferred to Aiven but new data is still continuously being synced between the connected databases.

.. image:: /images/products/mysql/migration-completed-mysql.png
   :width: 700px
   :alt: Set up migration

Step 5 - close
''''''''''''''

When the wizard communicates the completion of the migration without indicating an active replication process, select **Close connection**.

.. topic:: Result

   All the data in your database has been transferred to Aiven.

.. _start-over-mysql:

Start over
----------

If you :ref:`stop a migration process <stop-migration-mysql>`, you cannot restart the same process. Still, the data already migrated is retained in the target database.

.. warning::
   
   If you start a new migration using the same connection details when your *target* database is not empty, the migration tool truncates your *target* database and an existing data set gets overwritten with the new data set.

Related reading
---------------

- :doc:`Migrate to Aiven for MySQL from an external MySQL </docs/products/mysql/howto/migrate-from-external-mysql>`
- :doc:`About aiven-db-migrate </docs/products/postgresql/concepts/aiven-db-migrate>`
