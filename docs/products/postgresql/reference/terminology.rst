Terminology for PostgreSQL®
===========================

- **Primary node**: The PostgreSQL® primary node is the main server node that processes SQL queries, makes the necessary changes to the database files on the disk, and returns the results to the client application.
- **Standby node**: PostgreSQL standby nodes (also called replicas) replicate the changes from the primary node and try to maintain an up-to-date copy of the same database files that exists on the primary node.
- **Write-Ahead Log (WAL)**: The WAL is a log file storing all the database transactions in a sequential manner.
- **pglookout**: `pglookout <https://github.com/aiven/pglookout>`_ is a PostgreSQL replication monitoring and failover daemon.
- **PGHoard**: `PGHoard <https://github.com/aiven/pghoard>`_ is a PostgreSQL backup daemon and restore tooling that stores backup data in cloud object stores
