Aiven for Apache Flink® limitation
==================================

There are likely differences between Aiven for Apache Flink and an Apache Flink service you run yourself. This is because Aiven for Apache Flink is a fully managed service. Aiven takes care of the underlying infrastructure and configuration tasks required to run a stable and reliable Flink service. 

Some of the differences you might see between Aiven for Apache Flink and a self-managed Flink service include:

- **User-defined functions:** Aiven for Apache Flink does not currently support using user-defined functions (UDFs).
- **Apache Flink CLI tool:** The Apache Flink® CLI tool is not currently supported as it requires access to the - JobManager in production, which is not exposed to customers.
- **Job-level settings:** In Aiven for Apache Flink, each job inherits the cluster-level settings, and job-level settings are not yet supported. You cannot specify separate settings for individual jobs within the same cluster.
- **Flame graphs:** Flame graphs are marked as an experimental feature in Apache Flink 1.15 and are not currently enabled in the Aiven for Apache Flink web UI.

