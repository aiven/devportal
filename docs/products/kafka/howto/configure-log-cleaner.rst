Configure log cleaner for topic compaction
==========================================

The log cleaner serves the purpose of preserving only the latest value associated with a specific message key in a partition for :doc:`compacted topics <../concepts/log-compaction>`. In Aiven for Apache Kafka®, the log cleaner is enabled by default, while log compaction remains disabled. To enable log compaction, follow these steps:

Enable log compaction for all topics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. In the `Aiven Console <https://console.aiven.io/>`_, select your project and then choose your Aiven for Apache Kafka® service.
#. In the service page, select **Service settings** from the sidebar. 
#. On the **Service settings** page, scroll down to the **Advanced configuration** section, and click **Configure**.
#. In the **Advanced configuration** dialog, click **Add configuration options**.
#. Find ``log.cleanup.policy`` in the list and select it.
#. Set the value to ``compact``.
#. Click **Save configuration**. 

.. warning:: This change will affect all topics in the cluster that do not have a configuration override in place.

Enable log compaction for a specific topic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. In the `Aiven Console <https://console.aiven.io/>`_, select your project and then choose your Aiven for Apache Kafka® service.
#. Select **Topics** from the left sidebar.
#. Select a topic you want to modify and select **Modify** in the context menu.
#. From the drop-down options for the **Cleanup policy**, select the value ``compact``.
#. Select **Update**. 


Log cleaning frequency and delay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before the cleaning begins, the cleaner thread will inspect the logs to find those with highest **dirty ratio** calculated as the number of bytes in the head vs the total number of bytes in the log (tail + head); you can read more about head and tail definition in the :doc:`compacted topic documentation <../concepts/log-compaction>`. The ratio provides an estimation of how many duplicated keys are present in a topic, and therefore need to be compacted.

.. Tip::

    For the log cleaner to start compacting a topic, the dirty ratio needs to be bigger than a threshold set to 50% by default. You can change this value either globally for the cluster by modifying the property ``kafka.log_cleaner_min_cleanable_ratio`` in the *Advanced configuration* section of the service overview or for a specific topic by modifying ``min_cleanable_ratio`` value.

The log cleaner can be configured to leave some amount of not compacted "head" of the log by setting compaction time lag. You can achieve this by setting two additional properties from the *Advanced configuration* or a corresponding value for an individual topic:

* ``log.cleaner.min.compaction.lag.ms`` : setting to a value greater than 0 will prevent log cleaner from compacting messages with an age newer than a minimum message age, thus allowing to delay compacting records.

* ``log.cleaner.max.compaction.lag.ms`` : the maximum amount of time a message will remain not compacted. 

.. Tip::

    Please note, that exact compaction lag can be bigger than the ``log.cleaner.max.compaction.lag.ms`` setting since it directly depends on the time to complete the actual compaction process and can be delayed by the log cleaner threads availability.

Tombstone records
~~~~~~~~~~~~~~~~~

During the cleanup process, log cleaner threads also removes records that have a null value, also known as **tombstone** records. These records can be delayed from being deleted by configuring ``delete.retention.ms`` for the compacted topic.

Consumers can read all tombstone messages as long as they reach the head of the topic before the period defined in ``delete.retention.ms`` (default: 24 hours) is passed.

