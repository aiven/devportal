Perform a Cassandra major version upgrade
==========================================

Cassandra in-place upgrades allows to upgrade an instances to a new major version without needing to fork and redirect the traffic. The whole procedure usually around one hour or more depending on the size of the cluster.

.. Warning::
    Aiven recommends to **test the upgrade on a fork** of an existing database. Testing on a fork provides the benefit of verifying the impact of the upgrade for the specific service without affecting the running service.

Here are the steps to upgrade a PostgreSQL service:

1. Log in to the Aiven web console and select the instance that you want to upgrade.

2. On the **Overview** page, scroll down to the **Cassandra version** section and click **Upgrade Cassandra**.

3. Select the version that you want to upgrade to.

.. Note::
    When you select the version, the system checks the compatibility of the upgrade.


4. Click **Upgrade**.

   The system starts applying the upgrade.

   a. We will take a fresh backup of the Cassandra cluster.
   b. We do a rolling restart if the nodes within the cluster.
   c. Once all nodes are running the new version we upgrade the sstables to the new format.
.. Note::
   Upgrading the sstables to the new format takes a long time. During the upgrade the cluster is available but with reduced performance.

