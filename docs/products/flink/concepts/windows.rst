Windows
=======

Apache Flink® uses *windows* to split the streamed data into segments that can be processed. Due to the unbounded nature of data streams, there is never a situation where *all* of the data is available, because you would be waiting indefinitely for new data points to arrive - so instead, windowing offers a way to define a subset of data points that you can then process and analyze.

A window is created when the first element matching the criteria that is set for it appears. The window's trigger defines when the window is considered ready for processing, and the function set for the window specifies how to process the data. Each window also has an allowed lateness value - this indicates how long new events are accepted for inclusion in the window after the trigger closes it.

For example, you can set 15:00 as the start time for a time-based window, with the end timestamp set to 15:10 and an allowed lateness of 1 minute. The first event with a timestamp between 15:00 and 15:10 creates the window, and any event that arrives between 15:10 and 15:11 with a timestamp between 15:00 and 15:10 is still included in the window.

Events may still arrive after the allowed lateness for the window, so your application should include a means of handling those events, for example by logging them separately and then discarding them.

For more information, see the `Apache Flink® documentation on windows <https://ci.apache.org/projects/flink/flink-docs-release-1.15/docs/dev/datastream/operators/windows/>`_.


