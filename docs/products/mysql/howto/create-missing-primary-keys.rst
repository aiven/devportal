Create missing primary keys
===========================

Find here strategies to create missing primary keys in your Aiven for MySQL service. First, you can determine which tables are missing primary keys by running:

.. code::

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


To see the exact table definition for the problematic tables you can do:

.. code::

    SHOW CREATE TABLE database_name.table_name;

If your table already contains a column or set of columns that can be used as primary key or composite key, then using such column(s) is recommended. Here are some examples of tables definitions and how to create the missing primary keys:

Example: adding primary key
'''''''''''''''''''''''''''

.. code::

    CREATE TABLE person (
    social_security_number VARCHAR(30) NOT NULL,
    first_name TEXT,
    last_name TEXT
    );

You can create the missing primary key by first adding the primary key:

.. code::

    ALTER TABLE person ADD PRIMARY KEY (social_security_number);

You don't have to explicitly define it as UNIQUE, `as primary key is always unique in MySQL <https://dev.mysql.com/doc/refman/8.0/en/primary-key-optimization.html>`_.

Example: add a new separate id column
'''''''''''''''''''''''''''''''''''''

.. code::

    CREATE TABLE team_membership (
    user_id BIGINT NOT NULL,
    team_id BIGINT NOT NULL
    );

Same as before, add the primary key by following:

.. code::

    ALTER TABLE team_membership ADD PRIMARY KEY (user_id, team_id); 

If none of the existing columns or a combination of the existing columns can not be used as the primary key, then you should add a new separate id column.

.. code::

    ALTER TABLE mytable ADD id BIGINT PRIMARY KEY AUTO_INCREMENT;

When executing the ``ALTER TABLE`` statement for a large table, you may encounter an error like this:

.. code::
    
    Creating index 'PRIMARY' required more than 'innodb_online_alter_log_max_size' bytes of modification log. Please try again.

You will need to set a high enough value for the operation to succeed. Depending on the table size this could be a few gigabytes or even more for very large tables. You can change the ``innodb_online_alter_log_max_size`` by selecting your Aiven for MySQL service and go to **Overview** > **Advanced configuration** > **Change** > **Add configuration option** to add the parameter and make changes.


.. seealso::
    
    Learn how to :doc:`create new tables without primary keys </docs/products/mysql/howto/create-tables-without-primary-keys>` in your Aiven for MySQL.