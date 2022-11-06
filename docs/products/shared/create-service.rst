Create a new |Service| service
==============================

You can add services for the various Aiven products in the Aiven web console.

.. raw:: html

    <iframe width="712" height="400" src="https://video.aiven.io/watch/2cQUuV7pxtSWabGMmwkGYJ?" frameborder="0" allowfullscreen></iframe>

.. raw:: html

    <iframe width="712" height="600" src="https://video.aiven.io/watch/2cQUuV7pxtSWabGMmwkGYJ?" frameborder="0" allowfullscreen></iframe>

.. raw:: html

    <iframe width="712" height="500" src="https://video.aiven.io/watch/2cQUuV7pxtSWabGMmwkGYJ?" allowfullscreen></iframe>

.. raw:: html

    <iframe width="800" height="400" src="https://video.aiven.io/watch/2cQUuV7pxtSWabGMmwkGYJ?" frameborder="50" allowfullscreen></iframe>

.. raw:: html

    <iframe width="750" height="550" src="https://video.aiven.io/watch/2cQUuV7pxtSWabGMmwkGYJ?" frameborder="0" allowfullscreen></iframe>

.. raw:: html

    <iframe width="750" height="550" src="https://video.aiven.io/watch/2cQUuV7pxtSWabGMmwkGYJ?" frameborder="100" allowfullscreen></iframe>

.. raw:: html

    <iframe width="750" height="550" src="https://video.aiven.io/watch/2cQUuV7pxtSWabGMmwkGYJ?" allowfullscreen></iframe>

To create a new |Service| service:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. On the **Services** page, select **Create a new service**.

   This opens a new page with the available service options.

3. Select the main properties for your service:

   a. Select the service type.

      If there are several versions available, select the version that you want to use. By default, the latest available version is selected.

   b. Select the cloud provider and region that you want to run your |Service| service on.

      .. note:: 
	      The pricing for the same service may vary between different providers and regions. The service summary on the right side of the console shows you the pricing for your selected options.

   c. Select a service plan.

      This defines the number of servers and what kind of memory, CPU, and disk resources are allocated to your |Service| service.

   d. Add additional disk space
      
      Configure :doc:`additional disk storage <../concepts/dynamic-disk-sizing>` for your service by using the slider and selecting the desired additional disk capacity. You can also see the cost for the additional storage on the right side and in the Service summary section on the console.  

      .. note::
         The option of adding storage space is not available for all cloud environments and |Service| service plans.

   e.  Enter a name for your service.

      A random name is provided by default, but you can enter a more recognizable name to distinguish it from other services.


4. Select **Create Service** under the summary on the right side of the console.

   This brings you back to the **Services** view. Your new |Service| service is listed with a status indicator to show that it is being created.

5. Click the service name.

   The **Overview** page for the service opens.

   This view shows you the connection parameters for your |Service| service, its current status, and the configuration options.

   The status is *Rebuilding* while the service is being created for you. Once the service is ready, the status changes to *Running*. While services typically start up in a couple of minutes, the performance varies between cloud providers and regions, and it may take longer in some circumstances.

.. note::
    You can :ref:`create a service using the Aiven CLI <avn-cli-service-create>` as well.
