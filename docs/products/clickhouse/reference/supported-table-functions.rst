Table functions supported in Aiven for ClickHouse®
==================================================

`Table functions <https://clickhouse.com/docs/en/sql-reference/table-functions>`_ can be used to construct tables, for example, in a FROM clause of a query or in an INSERT INTO TABLE FUNCTION statement.

.. topic:: Sample usage of the S3 table function

   .. code-block:: bash

      SELECT *
      FROM deltaLake('s3://bucket/path/to/lake')

.. note::

   Occasionally, you may find specific table functions disabled for security reasons.

Aiven for ClickHouse® supports the following table functions:

* ``cluster``
* ``clusterAllReplicas``
* ``cosn``
* ``deltaLake``
* ``format``
* ``gcs``
* ``generateRandom``
* ``hudi``
* ``iceberg``
* ``input``
* ``merge``
* ``mysql``
* ``null``
* ``numbers``
* ``numbers_mt``
* ``oss``
* ``postgresql``
* ``remoteSecure``
* ``s3``
* ``s3Cluster``
* ``url``
* ``values``
* ``view``
* ``viewExplain``
* ``viewIfPermitted``
* ``zeros``
* ``zeros_mt``
