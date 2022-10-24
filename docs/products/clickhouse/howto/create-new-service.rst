Creating and connecting to a managed ClickHouse® service
==========================================

Check out how to create a new ClickHouse® service in the Aiven console. Learn how to add a database and connect to the service.

Prerequisites
_____________

* Aiven account
* `Docker <https://www.docker.com/>`_ (to connect to the service with the ClickHouse® client)

Create a ClickHouse® service
---------------------------

.. raw:: html

    <video width="500px" height="500px" controls="controls"/><source src="_static/clickhouse-create-service.mp4" type="video/mp4"></video>

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. From **Current services** view, select **Create service**.

3. In the **Create service** view, set up your new service's properties.

  1. Service type (**ClickHouse®**)
    
  2. Cloud provider

  3. Cloud region

  4. Service plan (number of servers, kind of memory, CPU, and disk resources)

  5. :doc:`additional disk storage <../concepts/dynamic-disk-sizing>`

  6. Service name

.. note:: 
  The pricing for the same service may vary between different providers and regions. The **Service summary** box on the right side of the console shows the pricing for your selected options.

4. Verify your choices in the **Service summary** box and, if your setup looks as expected, select select **+ Create service** at the bottom of the box.

   As a result, **Overview** of your new service opens and you can see your service in the **Rebuilding** status,its connection parameters, and configuration options. Once the service is ready, the status changes to **Running**. While services typically start up in a couple of minutes, the performance varies between cloud providers and regions.

.. note::
    You can :ref:`create a service using the Aiven CLI <avn-cli-service-create>` as well.

Create a database
-----------------

1. When the service is running, go to the *Databases & Tables* tab.

2. Enter a name for your database, then click **Create database**.

.. note::

    All databases must be created through the web console.


Connect to ClickHouse®
---------------------

1. Get the latest Docker image of `the ClickHouse® client from Docker Hub <https://hub.docker.com/r/clickhouse/clickhouse-client>`_

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

For more information on using the ClickHouse® client, see :doc:`this article <howto/use-cli>`.

Next steps
----------

Now that you have your service and connection set up, see our :doc:`sample dataset article <sample-dataset>` to try out your service with actual data.
