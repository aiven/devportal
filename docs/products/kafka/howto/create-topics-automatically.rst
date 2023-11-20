Create Apache Kafka® topics automatically
===========================================

Apache Kafka® provides the capability to automatically create topics when a message is produced to a topic that does not exist. By default, this feature is disabled in Aiven for Apache Kafka as a precaution against accidental topic creation. When a message is produced to a non-existent topic, the common error message is as follows:

.. code::
   
   KafkaTimeoutError: Failed to update metadata after 60.0 secs.

In such cases, you have two options available:

#. Create topics in advance: This approach involves manually :doc:`creating the topics </docs/products/kafka/howto/create-topic>` before they are used. It is generally recommended for production environments as it provides better control over topic settings such as partition count, replication factor, and retention time.  

#. Enable topic automatic creation: While simpler, enabling automatic topic creation carries some drawbacks. It introduces the risk of inadvertently creating new topics, especially in the case of typos. Additionally, it may result in topics created with :doc:`default configuration values <set-kafka-parameters>` defined at the service level.


Enable automatic topic creation using Aiven Console
-----------------------------------------------------

To enable automatic topic creation through the Aiven Console, follow these steps: 

1. Log in to `Aiven Console <https://console.aiven.io/>`_ and select your Aiven for Apache Kafka service.
2. On the **Overview** page, scroll down to **Advanced configuration** and select **Change**. 
3. In the **Edit advanced configuration** screen, select **Add configuration option**.
4. Find the ``auto_create_topics_enable`` parameter and set it to true to enable automatic topic creation.
5. Select **Save advanced configuration**. 

.. Warning::

    Even when you enable automatic topic creation, the user account that produces a message to a non-existing topic must have ``admin`` permissions. Aiven for Apache Kafka validates the access control list (ACL) before creating the topic. To change user permissions, navigate to the **Users** tab in your service detail page in the `Aiven web console <https://console.aiven.io/>`_.

Enable automatic topic creation with Aiven CLI
---------------------------------------------------

The :ref:`Aiven CLI service update command <avn-cli-service-update>` enables to modify service parameters on an existing service. To enable the automatic creation of topics on an existing Aiven for Apache Kafka service set the ``auto_create_topics_enable`` to ``true`` by using the following command replacing the ``SERVICE_NAME`` with the name of your service:

You can enable the automatic creation of topics on an existing Aiven for Apache Kafka service by using the :ref:`Aiven CLI service update <avn-cli-service-update>` command. Set the ``auto_create_topics_enable`` parameter to ``true`` with the following command, replacing ``SERVICE_NAME`` with the name of your service:

.. code::

    avn service update SERVICE_NAME -c kafka.auto_create_topics_enable=true
