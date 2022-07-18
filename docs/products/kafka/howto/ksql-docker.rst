Use ksqlDB with Aiven for Apache Kafka®
=======================================

Aiven provides a managed Apache Kafka® solution together with a number of auxiliary services like Apache Kafka Connect, Kafka REST and Schema Registry via `Karapace <https://github.com/aiven/karapace>`_. A managed `ksqlDB <https://ksqldb.io/>`_ service in Aiven is, however, not supported. if you want to define streaming data pipelines with SQL, you have two options:

* Use :doc:`Aiven for Apache Flink </docs/products/flink/index>` 
* Run a self-hosted ksqlDB cluster.


Prerequisites
-------------

To connect ksqlDB to Aiven for Apache Kafka® you need to create a :doc:`Java keystore and truststore containing the service SSL certificates <keystore-truststore>`. 

Furthermore, you need to collect the following information:

* ``APACHE_KAFKA_HOST``: The Aiven for Apache Kafka hostname
* ``APACHE_KAFKA_PORT``: The Aiven for Apache Kafka port
* ``SCHEMA_REGISTRY_PORT``: The Aiven for Apache Kafka schema registry port, if enabled
* ``SCHEMA_REGISTRY_PASSWORD``: The password associated to the ``avnadmin`` user for Schema Registry
* ``KEYSTORE_FILE_NAME``: The name of the Java keystore containing the Aiven for Apache Kafka SSL certificates
* ``TRUSTSTORE_FILE_NAME``: The name of the Java truststore containing the Aiven for Apache Kafka SSL certificates
* ``SSL_KEYSTORE_PASSWORD``: The password used to secure the Java keystore
* ``SSL_KEY_PASSWORD``: The password used to secure the Java key
* ``SSL_TRUSTSTORE_PASSWORD``: The password used to secure the Java truststore
* ``SSL_STORE_FOLDER``: The absolute path of the folder containing both the truststore and keystore
* ``TRUSTSTORE_SCHEMA_REGISTRY_FILE_NAME``: The name of the Java truststore containing the schema registry (`Karapace <https://karapace.io/>`__) certificate 
* ``TRUSTSTORE_SCHEMA_REGISTRY_PASSWORD``: The password used to secure the Java truststore for the schema registry (`Karapace <https://karapace.io/>`__)  certificate

Create a keystore for schema registry's ca file
'''''''''''''''''''''''''''''''''''''''''''''''

ksqlDB by default uses the ``ssl.truststore`` settings for the Schema Registry connection. 

To have ksqlDB working with Aiven's `Karapace <https://karapace.io/>`__ Schema Registry you need to explicitly define a truststore that contains the commonly trusted root CA of Schema Registry server. To create such a truststore:

1. Obtain the root CA of the server with the following ``openssl`` command by replacing the ``APACHE_KAFKA_HOST`` and ``SCHEMA_REGISTRY_PORT`` placeholders::

    openssl s_client -connect APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT \
        -showcerts < /dev/null 2>/dev/null | \
        awk '/BEGIN CERT/{s=1}; s{t=t "\n" $0};
            /END CERT/ {last=t; t=""; s=0}; END{print last}' \
        > ca_schema_registry.cert

2. Create the truststore with the following ``keytool`` command  by replacing the ``TRUSTSTORE_SCHEMA_REGISTRY_FILE_NAME`` and ``TRUSTSTORE_SCHEMA_REGISTRY_PASSWORD`` placeholder::

    keytool -import -file ca_schema_registry.cert \
        -alias CA \
        -keystore TRUSTSTORE_SCHEMA_REGISTRY_FILE_NAME \
        -storepass TRUSTSTORE_SCHEMA_REGISTRY_PASSWORD \
        -noprompt

.. Tip::

    The ``TRUSTSTORE_SCHEMA_REGISTRY_FILE_NAME`` can be any name with extension should be ``.jks``


Run ksqlDB on Docker
--------------------

You can run ksqlDB on Docker with the following command, by replacing the placeholders:

* ``SSL_STORE_FOLDER``
* ``APACHE_KAFKA_HOST``
* ``APACHE_KAFKA_PORT``
* ``KEYSTORE_FILE_NAME``
* ``SSL_KEYSTORE_PASSWORD``
* ``SSL_KEY_PASSWORD``
* ``TRUSTSTORE_FILE_NAME``
* ``SSL_TRUSTSTORE_PASSWORD``
* ``SCHEMA_REGISTRY_PORT``
* ``SCHEMA_REGISTRY_PASSWORD``
* ``TRUSTSTORE_SCHEMA_REGISTRY_FILE_NAME``
* ``TRUSTSTORE_SCHEMA_REGISTRY_PASSWORD``

::

    docker run -d --name ksql  \
        -v SSL_STORE_FOLDER/:/ssl_settings/ \
        -p 127.0.0.1:8088:8088 \
        -e KSQL_BOOTSTRAP_SERVERS=APACHE_KAFKA_HOST:APACHE_KAFKA_PORT \
        -e KSQL_LISTENERS=http://0.0.0.0:8088/ \
        -e KSQL_KSQL_SERVICE_ID=ksql_service_1_ \
        -e KSQL_OPTS="-Dsecurity.protocol=SSL
            -Dssl.keystore.type=PKCS12
            -Dssl.keystore.location=/ssl_settings/KEYSTORE_FILE_NAME
            -Dssl.keystore.password=SSL_KEYSTORE_PASSWORD
            -Dssl.key.password=SSL_KEY_PASSWORD
            -Dssl.truststore.type=JKS
            -Dssl.truststore.location=/ssl_settings/TRUSTSTORE_FILE_NAME
            -Dssl.truststore.password=SSL_TRUSTSTORE_PASSWORD
            -Dksql.schema.registry.url=APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT
            -Dksql.schema.registry.basic.auth.credentials.source=USER_INFO
            -Dksql.schema.registry.basic.auth.user.info=avnadmin:SCHEMA_REGISTRY_PASSWORD
            -Dksql.schema.registry.ssl.truststore.location=/ssl_settings/TRUSTSTORE_SCHEMA_REGISTRY_FILE_NAME
            -Dksql.schema.registry.ssl.truststore.password=TRUSTSTORE_SCHEMA_REGISTRY_PASSWORD" \
        confluentinc/ksqldb-server:0.23.1

.. Tip::

    ``USER_INFO`` is **not** a placeholder, but rather a literal that shouldn't be changed

.. Warning::

    Some docker setup has issues using mounting options ``-v``, in those cases copying the Keystore and Truststore in the container could be an easier option. This can be achieved with the following::

        docker container create --name ksql  \
            -p 127.0.0.1:8088:8088 \
            -e KSQL_BOOTSTRAP_SERVERS=APACHE_KAFKA_HOST:APACHE_KAFKA_PORT \
            -e KSQL_LISTENERS=http://0.0.0.0:8088/ \
            -e KSQL_KSQL_SERVICE_ID=ksql_service_1_ \
            -e KSQL_OPTS="-Dsecurity.protocol=SSL
                -Dssl.keystore.type=PKCS12
                -Dssl.keystore.location=/home/appuser/KEYSTORE_FILE_NAME
                -Dssl.keystore.password=SSL_KEYSTORE_PASSWORD
                -Dssl.key.password=SSL_KEY_PASSWORD
                -Dssl.truststore.type=JKS
                -Dssl.truststore.location=/home/appuser/TRUSTSTORE_FILE_NAME
                -Dssl.truststore.password=SSL_TRUSTSTORE_PASSWORD
                -Dksql.schema.registry.url=APACHE_KAFKA_HOST:SCHEMA_REGISTRY_PORT
                -Dksql.schema.registry.basic.auth.credentials.source=USER_INFO
                -Dksql.schema.registry.basic.auth.user.info=avnadmin:SCHEMA_REGISTRY_PASSWORD
                -Dksql.schema.registry.ssl.truststore.location=/home/appuser/TRUSTSTORE_SCHEMA_REGISTRY_FILE_NAME
                -Dksql.schema.registry.ssl.truststore.password=TRUSTSTORE_SCHEMA_REGISTRY_PASSWORD" \
            confluentinc/ksqldb-server:0.23.1
        docker cp KEYSTORE_FILE_NAME ksql:/home/appuser/
        docker cp TRUSTSTORE_FILE_NAME ksql:/home/appuser/
        docker cp TRUSTSTORE_SCHEMA_REGISTRY_FILE_NAME ksql:/home/appuser/
        docker start ksql



Once the Docker image is up and running you should be able to access ksqlDB's at ``localhost:8088`` or connect via terminal with the following command::

    docker exec -it ksql ksql