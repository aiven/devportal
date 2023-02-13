Dynamic Disk Sizing
====================

Dynamic Disk Sizing (DDS) allows you to add or remove additional storage to your services from within the `Aiven Console <https://console.aiven.io/>`_. You can add additional storage during service creation or on-demand without interruption to meet the growing business needs. 

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
When creating a service on Aiven, you have a fixed pre-defined storage allocation based on your plan selection. However, when running your service, there is a possibility that you may soon realize the need for scaling up the storage alone.

Predicting future growth and storage requirements can sometimes be challenging, and upgrading your service plans for additional storage requirements alone may not be feasible. Upgrading the service plans means paying for more compute resources (or RAM) that your current usage does not require. 

To cater to the needs of additional storage requirements on-demand, Aiven provides you the option of Dynamic Disk Sizing to manage storage dynamically.  

Using DDS provides the following benefits: 

- Provides an easy way to increase the disk storage available with the selected service plan.
- You can dynamically add or remove additional storage without disrupting your running service.
- It is cost-effective, as you pay only for the additional storage, not the compute resources that would have been part of an upgraded service plan. 

How does Dynamic Disk Sizing work?
----------------------------------
You can add additional disk storage to your service plan when you :doc:`create a new service <../howto/create_new_service>` on the `Aiven Console <https://console.aiven.io/>`_ or on-demand when you need more storage while :doc:`running your service<../howto/add-storage-space>`. Adding additional storage will not affect or interrupt the operations of your service. 

When you add additional storage to your service, the Aiven platform provisions additional disk storage and dynamically adds it to your running instances. The total amount of additional storage you can add to your service is based on your service plan and the cloud provider.

In a clustered service (Apache Cassandra or Apache Kafka), the additional storage added will be equally divided between the nodes. In a shared service, each node receives the total shared capacity of the additional storage added. All the additional storage added will remain usable.

Pricing for dynamic disk sizing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Suppose you add additional storage at the time of service creation. In that case, the cost is calculated based on the total amount of additional storage added in GB and included as part of your service's total cost. It is also visible in the service summary.

Likewise, the cost of adding storage on-demand when your service is running is visible on the Aiven web console when you add storage. 

The total price you see is the cost of the additional storage and any backups associated with it. You can also see the additional storage usage costs in your invoices.

Limitations
~~~~~~~~~~~

- Maximum storage size depends on the plan and the service type and can go as high as five times the base storage size of the plan. 
- Storage optimization is performed at the next maintenance update after a change to the storage size. Due to limitations on the cloud provider, there is a limit on how many times storage can be increased between maintenance updates. If this limit is reached, you see a prompt to perform a maintenance update for performance optimization.

  .. tip::
    
    To avoid reaching the limit on how many times storage can be increased between maintenance updates, plan with foresigt to add a sufficient amount of the disk capacity.

- If there is an ongoing maintenance update, you cannot add additional storage until the maintenance is completed.

Next steps
----------
For information on how to add additional disk storage to your service from the `Aiven Console <https://console.aiven.io/>`_, see :doc:`Add additional storage <../howto/add-storage-space>`. 


.. note:: 

    It is unlikely that any performance degradation from additional disk storage would be noticeable in your clients, but it is possible.

