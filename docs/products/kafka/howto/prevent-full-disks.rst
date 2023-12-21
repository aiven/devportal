Prevent full disks
===================

To ensure the smooth functioning of your **Aiven for Apache Kafka®** services, preventing disk space from running low is important. The Aiven platform actively monitors the available disk space, and if the usage exceeds 90%, you will be notified.

If any node in the service surpasses the critical threshold of disk usage (more than 97%), the access control list (ACL) used to authorize API requests by Apache Kafka clients will be updated on all nodes. This update will prevent operations that could further increase disk usage, including:

- The ``Write`` and ``IdempotentWrite`` operations that clients use to produce new messages.
- The ``CreateTopics`` operation that creates one or more topics, each carrying some overhead on disk.

When the disk space is insufficient, and the ACL blocks write operations, you will encounter an error. For example, if you are using the Python client for Apache Kafka, you may receive the following error message:

.. code::

   TopicAuthorizationFailedError: [Error 29] TopicAuthorizationFailedError: your-topic


Upgrade to a larger service plan
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. In the `Aiven Console <https://console.aiven.io/>`_, select your project and then choose your Aiven for Apache Kafka® service.

#. In the service, select **Service settings** from the sidebar. 

#.  On the **Service settings** page, scroll to **Service plan** and select **Change plan** from the **Actions (…)** menu. 

#. In the **Change service plan** dialog, select your new service plan and select **Change**. 

This will deploy new nodes with increased disk space. Once the data is migrated from the old nodes to the new ones, disk usage will return to an acceptable level, and write operations will be allowed again. 

You can also use the CLI command :ref:`avn-cli-service-update` to upgrade your service plan.

Add additional storage space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the steps from our article on :doc:`how to add additional storage to your services </docs/platform/howto/add-storage-space>`.

Delete one or more topics
~~~~~~~~~~~~~~~~~~~~~~~~~

#. In the `Aiven Console <https://console.aiven.io/>`_, select your project and then choose your Aiven for Apache Kafka® service.

#. Select **Topics** from the sidebar.

#. Select the topic you want to remove, and in the **Topic info** screen, select **Remove**. 

#. Select **Delete** to confirm that you want to delete the topic.

Deleting a topic frees up the disk space it previously used. The log cleaner process may take a few minutes to remove the associated data files from the disk. Once completed, the access control list (ACL) is updated to allow write operations.

You can also use the CLI command :doc:`avn cli delete-topic </docs/tools/cli/service/topic>` or make a call to `API endpoint <https://api.aiven.io/doc/#operation/ServiceKafkaTopicDelete>`_ from any native Apache Kafka client to delete topics.

.. note:: You must use an admin-level user account for the connection.

Decrease retention time/size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another way to make more space available without deleting an entire topic is to reduce the retention time or size for one or more topics. If
you know how old the oldest messages are in a topic, you can lower the retention time for the topic to make more space available. Follow the instructions :doc:`to change retention period </docs/products/kafka/howto/change-retention-period>`.

