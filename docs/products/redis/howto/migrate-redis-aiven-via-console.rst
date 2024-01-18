Migrate from Redis®* to Aiven for Redis®* using Aiven Console
===============================================================

Redis®* is an open-source, in-memory data structure store used as a database, cache, message broker, and streaming engine.

Migrating your Redis®* databases, whether on-premise or cloud-hosted, to Aiven for Redis®* managed service is straightforward. The Aiven console provides a guided wizard to assist you with the migration process.

.. Important::

    Migrating from Google Cloud Memorystore for Redis®* is not currently supported.


Prerequisites
-------------
Before starting the migration process, ensure you have the following: 

* A target Aiven for Redis®* service. To create one, see :doc:`/docs/products/redis/get-started`.
* Source database information:

  * **Hostname or connection string:** This is the public hostname, connection string, or IP address used to connect to the database. Refer to :doc:`accessible from the public Internet </docs/platform/howto/public-access-in-vpc>`.
  * **Port:** The port used to connect to the database. 
  * **Username:** The username used to connect to the database. Ensure this user has sufficient permissions to access the data you want to migrate.
  * **Password:** The password used to connect to the database.

* To enable traffic and connection between the source and target databases, ensure that you update or disable the firewalls that protect them. If necessary, you can temporarily disable the firewalls.
* A source Redis®* service that is secured with SSL is a default migration requirement.
* A publicly accessible source Redis®* service or a service with a VPC peering connection between private networks. The VPC ID and cloud name are required for the migration process.

.. Note::
    AWS ElastiCache for Redis®* instances cannot have public IP addresses and thus require project VPC and peering connection.

Migrate a Redis®* database
-----------------------------

Follow these steps to migrate a Redis®* database to Aiven for Redis®* service: 

1. Log in to the `Aiven Console <https://console.aiven.io/>`_, and select the target Aiven for Redis®* service to which you want to migrate the Redis®* database. 
2. Click **Service settings** on the sidebar. 
3. Scroll to the **Service management** section, and click **Actions** (**...**) menu. 
4. Click **Import database** to initiate the import process. 
5. You will see a wizard that guides you through the database migration process. 

Step 1: Configure
`````````````````````
Read through the guidelines on the Redis migration wizard and select **Get started** to proceed with the database migration.

.. image:: /images/products/redis/redis-db-migration-get-started.png
    :width: 500px
    :alt: Screenshot of the database migration wizard

Step 2: Validation
`````````````````````
1. On the **Database connection and validation** screen, enter the following information to establish a connection to your source database:

   * **Hostname:** This is the public hostname, connection string, or IP address used to connect to the database.
   * **Port:** The port used to connect to the database.
   * **Username:** The username used to connect to the database.
   * **Password:** The password used to connect to the database.

2. Select the **SSL encryption recommended** checkbox.
3. Select the **Run check** to validate the connection. If the check returns any warning, resolve the issues before proceeding with the migration process.

   .. image:: /images/products/redis/redis-migration-validation.png
       :width: 500px
       :alt: Connect to database

Step 3: Migration
```````````````````
On the **Database migration** screen, select **Start Migration** to begin the migration.

.. image:: /images/products/redis/redis-start-migration.png
    :width: 500px
    :alt: Start database migration

While the migration is in progress, you can

* Close the wizard by selecting **Close window** and check the migration status anytime by returning to the wizard from the service's overview page. 
* Continue to write to the target database.
* Stop the migration by selecting **Stop migration**. The migrated data will be retained, and you can start a new migration.

.. note:: 
    If you choose to stop the migration, this action will immediately halt the replication of your data. However, any data that has already been migrated to Aiven will be retained. You can initiate a new migration later, and this process will overwrite any previously migrated databases.

.. topic:: Migration attempt failed?

    If you receive such a notification, it is important to investigate the possible causes of the failure and address the issues. Once you have resolved the underlying problems, you can initiate the migration by choosing **Start over**.


Step 4: Close 
```````````````
When the wizard informs you about the completion of the migration, you can choose one of the following options:

* Select **Close connection** to disconnect the databases and stop the replication process if it is still active.
* Select **Keep replicating** if the replication is ongoing and you wish to maintain the connection open for continuous data synchronization.

  .. image:: /images/products/redis/redis-migration-complete.png
    :width: 500px
    :alt: Close database connection

.. topic:: Replication mode active?

    Your data has been successfully migrated to the designated Aiven for Redis database, and any subsequent additions to the connected databases are being continuously synchronized. 

Related pages
----------------

*  :doc:`/docs/products/redis/howto/migrate-aiven-redis` 

