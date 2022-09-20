Add additional storage 
=======================

You can add additional storage at the time of new service creation or on-demand to a running service. This section provides you with information on how to add additional storage. 
For more information, see :doc:`Dynamic disk sizing <../concepts/dynamic-disk-sizing>` . 

Add additional storage during new service creation
--------------------------------------------------
You can add additional storage when creating a new service. For information on how to add additional storage during new service creation, see :doc:`Create a new service <../howto/create_new_service>`. 

Add additional storage to running service
-----------------------------------------
You can add additional storage to your running service from the Aiven web console without interrupting the service. 

1. Log in to the `Aiven Console <https://console.aiven.io/>`_, and go to **Services** to select your running service. 
2. In the **Overview** tab, scroll down to **Service plan**.
3. Click **Add storage**. 

   .. image:: /images/platform/howto/add-addition-storage.png
      :alt: Add additional storage 

   .. note:: 
      This feature is not available for all service plans. 
4. In the **Upgrade service disk space** pop-up window, use the slider under **Additional disk storage** to add extra disk capacity. As you add storage, you can also see the cost associated with the storage. The price you see is the cost of the storage, as well as any backup associated with it.
   
   .. image:: /images/platform/howto/upgrade-service-disk-space.png
      :alt: Add additional storage using the slider

5. Click **Save changes**. The additional storage is added  and available for immediate use.  

.. note:: 
   Depending on the service type, the amount of storage you can add in increments varies. For example, some services allow you to add storage in 10GB increments, while others allow 30GB increments. 

.. warning:: 
   The number of times you can add additional storage is limited to two times until the maximum storage limit is reached. When you exceed this limit, you will see a notification to perform a maintenance update to optimize disk performance. As a result, we recommend you plan to add sufficient disk capacity each time.

Decrease or remove additional storage
-------------------------------------
Depending on the business requirements, you can decrease or remove additional storage added.

Before you decrease or remove the additional storage on your service: 

- Ensure the amount of data in the additional storage does not exceed your service plan's allocated storage. If the data exceeds the allocated storage, you will not be able to decrease or remove the additional storage. 
- Decreasing the additional storage capacity or setting it to **None** recycles the nodes and, therefore, can take a moderate amount of time, depending on the service. We advise you to plan this task.   

Follow these steps to decrease or remove the added storage:

1. In the `Aiven Console <https://console.aiven.io/>`_, select your **Service**. 
2. In the **Overview** tab of the service, scroll down to **Service plan**. 
3. Click **Edit** next to **Additional disk storage**. 
4. On the **Upgrade service disk space** pop-up window, use the slider under **Additional disk storage** to reduce the additional disk storage capacity or set it to None. 
5. Click **Save changes**. 

   Your service will be in a **Rebalancing** state, indicating the nodes are being recycled. 

