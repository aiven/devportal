View and reset consumer group offsets
============================================

The `open source Apache Kafka® code <https://kafka.apache.org/downloads>`_ includes a ``kafka-consumer-groups.sh`` utility enabling you to view and manipulate the state of consumer groups.

.. Note::

    Before using the ``kafka-consumer-groups.sh`` you need to configure a ``consumer.properties`` file pointing to a Java keystore and truststore which contain the required certificates for authentication. Check out how to do it in the :doc:`dedicated page <kafka-tools-config-file>`.


Managing consumer group offsets with ``kafka-consumer-groups.sh``
-----------------------------------------------------------------

The ``kafka-consumer-groups.sh`` tool enables to manage consumer group offsets, the following commands are available.

List active consumer groups
'''''''''''''''''''''''''''''''''''''''''

To list the currently active consumer groups use the following command replacing the ``demo-kafka.my-project.aivencloud.com:17072`` with your service URI:

::

    kafka-consumer-groups.sh \
        --bootstrap-server demo-kafka.my-project.aivencloud.com:17072 \
        --command-config consumer.properties \
        --list

Retrieve the details of a consumer group
''''''''''''''''''''''''''''''''''''''''''''''''

To retrieve the details of a consumer group use the following command replacing the ``demo-kafka.my-project.aivencloud.com:17072`` with the Aiven for Apache Kafka service URI and the ``my-group`` with the required consumer group name:

::

    kafka-consumer-groups.sh \
        --bootstrap-server demo-kafka.my-project.aivencloud.com:17072 \
        --command-config consumer.properties \
        --group my-group \
        --describe
          
The details of the consumer group ``my-group`` are printed out in the following output:

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

The members of the ``my-group`` consumer group are printed out in the following output:

.. code:: text

    GROUP           CONSUMER-ID                                  HOST            CLIENT-ID       #PARTITIONS
    my-group        rdkafka-a4c0a09c-8c6e-457e-bf9e-354a8e2f4bb8 /151.62.82.140  rdkafka         0
    my-group        rdkafka-39404560-f8f2-4b0b-9518-811e2eb20074 /151.62.82.140  rdkafka         1


Reset the offset of a consumer group
'''''''''''''''''''''''''''''''''''''

You might want to reset the consumer group offset when the topic parsing needs to start at a specific (non default) offset.
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
