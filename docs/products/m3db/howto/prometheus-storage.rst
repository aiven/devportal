Use M3DB as remote storage for Prometheus
#########################################

M3DB is an excellent candidate for a highly scalable remote storage solution for your `Prometheus <https://prometheus.io/>`_ monitoring system. Many organisations are already using Prometheus and come to M3DB when they have outgrown their existing storage setup. With the ability to scale as needed and store large quantities of time series data, serving as back end storage for Prometheus is one of the main use cases for M3DB.

Configure M3DB to store data in Prometheus
------------------------------------------

1. Configure Prometheus to write its data to local storage. Copy the **Service URI** value from the **Prometheus (Write)** tab. In your Prometheus configuration file (mine is called ``prometheus.yml``), add the following section, replacing ``<PROM_WRITE_URL>`` with the URL you copied.

.. code:: yaml

    remote_write:
      - url: "<PROM_WRITE_URL>"

Prometheus is now configured to send data to your Aiven for M3 service.

2. So that you can still access the data using your existing Prometheus service, configure Prometheus with the ``remote_read`` configuration to read data from the remote storage. Copy the **Service URI** value from the **Prometheus (Read)** tab. In your Prometheus configuration file, add the following section, replacing ``<PROM_READ_URL>`` with the URL you copied.

.. code:: yaml

    remote_read:
      - url: "<PROM_READ_URL>"
        read_recent: true

The ``read_recent`` parameter makes Prometheus read all data from the remote storage; this is useful so that you can test that the setup is working. Without this setting, Prometheus will return the most recent data from local storage if it still has it there.

3. Run Prometheus, and check that data is flowing

.. tip::

    Try :doc:`visualizing your data with Grafana <grafana>` by following our guide.

