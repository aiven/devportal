Event and processing times
==========================

Event time refers to when events actually happen, while processing time refers to when events are observed within a system. Various factors affect how events are processed, including shared hardware resources and network congestion, distributed system logic, and variances in the data throughput and order. Because of this, there can be significant differences between the event time and processing time for an event, even though ideally they would be equal.

In Apache Flink®, the streamed data does not always arrive in the same order as the events occurred. This means that using processing time in your applications can cause issues in system behavior. For this reason, we recommend that you use event time to process data, as it allows your applications to maintain the correct event sequence throughout the data streaming pipeline. In addition, using event time to process your data allows you to reprocess the data later on with consistent results.

For more information, see the `Apache Flink® documentation on event time and processing time <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/concepts/time/>`_.


