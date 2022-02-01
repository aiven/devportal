Requirements for Apache Kafka® connectors
=========================================

This article outlines the required settings for standard and upsert Kafka connectors in Aiven for Apache Flink®.

.. note::

   Aiven for Apache Flink® supports the following data formats: JSON (default), Apache Avro, Confluent Avro, Debezium CDC. For more information on these, see the `Apache Flink® documentation on formats <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/connectors/table/formats/overview/>`_.

.. list-table::
  :header-rows: 1
  :align: left

  * - Parameter
    - Description
    - Standard connector
    - Upsert connector
  * - Key data format
    - Sets the format that is used to convert the *key* part of Kafka messages.
    - Optional
    - Required
  * - Key fields
    - Defines the columns from the SQL schema of the data table that are considered keys in the Kafka messages.
    - Optional (required if a key data format is selected)
    - Not available
  * - Value data format
    - Sets the format that is used to convert the *value* part of Kafka messages.
    - Required
    - Required
  * - Primary key
    - Defines the column in the SQL schema that is used to identify each message. Flink uses this to determine whether to insert a new message or update or delete an existing message. Defined with the ``PRIMARY KEY`` entry in the SQL schema for the data table. For example::

         PRIMARY KEY (hostname) NOT ENFORCED

    - Optional
    - Required


