Database monitoring with Datadog
======================================

`Database Monitoring with Datadog <https://www.datadoghq.com/product/database-monitoring/>`_ enables you to capture key metrics on the Datadog platform for any Aiven for PostgreSQL® service with :doc:`Datadog Metrics </docs/integrations/datadog/datadog-metrics>` integration.

Datadog Database Monitoring allows you to view query metrics and explain plans in a single place, with the ability to drill into precise execution details, along with query and host metrics correlation.

Prerequisites
-------------
To use Datadog Database Monitoring with your Aiven for PostgreSQL® services, you must perform the following steps: 

* Apply any outstanding maintenance updates mentioning the Datadog integration. 
* Ensure the :doc:`Datadog Metrics integration </docs/integrations/datadog/datadog-metrics>` is enabled. 
* The :doc:`PostgreSQL extensions <../reference/list-of-extensions>` - ``pg_stat_statements`` and ``aiven_extras``, must be enabled by executing the following `CREATE EXTENSION <https://www.postgresql.org/docs/current/sql-createextension.html>`_ SQL commands directly on the Aiven for PostgreSQL® database service.
::

    CREATE EXTENSION pg_stat_statements;   
    CREATE EXTENSION aiven_extras;

Enable monitoring 
-----------------

You can individually enable Datadog Database Monitoring for the specific :doc:`Datadog Metrics </docs/integrations/datadog/datadog-metrics>` integration for Aiven for PostgreSQL®, by configuring the ``datadog_dbm_enabled`` parameter. Repeat this action for every Datadog Metrics integration for Aiven for PostgreSQL®, which you plan to monitor.

Using the ``avn service integration-list`` :ref:`Aiven CLI command <avn_service_integration_list>`, you can obtain the Datadog Metric integration you want to monitor and enable the Datadog Database monitoring functionality by using the ``datadog_dbm_enabled`` configuration parameter. For example: 

* Find the UUID of the Datadog Metrics integration for a particular service: 
::

    avn service integration-list --project <project name> <service name>

* Enable the Datadog Database Monitoring for the Datadog Metrics integration with the following command, substituting the ``<INTEGRATION_UUID>`` with the integration UUID retrieved at the previous step:
::

    avn service integration-update --user-config '{"datadog_dbm_enabled": true}' <INTEGRATION_UUID>

.. seealso:: 
    -  Learn more about :doc:`Datadog and Aiven </docs/integrations/datadog>`.
    - Learn more about `Datadog Deep Database Monitoring <https://www.datadoghq.com/product/database-monitoring/>`_ from their product page. 

