Migrate from Redis® database to Aiven using Aiven Console
==========================================================

Redis® is an open source, in-memory data structure store used as a database, cache, message broker, and streaming engine. 

Migrating your Redis® databases, whether on-premise or cloud-hosted, to Aiven for Redis® managed service is a straightforward process. The Aiven console provides a guided wizard to assist you with the migration process.

.. Important::

    Migrating from Google Cloud Memorystore for Redis® is not currently supported.


Prerequisites
-------------
Before starting the migration process, ensure you have the following: 

* A target Aiven for Redis® service. To create one, see :doc:`/docs/products/redis/get-started`.
* Source database information:

  * **Hostname or connection string:** This is the public hostname, connection string, or IP address used to connect to the database. Refer to :doc:`accessible from the public Internet </docs/platform/howto/public-access-in-vpc>`.
  * **Port:** - The port used to connect to the database. 
  * **Username:** - The username used to connect to the database. Ensure this user has sufficient permissions to access the data you want to migrate.
  * **Password:** - The password used to connect to the database.

* Update or disable firewalls between the databases: Make sure to update or disable firewalls that protect the source and target databases to allow traffic and connection between them. If needed, you can temporarily disable the firewalls.
* A source Redis® service that is secured with SSL, which is a default requirement for migration.
* A publicly accessible source Redis® service or a service with a VPC peering connection between private networks. Tthe VPC ID and cloud name are required for the migration process.

.. Note::
    AWS ElastiCache for Redis® instances cannot have public IP addresses, and thus require project VPC and peering connection.

Migrate Redis® database
------------------------

Follow these steps to migrate a Redis® database to Aiven for Redis® service: 

1. Log in to the `Aiven Console <https://console.aiven.io/>`_, and select the target Aiven for Redis® service to which you want to migrate the Redis® database. 
2. From the **Overview** tab, scroll down to the **Migrate database** section. 
3. Select **Set up migration**.
4. You will see a wizard that guides you through the database migration process. 
5. On the migration wizard, read through the guidelines and select **Get started** to proceed with the database migration.
6. On the **Database connection and validation** screen, enter the following information to establish a connection to your source database:
   
   * **Hostname:** This is the public hostname, connection string, or IP address used to connect to the database.
   * **Port:** The port used to connect to the database.
   * **Database name:** Name of the database you want to migrate.
   * **Username:** The username used to connect to the database.
   * **Password:** The password used to connect to the database.

7. Enable SSL encryption (recommended) by selecting the corresponding checkbox.
8. Select the **Run check** to check the connection. If the test returns any warning, resolve the issues before proceeding with the migration process.
9.  On the **Database migration** screen, select **Start Migration** to begin the migration.
10. While the migration is in progress, you can
    
    * You can close the wizard by selecting **Close window** and check the migration status anytime by returning to the wizard. 
    * You can continue to write to the target database.
    * Stop the migration by selecting **Stop migration**. The migrated data will be retained, and you can start a new migration.
    
    .. note:: 
        If you choose to stop the migration, this action will immediately halt the replication of your data. However, any data that has already been migrated to Aiven will be retained. You can initiate a new migration later, and this process will overwrite any previously migrated databases.

11. Once the migration is complete, select **Close connection** to exit the wizard.

Related articles
----------------

* Migrate to Aiven for Redis® using CLI :doc:`/docs/products/redis/howto/migrate-aiven-redis` 

