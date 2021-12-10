Configuring Java SSL to access Apache Kafka
=================================================

Aiven for Apache Kafka utilises TLS (SSL) to secure the traffic between its services and client applications. This means that clients must be configured with the
right tools to be able to communicate with the Aiven services.

Keystores and truststores are password-protected files accessible by the client that interacts with the service. 
To create these files:

1. Log into the `Aiven web console <https://console.aiven.io/>`_ and select your Aiven for Apache Kafka service.

2. Download the **Access Key**, **Access Certificate** and **CA Certificate**. The resulting ``service.key``, ``service.cert`` and ``ca.pem`` are going to be used in the following steps.

.. image:: /images/products/kafka/ssl-certificates-download.png
    :alt: Download the Access Key, Access Certificate and CA Certificate from the Aiven console  

3. Use the ``openssl`` utility to create the keystore with the ``service.key`` and
   ``service.cert`` files downloaded previously:

::

    openssl pkcs12 -export       \
        -inkey service.key       \
        -in service.cert         \
        -out client.keystore.p12 \
        -name service_key

.. Note::
    The format has to be ``PKCS12`` , which is the default since Java 9.

5. Enter a password to protect the keystore and the key, when prompted

6. In the folder where the certificates are stored, use the ``keytool`` utility to create the truststore with the ``ca.pem`` file as input:

::
    
    keytool -import  \
        -file ca.pem \
        -alias CA    \
        -keystore client.truststore.jks

7. Enter a password to protect the truststores, when prompted

8. Reply to `yes` to confirm trusting the CA certificate, when prompted

The result are the keystore named ``client.keystore.p12`` and truststore named ``client.truststore.jks`` that can be used for client applications configuration.

.. Tip::

    You can use :doc:`Aiven CLI </docs/tools/cli>` ``avn service user-kafka-java-creds`` to automate the creation of both the keystore and the truststore. Check the :ref:`dedicated page <avn_service_user_kafka_java_creds>` for more details.