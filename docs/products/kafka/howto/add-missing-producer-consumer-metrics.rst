Add client-side Apache Kafka® producer and consumer Datadog metrics
===================================================================

When you enable the :doc:`Datadog integration </docs/integrations/datadog/datadog-metrics>` in Aiven for Apache Kafka®, the service supports all of the broker-side metrics listed in the `Datadog Kafka integration documentation <https://docs.datadoghq.com/integrations/kafka/?tab=host#data-collected>`_ and allows you to send additional :doc:`custom metrics <datadog-customised-metrics>`.

Additionally, you can collect client-side metrics directly from the producer or consumer and send them to Datadog. For guidance, refer to the *Missing producer and consumer metrics* section in the `Datadog documentation <https://docs.datadoghq.com/integrations/faq/troubleshooting-and-deep-dive-for-kafka>`_, which outlines the process for integrating missing metrics natively for Java-based producers and consumers. For clients using languages other than Java, incorporating these metrics can be achieved through `DogStatsD <https://docs.datadoghq.com/developers/dogstatsd/>`_.
