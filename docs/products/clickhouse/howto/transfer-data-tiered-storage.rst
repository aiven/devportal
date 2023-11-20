Transfer data between storage devices in Aiven for ClickHouse®'s tiered storage
===============================================================================

Check out this article for instructions on transferring data from and to SSD for an Aiven for ClickHouse® service.

About moving data between storage devices
-----------------------------------------

After :doc:`enabling </docs/products/clickhouse/howto/enable-tiered-storage>` the tiered storage feature, you can move your data from SSD to object storage. Next, you may want to size down your SSD by selecting a service plan with less SSD capacity. Later, you can move your data from object storage back to your SSD if needed. Both operations can be performed using SQL statements against your tables directly.

Prerequisites
-------------

* Aiven organization
* Tiered storage feature :doc:`enabled </docs/products/clickhouse/howto/enable-tiered-storage>` at project level
* Command line tool (:doc:`ClickHouse client </docs/products/clickhouse/howto/connect-with-clickhouse-cli>`)

Transfer data from SSD to object storage
----------------------------------------

If you :doc:`enable </docs/products/clickhouse/howto/enable-tiered-storage>` the tiered storage feature on your table, by default your data is moved from SSD to object storage as soon as the SSD reaches 80% of its capacity. You can also :doc:`configure your tiered storage </docs/products/clickhouse/howto/configure-tiered-storage>` so that data is moved to object storage at a specific time.

1. :doc:`Connect to your Aiven for ClickHouse service </docs/products/clickhouse/howto/list-connect-to-service>` using, for example, the ClickHouse client (CLI).

2. Run the following query:

   .. code-block:: bash

      ALTER TABLE database-name.tablename MODIFY SETTING storage_policy = 'tiered'

.. topic:: Result

   Now, with the tiered storage feature :doc:`enabled </docs/products/clickhouse/howto/enable-tiered-storage>`, your data is moved from SSD to object storage when the SSD reaches 80% of its capacity.

Transfer data from object storage to SSD
----------------------------------------

Use the MOVE statement `MOVE PARTITION|PART <https://clickhouse.com/docs/en/sql-reference/statements/alter/partition#move-partitionpart>`_ to transfer data to your SSD.

1. :doc:`Connect to your Aiven for ClickHouse service </docs/products/clickhouse/howto/list-connect-to-service>` using, for example, the ClickHouse client (CLI).

2. Select a database for operations you intend to perform.

   .. code-block:: bash

      USE database-name

3. Run the following query:

   .. code-block:: bash

      ALTER TABLE table_name MOVE PARTITION partition_expr TO VOLUME 'default'

.. topic:: Result

   Your data has been moved to the SSD.

What's next
-----------

* :doc:`Check data distribution between SSD and object storage </docs/products/clickhouse/howto/check-data-tiered-storage>`
* :doc:`Configure data retention thresholds for tiered storage </docs/products/clickhouse/howto/configure-tiered-storage>`

Related reading
---------------

* :doc:`About tiered storage in Aiven for ClickHouse </docs/products/clickhouse/concepts/clickhouse-tiered-storage>`
* :doc:`Enable tiered storage in Aiven for ClickHouse </docs/products/clickhouse/howto/enable-tiered-storage>`
