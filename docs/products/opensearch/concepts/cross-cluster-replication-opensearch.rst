OpenSearch® cross-cluster replication (beta)
============================================

.. note:: 
    Cross-cluster replication feature for Aiven for OpenSearch is a beta release. 

Cross-cluster replication in Aiven for OpenSearch allows you to replicate the entire cluster, including all of its indexes, mappings, and metadata, from one service to another across different regions and cloud providers. 

Cross-cluster replication follows an `active-passive` model where the follower service pulls all data and indexes from the leader service. Once you have a :doc:`cross-cluster replication setup <../howto/setup-cross-cluster-replication-opensearch>`, the leader cluster automatically replicates data to all its follower clusters. You can set up follower clusters in different regions and on different cloud providers. For simplicity, all index creation, deletion, new data, metadata, and configuration will be replicated automatically.

Benefits of cross-cluster replication
-------------------------------------
Some of the key benefits of cross-cluster replication include the following: 

- **Data locality/proximity:** Replicating data to a cluster closer to the user's geographical location helps reduce latency and response time. 
- **Horizontal scalability:** Splits a query-heavy workload across multiple replica clusters to improve application availability.
- **High availability and Disaster recovery (active-passive):**  With tolerance for outages or complete failure of clusters, cross-cluster replication ensures uninterrupted service availability with the ability to failover to an alternate cluster.
- **Centralized reporting cluster:**  Having a single replica cluster as a single source of truth between different master cluster

.. _ccr-limitatons: 

Limitations
-----------
- Cross cluster replication is not available for Hobbyist and Startup plans.
- Follower service needs to have the same service plan as the leader service.
- To delete the cross cluster replication integration, you need to **delete** the follower cluster service.
- Maintenance upgrade, major version upgrade needs to be done manually for both Leader and Follower service.
- In case of a node recycle event, replication will be paused until the service is running again.

.. seealso:: 
    Learn how to :doc:`Set up cross-cluster replication for Aiven for OpenSearch® <../howto/setup-cross-cluster-replication-opensearch>`. 
