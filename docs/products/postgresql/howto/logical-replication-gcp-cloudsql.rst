Enable logical replication on Google Cloud SQL
================================================

If you have not enabled logical replication on Cloud SQL PostgreSQL® already, the following instructions shows how to set the ``cloudsql.logical_decoding`` parameter to ``On``.

1. Set logical replication parameter for your Cloud SQL PostgreSQL® database.

    .. image:: /images/products/postgresql/migrate-cloudsql-flags.png
        :alt: Cloud SQL PostgreSQL flags

2. Authorize Aiven PostgresSQL IP to Cloud SQL's allowed network CIDR.

    .. image:: /images/products/postgresql/migrate-cloudsql-network.png
        :alt: Cloud SQL PostgreSQL network

3. Set replication role to PostgreSQL user (or the user will be used for migration) in Cloud SQL PostgreSQL::

    ALTER ROLE postgres REPLICATION;