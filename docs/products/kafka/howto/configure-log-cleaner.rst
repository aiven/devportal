Configure log cleaner for topic compaction
==========================================


The log cleaner is the process ensuring only the most recent value for a certain message key is kept within a partition for :doc:`compacted topics <../concepts/log-compaction>`.  In Aiven for Apache Kafka the log cleaner is enabled, but the **log compaction** is disabled by default. To enable log compaction, follow these steps:


Enable log compaction for all topics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#. Log into the `Aiven web console <https://console.aiven.io/>`_ and select your Aiven for Apache Kafka service.
#. Scroll down to *Advanced configuration* and click on **Add configuration option**.
#. Find ``log.cleanup.policy`` in the list and select it.
#. Set the value to ``compact``.

.. warning:: This change will affect all topics in the cluster that do not have a configuration override in place.

Enable log compaction for a specific topic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Log into the `Aiven web console <https://console.aiven.io/>`_ and select your Aiven for Apache Kafka service.
#. Open **Topics** tab.
#. Select a topic you want to modify and click on **Modify** in the context menu.
#. Find ``cleanup.policy`` in the list and select it.
#. Set the value to ``compact``.

Log cleaning frequency and delay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before the cleaning begins, the cleaner thread will inspect the logs to find those with highest **dirty ratio** calculated as the number of bytes in the head vs the total number of bytes in the log (tail + head); you can read more about head and tail definition in the :doc:`compacted topic documentation <../concepts/log-compaction>`. The ratio provides an estimation of how many duplicated keys are present in a topic, and therefore need to be compacted.

.. Tip::

For the log cleaner to start compacting a topic, the dirty ratio needs to be bigger than a threshold set to 50% by default. You can change this value either globally for the cluster by modifying the property ``kafka.log_cleaner_min_cleanable_ratio`` in the *Advanced configuration* section of the service overview, or for a specific topic modifying ``min_cleanable_ratio`` value.

The log cleaner can be configured to leave some amount of not compacted "head" of the log by setting compaction time lag. You can achieve this by setting two additional properties from the *Advanced configuration*, or a corresponding value for an individual topic:

* ``log.cleaner.min.compaction.lag.ms`` : setting to a value greater than 0 will prevent log cleaner from compacting messages with an age newer than a minimum message age thus allowing to delay compacting records.

* ``log.cleaner.max.compaction.lag.ms`` : the maximum amount of time a message will remain not compacted. 

.. Tip::

    Please note, that exact compaction lag can be bigger than the ``log.cleaner.max.compaction.lag.ms`` setting since it directly depends on the time to complete the actual compaction process and can be delayed by the log cleaner threads availability.

Tombstone records
~~~~~~~~~~~~~~~~~

During the cleanup process, log cleaner threads also removes records that have a null value, also known as **tombstone** records. These records can be delayed from being deleted by configuring ``delete.retention.ms`` for the compacted topic.

Consumers are able to read all tombstone messages as long as they reach the head of the topic before the period defined in ``delete.retention.ms`` (default: 24 hours) is passed.

