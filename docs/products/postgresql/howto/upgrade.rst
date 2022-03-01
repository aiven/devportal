Perform a PostgreSQL® major version upgrade
===========================================

PostgreSQL® in-place upgrades allows to upgrade an instances to a new major version without needing to fork and redirect the traffic. The whole procedure usually takes 60 seconds or less for small databases.

.. Warning::
    Aiven recommends to **test the upgrade on a fork** of an existing database. Testing on a fork provides the benefit of verifying the impact of the upgrade for the specific service without affecting the running service.
    Very large databases may take a long time to upgrade, but a :doc:`read-only replica service <create-read-replica>` may be used if it is necessary to keep the data readable during an upgrade.

Here are the steps to upgrade a PostgreSQL service:

1. Log in to the Aiven web console and select the instance that you want to upgrade.

2. On the **Overview** page, scroll down to the **PostgreSQL version** section and click **Upgrade PostgreSQL**.

3. Select the version that you want to upgrade to.

.. Note::
    When you select the version, the system checks the compatibility of the upgrade.


4. Click **Upgrade**.

   The system starts applying the upgrade.

   a. An automatic check is executed to confirm whether an upgrade is possible (``pg_upgrade --check``).
   b. If the service has more than one node, any standby nodes are shut down and removed, as replication can not be performed during the upgrade.
   c. The primary node starts an in-place upgrade to the new major version.
   d. After a successful upgrade the primary node becomes available for use. A new full backup is initiated.
   e. After completion of the full backup, new standby nodes are created for services with more than one node.
   f. If the service is a configured to have a :doc:`read-only replica service <create-read-replica>`, the replica service will now be upgraded to the same version using the very same process. Read-only replicas remain readable during the upgrade of the primary service, but will go offline for the upgrade at this point.
   g. ``ANALYZE`` will be automatically run for all tables after the upgrade to refresh table statistics and optimize queries.

.. Note::
   A full backup of a large database may take a long time to complete. It may take some time before the standby node becomes available, as they can only be launched when a backup taken from the new version is available.

More information about upgrade and failover procedures can be found in the :doc:`dedicated page <../concepts/upgrade-failover>`.

.. Warning::
    Once the upgrade is started, the PostgreSQL instance can't be restored to the previous version. Similarly, the pre-existing backups cannot be used for procedures such as Point In Time Recovery since they were created with an earlier version of PostgreSQL.
