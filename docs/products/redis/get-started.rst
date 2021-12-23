Get started with Aiven for Redis
================================

Aiven for Redis services are managed from the `Aiven
Console <https://console.aiven.io/>`__. Create a new Aiven for Redis service by following the steps laid out in :doc:`this article </docs/platform/howto/create_new_service>`.

Once the service creation is initiated, you can go to its dedicated service page where the new service is shown with an indicator that it is being created.

Click the service name in the list to go to the **Overview** page. The **Overview** tab shows the connection parameters for your Redis service and its current status. You can make changes to the service configuration in **Overview** > **Advanced configuration**, even while the service is being built. You can find the available configuration options on the :doc:`reference page <reference/advanced-params>`.

The "Status" indicator says **REBUILDING** while the service is
being created. Once the service is up and running, the light changes to
green and the indicator says **RUNNING**.

.. note::
   Services typically start in a couple of minutes, the performance between clouds varies and it can take longer under some circumstances.

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

* :doc:`SSL connectivity <concepts/ssl-connectivity>`.

  Check how Aiven for Redis supports SSL connections and how can be configured.

* :doc:`Memory usage, on-disk persistence and replication in Aiven for Redis <concepts/memory-usage>`.

  See how Aiven for Redis solves the challenges related to high memory usage and high change rate.

* :doc:`Estimate maximum number of connections in Aiven for Redis <howto/estimate-max-number-of-connections>`.

  Learn how estimate the max number of simultaneous connections in Aiven for Redis service.
  

* :doc:`Lua scripts with Aiven for Redis <concepts/lua-scripts-redis>`.

  Learn about inbuilt support for running Lua scripts in Aiven for Redis service.
  
