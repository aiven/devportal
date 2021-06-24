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

   The system starts applying the upgrade.

   a. Standby nodes are removed and replacements are created for the new version.
   b. The primary node starts an in-place upgrade to the new major version.
   c. Once the upgrade is complete, the replacement standby nodes point to the new primary node for replication.



5. After the upgrade is complete, run ``ANALYZE`` for all active tables in your database to refresh the table statistics.

.. Note::
   Optimizer statistics are not transferred during major version upgrades, running ``ANALYZE`` ensures that queries run efficiently.


More information about upgrade and failover procedures can be found in the :doc:`dedicated page <../concepts/upgrade-failover>`.

.. Warning::
    Once the upgrade is started, the PostgreSQL instance can't be restored to the previous version. Similarly, the pre-existing backups cannot be used for procedures such as Point In Time Recovery since they were created with an earlier version of PostgreSQL.
