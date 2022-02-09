Create additional MySQL databases
==================================

Once you've created your MySQL service, you can add additional databases


Using the Aiven web console
----------------------------

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. On the **Services** page, click on the service name.

3. Select the **Databases** tab:

   a. Enter a name for your database.

4. Click **Add database** on the right hand side of the console.

   The new database will be visible immediately.

Using the Aiven client (CLI)
-----------------------------

1. Prepare the command to add the database to your MySQL service.

2. Add the ``mysql_service`` parameter to specify the service for which you want to create a new database, and the ``database_name`` for the new database. For instance, to add the topic ``database_name`` to the service ``mysql_service``, you would use this command::

    avn service topic-create --dbname  mysql_service 

The changes are applied immediately.

Using a MySQL client (CLI)
-----------------------------

1. :doc:`Connect to your service <connect-from-cli>` using either the ``mysqlsh`` or ``mysql`` utilities.
2. Run the following command from the MySQL prompt::

    CREATE DATABASE database_name;

