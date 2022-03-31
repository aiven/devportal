Setup Apache Kafka® MirrorMaker 2 monitoring
============================================

The metrics about replication flows run by Aiven for Apache Kafka® MirrorMaker 2 are collected and can be exported via a metric integration.

Setup a metric integration to an Aiven for InfluxDB® service
------------------------------------------------------------

The setup of an integration pushing the Aiven for Apache Kafka MirrorMaker 2 metrics into an existing Aiven for InfluxDB® service can be performed via both the `Aiven console <https://console.aiven.io/>`_ or the :ref:`Aiven CLI <avn_service_integration_create>`.

The following example demonstrate how to push the metrics of an Aiven for Apache Kafka MirrorMaker 2 service named ``mirrormaker-demo`` into an Aiven for InfluxDB service named ``influxdb-demo`` via the :ref:`Aiven CLI <avn_service_integration_create>`.

::

    avn service integration-create      \
            -t influxdb-demo            \
            -s mirrormaker-demo         \
            -d influxdb

Once the integration is created the Apache Kafka MirrorMaker 2 metrics will flow into the Aiven for InfluxDB service in the measurement named ``kafka_mirrormaker_summary`` and can, for example, be visualised using :doc:`Aiven for Grafana® </docs/products/grafana/index>`

.. image:: /images/products/kafka/kafka-mirrormaker/grafana-mirrormaker2-lag.png
   :alt: Grafana® Dashboard showing MirrorMaker 2 replica lag per topic
