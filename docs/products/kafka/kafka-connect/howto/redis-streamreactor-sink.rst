Create a Redis®* stream reactor sink connector by Lenses.io
===========================================================

**The Redis stream reactor sink connector** enables you to move data from **an Aiven for Apache Kafka® cluster** to **a Redis®* database**. The Lenses.io implementation enables you to write `KCQL transformations <https://docs.lenses.io/connectors/sink/redis.html>`_ on the topic data before sending it to the Redis database.


.. _connect_redis_lenses_sink_prereq:

Prerequisites
-------------

To setup a Redis sink connector, you need an Aiven for Apache Kafka service :doc:`with Kafka Connect enabled <enable-connect>` or a :ref:`dedicated Aiven for Apache Kafka Connect cluster <apache_kafka_connect_dedicated_cluster>`.

Furthermore you need to collect the following information about the target Redis database upfront:

* ``REDIS_HOSTNAME``: The Redis hostname
* ``REDIS_PORT``: The Redis port
* ``REDIS_PASSWORD``: The Redis password
* ``REDIS_SSL``: The Redis SSL setting, should be ``true`` or ``false``
* ``TOPIC_LIST``: The list of topics to sink divided by comma
* ``KCQL_TRANSFORMATION``: The KCQL syntax to parse the topic data, should be in the format:

  ::

    [INSERT INTO REDIS_CACHE]
    SELECT LIST_OF_FIELDS 
    FROM APACHE_KAFKA_TOPIC


* ``APACHE_KAFKA_HOST``: The hostname of the Apache Kafka service, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PORT``: The Apache Kafka's schema registry port, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_USER``: The Apache Kafka's schema registry username, only needed when using Avro as data format
* ``SCHEMA_REGISTRY_PASSWORD``: The Apache Kafka's schema registry user password, only needed when using Avro as data format


.. Note::

    If you're using Aiven for Redis and Aiven for Apache Kafka, the above details are available in the `Aiven console <https://console.aiven.io/>`_ service *Overview tab* or via the dedicated ``avn service get`` command with the :ref:`Aiven CLI <avn_service_get>`.

    The ``SCHEMA_REGISTRY`` related parameters are available in the Aiven for Apache Kafka® service page, *Overview* tab, and *Schema Registry* subtab

    As of version 3.0, Aiven for Apache Kafka no longer supports Confluent Schema Registry. For more information, read `the article describing the replacement, Karapace <https://help.aiven.io/en/articles/5651983>`_

Setup a Redis sink connector with Aiven Console
-----------------------------------------------

The following example demonstrates how to setup a Redis sink connector for Apache Kafka using the `Aiven Console <https://console.aiven.io/>`_.

Define a Kafka Connect configuration file
'''''''''''''''''''''''''''''''''''''''''

Define the connector configurations in a file (we'll refer to it with the name ``redis_sink.json``) with the following content, creating a file is not strictly necessary but allows to have all the information in one place before copy/pasting them in the `Aiven Console <https://console.aiven.io/>`_:

.. code-block:: json

    {
        "name":"CONNECTOR_NAME",
        "connector.class": "com.datamountaineer.streamreactor.connect.redis.sink.RedisSinkConnector",
        "topics": "TOPIC_LIST",
        "connect.redis.host": "REDIS_HOSTNAME",
        "connect.redis.port": "REDIS_PORT",
        "connect.redis.password": "REDIS_PASSWORD",
        "connect.redis.ssl.enabled": "REDIS_SSL",
        "connect.redis.kcql": "KCQL_TRANSFORMATION",
        "key.converter": "io.confluent.connect.avro.AvroConverter",
        "key.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "key.converter.basic.auth.credentials.source": "USER_INFO",
        "key.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD",
        "value.converter": "io.confluent.connect.avro.AvroConverter",
        "value.converter.schema.registry.url": "https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT",
        "value.converter.basic.auth.credentials.source": "USER_INFO",
        "value.converter.schema.registry.basic.auth.user.info": "SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD"
    }

The configuration file contains the following entries:

* ``name``: the connector name, replace ``CONNECTOR_NAME`` with the name you want to use for the connector.
* ``connect.redis.*``: sink parameters collected in the :ref:`prerequisite <connect_redis_lenses_sink_prereq>` phase. 

* ``key.converter`` and ``value.converter``:  defines the messages data format in the Apache Kafka topic. The ``io.confluent.connect.avro.AvroConverter`` converter translates messages from the Avro format. To retrieve the messages schema we use Aiven's `Karapace schema registry <https://github.com/aiven/karapace>`_ as specified by the ``schema.registry.url`` parameter and related credentials.

.. Note::

    The ``key.converter`` and ``value.converter`` sections define how the topic messages will be parsed and needs to be included in the connector configuration. 

    When using Avro as source data format, you need to set following parameters

    * ``value.converter.schema.registry.url``: pointing to the Aiven for Apache Kafka schema registry URL in the form of ``https://APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT`` with the ``APACHE_KAFKA_HOST`` and ``SCHEMA_REGISTRY_PORT`` parameters :ref:`retrieved in the previous step <connect_redis_lenses_sink_prereq>`.
    * ``value.converter.basic.auth.credentials.source``: to the value ``USER_INFO``, since you're going to login to the schema registry using username and password.
    * ``value.converter.schema.registry.basic.auth.user.info``: passing the required schema registry credentials in the form of ``SCHEMA_REGISTRY_USER:SCHEMA_REGISTRY_PASSWORD`` with the ``SCHEMA_REGISTRY_USER`` and ``SCHEMA_REGISTRY_PASSWORD`` parameters :ref:`retrieved in the previous step <connect_redis_lenses_sink_prereq>`. 


Create a Kafka Connect connector with the Aiven Console
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

To create the connector, access the `Aiven Console <https://console.aiven.io/>`_ and select the Aiven for Apache Kafka® or Aiven for Apache Kafka Connect® service where the connector needs to be defined, then:

1. Click on the **Connectors** tab
2. Clink on **Create New Connector**, the button is enabled only for services :doc:`with Kafka Connect enabled <enable-connect>`.
3. Select the **Stream Reactor Redis Sink**
4. Under the *Common* tab, locate the **Connector configuration** text box and click on **Edit**
5. Paste the connector configuration (stored in the ``redis_sink.json`` file) in the form
6. Click on **Apply**

.. Note::

    The Aiven Console parses the configuration file and fills the relevant UI fields. You can review the UI fields across the various tab and change them if necessary. The changes will be reflected in JSON format in the **Connector configuration** text box.

7. After all the settings are correctly configured, click on **Create new connector**
8. Verify the connector status under the **Connectors** tab
9. Verify the presence of the data in the target Redis service

.. Note::

    Connectors can be created also using the dedicated :ref:`Aiven CLI command <avn_service_connector_create>`.

Example: Create a Redis sink connector
-------------------------------------------------------

If you have a topic named ``students`` containing the following data that you want to move to Redis:

.. code-block::

    {"id":1, "name":"carlo", "age": 77}
    {"id":2, "name":"lucy", "age": 55}
    {"id":3, "name":"carlo", "age": 33}
    {"id":2, "name":"lucy", "age": 21}

You can sink the ``students`` topic to Redis with the following connector configuration, after replacing the placeholders for ``REDIS_HOST``, ``REDIS_PORT``, ``REDIS_DB_NAME``, ``REDIS_USERNAME`` and ``REDIS_PASSWORD``:

.. code-block:: json

    {
        "name": "my-redis-sink",
        "connector.class": "com.datamountaineer.streamreactor.connect.redis.sink.RedisSinkConnector",
        "connect.redis.host": "REDIS_HOSTNAME",
        "connect.redis.port": "REDIS_PORT",
        "connect.redis.password": "REDIS_PASSWORD",
        "connect.redis.ssl.enabled": "REDIS_SSL",
        "topics": "students",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "value.converter.schemas.enable": "false",
        "connect.redis.kcql": "INSERT INTO students- SELECT * FROM students PK id"    
    }

The configuration file contains the following peculiarities:

* ``"topics": "students"``: setting the topic to sink
* ``"connect.redis"``: the connection parameters placeholders
* ``"value.converter": "org.apache.kafka.connect.json.JsonConverter"`` and ``"value.converter.schemas.enable": "false"``: the topic value is in JSON format without a schema
* ``"connect.redis.kcql": "INSERT INTO students- SELECT * FROM students PK id"``: the connector logic is to insert every topic message as new entry in Redis, using the ``id`` field as key prefixed with ``students-`` (configured in the ``INSERT INTO`` statement).

Once the connector is created successfully, you should see the following three entries in the target Redis database.

::

    1) "students-1" containing "{\"name\":\"carlo\",\"id\":1,\"age\":77}"
    2) "students-2" containing "{\"name\":\"lucy\",\"id\":2,\"age\":21}"
    3) "students-3" containing "{\"name\":\"carlo\",\"id\":3,\"age\":33}"

There are only three keys in Redis since there were two messages in the topic sharing the ``"id": 2``, and the connector will overwrite entries sharing the same key.