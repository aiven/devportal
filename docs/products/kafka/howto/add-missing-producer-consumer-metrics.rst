Add ``kafka.producer.`` and ``kafka.consumer`` Datadog metrics
==============================================================

When you enable the :doc:`Datadog integration </docs/integrations/datadog/datadog-metrics>` in Aiven for Apache Kafka®, the service supports all of the broker-side metrics listed in the `Datadog Kafka integration documentation <https://docs.datadoghq.com/integrations/kafka/?tab=host#data-collected>`_ and allows you to send additional :doc:`custom metrics <datadog-customised-metrics>`.

However, all metrics that have a prefix like ``kafka.producer.*`` or ``kafka.consumer.*`` are client-side metrics that should be collected from the producer or consumer, and sent to Datadog.

The dedicated `Datadog documentation <https://docs.datadoghq.com/integrations/faq/troubleshooting-and-deep-dive-for-kafka>`_ (see "Missing producer and consumer metrics" chapter) provides a way to include the missing metrics natively for Java based producers and consumers or via `DogStatsD <https://docs.datadoghq.com/developers/dogstatsd/>`_ for clients in other languages.
