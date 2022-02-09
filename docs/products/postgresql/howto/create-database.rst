Create additional PostgreSQL databases
=============================================

Once you've created your PostgreSQL service, you can add additional databases


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

1. Prepare the command to add the database to your PostgreSQL service.

2. Add the ``postgresql_service`` parameter to specify the service for which you want to create a new database, and the ``database_name`` for the new database. For instance, to add the topic ``database_name`` to the service ``PostgreSQL_service``, you would use this command::

    avn service topic-create --dbname  postgresql_service 

The changes are applied immediately.

Using a PostgreSQL client (CLI)
-------------------------------------

1. :doc:`Connect to your service  <connect-psql>` using  the ``psql`` utility.

2. Run the following command from the PostgreSQL prompt::

    CREATE DATABASE database_name;

