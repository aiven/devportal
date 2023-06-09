Configure data retention thresholds in Aiven for ClickHouse®'s tiered storage |beta|
====================================================================================

Learn to control how your data is distributed between storage devices in the tiered storage of an Aiven for ClickHosue service. Check out how to configure tables so that your data is automatically written either to SSD or the object storage as needed.

About data retention control
----------------------------

If you have the tiered storage feature :doc:`enabled </docs/products/clickhouse/howto/enable-tiered-storage>` on your Aiven for ClickHouse service, your data is distributed between two storage devices (tiers). The data is stored either on SSD or in the object storage, depending on whether and how you configure this behavior. If you don't, by default the data is moved from SSD to the object storage when SSD reaches 80% of its capacity (default size-based data retention policy).

You may want to change this default data distribution behavior by :ref:`configuring your table's schema by adding a TTL (time-to-live) clause <time-based-retention-config>`. Such a configuration allows ignoring the SSD-capacity threshold and moving the data from SSD to the object storage based on how long the data is there on your SSD.

To enable this time-based data distribution mechanism, you can set up a retention policy (threshold) on a table level by using the TTL clause. For data retention control purposes, the TTL clause uses the following:

* Data item of the `Date` or `DateTime` type as a reference point in time
* INTERVAL clause as a time period to elapse between the reference point and the data transfer to the object storage

Prerequisites
-------------

* Aiven account
* Tiered storage feature :doc:`enabled </docs/products/clickhouse/howto/enable-tiered-storage>` on an Aiven for ClickHouse service level and on a table level
* Command line tool (:doc:`ClickHouse client </docs/products/clickhouse/howto/connect-with-clickhouse-cli>`)

.. _time-based-retention-config:

Configure time-based data retention
-----------------------------------

1. :doc:`Connect to your Aiven for ClickHouse service </docs/products/clickhouse/howto/list-connect-to-service>` using, for example, the ClickHouse client (CLI).
2. Select a database for operations you intend to perform.

   .. code-block:: bash

      USE database-name

Add TTL to a new table
''''''''''''''''''''''

Create a new table with the ``storage_policy`` setting set to ``tiered`` (to :doc:`enabled </docs/products/clickhouse/howto/enable-tiered-storage>` the feature) and TTL (time-to-live) configured to add a time-based data retention threshold on the table.

.. code-block:: shell

    CREATE TABLE example_table (
        SearchDate Date,
        SearchID UInt64,
        SearchPhrase String
    )
    ENGINE = MergeTree
    ORDER BY (SearchDate, SearchID)
    PARTITION BY toYYYYMM(SearchDate)
    TTL SearchDate + INTERVAL 1 WEEK TO VOLUME 'tiered'
    SETTINGS storage_policy = 'tiered';

Add TTL to an existing table
''''''''''''''''''''''''''''

Use the MODIFY TTL clause:

.. code-block:: shell

    ALTER TABLE database_name.table_name MODIFY TTL ttl_expression;

Update TTL to an existing table
'''''''''''''''''''''''''''''''

Change an already configured TTL in an existing table by using the ALTER TABLE MODIFY TTL clause:

.. code-block:: shell

    ALTER TABLE database_name.table_name MODIFY TTL ttl_expression; 

.. topic:: Result
   
   You have your time-based data retention policy set up. Now when a piece of data is there on your SSD for a specified time period, it's moved to the object storage, regardless of how much of the SSD capacity is still available.

What's next
-----------

* :doc:`Check data volume distribution between different disks </docs/products/clickhouse/howto/check-data-tiered-storage>`

Related reading
---------------

* :doc:`About tiered storage in Aiven for ClickHouse </docs/products/clickhouse/concepts/clickhouse-tiered-storage>`
* :doc:`Enable tiered storage in Aiven for ClickHouse </docs/products/clickhouse/howto/enable-tiered-storage>`
* :doc:`Transfer data between SSD and object storage </docs/products/clickhouse/howto/transfer-data-tiered-storage>`
* `Manage Data with TTL (Time-to-live) <https://clickhouse.com/docs/en/guides/developer/ttl>`_
* `Create table statement, TTL documentation <https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree#mergetree-table-ttl>`_
* `MergeTree - column TTL <https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree#mergetree-column-ttl>`_
