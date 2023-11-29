Aiven for ClickHouse® metrics available via Datadog
===================================================

This article provides the list of all metrics available via Datadog for Aiven for ClickHouse® services.

You can retrieve the complete list of available metrics for your service by requesting the Datadog endpoint as follows:

.. code-block:: bash

    curl --cacert ca.pem \
        --user '<Datadog_USER>:<Datadog_PASSWORD>' \
        'https://<CASSANDRA_HOSTNAME>:<Datadog_PORT>/metrics'

Where you substitute the following:

* Aiven project certificate for ``ca.pem``
* Datadog credentials for ``<Datadog_USER>:<Datadog_PASSWORD>``
* Aiven for ClickHouse hostname for ``<CASSANDRA_HOSTNAME>``
* Datadog port for ``<Datadog_PORT>``

.. Tip::

    You can check how to use Datadog with Aiven in :doc:`Aiven and Datadog integration </docs/integrations/datadog/>`.
    See also :doc:`Increase metrics limit setting for Datadog </docs/platform/howto/integrations/datadog-increase-metrics-limit>`.
