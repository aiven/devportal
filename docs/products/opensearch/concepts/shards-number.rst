Optimal number of shards
========================

OpenSearch® has a default shard count limit per index (1024) and Aiven does not place any additional restrictions on the number of shards that you can use for your OpenSearch service. However, maintaining higher count of shards comes with the performance cost, and can make the cluster less efficient. In this article we'll give advice on how to determine number of shards you need.

The number of suggested shards depends heavily on the amount of data you have.
Somewhere between a few gigabytes and a few tens of gigabytes per shard
is a good rule of thumb.

-  If you know you will have a very small amount of data but many
   indexes, start with 1 shard, and split the index if necessary.

-  If you estimate you will have tens of gigabytes of data, start with 5
   shards per index in order to avoid splitting the index for a long
   time.

-  If you estimate you will have hundreds of gigabytes of data, start
   with something like (amount of data in gigabytes) / 10 for
   ``number_of_shards`` . For 250GB index, that would be 25 shards.

-  If you estimate you will have terabytes of data, increase shard size
   a bit. For example, for 1TB index 50 shards could be a relevant
   suggestion.

These suggestions are only indicative - optimal values depend heavily on
your usage pattern and anticipated growth of data in OpenSearch.

You can change the number of shards without losing your data, but this
process requires a brief downtime while the index is rewritten.

Performance numbers
-------------------

Having a large number of shards affect your OpenSearch performance
out from OpenSearch. Some rough numbers from three-node Aiven
OpenSearch business-8 cluster:

-  1 000 shards: no visible effect in OpenSearch performance.

-  10 000 shards is already quite a lot - creating new shards starts to
   take longer and longer time. Variance in performance grows.

-  15 000 shards: creating new shards takes significantly longer time,
   often tens of seconds.

-  20 000 shards: inserting new data randomly takes significantly longer
   times (20x longer than mean). Similarly, variance in search
   performance grows significantly.

Aiven for OpenSearch takes a snapshot once every hour. With 10 000 shards
cluster is continuously taking new backups and deleting old backups from
backup storage. This will naturally affect service performance, as part
of the capacity is continuously in use for managing backups.