High availability in Aiven for Redis®*
======================================

Aiven for Redis®* is available on a variety of plans, offering different levels of high availability. The selected plan defines the features available, and a summary is provided in the table below:

.. list-table::
    :header-rows: 1
    :widths: 20 20 30 30 10

    * - Plan
      - Nodes configuration
      - High availability & failover features
      - Backup features
      - Backup history
    * - **Hobbyist**
      - Single-node
      - Limited availability. No automatic failover.
      - Single backup only for disaster recovery.
      - N/A
    * - **Startup**
      - Single-node
      - Limited availability. No automatic failover.
      - Automatic backups to a remote location.
      - 1 day
    * - **Business**
      - Two-node (primary + standby)
      - High availability with automatic failover to a standby node if the primary fails.
      - Automatic backups to a remote location.
      - 3 days
    * - **Premium**
      - Three-node (primary + standby + standby)
      - Enhanced high availability with automatic failover among multiple standby nodes if the primary fails.
      - Automatic backups to a remote location.
      - 13 days
    * - **Custom**
      - Custom configurations
      - Custom high availability and failover features based on user requirements.
      - Custom backup features based on user requirements.
      - Custom based on user requirements



Check out our `Plans & Pricing <https://aiven.io/pricing?product=redis>`_ page for more information. 

Failure handling
----------------

- **Minor failures**: Aiven automatically handles minor failures, such as service process crashes or temporary loss of network access, without any significant changes to the service deployment. In all plans, the service instantly restores normal operation by automatically restarting the crashed process or restoring the network access once available.
- **Severe failures**: In case of severe hardware or software problems, such as losing an entire node, more drastic recovery measures are required. Aiven's monitoring infrastructure automatically detects a failing node when it reports problems with its self-diagnostics or stops communicating altogether. The monitoring infrastructure then schedules the creation of a new replacement node.


.. Note::
        In case of database failover, your service's **Service URI** remains the same—only the IP address changes to point to the new primary node.


Highly available business, premium, and custom service plans
------------------------------------------------------------

If a Redis node fails and is a standby node, the primary node continues to run normally, providing uninterrupted service to client applications. Once a new replacement standby node is ready and synchronized with the primary, it replicates it in real time until the situation returns to normal.

When the failed node is a Redis **primary**, the combined information from the Aiven monitoring infrastructure and the standby node is used to make a failover decision. The standby node is promoted as the new primary and immediately serves clients. A new replacement node is automatically scheduled and becomes the new standby node.

If both the **primary** and **standby** nodes fail simultaneously, new nodes will be created automatically to take their place as the new primary and standby. However, this process will involve some degree of data loss since the primary node will be restored from the most recent backup available. Therefore, any writes made to the database since the last backup will be lost.

.. Note::
        The amount of time it takes to replace a failed node depends mainly on the used **cloud region** and the **amount of data** that needs to be restored. However, in the case of services with two or more node Business, Premium and Custom plans the surviving nodes will keep on serving clients even during the recreation of the other node. All of this is automatic and requires no administrator intervention.


Single-node hobbyist and startup service plans
------------------------------------------------

Losing the only node in the service triggers an automatic process of creating a new replacement node. The new node then restores its state from the latest available backup and resumes serving customers.

Since there was just a single node providing the service, the service  will be unavailable for the duration of the restore operation. All the write operations made since the last backup are lost.



