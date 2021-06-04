About Scaling M3
================

`M3 <https://www.m3db.io/>`_ scales horizontally up to a really large number of nodes (at least low hundreds in single cluster, thousands overall); if you run out of resources in M3DB, for example, you can always add more nodes (or change to larger nodes). Same applies also to M3Aggregator (and M3Coordinator).

However, it is not always necessary to add more resources but instead use the existing ones better. This article attempts to describe what are actual costs of e.g. adding more namespaces (or more points being ingested) and how they relate to the overall load of the cluster.

Disk scaling (M3DB only)
------------------------

Starting with the least painful, M3Aggregator and M3Coordinator do not store anything on disk, only some state in shared etcd cluster. M3DB writes data in disk to:

* commit log (every point written)

* snapshots (condensed versions of future blocks when they are still open)

* filesets (historic data covering blocks to which data can no longer be inserted)

* indexes

They all scale based on number of points in the database. However, each namespace stores its data on the disk separately, so having namespaces with overlapping retention period means actually adding to the storage costs since the same data is repeated.

Example Configuration
'''''''''''''''''''''

.. list-table::
    :header-rows: 1
   
    * - Namespace
      - Retention
      - Resolution
      - Block size
    * - Unaggregated (U)
      - 1 week
      - 
      - 2 hours
    * - Aggregated A (A)
      - 2 weeks
      - 1 sec
      - 4 hours
    * - Aggregated B (B)
      - 4 weeks
      - 1 min
      - 4 hours
    * - Aggregated C (C)
      - 8 weeks
      - 1 hour
      - 12 hours


If we assume that there are 15 seconds per point in each time series, then we can look at the storage by week since the reading was taken:

* **week 1**: each point is actually stored 1 + 1 + 1/4 + 1/240 =~ 2.25 times

* **week 2**: unaggregated disk usage stays constant, but database still adds ~ 1.25 times the number of points ingested (namespace A has point per every unaggregated point; others fewer)

* **weeks 3-4**: namespace A disk usage stays also constant, but database adds ~0.25 times the number of points ingested

* **weeks 5-8**: namespace B disk usage stays also constant, but database adds ~0.004 times the number of points ingested

* **weeks 9+**: disk usage should stay constant

Rough calculation of all this, taken together::

    (U) 1 week *1 +

    (A) 2 weeks *1 +

    (B) 4 weeks * 1/4 +

    (C) 8 weeks * 1/240 =

    = ~ 4 weeks worth of unaggregated data.

The storage efficiency is affected by block duration configured for the namespaces; the longer the blocks, the more efficiently they are stored on the disk, but on the other hand the memory usage grows from it as well as data is retained in the memory longer.

Beyond the disk space usage, another potential limit is number of files. For each shard of every block of every namespace (times replication factor), there are 7 files in the m3db cluster. And they are allocated the moment namespace is created.

Example math with the namespace U above: It has 24*7/2 = 84 blocks. Given 3-node cluster with RF=3, that means 84 * 60 = 5040 shards per node, and that means 35280 files. 

Aiven for M3 has hardcoded limit for total number of files, which limits the total number of block shards that can be allocated for single node. If desired namespace configuration would exceed this limit, by increasing number of nodes, it is possible to have more total blocks in the cluster.

CPU scaling
-----------

In general CPU usage scales with the amount of work done; the number of operations (especially if having to open new SSL connections) contributes significantly, as does the data mass described above. In general:

* M3Aggregators are not particularly CPU bound.

* M3Coordinator's main resource that is used is CPU. However, if there is some sort of network congestion and requests pile up, the memory usage can also spike. 

Memory scaling
--------------

In our experience memory has been the hardest to scale in M3 clusters. The memory usage of M3 consists of:

* fixed base cost (pretty low, ~hundreds of megabytes if configured with small or no pools)

* per-request overhead (main cost in M3Coordinator)

* cached data for queries

* storing data being aggregated in memory; only applicable if aggregated namespaces are configured (main cost in M3Aggregator or significant one in M3Coordinator if M3Aggregator is not in use)

* storing data not yet written to disk - current block (main cost in M3DB)

The first three are not that interesting as they do not scale directly with configuration and-or points stored. However, the last two are usually the ones that cause scalability problems.

The data being stored for aggregation scales with number of namespaces, times number of time series, and also number of points fitting in a single block for that namespace. Due to that, each added namespace adds significant memory cost (unless some of the time series are filtered).

The data in current blocks (not yet persisted to disk as filesets) has also same pattern. It grows as any of the following grow:

* number of time series

* number of points within single block

* number of configured namespaces

For efficient on-disk storage, M3's default recommendation is to have about 720 points per block. So for 15 seconds per point case, that would indicate 180 minutes, or 3 hours per block.  Following the recommendation may be worth it for high resolution namespaces, but for longer lived ones it may lead to too much data being kept in memory. For example, if there is a point per day, closing block every two years would not work. In that sort of case, e.g. day(s) or at most week's block size duration is recommended.

The data within current block (and for a bit longer depending on buffer past duration) is stored in RAM until they are flushed to disk, and this is multiplied by number of time series AND it is also multiplied by number of namespaces that contain those particular points. 

Given a consistent amount of points per second coming in, the memory usage can be reduced by:

* having smaller block size duration (disk usage will grow faster)

* having fewer namespaces

* filtering data that gets to aggregated namespaces 

* configuring shorter buffer past duration as data for current block is retained in memory that much longer after the block is already past; Aiven for M3 defaults to maximum value, which is block size - 1 second); note that if changing buffer past duration to e.g. 1 minute, data older than 1 minute will be simply discarded

For M3DB memory usage cost, using the disk example, what is in RAM per series is (at least)::

    (U) 4 * 60 * 2 = 480 points +

    (A) 4 * 60 * 4 = 960 points +

    (B) 60 * 4 = 240 points +

    (C) 12 = 12 points

    =~ 1700 points + whatever the not-quite-insignificant per-time-series overhead is (* replication factor)

M3Aggregator will also hold subset of this - unaggregated namespace (U) will not be included.  And this is for single time series; typically you may have more than that (we do have tens of millions at the time of this article's writing).


Scaling Recommendations
-----------------------

Have as few namespaces as you can, with as few points per block as you can afford (to minimize memory usage) to achieve what you want. Or filter the data that enters namespaces. If dealing only with short-term data, avoiding aggregation altogether may be the most resource effective choice.

Real-world example: Aiven production configuration
--------------------------------------------------

At the moment we use with 30 second typical scrape interval with following namespace configuration:

* 2 day unaggregated namespace, and 

* 1 month aggregated namespace with 10min resolution

and even that sort of aggregation configuration causes CPU and memory usage to be significantly more in M3DB than if we just had (longer) unaggregated namespace and no aggregation in use. However, our disk usage is only less than that of 4 days' worth of unaggregated data and the aggregated data performs much better for historic queries (e.g. looking at graph for one week).
