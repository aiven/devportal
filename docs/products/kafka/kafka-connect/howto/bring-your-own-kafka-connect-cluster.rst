Bring your own Apache Kafka® Connect cluster
============================================

Aiven provides Apache Kafka® Connect as a managed service in combination with the Aiven for Apache Kafka® managed service. However, there are circumstances where you may want to roll your own Kafka Connect cluster.

The following article defines the necessary steps to integrate your own Apache Kafka Connect cluster with Aiven for Apache Kafka and use the schema registry offered by `Karapace <https://help.aiven.io/en/articles/5651983>`__. The example shows how to create a JDBC sink connector to a PostgreSQL® database.

.. _bring_your_own_kafka_connect_prereq:

Prerequisites
-------------

To bring your own Apache Kafka Connector, you need an Aiven for Apache Kafka service up and running. 

Furthermore, for the JDBC sink connector database example, you need to collect the following information about the Aiven for Apache Kafka service and the target database upfront:

* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service
* ``APACHE_KAFKA_PORT``: The port of the Apache Kafka service
* ``REST_API_PORT``: The Apache Kafka's REST API port, only needed when testing data flow with REST APIs
* ``REST_API_USERNAME``: The Apache Kafka's REST API username, only needed when testing data flow with REST APIs
* ``REST_API_PASSWORD``: The Apache Kafka's REST API password, only needed when testing data flow with REST APIs
* ``SCHEMA_REGISTRY_PORT``: The Apache Kafka's schema registry port, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_USER``: The Apache Kafka's schema registry username, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PASSWORD``: The Apache Kafka's schema registry user password, only needed when using Avro as data format
* ``PG_HOST``: The PostgreSQL service hostname
* ``PG_PORT``: The PostgreSQL service port
* ``PG_USERNAME``: The PostgreSQL service username
* ``PG_PASSWORD``: The PostgreSQL service password
* ``PG_DATABASE_NAME``: The PostgreSQL service database name

.. Note::

    If you're using Aiven for PostgreSQL and Aiven for Apache Kafka the above details are available in the `Aiven console <https://console.aiven.io/>`_ service Overview tab or via the dedicated ``avn service get`` command with the :ref:`Aiven CLI <avn_service_get>`.


Attach your own Apache Kafka Connect cluster to Aiven for Apache Kafka®
-----------------------------------------------------------------------

The following example demonstrates how to setup a local Apache Kafka Connect cluster with a working JDBC sink connector and attach it to an Aiven for Apache Kafka service.

.. _setup_trustore_keystore_bring_your_own_connect:

Setup the truststore and keystore
''''''''''''''''''''''''''''''''''

Create a :doc:`Java keystore and truststore <../../howto/keystore-truststore>` for the Aiven for Apache Kafka service.
For the following example we assume:

* The keystore is available at ``KEYSTORE_PATH/client.keystore.p12``
* The truststore is available at ``TRUSTSTORE_PATH/client.truststore.jks``
* For simplicity, the same secret (password) is used for both the keystore and the truststore, and is shown here as ``KEY_TRUST_SECRET``

Configure the Aiven for Apache Kafka service
''''''''''''''''''''''''''''''''''''''''''''

You need to enable the schema registry features offered by `Karapace <https://help.aiven.io/en/articles/5651983>`__. You can do it in the `Aiven Console <https://console.aiven.io/>`_ in the Aiven for Apache Kafka service Overview tab.

1. Enable the **Schema Registry (Karapace)** and **Apache Kafka REST API (Karapace)**

2. In the **Topic** tab, create a new topic called ``jdbc_sink``, the topic will be used by the Apache Kafka Connect connector


Download the required binaries
''''''''''''''''''''''''''''''

The following binaries are needed to setup a Apache Kafka Connect cluster locally:

* `Apache Kafka <https://kafka.apache.org/quickstart>`_
* `Aiven for Kafka connect JDBC connector <https://github.com/aiven/jdbc-connector-for-apache-kafka/releases>`_
* If you are going to use Avro as the data format, `Avro Value Converter <https://www.confluent.io/hub/confluentinc/kafka-connect-avro-converter>`_. The examples below show how to do this.

Setup the local Apache Kafka Connect cluster
''''''''''''''''''''''''''''''''''''''''''''

The following process defines the setup required to create a local Apache Kafka Connect cluster. The example shows the steps needed with the Apache Kafka ``3.1.0``, Avro converter ``7.1.0`` and JDBC connector ``6.7.0`` versions:

1. Extract the Apache Kafka binaries

   .. code-block:: shell

      tar -xzf kafka_2.13-3.1.0.tgz

2. Within the newly created ``kafka_2.13-3.1.0`` folder, create a ``plugins`` folder containing a ``lib`` sub-folder

   .. code-block:: shell

      cd kafka_2.13-3.1.0
      mkdir -p plugins/lib


3. Unzip the JDBC and Avro binaries and copy the ``jar`` files in the ``plugins/lib`` folder

   .. code-block:: shell

      # extract aiven connect jdbc
      unzip jdbc-connector-for-apache-kafka-6.7.0.zip
      # extract confluent kafka connect avro converter
      unzip confluentinc-kafka-connect-avro-converter-7.1.0.zip
      # copying plugins in the plugins/lib folder
      cp jdbc-connector-for-apache-kafka-6.7.0/*.jar plugins/lib/
      cp confluentinc-kafka-connect-avro-converter-7.1.0/*.jar plugins/lib/

3. Create a properties file, ``my-connect-distributed.properties``, under the main ``kafka_2.13-3.1.0`` folder, for the Apache Kafka Connect settings. Change the following placeholders:

   * ``PATH_TO_KAFKA_HOME`` to the path to the ``kafka_2.13-3.1.0`` folder
   * ``APACHE_KAFKA_HOST``, ``APACHE_KAFKA_PORT``, ``SCHEMA_REGISTRY_PORT``, ``SCHEMA_REGISTRY_USER``, ``SCHEMA_REGISTRY_PASSWORD``, to the related parameters fetched in the :ref:`prerequisite step <bring_your_own_kafka_connect_prereq>`
   * ``KEYSTORE_PATH``, ``TRUSTSTORE_PATH`` and ``KEY_TRUST_SECRET`` to the keystore, truststore location and related secret as defined in the :ref:`related step <setup_trustore_keystore_bring_your_own_connect>`

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
               "connection.url": "jdbc:postgresql://PG_HOST:PG_PORT/PG_DATABASE_NAME?user=PG_USERNAME&password=PG_PASSWORD&ssl=required",
               "tasks.max": "1",
               "topics": "jdbc_sink",
               "auto.create": "true",
               "value.converter": "io.confluent.connect.avro.AvroConverter",
               "value.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
               "value.converter.basic.auth.credentials.source": "USER_INFO",
               "value.converter.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD"
         }
      }

2. Create the JDBC sink connector instance using Kafka Connect REST APIs

   .. code-block:: shell

      curl -s -H "Content-Type: application/json" -X POST \
         -d @jdbc-sink-pg.json                            \
         http://localhost:8083/connectors/

3. Check the status of the JDBC sink connector instance, ``jq`` is used to beautify the output

   .. code-block:: shell

      curl localhost:8083/connectors/jdbc-sink-pg/status | jq

   The result should be similar to the following

   .. code-block:: json

      {
         "name": "jdbc-sink-pg",
         "connector": {
            "state": "RUNNING",
            "worker_id": "10.128.0.12:8083"
         },
         "tasks": [
            {
               "id": 0,
               "state": "RUNNING",
               "worker_id": "10.128.0.12:8083"
            }
         ],
         "type": "sink"
      }


Verify the JDBC connector using Karapace REST APIs
''''''''''''''''''''''''''''''''''''''''''''''''''

To verify that the connector is working, you can write messages to the ``jdbc_sink`` topic in Avro format using `Karapace REST APIs <https://github.com/aiven/karapace>`_, by following the steps below:

1. Create a new **Avro schema** using the ``/subjects/`` endpoint, after changing the placeholders for ``REST_API_USER``, ``REST_API_PASSWORD``, ``APACHE_KAFKA_HOST``, ``REST_API_PORT``

   .. code-block:: shell

      curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" \
         --data '''
            {"schema":
               "{\"type\": \"record\",\"name\": \"jdbcsinkexample\",\"namespace\": \"example\",\"doc\": \"example\",\"fields\": [{ \"type\": \"string\", \"name\": \"name\", \"doc\": \"person name\", \"namespace\": \"example\", \"default\": \"mario\"},{ \"type\": \"int\", \"name\": \"age\", \"doc\": \"persons age\", \"namespace\": \"example\", \"default\": 5}]}"
            }''' \
         https://REST_API_USER:REST_API_PASSWORD@APACHE_KAFKA_HOST:REST_API_PORT/subjects/jdbcsinkexample/versions/

   The above call creates a new schema called ``jdbcsinkexample`` with a schema containing two fields (``name`` and ``age``).

2. Create a new **message** in the ``jdbc_sink`` topic using the ``jdbcsinkexample`` schema, after changing the placeholders for ``REST_API_USER``, ``REST_API_PASSWORD``, ``APACHE_KAFKA_HOST``, ``REST_API_PORT``

   .. code-block:: shell

      curl -H "Content-Type: application/vnd.kafka.avro.v2+json" -X POST \
         -d '''
            {"value_schema":
               "{\"namespace\": \"test\", \"type\": \"record\", \"name\": \"example\", \"fields\": [{\"name\": \"name\", \"type\": \"string\"},{\"name\": \"age\", \"type\": \"int\"}]}",
            "records": [{"value": {"name": "Eric","age":77}}]}'''   \
         https://REST_API_USER:REST_API_PASSWORD@APACHE_KAFKA_HOST:REST_API_PORT/topics/jdbc_sink

3. Verify the presence of a table called ``jdbc_sink`` in PostgreSQL containing the row with name ``Eric`` and age ``77``
