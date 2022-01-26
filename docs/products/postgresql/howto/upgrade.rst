Perform a PostgreSQL major version upgrade
==========================================

PostgreSQL in-place upgrades allows to upgrade an instances to a new major version without needing to fork and redirect the traffic. The whole procedure usually takes 60 seconds or less.

.. Warning::
    Aiven recommends to **test the upgrade on a fork** of an existing database. Testing on a fork provides the benefit of verifying the impact of the upgrade for the specific service without affecting the running service.

Here are the steps to upgrade a PostgreSQL service:

1. Log in to the Aiven web console and select the instance that you want to upgrade.

2. On the **Overview** page, scroll down to the **PostgreSQL version** section and click **Upgrade PostgreSQL**.

3. Select the version that you want to upgrade to.

.. Note::
    When you select the version, the system checks the compatibility of the upgrade.


4. Click **Upgrade**.

   Here is the sequence of events that happen:

   a. A ``pg_upgrade --check`` on the server to be as sure as possible that the upgrade on the master node is possible.
   b. Reduce cluster size to 1 node (master) - if there is a standby node in the service, it is deleted.
   c. Perform upgrade **ONLY** on master node.
      1. systemd service is restarted several times in the process.
      2. Extensions get updated.
      3. data dir changes, data dir format changes, pghoard directory changes.
      4. service_state, user_config changes to reflect the changes.
   d. Do the first basebackup with the new version.
   e. Create the rest of the nodes in the service, and update & recycle the read replica (if any).
   f. The standby nodes are only recreated **after** the upgrade is ready on the primary and the first basebackup has been taken with the new version.
   g. Standby nodes are running. Any service alert blackout existing on the read replica is being removed. 
   g. Once the upgrade is complete, the replacement standby nodes point to the new primary node for replication.


5. After the upgrade is complete, run ``ANALYZE`` for all active tables in your database to refresh the table statistics.

.. Note::
   Optimizer statistics are not transferred during major version upgrades, running ``ANALYZE`` ensures that queries run efficiently.


More information about upgrade and failover procedures can be found in the :doc:`dedicated page <../concepts/upgrade-failover>`.

.. Warning::
    Once the upgrade is started, the PostgreSQL instance can't be restored to the previous version. Similarly, the pre-existing backups cannot be used for procedures such as Point In Time Recovery since they were created with an earlier version of PostgreSQL.
