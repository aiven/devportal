Getting started with Aiven for ClickHouse® |beta|
=================================================

The first step in using Aiven for ClickHouse® is to create a service and a database that you can use to try out the service. You can do this in the `Aiven web console <https://console.aiven.io/>`_.

This example shows you how to create a new service, add a database to it, and use `Docker <https://www.docker.com/>`_ to connect to the service with the ClickHouse client.

Create a ClickHouse service
---------------------------

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. Follow :doc:`these instructions </docs/platform/howto/create_new_service>` to create a new ClickHouse service.

   Once the service is ready, the status changes to *Running*. This typically takes a couple of minutes, depending on your selected cloud provider and region.


Create a database
-----------------

1. When the service is running, go to the *Databases & Tables* tab.

2. Enter a name for your database, then click **Create database**.

.. note::

    All databases must be created through the web console.


Connect to ClickHouse
---------------------

1. Get the latest Docker image of `the ClickHouse client from Docker Hub <https://hub.docker.com/r/clickhouse/clickhouse-client>`_

2. Go to the *Overview* tab and copy the **Host**, **Port**, **User**, and **Password** parameters that you need for connecting to the service.

3. Run the following command to connect to your service and run SQL queries on your database, substitute the placeholders for ``USERNAME``, ``PASSWORD``, ``HOST`` and ``PORT``:

   .. code:: bash

       docker run -it                       \
       --rm clickhouse/clickhouse-client    \
       --user USERNAME                      \
       --password PASSWORD                  \
       --host HOST                          \
       --port PORT                          \
       --secure

For more information on using the ClickHouse client, see :doc:`this article <howto/connect-with-clickhouse-cli>`.

Next steps
----------

Now that you have your service and connection set up, see our :doc:`sample dataset article <sample-dataset>` to try out your service with actual data.
