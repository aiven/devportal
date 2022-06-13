Use Provectus® UI for Apache Kafka® with Aiven for Apache Kafka®
================================================================

`Provectus® UI for Apache Kafka® <https://github.com/provectus/kafka-ui>`_ is a popular Open-Source web GUI for Apache Kafka® management that allows you to monitor and manage Apache Kafka® clusters.

Prerequisites
-------------

To connect Provectus® UI for Apache Kafka® to Aiven for Apache Kafka® you need to create a :doc:`Java keystore and truststore containing the service SSL certificates <keystore-truststore>`. 

Furthermore, you need to collect the following information:

* ``APACHE_KAFKA_HOST``: The Aiven for Apache Kafka hostname
* ``APACHE_KAFKA_PORT``: The Aiven for Apache Kafka port
* ``SSL_KEYSTORE_FILE_NAME``: The name of the Java keystore containing the Aiven for Apache Kafka SSL certificates
* ``SSL_TRUSTSTORE_FILE_NAME``: The name of the Java truststore containing the Aiven for Apache Kafka SSL certificates
* ``SSL_KEYSTORE_PASSWORD``: The password used to secure the Java keystore
* ``SSL_TRUSTSTORE_PASSWORD``: The password used to secure the Java truststore
* ``SSL_STORE_FOLDER``: The absolute path of the folder containing both the truststore and keystore


Run Provectus® UI for Apache Kafka® on Docker or Podman
-------------------------------------------------------


Share keystores with non-root user
''''''''''''''''''''''''''''''''''

Since container for Provectus® UI for Apache Kafka® uses non-root user, to avoid permission problems, while keeping the secrets safe, perform the following steps (see example commands below):

1. Create separate directory for secrets::

    mkdir SSL_STORE_FOLDER

2. Restrict the directory to current user::

    chmod 700 SSL_STORE_FOLDER

3. Copy secrets there (replace the ``SSL_KEYSTORE_FILE_NAME`` and ``SSL_TRUSTSTORE_FILE_NAME`` with the keystores and truststores file names)::

    cp SSL_KEYSTORE_FILE_NAME SSL_TRUSTSTORE_FILE_NAME SSL_STORE_FOLDER

4. Give read permissions for secret files for everyone::

    chmod +r SSL_STORE_FOLDER/*


Execute Provectus® UI for Apache Kafka® on Docker or Podman
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

You can run Provectus® UI for Apache Kafka® in a Docker/Podman container with the following command, by replacing the placeholders for:

* ``APACHE_KAFKA_HOST``
* ``APACHE_KAFKA_PORT`` 
* ``SSL_STORE_FOLDER``
* ``SSL_KEYSTORE_FILE_NAME``
* ``SSL_KEYSTORE_PASSWORD``
* ``SSL_TRUSTSTORE_FILE_NAME``
* ``SSL_TRUSTSTORE_PASSWORD``


::

    docker run -p 8080:8080 \
        -v SSL_STORE_FOLDER/SSL_TRUSTSTORE_FILE_NAME:/client.truststore.jks:ro \
        -v SSL_STORE_FOLDER/SSL_KEYSTORE_FILE_NAME:/client.keystore.p12:ro \
        -e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=APACHE_KAFKA_HOST:APACHE_KAFKA_PORT \
        -e KAFKA_CLUSTERS_0_PROPERTIES_SECURITY_PROTOCOL=SSL \
        -e KAFKA_CLUSTERS_0_PROPERTIES_SSL_TRUSTSTORE_LOCATION=/client.truststore.jks \
        -e KAFKA_CLUSTERS_0_PROPERTIES_SSL_TRUSTSTORE_PASSWORD=SSL_TRUSTSTORE_PASSWORD \
        -e KAFKA_CLUSTERS_0_PROPERTIES_SSL_KEYSTORE_LOCATION=/client.keystore.p12 \
        -e KAFKA_CLUSTERS_0_PROPERTIES_SSL_KEYSTORE_PASSWORD=SSL_KEYSTORE_PASSWORD \
        -e KAFKA_CLUSTERS_0_PROPERTIES_SSL_KEYSTORE_TYPE=PKCS12 \
        -d provectuslabs/kafka-ui:latest

Use Provectus® UI for Apache Kafka®
-----------------------------------

Once Provectus® UI for Apache Kafka® starts, you should be able to access it at ``localhost:8080``.

.. image:: /images/products/kafka/provectus-ui.jpg
   :alt: Provectus in action