Use schema registry in Java with Aiven for Apache Kafka
=======================================================

Aiven for Apache Kafka provides the **schema registry** functionality via `Karapace <https://github.com/aiven/karapace>`_, including the possibility to store, retrieve a schema, and also evolve it without needing to rebuild existing Consumers and Producers code. 

.. Note::

    To use the schema registry functionality exposed by Karapace, you need to enable the **Schema Registry (Karapace)** functionality for the Aiven for Apache Kafka instance selected from the `Aiven console <https://console.aiven.io/>`_, service Overview tab.

The following steps are required in Java to make use of schema registry:

#. Create version 1 of a schema
#. Use Apache Avro to compile the schema
#. Create consumer and producer that utilize Aiven for Apache Kafka and Schema Registry

Prerequisites
'''''''''''''

To be able to produce and consume data in Java from an Aiven for Apache Kafka service you need to create a **Keystore** and **Truststore** containing the SSL certificates. 

You can do it manually by downloading the certificates and :doc:`composing the files locally on your machine <keystore-truststore>` or using the :ref:`dedicated Aiven CLI command <avn_service_user_kafka_java_creds>`.

.. _kafka_schema_registry_variables:

Variables
'''''''''

These are the placeholders you will need to replace in the code sample:

=============================      ===========================================================================================================================
Variable                           Description
=============================      ===========================================================================================================================
``BOOTSTRAPSERVERS``               Service URI for Kafka connection, can be obtained from the `Aiven console <https://console.aiven.io/>`_, service Overview tab
``KEYSTORE``                       Path to the keystore
``KEYSTOREPASSWORD``               Password for the keystore
``TRUSTSTORE``                     Path to the truststore
``TRUSTSTOREPASSWORD``             Password for the truststore
``SSLKEYPASSWORD``                 The password of the private key in the key store file
``SCHEMAREGISTRYURL``              Service Registry URI for Apache Kafka connection
``SCHEMAREGISTRYUSER``             Service Registry username, can be obtained from the `Aiven console <https://console.aiven.io/>`_, service Overview tab
``SCHEMAREGISTRYPASSWORD``         Service Registry password, can be obtained from the `Aiven console <https://console.aiven.io/>`_, service Overview tab
``TOPIC_NAME``                     Apache Kafka topic name to use
=============================      ===========================================================================================================================


Create version 1 of the Avro schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create an Avro schema, you need a definition file. As example you can use a **click record** schema defined in JSON and stored in a file named ``ClickRecord.avsc`` containing the following:

::

    {"type": "record",
      "name": "ClickRecord",
      "namespace": "io.aiven.avro.example",
      "fields": [
         {"name": "session_id", "type": "string"},
         {"name": "browser", "type": ["string", "null"]},
         {"name": "campaign", "type": ["string", "null"]},
         {"name": "channel", "type": "string"},
         {"name": "referrer", "type": ["string", "null"], "default": "None"},
         {"name": "ip", "type": ["string", "null"]}
      ]
    }

The JSON configuration above defines a schema named ``ClickRecord`` in the namespace ``io.aiven.avro.example`` with fields ``session_id``, ``browser``, ``campaign``, ``channel``, ``referrer`` and ``ip`` and related data types. 

Once the schema is defined, you need to compile it, and it can be done **manually** or **automatically**.

Manual schema compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~

In case of manual schema compilation, download ``avro-tools-1.11.0.jar`` from https://avro.apache.org/releases.html#Download or via maven using the following::

    mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:get -Dartifact=org.apache.avro:avro-tools:1.11.0:jar -Ddest=avro-tools-1.11.0.jar

The schema defined in the previous step, can be now compiled to produce a Java class ``ClickRecord.java`` in the ``io.aiven.avro.example`` package (taken from the ``namespace`` parameter)::

    java -jar avro-tools-1.11.0.jar compile schema ClickRecord.avsc .

.. Note:: 

    The package structure will also be generated if missing.

Auto schema compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~

With auto, the schema is compiled during the project build with, for example, ``maven-avro-plugin`` or ``gradle-avro-plugin``.
The following is a configuration example for ``maven-avro-plugin`` when ``ClickRecord.avsc`` is stored in the path ``src/main/avro/ClickRecord.avsc``::

    <plugin>
        <groupId>org.apache.avro</groupId>
        <artifactId>avro-maven-plugin</artifactId>
        <version>${avro-maven-plugin.version}</version>
        <executions>
            <execution>
                <id>schemas</id>
                <phase>generate-sources</phase>
                <goals>
                    <goal>schema</goal>
                    <goal>protocol</goal>
                    <goal>idl-protocol</goal>
                </goals>
                <configuration>
                    <sourceDirectory>${project.basedir}/src/main/avro/</sourceDirectory>
                    <outputDirectory>${project.basedir}/src/main/generated-sources/</outputDirectory>
                </configuration>
            </execution>
        </executions>
    </plugin>

The automatically generated Avro-schema code will be stored under the folder ``${project.basedir}/src/main/generated-sources/``.

Set consumer and producer properties for schema registry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The full code to create consumer and producers using the Schema Registry in Aiven for Apache Kafka can be found in the `Aiven examples GitHub repository <https://github.com/aiven/aiven-examples/tree/master/solutions/kafka-schema-registry>`_. The following contains a list of the properties required.

For producers you need to specify::

      props.put(CommonClientConfigs.BOOTSTRAP_SERVERS_CONFIG, [BOOTSTRAPSERVERS]);
      props.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SSL");
      props.put(SslConfigs.SSL_TRUSTSTORE_LOCATION_CONFIG, [TRUSTSTORE]);
      props.put(SslConfigs.SSL_TRUSTSTORE_PASSWORD_CONFIG, [TRUSTSTOREPASSWORD]);
      props.put(SslConfigs.SSL_KEYSTORE_TYPE_CONFIG, "PKCS12");
      props.put(SslConfigs.SSL_KEYSTORE_LOCATION_CONFIG, [KEYSTORE]);
      props.put(SslConfigs.SSL_KEYSTORE_PASSWORD_CONFIG, [KEYSTOREPASSWORD]);
      props.put(SslConfigs.SSL_KEY_PASSWORD_CONFIG, [SSLKEYPASSWORD]);
      props.put("schema.registry.url", [SCHEMAREGISTRYURL]);
      props.put("basic.auth.credentials.source", "USER_INFO");
      props.put("basic.auth.user.info", [SCHEMAREGISTRYUSER] + ":" + [SCHEMAREGISTRYPASSWORD]);
      props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
      props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, KafkaAvroSerializer.class.getName());

For consumers you need to specify::

      props.put(CommonClientConfigs.BOOTSTRAP_SERVERS_CONFIG, [BOOTSTRAPSERVERS]);
      props.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SSL");
      props.put(SslConfigs.SSL_TRUSTSTORE_LOCATION_CONFIG, [TRUSTSTORE]);
      props.put(SslConfigs.SSL_TRUSTSTORE_PASSWORD_CONFIG, [TRUSTSTOREPASSWORD]);
      props.put(SslConfigs.SSL_KEYSTORE_TYPE_CONFIG, "PKCS12");
      props.put(SslConfigs.SSL_KEYSTORE_LOCATION_CONFIG, [KEYSTORE]);
      props.put(SslConfigs.SSL_KEYSTORE_PASSWORD_CONFIG, [KEYSTOREPASSWORD]);
      props.put(SslConfigs.SSL_KEY_PASSWORD_CONFIG, [SSLKEYPASSWORD]);
      props.put("schema.registry.url", [SCHEMAREGISTRYURL]);
      props.put("basic.auth.credentials.source", "USER_INFO");
      props.put("basic.auth.user.info", [SCHEMAREGISTRYUSER] + ":" + [SCHEMAREGISTRYPASSWORD]);
      props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
      props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, KafkaAvroDeserializer.class.getName());
      props.put(KafkaAvroDeserializerConfig.SPECIFIC_AVRO_READER_CONFIG, true);
      props.put(ConsumerConfig.GROUP_ID_CONFIG, "clickrecord-example-group");

.. Note::

    In the above properties replace all the required input parameters (within square brackets) with the appropriate information defined in the :ref:`Variables section <kafka_schema_registry_variables>`.  