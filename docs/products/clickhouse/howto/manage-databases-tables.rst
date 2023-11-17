Manage ClickHouse® databases and tables
=======================================

Databases and tables are at the core of any Database Management System. ClickHouse® is no different. In this article, we will look at how to create and work with databases and tables in Aiven for ClickHouse®.

.. _create-a-clickhouse-database:

Create a database
-----------------

Creating databases in an Aiven for ClickHouse service can only be done via the Aiven platform; the `admin` user is not allowed to create databases directly for security and reliability reasons. However, you can create a new database through the web interface of `Aiven console <https://console.aiven.io/>`_:

1. Log in to the  `Aiven Console <https://console.aiven.io/>`_, and select your service from the **Services** page.
2. In your service's page, select **Databases and tables** from the sidebar.
3. In the **Databases and tables** page, select **Create database** > **ClickHouse database**.
4. In the **Create ClickHouse database** window, enter a name for your database and select **Create database**.

   You'll see the name of the database appear in the list of databases in the **Databases and tables** page.
   On our side, we enable necessary customizations and run secondary queries to grant access to the admin user.

Remove a database
-----------------

Similar to creating the database, removal should also be done through the Aiven platform. In the web interface of `Aiven console <https://console.aiven.io/>`_ you'll find a delete button next to the database you created in the list of databases in the **Databases and tables** page.

.. note::

    If you try adding or removing a database in for your Aiven for ClickHouse service through the command line, you'll encounter an exception ``Not enough privileges.(ACCESS_DENIED)``. Please use the Aiven web interface to add or remove a database.

Create a table
--------------

Tables can be added with an SQL query, either with the help of the web query editor or with CLI. In both cases, the SQL query looks the same. The example below shows a query to add new table ``expenses`` to ``transactions`` database. To keep it simple, this example has an unrealistically small amount of columns:

.. code:: sql

        CREATE TABLE transactions.expenses (
            Title String,
            Date DateTime,
            UserID UInt64,
            Amount UInt32
        )
        ENGINE = ReplicatedMergeTree ORDER BY Date;

Select a table engine
^^^^^^^^^^^^^^^^^^^^^

Part of the table definition includes a targeted table engine. The full list of supported table engines in Aiven for ClickHouse can be found :doc:`in this article <../reference/supported-table-engines>`. Aiven for ClickHouse uses ``replicated`` variants of table engines to ensure high availability. Even if you select ``MergeTree`` engine, we will automatically use the replicated variant on our side.

With this knowledge, try out an example dataset described :doc:`over here </docs/products/clickhouse/howto/load-dataset>`.

Remove a table
--------------

A table can be removed using either CLI or `Aiven Console <https://console.aiven.io/>`_.

.. note::

   You can remove a table of any size if you have the ``DROP`` permission since parameters
   ``max_table_size_to_drop`` and ``max_partition_size_to_drop`` are disabled for Aiven
   services. Consider :doc:`granting
   </docs/products/clickhouse/howto/manage-users-roles>` only necessary permissions to your database users.

Remove a table with CLI
^^^^^^^^^^^^^^^^^^^^^^^

Run the following SQL command to remove your table:

.. code-block:: bash

   DROP TABLE NAME_OF_YOUR_DATABASE.NAME_OF_YOUR_TABLE;

Remove a table in the console
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To remove your table in `Aiven Console <https://console.aiven.io/>`_, take the following steps:

1. Log in to the  `Aiven Console <https://console.aiven.io/>`_.
2. Navigate to the table you want to remove: organization > project > service > **Databases and tables**.
3. In the **Databases and tables** view, navigate to the table and select **Actions** menu (**...**) > **Remove** > **Delete table**.
