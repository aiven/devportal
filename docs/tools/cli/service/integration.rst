Command reference: ``avn service integration``
==============================================

Here you’ll find the full list of commands for ``avn service integration``.


Manage Aiven internal and external integrations
--------------------------------------------------------

``avn service integration-create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Creates a new service integration.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--integration-type``
    - The type of integration (check :ref:`the command details<avn service integration types>` for more details)
  * - ``--source-service``
    - The integration source service
  * - ``--dest-service``
    - The integration destination service
  * - ``--source-endpoint-id``
    - The integration source endpoint ID
  * - ``--dest-endpoint-id``
    - The integration destination endpoint ID
  * - ``--user-config-json`` 
    - The integration parameters as JSON string or path to file (preceded by ``@``)
  * - ``-c KEY=VALUE``
    - The custom configuration settings. 

.. Note::

  Both the ``--user-config-json`` and ``-c`` flags provide a way to customise the service integration using different methods. Only one of the flag is allowed per command. When using both in the same command, an error will be shown
  ::

    ERROR	command failed: UserError: -c (user config) and --user-config-json parameters can not be used at the same time

**Example:** Create a new ``kafka_logs`` service integration to send the logs of the service named ``demo-pg`` to an Aiven for Kafka service named ``demo-kafka`` in the topic ``test_log``.

::

  avn service integration-create            \
    --integration-type kafka_logs           \
    --source-service demo-pg                \
    --dest-service demo-kafka               \
    -c 'kafka_topic=test_log'

``avn service integration-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Deletes a service integration.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``integration-id``
    - The ID of the integration to delete

**Example:** Delete the integration with id ``8e752fa9-a0c1-4332-892b-f1757390d53f``.

::

    avn service integration-delete 8e752fa9-a0c1-4332-892b-f1757390d53f

``avn service integration-endpoint-create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Creates an external service integration endpoint. 

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``--endpoint-name``
    - The name of the endpoint
  * - ``--endpoint-type``
    - The type of endpoint (check :ref:`the command details<avn service integration endpoint types>` for more details)
  * - ``--user-config-json``
    - The endpoint configuration in JSON format or as path to a file (preceded by ``@``)
  * - ``-c KEY=VALUE``
    - The custom configuration settings. 

**Example:** Create an external Apache Kafka endpoint named ``demo-ext-kafka``.

::

    avn service integration-endpoint-create --endpoint-name demo-ext-kafka \
        --endpoint-type external_kafka  \
        --user-config-json  '{"bootstrap_servers":"servertest:123","security_protocol":"PLAINTEXT"}'


``avn service integration-endpoint-delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Deletes a service integration endpoint.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``endpoint-id``
    - The ID of the endpoint to delete

**Example:** Delete the endpoint with ID ``97590813-4a58-4c0c-91fd-eef0f074873b``.

::

    avn service integration-endpoint-delete 97590813-4a58-4c0c-91fd-eef0f074873b


``avn service integration-endpoint-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Lists all service integration endpoints available in a selected project.

**Example:** Lists all service integration endpoints available in the selected project.

::

    avn service integration-endpoint-list

An example of ``avn service integration-endpoint-list`` output:

.. code:: text

    ENDPOINT_ID                           ENDPOINT_NAME     ENDPOINT_TYPE
    ====================================  ================  ==============
    97590813-4a58-4c0c-91fd-eef0f074873b  datadog instance  datadog
    821e0144-1503-42db-aa9f-b4aa34c4af6b  demo-ext-kafka    external_kafka


.. _avn service integration endpoint types:

``avn service integration-endpoint-types-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Lists all available integration endpoint types for given project.

**Example:** Lists all service integration endpoint types available in the selected project.

::

    avn service integration-endpoint-types-list

An example of ``account service integration-endpoint-types-list`` output:

.. code:: text

    TITLE                                        ENDPOINT_TYPE                    SERVICE_TYPES
    ===========================================  ===============================  =====================================================================================================================================================================================================================
    Send service metrics to Datadog              datadog                          cassandra, elasticsearch, kafka, kafka_connect, kafka_mirrormaker, mysql, pg, redis
    Send service logs to AWS CloudWatch          external_aws_cloudwatch_logs     alerta, alertmanager, cassandra, clickhouse, elasticsearch, flink, grafana, influxdb, kafka, kafka_connect, kafka_mirrormaker, m3aggregator, m3coordinator, m3db, mysql, opensearch, pg, redis, sw
    Send service metrics to AWS CloudWatch       external_aws_cloudwatch_metrics  cassandra, elasticsearch, kafka, kafka_connect, kafka_mirrormaker, mysql, pg, redis
    Send service logs to external Elasticsearch  external_elasticsearch_logs      alerta, alertmanager, cassandra, clickhouse, elasticsearch, flink, grafana, influxdb, kafka, kafka_connect, kafka_mirrormaker, m3aggregator, m3coordinator, m3db, mysql, opensearch, pg, redis, sw
    Send service logs to Google Cloud Logging    external_google_cloud_logging    alerta, alertmanager, cassandra, clickhouse, elasticsearch, flink, grafana, influxdb, kafka, kafka_connect, kafka_mirrormaker, m3aggregator, m3coordinator, m3db, mysql, opensearch, pg, redis, sw
    Integrate external Kafka cluster             external_kafka                   alerta, alertmanager, cassandra, clickhouse, elasticsearch, flink, grafana, influxdb, kafka, kafka_connect, kafka_mirrormaker, kafka_mirrormaker, m3aggregator, m3coordinator, m3db, mysql, opensearch, pg, redis, sw
    Integrate external Schema Registry           external_schema_registry         kafka
    Access JMX metrics via Jolokia               jolokia                          kafka, kafka_connect, kafka_mirrormaker
    Send service metrics to Prometheus           prometheus                       cassandra, elasticsearch, kafka, kafka_connect, kafka_mirrormaker, mysql, pg, redis
    Send service logs to remote syslog           rsyslog                          alerta, alertmanager, cassandra, clickhouse, elasticsearch, flink, grafana, influxdb, kafka, kafka_connect, kafka_mirrormaker, m3aggregator, m3coordinator, m3db, mysql, opensearch, pg, redis, sw
    Send service metrics to SignalFX             signalfx                         kafka

``avn service integration-endpoint-update``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Updates a service integration endpoint.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``endpoint-id``
    - The ID of the endpoint
  * - ``--user-config-json``
    - The endpoint configuration in JSON format or as path to a file (preceded by ``@``)
  * - ``-c KEY=VALUE``
    - The custom configuration settings. 

**Example:** Update an external Apache Kafka endpoint with id ``821e0144-1503-42db-aa9f-b4aa34c4af6b``.

::

    avn service integration-endpoint-update 821e0144-1503-42db-aa9f-b4aa34c4af6b \
        --user-config-json  '{"bootstrap_servers":"servertestABC:123","security_protocol":"PLAINTEXT"}'

``avn service integration-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Lists the integrations defined for a selected service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  
**Example:** List all integrations for the service named ``demo-pg``.

::

    avn service integration-list demo-pg

An example of ``account service integration-list`` output:

.. code:: text

    SERVICE_INTEGRATION_ID                SOURCE        DEST        INTEGRATION_TYPE  ENABLED  ACTIVE  DESCRIPTION
    ====================================  ============  ==========  ================  =======  ======  ============================================================
    0e431dab-175a-4029-b417-d74a6437af1a  demo-grafana  demo-pg     dashboard         true     true    Provide a datasource for Grafana service
    (integration not enabled)             demo-grafana  demo-pg     datasource        false    false   Provide a datasource for Grafana service (without dashboard)
    (integration not enabled)             demo-kafka    demo-pg     metrics           false    false   Receive service metrics from service
    8e752fa9-a0c1-4332-892b-f1757390d53f  demo-pg       demo-kafka  kafka_logs        true     true    Send logs to Kafka
    (integration not enabled)             demo-pg       demo-pg     metrics           false    false   Send service metrics to InfluxDB, M3 or PostgreSQL service

.. _avn service integration types:

``avn service integration-types-list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Lists all available integration types for given project.
  
**Example:** List all integration types for the currently selected project.

::

    avn service integration-types-list

An example of ``account service integration-types-list`` output:

.. code:: text

    INTEGRATION_TYPE                 DEST_DESCRIPTION                                                      DEST_SERVICE_TYPE                SOURCE_DESCRIPTION                                          SOURCE_SERVICE_TYPES
    ===============================  ====================================================================  ===============================  ==========================================================  ==================================================================================================================================================================================================
    alertmanager                     Runs alert rules against time series databases and sends to Opsgenie  alertmanager                     Provide a datasource for Alertmanager service               m3coordinator
    dashboard                        Provide a datasource for Grafana service                              influxdb                         Dashboards for InfluxDB, M3 or PostgreSQL backed metrics    grafana
    datadog                          Receive service metrics from service                                  datadog                          Send service metrics to Datadog endpoint                    cassandra, elasticsearch, kafka, kafka_connect, kafka_mirrormaker, mysql, pg, redis
    datasource                       Provide a datasource for Grafana service (without dashboard)          elasticsearch                    Grafana datasource                                          grafana
    datasource                       Provide a datasource for Kafka Connect service                        alerta                           Kafka Connect datasource                                    kafka, kafka_connect
    datasource                       Provide a datasource for PostgreSQL service                           pg                               PostgreSQL datasource                                       pg
    datasource                       Provide a datasource for Elasticsearch service                        elasticsearch                    Elasticsearch datasource                                    elasticsearch
    ...
    schema_registry_proxy            Proxy Schema Registry requests                                        kafka                                                                                        external_schema_registry
    signalfx                         Receive service metrics from service                                  signalfx                         Send service metrics to SignalFX                            kafka


``avn service integration-update``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Updates an existing service integration.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``integration_id``
    - The ID of integration
  * - ``--user-config-json`` 
    - The integration parameters as JSON string or path to file (preceded by ``@``)
  * - ``-c KEY=VALUE``
    - The custom configuration settings. 
  

**Example:** Update the service integration with ID  ``8e752fa9-a0c1-4332-892b-f1757390d53f`` changing the Aiven for Kafka topic storing the logs to ``test_pg_log``.

::

  avn service integration-update 8e752fa9-a0c1-4332-892b-f1757390d53f \
    -c 'kafka_topic=test_pg_log'