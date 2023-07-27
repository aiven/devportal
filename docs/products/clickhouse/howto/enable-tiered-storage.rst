Enable tiered storage in Aiven for ClickHouse®
==============================================

.. important::

Aiven for ClickHouse® tiered storage is a limited availability feature. If you're interested in trying out this feature, contact the sales team at `sales@Aiven.io <mailto:sales@Aiven.io>`_.

Learn how to enable the tiered storage feature on your Aiven for ClickHouse® service and activate it for specific tables.
To check what the tiered storage is, how it works, and why use it, see :doc:`Tiered storage in Aiven for ClickHouse® </docs/products/clickhouse/concepts/clickhouse-tiered-storage>`.

About enabling tiered storage
-----------------------------

You can enable the tiered storage feature in Aiven for ClickHouse either for a new service or for an existing one.
To enable the feature, you need to activate it on a service level in Aiven Console and, next, set it up on a table level, which is done using SQL (via CLI, for example).

Limitations
'''''''''''

See :ref:`tiered storage limitations <tiered-storage-limitations>` for restrictions that apply to the feature for Aiven for ClickHouse.

Tools
'''''

To enable the tiered storage, you need to use the following:

* `Aiven Console <https://console.aiven.io/>`_
* SQL and an SQL client (for example, ClickHouse CLI client)

Prerequisites
-------------

* Aiven account
* Access to the `Aiven Console <https://console.aiven.io/>`_
* Command line tool (:doc:`ClickHouse client </docs/products/clickhouse/howto/connect-with-clickhouse-cli>`)
* All maintenance updates applied (check in the **Overview** tab of your service in Aiven Console)

Enable tiered storage on a service
----------------------------------

Using the `Aiven Console <https://console.aiven.io/>`_, you can enable the tiered storage both on new and existing services.

New service
'''''''''''

You can enable the tiered storage on your new service while creating this service. For a general information on how to add a new service using Aiven Console, see :doc:`Create a new service </docs/platform/howto/create_new_service>`. One additional step you need to take to enable the tiered storage in the **Create new service** view of Aiven Console is selecting the **Enable Tiered Storage** toggle before you move on to selecting a cloud provider.

Existing service
''''''''''''''''

To enable the tiered storage on your existing service, log in to `Aiven Console <https://console.aiven.io/>`_, navigate to the **Overview** tab of your service, and select **Enable Tiered Storage** at the top of the page.

.. topic:: Result
   
   Your service has the tiered storage feature enabled, which is visible in the **Overview** tab as the **Tiered Storage** section added just below the **Connection information** area.

Enable tiered storage on a table
--------------------------------

When you have the tiered storage feature enabled on your service, you can move on to enabling it on your tables, both new and existing ones.

1. :doc:`Connect to your Aiven for ClickHouse service </docs/products/clickhouse/howto/list-connect-to-service>` using, for example, the ClickHouse client (CLI).

2. To activate the tiered storage feature on a specific table, set ``storage_policy`` to ``tiered`` on this table by executing the following SQL statement:

   .. code-block:: bash

      ALTER TABLE database-name.table-name SET storage_policy=”tiered”

.. topic:: Result
   
   The tiered storage is enabled on your table and data in this table is now distributed between two tiers: SSD and object storage.

What's next
-----------

* :doc:`Configure data retention thresholds for tiered storage </docs/products/clickhouse/howto/configure-tiered-storage>`
* :doc:`Check data volume distribution between different disks </docs/products/clickhouse/howto/check-data-tiered-storage>`

Related reading
---------------

* :doc:`About tiered storage in Aiven for ClickHouse </docs/products/clickhouse/concepts/clickhouse-tiered-storage>`
* :doc:`Transfer data between SSD and object storage </docs/products/clickhouse/howto/transfer-data-tiered-storage>`
