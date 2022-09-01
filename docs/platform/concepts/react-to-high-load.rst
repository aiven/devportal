React to high load
==================

If your services are currently under heavy load and you want to quickly diagnose and restore normal operations, here are some options to consider.

Low resources
'''''''''''''

First, using the Metrics tab in the Aiven Console you can check several metrics for your service in real time. Aiven automation monitors your services and sends warning emails if these reach critical levels, but by checking these indicators yourself you can see which resources are scarce (or close to running out) for your service and act accordingly.

The short term solution for a service operating at high resource utilization is to upgrade your service plan. In the long term you can look into optimizing your workload to reduce resource consumption. During the service plan upgrade your service(s) would still be online as the upgrade is performed in rolling forward style.

Disk full
'''''''''

Many of our services will stop accepting writes when the disk is almost full to avoid a situation where backups can no longer be taken. Check these service specific guides for resolutions:

- `https://docs.aiven.io/docs/products/kafka/howto/prevent-full-disks.html <https://docs.aiven.io/docs/products/kafka/howto/prevent-full-disks.html>`_

- `https://docs.aiven.io/docs/products/mysql/howto/prevent-disk-full.html <https://docs.aiven.io/docs/products/mysql/howto/prevent-disk-full.html>`_

- `https://docs.aiven.io/docs/products/postgresql/howto/prevent-full-disk.html <https://docs.aiven.io/docs/products/postgresql/howto/prevent-full-disk.html>`_

High load average
'''''''''''''''''

Note that the Load Average is not a percentage and should ideally be below the number of CPU available on your service plan. In the short term the simplest approach is to upgrade to a larger plan to accommodate the load.

Too many connections
''''''''''''''''''''

As your application scales horizontally to accommodate increased traffic it may also consume more and more database connections. In the short term, upgrading the plan will allow you to create more connections. The limits are give in service specific documentation:

- `https://docs.aiven.io/docs/products/mysql/concepts/max-number-of-connections.html <https://docs.aiven.io/docs/products/mysql/concepts/max-number-of-connections.html>`_

- `https://docs.aiven.io/docs/products/postgresql/reference/pg-connection-limits.html <https://docs.aiven.io/docs/products/postgresql/reference/pg-connection-limits.html>`_

- `https://docs.aiven.io/docs/products/redis/howto/estimate-max-number-of-connections.html <https://docs.aiven.io/docs/products/redis/howto/estimate-max-number-of-connections.html>`_

In the case of PostgreSQL®, where the connection limits are tightest, there is a longer term option to use transaction or statement level `connection pooling <https://docs.aiven.io/docs/products/postgresql/concepts/pg-connection-pooling.html>`_ to accommodate more connections even on smaller plans.

Plan upgrade
''''''''''''

The easiest and simplest measure to handle additional traffic is to temporarily upgrade your service plan in the Aiven Console.

After your start the upgrade, Aiven will provision new nodes with more CPU, RAM, and storage alongside the existing nodes, stream across the latest data, and then perform a controlled failover to the new nodes.

For service specific update details during an upgrade please see the following support article:

- `https://help.aiven.io/en/articles/495336-how-much-downtime-do-maintenance-operations-cause <https://help.aiven.io/en/articles/495336-how-much-downtime-do-maintenance-operations-cause>`_

**Note that this process is not instant**. Ideally plan upgrades should be started well in advance of high load.

The more modifications made to your data, the longer it will take for new nodes to catch up and take over. For large services already struggling under high load it can take hours for the process to complete. It is best to start the plan upgrade as soon as possible (just after a backup has been taken is the best) and to select a new plan generously to avoid having to upgrade to a new plan several times in a row.

If a plan upgrade is not progressing and downtime is acceptable, then temporarily cutting writes from your application code to reduce load on the existing nodes can help the node replacement complete faster.

Aiven services are billed per hour and almost all can be downgraded to a smaller plan at a later date if the heavy traffic is expected to fall, e.g. after a seasonal spike in demand. Currently the only exceptions are Cassandra® services: the size of the nodes can be changed freely but the total number of nodes cannot be reduced.

Slow queries
''''''''''''

In PostgreSQL® or MySQL®, inefficient queries can consume CPU time and memory unnecessarily. Upgrading the service plan can help but often this alone is not enough to solve the issue.

A good place to start is in the Aiven Console with the Query Statistics and Current Queries tabs. You can click the column headings in the statistics table to sort the rows to find the longest running or most frequent queries. Then you can run EXPLAIN queries from your database shell to see if there are missing indexes that should be created.

If your service is running a PostgreSQL® business-* or premium-* plan then you have standby nodes available in a high availability setup. These are `able to support read-only queries <https://docs.aiven.io/docs/products/postgresql/howto/create-read-replica.html>`_ by direct connections to the Read-only replica URL to reduce the effect of slow queries on the primary node.

For PostgreSQL® and MySQL®, we also offer an option to create a `remote read replica <https://docs.aiven.io/docs/products/postgresql/howto/create-read-replica.html>`_ service which can be setup in the same (or different) cloud and/or region which will provide a dedicated read only service that can be used to reduce the load on the master in case it is under heavy write load.

Support contracts
'''''''''''''''''

All customers have access to our free Basic support service through the chat widget found in the Aiven Console and these help pages. You can also start a conversation with support by emailing support@Aiven.io.

Aiven also offer `three additional support tiers <https://aiven.io/support-services>`_ for our customers. To discuss higher tiers of support please contact your account manager or sales@Aiven.io