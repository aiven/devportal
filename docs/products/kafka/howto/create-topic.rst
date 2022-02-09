Creating an Apache Kafka topic
===============================

While you can set Kafka to automatically create a topic when a message is produced to a topic that does not exist, creating topics beforehand is generally considered a preferred practice and recommended for production environments. 

Create a new Apache Kafka topic using the Aiven console
--------------------------------------------------------

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. On the **Services** page, click on the service name.

3. Select the **Topics** tab:

   a. Enter a name for your topic.

   b. Select **Advanced configuration** to set the replication factor, number of partitions and other advanced settings. These can be modified later.

4. Click **Add Topic** on the right hand side of the console.

   The new topic will be visible immediately, but may take a few minutes before you can update its settings.


Create an Apache Kafka topic using the Aiven client (CLI)
----------------------------------------------------------

1. Prepare the command to add the topic to your Apache Kafka service.


2. Add the ``kafka_service`` parameter to specify the service for which you want to create a new topic, and the ``topic_name`` for the new topic. You will also need to specify the replication factor and number of partitions. For instance, to add the topic ``topic_name`` to the Apache Kafka service ``kafka_service``, with a replication factor of 3 and 2 partitions per topic, you would use this command:

    avn service topic-create --partitions 2 --replication 3 kafka_service topic_name

The changes are applied immediately.

