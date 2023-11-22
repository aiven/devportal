Manage connection pooling
=========================

Connection Pooling allows you to maintain very large numbers of connections to a database while minimizing the consumption of server resources. Read more about it on :doc:`/docs/products/postgresql/concepts/pg-connection-pooling`.

Connection pooling tips
-----------------------------

You can connect directly to the PostgreSQL® server using the **Service URI** setting listed on the **Overview** page. However, this URI doesn't make use of the PgBouncer pooling. PgBouncer pools use a different port number than the regular PostgreSQL server port. The PgBouncer **Service URI** for a particular pool can be found in `Aiven Console <https://console.aiven.io/>`_ > your service's page > **Pools** view (available from the sidebar).
You can also view the generic PgBouncer **Service URI** for your pools in `Aiven Console <https://console.aiven.io/>`_: your service's page > **Overview** page > **PgBouncer** tab > **Service URI**.

You can use both pooled and non-pooled connections at the same time.

.. Note::
    If you have set a custom ``search_path`` for your database, this is not automatically set for your new connection pool. Remember to set it also for new connection pools when you create them.

Manage connection pools
-----------------------------

To manage the connection pools, take the following steps:

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and select your Aiven for PostgreSQL service.

2. In your service's page, select **Pools** from the sidebar.

3. In the **Pools** view, you can check the available connection pools and add or remove them.

   The settings available are as follows:

   * **Pool name**: Enter a name for your connection pool here. This also becomes the ``database`` or ``dbname`` connection parameter for your pooled client connections. This parameter must be equal to the ``Database`` parameter. 
   * **Database**: Choose the database that you want to connect to. Each pool can only connect to a single database.
   * **Username**: Select the database username that you want to use when connecting to the backend database.
   * **Pool Mode**: Select the pooling mode as described in more detail above.
   * **Pool Size**: Select how many PostgreSQL server connections this pool can use at a time. 
   
   .. important:: 
    The **Pool Size** parameter is NOT the maximum number of client connections of this pool.
    
    Each pool can handle from a minimum of 5000 client connections to a maximum defined by the lower threshold between:
    
    * 500 for each GB of RAM in the service plan
    * A total of 50000 client connections

4. Select **Info** on an existing pool.

   This shows you the database connection settings for the pool.

Connection pools for replicas
-----------------------------

For all Business and Premium plans, whenever you define a connection pool, the same connection pool is created both for primary and standby servers. For standby servers, the connection pool URI is exactly the same as for the primary server, except that the host name has a ``replica-`` prefix.

For example, if the primary connection URI is as follows::

    postgres://avnadmin:password@pg-prod-myproject.aivencloud.com:20986/mypool?params

The replica connection pool URI is as follows::

    postgres://avnadmin:password@replica-pg-prod-myproject.aivencloud.com:20986/mypool?params
