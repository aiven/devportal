Terminology for PostgreSQL®
===========================

.. _Terminology PGPrimary:

Primary node
    The PostgreSQL® primary node is the main server node that processes SQL queries, makes the necessary changes to the database files on the disk, and returns the results to the client application.

.. _Terminology PGStandby:

Standby node
    PostgreSQL standby nodes (also called replicas) replicate the changes from the primary node and try to maintain an up-to-date copy of the same database files that exists on the primary node.

.. _Terminology PGWAL:

Write-Ahead Log (WAL)
    The WAL is a log file storing all the database transactions in a sequential manner.

.. _Terminology PGLookout:

PGLookout
    `PGLookout <https://github.com/aiven/pglookout>`_ is a PostgreSQL replication monitoring and failover daemon.

.. _Terminology PGHoard:

PGHoard
    `PGHoard <https://github.com/aiven/pghoard>`_ is a PostgreSQL backup daemon and restore tooling that stores backup data in cloud object stores
