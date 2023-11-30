Migrate xxternal Redis databases to Aiven for Dragonfly®
===========================================================================

Redis is an in-memory data structure store commonly used as a database, cache, message broker, and queue. The Aiven Console provides an intuitive wizard to facilitate the migration of your external Redis databases to Aiven for Dragonfly.

.. important::
   The migration of databases from Google Cloud Memorystore for Redis is not supported at this time.

Prerequisites
-------------

Before starting the migration process, ensure you have the following:

* A target Aiven for Dragonfly service set up and ready. For setup instructions, see to :doc:`/docs/products/dragonfly/get-started`.
* Source database information:

  * **Hostname or connection string:** The public hostname, connection string, or IP address used to connect to the database, which should be :doc:`accessible from the public Internet </docs/platform/howto/public-access-in-vpc>`.
  * **Port:** The port number used for connecting to the database.
  * **Username:** The username with appropriate permissions for accessing the database data you intend to migrate.
  * **Password:** The password associated with the username.

* Ensure firewalls allow traffic between databases or disable them temporarily.
* The source Redis database must be SSL-secured, a standard migration requirement.
* If the source Redis service is not publicly accessible, establish a VPC peering connection between the private networks. You will need the VPC ID and cloud name for the migration.

.. note::
   Instances such as AWS ElastiCache for Redis that do not have public IP addresses will require a VPC and peering connection to establish a migration.


Database migration steps
--------------------------

To migrate a Redis database to Aiven for Dragonfly:

1. Log in to the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Dragonfly service to which you want to migrate your Redis database.
2. Navigate to **Service settings** from the sidebar.
3. Scroll to the **Service management** section and use the ellipsis to view additional menu options.
4. Select **Import database** to initiate the import process.


Step 1: Configure
``````````````````
Start by reviewing the database migration configuration guidelines. Confirm compatibility with Dragonfly and proceed as follows:

* Select **Import an external Redis database**.
* Click **Get started** to begin the migration.

Step 2: Validation
````````````````````
Enter the required details to establish a connection with your source Redis database:

* **Hostname:** The public hostname, connection string, or IP address for the database connection.
* **Port:** The port number used for connections.
* **Username:** The username required to access your database.
* **Password:** The password for database access.
* Select the SSL encryption option for a secure migration and click **Run check** to verify the connection.

.. important::
   Address any issues that arise to ensure a smooth migration. Note that not all components of your Redis setup will be migrated. User accounts, ACLs, configurations, and active commands or scripts will not be transferred, but all database data and its content will be.

Step 3: Migration
````````````````````

Once all the necessary checks have been completed successfully, you can proceed with the migration process.

* Select **Start migration** to initiate th data migration process to Aiven for Dragonfly.

Migration in progress
'''''''''''''''''''''''

During the migration, you can:

* Close the migration wizard by clicking **Close window** and later return to monitor the migration status from the service overview page.
* The migration duration varies based on the size of your database. You can continue writing to the target database during migration but avoid manual changes that might impact replication.
* Certain managed database features will be disabled while the mirgration is in progress. 
* If necessary, stop the migration by selecting **Stop migration**. Data that has already been migrated will remain on Aiven.

.. warning::
   
   * Stopping this migration will immediately halt the ongoing replication process, preserving the data already transferred to Aiven. You have the option to  initiate a new database migration at any time in the future, which will overwrite the entire database and its contents on Aiven with the latest data from the source.
   * Avoid actions that could disrupt the replication process, such as changing replication configurations or firewall settings.

Step 4 - Close and post-migration steps
``````````````````````````````````````````
Once the migration is complete:

* Click **Close connection** to end replication. 
* Click **Keep replicating** to maintain ongoing data synchronization.

.. warning:: 
   
   System updates or any configuration changes during replication may restart nodes and trigger a new database migration. Before making any modifications, confirm that replication is either complete or stopped.

.. topic:: Replication Mode Active?

   Newly added data to the original Redis database will continue to sync with your Aiven for Dragonfly service until you decide to stop replication.




Related Reading
---------------
* Migrating to Aiven for Dragonfly 
* Aiven for Dragonfly documentation </docs/products/dragonfly/index>`


