Get started with Aiven for Apache Cassandra®
============================================

The first step in using Aiven for Apache Cassandra® is to create a service. You can do so either using `Aiven Console <https://console.aiven.io/>`_ or the `Aiven CLI <https://github.com/aiven/aiven-client>`_.

Create an Aiven for Apache Cassandra service using the Aiven Console
--------------------------------------------------------------------

1. Log in to the `Aiven Console <https://console.aiven.io/>`_.

2. Follow :doc:`these instructions </docs/platform/howto/create_new_service>` to create a new Aiven for Apache Cassandra service.

   Once the service is ready, the status changes to *Running*. This typically takes a couple of minutes, depending on your selected cloud provider and region.

Create an Aiven for Apache Cassandra service using the Aiven CLI
----------------------------------------------------------------

If you prefer launching a new service from the CLI, `Aiven CLI <https://github.com/aiven/aiven-client>`_ includes a command for doing so. 

In order to launch a service, decide on the service plan, cloud provider, and region you want to run your service on. Then run the following command to create an Aiven for Apache Cassandra service named ``demo-cassandra``: 

::

      avn service create demo-cassandra       \
         --service-type cassandra             \
         --cloud CLOUD_AND_REGION             \
         --plan PLAN                          \
         --project PROJECT_NAME 

.. note::

   See the full list of default flags using the ``avn service create -h`` command. Additionally, there are some type-specific options, which you can see executing the ``avn service types -v`` command.
