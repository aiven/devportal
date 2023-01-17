Disaster recovery in Aiven for ClickHouse®
==========================================

Disaster recovery is a process of coping with emergencies or crises using dedicated methods for protecting resources and/or reestablishing their desired status. In the context of data infrastructure, well-established disaster recovery methods are of a particular importance for preventing data loss or corruption. Software failure, loss of an availability zone, or datacenter outage are only a few examples of emergencies when disaster recovery comes in. This article helps you understand how Aiven for ClickHouse® prevents and mitigates such emergencies and what disaster recovery methods it uses to keep your data safe and sound.

High availability
-----------------

High availability (HA) is an entity's ability to continuously maintain a certain level of operational performance for a desired period of time. HA is typically achieved by redundancy - securing replicas of databases or services to be highly available. To support disaster recovery technologies, a database service needs to stay highly available, for example, by operating on a few nodes holding the same data.

With Aiven, HA for your service is supported in business and premium plans. See `Plan comparison <https://aiven.io/pricing?tab=plan-comparison&product=clickhouse>`_ for details.

.. seealso::

    :ref:`Cross-availability-zone data distribution <cross-zone data distro>` 

.. _backup-and-restore:

Backup and restore
------------------

Backups
'''''''

Backups of Aiven for ClickHouse services happen automatically on a daily basis.

They cover the following:

* Access entities (for example, users, roles, passwords, or secrets) stored in Zookeeper
* Database definitions (DDL files)
* Table definitions (DDL files)
* Table schemas
* Table content (:ref:`part files <part-files>`)

.. _part-files:

.. topic:: Part files
    
    With the ClickHouse's ReplicatedMergeTree table engine, each INSERT query results in creating a new file, so-called part, written only once and not modifiable.

Using part files allows incremental backups in Aiven for ClickHouse: only changed parts are backed up and files already available in the object storage are left out from the backup.

Recovery
''''''''

The restoration of a backup of an Aiven for ClickHouse service is performed on a running ClickHouse server and proceeds as a regular power-on of the service. The restoration happens only for powering up a service after powering it down or forking a service.

.. seealso::

    For more information on backups in Aiven, see :doc:`Backups at Aiven </docs/platform/concepts/service_backups>`.

Sharding
--------

Essentially, sharding is a technique of splitting database rows across multiple database nodes, which usually significantly increases performance. However, integrating sharding with database replication technologies, data can be replicated across shards of the sharded database. Replication at the shard level provides high availability and helps to achieve disaster recovery. A shard group can be replicated to one or more data centers, which improves the disaster recovery capability.

With Aiven for ClickHouse `business and premium plans <https://aiven.io/pricing?tab=plan-comparison&product=clickhouse>`_, each shard is replicated across three availability zones. The service and the data stay fully available even if an entire availability zone is lost.

.. note::
    
    Although sharding with replicated nodes can reduce failures, it still cannot save a service from the loss of an entire region.

.. seealso::
    
    For information on how to work with shards in Aiven for ClickHouse, see :doc:`Enable reading and writing data across shards </docs/products/clickhouse/howto/use-shards-with-distributed-table>`.

Limitations
-----------

Aiven for ClickHouse has a few restrictions on the disaster recovery capability.

* No backup to another region
* No point in time recovery (PITR)

.. seealso::
    
    For all the restrictions and limits for Aiven for ClickHouse, see :doc:`Aiven for ClickHouse limits and limitations </docs/products/clickhouse/reference/limitations>`.

Related reading
---------------

* :doc:`Disaster Recovery testing scenarios </docs/platform/concepts/disaster-recovery-test-scenarios>`
* :doc:`Failover procedures </docs/products/postgresql/concepts/upgrade-failover>`
