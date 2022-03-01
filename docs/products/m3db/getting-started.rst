Getting started
===============

There are two M3-related services available in the `Aiven console <https://console.aiven.io>`_. Get started with an **M3DB** service; this is the part that stores data.

.. note::
   The M3 Aggregator service provides extra query functionality when performing complex queries against the distributed data set

Choose your cloud provider and region to deploy to, then choose which plan to use.

If you're just trying out M3DB, a single-node setup is available with our startup plans. This isn't recommended for production use however; for that you should try the 3-node clusters on the business plans, or a premium plan to meet your needs. Remember that you can scale up your plan whenever you need to so don't worry if you aren't sure about the details up front.

Finally, give the service a name and then select "Create Service", and your shiny new M3 database will start building. While it does that, you can already visit the service overview page to see the details of the service.

.. image:: /images/products/m3db/m3db-connection-details.png

Connection details
------------------

The connection information on the main service overview tab contains sections for each of the main ways of connecting to M3DB.

**M3 Coordinator** is the endpoint for a direct connection.

**InfluxDB®** protocol is also supported by M3DB. This means you can use a new or existing InfluxDB application to store data in M3DB instead.

**Prometheus** gets two entries since the read and write operations are on different paths.

**Graphite** section shows the details you will need to connect with Graphite.
