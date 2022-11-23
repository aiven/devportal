InfluxDB® retention policies
============================

InfluxDB® enforces what is known as **Retention policies** to automatically manage the lifetime of data points in measurements.

The duration of the default retention policy in Aiven for InfluxDB® data points is 720 hours, i.e., 30 days. Any data points older than this (compared to the current time) will be automatically removed. You can change the retention period, say, 90 days, as per your requirement, and it will adhere to the modified configuration even after a restart, migration, or plan upgrade/downgrade. 

.. note:: 
    The default InfluxDB service user ``avnadmin`` in Aiven services is not a full **admin** account (as per InfluxDB terminology), but it has the capability to manipulate retention policies and continuous queries.

.. note:: While you can create databases via the `Aiven Console <https://console.aiven.io/>`_ or the `REST API <https://api.aiven.io/doc/>`_, some cluster manipulation commands have been disabled as they could interfere with Aiven being able to provide the best service level possible.

You can manage retention policies using the InfluxDB query language commands: 

* ``SHOW RETENTION POLICIES``
* ``CREATE RETENTION POLICY``
* ``ALTER RETENTION POLICY`` 
* ``DROP RETENTION POLICY``

You can find more about these commands in the `InfluxDB documentation <https://docs.influxdata.com/enterprise_influxdb/v1.10/query_language/manage-database/#retention-policy-management>`_.

.. note:: If you are using the InfluxDB HTTP API directly, you may need to pass the name of the database as a URI argument, for example, ``&db=defaultdb``, for some of the management commands to work.