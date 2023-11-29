Aiven for Apache Cassandra® metrics available via Datadog
=========================================================

Learn what metrics are available via Datadog for Aiven for Apache Cassandra® services.

Request a metrics list for your service
---------------------------------------

You can retrieve the complete list of available metrics for your Aiven service by requesting the Datadog endpoint as follows:

.. code-block:: bash

    curl --cacert ca.pem \
        --user 'API_KEY' \
        'https://<CASSANDRA_HOSTNAME>:<DATADOG_PORT>/metrics'

Where you substitute the following:

* Aiven project certificate for ``ca.pem``
* Datadog endpoint API key for ``API_KEY``
* Aiven for Apache Cassandra hostname for ``<CASSANDRA_HOSTNAME>``
* Datadog port for ``<DATADOG_PORT>``

Get the standard list of Cassandra metrics in Datadog
-----------------------------------------------------

Check out `Metrics <https://docs.datadoghq.com/integrations/cassandra/#metrics>`_ for the full list of Apache Cassandra metrics available in Datadog.

Related reading
---------------

* Check how to use Datadog with Aiven services in :doc:`Datadog and Aiven </docs/integrations/datadog/>`.
* Check how to send metrics to Datadog from Aiven services in :doc:`Send metrics to Datadog </docs/integrations/datadog/datadog-metrics>`.
