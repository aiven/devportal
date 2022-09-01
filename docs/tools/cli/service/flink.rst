``avn service flink`` |beta|
==================================================================

Here you'll find the full list of commands for ``avn service flink``.


Manage an Apache Flink® table
--------------------------------------------------------

``avn service flink table create``
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Creates a new Aiven for Apache Flink® table.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  * - ``service_name``
    - The name of the service
  * - ``table_properties``
    - Table properties definition as JSON string or path (preceded by '@') to a JSON configuration file

The ``table_properties`` parameter should contain the following common properties in JSON format

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information

  * - ``name``
    - Logical table name
  * - ``integration_id``
    - The ID of the integration to use to locate the source/sink table/topic. The integration ID can be found with the :ref:`integration-list<avn_service_integration_list>` command
  * - ``schema_sql``
    - The Flink table SQL schema definition

And then a property identifying the type of Flink table connector within the one supported.

For the Aiven for Apache Kafka® :doc:`insert only mode </docs/products/flink/concepts/kafka-connectors>`, add a JSON field named ``kafka`` with the following fields included in a JSON object:

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  
  * - ``scan_startup_mode``
    - The Apache Kafka consumer starting offset; possible values are ``earliest-offset`` starting from the beginning of the topic and ``latest-offset`` starting from the last message
  * - ``topic``
    - The name of the source or target Aiven for Apache Kafka topic
  * - ``value_fields_include``
    - Defines if the message key fields are included in the value; possible values are ``ALL`` to include the key fields in the value, ``EXCEPT_KEY`` to remove them
  * - ``key_format``
    - Defines the format used to convert the message value; possible values are ``json`` or ``avro``; if the key is not used, the ``key_format`` field can be omitted
  * - ``value_format``
    - Defines the format used to convert the message value; possible values are ``json`` or ``avro``

For the Aiven for Apache Kafka® :doc:`upsert mode </docs/products/flink/concepts/kafka-connectors>`, add a JSON field named ``upsert-kafka`` with the following fields included in a JSON object:

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information
  
  * - ``topic``
    - The name of the source or target Aiven for Apache Kafka topic
  * - ``value_fields_include``
    - Defines if the message key fields are included in the value; possible values are ``ALL`` to include the key fields in the value, ``EXCEPT_KEY`` to remove them
  * - ``key_format``
    - Defines the format used to convert the message value; possible values are ``json`` or ``avro``; if the key is not used, the ``key_format`` field can be omitted
  * - ``value_format``
    - Defines the format used to convert the message value; possible values are ``json`` or ``avro``


For the Aiven for PostgreSQL® :doc:`JDBC query mode </docs/products/flink/howto/connect-pg>`, add a JSON field named ``jdbc`` with the following fields included in a JSON object:

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information

  * - ``table_name``
    - The name of the Aiven for PostgreSQL® database table

For the Aiven for OpenSearch® :doc:`index integration </docs/products/flink/howto/connect-pg>`, add a JSON field named ``opensearch`` with the following fields included in a JSON object:

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Information

  * - ``index``
    - The name of the  Aiven for OpenSearch® index to use


**Example:** Create a Flink table named ``KAlert`` on top of an Aiven for Apache Kafka topic in **insert mode** with:

* ``alert`` as source Apache Kafka **topic**
* ``kafka`` as connector type
* ``json`` as value and key data format
* ``earliest-offset`` as starting offset
* ``cpu FLOAT, node INT, cpu_percent INT, occurred_at TIMESTAMP_LTZ(3)`` as **SQL schema**
* ``ab8dd446-c46e-4979-b6c0-1aad932440c9`` as integration ID
* ``flink-devportal-demo`` as service name

::
  
  avn service flink table create flink-devportal-demo \
    """{
        \"name\":\"KAlert\",
        \"integration_id\": \"ab8dd446-c46e-4979-b6c0-1aad932440c9\",
        \"kafka\": {
            \"scan_startup_mode\": \"earliest-offset\",
            \"topic\": \"alert\",
            \"value_fields_include\": \"ALL\",
            \"value_format\": \"json\",
            \"key_format\": \"json\"
        },
        \"schema_sql\":\"cpu FLOAT, node INT, cpu_percent INT, occurred_at TIMESTAMP_LTZ(3)\"    
    }"""

**Example:** Create a Flink table named ``KAlert`` on top of an Aiven for Apache Kafka topic in **upsert mode** with:

* ``alert`` as source Apache Kafka **topic**
* ``upsert-kafka`` as connector type
* ``json`` as value and key data format
* ``cpu FLOAT, node INT PRIMARY KEY, cpu_percent INT, occurred_at TIMESTAMP_LTZ(3)`` as **SQL schema**
* ``ab8dd446-c46e-4979-b6c0-1aad932440c9`` as integration ID
* ``flink-devportal-demo`` as service name

::
  
  avn service flink table create flink-devportal-demo \
    """{
        \"name\":\"Kalert\",
        \"integration_id\": \"ab8dd446-c46e-4979-b6c0-1aad932440c9\",
        \"upsert_kafka\": {
            \"key_format\": \"json\",
            \"topic\": \"alert\",
            \"value_fields_include\": \"ALL\",
            \"value_format\": \"json\"
        },
        \"schema_sql\":\"cpu FLOAT, node INT PRIMARY KEY, cpu_percent INT, occurred_at TIMESTAMP_LTZ(3)\"    
    }"""

**Example:** Create a Flink table named ``KAlert`` on top of an Aiven for PostgreSQL table with:

* ``alert`` as source PostgreSQL **table**
* ``jdbc`` as connector type
* ``cpu FLOAT, node INT PRIMARY KEY, cpu_percent INT, occurred_at TIMESTAMP(3)`` as **SQL schema**
* ``ab8dd446-c46e-4979-b6c0-1aad932440c9`` as integration ID
* ``flink-devportal-demo`` as service name

::
  
  avn service flink table create flink-devportal-demo \
    """{
        \"name\":\"KAlert\",
        \"integration_id\": \"ab8dd446-c46e-4979-b6c0-1aad932440c9\",
        \"jdbc\": {
            \"table_name\": \"alert\"
        },
        \"schema_sql\":\"cpu FLOAT, node INT PRIMARY KEY, cpu_percent INT, occurred_at TIMESTAMP(3)\"    
    }"""

**Example:** Create a Flink table named ``KAlert`` on top of an Aiven for OpenSearch index with:

* ``alert`` as source OpenSearch **index**
* ``opensearch`` as connector type
* ``cpu FLOAT, node INT PRIMARY KEY, cpu_percent INT, occurred_at TIMESTAMP(3)`` as **SQL schema**
* ``ab8dd446-c46e-4979-b6c0-1aad932440c9`` as integration ID
* ``flink-devportal-demo`` as service name

::
  
  avn service flink table create flink-devportal-demo \
    """{
        \"name\":\"KAlert\",
        \"integration_id\": \"ab8dd446-c46e-4979-b6c0-1aad932440c9\",
        \"opensearch\": {
            \"index\": \"alert\"
        },
        \"schema_sql\":\"cpu FLOAT, node INT PRIMARY KEY, cpu_percent INT, occurred_at TIMESTAMP(3)\"    
    }"""


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

An example of ``avn service flink table get`` output:

.. code:: text

  INTEGRATION_ID                        TABLE_ID                              TABLE_NAME   SCHEMA_SQL              COLUMNS
  ====================================  ====================================  ===========  ======================  ===============================================================================================================
  77741d89-71f1-4de6-897a-fd83bce0ee62  f7bbe17b-ab47-46fd-83cb-2f5d23656018  mytablename  "id INT,name string"   ß{"data_type": "INT", "name": "id", "nullable": true}, {"data_type": "STRING", "name": "name", "nullable": true}

.. Tip::

  Adding the ``--json`` flag retrieves the table information in a richer JSON format

.. code:: json

  [
      {
          "columns": [
              {
                  "data_type": "INT",
                  "name": "id",
                  "nullable": true
              },
              {
                  "data_type": "STRING",
                  "name": "name",
                  "nullable": true
              }
          ],
          "integration_id": "77741d89-71f1-4de6-897a-fd83bce0ee62",
          "jdbc": {
              "table_name": "mysourcetablename"
          },
          "schema_sql": "id INT,name string",
          "table_id": "f7bbe17b-ab47-46fd-83cb-2f5d23656018",
          "table_name": "mytablename"
      }
  ]

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

  INTEGRATION_ID                        TABLE_ID                              TABLE_NAME   SCHEMA_SQL
  ====================================  ====================================  ===========  ======================
  315fe8af-34d9-4d7e-8711-bc7b6841dc55  882ee0be-cb0b-4ccf-b4d1-89d2e4a34260  ttt5         "id INT,\nage int"
  77741d89-71f1-4de6-897a-fd83bce0ee62  f7bbe17b-ab47-46fd-83cb-2f5d23656018  testname445  "id INT,\nname string"

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
    - The ID of the job to retrieve

**Example:** Retrieve the definition of the Flink job with ID ``8b8ac2fe-b6eb-46bc-b327-fb4b84d27276`` belonging to the Aiven for Flink service ``flink-devportal-demo``.

::
  
  avn service flink job get flink-devportal-demo 8b8ac2fe-b6eb-46bc-b327-fb4b84d27276

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
