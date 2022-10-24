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

       :doc:`Debezium for MySQL <kafka-connect/howto/debezium-source-connector-mysql>` 

       :doc:`Debezium for PostgreSQL® <kafka-connect/howto/debezium-source-connector-pg>`

       :doc:`Debezium for SQL Server <kafka-connect/howto/debezium-source-connector-sql-server>`

       :doc:`JDBC <kafka-connect/howto/jdbc-source-connector-pg>` 

   .. grid-item-card:: **Streaming**
       :shadow: md
       :margin: 2 2 0 0

       `Google Cloud Pub/Sub <https://github.com/GoogleCloudPlatform/pubsub/tree/master/kafka-connector>`__ 

       `Google Cloud Pub/Sub Lite <https://github.com/GoogleCloudPlatform/pubsub/>`_ 

       :doc:`Stream Reactor Cassandra® <kafka-connect/howto/cassandra-streamreactor-source>`

       `Stream Reactor MQTT <https://docs.lenses.io/connectors/source/mqtt.html>`__ 

   .. grid-item-card:: **NoSQL**
       :margin: 2 2 0 0
       :shadow: md

       `Couchbase <https://github.com/couchbase/kafka-connect-couchbase>`__

       :doc:`Official MongoDB® <kafka-connect/howto/mongodb-poll-source-connector>`

       :doc:`Debezium for MongoDB® <kafka-connect/howto/debezium-source-connector-mongodb>`


Sink connectors
---------------

.. grid:: 1 2 2 2

   .. grid-item-card:: **Filestore**
      :margin: 2 2 0 0
      :shadow: md

      :doc:`Aiven for Apache Kafka® S3 Sink Connector <kafka-connect/howto/s3-sink-connector-aiven>`

      :doc:`Confluent Amazon S3 Sink <kafka-connect/howto/s3-sink-connector-confluent>`

      :doc:`Google Cloud Storage <kafka-connect/howto/gcs-sink>`

   .. grid-item-card:: **NoSQL**
       :margin: 2 2 0 0
       :shadow: md

       `Couchbase® <https://github.com/couchbase/kafka-connect-couchbase>`__

       :doc:`Official MongoDB® <kafka-connect/howto/mongodb-sink-mongo>`

       :doc:`OpenSearch® <kafka-connect/howto/opensearch-sink>` |preview|

       :doc:`Elasticsearch <kafka-connect/howto/elasticsearch-sink>`

   .. grid-item-card:: **RDBMS**
       :margin: 2 2 0 0
       :shadow: md

       :doc:`JDBC <kafka-connect/howto/jdbc-sink>`

   .. grid-item-card:: **Data Warehouse**
       :margin: 2 2 0 0
       :shadow: md

       :doc:`Google BigQuery <kafka-connect/howto/gcp-bigquery-sink>`

       :doc:`Snowflake <kafka-connect/howto/snowflake-sink>`

   .. grid-item-card:: **Streaming**
       :margin: 2 2 0 0
       :shadow: md

       `Google Cloud Pub/Sub <https://github.com/GoogleCloudPlatform/pubsub/>`__

       `Google Cloud Pub/Sub Lite <https://github.com/GoogleCloudPlatform/pubsub/>`_

       :doc:`Stream Reactor Cassandra® <kafka-connect/howto/cassandra-streamreactor-sink>`

       :doc:`Stream Reactor InfluxDB® <kafka-connect/howto/influx-sink>`

       :doc:`Stream Reactor MongoDB® <kafka-connect/howto/mongodb-sink-lenses>`

       `Stream Reactor MQTT <https://docs.lenses.io/connectors/sink/mqtt.html>`__

       :doc:`Stream Reactor Redis®* <kafka-connect/howto/redis-streamreactor-sink>`

   .. grid-item-card:: **Other**
       :margin: 2 2 0 0
       :shadow: md

       :doc:`HTTP <kafka-connect/howto/http-sink>`

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


------

*Elasticsearch is a trademark of Elasticsearch B.V., registered in the U.S. and in other countries.*
*Couchbase is a trademark of Couchbase, Inc.*
