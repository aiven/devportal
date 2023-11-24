Migrate Aiven for Redis®•* to Aiven for Dragonfly
=====================================================

Migrating your database from Aiven for Redis to Aiven for Dragonfly is a significant step in enhancing your data infrastructure's scalability and performance. The Aiven Console provides a user-friendly wizard to assist with this migration process.

Prerequisites
-------------

Before you begin the migration, ensure you have:

* A target Aiven for Dragonfly service. For creation instructions, see `Get started with Aiven for Dragonfly`_.
* Source database details including:
  
  * **Hostname or connection string:** The public hostname, connection string, or IP address for database connection. See `Public Internet Access <../platform/howto/public-access-in-vpc>`_ for more details.
  * **Port:** The port number used for database connections.
  * **Username:** The username with sufficient permissions for data migration.
  * **Password:** The password for database access.

* Updated or disabled firewalls to allow traffic and connections between the source and target databases.
* An SSL-secured source Redis service.
* A publicly accessible source Redis service or one with a VPC peering connection. VPC ID and cloud name are needed for migration.


Migration steps
-----------------
Follow these steps to migrate an Aiven for Redis®* database to Aiven for Dragonfly: 

1. Log in to the `Aiven Console <https://console.aiven.io/>`_.
2. Choose the target Aiven for Dragonfly service for your Redis database migration.
3. From the **Overview** tab, scroll down to the **Migrate database** section.
4. Initiate the migration process by clicking on **Set up migration**.
5. A guided wizard is displayed, providing step-by-step instructions for the migration.
6. Within the wizard, choose the option to **Import an Aiven for Redis service** and proceed by clicking **Next**.
   
Step 1: Configure
~~~~~~~~~~~~~~~~~

Read the guidelines in the migration wizard and click **Get started**.

.. image:: /images/products/dragonfly/dragonfly-db-migration-get-started.png
   :width: 500px
   :alt: Database migration wizard

Step 4: Validate Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. On the **Database connection and validation** screen, enter your source database details: hostname, port, username, and password.
2. Check the **SSL encryption recommended** box.
3. Click **Run check** to validate the connection. Address any warnings before proceeding.

.. image:: /images/products/dragonfly/dragonfly-migration-validation.png
   :width: 500px
   :alt: Database connection validation

Step 5: Start Migration
~~~~~~~~~~~~~~~~~~~~~~~

On the **Database migration** screen, click **Start Migration**.

.. image:: /images/products/dragonfly/dragonfly-start-migration.png
   :width: 500px
   :alt: Starting the migration

Step 6: Monitor Migration
~~~~~~~~~~~~~~~~~~~~~~~~~

* You can close the wizard and check the migration status later in the service's overview page.
* Continue using the target database during migration.
* To stop migration, click **Stop migration**. Already migrated data will be retained.

.. note::
    Stopping the migration halts data replication but retains migrated data. You can restart migration later, overwriting previously migrated data.

Step 7: Finalize Migration
~~~~~~~~~~~~~~~~~~~~~~~~~~

When notified of migration completion:

* Choose **Close connection** to disconnect the databases and stop active replication.
* Select **Keep replicating** for ongoing data synchronization.

.. image:: /images/products/dragonfly/dragonfly-migration-complete.png
   :width: 500px
   :alt: Migration completion

.. topic:: Replication Mode Active?

    Post-migration, your data is now in Aiven for Dragonfly, with continuous synchronization for any new data.

Troubleshooting
---------------

If a migration attempt fails, investigate and resolve the underlying issues before restarting the migration process.

Conclusion
----------

Following these steps will successfully migrate your Redis database to Aiven for Dragonfly, leveraging its advanced capabilities for improved performance and scalability.

Related Articles
----------------

* `Migrate Aiven for Redis <../products/redis/howto/migrate-aiven-redis>`_
