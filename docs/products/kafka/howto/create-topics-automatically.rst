Create Apache Kafka topics automatically
==========================================

You can set Apache Kafka to automatically create a topic when a message is produced to a topic that does not exist. 
By default, in Aiven for Apache Kafka this features is turned off as safeguard against accidental topic creation and when a message is produced to a topic that does not yet exist. In such cases the common error message is the following::

    KafkaTimeoutError: Failed to update metadata after 60.0 secs.

In such cases two options are available:

#. :doc:`Create topics beforehand </docs/products/kafka/create-topic>`
#. Enable topic automatic creation

While option 2 seems the easier solution it has drawbacks like the risk of creating new topics in case of typos or accepting all the :doc:`topic configuration default values <set-kafka-parameters>` set at service level such as partition count, replication factor, and retention time.

Creating topics beforehand is generally considered a preferred practice and recommended for production environments. However, for specific needs, you might want/need to enable automatic topic creation, which can be done by changing the ``auto_create_topics_enable`` parameter using the :doc:`Aiven CLI </docs/tools/cli>` or the `Aiven web console <https://console.aiven.io/>`_ by selecting the corresponding settings in the *Advanced configuration* section of the *Overview* page for your service.

.. Warning::

    Even when you enable automatic topic creation, the user account that produces a message to a non-existing topic must have ``admin`` permissions. Aiven for Apache Kafka validates the access control list (ACL) before creating the topic. To change user permissions, navigate to the **Users** tab in your service detail page in the `Aiven web console <https://console.aiven.io/>`_.

Enable automatic topic creation with Aiven CLI
---------------------------------------------------

The :ref:`Aiven CLI service update command <avn-cli-service-update>` enables to modify service parameters on an existing service. To enable the automatic creation of topics on an existing Aiven for Apache Kafka service set the ``auto_create_topics_enable`` to ``true`` by using the following command replacing the ``SERVICE_NAME`` with the name of your service:

::

    avn service update SERVICE_NAME -c kafka.auto_create_topics_enable=true
