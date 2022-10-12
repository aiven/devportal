Use of deprecated TLS versions
==============================

TLS versions ``TLSv1`` and ``TLSv1.1`` are considered insecure, and are no longer supported in Aiven for PostgreSQL® deployments.

Older services (and forks of older services) may still allow connections using these TLS versions. Support for these versions is deprecated and will be removed in the future.

We recommend updating clients, or configuring them to only use ``TLSv1.2`` and above. Please refer to the documentation for your PostgreSQL client(s) on how to accomplish this.

To check the TLS versions clients are connecting with, you can query the ``pg_stat_activity`` table joined with ``pg_stat_ssl``:

.. code::

    SELECT
        datname,
        pid,
        usesysid,
        usename,
        application_name,
        client_addr,
        ssl,
        version,
        cipher,
        backend_start
    FROM
        pg_stat_activity JOIN pg_stat_ssl USING (pid)
    WHERE
        client_addr IS NOT NULL;

.. code::

     datname  │   pid   │ usesysid │ usename  │ application_name │  client_addr   │ ssl │ version │         cipher         │         backend_start         
    ──────────┼─────────┼──────────┼──────────┼──────────────────┼────────────────┼─────┼─────────┼────────────────────────┼───────────────────────────────
    defaultdb │ 2172508 │    16412 │ avnadmin │ psql             │ 192.178.0.1    │ t   │ TLSv1.3 │ TLS_AES_256_GCM_SHA384 │ 2022-09-12 12:39:12.644646+00

Connections logs are also available that contain this information, for example:

.. code::

    [11-1] pid=2460224,user=test-user,db=test-db,app=[unknown],client=192.18.0.1 LOG:  connection authorized: user=test-user database=test-db SSL enabled (protocol=TLSv1.1, cipher=AES256-SHA, bits=256, compression=off)
