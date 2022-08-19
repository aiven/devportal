Integrate with Apache Kafka®
=============================

You can integrate Aiven for ClickHouse® with either *Aiven for Apache Kafka* service located in the same project, or *an external Apache Kafka endpoint*. A single Aiven for ClickHouse instance can connect to multiple Kafka clusters with different authentication mechanism and credentials.

Behind the scenes the integration between Aiven for ClickHouse and Apache Kafka services relies on `ClickHouse Kafka Engine <https://clickhouse.com/docs/en/engines/table-engines/integrations/kafka/>`_.

.. note::

    ClickHouse service integrations are available for Startup plans and higher.

Prerequisites
-------------

You will need:

* Aiven for ClickHouse service
* Aiven for Apache Kafka service or a self-hosted Apache Kafka service
* If you use the self-hosted Apache Kafka service, an external Apache Kafka endpoint should be configured in **Service Integrations**
* At least one topic in the Apache Kafka service

Variables
-------------

The following variables will be used later in the code snippets:

============================     ==========================================================================================================
Variable                         Description
============================     ==========================================================================================================
``CLICKHOUSE_SERVICE_NAME``      Name of your Aiven for ClickHouse service.
``KAFKA_SERVICE_NAME``           Name of the Apache Kafka service you use for the integration.
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
#. Select Apache Kafka from the list of the options.
#. Choose your service from the list. This is also a place where you can trigger creation of a new Aiven for Apache Kafka service.
#. Click on **Enable**.
#. Your Apache Kafka service will be added to the list of enabled service integrations.
#. You can now close *Service integrations* modal window.
#. The Kafka integration database will now be added.

The newly created database name has the following format: `service_KAFKA_SERVICE_NAME`, where KAFKA_SERVICE_NAME is the name of your Apache Kafka service.

.. note::

    During this step we only created an empty database in ClickHouse, but we didn't create any tables yet. Creation of the virtual connector table is done by setting specific integration configuration, see the section below.


Update Apache Kafka integration settings
-----------------------------------------

Next step is to configure the topic and data format options for the integration. This will create a virtual table in ClickHouse that can receive and send messages from multiple topics. You can have as many of such tables as you need. You need to define for each table following:


* ``name`` - name of the connector table
* ``columns`` - array of columns, with names and types
* ``topics`` - array of topics, where you want to bring the data from
* ``data_format`` - your preferred format for data input, see :doc:`../reference/supported-input-output-formats`
* ``group_name`` - consumer group name, that will be created on your behalf

Integration settings in a JSON format:

.. code:: json

    {
        "tables": [
            {
                "name": "CONNECTOR_TABLE_NAME",
                "columns": [
                    {"name": "id", "type": "UInt64"},
                    {"name": "name", "type": "String"}
                ],
                "topics": [{"name": "topic1"}, {"name": "topic2"}],
                "data_format": "DATA_FORMAT",
                "group_name": "CONSUMER_NAME"
            }
        ]
    }

Configure integration with CLI
--------------------------------

Currently the configurations can be set only with the help of CLI command :ref:`avn service integration-update <avn service integration-update>`

Follow these instructions:

1. Get *the service integration id* by requesting the full list of integrations. Replace ``PROJECT``, ``CLICKHOUSE_SERVICE_NAME`` and ``KAFKA_SERVICE_NAME`` with the names of your services:

.. code::

    avn service integration-list                        \
    --project PROJECT                                   \
    CLICKHOUSE_SERVICE_NAME | grep KAFKA_SERVICE_NAME

2. Update the configuration settings using the service integration id retrieved in the previous step and your integration settings. Replace ``SERVICE_INTEGRATION_ID``, ``CONNECTOR_TABLE_NAME``, ``DATA_FORMAT`` and ``CONSUMER_NAME`` with your values:

.. code::

    avn service integration-update SERVICE_INTEGRATION_ID \
    --project PROJECT                                     \
    --user-config-json '{
        "tables": [
            {
                "name": "CONNECTOR_TABLE_NAME",
                "columns": [
                    {"name": "id", "type": "UInt64"},
                    {"name": "name", "type": "String"}
                ],
                "topics": [{"name": "topic1"}, {"name": "topic2"}],
                "data_format": "DATA_FORMAT",
                "group_name": "CONSUMER_NAME"
            }
        ]
    }'


Read and store data
-------------------
In Aiven for ClickHouse you can consume messages by running SELECT command. Replace ``KAFKA_SERVICE_NAME`` and ``CONNECTOR_TABLE_NAME`` with your values and run:

.. code:: sql

    SELECT * FROM service_KAFKA_SERVICE_NAME.CONNECTOR_TABLE_NAME

However, the messages are only read once (per consumer group). If you want to store the messages for later, you can send them into a separate ClickHouse table with the help of a materialized view.

For example, run to creating a destination table:

.. code:: sql

    CREATE TABLE destination (id UInt64, name String)
    ENGINE = ReplicatedMergeTree()
    ORDER BY id;

Add a materialised view to bring the data from the connector:

.. code:: sql

    CREATE MATERIALIZED VIEW materialised_view TO destination AS
    SELECT *
    FROM service_KAFKA_SERVICE_NAME.CONNECTOR_TABLE_NAME;


Now the messages consumed from the Apache Kafka topic will be read automatically and sent into the destination table directly.


.. note::

    ClickHouse is strict about allowed symbols in database and table names. You can use backticks around the names when running ClickHouse requests, particularly in the cases when the name contains dashes.


Write data back to the topic
----------------------------

You can also bring the entries from ClickHouse table into the Apache Kafka topic. Replace ``KAFKA_SERVICE_NAME`` and ``CONNECTOR_TABLE_NAME`` with your values:

.. code:: sql

    INSERT INTO service_KAFKA_SERVICE_NAME.CONNECTOR_TABLE_NAME(id, name)
    VALUES (1, 'Michelangelo')

.. warning::

    Writing to more than one topic is not supported.
