Standard and upsert Apache Kafka connectors
===========================================

In addition to integration with Apache Kafka through a standard connector, Aiven for Apache Flink also supports the use of *upsert* connectors, which allows you to create changelog-type data streams.

When you integrate a standard Apache Kafka with your Aiven for Apache Flink service, you can use the service to read data from one Kafka topic and write the processed data to another Kafka topic. Each message in the source topic that is processed and written to the sink topic is considered unique and is handled as an individual entry.

.. mermaid::

    graph LR;

        id1>Source topic]-- message --> id2{Flink processing};
        id2-- processed message --> id3[sink topic];


Another integration approach is upsert, or ``INSERT/UPDATE``, which is a method of updating or deleting data based on a primary key. If a message in the source upsert topic uses a primary key with a value that already exists, the message data is interpreted as an update to the existing data that uses the same key in the upsert sink topic. If the key does not exist, it is inserted as new data, and if the message data is null, it is interpreted as a ``DELETE`` operation for that key.

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

