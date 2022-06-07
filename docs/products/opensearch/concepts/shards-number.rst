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

-  If you estimate you will have hundreds of gigabytes of data, calculate the starting number of shards as

   .. math:: 
   
      number\_of\_shards = amount\_of\_data\_in\_gigabytes / 10 
   
   For example: for 250GB index, that would be 25 shards.

-  If you estimate you will have terabytes of data, increase the shard size compared to the previous example. 

   For example, for 1TB index 50 shards could be a relevant suggestion.

These suggestions are only indicative - optimal values depend heavily on
your usage pattern and anticipated growth of data in OpenSearch.

.. Tip::

   You can change the number of shards without losing your data, but this process requires a brief downtime while the index is rewritten.
