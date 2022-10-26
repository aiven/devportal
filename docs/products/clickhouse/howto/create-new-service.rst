Create and connect to a managed ClickHouse® service
==========================================

Check out how to create a new ClickHouse® service in the Aiven console. Learn how to add a database and connect to the service.

Prerequisites
-------------

* Aiven account (access to the console)
* `Python 3.7 or later <https://www.python.org/downloads/>`_ and the `pip package manager <https://pypi.org/project/pip/>`_ (to connect to the service)

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
   :width: 800px
   :alt: Set up your service's properties

.. note:: 
  The pricing for the same service may vary between different providers and regions. The **Service summary** box on the right side of the console shows the pricing for your selected options.

4. Verify your choices in the **Service summary** box and, if your setup looks as expected, select select **+ Create service** at the bottom of the box.

   As a result, **Overview** of your new service opens and you can see your service in the **Rebuilding** status, its connection parameters, and configuration options. Once the service is ready, the status changes to **Running**. While services typically start up in a couple of minutes, the performance varies between cloud providers and regions.

.. note::
    You can :ref:`create a service using the Aiven CLI <avn-cli-service-create>` as well.

.. _create db:

Create a database
-----------------

1. When the service is running, go to the **Databases & Tables** tab.

2. Enter a name for your database and select **Create database**.

.. note::

    All databases must be created through the web console.

Connect to ClickHouse® with Aiven CLI
-------------------------------------

1. In your terminal, install Aiven CLI and authenticate as a user according to instructions in :doc:`Getting started </docs/tools/cli>`.

   .. code:: bash
      
      python3 -m pip install aiven-client

      python3 -m aiven.client user login name.surname@example.io

      python3 -m aiven.client user login name.surname@example.io --token

2. Connect to the service by running command

   .. code:: bash

      python3 -m aiven.client service cli SERVICE-NAME

3. Verify if the :ref:`database you created <create db>` is there by running

   .. code:: bash

      avn service database-list SERVICE-NAME

   In the output you should get a list of databases available for your service.

.. seealso::
   For more information, see the `Aiven CLI documentation <https://docs.aiven.io/docs/tools/cli.html>`_ or open an issue in the `Aiven CLI GitHub repository <https://github.com/aiven/aiven-client>`_.

Next steps
----------

Now that you have your service and connection set up, see our :doc:`sample dataset article </docs/products/clickhouse/sample-dataset>` to try out your service with actual data.
