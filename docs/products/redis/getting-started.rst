Get started with Aiven for Redis™*
==================================

The first step in using Aiven for Redis™* is to create a service. You can do so either using the `Aiven Web Console <https://console.aiven.io/>`_ or the `Aiven CLI <https://github.com/aiven/aiven-client>`_.

Create a Redis™* service using the Aiven web console
----------------------------------------------------
1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. Follow :doc:`these instructions </docs/platform/howto/create_new_service>` to create a new Redis service.

   Once the service is ready, the status changes to *Running*. This typically takes a couple of minutes, depending on your selected cloud provider and region.

Create a Redis™* service using the Aiven CLI
--------------------------------------------

If you prefer launching a new service from the CLI, `Aiven CLI <https://github.com/aiven/aiven-client>`_ includes a command for doing so. 

In order to launch a service, decide on the service plan, cloud provider, and region you want to run your service on. Then run the following command to create a **Redis™\*** service named ``demo-redis``: 

::

      avn service create demo-redis       \
         --service-type redis             \
         --cloud CLOUD_AND_REGION         \
         --plan PLAN                      \
         --project PROJECT_NAME 

.. note::
   See the full list of default flags with the following command: ``avn service create -h``. Additionally, there are some type specific options, which you can see executing the following command: ``avn service types -v`` 

Next steps
----------

* Learn how to connect to Aiven for Redis by using different programming languages:
   - :doc:`Go <howto/connect-go>`
   - :doc:`Node <howto/connect-node>`
   - :doc:`PHP <howto/connect-php>`
   - :doc:`Python <howto/connect-python>`

Check out more technical information:

* :doc:`High availability in Aiven for Redis <concepts/high-availability-redis>`.

  Learn about how Aiven for Redis supports high availability.

* :doc:`Manage SSL connectivity <howto/manage-ssl-connectivity>`.

  Check how Aiven for Redis supports SSL connections and how can be configured.

* :doc:`Memory usage, on-disk persistence and replication in Aiven for Redis <concepts/memory-usage>`.

  See how Aiven for Redis solves the challenges related to high memory usage and high change rate.

* :doc:`Estimate maximum number of connections in Aiven for Redis <howto/estimate-max-number-of-connections>`.

  Learn how estimate the max number of simultaneous connections in Aiven for Redis service.

* :doc:`Lua scripts with Aiven for Redis <concepts/lua-scripts-redis>`.

  Learn about inbuilt support for running Lua scripts in Aiven for Redis service.
