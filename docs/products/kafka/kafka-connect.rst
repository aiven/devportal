Aiven for Apache Kafka® Connect
===============================

What is Aiven for Apache Kafka® Connect?
----------------------------------------

Aiven for Apache Kafka® Connect is a fully managed **distributed Apache Kafka® integration component**, deployable in the cloud of your choice. Apache Kafka Connect lets you integrate your existing data sources and sinks with Apache Kafka.

With an Apache Kafka Connect connector, you can source data from an existing technology into a topic or sink data from a topic to a target technology by defining the endpoints.


Why Apache Kafka® Connect?
--------------------------

Apache Kafka represents the best in class data streaming solution. Apache Kafka Connect allows integrating Apache Kafka with the rest of your data architecture with a configuration file which defines the source and the target of your data.

Source connectors
-----------------

.. grid:: 1 2 2 2

   .. grid-item-card:: **RDBMS**
       :margin: 2 2 0 0
       :shadow: md

       `Debezium for MySQL <https://debezium.io/docs/connectors/mysql/>`__ 

       :doc:`Debezium for PostgreSQL® <kafka-connect/howto/debezium-source-connector-pg>`

       `Debezium for SQL Server <https://debezium.io/docs/connectors/sqlserver/>`__ 

       `JDBC <https://github.com/aiven/aiven-kafka-connect-jdbc/blob/master/docs/source-connector.md>`__ 

   .. grid-item-card:: **Streaming**
       :shadow: md
       :margin: 2 2 0 0

       `Google Cloud Pub/Sub <https://github.com/GoogleCloudPlatform/pubsub/tree/master/kafka-connector>`__ 

       `Google Cloud Pub/Sub Lite <https://github.com/GoogleCloudPlatform/pubsub/>`_ 

       `Stream Reactor Cassandra® <https://docs.lenses.io/connectors/source/cassandra.html>`__

       `Stream Reactor MQTT <https://docs.lenses.io/connectors/source/mqtt.html>`__ 

   .. grid-item-card:: **NoSQL**
       :margin: 2 2 0 0
       :shadow: md

       `Couchbase <https://github.com/couchbase/kafka-connect-couchbase>`__

       `Official MongoDB® <https://docs.mongodb.com/kafka-connector/current/>`__

       `Debezium for MongoDB® <https://debezium.io/docs/connectors/mongodb/>`__


Sink connectors
---------------

.. grid:: 1 2 2 2

   .. grid-item-card:: **Filestore**
      :margin: 2 2 0 0
      :shadow: md

      :doc:`Aiven for Apache Kafka® S3 Sink Connector <kafka-connect/howto/s3-sink-connector-aiven>`

      `Confluent Amazon S3 Sink <https://developer.aiven.io/docs/products/kafka/kafka-connect/howto/s3-sink-connector-confluent>`__

      :doc:`Google Cloud Storage </docs/products/kafka/kafka-connect/howto/gcs-sink>`

   .. grid-item-card:: **NoSQL**
       :margin: 2 2 0 0
       :shadow: md

       `Couchbase® <https://github.com/couchbase/kafka-connect-couchbase>`__

       `Official MongoDB® <https://docs.mongodb.com/kafka-connector/current/>`__

       :doc:`OpenSearch® </docs/products/kafka/kafka-connect/howto/opensearch-sink>`

       `OpenSearch® <https://github.com/aiven/opensearch-connector-for-apache-kafka/blob/main/docs/opensearch-sink-connector-config-options.rst>`_ |preview|

       :doc:`Elasticsearch </docs/products/kafka/kafka-connect/howto/elasticsearch-sink>`

   .. grid-item-card:: **RDBMS**
       :margin: 2 2 0 0
       :shadow: md

       `JDBC <https://github.com/aiven/aiven-kafka-connect-jdbc/blob/master/docs/sink-connector.md>`__

   .. grid-item-card:: **Data Warehouse**
       :margin: 2 2 0 0
       :shadow: md

       `Google BigQuery <https://github.com/confluentinc/kafka-connect-bigquery>`__

       `Snowflake <https://docs.snowflake.net/manuals/user-guide/kafka-connector.html>`__ |preview|

   .. grid-item-card:: **Streaming**
       :margin: 2 2 0 0
       :shadow: md

       `Google Cloud Pub/Sub <https://github.com/GoogleCloudPlatform/pubsub/>`__

       `Google Cloud Pub/Sub Lite <https://github.com/GoogleCloudPlatform/pubsub/>`_

       `Stream Reactor Cassandra® <https://docs.lenses.io/connectors/sink/cassandra.html>`__

       `Stream Reactor InfluxDB® <https://docs.lenses.io/connectors/sink/influx.html>`__

       `Stream Reactor MongoDB® <https://docs.lenses.io/connectors/sink/mongo.html>`__

       `Stream Reactor MQTT <https://docs.lenses.io/connectors/sink/mqtt.html>`__

       `Stream Reactor Redis®* <https://docs.lenses.io/connectors/sink/redis.html>`__

   .. grid-item-card:: **Other**
       :margin: 2 2 0 0
       :shadow: md

       `HTTP <https://github.com/aiven/aiven-kafka-connect-http>`__ |preview|

       `Splunk <https://github.com/splunk/kafka-connect-splunk>`__




Get started with Aiven for Apache Kafka® Connect
------------------------------------------------

Take your first steps with Aiven for Apache Kafka Connect by following our :doc:`/docs/products/kafka/kafka-connect/getting-started` article, or browse through our full list of articles:


.. grid:: 1 2 2 2

    .. grid-item-card::
        :shadow: md
        :margin: 2 2 0 0

        📚 :doc:`Concepts </docs/products/kafka/kafka-connect/concepts>`

    .. grid-item-card::
        :shadow: md
        :margin: 2 2 0 0

        💻 :doc:`HowTo </docs/products/kafka/kafka-connect/howto>`

    .. grid-item-card::
        :shadow: md
        :margin: 2 2 0 0

        📖 :doc:`Reference </docs/products/kafka/kafka-connect/reference>`


Apache Kafka® Connect resources
-------------------------------

If you are new to Apache Kafka Connect, try these resources to learn more:

* The main Apache Kafka project page: http://kafka.apache.org/

* The Karapace schema registry that Aiven maintains and makes available for every Aiven for Apache Kafka service: https://karapace.io/

* Our code samples repository, to get you started quickly: https://github.com/aiven/aiven-examples

