Upgrade and failover procedures
===============================

Aiven for PostgreSQL® Business and Premium plans include **standby read-replica** servers. If the primary server fails, a standby replica server is automatically promoted as new primary server.

.. Warning::
    Standby read-replica servers available on PostgreSQL Business and Premium plans are substantially different from manually created read-replica services since the latter are not promoted if the primary server fails.

There are two distinct cases when failover or switchover occurs:

1. Uncontrolled primary/replica disconnection
2. Controlled switchover during rolling-forward upgrades

.. Warning::
    For Hobbyist and Startup plans, due to missing standby read-replica servers, uncontrolled disconnections can only be mitigated by restoring data from a backup, and can result in data loss of the database changes since the latest backup data that was uploaded to object storage.

.. _Failover PGUncontrolled:

Uncontrolled primary/replica disconnection
------------------------------------------

When a server unexpectedly disconnects, there is no certain way to know whether it really disappeared or whether there is a temporary glitch in the cloud provider's network. Aiven's management platform has different procedures in case of primary or replica nodes disconnections.

Primary server disconnection
""""""""""""""""""""""""""""

If the **primary** server disappears, Aiven's management platform uses a **60-second timeout** before marking the server as down and promoting a replica server as new primary. During this 60-second timeout, the master is unavailable (``servicename-projectname.aivencloud.com`` does not respond), and ``replica-servicename-projectname.aivencloud.com`` works fine (in read-only mode).

After the replica promotion, ``servicename-projectname.aivencloud.com`` would point to the new primary server, while ``replica-servicename-projectname.aivencloud.com`` becomes unreachable. Finally, a new replica server is created, and after the synchronisation with the primary, the  ``replica-servicename-projectname.aivencloud.com`` DNS is switched to point to the new replica server.

Replica server disconnection
""""""""""""""""""""""""""""

If the **replica** server disappears, Aiven's management platform uses a **300-second timeout** before marking the server as down and creating a new replica server. During this period, the DNS ``replica-servicename-projectname.aivencloud.com`` points to the disappeared server that might not serve queries anymore. The DNS record pointing to the primary server (``servicename-projectname.aivencloud.com``) remains unchanged.

If the replica server does not come back online during these 300 seconds, ``replica-servicename-projectname.aivencloud.com`` is pointed to the primary server until a new replica server is fully functional.

Controlled switchover during upgrades or migrations
---------------------------------------------------

.. Note::
    
    The below doesn't apply to major version upgrade with ``pg_upgrade``, for major version upgrade please read the related :doc:`how-to </docs/products/postgresql/howto/upgrade>`.

During maintenance updates, cloud migrations, or plan changes, the below procedure is followed:

1. For each of the **replica** nodes (available only on Business and Premium plans), a new server is created, and data restored from a backup. Then the new server starts following the existing primary server. After the new server is up and running and data up-to-date, ``replica-servicename-projectname.aivencloud.com`` DNS entry is changed to point to it, and the old replica server is deleted.

2. An additional server is created, and data restored from a backup. Then the new server is synced up to the old primary server.

3. Cluster replication is changed to **quorum commit synchronous** to avoid data loss when changing primary server.

.. Note::
    At this stage, one extra server is running: the old primary server, and N+1 replica servers (2 for Business and 3 for Premium plans).

3. The old primary server is scheduled for termination, and one of the new replica servers is immediately promoted as a primary server. ``servicename-projectname.aivencloud.com`` DNS is updated to point to the new primary server. The new primary server is removed from the ``replica-servicename-projectname.aivencloud.com`` DNS record.

.. Note::
    The old primary server is kept alive for a short period of time (minimum 60 seconds) with a TCP forwarding setup pointing to the new primary server allowing clients to connect before learning the new IP address.

Recreation of replication slots
-------------------------------

In case of failover or controlled switchover of an Aiven for PostgreSQL service, the replication slots from the old primary server are automatically recreated in the new primary server.

One-node cluster
""""""""""""""""

Before replacing a node in the one-node cluster, the new node acquires information on replication slots on the original service, re-creates them, and only then the failover is performed.

Multi-node cluster
""""""""""""""""""

For multi-node setups, replication slots from the primary are synchronized to the standbys periodically. At regular time intervals

* Dependencies for newly-created slots are installed in the corresponding databases (currently, every 30 seconds)
* Positions (``confirmed_flush_lsn``) of the slots are synchronized on the primary and the standbys.

At the time when a failover to a standby occurs, the standby already has active replication slots with fairly up-to-date positions from the primary (with a possible 5-second delay).

.. note::

    * In case of uncontrolled failover, slots created up to 30 seconds before the failover might be lost.
    * Since, positions of recovered replication slots on the new primary might be several seconds delayed from the old primary, you might receive entities that you've already received before when connecting to the slot after the failover without specifying a position.

