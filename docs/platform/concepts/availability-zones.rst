Availability zones
========================

About availability zones
------------------------

Availability zones (AZs) are physically isolated locations (data centers) where cloud services operate. There are multiple AZs within a region, each with independent power, cooling, and network infrastructure. The choice of AZs is usually affected by the latency/proximity to customers, compliance, SLA, redundancy/data security requirements, and cost. All AZs in a region are interconnected for an easy resource replication and application partitioning.

Cross-availability-zone data distribution
-----------------------------------------

Services can be replicated across multiple availability zones (AZs), which simplifies handling failures, decreases network latency, and enhances resource protection. This deployment model provides redundancy and failover in case an AZ gets down. Deploying services across multiple AZs enables smooth traffic transfer between AZs. It improves resiliency and reliability of workloads.

Aiven services across availability zones
-----------------------------------------

For Aiven services, nodes automatically spread across multiple availability zones (AZs). All Aiven's multi-node service plans are automatically spread among AZs of a region as long as the underlying cloud provider supports it. 

The virtual machines (VMs) are distributed evenly across the zones to provide the best possible availability guarantees in cases when an entire Availability Zone (which may include one or more datacenters) becomes unavailable.

Cloud providers in Aiven with the AZ support are the following:

- Amazon Web Services

- Google Cloud Platform

- Microsoft Azure

- :ref:`UpCloud<UpCloud Availability Zone>`

Smart availability zones for Apache Kafka®
-------------------------------------------

On top of spreading service's nodes across the availability zones (AZs) of a cloud region, Aiven automatically balances replicas of your Apache Kafka® partitions into different AZs. 

Since Aiven automatically rebalances the data in your Apache Kafka® cluster, your data remains fully available when a node or a whole AZ is lost.

UpCloud availability zones
---------------------------

With UpCloud, it only applies to ``upcloud-fi-hel``, where UpCloud provides datacenters (*fi-hel1* and *fi-hel2*). For example, with a two-node plan, it will result in one of the servers in *fi-hel1* and the other in *fi-hel2*.

Azure regions with availability-zone suppport at Aiven
-------------------------------------------------------

Here are Azure cloud regions where Aiven supports availability zones (AZs):

- azure-australiaeast
- azure-brazilsouth
- azure-canadacentral
- azure-centralus
- azure-france-central
- azure-korea-central
- azure-northeurope
- azure-southeastasia
- azure-switzerland-north
- azure-uae-north
- azure-westeurope
- azure-westus2

Related reading
---------------

- :doc:`PostgreSQL® backups </docs/products/postgresql/concepts/pg-backups>`
- :doc:`High availability </docs/products/postgresql/concepts/high-availability>`
- :doc:`Create and use read-only replicas </docs/products/postgresql/howto/create-read-replica>`
- :doc:`Migrate service to another cloud or region </docs/platform/howto/migrate-services-cloud-region>`
- :doc:`Aiven for Apache Kafka® MirrorMaker 2 </docs/products/kafka/kafka-mirrormaker>`
- :doc:`OpenSearch backups </docs/products/opensearch/concepts/backups>`
- :doc:`MySQL Backups </docs/products/mysql/concepts/mysql-backups>`
