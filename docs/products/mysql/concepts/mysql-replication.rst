MySQL replication
=================

.. _replication-overview:

Overview
--------

MySQL replication is always based on replicating logical changes. This means that the replication protocol may contain an actual statement that the target server should apply or it may have an entry saying **update row with these old attributes to have these new attributes**. These are called statement and row formats.

The statement format is more compact but cannot represent all changes because some statements would yield different results if executed as is on different servers. The row format statement can represent all changes, and it allows using tools like Debezium since the binary log contains full details of all changes in itself. For these reasons Aiven uses row format by default. 

The row based replication works very well as long as the tables being replicated have a primary key. MySQL primary key look ups are very fast and the target server can find the rows to update and delete very quickly. However, when the table being replicated is lacking a primary key the, the target server needs to make a sequential table scan for each individual update or delete statement and the replication can become extremely slow if the table is large.

.. code::

    DELETE FROM nopk WHERE modified_time > '2022-01-13' 

If a statement like above matched 500 rows and the table had a million rows altogether, the row based replication format would contain 500 individual delete operations and the target server needed to do sequential scan over the one million rows for each of the individual deletions, which could take tens of minutes. If the table had a primary key the same statement would likely be replicated in under a second.

Replication use in Aiven for MySQL
----------------------------------

The considerations presented on the :ref:`Replication Overview <replication-overview>` section are not only valid for services that actually have standby nodes or read replicas. Whenever the Aiven management platform needs to create a new node for a service, the node is first initialized from backup to most recent backed up state. This includes applying the full replication stream that has been created after the most recent full base backup. Once the latest backed
up state has been restored the node will connect to the current master, if available, and replicate latest state from that, which is also affected by possible replication slowness.

When new nodes are created, it needs to perform replication and having large tables without primary keys may make operations such as replacing failed nodes, upgrading service plan, migrating service to a different cloud provider or region, starting up new read replica service, forking a service, and some others to take extremely long time or depending on the situation practically not complete at all without manual operator intervention (e.g. new read replica might never be able to catch up with existing master because replication is too slow). 

To work around these issues Aiven operations people may need to resort to operations such as temporarily making ``master`` read only or promoting a replacement server before it has fully applied the replication stream, resulting in data loss. 

To make the service operate correctly and avoid such drastic measures you should ensure the primary keys exist for any tables that are not trivially small. You can check the article how to :doc:`create missing primary keys </docs/products/mysql/howto/create-missing-primary-keys>` to ensure primary keys exists in your Aiven for MySQL service.
