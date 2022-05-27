Enable logical replication on Amazon RDS PostgreSQL®
======================================================

If you have not enabled logical replication on RDS already, the following instructions shows how to set the ``rds.logical_replication`` parameter to ``1`` (true) in the parameter group.

1. Create a parameter group for your RDS database.

    .. image:: /images/products/postgresql/migrate-rds-pg-parameter-group.png
        :alt: RDS PostgreSQL parameter group

2. Set the ``rds.logical_replication`` parameter to ``1`` (true) in the parameter group

    .. image:: /images/products/postgresql/migrate-rds-pg-parameter-value.png
        :alt: RDS PostgreSQL parameter value

3. Modify Database options to use the new DB parameter group - ``RDS`` -> ``Databases`` -> ``Modify``

    .. image:: /images/products/postgresql/migrate-rds-pg-parameter-modify.png
        :alt: RDS PostgreSQL parameter modify

.. Warning::
    Apply immediately or reboot is required to see configuration change reflected to ``wal_level``