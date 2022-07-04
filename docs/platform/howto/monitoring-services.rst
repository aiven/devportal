Monitoring services
===================

When running Aiven services, you get access by default to both metrics and logs to monitor the health of your service from the `Aiven console <https://console.aiven.io/>`_.

1. Go to your **Services**, and open the service you want to review.
2. Metrics can be reviewed under the **Metrics** tab, with the choice of spanning the last hour, day, week, month or year.
3. Logs can be reviewed under the **Logs** tab. Older logs are loaded progressively. To come back to the most recent log entry, click on **Got to most recent message**

You can also use the dedicated functions :ref:`service logs <avn-service-logs>` and :ref:`service metrics <avn-service-metrics>` to export your service's monitoring data via the :doc:`Aiven CLI </docs/tools/cli>`.

Note that it is also possible to :doc:`export logs and metrics to an Aiven service or external provider</docs/platform/concepts/logs-metrics-alerts>`. For instance:

    - Sending logs to :doc:`Aiven for Opensearch</docs/products/opensearch>`.
    - Sending metrics to :doc:`Aiven for m3</docs/products/m3db>`, and visualise these metrics with :doc:`Aiven for Grafana</docs/products/grafana>`.


