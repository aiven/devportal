Create new tables without primary keys
======================================

If your Aiven for MySQL® service was created after 2020-06-03, by default it does not allow creating new tables without primary keys. You can check this by taking the following steps:

1. Log in to `Aiven Console <https://console.aiven.io/>`_.
2. In the **Services** page, select your Aiven for MySQL service that you want to check.
3. In the **Overview** page of your service, scroll down to the **Advanced configuration** section.
4. Check the **Advanced configuration** section for the ``mysql.sql_require_primary_key`` parameter and its status.

If ``mysql.sql_require_primary_key`` is enabled, your Aiven for MySQL does not allow you to create new tables without primary keys. Attempts to create tables without primary keys will result in the following error message::

    Unable to create or change a table without a primary key, when the system variable 'sql_require_primary_key' is set. Add a primary key to the table or unset this variable to avoid this message. Note that tables without a primary key can cause performance problems in row-based replication, so please consult your DBA before changing this setting.

If creating tables without primary keys is prevented and the table that you're trying to create is known to be small, you may override this setting and create the table anyway. 

.. seealso::
    You can read more about the MySQL replication in the :ref:`Replication overview <myslq-replication-overview>` article.

You have two options to create the tables:

* Setting ``mysql.sql_require_primary_key`` to ``0`` for the current session with the following command:
  
  .. code-block:: shell

      SET SESSION sql_require_primary_key = 0; and then execute the CREATE TABLE or ALTER TABLE statement again in the same session.

* Disabling ``mysql.sql_require_primary_key`` parameter. To disable the ``mysql.sql_require_primary_key`` parameter, take the following steps:
  
1. Log in to `Aiven Console <https://console.aiven.io/>`_.
2. In the **Services** page, select your Aiven for MySQL service that you want to check.
3. In the **Overview** page of your service, scroll down to the **Advanced configuration** section and select **Change**.
4. In the **Edit advanced configuration** window, find ``mysql.sql_require_primary_key`` and disable it by using the toggle switch. Select **Save advanced configuration**.

  .. warning::
    
    It is only recommended to use this approach when the table is created by an external application and using the session variable is not an option. To prevent more problematic tables from being unexpectedly created in the future you should enable the setting again once you finished creating the tables without primary keys.

.. seealso::
  
    Learn how to :doc:`create missing primary keys </docs/products/mysql/howto/create-missing-primary-keys>` in your Aiven for MySQL.
