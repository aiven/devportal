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
     -  Description
     - Recommended approach
   * - Backups - one snapshot a day
     - | Since Aiven for ClickHouse service takes a single snapshot a day only,
       |
       | - When powering off the service, all data after the last backup is lost.
       | - Point-in-time recovery is not supported. A database can be restored to one of the daily backups states only.
       | - When creating a database fork, you can only create a fork that matches the state of one of the backups.
       | - Any data inserted before the next snapshot is lost if all nodes in a given shard malfunction and need to be replaced.
       |
       | This limitation doesn't apply to patches, migrations, or scaling, which are handled safely and automatically.
     - \-
   * - Service integrations
     - You can integrate your Aiven for ClickHouse service with PostgreSQL® and Kafka® only.
     - \-
   * - Table engines availability
     - * Log engine is not supported in Aiven for ClickHouse.

       * Some special table engines and the Log engine are not supported in Aiven for ClickHouse.

       * Some engines are remapped to their ``Replicated`` alternatives, for example, ``MergeTree`` **>** ``ReplicatedMergeTree``.
     - * For storing data, use the `Buffer engine <https://clickhouse.com/docs/en/engines/table-engines/special/buffer/>`_ instead of the Log engine.

       * Use the available table engines listed in :doc:`Supported table engines in Aiven for ClickHouse </docs/products/clickhouse/reference/supported-table-engines>`.
   * - Cloud availability
     - Available on AWS, GCP, and Azure only
     - Use the available cloud providers.
   * - Kafka Schema Registry
     - Aiven for ClickHouse doesn't support Kafka Schema Registry, which allows to build stream processing pipelines with schemas.
     - \-
   * - Querying all shards at once
     - If you have a sharded plan, you must use a Distributed view on top of your MergeTree table to query all the shards at the same time, and you should use it for inserts too.
     - Use the ``Distributed`` view with sharded plans.
   * - ON CLUSTER queries
     - Aiven for ClickHouse doesn't support ON CLUSTER queries because it actually runs each data definition query on all the servers of the cluster without using `ON CLUSTER`.
     - Run queries without ``ON CLUSTER``.
   * - Creating a database using SQL
     - You cannot create a database directly using SQL, for example, if you'd like to add a non-default database.
     - Use the Aiven's public API.
   * - Scaling down the number of nodes
     - You only can scale up the number of nodes in a cluster.
     - \-

Limits
------

Service limits are determined by a plan that this service uses.

.. list-table::
   :widths: 10 10 15 15 20
   :header-rows: 1
   :stub-columns: 1

   * - Plan
     - VMs
     - CPU per VM
     - RAM per VM
     - Total storage
   * - Hobbyist
     - 1
     - 1 (2 for AWS only)
     - 4 GB
     - 180 GB
   * - Startup
     - 1
     - 2
     - 16 GB
     - 1150 GB
   * - Business
     - 3
     - 2 - 8
     - 16 - 64 GB
     - 1150 - 4600 GB
   * - Premium
     - 6 - 30
     - 2 - 8
     - 16 - 64 GB
     - 2300 - 46000 GB

.. tip::

    If you need a custom plan with capacity beyond the listed limits, `contact us <https://aiven.io/contact?department=1306714>`_.

.. seealso::

    * `Quotas for specific tiers of Business and Premium plans <https://aiven.io/pricing?tab=plan-pricing&product=clickhouse>`_
    * `Plans comparison <https://aiven.io/pricing?tab=plan-comparison&product=clickhouse>`_
