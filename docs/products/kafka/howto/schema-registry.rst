Using Schema Registry with Aiven for Apache Kafka
=====================================================

Schema Registry makes it possible to evolve a schema without having to rebuild existing Consumers and Producers. This help article walks through steps required to:

#. Create the Java keystore and truststore for your Aiven for Apache Kafka service using the :ref:`dedicated Aiven CLI command <avn_service_user_kafka_java_creds>`.
#. Create version 1 of schema
#. Use Apache Avro to compile the schema
#. Create Consumer and Producer that utilize Aiven for Apache Kafka and Schema Registry

Variables
'''''''''
These are the placeholders you will need to replace in the code sample:

=============================      =======================================================================
Variable                           Description
=============================      =======================================================================
``bootstrapServers``               Service URI for Kafka connection
``keystore``                       Path to keystore
``keystorePassword``               Password for keystore
``truststore``                     Path to keystore
``truststorePassword``             Password for truststore
``sslKeyPassword``                 The password of the private key in the key store file
``schemaRegistryUrl``              Service Registry URI for Kafka connection
``schemaRegistryUser``             Service Registry username
``schemaRegistryPassword``         Service Registry password
``topic``                          Kafka topic to use
``filename``                       File with data (default name: FileWithData.csv)
=============================      =======================================================================

Create version 1 of schema
~~~~~~~~~~~~~~~~~~~~~~~~~~

In this tutorial we explore a simple click record schema, ``ClickRecord.avsc``, defined in JSON as follows::

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

Manual Schema Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~
There are two ways to compile the schema: manual and auto.

In case of manual download ``avro-tools-1.11.0.jar`` from https://avro.apache.org/releases.html#Download or it could be done with maven like::

    mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:get -Dartifact=org.apache.avro:avro-tools:1.11.0:jar -Ddest=avro-tools-1.11.0.jar

Use the following command to compile the schema defined in the previous step to produce Java class ``ClickRecord.java`` in ``io.aiven.avro.example`` package (taken from namespace)::

    java -jar avro-tools-1.11.0.jar compile schema ClickRecord.avsc .

Auto Schema Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~
Schema could be compiled during build with e.g. ``maven-avro-plugin`` or ``gradle-avro-plugin``.
Here there is an example of configuration for ``maven-avro-plugin`` when ``ClickRecord.avsc`` is ``src/main/avro/ClickRecord.avsc``::

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

Create Consumer & Producer that utilize Aiven for Apache Kafka & Schema Registry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create ``Consumer.java`` and ``Producer.java`` classes as follows. (NOTE: generate the keystore and truststore per `Configuring Java SSL to access Kafka <https://developer.aiven.io/docs/products/kafka/howto/keystore-truststore>`_).

Full ready to use example with instructions could be found at https://github.com/aiven/aiven-examples/pull/35

For producer we need to specify properties::

      props.put(CommonClientConfigs.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
      props.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SSL");
      props.put(SslConfigs.SSL_TRUSTSTORE_LOCATION_CONFIG, truststore);
      props.put(SslConfigs.SSL_TRUSTSTORE_PASSWORD_CONFIG, truststorePassword);
      props.put(SslConfigs.SSL_KEYSTORE_TYPE_CONFIG, "PKCS12");
      props.put(SslConfigs.SSL_KEYSTORE_LOCATION_CONFIG, keystore);
      props.put(SslConfigs.SSL_KEYSTORE_PASSWORD_CONFIG, keystorePassword);
      props.put(SslConfigs.SSL_KEY_PASSWORD_CONFIG, sslKeyPassword);
      props.put("schema.registry.url", schemaRegistryUrl);
      props.put("basic.auth.credentials.source", "USER_INFO");
      props.put("basic.auth.user.info", schemaRegistryUser + ":" + schemaRegistryPassword);
      props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
      props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, KafkaAvroSerializer.class.getName());

For consumer we need to specify properties::

      props.put(CommonClientConfigs.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
      props.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SSL");
      props.put(SslConfigs.SSL_TRUSTSTORE_LOCATION_CONFIG, truststore);
      props.put(SslConfigs.SSL_TRUSTSTORE_PASSWORD_CONFIG, truststorePassword);
      props.put(SslConfigs.SSL_KEYSTORE_TYPE_CONFIG, "PKCS12");
      props.put(SslConfigs.SSL_KEYSTORE_LOCATION_CONFIG, keystore);
      props.put(SslConfigs.SSL_KEYSTORE_PASSWORD_CONFIG, keystorePassword);
      props.put(SslConfigs.SSL_KEY_PASSWORD_CONFIG, sslKeyPassword);
      props.put("schema.registry.url", schemaRegistryUrl);
      props.put("basic.auth.credentials.source", "USER_INFO");
      props.put("basic.auth.user.info", schemaRegistryUser + ":" + schemaRegistryPassword);
      props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
      props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, KafkaAvroDeserializer.class.getName());
      props.put(KafkaAvroDeserializerConfig.SPECIFIC_AVRO_READER_CONFIG, true);
      props.put(ConsumerConfig.GROUP_ID_CONFIG, "clickrecord-example-group");
