Monitor PostgreSQL® metrics with pgwatch2
==========================================

`pgwatch2`_ is an open source monitoring solution for PostgreSQL®, created by CYBERTEC and can be used to monitor instances of Aiven for PostgreSQL collecting key PostgreSQL metrics and also gathering data from a wide range of PostgreSQL extensions.

.. Note::

    Aiven for PostgreSQL supports the most popular extensions, but, due to security implications, can't support all the available extensions.
    Check :doc:`../reference/list-of-extensions` and :doc:`../howto/manage-extensions` for details on the supported PostgreSQL extensions on the Aiven platform.

Prepare an Aiven for PostgreSQL instance for pgwatch2
-------------------------------------------------------

The following steps need to be executed on the Aiven for PostgreSQL instance to be monitored with pgwatch2:

1. Create a user for pgwatch2 (with a sensible password)::

    CREATE USER pgwatch2 WITH PASSWORD 'password';

2. Limit the number of connections from pgwatch2 (optional, but recommended in the `pgwatch2 documentation`_)::

    ALTER ROLE pgwatch2 CONNECTION LIMIT 3;

3. Allow pgwatch2 to read database statistics::

    GRANT pg_read_all_stats TO pgwatch2;

4. If you want to collect data gathered from the ``pg_stat_statements`` extension, it needs to be enabled::

    CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

5. The `pgwatch2 documentation`_ recommends to enable timing of database I/O calls by setting the PostgreSQL configuration parameter ``track_io_timing`` (see :doc:`../reference/list-of-advanced-params`).
    .. warning::  According to the `PostgreSQL documentation`_, setting ``track_io_timing = on`` can cause significant overhead.


Running pgwatch2
----------------

pgwatch2 has multiple `installation options`_ to choose from. For the sake of simplicity, the following example uses `ad-hoc mode`_ with a Docker container::

    docker run --rm -p 3000:3000 -p 8080:8080 \
        -e PW2_ADHOC_CONN_STR='postgres://pgwatch2:password@HOST:PORT/defaultdb?sslmode=require' \
        -e PW2_ADHOC_CONFIG='rds' --name pw2 cybertec/pgwatch2-postgres

This runs pgwatch2 with the container image provided by CYBERTEC. ``PW2_ADHOC_CONN_STR`` is set to the connection string of the PostgreSQL instance to be monitored, copied from the `Aiven web console`_ replacing the username/password have been replaced by the ones specifically created for pgwatch2. Please consult the `pgwatch2 documentation`_ to decide on the best way to set up pgwatch2 in your environment.

.. Note::
    pgwatch2 contains several dashboards that rely on extensions not available in Aiven for PostgreSQL, so it is to be expected that some dashboards are either empty or display error symbols.

.. image:: /images/products/postgresql/pgwatch2.png
   :alt: Screenshot of a pgwatch2 Dashboard

.. _pgwatch2: https://github.com/cybertec-postgresql/pgwatch2
.. _pgwatch2 documentation: https://pgwatch2.readthedocs.io/en/latest/
.. _installation options: https://pgwatch2.readthedocs.io/en/latest/installation_options.html
.. _ad-hoc mode: https://pgwatch2.readthedocs.io/en/latest/installation_options.html#ad-hoc-mode
.. _PostgreSQL documentation: https://www.postgresql.org/docs/current/runtime-config-statistics.html
.. _Aiven web console: https://console.aiven.io/
