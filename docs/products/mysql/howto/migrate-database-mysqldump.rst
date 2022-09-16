Backup and restore MySQL data using ``mysqldump``
=================================================

Backing up your MySQL data to another storage service is a good way to ensure access to your data in case a failure occurs. This article shows you how to copy your Aiven for MySQL data to a file, back it up to another Aiven for MySQL database, and restore it using the ``mysqldump`` `tool <https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html>`__.

Prerequisites
-------------

* The ``mysqldump`` `tool <https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html>`_ installed. Check out the `official MySQL <https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-install.html>`_ documentation on how to install it.
  
* A source MySQL database to copy your data from. We will refer to it as ``source-db``.
  
* A target MySQL database to dump your ``source-db`` data to. We will refer to it as ``target-db``.

.. tip::

    For the restore process, we recommend you pick a plan size that is large enough to store your data, so you can limit the downtime if you're performing a migration.

The below example uses Aiven for MySQL databases for both the ``source-db`` and ``target-db``. You can create the databases by going to your running service for **Aiven for MySQL** > **Databases** > **Create a new database**.


Back up the data
---------------

Variables
'''''''''

To backup the ``source-db`` data to a file called ``mydb_backup.sql`` you need to collect some information about your Aiven for MySQL ``source-db`` database. Go to your Aiven ``source-db`` service, from **Overview** page, find the following information:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Variable
     - Description
   * - ``SOURCE_DB_HOST``
     - **Host** name for the connection
   * - ``SOURCE_DB_USER``
     - **User** name for the connection
   * - ``SOURCE_DB_PORT``
     - Connection **Port** number
   * - ``SOURCE_DB_PASSWORD``
     - Connection **Password**
   * - ``DEFAULTDB``
     - Database that contains the ``source-db`` data

Commands
'''''''''

Use the following command to back up your Aiven for MySQL data to a file named ``mydb_backup.sql``:

.. code-block:: shell

    mysqldump \
    -p DEFAULTDB -P SOURCE_DB_PORT \
    -h SOURCE_DB_HOST --single-transaction \
    -u SOURCE_DB_USER --set-gtid-purged=OFF \
    --password > mydb_backup.sql


With this command, the password will be requested at the prompt; paste ``SOURCE_DB_PASSWORD`` to the terminal, then a file named ``mydb_backup.sql`` will be created with your backup data. Note that having the prompt request for the password is more secure than including the password straight away in the command. 

The ``--single-transaction`` `flag <https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_single-transaction>`_ starts a transaction in isolation mode ``REPEATABLE READ`` before running. This allows ``mysqldump`` to read the database in its current state at the time of the transaction, ensuring consistency of the data.

.. warning::

  If you are using `Global Transaction Identifiers <https://dev.mysql.com/doc/refman/5.7/en/replication-gtids-concepts.html>`_ (GTIDs) with InnoDB use the ``--set-gtid-purged=OFF`` `option <https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_set-gtid-purged>`_. The reason is that GTID's are not available with MyISAM.

Restore the data
----------------

Variables
'''''''''

To restore data saved in a file to an Aiven for MySQL database, you need to include the connection information for the service in the ``mysqldump`` command. Go to your Aiven ``target-db`` service, on the **Overview** page find the following information:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Variable
     - Description
   * - ``TARGET_DB_HOST``
     - **Host** name for the connection
   * - ``TARGET_DB_USER``
     - **User** name for the connection
   * - ``TARGET_DB_PORT``
     - Connection **Port** number
   * - ``TARGET_DB_PASSWORD``
     - Connection **Password**
   * - ``DEFAULTDB``
     - Database that contains the ``target-db`` data

Commands
'''''''''

Run the following command to load your saved data into your Aiven for MySQL database:

.. code-block:: shell

    mysqldump \
    -p DEFAULTDB -P TARGET_DB_PORT \
    -h TARGET_DB_HOST \
    -u TARGET_DB_USER \
    --password < mydb_backup.sql

The password will be requested at the prompt. You can paste ``TARGET_DB_PASSWORD`` into the terminal. Your data should be stored in your Aiven for MySQL ``target-db``. You can check out ``mysqlcheck`` `command <https://dev.mysql.com/doc/refman/8.0/en/mysqlcheck.html>`_ to perform further analysis of your current MySQL data.


Read more about migrations
--------------------------

- :doc:`How to migrate to Aiven for MySQL from an external MySQL </docs/products/mysql/howto/migrate-from-external-mysql>`
- :doc:`How to perform migration check on your Aiven for MySQL database </docs/products/mysql/howto/migrate-from-external-mysql>`