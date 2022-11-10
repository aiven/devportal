List of available Apache Kafka® Connect connectors
==================================================

The following connectors can be used in any Aiven for Apache Kafka® services with Apache Kafka Connect enabled. 


Source connectors
-----------------

Source connectors enable the integration of data from an existing technology into an Apache Kafka topic. The following is the list of available source connectors:

* `Couchbase <https://github.com/couchbase/kafka-connect-couchbase>`__

* `Official MongoDB® <https://www.mongodb.com/docs/kafka-connector/current/>`__

* `Debezium for MongoDB® <https://debezium.io/docs/connectors/mongodb/>`__

* `Debezium for MySQL <https://debezium.io/docs/connectors/mysql/>`__ 

* :doc:`Debezium for PostgreSQL® <../howto/debezium-source-connector-pg>`

* `Debezium for SQL Server <https://debezium.io/docs/connectors/sqlserver/>`__ 

* `Google Cloud Pub/Sub <https://github.com/GoogleCloudPlatform/pubsub/tree/master/kafka-connector>`__ 

* `Google Cloud Pub/Sub Lite <https://github.com/GoogleCloudPlatform/pubsub/>`_ 

* `JDBC <https://github.com/aiven/jdbc-connector-for-apache-kafka/blob/master/docs/source-connector.md>`__

* Schema Source 

* `Stream Reactor Cassandra® <https://docs.lenses.io/connectors/source/cassandra.html>`__

* `Stream Reactor MQTT <https://docs.lenses.io/connectors/source/mqtt.html>`__ 

Sink connectors
-----------------

Sink connectors enable the integration of data from an existing Apache Kafka topic to a target technology. The following is the list of available sink connectors:

* :doc:`Aiven for Apache Kafka® S3 Sink Connector <../howto/s3-sink-connector-aiven>`

* `Confluent Amazon S3 Sink <https://developer.aiven.io/docs/products/kafka/kafka-connect/howto/s3-sink-connector-confluent>`__

* `Couchbase® <https://github.com/couchbase/kafka-connect-couchbase>`__

* :doc:`OpenSearch® </docs/products/kafka/kafka-connect/howto/opensearch-sink>`

* :doc:`Elasticsearch </docs/products/kafka/kafka-connect/howto/elasticsearch-sink>`

* `Google BigQuery <https://github.com/confluentinc/kafka-connect-bigquery>`__

* `Google Cloud Pub/Sub <https://github.com/GoogleCloudPlatform/pubsub/>`__

* `Google Cloud Pub/Sub Lite <https://github.com/GoogleCloudPlatform/pubsub/>`_

* :doc:`Google Cloud Storage </docs/products/kafka/kafka-connect/howto/gcs-sink>`

* `HTTP <https://github.com/aiven/http-connector-for-apache-kafka>`__ |preview|

* `JDBC <https://github.com/aiven/jdbc-connector-for-apache-kafka/blob/master/docs/sink-connector.md>`__

* `Official MongoDB® <https://docs.mongodb.com/kafka-connector/current/>`__

* `OpenSearch® <https://github.com/aiven/opensearch-connector-for-apache-kafka/blob/main/docs/opensearch-sink-connector-config-options.rst>`_ |preview|

* `Snowflake <https://docs.snowflake.net/manuals/user-guide/kafka-connector.html>`__ |preview|

* `Splunk <https://github.com/splunk/kafka-connect-splunk>`__

* `Stream Reactor Cassandra® <https://docs.lenses.io/connectors/sink/cassandra.html>`__

* `Stream Reactor InfluxDB® <https://docs.lenses.io/connectors/sink/influx.html>`__

* `Stream Reactor MongoDB® <https://docs.lenses.io/connectors/sink/mongo.html>`__

* `Stream Reactor MQTT <https://docs.lenses.io/connectors/sink/mqtt.html>`__

* `Stream Reactor Redis®* <https://docs.lenses.io/connectors/sink/redis.html>`__


Preview connectors
------------------

.. image:: /images/products/kafka/kafka-connect/preview-kafka-connect-connectors.png
   :alt: Preview icon next to a OpenSearch Apache Kafka Connect connector

Some of the available connectors have the |preview| tag next to the name. **Preview connectors do not come under our SLA**, consider this before using them for production purposes. 
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



------

*Elasticsearch is a trademark of Elasticsearch B.V., registered in the U.S. and in other countries.*
*Couchbase is a trademark of Couchbase, Inc.*
