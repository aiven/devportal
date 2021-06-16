Connection Limits Per Plan
=====================================

Aiven for PostgreSQL instances limit the number of allowed connections to make sure that the database is able to serve them all. The ``max_connections`` setting varies according to the service plan as follows:

.. list-table::
   :header-rows: 1

   * - Plan
     - Max Connections
   * - Hobbyist
     - 25
   * - Startup/Business/Premium-4
     - 100
   * - Startup/Business/Premium-8
     - 200
   * - Startup/Business/Premium-16
     - 400
   * - Startup/Business/Premium-32
     - 800
   * - Startup/Business/Premium-64 and above
     - 1000

When several clients or client threads are connecting to the database, Aiven recommends using :doc:`connection pooling<../concepts/pg-connection-pooling>` to limit the number of actual backend connections. Connection pooling is available in all Aiven for PostgreSQL Startup, Business, and Premium plans, and can be :doc:`configured in the console<../howto/manage-pool>`.
