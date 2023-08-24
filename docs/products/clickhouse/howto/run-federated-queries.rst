Run federated queries from Aiven for ClickHouse®
================================================

.. _access-permissions:

Access and permissions
''''''''''''''''''''''

To run a federated query, the ClickHouse service user connecting to the cluster requires grants to the S3 and/or URL sources. The main service user is granted access to the sources by default, and new users can be allowed to use the sources with the following query:

.. code-block:: bash

   GRANT CREATE TEMPORARY TABLE, S3, URL ON *.* TO <username> [WITH GRANT OPTION]


The CREATE TEMPORARY TABLE grant is required for both sources. Adding WITH GRANT OPTION allows the user to further transfer the privileges.

Related reading
---------------

* :doc:`Read and pull data from external S3 with federated queries </docs/products/clickhouse/concepts/federated-queries>`
* `Cloud Compatibility | ClickHouse Docs <https://clickhouse.com/docs/en/whats-new/cloud-compatibility#federated-queries>`_
* `Integrating S3 with ClickHouse <https://clickhouse.com/docs/en/integrations/s3>`_
* `remote, remoteSecure | ClickHouse Docs <https://clickhouse.com/docs/en/sql-reference/table-functions/remote>`_
