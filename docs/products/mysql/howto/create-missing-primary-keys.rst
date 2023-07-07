Create missing primary keys
===========================

Primary keys are important :ref:`for MySQL replication process <myslq-replication-overview>`. In this article, you can find strategies to create missing primary keys in your Aiven for MySQL® service. 

List tables without primary key
'''''''''''''''''''''''''''''''

Once you are connected to the MySQL database, you can determine which tables are missing primary keys by running the following commands:

.. code-block:: shell

    SELECT    
        tab.table_schema AS database_name,
        tab.table_name AS table_name,
        tab.table_rows AS table_rows
    FROM information_schema.tables tab
    LEFT JOIN information_schema.table_constraints tco          
        ON (tab.table_schema = tco.table_schema              
            AND tab.table_name = tco.table_name
            AND tco.constraint_type = 'PRIMARY KEY')
    WHERE
        tab.table_schema NOT IN ('mysql', 'information_schema', 'performance_schema', 'sys')
        AND tco.constraint_type IS NULL
        AND tab.table_type = 'BASE TABLE'; 


To see the exact table definition for the problematic tables you can run the following command:

.. code-block:: shell

    SHOW CREATE TABLE database_name.table_name;

If your table already contains a column or set of columns that can be used as primary key or composite key, then using such column(s) is recommended.

In the next sections, find examples of tables definitions and the guidance on how to create the missing primary keys.

Example: add primary key
''''''''''''''''''''''''

.. code-block:: shell

    CREATE TABLE person (
    social_security_number VARCHAR(30) NOT NULL,
    first_name TEXT,
    last_name TEXT
    );

You can create the missing primary key by adding the primary key:

.. code-block:: shell

    ALTER TABLE person ADD PRIMARY KEY (social_security_number);

You don't have to explicitly define it as UNIQUE, `as the primary key is always unique in MySQL <https://dev.mysql.com/doc/refman/8.0/en/primary-key-optimization.html>`_.

Example: add a new separate id column
'''''''''''''''''''''''''''''''''''''

.. code-block:: shell

    CREATE TABLE team_membership (
    user_id BIGINT NOT NULL,
    team_id BIGINT NOT NULL
    );

Add the primary key using the following query:

.. code-block:: shell

    ALTER TABLE team_membership ADD PRIMARY KEY (user_id, team_id); 

If none of the existing columns or a combination of the existing columns cannot be used as the primary key, add a new separate id column. Check how to deal with it in :ref:`Example: alter table error <myslq-alter-table-error>`.

.. code-block:: shell

    ALTER TABLE mytable ADD id BIGINT PRIMARY KEY AUTO_INCREMENT;

.. _myslq-alter-table-error:

Example: alter table error ``mysql.innodb_online_alter_log_max_size``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

When executing the ``ALTER TABLE`` statement for a large table, you may encounter an error similar to the following:

.. code-block:: shell
    
    Creating index 'PRIMARY' required more than 'mysql.innodb_online_alter_log_max_size' bytes of modification log. Please try again.

For the operation to succeed, you need to set a value that is high enough. Depending on the table size, this could be a few gigabytes or even more for very large tables. You can change ``mysql.innodb_online_alter_log_max_size`` as follows: `Aiven Console <https://console.aiven.io/>`_ > your Aiven for MySQL service > the **Overview** page of your service > the **Advanced configuration** section > **Change** > **Add configuration option** > ``mysql.innodb_online_alter_log_max_size`` > set a value > **Save advanced configuration**.

.. seealso::
    
    Learn how to :doc:`create new tables without primary keys </docs/products/mysql/howto/create-tables-without-primary-keys>` in your Aiven for MySQL.
