Standard and upsert Apache Kafka connectors
===========================================

In addition to integration with Apache Kafka through a standard connector, Aiven for Apache Flink also supports the use of *upsert* connectors, which allows you to create changelog-type data streams.

When you integrate a standard Apache Kafka with your Aiven for Apache Flink service, you can use the service to read data from one Kafka topic and write the processed data to another Kafka topic. Each message in the source topic that is processed and written to the sink topic is considered unique and is handled as an individual entry.

.. mermaid::

    graph LR;

        id1>Source topic]-- message --> id2{Flink processing};
        id2-- processed message --> id3[sink topic];


Another integration approach is upsert, or ``INSERT/UPDATE``, which is a method of updating or deleting data based on the message key. When used as a source, Flink interprets a message that has an existing key as an update and replaces the value for that key. If the key does not exist, it is inserted as new data, and if the message data is null, it is interpreted as a ``DELETE`` operation for that key.

When used as a sink, upsert provides a method to create Kafka compacted topics (see the Log Compaction section in the `Apache Kafka documentation <https://kafka.apache.org/documentation/>`_ for details), containing only the latest value for a specific key and pushing a tombstone message on deletion.

.. mermaid::

    graph LR;

        id1>Source topic]-- key, value --> id2{Flink processing};
        id2-. key not found .-> id3(INSERT);
        id2-. key found, value .-> id4(UPDATE);
        id2-. key found, no value .-> id5(DELETE);
        id3-.->id6[Sink topic];
        id4-.->id6;
        id5-.->id6;


How to choose the right connector type
--------------------------------------

For most common purposes, such as filtering data or performing calculations on streamed data, a standard Kafka connector is sufficient. You can also perform data aggregation with standard connectors, but depending on the type of aggregation, it may require more careful planning and more complex SQL compared to using upsert connectors.

If you want to use multiple data streams as a source, but have the results for matching identifiers combined into single events within the same target topic, choose upsert connectors. While it varies to some extent depending on your specific use case, this means that using upsert connectors often makes it easier and more efficient to implement data aggregation.

In addition, choose upsert connectors if you want to provide the output as a compacted topic and read only the latest value for each message key.


Requirements for each connector type
------------------------------------

.. note::

   Aiven for Apache Flink supports the following data formats: JSON (default), Apache Avro, Confluent Avro, Debezium CDC. For more information on these, see the `Apache Flink documentation on formats <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/connectors/table/formats/overview/>`_.

**Key data format**
  This sets the format that is used to convert the *key* part of Kafka messages.

  This is optional for standard Kafka connectors, but required for upsert Kafka connectors.

**Key fields**
  This defines the columns from the SQL schema of the data table that are considered keys in the Kafka messages.

  For standard Kafka connectors, this is required if you select a **Key data format**. It is not available for upsert Kafka connectors.

**Value data format**
  This sets the format that is used to convert the *value* part of Kafka messages.

  This is required for both types of Kafka connector.

**Primary key**
  This defines the column in the SQL schema that is used to identify each message. Flink uses this to determine whether to insert a new message or update or delete an existing message.

  Required for upsert Kafka connectors and defined with the ``PRIMARY KEY`` entry in the SQL schema for the data table. For example::

      PRIMARY KEY (hostname) NOT ENFORCED

