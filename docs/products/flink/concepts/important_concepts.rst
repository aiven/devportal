Important concepts in Apache Flink
==================================

This article gives you a brief explanation of some of the relevant terms and concepts in Apache Flink. A basic understanding of these helps you get the most out of our other Apache Flink articles.


Event and processing times
--------------------------

Event time refers to when events actually happen, while processing time refers to when events are observed within a system. Various factors affect how events are processed, including shared hardware resources and network congestion, distributed system logic, and variances in the data throughput and order. Because of this, there can be significant differences between the event time and processing time for an event, even though ideally they would be equal.

In Apache Flink, the streamed data does not always arrive in the same order as the events occurred. This means that using processing time in your applications can cause issues in system behavior. For this reason, we recommend that you use event time to process data, as it allows your applications to maintain the correct event sequence throughout the data streaming pipeline.

For more information, see the `Apache Flink documentation <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/concepts/time/>`_.


Windows
-------

Apache Flink uses *windows* to split the streamed data into segments that can be processed. Due to the nature of data streams, there is never a situation where *all* of the data is available, because you would be waiting indefinitely for new data points to arrive - so instead, windowing offers a way to define a subset of data points that you can then process and analyze.

A window is created when the first element matching the criteria that is set for it appears. The window's trigger defines when the window is considered ready for processing, and the function set for the window specifies how to process the data. Each window also has an allowed lateness value - this indicates how long new events are accepted for inclusion in the window after the trigger closes it.

For example, you can set 15:00 as the start time for a time-based window, with the end timestamp set to 15:10 and an allowed lateness of 1 minute. The first event with a timestamp between 15:00 and 15:10 creates the window, and any event that arrives between 15:10 and 15:11 with a timestamp between 15:00 and 15:10 is still included in the window.

Events may still arrive after the allowed lateness for the window, so your application should include a means of handling those events, for example by logging them separately and then discarding them.

For more information, see the `Apache Flink documentation <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/datastream/operators/windows/>`_.

Another concept closely related to windows in Apache Flink is *watermarks*. For more information on watermarks, see the `Apache Flink documentation <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/datastream/event-time/generating_watermarks/>`_.


Checkpoints
-----------

To achieve resilience and fault tolerance, Apache Flink uses *checkpoints* with stateful functions. These checkpoints allow Flink to recover the state and position within the stream and provide failure-free execution for applications.

Essentially, a checkpoint creates a snapshot of the data stream and stores it. The snapshots then provide a mechanism to recover from unexpected job failures. Compared to traditional database systems, checkpoints are closer to recovery logs than to backups.

For more information, see the `Apache Flink documentation <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/ops/state/checkpoints/>`_.


