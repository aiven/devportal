Check data distribution between storage devices in Aiven for ClickHouse®'s tiered storage
=========================================================================================

.. important::

Aiven for ClickHouse® tiered storage is a limited availability feature. If you're interested in trying out this feature, contact the sales team at `sales@Aiven.io <mailto:sales@Aiven.io>`_.

Verify how your data is distributed between the two layers of your tiered storage: SSD and object storage.

About checking data distribution
--------------------------------

If you have the tiered storage feature :doc:`enabled </docs/products/clickhouse/howto/enable-tiered-storage>` on your Aiven for ClickHouse service, your data is distributed between two storage devices (tiers). You can learn on what storage devices specific databases and tables are stored. You can also preview their total sizes as well as part counts, minimum part sizes, median part sizes, and maximum part sizes.

Prerequisites
-------------

* Aiven account
* Tiered storage feature :doc:`enabled </docs/products/clickhouse/howto/enable-tiered-storage>` on an Aiven for ClickHouse service level and on a table level
* Command line tool (:doc:`ClickHouse client </docs/products/clickhouse/howto/connect-with-clickhouse-cli>`)

Run a data distribution check
-----------------------------

1. :doc:`Connect to your Aiven for ClickHouse service </docs/products/clickhouse/howto/list-connect-to-service>` using, for example, the ClickHouse client (CLI).
2. Run the following query:

   .. code-block:: bash

    SELECT
        database,
        table,
        disk_name,
        formatReadableSize(sum(data_compressed_bytes)) AS total_size,
        count(*) AS parts_count,
        formatReadableSize(min(data_compressed_bytes)) AS min_part_size,
        formatReadableSize(median(data_compressed_bytes)) AS median_part_size,
        formatReadableSize(max(data_compressed_bytes)) AS max_part_size
    FROM system.parts
    GROUP BY
        database,
        table,
        disk_name
    ORDER BY
        database ASC,
        table ASC,
        disk_name ASC

   You can expect to receive the following output:

   .. code-block:: bash

    ┌─database─┬─table─────┬─disk_name─┬─total_size─┬─parts_count─┬─min_part_size─┬─median_part_size─┬─max_part_size─┐
    │ datasets │ hits_v1   │ default   │ 1.20 GiB   │           6 │ 33.65 MiB     │ 238.69 MiB       │ 253.18 MiB    │
    │ datasets │ visits_v1 │ S3        │ 536.69 MiB │           5 │ 44.61 MiB     │ 57.90 MiB        │ 317.19 MiB    │
    │ system   │ query_log │ default   │ 75.85 MiB  │         102 │ 7.51 KiB      │ 12.36 KiB        │ 1.55 MiB      │
    └──────────┴───────────┴───────────┴────────────┴─────────────┴───────────────┴──────────────────┴───────────────┘

.. topic:: Result
   
   The query returns a table with data distribution details for all databases and tables that belong to your service: storage device they use, their total sizes as well as parts' counts and sizing.

What's next
-----------

* :doc:`Transfer data between SSD and object storage </docs/products/clickhouse/howto/transfer-data-tiered-storage>`
* :doc:`Configure data retention thresholds for tiered storage </docs/products/clickhouse/howto/configure-tiered-storage>`

Related reading
---------------

* :doc:`About tiered storage in Aiven for ClickHouse </docs/products/clickhouse/concepts/clickhouse-tiered-storage>`
* :doc:`Enable tiered storage in Aiven for ClickHouse </docs/products/clickhouse/howto/enable-tiered-storage>`
