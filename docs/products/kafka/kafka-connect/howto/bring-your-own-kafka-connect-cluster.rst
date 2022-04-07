Bring your own Kafka connect cluster
====================================

Aiven provides Kafka connect cluster as a managed service in combination
with Aiven for Apache Kafka managed service. However, there are
circumstances where you may want to roll your own Connect cluster. This
help article shows the steps necessary to integrate your own connect
cluster with Aiven for Apache Kafka (and Schema registry). In this
example we create a JDBC sink connector to PostgreSQL database.

**Note:** As of version 3.0, Aiven for Apache Kafka no longer supports
Confluent Schema Registry. For more information, see `this article that
describes the replacement,
Karapace <https://help.aiven.io/en/articles/5651983>`__ .

As a prerequisite, the following information should be collected.

.. _following-aiven-kafka-and-postgresql-services-details-are-required-from-aiven-console-for-the-respective-service:

The following Aiven for Apache Kafka and PostgreSQL services' details are required from Aiven console for the respective service:
---------------------------------------------------------------------------------------------------------------------------------

| *KAFKA_HOST*
| *KAFKA_PORT*
| *SCHEMA_REGISTRY_PORT*
| *SCHEMA_REGISTRY_PW*
| *KAFKA_CONNECT_SERVICE_URI*
| *PG_SERVICE_URI*
| *PG_HOST*
| *PG_PORT*
| *PG_PW*

Setup the truststore and keystore:
----------------------------------

Create a :doc:`Java keystore and truststore <../../howto/keystore-truststore>` for the Aiven for Apache Kafka service.

Setup the Kafka service:
------------------------

#. Make sure that the advanced setting, ``kafka.auto_create_topics_enable`` is enabled. This can be set from
   the Overview tab for the Kafka service in the Aiven console.

#. Enable the Schema Registry from the Overview tab for the Kafka service

#. Create a topic named ``jdbc_sink``

Download Kafka Connect binaries:
--------------------------------

#. Download the latest Kafka release from https://kafka.apache.org/quickstart

#. Download the Aiven Kafka connect JDBC connector from https://github.com/aiven/jdbc-connector-for-apache-kafka/releases

#. Download the Avro Value Converter from https://www.confluent.io/hub/confluentinc/kafka-connect-avro-converter

Preparing Kafka connect software on a VM:
-----------------------------------------

Log in to your VM.

::

   cd $HOME

   # extract kafka
   tar -xzf kafka_2.13-VERSION.tgz

   cd kafka_2.13-VERSION
   mkdir -p /share/kafka/plugins
   cd kafka/plugins
   # extract aiven connect jdbc
   unzip jdbc-connector-for-apache-kafka-VERSION.zip
   # extract confluent kafka connect avro converter
   unzip confluentinc-kafka-connect-avro-converter-VERSION.zip

|
| Create a properties file, ``my-connect-distributed.properties`` , for Kafka connect.

::

   cd $HOME
   cd kafka_2.13-VERSION
   vi ./my-connect-distributed.properties

.. literalinclude:: /code/products/kafka/my-connect-distributed.properties

|
| **Import the Aiven project CA into the JVM's trust store.**

#. Download Aiven project CA - ca.pem.

Then transfer it to the VM. Execute the following steps on each VM
participating in the connect cluster:

::

   # Import the Aiven project CA into the JVM's trust store
   sudo su
   cd /tmp
   openssl x509 -in /path/ca.pem -inform pem -out ca.der -outform der
   keytool -v -printcert -file ca.der
   #
   cp $JAVA_HOME/jre/lib/security/cacerts $JAVA_HOME/jre/lib/security/cacerts.orig
   #
   keytool -importcert -alias startssl -keystore $JAVA_HOME/jre/lib/security/cacerts -storepass changeit -file ca.der
   #
   keytool -keystore $JAVA_HOME/jre/lib/security/cacerts -storepass changeit -list | grep startssl
   #
   exit

|
| **Start the cluster**

::

   cd $HOME
   cd kafka_2.13-VERSION
   ./bin/connect-distributed ./my-connect-distributed.properties

Create the JDBC sink connector ``json`` configuration ``jdbc-sink-pg.json``

::

   {
     "name": "jdbc-sink-pg",
     "config":
     {
     "connector.class": "io.aiven.connect.jdbc.JdbcSinkConnector",
     "connection.url":"jdbc:postgresql://PG_HOST:PG_PORT/defaultdb?user=avnadmin&password=PG_PW&ssl=true",
     "tasks.max":"1",
     "topics": "jdbc_sink",
     "auto.create": "true",
     "value.converter":"io.confluent.connect.avro.AvroConverter",
    "value.converter.schema.registry.url":"https://KAFKA_HOST:SCHEMA_REGISTRY_PORT",
     "value.converter.basic.auth.credentials.source":"USER_INFO",
     "value.converter.basic.auth.user.info":"avnadmin:SCHEMA_REGISTRY_PW"
     }
   }

Create the JDBC sink connector instance

::

   curl -s -H "Content-Type: application/json" -X POST -d @jdbc-sink-pg.json http://localhost:8083/connectors/ | jq .

Check the status of the JDBC sink connector instance

::

   # check the status
   curl localhost:8083/connectors/jdbc-sink-pg/status | jq

   # check running tasks
   curl localhost:8083/connectors/jdbc-sink-pg/tasks

Publish data to the ``jdbc_sink`` topic using ``kafka-avro-console-producer`` ``console-producer.properties``

::

   security.protocol=SSL
   ssl.truststore.location=/path/client.truststore.jks
   ssl.truststore.password=secret
   ssl.keystore.type=PKCS12
   ssl.keystore.location=/path/client.keystore.p12
   ssl.keystore.password=secret
   ssl.key.password=secret

::

   cd $HOME
   cd kafka_2.13-VERSION

   ./bin/kafka-avro-console-producer --broker-list KAFKA_HOST:KAFKA_PORT --topic jdbc_sink  --producer.config ./console-producer.properties --property schema.registry.url=https://KAFKA_HOST:SCHEMA_REGISTRY_PORT --property basic.auth.credentials.source=USER_INFO --property basic.auth.user.info=avnadmin:SCHEMA_REGISTRY_PW --property value.schema='{"type":"record","name":"myrecord","fields":[{"name":"id","type":"int"},{"name":"product","type":"string"},{"name":"quantity","type":"int"},{"name":"price","type":"float"}]}'

Data...

::

   {"id": 999, "product": "foo", "quantity": 100, "price": 50}

Login into PostgreSQL database and check for data.

::

   psql PG_SERVICE_URI

   psql> select * from jdbc_sink;

|
| *Got here by accident? Learn how Aiven simplifies working with Apache
  Kafka:*

-  `Managed Kafka as a Service <https://aiven.io/kafka>`__
