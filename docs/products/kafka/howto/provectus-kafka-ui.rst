Use Provectus® UI for Apache Kafka® with Aiven for Apache Kafka®
================================================================

`Provectus® UI for Apache Kafka® <https://github.com/provectus/kafka-ui>`_ is a popular Open-Source web GUI for Apache Kafka® management that allows you to monitor and manage Apache Kafka® clusters.

Retrieve Aiven for Apache Kafka® SSL certificate files
------------------------------------------------------

Aiven for Apache Kafka® by default enables TLS security.
The certificates can be manually downloaded from the service overview page in the Aiven console, or via the :ref:`dedicated Aiven CLI command <avn_service_user_creds_download>`.

Run Provectus® UI for Apache Kafka® on Docker or Podman
-------------------------------------------------------

Since container for Provectus® UI for Apache Kafka® uses non-root user, to avoid permission problems, while keeping the secrets safe, perform the following steps (see example commands below):

1. Create separate directory for secrets.
2. Restrict the directory to current user.
3. Copy secrets there (replace the ``client.truststore.jks`` and ``client.keystore.p12`` with the keystores and truststores file names).
4. Give read permissions for secret files for everyone.
5. Change the directory.

::

    mkdir kafka-secrets  # Step 1
    chmod 700 kafka-secrets  # Step 2
    cp client.truststore.jks client.keystore.p12 kafka-secrets  # Step 3
    chmod +r kafka-secrets/*  # Step 4
    cd kafka-secrets  # Step 5

You can run Provectus® UI for Apache Kafka® in a Docker/Podman container with the following command, by replacing the ``KAFKA_SERVICE_URI`` with the Aiven for Apache Kafka® service URI available in the service Overview tab of the Aiven console, ``KEYSTORE_PWD`` and ``TRUSTSTORE_PWD`` with the keystore and truststore passwords respectively, and the ``client.truststore.jks`` and ``client.keystore.p12`` with the keystores and truststores file names:

::

    docker run -p 8080:8080 \
        -v (pwd)/client.truststore.jks:/client.truststore.jks \
        -v (pwd)/client.keystore.p12:/client.keystore.p12 \
        -e KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS=KAFKA_SERVICE_URI \
        -e KAFKA_CLUSTERS_0_PROPERTIES_SECURITY_PROTOCOL=SSL \
        -e KAFKA_CLUSTERS_0_PROPERTIES_SSL_TRUSTSTORE_LOCATION=/client.truststore.jks \
        -e KAFKA_CLUSTERS_0_PROPERTIES_SSL_TRUSTSTORE_PASSWORD=TRUSTSTORE_PWD \
        -e KAFKA_CLUSTERS_0_PROPERTIES_SSL_KEYSTORE_LOCATION=/client.keystore.p12 \
        -e KAFKA_CLUSTERS_0_PROPERTIES_SSL_KEYSTORE_PASSWORD=KEYSTORE_PWD \
        -e KAFKA_CLUSTERS_0_PROPERTIES_SSL_KEYSTORE_TYPE=PKCS12 \
        -d provectuslabs/kafka-ui:latest

Use Provectus® UI for Apache Kafka®
-----------------------------------

Once Provectus® UI for Apache Kafka® starts, you should be able to access it at ``localhost:8080``.