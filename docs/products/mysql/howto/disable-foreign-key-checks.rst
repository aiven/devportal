Disable foreign key checks
==========================

It can be useful to know how to disable foreign key checks. For example, your migration to Aiven for MySQL may face foreign key violations which can result in an error, similar to::

  ERROR 3780 (HY000) at line 11596: Referencing column 'g_id' and referenced column 'g_id' in foreign key constraint 'FK_33b11dcfac6148578da087b07c2f388f' are incompatible.

In this article, we will explain how to temporarily disable Aiven for MySQL foreign key checking for the duration of a session. 

.. note::

    Aiven for MySQL has by default foreign key checks enabled.

Prerequisites
-------------

* The ``mysqlsh`` client installed. You can install this by following the MySQL shell installation `documentation <https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-install.html>`_.

* An Aiven account with an Aiven for MySQL service running.

Variables
---------

You need those variables to run the commands. You can find this information in the **Overview** tab of your on your Aiven for MySQL service, under **MySQL** tab.

.. list-table::
  :header-rows: 1
  :widths: 15 60
  :align: left

  * - Variable
    - Description
  * - ``USER_HOST``
    - Hostname for MySQL connection
  * - ``USER_PORT``
    - Port for MySQL connection
  * - ``USER_PASSWORD``
    - Password of your Aiven for MySQL connection
  * - ``DB_NAME``
    - Database Name of your Aiven for MySQL connection

Disable foreign key checks
--------------------------

You can connect to your Aiven for MySQL following this command::
    
    mysql --user avnadmin --password=USER_PASSWORD --host USER_HOST --port USER_PORT DB_NAME

After connecting, you can run the following command to check the default configuration for your foreign key checks.

.. code:: shell

    mysql> SHOW VARIABLES LIKE 'foreign_key_checks';

As result, you can verify that the foreign keys are enabled by default. This is the output you will see:

.. code::

    +--------------------+-------+
    | Variable_name      | Value |
    +--------------------+-------+
    | foreign_key_checks | ON    |
    +--------------------+-------+
    1 row in set (0.05 sec)

To disable the foreing key checks for the session, you give an additional parameter when you connect to your Aiven for MySQL using the ``mysqlsh``:

.. code::shell

    mysql --user avnadmin --password=USER_PASSWORD --host USER_HOST --port USER_PORT DB_NAME --init-command="SET @@SESSION.foreign_key_checks = 0;"

Once again, we can check the current status of the foreign key checks by running::

  mysql> SHOW VARIABLES LIKE 'foreign_key_checks';

As result, we can see that the foreign key checks are disabled for this session:

.. code::

    +--------------------+-------+
    | Variable_name      | Value |
    +--------------------+-------+
    | foreign_key_checks | OFF   |
    +--------------------+-------+
    1 row in set (0.04 sec)


More resources
--------------

Read the official documentation to understand possible implications that can happen when disabling foreign key checks in your service.

- `Foreign Key Checks <https://dev.mysql.com/doc/refman/8.0/en/create-table-foreign-keys.html#foreign-key-checks>`_.

- `Server System Variables <https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_foreign_key_checks>`_.