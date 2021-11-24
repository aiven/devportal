List of available Apache Kafka Connect connectors
=================================================

The following Apache Kafka Connect connectors are currently available, and can
be used in any Aiven for Kafka services with Kafka Connect enabled. 


Source connectors
-----------------

Source connectors enable the integration of data from an existing technology into an Apache Kafka topic. The following is the list of available connectors:

* `Couchbase <https://github.com/couchbase/kafka-connect-couchbase>`__

* `Official MongoDB <https://docs.mongodb.com/kafka-connector/current/>`__ :badge:`preview,cls=badge-secondary badge-pill`

* `Debezium for MongoDB <https://debezium.io/docs/connectors/mongodb/>`__

* `Debezium for MySQL <https://debezium.io/docs/connectors/mysql/>`__

* `Debezium for PostgreSQL <https://help.aiven.io/kafka/setting-up-debezium-with-aiven-postgresql>`__

* `Debezium for SQL Server <https://debezium.io/docs/connectors/sqlserver/>`__

* `Google Cloud Pub/Sub <https://github.com/GoogleCloudPlatform/pubsub/tree/master/kafka-connector>`__

* `JDBC <https://github.com/aiven/aiven-kafka-connect-jdbc/blob/master/docs/source-connector.md>`__

* Schema Source

* `Stream Reactor Cassandra <https://docs.lenses.io/connectors/source/cassandra.html>`__

* `Stream Reactor MQTT <https://docs.lenses.io/connectors/source/mqtt.html>`__

Sink connectors
-----------------

Sink connectors enable the integration of data from an existing Apache Kafka topic to a target technology. The following is the list of available connectors:

* `Aiven for Kafka GCS Sink Connector <https://help.aiven.io/kafka/connectors/aiven-kafka-gcs-sink-connector>`__

* `Aiven for Kafka S3 Sink Connector <https://help.aiven.io/kafka/connectors/aiven-kafka-s3-sink-connector>`__

* `Confluent Amazon S3 Sink <https://help.aiven.io/kafka/aiven-kafka-kafka-connect-s3>`__

* `Official MongoDB <https://docs.mongodb.com/kafka-connector/current/>`__ :badge:`preview,cls=badge-secondary badge-pill`

* `Couchbase <https://github.com/couchbase/kafka-connect-couchbase>`__

* `Elasticsearch <https://help.aiven.io/kafka/aiven-kafka-elasticsearch-sink-connector>`__

* `Confluent Elasticsearch Sink <https://docs.confluent.io/kafka-connect-elasticsearch/current/index.html>`__

* `Google Cloud Pub/Sub <https://github.com/GoogleCloudPlatform/pubsub/>`__

* `Google BigQuery <https://github.com/wepay/kafka-connect-bigquery>`__

* `HTTP <https://github.com/aiven/aiven-kafka-connect-http>`__ :badge:`preview,cls=badge-secondary badge-pill`

* `JDBC <https://github.com/aiven/aiven-kafka-connect-jdbc/blob/master/docs/sink-connector.md>`__

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

Upon creating a support requests, Aiven will evaluate the requested connector and might add support for it. 

Aiven evaluation process for new Apache Kafka Connect connectors checks:

* license compatibility
* technical evaluation
* active repository maintenance

The addition of new Apache Kafka connectors is done at the sole discretion of Aiven.

.. Tip::

    When requesting connectors that are not on the pre-approved list through a support ticket, specify the target Aiven for Apache Kafka service you'd like to have it installed to.

If you know about new and interesting connectors you'd like Aiven to support, please open a support request about it to help us shaping the future roadmap.