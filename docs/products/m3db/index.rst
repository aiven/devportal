M3DB welcome
============

M3DB is an open source, **distributed time series database**. It's ideal for organisations that have a very large volume of metrics to handle. This platform was originally developed at Uber, so that gives an idea of the scale of metrics that it can handle.

M3DB plays nicely with other tools that might be in the stack already:

* Collect metrics with Prometheus; M3DB is designed as a scalable storage backend for Prometheus.
* Write metrics direct from your applications using the InfluxDB-compatible wire protocol.
* Dashboards and query features available using Grafana and PromQL.

First steps
-----------

Check out our :doc:`getting-started` guide for M3DB and take your first steps right away.


.. panels::

    📙 :doc:`concepts`

    ---

    💻 :doc:`howto`

.. tip::
   Aiven offers M3DB because we needed a solution this size for our own metrics - and we love it!

M3DB resources
--------------

If you are new to M3 then there are lots of great resources out there to get you started with the platform. Here's our recommended reading list:

* An excellent `overview of the M3DB, M3 query and M3 aggregator components <https://m3db.io/docs/overview/components/>`_ on the main M3DB project documentation.

* Also from the upstream project, guides for:

  - using M3DB with `Prometheus <https://m3db.io/docs/integrations/prometheus/>`_
  - ingesting data from `Graphite <https://m3db.io/docs/integrations/graphite/>`_
  - integrating M3DB with `Grafana <https://m3db.io/docs/integrations/grafana/>`_
  - writing to M3DB using `InfluxDB protocol <https://m3db.io/docs/integrations/influx/>`_
