High availability in Aiven for OpenSearch®
==========================================

Aiven for OpenSearch® is available on a variety of plans, offering different levels of high availability. The selected plan defines the features available, and a summary is provided in the table below:

.. list-table::
    :header-rows: 1

    * - Plan
      - High Availability Features
      - Backup History
    * - **Hobbyist**
      - Single-node with limited availability
      - single backup for disaster recovery
    * - **Startup**
      - Single-node with limited availability
      - 2 days, with hourly backup for 24 hours
    * - **Business**
      - Three-node cluster configured for high availability
      - 14 days, with hourly backup for 24 hours
    * - **Premium**
      - Six-node (or more) cluster configured for high availability
      - 30 days, with hourly backup for 24 hours

Failure handling
----------------

**Minor failures**, such as service process crashes or temporary loss of network access, are handled by Aiven automatically in all plans without any major changes to the service deployment. The service automatically restores normal operation once the crashed process is automatically restarted or when the network access is restored.

**Severe failures**, such as loss of a cluster node, require more drastic recovery measures. Aiven platform continuously monitors the health of every node in a cluster. When a node reports failures from its own self-diagnostics or when no response to a health check is returned, Aiven platform starts a replacement node. While the node is being replaced, client requests are rerouted to the other nodes that have replica shards. When the new node joins the cluster, it restores data from the existing nodes or from a backup if no old nodes can be reached anymore, and starts servicing requests when data restoration is completed.

High Availability in Business and Premium plans
---------------------------------------------------

To achieve high availability in business and premium plans, Aiven for OpenSearch configures your indices to have at least one replica. You will want to choose a cloud region with at least three availability zones to ensure that the primary and replica shards will not be down at the same time. The setting that controls the replication factor in index settings is called ``number_of_replicas``. Having its value as 1 is enough to have your data resilient to an outage in a single zone, and setting it to higher values will add tolerance for more availability zone failures.

Cluster nodes in business and premium plans are distributed evenly across availability zones in a cloud region. Moreover, each node is configured to be aware of its zone. Therefore a primary copy of your data and a replica copy will be allocated on the nodes in different availability zones.

Aiven platform constantly monitors all nodes in an OpenSearch cluster. When a node stops responding to a health check for sufficiently long time, Aiven platform starts a replacement node, waits for the node to start, and then replaces the failed node with the new node in the cluster's configuration.

.. Note::
    The amount of time it takes for a new node to become fully operational depends mainly on the used cloud region and the amount of data that needs to be copied from primary shards. However, in a multi-node cluster on a Business or Premium plan all the nodes with in-sync shards will keep responding to client requests even before the new node is fully operational. Moreover, for every primary shard on the lost node, the cluster promotes one in-sync replica shard. Write requests from the clients will be routed to the promoted shards. All of this is automatic and requires no administrator intervention.

Single-node Hobbyist and Startup service plans
----------------------------------------------

Losing the only node from the service starts the automatic process of creating a new replacement node. The new node starts up, restores its state from the latest available backup and resumes serving customers.
Since there was just a single node providing the service, the service will be unavailable for the duration of the restore operation. All the write operations made since the last backup are lost.
