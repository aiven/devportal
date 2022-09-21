Monitor query performance with Datadog
======================================

`Datadog Deep Database Monitoring <https://www.datadoghq.com/product/database-monitoring/>`_ enables you to track and visualize query metrics and explain plans of Aiven for PostgreSQL® services.

Slow-running database queries are often the cause of incidents and database performance problems. With insights into the query performance and explains plans from your databases in a single place, DataDog Database monitoring allows you to identify these slow queries in real-time and take action to improve the database performance. 

For more information, see `Datadog Deep Database Monitoring <https://www.datadoghq.com/product/database-monitoring/>`_ product page.

Prerequisites
-------------
To use Datadog Database Monitoring with your Aiven for PostgreSQL® services, you must perform the following steps: 

* Apply any outstanding maintenance updates mentioning the Datadog integration. 
* Ensure the :doc:`Datadog Metrics integration </docs/integrations/datadog/datadog-metrics>` is enabled. 
* The :doc:`PostgreSQL extensions <../reference/list-of-extensions>` - ``pg_stat_statements`` and ``aiven_extras``, must be enabled by executing the following `CREATE EXTENSION <https://www.postgresql.org/docs/current/sql-createextension.html>`_ SQL commands directly on the Aiven for PostgreSQL® database service.
::

    CREATE EXTENSION pg_stat_statements;
::
    
    CREATE EXTENSION aiven_extras;

Enable monitoring of DataDog Metrics integration
------------------------------------------------
To enable the DataDog Database Monitoring for your Aiven for PostgreSQL® integration with Datadog Metrics, you must enable the ``datadog_dbm_enabled`` configuration parameter for each Datadog metric. 

Using the :doc:`Aiven CLI </docs/tools/cli>`, you can fetch the DataDog metric integration you want to monitor and enable it using the ``datadog_dbm_enabled`` configuration parameter. For example: 

* Find the UUID of the Datadog Metrics integration for a particular service: 
::
    
    avn service integration-list --project <project name> <service name>

* Enable the Datadog Database Monitoring for the Datadog Metrics integration using:
::
    
    avn service integration-update --user-config '{"datadog_dbm_enabled": true}' <integration uuid>



