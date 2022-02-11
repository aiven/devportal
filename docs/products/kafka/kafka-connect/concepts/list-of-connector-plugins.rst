List of available Apache Kafka Connect connectors
=================================================

The following connectors can be used in any Aiven for Kafka services with Kafka Connect enabled. 


Source connectors
-----------------

Source connectors enable the integration of data from an existing technology into an Apache Kafka topic. The following is the list of available source connectors:

* `Couchbase <https://github.com/couchbase/kafka-connect-couchbase>`__ (author: Couchbase)

* `Official MongoDB <https://docs.mongodb.com/kafka-connector/current/>`__ :badge:`preview,cls=badge-secondary badge-pill` (author: MongoDB)

* `Debezium for MongoDB <https://debezium.io/docs/connectors/mongodb/>`__ (author: Debezium)

* `Debezium for MySQL <https://debezium.io/docs/connectors/mysql/>`__ (author: Debezium)

* `Debezium for PostgreSQL <https://help.aiven.io/kafka/setting-up-debezium-with-aiven-postgresql>`__ (author: Debezium)

* `Debezium for SQL Server <https://debezium.io/docs/connectors/sqlserver/>`__ (author: Debezium)

* `Google Cloud Pub/Sub <https://github.com/GoogleCloudPlatform/pubsub/tree/master/kafka-connector>`__ (author: Google)

* Google Cloud Pub/Sub Lite (author: Google)

* `JDBC <https://github.com/aiven/aiven-kafka-connect-jdbc/blob/master/docs/source-connector.md>`__ (author: Aiven)

* Schema Source (author: Confluent)

* `Stream Reactor Cassandra <https://docs.lenses.io/connectors/source/cassandra.html>`__ (author: Lenses.io)

* `Stream Reactor MQTT <https://docs.lenses.io/connectors/source/mqtt.html>`__ (author: Lenses.io)

Sink connectors
-----------------

Sink connectors enable the integration of data from an existing Apache Kafka topic to a target technology. The following is the list of available sink connectors:

* `Aiven for Kafka S3 Sink Connector <https://help.aiven.io/kafka/connectors/aiven-kafka-s3-sink-connector>`__

* `Confluent Amazon S3 Sink <https://help.aiven.io/kafka/aiven-kafka-kafka-connect-s3>`__

* `Couchbase <https://github.com/couchbase/kafka-connect-couchbase>`__

* `Elasticsearch <https://help.aiven.io/kafka/aiven-kafka-elasticsearch-sink-connector>`__

* `Google BigQuery <https://github.com/wepay/kafka-connect-bigquery>`__

* `Google Cloud Pub/Sub <https://github.com/GoogleCloudPlatform/pubsub/>`__

* Google Cloud Pub/Sub Lite

* Google Cloud Storage

* `HTTP <https://github.com/aiven/aiven-kafka-connect-http>`__ :badge:`preview,cls=badge-secondary badge-pill`

* `JDBC <https://github.com/aiven/aiven-kafka-connect-jdbc/blob/master/docs/sink-connector.md>`__

* `Official MongoDB <https://docs.mongodb.com/kafka-connector/current/>`__ :badge:`preview,cls=badge-secondary badge-pill`

* Opensearch

* `Snowflake <https://docs.snowflake.net/manuals/user-guide/kafka-connector.html>`__ :badge:`preview,cls=badge-secondary badge-pill`

* `Splunk <https://github.com/splunk/kafka-connect-splunk>`__

* `Stream Reactor Cassandra <https://docs.lenses.io/connectors/sink/cassandra.html>`__

* `Stream Reactor InfluxDB <https://docs.lenses.io/connectors/sink/influx.html>`__

* `Stream Reactor Mongo DB <https://docs.lenses.io/connectors/sink/mongo.html>`__

* `Stream Reactor MQTT <https://docs.lenses.io/connectors/sink/mqtt.html>`__

* `Stream Reactor Redis <https://docs.lenses.io/connectors/sink/redis.html>`__


Preview connectors
------------------

.. image:: /images/products/kafka/kafka-connect/preview-kafka-connect-connectors.png
   :alt: Preview icon next to a MongoDB Apache Kafka Connect connector

Some of the available connectors have the :badge:`preview,cls=badge-secondary badge-pill` tag next to the name. **Preview connectors do not come under our SLA**, consider this before using them for production purposes. 
Bugs should be reported to the code owner directly.


Requesting new connectors
-------------------------

If you know about new and interesting connectors you'd like us to support, please open a support request about it to help us shaping the future roadmap.
You can request adding support of a new connector by creating a support ticket. We will evaluate the requested connector and might add support for it.

Aiven evaluation process for new Apache Kafka Connect connectors checks:

* license compatibility
* technical implementation
* active repository maintenance

.. Tip::

    When requesting connectors that are not on the pre-approved list through a support ticket, specify the target Aiven for Apache Kafka service you'd like to have it installed to.

