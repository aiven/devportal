Watermarks
==========

Another concept closely related to windows and event time in Apache Flink is *watermarks*. Flink uses watermarks as a mechanism to measure progress in event time; they flow as part of the data stream, carrying a timestamp that declares the minimum event time reached in the data stream.

This allows Flink to set points in the stream when all events up to a certain timestamp should have arrived, so that operators can set their internal event time to the value of the watermarks that reach them.

For example, the following diagram shows how watermarks fit into an out-of-order stream, where the events are not ordered by their timestamps:

.. mermaid::

    graph TD;

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

For more information on watermarks, see the `Apache Flink documentation on generating watermarks <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/datastream/event-time/generating_watermarks/>`_.


