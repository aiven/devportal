Create new tables without primary keys
======================================

If you Aiven for MySQL was created after 2020-06-03, then by default your Aiven for MySQL does not allow creating new tables without primary keys. You can check this by following those steps:

#. Select the Aiven for MySQL service that you want to check.
#. On the **Overview** tab, in the **Advanced configuration** section, click **Change**.
#. Find the ``mysql.sql_require_primary_key`` parameter

If you ``mysql.sql_require_primary_key`` is enabled, then your Aiven for MySQL does not allow to create new tables without primary keys.

When this ``mysql.sql_require_primary_key`` is enabled, you won't be able to create tables without primary keys. You will get the following error message:

.. code::
    Unable to create or change a table without a primary key, when the system variable 'sql_require_primary_key' is set. Add a primary key to the table or unset this variable to avoid this message. Note that tables without a primary key can cause performance problems in row-based replication, so please consult your DBA before changing this setting.

If creating tables without primary keys is prevented and the table that you're trying to create is known to be small you may override this setting and create the table anyway. 

.. seealso::
    You can read more about MySQL replication in the :ref:`Replication Overview <myslq-replication-overview>` article.

You have two options to create the tables:

* Setting ``sql_require_primary_key`` to zero for the current session with the following command:
  
  .. code::

      SET SESSION sql_require_primary_key = 0; and then execute the CREATE TABLE or ALTER TABLE statement again in the same session.

* Enable ``mysql.sql_require_primary_key`` parameter. To enable the ``mysql.sql_require_primary_key`` parameter, you can follow those steps:
  
  #. Select your Aiven for MySQL service
  #. Go to **Overview** tab
  #. Scroll down to the **Advanced configuration**, and click **Change**
  #. Select the ``mysql.sql_require_primary_key`` to ``Synced``. 

  .. warning::
    
    It is only recommended to use this approach when the table is created by an external application and using the session variable is not an option. To prevent more problematic tables from being unexpectedly created in the future you should change the setting back to ``Not synced`` once you finished creating the tables without primary keys.


.. seealso::
  
    Learn how to :doc:`create missing primary keys </docs/products/mysql/howto/create-missing-primary-keys>` in your Aiven for MySQL.
