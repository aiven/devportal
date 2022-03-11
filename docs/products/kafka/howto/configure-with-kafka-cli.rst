Manage configurations with Apache Kafka® CLI tools
==================================================

ZooKeeper is an important part of Apache Kafka® since it tracks the status of the cluster and offers visibility its the current state. Moreover, by interacting with ZooKeeper, you're able to change any Apache Kafka parameter.

Aiven for Apache Kafka® is a fully managed service, therefore, to guarantee the service stability, good maintenance and functionality, we do not allow direct access to ZooKeeper. Instead, we monitor and manage it using the Aiven platform to make sure that we can react as quickly as possible if any issues occur.

Most of the changes usually performed via ZooKeeper are available via the :doc:`advanced configuration flags in the Aiven web console <use-zookeeper>` or via the :doc:`Aiven CLI </docs/tools/cli>`. However, you may want to use the client tools included in the `Apache Kafka binaries <https://kafka.apache.org/downloads>`_ to manage the configurations for your services. 

.. Warning::
    
    Without access to ZooKeeper, some of the Apache Kafka command line tools are not working. But some commands, with the Apache Kafka product maturation, removed the reliance on ZooKeeper giving you options to handle specific configuration changes.

Example: Create a topic with retention time to 30 minutes with ``kafka-topics.sh``
----------------------------------------------------------------------------------

Each topic in Apache Kafka can have a different retention time, defining for the messages' time to live. The Aiven web console and API offer the ability to set the retention time as part of the topic :ref:`creation <avn_cli_service_topic_create>` or :ref:`update <avn-cli-topic-update>`.

The same can be achieved using the ``kafka-topics.sh`` script included in the `Apache Kafka binaries <https://kafka.apache.org/downloads>`_ with the following steps:

1. Download the `Apache Kafka binaries <https://kafka.apache.org/downloads>`_ and unpack the archive
2. Navigate to the ``bin`` folder containing the Apache Kafka client tools commonly used
3. Create a :doc:`Java keystore and truststore <keystore-truststore>` for the Aiven for Apache Kafka service where you want to create a new topic
4. Create a :doc:`client configuration file <kafka-tools-config-file>` pointing at the keystore and truststore created at the previous steps
5. Run the following command to check the connectivity to the Aiven for Apache Kafka service, replacing the ``<KAFKA_SERVICE_URI>`` with the URI of the service available in the `Aiven Console <https://console.aiven.io/>`_.
   
   ::

        ./kafka-topics.sh                           \
            --bootstrap-server <KAFKA_SERVICE_URI>  \
            --command-config consumer.properties    \
            --list


   If successful, the above command lists all the available topics

6. Run the following command to create a new topic named ``new-test-topic`` with a retention rate of 30 minutes.
   Use the kafka-topics script for this and set the retention value in milliseconds ``((100 * 60) * 30 = 180000)``.

   ::

        ./kafka-topics.sh  \
            --bootstrap-server <KAFKA_SERVICE_URI>  \
            --command-config consumer.properties    \
            --topic new-test-topic                  \
            --create                                \
            --config retention.ms=180000

7. Run the same command as step 5 to check the topic creation. Optionally you could also run the ``kafka-topics.sh`` command with the ``--describe`` flag to check the details of your topic and the retention rate.

.. Note:: 

    It is currently not possible to change the configurations for an existing topic via ``kafka-topics.sh`` as that requires a connection to ZooKeeper.