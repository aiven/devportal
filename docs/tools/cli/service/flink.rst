``avn service flink`` |beta|
==================================================================

Here you’ll find the full list of commands for ``avn service flink``.


Manage an Apache Flink® table
--------------------------------------------------------

``avn service flink table create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Creates a new Aiven for Apache Flink table.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``integration_id``
    - The ID of the integration to use to locate the source/sink table/topic. The integration ID can be found with the :ref:`integration-list<avn_service_integration_list>` command
  * - ``--table-name``
    - The Flink table name
  * - ``--kafka-topic``
    - The Aiven for Apache Kafka® topic to be used as source/sink (Only for Kafka integrations)
  * - ``--kafka-connector-type``
    - The :doc:`Flink connector type for Apache Kafka </docs/products/flink/concepts/kafka-connectors>`; possible values are ``upsert-kafka`` and ``kafka``
  * - ``--kafka-key-format``
    - The :doc:`Apache Kafka message key format </docs/products/flink/concepts/kafka-connector-requirements>`; possible values are ``avro,avro-confluent``, ``debezium-avro-confluent``, ``debezium-json``, and ``json``
  * - ``--kafka-key-fields``
    - The list of :doc:`fields to be used as Key for the message </docs/products/flink/concepts/kafka-connector-requirements>`
  * - ``--kafka-value-format``
    - The :doc:`Apache Kafka message value format </docs/products/flink/concepts/kafka-connector-requirements>`; possible values are ``avro,avro-confluent``, ``debezium-avro-confluent``, ``debezium-json``, and ``json``
  * - ``--kafka-startup-mode``
    - The Apache Kafka consumer starting offset; possible values are ``earliest-offset`` starting from the beginning of the topic and ``latest-offset`` starting from the last message
  * - ``--jdbc-table``
    - The Aiven for PostgreSQL® table name to be used as source/sink (Only for PostgreSQL integrations)
  * - ``partitioned-by``
    - A column from the table schema to use as Flink table partition definition
  * - ``--like-options``
    - Creates the Flink table based on the definition of another existing Flink table
 

**Example:** Create a Flink table named ``KAlert`` with:

* ``alert`` as source Apache Kafka **topic**
* ``kafka`` as connector type
* ``json`` as value and key data format
* the field ``node`` as key
* ``earliest-offset`` as starting offset
* ``cpu FLOAT, node INT, cpu_percent INT, occurred_at TIMESTAMP_LTZ(3)`` as **SQL schema**
* ``ab8dd446-c46e-4979-b6c0-1aad932440c9`` as integration ID
* ``flink-devportal-demo`` as service name

::
  
  avn service flink table create flink-devportal-demo ab8dd446-c46e-4979-b6c0-1aad932440c9  \
    --table-name KAlert                                                                     \
    --kafka-topic alert                                                                     \
    --kafka-connector-type kafka                                                            \
    --kafka-key-format json                                                                 \
    --kafka-key-fields node                                                                 \
    --kafka-value-format json                                                               \
    --kafka-startup-mode earliest-offset                                                    \
    --schema-sql "cpu FLOAT, node INT, cpu_percent INT, occurred_at TIMESTAMP_LTZ(3)"

``avn service flink table delete``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Deletes an existing Aiven for Apache Flink table.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``table_id``
    - The ID of the table to delete

**Example:** Delete the Flink table with ID ``8b8ac2fe-b6eb-46bc-b327-fb4b84d27276`` belonging to the Aiven for Flink service ``flink-devportal-demo``.

::
  
  avn service flink table delete flink-devportal-demo 8b8ac2fe-b6eb-46bc-b327-fb4b84d27276

``avn service flink table get``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Retrieves the definition of an existing Aiven for Apache Flink table.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``table_id``
    - The ID of the table to retrieve

**Example:** Retrieve the definition of the Flink table with ID ``8b8ac2fe-b6eb-46bc-b327-fb4b84d27276`` belonging to the Aiven for Flink service ``flink-devportal-demo``.

::
  
  avn service flink table get flink-devportal-demo 8b8ac2fe-b6eb-46bc-b327-fb4b84d27276

.. _avn_service_flink_table_list:

``avn service flink table list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Lists all the Aiven for Apache Flink tables in a selected service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service

**Example:** List all the Flink tables available in the Aiven for Flink service ``flink-devportal-demo``.

::
  
  avn service flink table list flink-devportal-demo

An example of ``avn service flink table list`` output:

.. code:: text

  INTEGRATION_ID                        TABLE_ID                              TABLE_NAME
  ====================================  ====================================  ==========
  ab8dd446-c46e-4979-b6c0-1aad932440c9  acb601d7-2000-4076-ae58-563aa7d9ab5a  KAlert

Manage a Flink job
--------------------------------------------------------

``avn service flink job create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Creates a new Aiven for Apache Flink job.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``job_name``
    - Name of the Flink job
  * - ``--table-ids``
    - List of Flink tables IDs to use as source/sink. Table IDs can be found using the :ref:`list <avn_service_flink_table_list>` command
  * - ``--statement``
    - Flink job SQL statement
 

**Example:** Create a Flink job named ``JobExample`` with:

* ``KCpuIn`` (with id ``cac53785-d1b5-4856-90c8-7cbcc3efb2b6``) and ``KAlert`` (with id ``54c2f4e6-a446-4d62-8dc9-2b81179c6f43``) as source/sink **tables**
* ``INSERT INTO KAlert SELECT * FROM KCpuIn WHERE cpu_percent > 70`` as **SQL statement**
* ``flink-devportal-demo`` as service name

::
  
  avn service flink job create flink-devportal-demo JobExample                        \
    --table-ids cac53785-d1b5-4856-90c8-7cbcc3efb2b6 54c2f4e6-a446-4d62-8dc9-2b81179c6f43 \
    --statement "INSERT INTO KAlert SELECT * FROM KCpuIn WHERE cpu_percent > 70"

``avn service flink job cancel``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Cancels an existing Aiven for Apache Flink job.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``job_id``
    - The ID of the job to delete

**Example:** Cancel the Flink job with ID ``8b8ac2fe-b6eb-46bc-b327-fb4b84d27276`` belonging to the Aiven for Flink service ``flink-devportal-demo``.

::
  
  avn service flink job cancel flink-devportal-demo 8b8ac2fe-b6eb-46bc-b327-fb4b84d27276

``avn service flink job get``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Retrieves the definition of an existing Aiven for Apache Flink job.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``job_id``
    - The ID of the table to retrieve

**Example:** Retrieve the definition of the Flink job with ID ``8b8ac2fe-b6eb-46bc-b327-fb4b84d27276`` belonging to the Aiven for Flink service ``flink-devportal-demo``.

::
  
  avn service flink table get flink-devportal-demo 8b8ac2fe-b6eb-46bc-b327-fb4b84d27276

An example of ``avn service flink job get`` output:

.. code:: text

  JID                               NAME        STATE    START-TIME     END-TIME  DURATION  ISSTOPPABLE  MAXPARALLELISM
  ================================  ==========  =======  =============  ========  ========  ===========  ==============
  b63c78c70033e00afa84de9029257e31  JobExample  RUNNING  1633336792083  -1        423503    false        96

``avn service flink job list``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Lists all the Aiven for Apache Flink jobs in a selected service.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service

**Example:** List all the Flink jobs available in the Aiven for Flink service ``flink-devportal-demo``.

::
  
  avn service flink jobs list flink-devportal-demo

An example of ``avn service flink job list`` output:

.. code:: text

  ID                                STATUS
  ================================  =======
  b63c78c70033e00afa84de9029257e31  RUNNING
