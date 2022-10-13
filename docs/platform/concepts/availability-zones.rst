Availability zones
========================

About availability zones
------------------------

Availability zones (AZs) are physically isolated locations (data centers) where cloud services operate. There are multiple AZs within a region, each with independent power, cooling, and network infrastructure. The choice of AZs is usually affected by the latency/proximity to customers, compliance, SLA, redundancy/data security requirements, and cost. All AZs in a region are interconnected for an easy resource replication and application partitioning.

Cross-AZs data distribution
---------------------------

Services can be replicated across multiple AZs, which simplifies handling failures, decreases network latency, and enhances resource protection. This deployment model provides redundancy and failover in case an AZ gets down. Deploying services across multiple AZs enables smooth traffic transfer between AZs. It improves resiliency and reliability of workloads.

Aiven services across AZs
-------------------------

For Aiven services, nodes automatically spread across multiple AZs. All Aiven's multi-node service plans are automatically spread among AZs of a region as long as the underlying cloud provider supports it. 

The virtual machines (VMs) are distributed evenly across the zones to provide the best possible availability guarantees in cases when an entire Availability Zone (which may include one or more datacenters) becomes unavailable.

Cloud providers in Aiven with the AZ support are the following:

- Amazon Web Services

- Google Cloud Platform

- Microsoft Azure

- :ref:`UpCloud<UpCloud Availability Zone>`

Smart AZ for Apache Kafka®
--------------------------

On top of spreading service's nodes across the AZs of a cloud region, Aiven automatically balances replicas of your Apache Kafka® partitions into different AZs. 

Since Aiven automatically rebalances the data in your Apache Kafka® cluster, your data remains fully available when a node or a whole AZ is lost.

UpCloud AZ
----------

With Upcloud, it only applies to *upcloud-fi-hel*, where Upcloud provides datacenters (*fi-hel1* and *fi-hel2*). For example, with a two-node plan, it will result in one of the servers in *fi-hel1* and the other in *fi-hel2*.

Azure AZ availability
---------------------

AZs in Aiven Production
^^^^^^^^^^^^^^^^^^^^^^^

Here are Azure AZs available in Aiven Production:

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

AZs not in Aiven Production
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Due to a limited availability, the following AZ are not included in Aiven Production:

- azure-eastasia

    - Only two zones available for most instance types

- azure-eastus

    - Third zone not available for

        - a64/standard_l8s_v2
        - a120/standard_l16s_v2
        - a240/standard_l32s_v2

- azure-eastus2

    - No zones available for

        - m150/standard_d15_v2
        - m150/standard_ds15_v2
        - m150/standard_d15_v2
        - m150/standard_ds15_v2

- azure-germany-westcentral

- No issues with availability zones so this actually can be enabled.

        - m150/standard_ds15_v2 used in *influxdb/startup-150* is not available in the region
        - m150/standard_d15_v2 is not available in the region

- azure-india-central

    - Only one zone available for

        - a64/standard_l8s_v2
        - a120/standard_l16s_v2

- azure-japaneast

    - No zones available for

        - a64/standard_l8s_v2
        - a120/standard_l16s_v2
        - a240/standard_l32s_v2
        - m150/standard_d15_v2
        - m150/standard_ds15_v2
        - m150/standard_d15_v2
        - m150/standard_ds15_v2

- azure-norway-east

    - No issues with availability zones so this actually can be enabled.

        - m150/standard_d15_v2 is not available in the region

- azure-south-africa-north

    - No issues with availability zones so this actually can be enabled.

        - m150/standard_ds15_v2 used in *influxdb/startup-150* is not available in the region
        - m150/standard_d15_v2 is not available in the region

- azure-southcentralus

    - Only two zones available for

        - a64/standard_l8s_v2
        - a120/standard_l16s_v2

- azure-uksouth

    - No zones available for

        - a64/standard_l8s_v2
        - a120/standard_l16s_v2
        - a240/standard_l32s_v2
        - m150/standard_d15_v2
        - m150/standard_ds15_v2
        - m150/standard_d15_v2
        - m150/standard_ds15_v2

Read more
----------

- :doc:`PostgreSQL® backups </docs/products/postgresql/concepts/pg-backups>`
- :doc:`High availability </docs/products/postgresql/concepts/high-availability>`
- :doc:`Create and use read-only replicas </docs/products/postgresql/howto/create-read-replica>`
- :doc:`Migrate service to another cloud or region <docs/platform/howto/migrate-services-cloud-region>`
- :doc:`Aiven for Apache Kafka® MirrorMaker 2 </docs/products/Kafka/Kafka-mirrormaker>`
- :doc:`OpenSearch backups </docs/products/opensearch/concepts/backups>`
- :doc:`MySQL Backups </docs/products/mysql/concepts/mysql-backups>`
