Create the Aiven services
=========================

This section of the tutorial will showcase how to create the needed Aiven services via the `Aiven Console <https://console.aiven.io/>`_. We'll create three services:

* An :doc:`Aiven for Apache Kafka®</docs/products/kafka>` named ``demo-kafka`` for data streaming
* An :doc:`Aiven for Apache Flink®</docs/products/flink>` named ``demo-flink`` for streaming data transformation
* An :doc:`Aiven for PostgreSQL®</docs/products/postgresql>` named ``demo-postgresql`` for data storage and query

.. mermaid::

    graph LR;

        id1(Kafka)-- IoT metrics stream -->id3(Flink);
        id2(PostgreSQL)-- alerting threshold data -->id3;
        id3-. curated data .->id1(Kafka);

.. button-ref:: create-kafka
    :align: right
    :color: primary
    :outline:

    Next