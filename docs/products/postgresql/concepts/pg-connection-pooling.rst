PostgreSQL connection pooling
=============================

Connection pooling in Aiven for PostgreSQL services allows you to maintain very large numbers of connections to a database while minimizing the consumption of server resources.


Aiven for PostgreSQL connection pooling uses `PGBouncer <https://www.pgbouncer.org/>`_ to manage the database connection. Each pool can handle up to 5000 database client connections. Unlike when you connect directly to the PostgreSQL server, each client connection does not require a separate backend process on the server. PGBouncer automatically inserts the client queries and only uses a limited number of actual backend connections, leading to lower resource usage on the server and better total performance.

Why connection pooling?
------------------------

A high number of backend connections can become a problem with PostgreSQL, as the resource cost per connection is quite high due to how PostgreSQL manages client connections. PostgreSQL creates a separate backend process for each connection, and the unnecessary memory usage caused by the processes will start affecting the total throughput of the system at some point. Moreover, if each connection is very active, the performance can be affected by the high number of parallel executing tasks.

It makes sense to have enough connections so that each CPU core on the server has something to do (each connection can only utilise a single CPU core), but a hundred connections per CPU core may be too much. All this is workload-specific, but often a good number of connections to have is roughly 3-5 times the CPU core count. Aiven enforces :doc:`connection limits <../reference/pg-connection-limits>` to avoid overloading the PostgreSQL database.



.. Note::
    Since 9.6, PostgreSQL offers parallelization support enabling to `run queries in parallel <https://www.postgresql.org/docs/current/parallel-query.html>`_ on multiple CPU cores.


Without a connection pooler, the database connections are handled directly by PostgreSQL backend processes, with one process per connection:

.. mermaid::

    graph LR
        pg_client_1(PG client) <-.->|Client establishing a new connection| postmaster
        pg_client_2(PG client) ---> pg_backend_1(PG Backend 1)
        pg_client_3(PG client) ---> pg_backend_2(PG Backend 2)
        pg_client_4(PG client) ---> pg_backend_3(PG Backend 3)
        pg_client_5(PG client) --->|Existing client connections| pg_backend_4(PG Backend 4)
        pg_client_6(PG client) ---> pg_backend_5(PG Backend 5)
        pg_client_7(PG client) ---> pg_backend_6(PG Backend 6)

    subgraph PostgreSQL server
        postmaster & pg_backend_1 & pg_backend_2 & pg_backend_3 & pg_backend_4 & pg_backend_5 & pg_backend_6
    end

    subgraph Clients
        pg_client_1 & pg_client_2 & pg_client_3 & pg_client_4 & pg_client_5 & pg_client_6 & pg_client_7
    end


Adding a PGBouncer pooler that utilizes fewer backend connections frees up server resources for more important uses, such as disk caching:

.. mermaid::

    graph LR
        pg_client_1(PG client) <-.->|Client establishing a new connection| pgbouncer
        pg_client_2(PG client) ---> pgbouncer
        pg_client_3(PG client) ---> pgbouncer
        pg_client_4(PG client) ---> pgbouncer
        pg_client_5(PG client) --->|Existing client connections| pgbouncer
        pg_client_6(PG client) ---> pgbouncer
        pg_client_7(PG client) ---> pgbouncer
        pgbouncer --> postmaster
        pgbouncer --> pg_backend_1(PG Backend 1)
        pgbouncer --> pg_backend_2(PG Backend 2)
        pgbouncer --> pg_backend_3(PG Backend 3)
        pgbouncer --> pg_backend_4(PG Backend 4)


    subgraph PostgreSQL server
        pgbouncer
        postmaster & pg_backend_1 & pg_backend_2 & pg_backend_3 & pg_backend_4
    end

    subgraph Clients
        pg_client_1 & pg_client_2 & pg_client_3 & pg_client_4 & pg_client_5 & pg_client_6 & pg_client_7
    end


Instead of having dedicated connections per client, now PGBouncer manages the connections assignment optimising them based on client request and settings like the :ref:`pooling-modes`.

.. Tip::
    Many frameworks and libraries (ORMs, Django, Rails, etc.) support client-side pooling, which solves much the same problem. However, when there are many distributed applications or devices accessing the same database, a server-side solution is a better approach.

.. _pooling-modes:

Connection Pooling Modes
------------------------

Aiven PostgreSQL supports three different operational pool modes: ``transaction``, ``session`` and ``statement``.

* The default and recommended setting option is ``transaction`` pooling mode allows each client connection to take their turn in using a backend connection for the duration of a single transaction. After the transaction is committed, the backend connection is returned back into the pool and the next waiting client connection gets to reuse the same connection immediately. In practice, this provides quick response times for queries as long as the typical execution times for transactions are not excessively long. This is the most commonly used PGBouncer mode and also the default pooling mode in Aiven for PostgreSQL.
* The ``session`` pooling mode means that once a client connection is granted access to a PostgreSQL server-side connection, it can hold it until the client disconnects from the pooler. After this, the server connection is added back onto the connection pooler's free connection list to wait for its next client connection. Client connections are accepted (at TCP level), but their queries only proceed once another client disconnects and frees up its backend connection back into the pool. This mode can be helpful in some cases for providing a wait queue for incoming connections while keeping the server memory usage low, but is of limited use under most common scenarios due to the slow recycling of the backend connections.
* The ``statement`` operational pooling mode, similar to the ``transaction`` pool mode, except that instead of allowing a full transaction to run, it cycles the server-side connections after each and every database statement (``SELECT``, ``INSERT``, ``UPDATE``, ``DELETE`` statements, etc.). Transactions containing multiple SQL statements are not allowed in this mode. This mode is sometimes used, for example when running specialised sharding frontend proxies.
