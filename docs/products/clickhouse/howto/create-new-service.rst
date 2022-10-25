Creating and connecting to a managed ClickHouse® service
==========================================

Check out how to create a new ClickHouse® service in the Aiven console. Learn how to add a database and connect to the service.

Prerequisites
^^^^^^^^^^^^^

* Aiven account
* `Docker <https://www.docker.com/>`_ (to connect to the service with the ClickHouse® client)

Create a ClickHouse® service
---------------------------

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. From **Current services** view, select **Create service**.

3. In the **Create service** view, set up your new service's properties.

  1. Service type (**ClickHouse®**)
    
  2. Cloud provider

  3. Cloud region

  4. Service plan (number of servers, kind of memory, CPU, and disk resources)

  5. Additional disk space

  6. Service name

.. image:: /images/products/clickhouse/ch-create-service.png
   :width: 500px
   :alt: Set up your service's properties

.. note:: 
  The pricing for the same service may vary between different providers and regions. The **Service summary** box on the right side of the console shows the pricing for your selected options.

4. Verify your choices in the **Service summary** box and, if your setup looks as expected, select select **+ Create service** at the bottom of the box.

   As a result, **Overview** of your new service opens and you can see your service in the **Rebuilding** status, its connection parameters, and configuration options. Once the service is ready, the status changes to **Running**. While services typically start up in a couple of minutes, the performance varies between cloud providers and regions.

.. note::
    You can :ref:`create a service using the Aiven CLI <avn-cli-service-create>` as well.

Create a database
-----------------

1. When the service is running, go to the **Databases & Tables** tab.

2. Enter a name for your database and select **Create database**.

.. note::

    All databases must be created through the web console.

Connect to ClickHouse®
---------------------

1. Get the latest Docker image of `the ClickHouse® client from Docker Hub <https://hub.docker.com/r/clickhouse/clickhouse-client>`_.

2. In the Aiven console, go to the **Overview** tab for your service and copy the **Host**, **Port**, **User**, and **Password** parameters.

.. image:: /images/products/clickhouse/ch-create-db.png
   :width: 500px
   :alt: Copy service parameters

3. To connect to your service and run SQL queries on your database, run the following command substituting the placeholders for ``USERNAME``, ``PASSWORD``, ``HOST`` and ``PORT``:

   .. code:: bash

       docker run -it                       \
       --rm clickhouse/clickhouse-client    \
       --user USERNAME                      \
       --password PASSWORD                  \
       --host HOST                          \
       --port PORT                          \
       --secure

For more information on using the ClickHouse® client, see :doc:`this article </docs/products/clickhouse/howto/use-cli>`.

Next steps
----------

Now that you have your service and connection set up, see our :doc:`sample dataset article </docs/products/clickhouse/sample-dataset>` to try out your service with actual data.
