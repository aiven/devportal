Configure log cleaner for compaction
=====================================

By default the log cleaner is enabled, but the log compaction is disabled. To enable log compaction, follow these steps:

#. Log into the `Aiven web console <https://console.aiven.io/>`_ and select your Aiven for Apache Kafka service.
#. Scroll down to *Advanced configuration* and click on **Add configuration option**.
#. Find ``log.cleanup.policy`` in the list and select it.
#. Set the value to ``compact``.

This change will affect all topics in the cluster that do not have a configuration override in place.

Control the frequency and delay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before the cleaning begins, the cleaner thread will inspect the logs to find those with highest **dirty ratio** which is calculated as the ratio of the number of bytes in the head vs the total number of bytes in the log (tail + head). The default ratio value is 50%, but you can change it by change value of the property ``kafka.log_cleaner_min_cleanable_ratio`` from the *Advanced configuration* list.

Log cleaner can be configured to leave some amount of not compacted "head" of the log by setting compaction time lag. You can achieve this by setting two additional properties from the  *Advanced configuration*:

-  ``log.cleaner.min.compaction.lag.ms`` : setting to a value greater than 0 will prevent log cleaner from compacting messages with an age newer than a minimum message age. Allows to delay compacting records.

-  ``log.cleaner.max.compaction.lag.ms`` : the maximum amount of time message will remain not compacted. Please note, that exact time of compression can be later when comparing to the maximum compaction lag, depending on the availability log cleaner threads and actual compaction time.

Tombstone records
~~~~~~~~~~~~~~~~~

During the cleanup process, log cleaner threads would also remove records that have a null value, also known as **tombstone** records. These records can be delayed from being deleted by configuring ``delete.retention.ms`` for compacted topic.

The consumer sees all tombstones as long as the consumer reaches head of a log in a period less than the topic configuration ``delete.retention.ms`` (the default is 24 hours).

