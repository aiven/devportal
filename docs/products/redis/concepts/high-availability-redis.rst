High availability in Aiven for Redis 
====================================

Aiven for Redis is available on a variety of plans, offering different levels of high availability. The selected plan defines the features available, and a summary is provided in the table below:

.. list-table::
    :header-rows: 1

    * - Plan
      - High Availability Features
      - Backup History
    * - **Hobbyist**
      - Single-node with limited availability and durability when faults occur
      - 2 days
    * - **Startup**
      - Single-node with limited availability and durability when faults occur
      - 2 days
    * - **Business**
      - Two-node (primary + standby) with higher availability
      - 14 days
    * - **Premium**
      - Three-node (primary + standby + standby) with top availability characteristics
      - 30-day
    * - **Custom**
      - Four-node (primary + N x standby) with top availability characteristics
      - 30-day


Failure handling
----------------

- **Minor failures**, such as service process crashes or temporary loss of network access are handled by Aiven automatically in all plans without any major changes to the service deployment. The service automatically restores normal operation once the crashed process is automatically restarted or when the network access is restored.
- **Severe failure**, such as losing a node entirely in case of hardware or severe software problems, requires more drastic recovery measures. Losing an entire node (virtual machine) could happen, for example, due to hardware failure or a severe enough software failure. The Aiven monitoring infrastructure automatically detects a failing node both when the node starts reporting that its own self-diagnostics is having problems or when the node stops communicating entirely. The monitoring infrastructure automatically schedules a new replacement node to be created.

.. Note::
        In case of database failover, the **Service URI** of your service remains the same, only the IP address changes to point to the new master node.

Highly available business, premium and custom service plans
------------------------------------------------------------

When the failed node is a Redis **standby**, the **primary** node keeps on running normally, and provides normal service level to the client applications. Once the new replacement standby node is ready and synchronized with the master, it starts replicating the master in real time as the situation reverts back to normal.

When the failed node is a Redis **primary**, the combined information from the Aiven monitoring infrastructure and the standby node is used to make a failover decision. The standby node is then promoted as the new primary and immediately starts serving clients. A new replacement node is automatically scheduled and becomes the new standby node.

If all the **primary** and **standby nodes** fail at the same time, new nodes are automatically scheduled for creation to become the new primary and standby. The primary node is restored from the latest available backup, which could involve some degree of data loss. Namely all the writes to the database since the last backup will be lost.

.. Note::
        The amount of time it takes to replace a failed node depends mainly on the used **cloud region** and the **amount of data** that needs to be restored. However, in the case of services with two or more node Business, Premium and Custom plans the surviving nodes will keep on serving clients even during the recreation of the other node. All of this is automatic and requires no administrator intervention.


Single-node hobbyist and startup service plans
------------------------------------------------

Losing the only node from the service immediately starts the automatic process of creating a new replacement node. The new node starts up, restores its state from the latest available backup and resumes serving customers.

Since there was just a single node providing the service, the service  will be unavailable for the duration of the restore operation. All the write operations made since the last backup are lost.



