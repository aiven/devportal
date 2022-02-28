``avn service connector``
============================================

Here you’ll find the full list of commands for ``avn service connector``.


Manage Kafka® Connect connectors details
--------------------------------------------------------

Commands for managing Aiven for Apache Kafka® Connect connectors via ``avn`` commands.


``avn service connector available``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Lists Kafka® Connect connector plugins available in a given Aiven for Apache Kafka® service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the Service

**Example:** List the Kafka Connect connector plugins available for the service ``kafka-demo``.

::

  avn service connector available kafka-demo

.. _avn_service_connector_create:

``avn service connector create``
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Creates a new Kafka® Connect connector in a given Aiven for Apache Kafka® service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the Service
  * - ``connector_config``
    - JSON string or path (preceded by ``@``) to a Kafka Connect connector JSON configuration file

**Example:** Create a new JDBC source Kafka Connect connector in the service ``kafka-demo`` passing the JSON configuation string.

::

  avn service connector create kafka-demo '{
    "name": "pg-bulk-invoices-source",
    "connector.class": "io.aiven.connect.jdbc.JdbcSourceConnector",
    "connection.url": "jdbc:postgresql://demo-pg-myinventedprojectname.aivencloud.com:13039/defaultdb?sslmode=require",
    "connection.user": "avnadmin",
    "connection.password": "verysecurepassword123",
    "table.whitelist": "invoices",
    "mode": "bulk",
    "poll.interval.ms": "10000",
    "topic.prefix": "pg_source_"
    }'


``avn service connector delete``
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Deletes Kafka® Connect connector in a given Aiven for Apache Kafka® service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the Service
  * - ``connector``
    - Kafka Connect connector name

**Example:** Delete the Kafka Connect connector named ``pg-bulk-invoices-source`` in the service ``kafka-demo``.

::

   avn service connector delete kafka-demo pg-bulk-invoices-source 

``avn service connector list``
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Lists Kafka® Connect connectors in a given Aiven for Apache Kafka® service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the Service

**Example:** List all Kafka Connect connectors in the service ``kafka-demo``.

::

    avn service connector list kafka-demo

An example of ``avn service connector list`` output:

.. code:: text

    {
        "connectors": [
            {
                "config": {
                    "connection.password": "verysecurepassword123",
                    "connection.url": "jdbc:postgresql://demo-test-myinventedprojectname.aivencloud.com:13039/defaultdb?sslmode=require",
                    "connection.user": "avnadmin",
                    "connector.class": "io.aiven.connect.jdbc.JdbcSourceConnector",
                    "mode": "bulk",
                    "name": "pg-bulk-invoices-source",
                    "poll.interval.ms": "10000",
                    "table.whitelist": "invoices",
                    "topic.prefix": "pg_source_"
                },
                "name": "pg-bulk-invoices-source",
                "plugin": {
                    "author": "Aiven",
                    "class": "io.aiven.connect.jdbc.JdbcSourceConnector",
                    "docURL": "https://github.com/aiven/aiven-kafka-connect-jdbc/blob/master/docs/source-connector.md",
                    "title": "JDBC Source",
                    "type": "source",
                    "version": "6.6.0"
                },
                "tasks": []
            }
        ]
    }

``avn service connector pause``
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Pauses a Kafka® Connect connector in a given Aiven for Apache Kafka® service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the Service
  * - ``connector``
    - Kafka Connect connector name

**Example:** Pause the Kafka Connect connector named ``pg-bulk-invoices-source`` in the service ``kafka-demo``.

::

   avn service connector pause kafka-demo pg-bulk-invoices-source 


``avn service connector restart``
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Restarts a Kafka® Connect connector in a given Aiven for Apache Kafka® service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the Service
  * - ``connector``
    - Kafka Connect connector name

**Example:** Restart the Kafka Connect connector named ``pg-bulk-invoices-source`` in the service ``kafka-demo``.

::

   avn service connector restart kafka-demo pg-bulk-invoices-source 

``avn service connector restart-task``
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Restarts a Kafka® Connect connector task in a given Aiven for Apache Kafka® service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the Service
  * - ``connector``
    - Kafka Connect connector name
  * - ``task``
    - Kafka Connect connector task id

**Example:** Restart the task with id ``0`` in the Kafka Connect connector named ``pg-bulk-invoices-source`` belonging to the service ``kafka-demo``.

::

    avn service connector restart-task kafka-demo pg-bulk-invoices-source 0

``avn service connector resume``
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Resumes a Kafka® Connect connector in a given Aiven for Apache Kafka® service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the Service
  * - ``connector``
    - Kafka Connect connector name

**Example:** Resume the Kafka Connect connector named ``pg-bulk-invoices-source`` belonging to the service ``kafka-demo``.

::

    avn service connector resume kafka-demo pg-bulk-invoices-source

``avn service connector schema``
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Retrieves the configuration information for a Kafka® Connect connector plugin in a given Aiven for Apache Kafka® service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the Service
  * - ``connector``
    - Kafka Connect connector plugin class name

**Example:** Retrieve the schema for the Kafka Connect plugin with class ``io.debezium.connector.sqlserver.SqlServerConnector`` belonging to the service ``kafka-demo``.

::

    avn service connector schema kafka-demo io.debezium.connector.sqlserver.SqlServerConnector

``avn service connector status``
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Gets a Kafka® Connect connector status in a given Aiven for Apache Kafka service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the Service
  * - ``connector``
    - Kafka Connect connector name

**Example:** Check the status of a Kafka Connect connector named ``pg-bulk-invoices-source`` belonging to the service ``kafka-demo``.

::

    avn service connector status kafka-demo pg-bulk-invoices-source

An example of ``avn service connector status`` output:

.. code:: text

    {
        "status": {
            "state": "RUNNING",
            "tasks": [
                {
                    "id": 0,
                    "state": "RUNNING",
                    "trace": ""
                }
            ]
        }
    }

``avn service connector update``
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Updates a Kafka® Connect connector in a given Aiven for Apache Kafka® service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the Service
  * - ``connector``
    - Kafka Connect connector name
  * - ``connector_config``
    - JSON string or path (preceded by ``@``) to a Kafka Connect connector JSON configuration file

**Example:** Update a the JDBC source Kafka Connect connector named ``pg-bulk-invoices-source`` in the service ``kafka-demo`` with the JSON configuation string contained in the file ``kafka-connect-config.json``.

::

    avn service connector update kafka-demo pg-bulk-invoices-source @kafka-connect-config.json
