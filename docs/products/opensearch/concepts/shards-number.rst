Optimal number of shards
==========================

A key component of using OpenSearch® is determining the optimal number of shards for your index. This article provides helpful insights on choosing the appropriate number of shards and maximizing performance.

Considerations for optimal shard count 
----------------------------------------
OpenSearch® has a default shard count limit of 1024 per index, and Aiven imposes no additional restrictions on the number of shards for your OpenSearch® service. 

The ideal number of shards largely depends on your data volume, usage patterns, and expected data growth in OpenSearch®. As a general rule of thumb, aim for a shard size between a few gigabytes and tens of gigabytes. It's better to have a slightly higher number of shards, but avoid overdoing it, as OpenSearch® will issue warnings for excessively large or numerous shards.

For a multi-node OpenSearch® service, Aiven enforces a minimum of one replica per shard to ensure high availability and data redundancy. While there is no limit on the number of replicas per shard, adding too many can impact performance and increase disk usage.

Determining shard count
------------------------
Consider the following recommendations for selecting the appropriate number of shards for your OpenSearch® index:

* **Small data volumes with many indexes:** Start with one shard and split the index if necessary.
* **Tens of gigabytes of data:** Begin with five shards per index to avoid splitting the index for an extended period.
* **Hundreds of gigabytes of data:** Calculate the starting number of shards by dividing the amount of data by 10. 
   
   .. math:: 
   
      number\_of\_shards = amount\_of\_data\_in\_gigabytes / 10 
   
  For example, a 250GB index would need 25 shards.

* **Terabytes of data:** Consider increasing the shard size accordingly. For example, a 1TB index might require 50 shards.

These suggestions are only indicative, and optimal values depend on your usage patterns and anticipated data growth in OpenSearch®. Monitoring disk and CPU usage and upgrading when necessary to ensure optimal performance is essential.



Adjusting shard count
----------------------

You can change the number of shards without losing your data, but this process requires a brief downtime while the index is rewritten. Additionally, if you are using OpenSearch® for daily logs or similar use cases, you could consider adding more shards per index to new indexes. Doing so will increase the number of shards per index for subsequent days, providing an alternative option for managing your data. 

OpenSearch® streamlines the distribution and organization of shards across nodes by automating the allocation and rebalancing processes, simplifying scaling up or down. If you need to change the number of shards, you can re-index your data. However, modifying existing indexes can be challenging, and therefore it is best to aim for an optimal shard count from the beginning. If a shard grows significantly larger than the others, OpenSearch® will attempt to redistribute them to balance the node load.

