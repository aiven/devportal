Aiven for M3
============

What is Aiven for M3?
---------------------

Aiven for M3 is a fully managed **distributed time series database**, deployable in the cloud of your choice which can bring unlimited scalability and high-availability to your monitoring environment and other time series applications.

Aiven for M3 consists of  ``n`` number of **M3DB** and **M3 Coordinator** pairs (where  ``n`` is the number of nodes as chosen for your Aiven plan). 


Why M3?
-------

M3 is a specialized time series store which is a great choice if your organization has a very large volume of metrics to handle, and it can be used as part of your observability solution. It is optimized for storing and serving time series through associated pairs of times and values. It also provides a reverse index of time series. 

.. note::
   Aiven offers M3 because we ourselves needed a solution that would work with the size of our own metrics - and we love it!

Read more about `the M3 components <https://m3db.io/docs/overview/components/>`_.


Get started with Aiven for M3
-----------------------------

Take your first steps with Aiven for M3 by following our :doc:`getting-started` article, or browse through our full list of articles:


.. panels::

    📚 :doc:`concepts`

    ---

    💻 :doc:`howto`


Integrates with your existing tools
------------------------------------

M3 is highly compatible with other Aiven products for the following tasks:

- To collect metrics with Prometheus, M3 is designed as a scalable storage backend.

- To write metrics directly from your applications using the InfluxDB-compatible wire protocol.

- To create dashboards and query available features using Grafana and PromQL.

Check out all the features on our `M3 product page <https://aiven.io/m3#full-feature-list>`_. 




Ways to use Aiven for M3
------------------------
Handle and analyse the time-stamped data from multiple connected devices and services, scale up as needed, and compare datasets to provide insights into past and present.

With Aiven for M3, you can set up the following example solutions:

- Monitor IoT deployments, applications performance, financial trends.

- Detect problems, respond promptly to incidents and plan maintenance.

- Provide fast data ingest and queries, with strong data compression.



M3 resources
------------

If you are new to M3, we recommend the following resources to get you started with the platform:

* Read about the `overview of the M3DB, M3 query and M3 aggregator components <https://m3db.io/docs/overview/components/>`_ on the main M3DB project documentation.

* From the upstream project:

  - Using M3DB with `Prometheus <https://m3db.io/docs/integrations/prometheus/>`_

  - Ingesting data from `Graphite <https://m3db.io/docs/integrations/graphite/>`_

  - Integrating M3DB with `Grafana <https://m3db.io/docs/integrations/grafana/>`_

  - Writing to M3DB using `InfluxDB protocol <https://m3db.io/docs/integrations/influx/>`_
