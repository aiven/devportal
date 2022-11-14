Continuous queries
==================

Continuous queries run automatically and periodically on real-time data and store query results in a specified measurement.
You can manage continuous queries using ``CREATE CONTINUOUS QUERY`` and similar commands.

For more information on Continuous Query commands, see `InfluxQL Continuous Queries <https://docs.influxdata.com/enterprise_influxdb/v1.10/query_language/continuous_queries/>`_. 

.. note:: If you are using the InfluxDB HTTP API directly, you may need to pass the name of the database as a URI argument, for example, ``&db=defaultdb``, for some of the management commands to work.