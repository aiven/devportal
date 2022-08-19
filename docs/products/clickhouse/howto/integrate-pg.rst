Integrate with PostgreSQL®
=============================

You can integrate Aiven for ClickHouse® with either *Aiven for PostgreSQL* service located in the same project, or *an external PostgreSQL endpoint*.

Behind the scenes the integration between Aiven for ClickHouse and Apache Kafka services relies on `ClickHouse PostgreSQL Engine <https://clickhouse.com/docs/en/engines/table-engines/integrations/postgresql>`_.

.. note::

    ClickHouse service integrations are available for Startup plans and higher.

Prerequisites
-------------

You will need:

* Aiven for ClickHouse service
* Aiven for PostgreSQL service or a self-hosted PostgreSQL service
* If you use the self-hosted PostgreSQL service, an external PostgreSQL endpoint should be configured in **Service Integrations**
* These instructions assume that you have at least one table in your PostgreSQL service

Variables
-------------

The following variables will be used later in the code snippets:

============================     ==========================================================================================================
Variable                         Description
============================     ==========================================================================================================
``CLICKHOUSE_SERVICE_NAME``      Name of your Aiven for ClickHouse service.
``PG_SERVICE_NAME``              Name of the Apache Kafka service you use for the integration.
``PROJECT``                      Name of Aiven project where your services are located.
``CONNECTOR_TABLE_NAME``         Name of the Kafka engine virtual table that is used as a connector.
``DATA_FORMAT``                  Input/output data format in which data is accepted into ClickHouse. See :doc:`../reference/supported-input-output-formats`
``CONSUMER_GROUP_NAME``          Name of the consumer group. Each message is delivered once per consumer group.
============================     ==========================================================================================================

Create an integration
----------------------

You can create an integration with the help of :ref:`Aiven CLI <avn_service_integration_create>`, or through the `Aiven console <https://console.aiven.io/>`_ by following these steps:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_, choose the right project, and select your Aiven for ClickHouse service.
#. In the *Overview* tab, scroll till the section *Service integrations* and click on **Set up integration**. A modal window with available integration options will appear.
#. Select PostgreSQL from the list of the options.
#. Choose your service from the list. This is also a place where you can trigger creation of a new Aiven for PostgreSQL service.
#. Click on **Enable**.
#. Your PostgreSQL service will be added to the list of enabled service integrations.
#. You can now close *Service integrations* modal window.
#. The PostgreSQL integration database will now be added.

The newly created database name has the following format: ``service_PG_SERVICE_NAME_PG_DATABASE_PG_SCHEMA`` (for example, ``service_myPGService_myDatabase_mySchema``), where PG_SERVICE_NAME is the name of your PostgreSQL service.

.. note::

    When connecting to an Aiven for PostgreSQL, we connect as the main service user of that service, which has access to all the PostgreSQL tables. SELECT and INSERT privileges are granted to the main service user. It is up to the main service user to grant access to other users.


Update PostgreSQL integration settings
-----------------------------------------

When connecting to a PostgreSQL service, ClickHouse needs to know the name of the PostgreSQL schema and database you want to access. By default these settings are set to the public schema in the ``defaultdb``. However, you can update these values by following next steps.

.. note::

    Currently the configurations can be set only with the help of CLI command :ref:`avn service integration-update <avn service integration-update>`.


1. Get *the service integration id* by requesting the full list of integrations. Replace ``CLICKHOUSE_SERVICE_NAME`` and ``PG_SERVICE_NAME`` with the names of your services:

.. code::

    avn service integration-list CLICKHOUSE_SERVICE_NAME | grep PG_SERVICE_NAME

2. Update the configuration settings using the service integration id retrieved in the previous step and your integration settings. Replace ``SERVICE_INTEGRATION_ID``, ``PG_DATABASE`` and ``PG_SCHEMA`` with your values:

.. code::

    avn service integration-update SERVICE_INTEGRATION_ID \
    --user-config-json '{
        "databases":[{"database":"PG_DATABASE","schema":"PG_SCHEMA"}]
    }'


Read and store data
-------------------
In Aiven for ClickHouse you can read data by running SELECT command. Replace ``PG_SERVICE_NAME``, ``PG_DATABASE``, ``PG_SCHEMA`` and ``PG_TABLE`` with your values and run:

.. code:: sql

    SELECT * FROM service_PG_SERVICE_NAME_PG_DATABASE_PG_SCHEMA.PG_TABLE

If you want to copy the messages into a separate Clickhouse table, you can a materialized view.

For example, create a destination table in ClickHouse:

.. code:: sql

    CREATE TABLE destination (id UInt64, name String)
    ENGINE = ReplicatedMergeTree()
    ORDER BY id;

Add use a materialised view to bring the data from the connector:

.. code:: sql

    CREATE MATERIALIZED VIEW materialised_view TO destination AS
    SELECT *
    FROM service_PG_SERVICE_NAME_PG_DATABASE_PG_SCHEMA.PG_TABLE;


Now the new entries added into PostgreSQL table will be automatically sent into the destination table.


Write data to PostgreSQL table
-------------------------------

You can also bring the entries from ClickHouse table into the PostgreSQL table. Replace ``PG_SERVICE_NAME``, ``PG_DATABASE``, ``PG_SCHEMA`` and ``PG_TABLE`` with your values:

.. code:: sql

    INSERT INTO service_PG_SERVICE_NAME_PG_DATABASE_PG_SCHEMA.PG_TABLE(id, name)
    VALUES (1, 'Michelangelo')


