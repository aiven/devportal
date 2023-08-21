Create and use read-only replicas
=================================

PostgreSQL® read-only replicas provide a great way to reduce the load on the primary server by enabling read-only queries to be performed against the replica. It's also a good way to optimise query response times across different geographical locations since, with Aiven, the replica can be placed in different regions or even different cloud providers.

.. note::
    If your service is running a ``business-*`` or ``premium-*`` plan, you have
    standby nodes available in a high availability setup. These support read-only
    queries to reduce the effect of slow queries on the primary node.


Create a replica
----------------

To set up a remote replica:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.
2. Select the PostgreSQL instance for which you want to create a remote replica.
3. In the **Overview** page of your service, select **Create replica**.

.. image:: /images/products/postgresql/replica-create.png
    :alt: Create replica button

4. Enter a name for the remote replica and select the cloud provider, region, and Aiven for PostgreSQL service plan that you want to use, then select **Create**.

The read-only replica is created and added to the list of services in your project. The **Overview** page of the replica indicates the name of the primary service for the replica.

Read-only replicas can be manually promoted to become the master database if the need arises. For more complex high availability and failover scenarios check the :doc:`related documentation <../concepts/high-availability>`.

.. Tip::
    
    You can promote a read-replica to master using the API endpoint to `delete the service integration <https://api.aiven.io/doc/#operation/ServiceIntegrationDelete>`_ and passing the ``integration_id`` of the replica service. 
    
    Deleting the integration that comes with ``integration_type`` of value ``read_replica`` will lead to the service to no longer be a read-replica, hence becoming the master.


Use a replica
-------------

To use a read only replica:

1. Log in to the Aiven web console and select your PostgreSQL service.
2. In the **Overview** page, copy the **Replica URI** an use it to connect via ``psql``::

    psql POSTGRESQL_REPLICA_URI


Identify replica status
-----------------------

To check whether you are connected to a primary or replica node, run the following command within a ``psql`` terminal already connected to a database::

    SELECT * FROM pg_is_in_recovery();

If the above command returns ``TRUE`` if you are connected to the replica, and ``FALSE`` if you are connected to the primary server.

.. Warning::

    Aiven for PostgreSQL uses asynchronous replication and so a small lag is expected. When running an ``INSERT`` operation on the primary node, a minimal delay (usually less than a second) can be expected for the change to be propagated to the replica and to be visible there.

Read-replica for disaster recovery
----------------------------------
High availability enables data distribution across availability zones within a single region. To accomplish that without a default multi-region service with node allocation spanning multiple regions, you can take the following steps:

- Establish a high-availability Aiven for PostgreSQL service within a single region.
- Configure a remote read-only replica in a different region or even on an alternate cloud platform.

As a result, you introduce an additional node in the distinct region/cloud. Since this node does not work as a hot standby node, you might want to promote it manually to the primary role, which makes it operate as an independent standalone service.