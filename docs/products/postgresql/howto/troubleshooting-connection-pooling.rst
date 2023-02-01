Troubleshooting connection pooling 
==================================

PgBouncer is a lightweight connection pooler for PostgreSQL® with low memory requirements (2 kB per connection by default).

PgBouncer offers several methods when rotating connections:

Session pooling
  Most polite method. When a client connects, a server connection will be assigned to it for the whole duration it stays connected. When the client disconnects, the server connection will be put back into pool. This mode supports all PostgreSQL features.

Transaction pooling
  A server connection is assigned to a client only during a transaction. When PgBouncer notices that the transaction is over, the server will be put back into the pool.
  This mode breaks a few session-based features of PostgreSQL. You can use it only when the application cooperates by not using features that break. See the table below for incompatible features.

Statement pooling
  Most aggressive method. This is transaction pooling, however Multi-statement transactions are disallowed. This is meant to enforce ``autocommit`` mode on the client, mostly targeted at PL/Proxy.

When PgBouncer pooling is used, high CPU utilization may indicate a usage anti-pattern with suboptimal pooling method selection, or frequent reconnect.

SSL handshakes are expensive, where asymmetric cryptography adds overhead; after negotiation, relatively efficient symmetric ciphers are used.
If clients in the application pool frequently disconnect between queries, this negates part of the benefit of the pooler and adds additional overhead.

For most applications, with a large pool of clients, ``Transaction pooling`` will allow the application pool to maintain their connections, thus avoiding the overhead of new connection requests.

For the setup and configurations of PgBouncer please refer to this `help article. <https://docs.aiven.io/docs/products/postgresql/concepts/pg-connection-pooling.html>`_