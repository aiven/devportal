About PostgreSQL® disk usage
============================

When you create your first Aiven for PostgreSQL® service, you may see the disk usage gradually increasing even though you are not yet inserting or updating much data.

.. image:: /images/products/postgresql/initial-disk-usage.png
   :alt: Disk space usage graph showing % growing over an hour

This is completely normal within the first 24 hours of operation for Aiven for PostgreSQL services because of our WAL (Write-Ahead Logging) archiving settings.

To prevent loss of data due to node failure on Hobbyist and Startup plans, we set the ``archive_timeout`` configuration to write WAL segments to disk at regular intervals. The WAL segments are then backed up to cloud storage. Even if your service is idle, each WAL segment occupies the same amount of space on disk, which is why the disk usage grows steadily over time.

After the first 24 hours of service, the system begins archiving old WAL segments and deleting them from disk to free up space. From this point onward, new WAL segments no longer have such a high impact on disk usage as the service reaches a steady state for low-traffic services.

You can read more about WAL archiving `in the PostgreSQL manual <https://www.postgresql.org/docs/current/runtime-config-wal.html#RUNTIME-CONFIG-WAL-ARCHIVING>`_.


---------------------------
High disk usage discrepancy
---------------------------
There can be instances when you notice your disk space usage increasing contrary to the amount of data is being written to your database.  This could be caused due to an inactive replication slot present in your database.

You can check the list of replication slot subscriptions created on your service using the following command:

.. code-block:: shell

   SELECT * FROM aiven_extras.pg_list_all_subscriptions();

Inactive replication slots can cause indefinite increase in WAL log size.  

To resolve the issue, you can perform one of the following options:

* Have a client connect to the replication slot so that the WAL files would be rotated and purged  
* Manually remove the unused replication slots (see our "Remove unused replication setup" under :doc:`Setup logical replication slots <../howto/setup-logical-replication>` documentation)