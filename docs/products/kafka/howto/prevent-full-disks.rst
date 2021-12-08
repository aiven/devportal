Prevent full disks
===================

To prevent **Aiven for Apache Kafka** from malfunctioning, the Aiven platform detects when the available disk space in **Aiven for Apache Kafka** services is running low.

If any of the nodes in the service exceeds the critical threshold of disk usage, the access control list (ACL) that is used to authorize API requests by Apache Kafka clients is updated on all nodes to prevent operations that would increase disk usage. Such operations include:

-  The ``Write`` and ``IdempotentWrite`` operations that clients use to produce new messages

-  The ``CreateTopics`` operation that creates one or more topics, each carrying some overhead on disk

When the ACL blocks write operations, clients see an error similar to the following example from the ``python-kafka`` client::

   TopicAuthorizationFailedError: [Error 29] TopicAuthorizationFailedError: mytopic


In ensure that enough disk space is available you can take one of the following actions:

Upgrade to a larger service plan
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Log in to the `Aiven web console <https://console.aiven.io/>`_ and select your service.

#. On the *Overview* page, scroll down to *Service plan* and click **Upgrade plan** .

#. Select your new service plan and click **Upgrade** .


This launches new nodes with more disk space. As data is moved from the old nodes to the new ones, disk usage returns to an acceptable level and the ACL is updated to allow write operations again.

You can also use the CLI command :ref:`avn-cli-service-update` to upgrade your service plan.

Add additional storage space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the steps from our article on :doc:`how to add additional storage to your services </docs/platform/howto/add-storage-space>`.

Delete one or more topics
~~~~~~~~~~~~~~~~~~~~~~~~~

#. Log in to the `Aiven web console <https://console.aiven.io/>`__ and select your service.

#. Click the **Topics** tab.

#. Click **Actions** > **Remove** for any topics that you no longer need.

#. Click **Remove** to confirm that you want to delete the topic.

This deletes the entire topic and frees up the used disk space. It may take up to a few minutes before the log cleaner starts removing the data files from disk. After that, the ACL is update to allow write operations again.

You can also use the CLI command :ref:`avn-cli-delete-topic` or make a call to `API endpoint <https://api.aiven.io/doc/#operation/ServiceKafkaTopicDelete>`_ from any native Apache Kafka client to delete topics.

.. note:: You must use an admin-level user account for the connection.

Decrease retention time/size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another way to make more space available without deleting an entire
topic is to reduce the retention time or size for one or more topics. If
you know how old the oldest messages are in a topic, you can lower the
retention time for the topic to make more space available:

#. Log in to the `Aiven web console <https://console.aiven.io/>`_ and select your service.

#. Click the **Topics** tab.

#. Click a topic that you want to edit. In the *Topic info* view, check how much space the topic is currently using. Make note of the current retention time.

#. In the *Topic info* view, click **Modify** .

#. If there is no field for **Retention ms**, select it from the drop-down menu.

#. Change the **Retention ms** value to a suitable value in milliseconds.

.. note:: Using a lower value for the retention time only makes more space available if there are messages in the topic that are older than the given value.

The log cleaner starts removing data from disk within a few minutes. After that, the ACL is update to allow write operations again.

You can also use the CLI command :ref:`avn-cli-topic-update` with admin permissions to change the ``retention.bytes`` topic configuration parameter to something lower than the current size for the topic.


