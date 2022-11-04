Manage ClickHouse® databases and tables
=======================================

About databases and tables
--------------------------

Databases and tables are at the core of any **Database Management System**. ClickHouse® is no different. In this article, we will look at how to create and work with databases and tables in Aiven for ClickHouse®.

Create a database
-----------------

Creating databases in an Aiven for ClickHouse service can only be done via the Aiven platform; the `admin` user is not allowed to create databases directly for security and reliability reasons. However, you can create a new database through the web interface of `Aiven console <https://console.aiven.io/>`_:

#. Log in to `Aiven console <https://console.aiven.io/>`_ and select your service.
#. On the service page, open the **Databases & Tables** tab.
#. Enter your database name in **Create a new database** and select **Create database**.

   You'll see the name of the database appear in the *Database List* section.
   On our side, we enable necessary customizations and run secondary queries to grant access to the admin user.

Remove a database
-----------------

Similar to creating the database, removal should also be done through the Aiven platform. In the web interface of `Aiven console <https://console.aiven.io/>`_ you'll find delete button next to the database you created in the *Database List*.

.. note::

    If you try adding or removing a database in **Aiven for ClickHouse** through the command line, you'll encounter an exception ``Not enough privileges.(ACCESS_DENIED)``. Please use the Aiven web interface to add or remove a database.

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

Part of the table definition includes a targeted table engine. The full list of supported table engines in **Aiven for ClickHouse** can be found :doc:`in this article <../reference/supported-table-engines>`. **Aiven for ClickHouse** uses "Replicated" variants of table engines to ensure high availability. Even if you select ``MergeTree`` engine, we will automatically use the replicated variant on our side.

With this knowledge, try out an example dataset described :doc:`over here <../sample-dataset>`.
