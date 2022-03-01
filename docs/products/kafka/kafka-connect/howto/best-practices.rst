Get the best from Apache Kafka® Connect
=======================================

We recommend to follow these best practices to ensure that your Apache Kafka® Connect service is fast and reliable.

Pay attention to ``tasks.max`` for connector configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, connectors run a maximum of **1** task, which usually leads
to under-utilization for large Apache Kafka Connect services (unless you have
many connectors with one task each). In general, it is good to keep the
cluster CPUs occupied with connector tasks without overloading them. If
your connector is under-performing, you can try increasing ``tasks.max``
to match the number of partitions.

Consider a standalone Apache Kafka Connect service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can run Apache Kafka Connect as part of your existing Aiven for Apache
Kafka service (for *business-4* and higher service plans). While this
allows you to try out Apache Kafka Connect by enabling the feature within your
existing service, for heavy usage we recommend that you enable a
standalone Apache Kafka Connect service to run your connectors. This allows you
to scale the Apache Kafka service and the connector service independently and
offers more CPU time and memory for the Apache Kafka Connect service.

Having a dedicated cluster that moves the data and does not add load to the main nodes goes according to the "separation of concerns" paradigm.
