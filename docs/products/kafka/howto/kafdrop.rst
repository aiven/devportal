Use Kafdrop Web UI with Aiven for Apache Kafka®
===============================================

`Kafdrop <https://github.com/obsidiandynamics/kafdrop>`_ is a popular Web UI for Apache Kafka that allows you to monitor a cluster, view topics and consumer groups with integration into the Schema Registry, with support for Avro, JSON and Protobuf.

Retrieve Aiven for Apache Kafka® SSL certificate files
------------------------------------------------------

Aiven for Apache Kafka® by default enables TLS security.
The certificates can be manually downloaded from the service overview page in the Aiven console, or via the :ref:`dedicated Aiven CLI command <avn_service_user_creds_download>`.

Setup a Kafdrop configuration file
----------------------------------

Kafdrop supports both :doc:`SASL and SSL authentication methods<../concepts/auth-types>`. The following example shows the SSL version which requires a keystore and truststore that can be created following the :doc:`dedicated documentation <keystore-truststore>`.

Once the keystore and truststore are created, you can define a Kafdrop configuration file named ``kafdrop.properties`` with the following content, replacing the ``KEYSTORE_PWD`` and ``TRUSTSTORE_PWD`` with the keystore and truststore passwords respectively:

::

    security.protocol=SSL
    ssl.keystore.password=KEYSTORE_PWD
    ssl.keystore.type=PKCS12
    ssl.truststore.password=TRUSTSTORE_PWD

Run Kafdrop on Docker
---------------------

You can run Kafdrop in a Docker/Podman container with the following command, by replacing the ``KAFKA_SERVICE_URI`` with the Aiven for Apache Kafka® service URI available in the service Overview tab of the Aiven console, and the ``client.truststore.jks`` and ``client.keystore.p12`` with the keystores and truststores file names:

::

    docker run -p 9000:9000                                                 \
        -e KAFKA_BROKERCONNECT=KAFKA_SERVICE_URI                            \
        -e KAFKA_PROPERTIES="$(cat kafdrop.properties | base64)"            \
        -e KAFKA_TRUSTSTORE="$(cat client.truststore.jks | base64)"         \
        -e KAFKA_KEYSTORE="$(cat client.keystore.p12 | base64)"             \
        obsidiandynamics/kafdrop

If you're also interested in Kafdrop to de-serialize Avro messages using `Karapace <https://github.com/aiven/karapace>`_ schema registry, add the following two lines to the ``docker run`` command:

::

    -e SCHEMAREGISTRY_AUTH="avnadmin:SCHEMA_REGISTRY_PWD"   \
    -e SCHEMAREGISTRY_CONNECT="https://SCHEMA_REGISTRY_URI" \

Replace, in the above, the ``SCHEMA_REGISTRY_PWD`` with the schema registry password and ``SCHEMA_REGISTRY_URI`` with the schema registry URI that you can find in the `Aiven console <https://console.aiven.io/>`_ service Overview page.

Use Kafdrop
-----------

Once Kafdrop starts, you should be able to access it at ``localhost:9000``

.. image:: /images/products/kafka/kafdrop.gif
   :alt: Kafdrop in action

You can perform the following tasks with Kafdrop over an Aiven for Apache Kafka® service:

* View and search topics
* Create and delete topics
* View brokers
* view messages
