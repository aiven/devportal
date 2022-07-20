Add ``kafka.producer.`` and ``kafka.consumer`` Datadog metrics
==============================================================

When you enable the :doc:`Datadog integration </docs/integrations/datadog/datadog-metrics>` in Aiven for Apache Kafka®, the service supports all of the broker-side metrics listed in the `Datadog Kafka integration documentation <https://docs.datadoghq.com/integrations/kafka/?tab=host#data-collected>`_ and allows you to send additional :doc:`custom metrics <datadog-customised-metrics>`.

However, all metrics that have a prefix like ``kafka.producer.*`` or ``kafka.consumer.*`` are client-side metrics and **require a connecting the Datadog agent to the Java producer or consumer processes**.

A setup where the Datadog agent running on the Apache Kafka nodes polls the application code processes is only feasible in environments where Apache Kafka brokers and clients are self hosted and available at specific IP addresses. 

Enabling Datadog to poll external processes would lower the security of a managed service like Aiven for Apache Kafka®. Therefore, Aiven does not support gathering client-side metrics with the Datadog integration. 

Add ``kafka.producer.`` and ``kafka.consumer`` metrics
------------------------------------------------------

The dedicated `Datadog documentation <https://docs.datadoghq.com/integrations/faq/troubleshooting-and-deep-dive-for-kafka>`_ (see "Missing producer and consumer metrics" chapter) provides a way to include the missing metrics natively for Java based producers and consumers or via `DogStatsD <https://docs.datadoghq.com/developers/dogstatsd/>`_ for clients in other languages.
