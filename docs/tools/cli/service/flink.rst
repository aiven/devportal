Command reference: ``avn service flink``
============================================

Here you’ll find the full list of commands for ``avn service flink``.


Create a new Flink table
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
    - The id of the integration to use to locate the source/sink table/topic
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
 

**Example:** Create a Flink table named ``analytics-it`` within the service named ``pg-demo``.

::
  
  avn service database-create pg-demo --dbname analytics-it