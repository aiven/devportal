Log compaction
==============

One way to reduce the disk space requirements in Kafka is to use **log compaction**. This operation retains only the newest record for each key on a topic, regardless of whether the retention period of the message has expired. Depending on the application, this can significantly reduce the amount of storage required for the topic.

To make use of log compaction, all messages sent to the topic must have an explicit key. You can enable log compaction under the **Topics** section of the web console by setting the **Cleanup policy** to "compact".

