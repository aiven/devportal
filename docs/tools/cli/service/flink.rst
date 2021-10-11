Command reference: ``avn service flink``
============================================

Here you’ll find the full list of commands for ``avn service flink``.


Manage a Flink table
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
    - The ID of the integration to use to locate the source/sink table/topic
  * - ``--table-name``
    - The Flink table name
  * - ``--kafka-topic``
    - The Aiven for Apache Kafka topic to be used as source/sink (Only for Kafka integrations)
  * - ``--jdbc-table``
    - The Aiven for PostgreSQL table name to be used as source/sink (Only for PostgreSQL integrations)
  * - ``partitioned-by``
    - A column from the table schema to use as Flink table partition definition
  * - ``--like-options``
    - Creates the Flink table based on the definition of another existing Flink table
  * - ``--schema-sql``
    - Flink table schema SQL definition
 

**Example:** Create a Flink table named ``KAlert`` with:

* ``alert`` as source Apache Kafka **topic**
* ``node INT, occurred_at TIMESTAMP_LTZ(3), cpu_in_mb FLOAT`` as **SQL schema**
* ``ab8dd446-c46e-4979-b6c0-1aad932440c9`` as integration ID
* ``flink-devportal-demo`` as service name

::
  
  avn service flink table create flink-devportal-demo ab8dd446-c46e-4979-b6c0-1aad932440c9  \
    --table-name KAlert                                                                     \
    --kafka-topic alert                                                                     \
    --schema-sql "node INT, occurred_at TIMESTAMP_LTZ(3), cpu_in_mb FLOAT"

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

.. code:: tex

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
  * - ``--tables``
    - List of Flink tables to use as source/sink
  * - ``--statement``
    - Flink job sql statement
 

**Example:** Create a Flink job named ``JobExample`` with:

* ``KCpuIn, KAlert`` as source/sink **tables**
* ``INSERT INTO KAlert SELECT * FROM KCpuIn WHERE cpu_in_mb > 70`` as **SQL statement**
* ``flink-devportal-demo`` as service name

::
  
  avn service flink job create flink-devportal-demo JobExample \
    --tables KCpuIn KAlert                                     \
    --statement "INSERT INTO KAlert SELECT * FROM KCpuIn WHERE cpu_in_mb > 70" 

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

.. code:: tex

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

.. code:: tex

  ID                                STATUS
  ================================  =======
  b63c78c70033e00afa84de9029257e31  RUNNING