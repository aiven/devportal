High availability
=================

Aiven for PostgreSQL is available on a variety of plans, offering different levels of high availability. The selected plan defines the features available, and a summary is provided in the table below:

.. list-table::
    :header-rows: 1

    * - Plan
      - High Availability Features
      - Backup History
    * - **Hobbyist**
      - Single-node with limited availability
      - 2 days
    * - **Startup**
      - Single-node with limited availability
      - 2 days
    * - **Business**
      - Two-node (primary + standby) with higher availability
      - 14 days
    * - **Premium**
      - Three-node (primary + standby + standby) with top availability characteristics
      - 30-day

About primary and standby nodes
-------------------------------

Aiven's Business and Premium plans offer :ref:`primary <Terminology PGPrimary>` and :ref:`standby <Terminology PGStandby>` nodes. Having a standby service is useful for multiple reasons:

* Provides another physical copy of the data in case of hardware, software, or network failures
* Typically reduces the data loss window in disaster scenarios
* Provides a quicker database time to restore with a controlled failover in case of failures, as the standby is already installed, running, and synchronised with the data
* Can be used for read-only queries to reduce the load on the primary server

Failure handling
----------------

**Minor failures**, such as service process crashes or temporary loss of network access, are handled automatically by Aiven in all plans without any major changes to the service deployment. The service automatically restores normal operation once the crashed process is automatically restarted or when network access is restored.

**Severe failures**, such as losing a node entirely in case of hardware or severe software problems, require drastic recovery measures. The Aiven monitoring infrastructure automatically detects a failing node both when the node starts reporting issues in the self-diagnostics or when stops communicating. In such cases, the monitoring infrastructure automatically schedules a new replacement node to be created.

.. Note::
    In the event of database failover, the **Service URI** of your service remains the same; only the IP address will change to point to the new primary node.

Highly available Business and Premium service plans
---------------------------------------------------

When the failed node is a PostgreSQL **standby** node, the primary node keeps running normally and provides a normal service level to the client applications. Once the new replacement standby node is ready and synchronised with the primary node, it starts replicating the primary node in real time as the situation reverts back to normal.

When the failed node is a PostgreSQL **primary** node, the combined information from the Aiven monitoring infrastructure and the standby node is used to make a failover decision. The standby node is then promoted as the new primary and immediately starts serving clients. A new replacement node is automatically scheduled and becomes the new standby node.

If all the **primary** and **standby nodes** fail at the same time, new nodes are automatically scheduled for creation to become the new primary and standby. The primary node is restored from the latest available backup, which could involve some degree of data loss. Any write operations made since the backup of the latest :ref:`WAL<Terminology PGWAL>` file are lost. Typically, this time window is limited to either five minutes of time or one :ref:`WAL<Terminology PGWAL>` file.

.. Note::
    The amount of time it takes to replace a failed node depends mainly on the selected cloud region and the amount of data to be restored. However, in the case of partial loss of the cluster, the surviving node keeps on serving clients even during the recreation of the other node. All of this is automatic and requires no administrator intervention.

**Premium** plans operate in a similar way as **Business** plans. The main difference comes when one of the **standby** or **primary** nodes fails. Premium plans have an additional, redundant standby node available, providing platform availability even in the event of losing two nodes. In cases where the primary node fails, Aiven monitoring tool, using :ref:`PGLookout<Terminology PGLookout>`, determines which of the standby nodes is the furthest along in replication (has the least potential for data loss) and does a controlled failover to that node.

.. Note::
    For backups and restoration, Aiven utilises the popular Open Source backup daemon :ref:`PGHoard <Terminology PGHoard>`, which Aiven maintains. It makes real-time copies of :ref:`WAL<Terminology PGWAL>` files to an object store in compressed and encrypted format.

Single-node Hobbyist and Startup service plans
----------------------------------------------

Hobbyist and Startup plans provide a single node; when it's lost, Aiven immediately starts the automatic process of creating a new replacement node. The new node starts up, restores its state from the latest available backup, and resumes serving customers.

Since there is just a single node providing the service, the service is unavailable for the duration of the restoration. In addition, any write operations made since the backup of the latest :ref:`WAL<Terminology PGWAL>` file are lost. Typically, this time window is limited to either five minutes of time or one :ref:`WAL<Terminology PGWAL>` file.

More information about on PostgreSQL upgrade and failover procedures is available at :doc:`the dedicated page <upgrade-failover>`.
