Migrate your MySQL data using ``mysqldump``
===========================================

Performing the backup of your MySQL data to another storage service is a good way to ensure access to your data in case a failure occurs. In this article, you can find out how to copy your Aiven for MySQL data to a file and backup to another Aiven for MySQL database using ``mysqldump`` `tool <https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html>`__.

Prerequisites
-------------

* The ``mysqldump`` `tool <https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html>`_ installed. Check out the `official MySQL <https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-install.html>`_ documentation on how to install it.
  
* A MySQL database that we aim to copy our data from. We will refer to it as ``source-db``.
  
* A target MySQL database that we aim to dump our ``source-db`` data. We will refer to it as ``target-db``.

.. tip::

    For the dumping process, we recommend you pick a plan size that is large enough to store your data, so you can limit the downtime during migration.

To simplify the example, we'll create Aiven for MySQL databases for both, ``source-db`` and ``target-db``. You can create the databases by going to your running service for **Aiven for MySQL** > **Databases** > **Create a new database**.


Backup the data
---------------

First, we will back up our ``source-db`` data to a file called ``mydb_backup.sql``. For that, you need to collect some information about your Aiven for MySQL ``source-db`` database. Go to your Aiven ``source-db`` service, from **Overview** page, find the following information:

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

Use the following command to backup your Aiven for MySQL data to the ``mydb_backup.sql`` file:

.. code-block:: shell

    mysqldump \
    -p DEFAULTDB -P SOURCE_DB_PORT \
    -h SOURCE_DB_HOST --single-transaction \
    -u SOURCE_DB_USER --set-gtid-purged=OFF \
    --password > mydb_backup.sql


With this command, the password will be requested at the prompt; paste ``SOURCE_DB_PASSWORD`` to the terminal, then a file named ``mydb_backup.sql`` will be created with your backup data.

.. note::
  
  Having the prompt request for the password is more secure than including the password straight away in the command. 

The ``--single-transaction`` `flag <https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_single-transaction>`_ starts a transaction before running. This means that the process does not lock the entire database. This allows ``mysqldump`` to read the database in the current state at the time of the transaction which ensures that your data is reliable


.. warning::
    
    If you are using `Global Transaction Identifiers <https://dev.mysql.com/doc/refman/5.7/en/replication-gtids-concepts.html>`_ (GTIDs) with InnoDB use the ``--set-gtid-purged=OFF`` `option <https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html#option_mysqldump_set-gtid-purged>`_. The reason is that GTID's are not available with MyISAM.

Restore the data
----------------

You can back up the data previously saved in a file to an Aiven for MySQL database. You need to collect some information about your Aiven for MySQL ``target-db`` to restore the data. Go to your Aiven ``target-db`` service, from **Overview** page, find the following information:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Variable
     - Description
   * - ``TARGET_DB_HOST``
     - Service host name
   * - ``TARGET_DB_USER``
     - Service user name
   * - ``TARGET_DB_PORT``
     - Port number to use
   * - ``TARGET_DB_PASSWORD``
     - Connection password
   * - ``DEFAULTDB``
     - Database that contains the ``target-db`` data

Run the following command to store your saved data to your Aiven for MySQL database:

.. code-block:: shell

    mysqldump \
    -p DEFAULTDB -P TARGET_DB_PORT \
    -h TARGET_DB_HOST \
    -u TARGET_DB_USER \
    --password < mydb_backup.sql

The password will be requested at the prompt. You can paste ``TARGET_DB_PASSWORD`` to the terminal. Your data should be stored in your Aiven for MySQL ``target-db``. You can check out ``mysqlcheck`` `command <https://dev.mysql.com/doc/refman/8.0/en/mysqlcheck.html>`_ to perform further analyzes of your current MySQL data.


Read more about migrations
--------------------------

- :doc:`How to migrate to Aiven for MySQL from an external MySQL </docs/products/mysql/howto/migrate-from-external-mysql>`
- :doc:`How to perform migration check on your Aiven for MySQL database </docs/products/mysql/howto/migrate-from-external-mysql>`