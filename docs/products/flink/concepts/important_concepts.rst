Important concepts in Apache Flink
==================================

This article gives you a brief explanation of some of the relevant terms and concepts in Apache Flink. A basic understanding of these helps you get the most out of our other Apache Flink articles.


Event and processing times
--------------------------

Event time refers to when events actually happen, while processing time refers to when events are observed within a system. Various factors affect how events are processed, including shared hardware resources and network congestion, distributed system logic, and variances in the data throughput and order. Because of this, there can be significant differences between the event time and processing time for an event, even though ideally they would be equal.

In Apache Flink, the streamed data does not always arrive in the same order as the events occurred. This means that using processing time in your applications can cause issues in system behavior. For this reason, we recommend that you use event time to process data, as it allows your applications to maintain the correct event sequence throughout the data streaming pipeline. In addition, using event time to process your data allows you to reprocess the data later on with consistent results.

For more information, see the `Apache Flink documentation <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/concepts/time/>`_.


Windows
-------

Apache Flink uses *windows* to split the streamed data into segments that can be processed. Due to the unbounded nature of data streams, there is never a situation where *all* of the data is available, because you would be waiting indefinitely for new data points to arrive - so instead, windowing offers a way to define a subset of data points that you can then process and analyze.

A window is created when the first element matching the criteria that is set for it appears. The window's trigger defines when the window is considered ready for processing, and the function set for the window specifies how to process the data. Each window also has an allowed lateness value - this indicates how long new events are accepted for inclusion in the window after the trigger closes it.

For example, you can set 15:00 as the start time for a time-based window, with the end timestamp set to 15:10 and an allowed lateness of 1 minute. The first event with a timestamp between 15:00 and 15:10 creates the window, and any event that arrives between 15:10 and 15:11 with a timestamp between 15:00 and 15:10 is still included in the window.

Events may still arrive after the allowed lateness for the window, so your application should include a means of handling those events, for example by logging them separately and then discarding them.

For more information, see the `Apache Flink documentation <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/datastream/operators/windows/>`_.


Watermarks
----------

Another concept closely related to windows and event time in Apache Flink is *watermarks*. Flink uses watermarks as a mechanism to measure progress in event time; they flow as part of the data stream, carrying a timestamp that declares the minimum event time reached in the data stream.

This allows Flink to set points in the stream when all events up to a certain timestamp should have arrived, so that operators can set their internal event time to the value of the watermarks that reach them.

For example, the following diagram shows how watermarks fit into an out-of-order stream, where the events are not ordered by their timestamps:

.. mermaid::

    graph LR;

        id1[/Data stream/]-->id2[21];
		id2 --- id3[19];
		id3-- watermark 17 ---id4[20];
		id4 --- id5[17];
		id5 --- id6[22];
		id6 --- id7[14];
		id7-- watermark 11 ---id8[12];
		id8 --- id9[9];
		id9 --- id10[15];
		id10 --- id11[11];
		id11-->id12[/Data stream/];


Flink uses *watermark strategies* and *watermark generators* to define how the watermark logic is implemented. For example, you can set Flink to generate watermarks either periodically at specific intervals or when triggered by an event or element with a specific marker.

For more information on watermarks, see the `Apache Flink documentation <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/datastream/event-time/generating_watermarks/>`_.


Checkpoints
-----------

To achieve resilience and fault tolerance, Apache Flink uses *checkpoints* with stateful functions. These checkpoints allow Flink to recover the state and position within the stream and provide failure-free execution for applications.

Essentially, a checkpoint creates a snapshot of the data stream and stores it. The snapshots then provide a mechanism to recover from unexpected job failures. Compared to traditional database systems, checkpoints are closer to recovery logs than to backups.

.. mermaid::

    graph LR;

        id5[/Older records in data stream/]-->id4[[Checkpoint barrier n-1]];
		id4 --- id3[(Checkpoint operator state)];
		id3 --- id2[[Checkpoint barrier n]];
		id2-->id1[/Newer records in data stream/];
        id3-->id6[(State backend)];


For more information, see the `Apache Flink documentation <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/ops/state/checkpoints/>`_.


