Enable tiered storage in Aiven for ClickHouse®
==============================================

.. important::

   Aiven for ClickHouse® tiered storage is a :doc:`limited availability feature </docs/platform/concepts/beta_services>`. If you're interested in trying out this feature, contact the sales team at `sales@Aiven.io <mailto:sales@Aiven.io>`_.

Learn how to enable the tiered storage feature on your project and activate it for specific tables.
To check what the tiered storage is, how it works, and why use it, see :doc:`Tiered storage in Aiven for ClickHouse® </docs/products/clickhouse/concepts/clickhouse-tiered-storage>`.

About enabling tiered storage
-----------------------------

To use the tiered storage feature, you need to enable it on the project level by contacting the sales team at `sales@Aiven.io <mailto:sales@Aiven.io>`_ and set it up on the table level using SQL (via CLI, for example).

Limitations
'''''''''''

* When :doc:`enabled </docs/products/clickhouse/howto/enable-tiered-storage>`, the tiered storage feature cannot be deactivated.

  .. tip::

    As a workaround, you can create a new table (without enabling the tiered storage) and copy the data from the original table (with the tiered storage :doc:`enabled </docs/products/clickhouse/howto/enable-tiered-storage>`) to the new table. As soon as the data is copied to the new table, you can remove the original table.

* With the tiered storage feature :doc:`enabled </docs/products/clickhouse/howto/enable-tiered-storage>`, it's not possible to connect to an external existing object storage or cloud storage bucket.

Tools
'''''

To enable the tiered storage, use SQL and an SQL client (for example, the ClickHouse CLI client).

Prerequisites
-------------

* You have an Aiven organization and at least one project.
* You have a command line tool (:doc:`ClickHouse client </docs/products/clickhouse/howto/connect-with-clickhouse-cli>`) installed.
* All maintenance updates are applied on your service (check on the **Overview** page of your service in Aiven Console).

Enable tiered storage on a project
----------------------------------

To enable the tiered storage feature on your project, request it from the sales team at `sales@Aiven.io <mailto:sales@Aiven.io>`_.

.. topic:: Result
   
   Your project supports the tiered storage feature, and you can enable the feature on tables for your Aiven for ClickHouse services.

Enable tiered storage on a table
--------------------------------

When you have the tiered storage feature enabled on your project, you can move on to enabling it on your tables, both new and existing ones.

1. :doc:`Connect to your Aiven for ClickHouse service </docs/products/clickhouse/howto/list-connect-to-service>` using, for example, the ClickHouse client (CLI).

2. To activate the tiered storage feature on a specific table, set ``storage_policy`` to ``tiered`` on this table by executing the following SQL statement:

   .. code-block:: bash

      ALTER TABLE database-name.table-name MODIFY SETTING storage_policy = 'tiered'

.. topic:: Result
   
   The tiered storage is enabled on your table and data in this table is now distributed between two tiers: SSD and object storage.

   You can check if the tiered storage is now supported (**Active** / **Not active**) on your table in `Aiven Console <https://console.aiven.io/>`_ > **Databases & Tables** > **Databases lists** > Your database > Your table > the **Tiered storage** column.

What's next
-----------

* :doc:`Configure data retention thresholds for tiered storage </docs/products/clickhouse/howto/configure-tiered-storage>`
* :doc:`Check data volume distribution between different disks </docs/products/clickhouse/howto/check-data-tiered-storage>`

Related reading
---------------

* :doc:`About tiered storage in Aiven for ClickHouse </docs/products/clickhouse/concepts/clickhouse-tiered-storage>`
* :doc:`Transfer data between SSD and object storage </docs/products/clickhouse/howto/transfer-data-tiered-storage>`
