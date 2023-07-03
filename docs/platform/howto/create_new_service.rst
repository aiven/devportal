Create a new service
====================

Follow these steps to create a new service in the `Aiven Console <https://console.aiven.io/>`_.  You can also :ref:`create a service using the Aiven CLI <avn-cli-service-create>`.

#. In the project you want to create a service in, go to **Services**.

#. On the **Current services** page, click **Create service**.

#. Select the service that you want to create.

#. Select the cloud provider and region that you want to run your service on.

   .. note:: 
	   The pricing for the same service may vary between different providers and regions. The service summary shows you the pricing for your selected options.

#. Select a service plan. This determines the number of servers and what kind of memory, CPU, and disk resources are allocated to your service.

#. Add :doc:`disk storage <../concepts/dynamic-disk-sizing>` for your service by using the slider, if needed. The cost for the additional storage is in the service summary section.  

   .. note::
      It's not possible to add storage space for all cloud environments and service plans.

#. Enter a name for your service. 

#. Click **Create service**.

The new service opens on the **Overview** tab, where you can find the connection parameters for your service, its current status, and the configuration options.

The status is **Rebuilding** while the service is being created. Once the service is ready, the status changes to **Running**. While services typically start up in a couple of minutes, the performance varies between cloud providers and regions, and it may take longer.