Supported table engines
=======================

This article lists the table engines that are currently supported in Aiven for ClickHouse.

ClickHouse supports several table engines that define the storage parameters, supported queries, and other aspects of the data tables. For details on each table engine, see the `ClickHouse documentation <https://clickhouse.com/docs/en/engines/table-engines/>`_.

.. note::
   To support node recycling for backup and restore procedures and high availability in the Aiven platform, some of the table engines are remapped. This means that in replicated databases, ``MergeTree`` engines are automatically replaced with ``ReplicatedMergeTree`` variants of the same engine.

Aiven for ClickHouse supports the following table engines:

.. list-table::
  :header-rows: 1
  :align: left

  * - Engine
    - Engine family
  * - ``AggregatingMergeTree`` (remapped)
    - MergeTree
  * - ``Buffer``
    - Special engines
  * - ``CollapsingMergeTree`` (remapped)
    - MergeTree
  * - ``Dictionary``
    - Special engines
  * - ``Distributed``
    - Special engines
  * - ``GenerateRandom``
    - Special engines
  * - ``GraphiteMergeTree`` (remapped)
    - MergeTree
  * - ``MaterializedView``
    - Special engines
  * - ``Memory``
    - Special engines
  * - ``Merge``
    - Special engines
  * - ``MergeTree`` (remapped)
    - MergeTree
  * - ``Null``
    - Special engines
  * - ``ReplacingMergeTree`` (remapped)
    - MergeTree
  * - ``ReplicatedAggregatingMergeTree`` (remapped)
    - MergeTree
  * - ``ReplicatedCollapsingMergeTree``
    - MergeTree
  * - ``ReplicatedGraphiteMergeTree``
    - MergeTree
  * - ``ReplicatedMergeTree``
    - MergeTree
  * - ``ReplicatedReplacingMergeTree``
    - MergeTree
  * - ``ReplicatedSummingMergeTree``
    - MergeTree
  * - ``ReplicatedVersionedCollapsingMergeTree``
    - MergeTree
  * - ``Set``
    - Special engines
  * - ``SummingMergeTree`` (remapped)
    - MergeTree
  * - ``VersionedCollapsingMergeTree`` (remapped)
    - MergeTree
  * - ``View``
    - Special engines
