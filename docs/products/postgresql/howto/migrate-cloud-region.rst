Migrate to a different cloud provider or region
===============================================

Any Aiven service has the ability to be relocated on a different cloud vendor or region. This is also valid for PostgreSQL where the migration happens without downtime. Cloud provider/region migration are useful in cases where specific needs about latency are required that can be satisfied only by moving the PostgreSQL to a specific new location.

To migrate a PostgreSQL service to a new cloud provider/region

1. Log in to the Aiven web console and select the PostgreSQL instance you want to move.
2. In the **Overview** tab, click **Migrate Cloud**.

.. image:: /images/products/postgresql/migrate-cloud.png
    :alt: Migrate Cloud button on Aiven web console

3. Select the new cloud provider and region where you want to deploy the PostgreSQL instance, then click **Create**

The PostgreSQL cluster will enter the ``REBALANCING`` state, still serving queries from the old provider/region.

.. image:: /images/products/postgresql/migrate-rebalancing.png
    :alt: Image showing a PostgreSQL cluster in ``REBALANCING`` state

New nodes will be added to the existing PostgreSQL cluster residing in the new provider/region and the data will be replicated to the new nodes. Once the new nodes are in sync, one of them will become the new primary node and all the nodes in the old provider/region will be decommissioned. After this phase the cluster enters in the ``RUNNING`` status, the PostgreSQL endpoint will not change.

.. image:: /images/products/postgresql/migrate-running.png
    :alt: Image showing a PostgreSQL cluster in ``RUNNING`` state

.. Tip::
    To have consistent query time across the globe, consider :doc:`creating several read-only replicas across different cloud provider/regions <create-read-replica>`
