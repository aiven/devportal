Connect PostgreSQL® to Aiven for ClickHouse®
============================================

You can integrate Aiven for ClickHouse® with either *Aiven for PostgreSQL* service located in the same project, or *an external PostgreSQL endpoint*.

Behind the scenes the integration between Aiven for ClickHouse and PostgreSQL relies on `ClickHouse PostgreSQL Engine <https://clickhouse.com/docs/en/engines/table-engines/integrations/postgresql>`_.

.. note::

    Aiven for ClickHouse service integrations are available for Startup plans and higher.

Prerequisites
-------------

To connect Aiven for ClickHouse to PostgreSQL, you need the following:

* Aiven for ClickHouse service
* Aiven for PostgreSQL service or a self-hosted PostgreSQL service

These instructions assume that you have at least one table in your PostgreSQL service.

.. tip::

    If you use the self-hosted PostgreSQL service, an external PostgreSQL endpoint should be configured in **Integration endpoints**.

Variables
-------------

The following variables will be used later in the code snippets:

============================     ==========================================================================================================
Variable                         Description
============================     ==========================================================================================================
``CLICKHOUSE_SERVICE_NAME``      Name of your Aiven for ClickHouse service.
``PG_SERVICE_NAME``              Name of the PostgreSQL service you use for the integration.
``PG_DATABASE``                  Name of PostgreSQL database you're integrating.
``PG_SCHEMA``                    Name of PostgreSQL schema.
``PG_TABLE``                     Name of the PostgreSQL table you use for the integration.
============================     ==========================================================================================================

Create an integration
----------------------

To connect Aiven for ClickHouse and Aiven for PostgreSQL by enabling a data service integration, see :ref:`Create data service integrations <create-data-service-integration>`.

The newly created database name has the following format: ``service_PG_SERVICE_NAME_PG_DATABASE_PG_SCHEMA``, for example, ``service_myPGService_myDatabase_mySchema``.

.. note::

    When connecting to an Aiven for PostgreSQL, we connect as the main service user of that service, which has access to all the PostgreSQL tables. SELECT and INSERT privileges are granted to the main service user (``avnadmin``). It is up to the main service user to grant access to other users. Read more :doc:`how to grant privileges </docs/products/clickhouse/howto/manage-users-roles>`.

Update PostgreSQL integration settings
-----------------------------------------

When connecting to a PostgreSQL service, ClickHouse needs to know the name of the PostgreSQL schema and database you want to access. By default these settings are set to the ``public`` schema in the ``defaultdb``. However, you can update these values by following next steps.

.. note::

    Currently the configurations can be set only with the help of CLI command :ref:`avn service integration-update <avn service integration-update>`.


1. Get *the service integration id* by requesting the full list of integrations. Replace ``CLICKHOUSE_SERVICE_NAME`` and ``PG_SERVICE_NAME`` with the names of your services:

.. code::

    avn service integration-list --project PROJECT_NAME CLICKHOUSE_SERVICE_NAME | grep PG_SERVICE_NAME

1. Update the configuration settings using the service integration id retrieved in the previous step and your integration settings. Replace ``SERVICE_INTEGRATION_ID``, ``PG_DATABASE`` and ``PG_SCHEMA`` with your values, you can add more than one combination of database/schema in the object ``databases``:

.. code::

    avn service integration-update --project PROJECT_NAME SERVICE_INTEGRATION_ID \
    --user-config-json '{
        "databases":[{"database":"PG_DATABASE","schema":"PG_SCHEMA"}]
    }'


Read and store data
-------------------
In Aiven for ClickHouse you can read data by running SELECT command. Replace ``PG_SERVICE_NAME``, ``PG_DATABASE``, ``PG_SCHEMA`` and ``PG_TABLE`` with your values and run:

.. code:: sql

    SELECT * FROM service_PG_SERVICE_NAME_PG_DATABASE_PG_SCHEMA.PG_TABLE

.. note::

    ClickHouse is strict about allowed symbols in database and table names. You can use backticks around the names when running ClickHouse requests, particularly in the cases when the name contains dashes. For example, ``SELECT * FROM `service_your-kafka-service`.table``.

Write data to PostgreSQL table
-------------------------------

You can also insert rows from the ClickHouse table into the PostgreSQL table. Replace ``PG_SERVICE_NAME``, ``PG_DATABASE``, ``PG_SCHEMA`` and ``PG_TABLE`` with your values:

.. code:: sql

    INSERT INTO service_PG_SERVICE_NAME_PG_DATABASE_PG_SCHEMA.PG_TABLE(id, name)
    VALUES (1, 'Michelangelo')


