Memory usage, on-disk persistence and replication in Aiven for Redis
=====================================================================

Here we show you how Aiven for Redis solves the challenges related to high memory usage and high change rate. 

One of the main ways Redis is used is as a database cache. Data is written to Redis whenever it is fetched from a database, and the following queries with the same parameters first try to look data up in Redis, skipping the database query if the data is found. This results in high memory usage, and can result in a high change rate. 


Data eviction policy in Aiven for Redis
---------------------------------------

Data eviction policy is one of the most important Redis settings and it is available in the Aiven web console. 

Redis has a ``max memory`` setting which controls how much data is allowed to be stored, and the data eviction policy controls what happens when that maximum is reached. All Aiven for Redis services has the eviction policy set to *No eviction* by default. This means that if you keep storing values, and never remove anything, the write operations will start failing when the maximum memory is reached.

This is acceptable when data is consumed at a similar rate to how it is written. However, for other use cases ``Evict all keys`` with least recently used first (LRU) - which starts dropping old keys when ``max memory`` is reached - works better.  Another way is to drop random keys.

Whichever way is chosen, only the keys that have an explicit expiration time set are dropped, and keys with shortest time-to-live (TTL) are dropped first. 

Regardless of the eviction policy, if you write, you will eventually reach the ``max memory`` setting.


High memory and high change rate behavior
-----------------------------------------

For all new Aiven for Redis services the ``max memory`` is set to **70% of available RAM** (minus management overhead) plus 10% for replication log. The memory usage is limited to below 100% because of the following situations when Redis performs operations that can require additional memory: 

- When a new Redis node connects to the existing master, the master forks a copy of itself, and sends current memory contents to the other node. 

- Similar forking is done when Redis persists its current state on disk. Currently, for an Aiven for Redis service this happens **every 10 minutes**.

.. Note::
    When Redis creates a fork of itself all the memory pages of the new process are identical to the parent, and don't consume any extra memory. However, any changes in the parent process cause memory to diverge, and the real memory allocation to grow. 
    
    **Example**

    If the forked process took 4 minutes to perform the task, and new data was written at 5 megabytes per second, the system memory usage can grow by 1.2 gigabytes during the operation. 

Additionally, the duration of the backup and replication operations are directly proportional to the total amount of memory that is in use so the larger the plan, the larger the possible memory diverge, and thus the memory reserved for allowing these operations to be complete (without using swap) is also proportional to total memory.

If Redis memory usage grows so big that it needs to use swap, the system can quickly go into a cycle that makes the node unresponsive, and it needs to be replaced. 

In the on-disk persistence case, the child process wants to dump all of its memory on disk. If the parent process diverges so much that the node runs out of RAM, then some pages that the child may not yet have persisted on disk are stored to swap on disk. This makes the child process become more IO bound and run slower, which - in turn - increases the divergence, and causes more memory to be swapped, making the child even slower. In such cases, the node is only able to write and read swap.

The rate at which data can be written depends on the size of values that are being written, and the Aiven plan details.  

.. Tip::        
    In general, writing on average 5 megabytes per second works in most cases, and writing on average 50 megabytes per second will almost always result in failure, especially if memory usage nears maximum allowed or if a new node needs to initialize itself.


Initial synchronization
-----------------------

During system upgrades or in a high-availability setup in case of node failure, a new Redis node needs to be synchronized with the current master. The new node starts with an empty state, connects to the master, and asks the master to send a full copy of its current state. After getting the full copy, the new node starts following the replication stream from the master to fully synchronize.

Initial synchronization implementation is CPU intensive, and - because Redis does not split the workload between multiple CPU cores - the maximum transfer speed is usually around 50 megabytes per second. Additionally, the new node persists data initially on disk, and does a separate loading phase, which is in the low hundreds of megabytes per second. For a 20 gigabyte data set the initial sync phase takes around 6 minutes with today's hardware, and it cannot be much faster.

Once initial sync is complete the new node starts following the replication stream from the master. Replication log size is set to 10% of the total memory Redis can use. For a 28 gigabyte plan, it is just under 2 gigabytes. 

If the amount of changes that happen during the 6 minutes of the initial sync is larger than the replication log size, the new node is not able to start following the replication log stream, and it needs to do new initial sync.

.. Tip::
    If new changes are written at 5 megabytes per second, AND the amount of changes is 1.8 gigabytes in the 6 minutes, the new node can start up successfully. A higher constant change rate makes the sync fail unless the replication log size is increased.


Mitigation
----------

Aiven does not have a rate limit traffic for Redis services because limiting only the relevant write operations requires a specialized Redis proxy, and restricting all traffic can affect non-write traffic. 

Rate limiting may be introduced in the future, but for now be mindful of your workloads, and try to keep Redis writes at a moderate level to avoid node failures due to too high memory usage or inability to initialize new nodes.

.. Note:: 
    If you have a use case where you need to constantly write large amounts of data you can contact Aiven support to discuss options for your service configuration.