View and reset consumer group offsets
============================================

The `open source Apache Kafka code <https://kafka.apache.org/downloads>`_ includes a ``kafka-consumer-groups.sh`` utility enabling you to view and manipulate the state of consumer groups. 
Before using the tool, few setup steps need to be performed.

Define the configuration file
-----------------------------

#. Create the Java keystore and truststore for your Aiven for Apache Kafka service using the :ref:`dedicated Aiven CLI command <avn_service_user_kafka_java_creds>`.

#. Create a ``consumer.properties`` properties file pointing to the keystore and truststore files with the following entries:

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


Managing consumer group offsets with ``kafka-consumer-groups.sh``
-----------------------------------------------------------------

The ``kafka-consumer-groups.sh`` tool enables to manage consumer group offsets, the following commands are available.

List the active consumer groups
'''''''''''''''''''''''''''''''''''''''''

To list the currently active consumer groups use the following command replacing the ``demo-kafka.my-project.aivencloud.com:17072`` with the Aiven for Apache Kafka service URI:

::

    kafka-consumer-groups.sh \
        --bootstrap-server demo-kafka.my-project.aivencloud.com:17072 \
        --command-config consumer.properties \
        --list

An example of the ``list`` option, showing two consumer groups, is the following:

.. code:: text

    my-group
    my-group-2

Retrieve the details of a consumer group
''''''''''''''''''''''''''''''''''''''''''''''''

To retrieve the details of a consumer group use the following command replacing the ``demo-kafka.my-project.aivencloud.com:17072`` with the Aiven for Apache Kafka service URI and the ``my-group`` with the required consumer group name:

::

    kafka-consumer-groups.sh \
        --bootstrap-server demo-kafka.my-project.aivencloud.com:17072 \
        --command-config consumer.properties \
        --group my-group \
        --describe
          
An example of the ``describe`` option, showing the details of the ``my-group`` consumer groups, is the following:

.. code:: text

    GROUP           TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID                HOST            CLIENT-ID
    my-group        test-topic      0          5509            5515            6               rdkafka-39404560-f8f2-4b0b /151.62.82.140  rdkafka

List the current members of a consumer group
''''''''''''''''''''''''''''''''''''''''''''

To retrieve the current members of a consumer group use the following command replacing the ``demo-kafka.my-project.aivencloud.com:17072`` with the Aiven for Apache Kafka service URI and the ``my-group`` with the required consumer group name:

::

    kafka-consumer-groups.sh \
        --bootstrap-server demo-kafka.my-project.aivencloud.com:17072 \
        --command-config consumer.properties \
        --group my-group \
        --describe \
        --members

An example of the ``--members`` option, showing the members of the ``my-group`` consumer groups, is the following:

.. code:: text

    GROUP           CONSUMER-ID                                  HOST            CLIENT-ID       #PARTITIONS
    my-group        rdkafka-a4c0a09c-8c6e-457e-bf9e-354a8e2f4bb8 /151.62.82.140  rdkafka         0
    my-group        rdkafka-39404560-f8f2-4b0b-9518-811e2eb20074 /151.62.82.140  rdkafka         1


Reset the offset of a consumer group
'''''''''''''''''''''''''''''''''''''

Resetting the consumer group offset might be needed when the topic parsing needs to start at a specific (non default) offset.
To reset the offset use the following command replacing: 

* ``demo-kafka.my-project.aivencloud.com:17072`` with the Aiven for Apache Kafka service URI 
* ``my-group`` with the required consumer group name
* ``test-topic`` with the required topic name

.. Warning:: 

    The consumer group must be inactive when you make offset changes.

::

   kafka-consumer-groups.sh \
       --bootstrap-server demo-kafka.my-project.aivencloud.com:17072 \
       --command-config consumer.properties \
       --group test-group \
       --topic test-topic \
       --reset-offsets \
       --to-earliest \
       --execute

The ``--reset-offsets`` command has the following additional options:

* ``--to-earliest`` : resets the offset to the beginning of the topic.

* ``--to-lastest`` : resets the offset to the end of the topic.

* ``--to-offset`` : resets the offset to a known, fixed offset number.

* ``--shift-by`` : performs a relative shift from the current offset position using the given integer.

.. Tip::
    
    Use positive values to skip forward or negative values to move backwards.

-  ``--to-datetime <YYYY-MM-DDTHH:mm:SS.sss>`` : resets to the given timestamp.

-  ``--topic <topicname>:<partition>``: Applies the change to a specific partition, for example ``--topic test-topic:0``. By default, the ``--topic`` argument applies to all partitions.