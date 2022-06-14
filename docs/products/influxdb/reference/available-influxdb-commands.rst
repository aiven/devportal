Available InfluxDB® commands
############################

InfluxDB® retention policy and continuous query management
----------------------------------------------------------

The default InfluxDB service user ``avnadmin`` in our services is not a full "admin" account (as per InfluxDB terminology), but it has the capability to manipulate retention policies and continuous queries.

Databases still need to be created via the Aiven web console or via the `REST API <https://api.aiven.io/doc/>`_. Also some cluster manipulation commands have been disabled as they could interfere with us being able to provide the best service level possible.

The normal retention policy commands, such as ``CREATE RETENTION POLICY`` and ``ALTER RETENTION POLICY`` can be used modify the retention periods.

Continuous Queries can be managed in the same way with ``CREATE CONTINUOUS QUERY`` and similar commands.

Here are the relevant links to the InfluxDB® documentation: 

* `Retention Policy commands <https://docs.influxdata.com/influxdb/v1.2/query_language/database_management/#create-retention-policies-with-create-retention-policy>`_

* `Continuous Query commands <https://docs.influxdata.com/influxdb/v1.2/query_language/continuous_queries/>`_

Note that if you are using the InfluxDB HTTP API directly, you may need pass the name of the database as an URI argument (for example ``&db=defaultdb``) for some of the management commands to work.