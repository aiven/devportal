Add or remove storage 
=======================

With :doc:`Dynamic disk sizing <../concepts/dynamic-disk-sizing>` you can add or remove disk storage both when you create a service and later on-demand for a running service. This feature is not available for all service plans.

Add storage during new service creation
-----------------------------------------
You can add disk storage when :doc:`creating a new service <../howto/create_new_service>`. 

Add storage to a running service
---------------------------------
You can add storage to your running service from the `Aiven Console <https://console.aiven.io/>`_ without interrupting the service. 

#. In **Services**, select the service.

#. On the **Overview** tab in the **Service plan** section, click **Add storage**. 

4. On the **Upgrade service disk space** window, use the slider to add disk storage. The price shown for the additional storage includes backup costs.

5. Click **Save changes**. 

The additional storage is available for immediate use.  

.. warning::

   Storage optimization is performed at the next maintenance update after a change to the storage size. Due to cloud provider limitations, there is a limit on how many times storage can be increased between two maintenance updates. When this limit is reached, you need to perform a maintenance update for performance optimization. It's best to carefully plan increases to avoid reaching this limit.

Remove additional storage
---------------------------
You can remove storage that you previously added to a service. Before you remove storage: 

- Make sure the data in your service does not exceed your service plan's allocated storage. If it does, you will not be able to remove the additional storage. 
- Plan for the time it takes to recycle the nodes. The service will be in a rebalancing state after removing storage. The time it takes depends on the service. 

Follow these steps to remove added storage:

#. In **Services**, select the service.

#. On the **Overview** tab in the **Service plan** section, click **Edit** next to **Additional disk storage**. 

4. On the **Upgrade service disk space** window, use the slider to remove disk storage. 

   .. note::
      You can only remove storage that you previously added using this feature. If you want to downgrade further, you can :doc:`change your service plan </docs/platform/howto/scale-services>`.

5. Click **Save changes**. 

Your service will be in a **Rebalancing** state while the nodes are being recycled. 
