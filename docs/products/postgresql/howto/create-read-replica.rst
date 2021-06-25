Create read-only replicas
=========================

PostgreSQL read-only replicas provide a great way to reduce the load on the primary server by enabling read-only queries to be performed against the replica. It's also a good option when willing to optimise query response time across different geographical locations since, with Aiven, the replica can be placed on different regions or even different cloud providers.

To set up a remote replica:

1. Log in to the Aiven web console.
2. Select the PostgreSQL instance for which you want to create a remote replica.
3. In the **Overview** tab, click **Create read replica**.

.. image:: /images/products/postgresql/read-replica-create.png
    :alt: Create read replica button

4. Enter a name for the remote replica and select the cloud provider, region, and Aiven for PostgreSQL service plan that you want to use, then click **Create**

The read-only replica is created and added to the list of services in your project. The **Overview** page of the replica indicates the name of the primary service for the replica.

.. image:: /images/products/postgresql/read-replica-detail.png
    :alt: Image of the name of the primary service in the read only replica overview tab

In case of need, read-only replicas can be manually promoted as master. For more complex high availability and failover scenarios check the :doc:`related documentation <../concepts/high-availability>`.
