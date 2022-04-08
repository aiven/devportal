Bring your own Apache Kafka® Connect cluster
============================================

Aiven provides Apache Kafka® Connect cluster as a managed service in combination with Aiven for Apache Kafka managed service. However, there are
circumstances where you may want to roll your own Kafka Connect cluster. The following article defines the necessary steps to integrate your own Apache Kafka Connect cluster with Aiven for Apache Kafka® and use schema registry offered by `Karapace <https://help.aiven.io/en/articles/5651983>`__. The example shows how to create a JDBC sink connector to a PostgreSQL® database.

.. _bring_your_own_kafka_connect_prereq:

Prerequisites
-------------

To bring your own Apache Kafka Connector, you need an Aiven for Apache Kafka service up and running. 

Furthermore, for the JDBC sink connector database example, you need to collect the following information about the Aiven for Apache Kafka service and the target database upfront:

* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service
* ``APACHE_KAFKA_PORT``: The port of the Apache Kafka service
* ``SCHEMA_REGISTRY_PORT``: The Apache Kafka's schema registry port, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_USER``: The Apache Kafka's schema registry username, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PASSWORD``: The Apache Kafka's schema registry user password, only needed when using Avro as data format
* ``PG_HOST``: The PostgreSQL service hostname
* ``PG_PORT``: The PostgreSQL service port
* ``PG_USERNAME``: The PostgreSQL service username
* ``PG_PASSWORD``: The PostgreSQL service password
* ``PG_DATABASE_NAME``: The PostgreSQL serrvice database name

.. Note::

    If you're using Aiven for PostgreSQL and Aiven for Apache Kafka the above details are available in the `Aiven console <https://console.aiven.io/>`_ service Overview tab or via the dedicated ``avn service get`` command with the :ref:`Aiven CLI <avn_service_get>`.


Attach your own Apache Kafka Connect cluster to Aiven for Apache Kafka
----------------------------------------------------------------------

The following example demonstrates how to setup a local Apache Kafka Connect cluster with a working JDBC sink connector and attach it to an Aiven for Apache Kafka service.

.. _setup_trustore_keystore_bring_your_own_connect:

Setup the truststore and keystore
''''''''''''''''''''''''''''''''''

Create a :doc:`Java keystore and truststore <../../howto/keystore-truststore>` for the Aiven for Apache Kafka service.
For the following example we assume:

* the keystore is available at ``KEYSTORE_PATH/client.keystore.p12``
* the truststore is available at ``TRUSTSTORE_PATH/client.truststore.jks``
* all the keystore and truststore secret is the same ``KEY_TRUST_SECRET``

Configure the Aiven for Apache Kafka service
''''''''''''''''''''''''''''''''''''''''''''

You need to enable the schema registry features offered by `Karapace <https://help.aiven.io/en/articles/5651983>`__. You can do it in the `Aiven Console <https://console.aiven.io/>`_ in the Aiven for Apache Kafka service overview tab.

1. Enable the **Schema Registry (Karapace)**

.. Tip::

   Enabling also **Apache Kafka REST API (Karapace)** allows you to browse messages in Aiven for Apache Kafka topics directly from the Aiven console.

2. In the **Topic** tab, create a new topic called ``jdbc_sink``, the topic will be used by the Apache Kafka Connect connector


Download the required binaries
''''''''''''''''''''''''''''''

The The Apache Kafka binaries are needed to setup a Apache Kafka Connect cluster locally:

* `Apache Kafka <https://kafka.apache.org/quickstart>`_
* `Aiven Kafka connect JDBC connector <https://github.com/aiven/jdbc-connector-for-apache-kafka/releases>`_
* `Avro Value Converter <https://www.confluent.io/hub/confluentinc/kafka-connect-avro-converter>`_

Setup the local Apache Kafka Connect cluster
''''''''''''''''''''''''''''''''''''''''''''

The following process defines the setup required to create a local Apache Kafka Connect cluster, the example shows the steps needed with the Apache Kafka ``3.1.0``, Avro converter ``7.1.0`` and JDBC connector ``6.7.0`` versions:

1. Extract the Apache Kafka binaries

.. code-block:: shell

   tar -xzf kafka_2.13-3.1.0.tgz

2. create a ``plugins`` folder and unzip the JDBC and avro binaries

.. code-block:: shell

   cd kafka_2.13-3.1.0
   mkdir -p plugins
   cd plugins
   # extract aiven connect jdbc
   unzip jdbc-connector-for-apache-kafka-6.7.0.zip
   # extract confluent kafka connect avro converter
   unzip confluentinc-kafka-connect-avro-converter-7.1.0.zip

3. Create a properties file, ``my-connect-distributed.properties``, under the main ``kafka_2.13-3.1.0`` folder for the Apache Kafka Connect settings. Change the following placeholders:
   * ``PATH_TO_KAFKA_HOME`` with the path to the ``kafka_2.13-3.1.0`` folder
   * ``APACHE_KAFKA_HOST``, ``APACHE_KAFKA_PORT``, ``SCHEMA_REGISTRY_PORT``, ``SCHEMA_REGISTRY_USER``, ``SCHEMA_REGISTRY_PASSWORD``, with the related parameters fetched in the :ref:`prerequisite step <bring_your_own_kafka_connect_prereq>`
   * ``KEYSTORE_PATH``, ``TRUSTSTORE_PATH`` and ``KEY_TRUST_SECRET`` with the keystore, truststore location and related secret as defined in the :ref:`related step <setup_trustore_keystore_bring_your_own_connect>`

.. literalinclude:: /code/products/kafka/my-connect-distributed.properties
    :language: properties

4. Start the local Apache Kafka Connect cluster, executing the following from the ``kafka_2.13-3.1.0`` folder: 

.. code-block:: shell

   ./bin/connect-distributed.sh ./my-connect-distributed.properties

Add the JDBC sink connector
'''''''''''''''''''''''''''

The following steps define how you can add a JDBC connector to the local Apache Kafka Connect cluster:

1. Create the JDBC sink connector JSON configuration file named ``jdbc-sink-pg.json`` with the following content, replacing the placeholders ``PG_HOST``, ``PG_PORT``, ``PG_USERNAME``, ``PG_PASSWORD``, ``PG_DATABASE_NAME``, ``APACHE_KAFKA_HOST``, ``SCHEMA_REGISTRY_PORT``, ``SCHEMA_REGISTRY_USER``, ``SCHEMA_REGISTRY_PASSWORD``.

.. code-block:: json

    {
        "name": "jdbc-sink-pg",
        "config": {
            "connector.class": "io.aiven.connect.jdbc.JdbcSinkConnector",
            "connection.url": "jdbc:postgresql://PG_HOST:PG_PORT/PG_DATABASE_NAME?user=PG_USERNAME&password=PG_PASSWORD&ssl=true",
            "tasks.max": "1",
            "topics": "jdbc_sink",
            "auto.create": "true",
            "value.converter": "io.confluent.connect.avro.AvroConverter",
            "value.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
            "value.converter.basic.auth.credentials.source": "USER_INFO",
            "value.converter.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD"
        }
    }

6. Create the JDBC sink connector instance using Kafka Connect REST APIs

.. code-block:: shell

   curl -s -H "Content-Type: application/json" -X POST -d @jdbc-sink-pg.json http://localhost:8083/connectors/ | jq .

7. Check the status of the JDBC sink connector instance

.. code-block:: shell

   # check the status
   curl localhost:8083/connectors/jdbc-sink-pg/status | jq

   # check running tasks
   curl localhost:8083/connectors/jdbc-sink-pg/tasks

8. Publish data to the ``jdbc_sink`` topic using ``kafka-avro-console-producer`` ``console-producer.properties``

.. code-block:: properties

   security.protocol=SSL
   ssl.truststore.location=/path/client.truststore.jks
   ssl.truststore.password=secret
   ssl.keystore.type=PKCS12
   ssl.keystore.location=/path/client.keystore.p12
   ssl.keystore.password=secret
   ssl.key.password=secret

.. code-block:: shell

   cd $HOME
   cd kafka_2.13-VERSION

   ./bin/kafka-avro-console-producer --broker-list KAFKA_HOST:KAFKA_PORT --topic jdbc_sink  --producer.config ./console-producer.properties --property schema.registry.url=https://KAFKA_HOST:SCHEMA_REGISTRY_PORT --property basic.auth.credentials.source=USER_INFO --property basic.auth.user.info=avnadmin:SCHEMA_REGISTRY_PW --property value.schema='{"type":"record","name":"myrecord","fields":[{"name":"id","type":"int"},{"name":"product","type":"string"},{"name":"quantity","type":"int"},{"name":"price","type":"float"}]}'

Data...

.. code-block:: json

   {"id": 999, "product": "foo", "quantity": 100, "price": 50}

9. Login into PostgreSQL database and check for data.

.. code-block:: shell

   psql PG_SERVICE_URI

   psql> select * from jdbc_sink;

|
| *Got here by accident? Learn how Aiven simplifies working with Apache
  Kafka:*

-  `Managed Kafka as a Service <https://aiven.io/kafka>`__
