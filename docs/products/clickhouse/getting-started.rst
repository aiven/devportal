Getting started
===============

The first step in using Aiven for ClickHouse is to create a service and a database that you can use to try out the service. You can do this in the `Aiven web console <https://console.aiven.io/>`_.

This example shows you how to create a new service, add a database to it, and use `Docker <https://www.docker.com/>`_ to connect to the service with the ClickHouse client.

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. Follow :doc:`these instructions </docs/platform/howto/create_new_service>` to create a new ClickHouse service.

   Once the service is ready, the status changes to *Running*. This typically takes a couple of minutes, depending on your selected cloud provider and region.

3. When the service is running, go to the *Databases & Tables* tab.

4. Enter a name for your database, then click **Create database**.

5. Go to the *Overview* tab and copy the **Host**, **Port**, **User**, and **Password** parameters that you need for connecting to the service.

6. Get the latest Docker image of `the ClickHouse client from Docker Hub <https://hub.docker.com/r/clickhouse/clickhouse-client>`_

7. Run the following command to connect to your service and run an SQL query on your database:

   .. code:: bash

       docker run --interactive \
       --rm clickhouse/clickhouse-client \
       --user USER-NAME \
       --password USER-PASSWORD \
       --host YOUR-HOST-NAME.aivencloud.com \
       --port YOUR-PORT \
       --secure \
       --query="YOUR SQL QUERY GOES HERE"

   For more information on using the ClickHouse client, see :doc:`this article <howto/use-cli>`.

Now that you have your service and connection set up, see our :doc:`sample dataset article <sample-dataset>` to try out your service with actual data.