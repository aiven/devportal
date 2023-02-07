Cross-cluster replication with Aiven for Apache Cassandra® |beta|
=================================================================

This article provides an overview of the cross-cluster replication (CCR) feature for Aiven for Apache Cassandra®. Learn what CCR is and how it works. Discover how you can benefit from this feature and what limits and limitations it has.

About cross-cluster replication
-------------------------------

Cross-cluster replication (CCR) is a process of reproducing resources from one datacenter to another (or, in the Aiven universe, from one service to another). It allows you to select a cloud provider and a cloud region for your data replica(s). CCR uses the multi-datacenter (multi-cloud) cluster deployment, enabling large and resilient Apache Cassandra clusters on Aiven.

Why use CCR
-----------

* CCR improves the disaster recovery capability for your service. Even if one service (cloud provider or region) goes down, your data stays safe and available in its replica (another service with a different cloud provider or region).
* Enabling CCR on your service, you can set up your client to interact with the service that is geographically close. The data locality benefit translates into a lower latency and improved data processing performance.
* CCR brings high availability benefits.

Data flow architecture
----------------------

When you enable CCR on your Aiven for Apache Cassandra service, you connect to another service so that the two services (CCR pair) can replicate data to each other. The CCR service pair constitutes a single Apache Cassandra cluster that comprises nodes from the two services. The services are located in different regions and the nodes of a single service comprise a single datacenter.

.. mermaid::

    flowchart LR
        subgraph Cluster_xy
        direction LR
        cluster_info[[User keyspace with replication<br>- NetworkTopologyStrategy<br>- Separate token rings for X & Y]]
        subgraph Service_x
        direction LR
        service_info_x[[dc=google-west-X<br>rack=google-west-2-b]]
        x1((node_x1)) --- x2((node_x2))
        x2((node_x2)) --- x3((node_x3))
        x3((node_x3)) --- x1((node_x1))
        end
        subgraph Service_y
        direction LR
        service_info_y[[dc=aws-wtf-Y<br>rack=aws-wtf-9-z]]
        y1((node_y1)) --- y2((node_y2))
        y2((node_y2)) --- y3((node_y3))
        y3((node_y3)) --- y1((node_y1))
        end
        Service_x<-. data_replicatioin .->Service_y
        end

How it works
------------

Replication strategy
''''''''''''''''''''

Apache Cassandra allows specifying the replication strategy when creating a keyspace.

.. note::
    
    The keyspace is an entity that determines how data replicates in the tables that belong to this keyspace.

With the replication strategy defined in the CREATE KEYSPACE query, every table in the keyspace is replicated within the cluster according to the specified strategy.

``NetworkTopologyStrategy``
'''''''''''''''''''''''''''

The replication strategy that allows CCR in Aiven for Apache Cassandra is called `NetworkTopologyStrategy <https://docs.datastax.com/en/cassandra-oss/3.0/cassandra/architecture/archDataDistributeReplication.html#archDataDistributeReplication__nts>`__.

``NetworkTopologyStrategy`` can be set up as the replication strategy when creating a keyspace on the cluster. The same CREATE KEYSPACE query can be used to specify the replication factor and a datacenter that data can be replicated to.

Datacenter per service
  For the CCR feature to work, the two services that cross-replicate need to be located in two different datacenters.

Replication factor
  The replication factor is defined in the CREATE KEYSPACE query to indicate the number of copies of the data to be saved per cluster (in each datacenter).

.. seealso::

    For more details on the replication factor for Apache Cassandra, see `NetworkTopologyStrategy <https://cassandra.apache.org/doc/4.1/cassandra/cql/ddl.html#networktopologystrategy>`__ in the Apache Cassandra documentation.

CCR setup
'''''''''

To make CCR work on your services, you need a cluster comprising two Apache Cassandra services with CCR enabled. On the cluster, you need to issue the CREATE KEYSPACE request, specifying ``NetworkTopologyStrategy`` as a replication strategy along with desired replication factors.

.. code-block:: bash
   :caption: Example

   CREATE KEYSPACE test WITH replication =  /
   {                                        /
    'class': 'NetworkTopologyStrategy',     /
    'dc-1': 3,                              /
    'dc-2': 3                               /
   };

Where ``dc-1`` and ``dc-2`` are the names of Apache Cassandra datacenter, which you can find in the Aiven console.

CCR in action
'''''''''''''

With CCR enabled and configured, Apache Cassandra replicates each write in the keyspace to both services (datacenters) with an appropriate number of copies as per replication factor.

Active-active model
  Apache Cassandra uses an active-active model: clients have the choice of reading/writing either from one service or the other.

Consistency level
  The consistency level regulates how many nodes need to confirm they executed an operation for this operation to be considered successfully completed by the client. You can set up the consistency level to one of the allowed consistency level arguments depending on your needs.

.. topic:: Examples

    * LOCAL_QUORUM consistency level
        The read is contained within the service you connect to (completes faster).
    * QUORUM consistency level
        The read produces more consistent results (replies from nodes of both services are required).

.. seealso::

    For more details on consistency levels for Apache Cassandra, see `CONSISTENCY <https://cassandra.apache.org/doc/4.1/cassandra/tools/cqlsh.html#consistency>`_ in the Apache Cassandra documentation.

Limitations
-----------

* Two CCR services need to share one service plan and the same amount of dynamic disk space.
* Limited replication configuration
  * ``SimpleReplicationStrategy`` not supported
  * ``Unbalanced NetworkTopologyStrategy`` not supported (no different replication factors for different services)
* Once a CCR service pair is split, the clusters cannot be reconnected.

Related reading
---------------

* :doc:`OpenSearch® cross-cluster replication</docs/products/opensearch/concepts/cross-cluster-replication-opensearch>`
* :doc:`Set up cross-cluster replication for OpenSearch</docs/products/opensearch/howto/setup-cross-cluster-replication-opensearch>`
* :doc:`Enabling cross-cluster replication for Apache Kafka® via Terraform</docs/tools/terraform/reference/cookbook/kafka-mirrormaker-recipe>`
* `Cassandra® documentation <https://cassandra.apache.org/doc/latest/>`_
