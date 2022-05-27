Enable logical replication on Amazon Aurora PostgreSQL®
=========================================================

If you have not enabled logical replication on Aurora already, the following instructions shows how to set the ``rds.logical_replication`` parameter to ``1`` (true) in the parameter group.

1. Create a DB Cluster parameter group for your Aurora database.

    .. image:: /images/products/postgresql/migrate-aurora-pg-parameter-group.png
        :alt: Aurora PostgreSQL cluster parameter group

2. Set the ``rds.logical_replication`` parameter to ``1`` (true) in the parameter group.

    .. image:: /images/products/postgresql/migrate-aurora-pg-parameter-value.png
        :alt: Aurora PostgreSQL cluster parameter value

3. Modify Database options to use the new DB Cluster parameter group - ``RDS`` -> ``Databases`` -> ``Modify``.

    .. image:: /images/products/postgresql/migrate-aurora-pg-parameter-modify.png
        :alt: Aurora PostgreSQL cluster parameter modify

.. Warning::
    Apply immediately or reboot is required to see configuration change reflected to ``wal_level``.