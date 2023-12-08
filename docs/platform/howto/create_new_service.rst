Create a new service
====================

Follow these steps to create a new service in `Aiven Console <https://console.aiven.io/>`_.  You can also :ref:`create a service using the Aiven CLI <avn-cli-service-create>`.

#. Log in to `Aiven Console <https://console.aiven.io/>`_.

#. Using the top navigation bar, go to the organization and the project that you want to create a service in.

#. On the project's page, make sure your in the **Services** view and select **Create service**.

#. From the **Select service** page, select the service that you want to create.

#. On the **Create service** page

   1. Select the cloud provider and region that you want to run your service on.

      .. note:: 

	      The pricing for the same service may vary between different providers and regions. The service summary shows you the pricing for your selected options.

   2. Select a service plan.

      .. note::

         This determines the number of servers and what kind of memory, CPU, and disk resources are allocated to your service. Check out `Plans & Pricing <https://aiven.io/pricing?product=pg>`_ for details.

   3. Add :doc:`disk storage </docs/platform/concepts/dynamic-disk-sizing>` for your service by using the slider, if needed. The cost for the additional storage is in the service summary section.  

      .. note::

         It's not possible to add storage space for all cloud environments and service plans.

   4. Enter a name for your service. 

   5. Select **Create service** from the right-side **Service Summary** card.

.. topic:: Result

   The new service opens on the **Overview** page, where you can find the connection parameters for your service, its current status, and the configuration options.

.. note:: 
   
   The service is in the **Rebuilding** status while it is being created. Once the service is ready, the status changes to **Running**. While services typically start up in a couple of minutes, the performance varies between cloud providers and regions, and it may take longer.
