Log compaction
==============

One way to reduce the disk space requirements in Kafka is to use **log compaction**. This operation retains only the newest record for each key on a topic, regardless of whether the retention period of the message has expired or not. Depending on the application, this can significantly reduce the amount of storage required for the topic.

To make use of log compaction, all messages sent to the topic must have an explicit key. To enable log compaction follow the steps described in :doc:`how to configure log cleaner <../howto/configure-log-cleaner>`.


How topic log compaction works
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kafka topics represent a continuous stream of messages that typically get discarded after log reaches a certain period of time or size. However for certain use cases we just need the most recent changes.

For example, if we have a topic that contains user's home address and every time there is an update, it gets sent to the topic using ``user_id`` as primary key and home address as the value:

::

   1001 -> "4 Privet Dr"
   1002 -> "221B Baker Street"
   ...
   1001 -> "21 Jump St"
   ...
   1001 -> "Paper St"


We have three different options on how long to retain the messages:

* infinite log retention: all changes to user's address would be maintained in the logs. This would lead to the log growing in size without a bound.
* simple log retention: older log records would be deleted after log reaches certain age or size.
* log compaction: only latest version of the key's value are kept.

With log compaction Apache Kafka would remove any older records for which there is a newer version available in the partition log. This retention policy can be set per-topic, so a single cluster can have some topics where retention is enforced by size or time and other topics where retention is enforced by compaction.

Log compaction basics
~~~~~~~~~~~~~~~~~~~~~

To understand better how log compaction work we will look at a partition log of a compacted topic before and after compaction has been applied.

Before compaction
*****************

.. list-table::
  :header-rows: 1
  :stub-columns: 1
  :align: left

  * - Offset
    - Key
    - Value
  * - 1
    - K1
    - 13
  * - 2
    - K2
    - 11
  * - 3
    - K3
    - 22
  * - 4
    - K3
    - 7
  * - 5
    - K1
    - 8
  * - 6
    - K4
    - 14

You can notice that there are two records with duplicate keys **K1**  and **K3.** After we apply log compaction, we only keep records with the latest offset (newest values) and the older ones get discarded.

After compaction
*****************

.. list-table::
  :header-rows: 1
  :stub-columns: 1
  :align: left

  * - Offset
    - Key
    - Value
  * - 2
    - K2
    - 11
  * - 4
    - K3
    - 7
  * - 5
    - K1
    - 8
  * - 6
    - K4
    - 14


When a log is compacted it consists of head and tail, where head is the traditional Kafka log and new records get appended to the end of it. Kafka ensures that the records in the tail consist only of unique keys because only the tail section is scanned during compaction process while head section may contain duplicate keys.

.. note:: Log compaction occurs inside a partition and if two records with the same key land in different partitions, they will not be compacted together.

Segments
~~~~~~~~

If we look "under the hood" of the partition we will find that Kafka divides the partitions into **segments** which are files (name ends with ``.log`` ) stored on a file system for each partition. A segment file is part of the partition. As the log cleaner cleans log partition segments, the segments get swapped into the log partition immediately replacing the older segments.

The first offset of the segment, **base offset,** corresponds to the file name of the segment. The last segment in the partition is called an **active segment** and it is the only segment to which new messages are appended to. **During the cleaning process, an active segment is excluded and you may see duplicate records.** The user-age partition below contains a segment 04.log that has not yet been compacted, hence you will see duplicate records.

Example of user age partition:
*******************************

**01.log:**

.. list-table::
  :header-rows: 1
  :stub-columns: 1
  :align: left

  * - Offset
    - Key
    - Value
  * - 1
    - K1
    - 13
  * - 2
    - K2
    - 11
  * - 3
    - K3
    - 22

**04.log:**

.. list-table::
  :header-rows: 1
  :stub-columns: 1
  :align: left

  * - Offset
    - Key
    - Value
  * - 4
    - K3
    - 13
  * - 5
    - K1
    - 11
  * - 6
    - K1
    - 22

**07.log (active segment):**

.. list-table::
  :header-rows: 1
  :stub-columns: 1
  :align: left

  * - Offset
    - Key
    - Value
  * - 7
    - K4
    - 9


When the segment file reaches a certain size of age, Kafka will create a new segment file. This can be controlled by the following settings:

-  ``segment.bytes`` : create a new segment when current segment becomes greater than this size. This setting can be set during topic creation and defaults to 1GB.

-  ``segment.ms`` : forces the segment to roll over and create a new one when the segment becomes older than this value.
