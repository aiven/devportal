InfluxDB® retention policies
############################

InfluxDB® enforces what are known as "Retention Policies" to automatically manage the lifetime of data points in measurements.

The duration of the default retention policy in Aiven for InfluxDB® data points is 720 hours, i.e. 30 days. Any data points older than this (compared to current time) will be automatically removed. The user can change the retention period (say, 90 days) as per their requirement, and it will stick to the modified configuration even after a restart, migration, plan upgrade/downgrade, etc.

Retention policies can be managed using the InfluxDB query language commands ``SHOW RETENTION POLICIES``, ``CREATE RETENTION POLICY``, ``ALTER RETENTION POLICY`` and ``DROP RETENTION POLICY``. You can find more about this commands in the `InfluxDB documentation <https://docs.influxdata.com/influxdb/v1.2/query_language/database_management/#create-retention-policies-with-create-retention-policy>`_.
