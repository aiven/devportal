Dynamic disk sizing
====================

Dynamic disk sizing (DDS) allows you to add or remove additional storage to your services from within the `Aiven web console <https://console.aiven.io/>`_. You can add additional storage during service creation or on-demand without interruption to meet the growing business needs. 

Dynamic Disk Sizing (DDS) is available for the following services:

- Aiven for Apache Kafka®
- Aiven for PostgreSQL®
- Aiven for MySQL®
- Aiven for OpenSearch®
- Aiven for Apache Cassandra®
- Aiven for M3DB®

.. note::

    Dynamic Disk Sizing is not supported on custom plans.

Why dynamic disk sizing?
------------------------
When creating a service on Aiven, you have a fixed pre-defined storage allocation based on your plan selection. However, when running your Service, there is a possibility that you may soon realize the need for scaling up the storage alone.

Predicting future growth and storage requirements can sometimes be challenging, and upgrading your service plans for additional storage requirements alone may not be feasible. Upgrading the service plans means paying for more compute resources (or RAM) that your current usage does not require. 

To cater to the needs of additional storage requirements on-demand, Aiven provides you the option of Dynamic Disk Sizing to manage storage dynamically.  

Using DDS provides the following benefits: 

- Provides an easy way to increase the disk storage available with the selected service plan.
- You can dynamically add or remove additional storage without disrupting your running service.
- It is cost-effective, as you pay only for the additional storage, not the compute resources that would have been part of an upgraded service plan. 

How does Dynamic Disk Sizing work?
----------------------------------
You can :doc:`add additional disk storage <../howto/add-storage-space>` to your service plan when you create a new service on the `Aiven web console <https://console.aiven.io/>`_ or on-demand when you need more storage while running your service. Adding additional storage will not affect or interrupt the operations of your service. 

When you add additional storage to your service, the Aiven platform provisions additional disk storage and dynamically adds it to your running instances. The total amount of additional storage you can add to your service is based on your service plan and the cloud provider.

In a clustered service (Cassandra or Kafka), the additional storage added will be equally divided between the nodes. In a shared service, each node receives the total shared capacity of the additional storage added. All the additional storage added will remain usable.

Pricing for dynamic disk sizing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Suppose you add additional storage at the time of service creation. In that case, the cost is calculated based on the total amount of additional storage added in GB and included as part of your service's total cost. It is also visible in the service summary.

Likewise, the cost of adding storage on-demand when your service is running is visible on the Aiven web console when you add storage. 

The total price you see is the cost of the additional storage and any backups associated with it. You can also see the additional storage usage costs in your invoices.

Limitations
~~~~~~~~~~~
- The maximum available additional storage capacity is based on your service plan and the cloud provider.
- Each time additional storage is added to the running service, an additional disk is added to the corresponding nodes. Since the cloud providers may limit the maximum number of disks attached to a node, this limits the number of times you can add additional storage. If this limit is reached, you will see a prompt to perform a maintenance update for performance optimization. You can add additional storage two times until the maximum storage limit is reached.  Therefore, we advise you to plan to add a sufficient amount of disk capacity. 
- If there is an ongoing Maintenance update, you will not be able to add additional storage until the maintenance is completed. 


Next steps
----------
For infromation on how to add additonal disk storage to your service from the `Aiven web console <https://console.aiven.io/>`_, see :doc:`Add additional storage <../howto/add-storage-space>`. 


.. note:: 

    It is unlikely that any performance degradation from additional disk storage would be noticeable in your clients, but it is possible.

