Access service logs
===================

Occasionally, there is the need to inspect logs from Aiven services. For example, to debug query performance or inspecting errors caused by a specific workload.

There are three built-in ways to inspect service logs at Aiven:

* For recent events, go to `Aiven Console <https://console.aiven.io/>`_ > your service's page > **Logs** view (available from the sidebat)

  .. Tip::

     Logs can be browsed back in time, but scrolling up several thousand lines is not very convenient.

* For downloading logs rogrammatically with the :ref:`dedicated command <avn-service-logs>`, use :doc:`Aiven CLI </docs/tools/cli>` supports

* For fetching the same information two above methods output, if the programmatic access is needed, use the `ProjectGetServiceLogs API <https://api.aiven.io/doc/#operation/ProjectGetServiceLogs>`_ endpoint.

Log retention policy
--------------------

Service logs are generally retained for a few days, and for some Aiven services up to 14 days maximum. Unless you are using :doc:`logs integration </docs/integrations>` to another service, older logs are not accessible.

If longer retention time or more comprehensive analytics or search functionality is needed, you can setup a :doc:`log integration with an Aiven for OpenSearch® service </docs/products/opensearch/howto/opensearch-log-integration>`. The integration allows you to configure longer retention times for your service logs, only limited by the disk space available on the Aiven for OpenSearch® plan you have selected. OpenSearch® together with OpenSearch® Dashboards offers comprehensive logs browsing and analytics platform.
