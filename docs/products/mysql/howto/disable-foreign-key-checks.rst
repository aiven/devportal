Disable foreign key checks
==========================

For several reasons, it can sometimes be useful to disable foreign key checks on a database. The setting controlling this behaviour is foreign_key_checks.

This may be useful, for example, if you are attempting to restore a database which will cause foreign key violations while you are migrating to Aiven for MySQL, you will see an error similar to:

.. code-block:: shell

    ERROR 3780 (HY000) at line 11596: Referencing column 'g_id' and referenced column 'g_id' in foreign key constraint 'FK_33b11dcfac6148578da087b07c2f388f' are incompatible.

There are a few implications to consider when altering this setting, these are covered in more detail in the MySQL documentation here and here. Aiven for MySQL has this set to the MySQL default, this can be seen by running:

.. code-block:: shell

    MySQL [(none)]> SHOW VARIABLES LIKE 'foreign_key_checks';
    +--------------------+-------+
    | Variable_name      | Value |
    +--------------------+-------+
    | foreign_key_checks | ON    |
    +--------------------+-------+
    1 row in set (0.021 sec)

To change this setting temporarily for the duration of a session is simple and requires passing only an single additional parameter to the ``mysql`` command:

.. code-block:: shell

    --init-command="SET @@SESSION.foreign_key_checks = 0;"

For example the full command I use to connect to a temporary developer service is:

.. code-block:: shell

    mysql -u avnadmin -p'mypassword' -P 12691 -h myservice.aivencloud.com --init-command="SET @@SESSION.foreign_key_checks = 0;"

After logging in we can see that the variable value has changed:

.. code-block:: shell

    MySQL [(none)]> SHOW VARIABLES LIKE 'foreign_key_checks';
    +--------------------+-------+
    | Variable_name      | Value |
    +--------------------+-------+
    | foreign_key_checks | OFF   |
    +--------------------+-------+
    1 row in set (0.022 sec)
    
This even works when redirecting input from a SQL file:

.. code-block:: shell

    mysql -u avnadmin -p'mypassword' -P 12691 -h myservice.aivencloud.com --init-command="SET @@SESSION.foreign_key_checks = 0;" < mysqlfile.sql
    Variable_name   Value
    foreign_key_checks      OFF