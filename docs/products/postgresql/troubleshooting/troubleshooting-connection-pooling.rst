Troubleshoot connection pooling problems
========================================

Discover the PgBouncer connection pooler and check out how to cope with some specific connection pooling issues.

About connection pooling with PgBouncer
---------------------------------------

PgBouncer is a lightweight connection pooler for PostgreSQL® with low memory requirements (2 kB per connection by default).

PgBouncer offers several methods when rotating connections:

Session pooling
    This is the most permissive method. When a client connects, it gets assigned with a server connection that is maintained as long as the client stays connected. When the client disconnects, the server connection is put back into the pool. This mode supports all PostgreSQL features.

Transaction pooling
  A server connection is assigned to a client only during a transaction. When PgBouncer notices that the transaction is over, the server connection is put back into the pool.

  .. warning::

    This mode breaks a few session-based features of PostgreSQL. Use it only when the application cooperates without using the features that break. For imcompatible features, see `PostgreSQL feature map for pooling modes <https://www.pgbouncer.org/features>`_.

Statement pooling
  This is the most restrictive method, which disallows multi-statement transactions. This is meant to enforce the ``autocommit`` mode on the client and is mostly targeted at PL/Proxy.

Handling connection pooling issues
----------------------------------

A high CPU utilization while using the PgBouncer pooling may indicate a usage anti-pattern with a suboptimal pooling method selection or frequent reconnect operations.

SSL handshakes are expensive resource-wise with asymmetric cryptography adding overhead. After a negotiation, relatively efficient symmetric ciphers are used.

If clients in the application pool frequently disconnect between queries, this negates part of the benefit of the pooler and adds additional overhead.

For most applications with a large pool of clients, the transaction pooling allows the application pool to maintain their connections, thus avoiding the overhead of new connection requests.

.. seealso::

    For the setup and configurations of PgBouncer, refer to :doc:`Connection pooling </docs/products/postgresql/concepts/pg-connection-pooling>`.
