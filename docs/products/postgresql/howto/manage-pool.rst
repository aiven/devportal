Manage connection pooling
=========================

Connection Pooling allows you to maintain very large numbers of connections to a database while minimizing the consumption of server resources. Read more about it on :doc:`../concepts/pg-connection-pooling`.

Connection pooling tips
-----------------------------

You can connect directly to the PostgreSQL server using the **Service URI** setting listed on the **Overview** page however this URI doesn't make use of PgBouncer pooling. PgBouncer pools use a different port number than the regular PostgreSQL server port, the PgBouncer **Service URI** for a particular pool can be found in the Aiven console, under the **Pool** tab in the service page.

You can use both pooled and non-pooled connections at the same time.

.. Note::
    If you have set a custom ``search_path`` for your database, this is not automatically set for your new connection pool. Remember to set it also for new connection pools when you create them.

Manage connection pools
-----------------------------

To manage the connection pools, follow the steps below:

1. Log in to the Aiven web console and select your PostgreSQL service.

2. On the **Pools** tab you can see the list, add or remove pools.

   The settings available are:

   * **Pool name:** Enter a name for your connection pool here. This also becomes the ``database`` or ``dbname`` connection parameter for your pooled client connections.
   * **Database**: Choose the database that you want to connect to. Each pool can only connect to a single database.
   * **Username:** Select the database username that you want to use when connecting to the backend database.
   * **Pool Mode:** Select the pooling mode as described in more detail above.
   * **Pool Size:** Select how many PostgreSQL server connections this pool can use at a time.


3. Click **Info** on an existing pool.

   This shows you the database connection settings for the pool, similar to the below

.. image:: /images/products/postgresql/connection-pool-details.png


Connection pools for replicas
-----------------------------

For all Business and Premium plans, whenever you define a connection pool, the same connection pool is created both for primary and standby servers. For standby servers, the connection pool URI is exactly the same as for the primary server, except that the host name has a ``replica-`` prefix.

For example, if the primary connection URI is::

    postgres://avnadmin:password@pg-prod-myproject.aivencloud.com:20986/mypool?params

The replica connection pool URI is::

    postgres://avnadmin:password@replica-pg-prod-myproject.aivencloud.com:20986/mypool?params
