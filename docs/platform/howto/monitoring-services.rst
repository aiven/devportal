Monitoring services
===================

When running Aiven services, you get access by default to both metrics and logs to monitor the health of your service from the `Aiven console <https://console.aiven.io/>`_.

1. From the left sidebar, navigate to **Services** and select the service you want to review.
2. To review metrics, select **Metrics** from the left sidebar. You can select a time range spanning the last hour, day, week, month, or year.
3. For log analysis, select **Logs** from the left sidebar. Older logs will load progressively. To return to the most recent log entry, select **Go to most recent message**.


You can also use the dedicated functions :ref:`service logs <avn-service-logs>` and :ref:`service metrics <avn-service-metrics>` to export your service's monitoring data via the :doc:`Aiven CLI </docs/tools/cli>`.

Additionaly, you have the option to :doc:`export logs and metrics to an Aiven service or external provider</docs/platform/concepts/logs-metrics-alerts>`, expanding your monitoring capabilities. For example:

- You can send logs to :doc:`Aiven for Opensearch</docs/products/opensearch>`.
- You can send metrics to :doc:`Aiven for m3</docs/products/m3db>`, and visualise these metrics with :doc:`Aiven for Grafana</docs/products/grafana>`.


