Configure consumer properties for Apache Kafka Toolbox
==========================================================

The `open source Apache Kafka code <https://kafka.apache.org/downloads>`_ includes a series of tools under the ``bin`` directory that can be useful to manage and interact with Aiven for Apache Kafka.
Before using the tools, you need to configure a ``consumer.properties`` file pointing to a Java keystore and truststore which contain the required certificates for authentication.

Define the configuration file
-----------------------------

#. Create the Java keystore and truststore for your Aiven for Apache Kafka service using the :ref:`dedicated Aiven CLI command <avn_service_user_kafka_java_creds>`.

#. Create a ``consumer.properties`` file pointing to the keystore and truststore with the following entries:

* ``security.protocol``: security protocol, SSL for the default TLS security settings
* ``ssl.keystore.type``: keystore type, ``PKCS12`` for the keystore generated with the :ref:`dedicated Aiven CLI command <avn_service_user_kafka_java_creds>`
* ``ssl.keystore.location``: keystore location on the file system
* ``ssl.keystore.password``: keystore password
* ``ssl.truststore.location``: truststore location on the file system
* ``ssl.truststore.password``: truststore password
* ``ssl.key.password``: keystore password

.. Tip::

    The ``avn service user-kafka-java-creds`` :ref:`Aiven CLI command <avn_service_user_kafka_java_creds>` accepts a ``--password`` parameter setting the same password for the truststore, keystore and key
   
An example of the ``consumer.properties`` content is the following::

    security.protocol=SSL
    ssl.keystore.type=PKCS12
    ssl.keystore.location=client.keystore.p12
    ssl.keystore.password=changeit
    ssl.key.password=changeit
    ssl.truststore.location=client.truststore.jks
    ssl.truststore.password=changeit