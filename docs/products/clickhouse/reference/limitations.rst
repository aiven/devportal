Aiven for ClickHouse® limits and limitations
============================================

This article covers quotas for the Aiven for ClickHouse® service and restrictions on its use. This information helps you make right choices when working with Aiven for ClickHouse, for example, on your infrastructure design, tools, modes of interactions, potential integrations, or handling concurrent workloads.

Limitations
-----------

From the information about restrictions on using Aiven for ClickHouse, you can easily draw conclusions on how get your service to operate closer to its full potential. Use *Recommended approach* as guidelines on how to work around specific restrictions.

.. list-table::
   :widths: 25 50 25
   :header-rows: 1

   * - Name
     - Description
     - Recommended approach
   * - Backups
     - Aiven for ClickHouse service takes a single snapshot a day. Any data inserted before the next snapshot is be lost when nodes recycle.
     - None
   * - Service integrations
     - You can integrate your Aiven for ClickHouse service with PostgreSQL® and Kafka® only.
     - None
   * - Table engines availability
     - * Log engine is not supported in Aiven for ClickHouse.

       * Some special table engines and the Log engine are not supported in Aiven for ClickHouse.

       * Some engines are remapped to their `Replicated` alternatives, for example, `MergeTree` -> `ReplicatedMergeTree`.
     - * For storing data, use the `Buffer engine <https://clickhouse.com/docs/en/engines/table-engines/special/buffer/>`_ instead of the Log engine.

       * Use the available table engines listed in :doc:`Supported table engines in Aiven for ClickHouse </docs/products/clickhouse/reference/supported-table-engines>`.
   * - Cloud availability
     - Available on AWS, GCP, and Azure only
     - Use the available cloud providers.
   * - Kafka Schema Registry
     - Aiven for ClickHouse doesn't support Kafka Schema Registry, which allows to build stream processing pipelines with schemas.
     - Coming soon...
   * - Querying all shards at once
     - If you have a sharded plan, you must use a Distributed view on top of your MergeTree table to query all the shards at the same time, and you should use it for inserts too.
     - Use the `Distributed` view with sharded plans.
   * - ON CLUSTER queries
     - Aiven for ClickHouse doesn't support ON CLUSTER queries because it actually runs each query on all the servers of the cluster without using `ON CLUSTER`.
     - Run queries without `ON CLUSTER`.
   * - Creating a database using SQL
     - You cannot create a database directly using SQL, for example, if you'd like to add a non-default database. You need to use the Aiven's public API for that purpose.
     - Use the Aiven's public API.
