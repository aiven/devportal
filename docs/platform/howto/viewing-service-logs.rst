Viewing service logs
====================

Accessing logs from Aiven service: PostgreSQL, Kafka, Cassandra, Redis, InfluxDB

Occasionally there is a need to inspect logs from Aiven services. For example, to debug query performance or inspecting errors caused by a specific workload.

There are three built-in ways to inspect service logs at Aiven:

* In `Aiven console <https://console.aiven.io/>`_, when selecting a specific service, under "Logs" tab recent events are available. Logs can be browsed back in time, but scrolling up several thousand lines is not very convenient.

* `Aiven command-line client <https://github.com/aiven/aiven-client>`_ supports programmatically downloading logs. avn service logs -S desc -f --project your-project-name your-service-name will show all stored logs.

* `Aiven API <https://api.aiven.io/doc/#operation/ProjectGetServiceLogs>`_ endpoint is available for fetching the same information two above methods output, in case programmatic access is needed.

Service logs included on the normal service price are stored only for a few days. Unless you are using logs integration to another service, older logs are not accessible.

If longer retention time or more comprehensive analytics or search functionality is needed, managed Elasticsearch service on Aiven. This will allow you to configure longer retention times for your service logs, only limited by disk space available on the Elasticsearch plan you have selected. Elasticsearch together with Kibana offers comprehensive logs browsing and analytics platform.
