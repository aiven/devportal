Add or remove storage 
=======================

With :doc:`dynamic disk sizing </docs/platform/concepts/dynamic-disk-sizing>`, you can add or remove disk storage (by factor of 10 GiB) both when you create a service and later for a running service.

.. note::
  
   - You cannot add or remove storage when service nodes are in the rebalancing state, for example, during a maintenance update or a service upgrade.
   - This feature is not available for all service plans.

Use Aiven Console
-----------------

Add storage during new service creation
'''''''''''''''''''''''''''''''''''''''

You can add disk storage when :doc:`creating a new service </docs/platform/howto/create_new_service>`. 


Add storage to a running service
''''''''''''''''''''''''''''''''

You can add storage to your running service in `Aiven Console <https://console.aiven.io/>`_ without interrupting the service. 

1. Log into the `Aiven Console <https://console.aiven.io/>`_, select your project and then select the service for which you want to add storage.
2. On the service page, click **Service settings** from the sidebar. 
3. In the **Service plan** section, click **Actions (...)**. 
4. From the dropdown menu, select **Manage additional storage**. 
5. In the **Upgrade service storage** dialog, click **Change plan** choose the new service plan and tier or use the slider to add disk storage.

   .. note::
      
      The price shown for the additional storage includes backup costs.

9. Click **Save changes**.

.. topic:: Result
   
   The additional storage is available for immediate use.  

.. warning::

   Storage optimization is performed at the next maintenance update after a change to the storage size. Due to cloud provider limitations, there is a limit on how many times storage can be increased between two maintenance updates. When this limit is reached, you need to perform a maintenance update for performance optimization. It's best to carefully plan increases to avoid reaching this limit.

Remove additional storage
'''''''''''''''''''''''''

You can remove storage that you previously added to a service.

Before you start
""""""""""""""""

- Make sure the data in your service does not exceed your service plan's allocated storage. If it does, you will not be able to remove the additional storage. 
- Plan for the time it takes to recycle the nodes. The service will be in a rebalancing state after removing storage. The time it takes depends on the service. 

Remove added storage
""""""""""""""""""""

1. Log into the `Aiven Console <https://console.aiven.io/>`_, select your project and then select the service for which you want to add storage.
2. On the service page, click **Service settings** from the sidebar. 
3. In the **Service plan** section, click **Actions (...)**. 
4. From the dropdown menu, select **Manage additional storage**. 
5. In the **Upgrade service storage** dialog, use the slider to remove disk storage. 

   .. note::
      You can only remove storage that you previously added using this feature. If you want to downgrade further, you can :doc:`change your service plan </docs/platform/howto/scale-services>`.

6. Click **Save changes**. 

.. topic:: Result

   Your additional disk space has been removed. The service is in the **Rebalancing** state while the nodes are being recycled. 

Use Aiven CLI
-------------

You can use :doc:`Aiven CLI </docs/tools/cli>` to add or remove additional storage by :ref:`updating the service configuration <avn-cli-service-update>` using command ``avn service update`` with flag ``--disk-space-gib``. Specify the value for the flag as the total disk space that you need for your service.
For example, if you use a ``Startup-4`` plan with a 80-GiB disk by default and you would like to add an extra 10-GiB disk, the value that the ``--disk-space-gib`` flag requires is ``90``.

.. code-block:: bash

      avn service update --disk-space-gib 90 --project PROJECT_NAME SERVICE_NAME

.. note::

   - When you perform a service upgrade or downgrade horizontally, remember to include all additional disks the service uses. For example, when switching from ``Startup-4`` to ``Business-4`` or from ``Business-4`` to ``Startup-4``, include all the additional disks available for this service.
   
   - Similarly, when you fork an existing service, include all additional disks the service uses.