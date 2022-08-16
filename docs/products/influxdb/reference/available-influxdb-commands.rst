Available InfluxDB® commands
############################

InfluxDB® retention policy and task management
----------------------------------------------

The default InfluxDB service user ``avnadmin`` in our services is not a full "admin" account (as per InfluxDB terminology), but it has the capability to manipulate retention policies and tasks (previously: continuous queries).

Databases still need to be created via the Aiven web console or via the `REST API <https://api.aiven.io/doc/>`_. Also some cluster manipulation commands have been disabled as they could interfere with us being able to provide the best service level possible.

The normal retention policy commands, such as ``CREATE RETENTION POLICY`` and ``ALTER RETENTION POLICY`` can be used to modify the retention periods.


Relevant links to the InfluxDB® documentation: 

* `Retention policy commands <https://docs.influxdata.com/influxdb/v1.8/concepts/glossary/#retention-policy-rp>`_
* `Tasks <https://docs.influxdata.com/influxdb/cloud/process-data/get-started/>`_

Note that if you are using the InfluxDB HTTP API directly, you may need pass the name of the database as an URI argument (for example ``&db=defaultdb``) for some of the management commands to work.