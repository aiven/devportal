Dynamic Disk Sizing
====================

Dynamic Disk Sizing (DDS) allows you to add storage to or remove storage from your services. You can add storage during service creation or later when service is running service without interruption. 

DDS is available for the following services:

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
When creating a service on Aiven, you have a fixed storage allocation based on your plan selection. When running your service, you may want to scale up only the storage.

Predicting future growth and storage requirements can sometimes be challenging, and upgrading your service plans for additional storage requirements alone may not be feasible. Upgrading the service plans means paying for more compute resources (or RAM) that your current usage does not require. DDS lets you add storage to meet your requirements.

Using DDS provides the following benefits: 

- Provides an easy way to increase the disk storage available with the selected service plan.
- You can dynamically add or remove storage without disrupting your running service.
- It is cost-effective as you pay only for the additional storage not the compute resources that are part of an upgraded service plan. 

How does Dynamic Disk Sizing work?
----------------------------------
You can add disk storage to your service plan when you :doc:`create a new service <../howto/create_new_service>` or on demand when you need more storage while :doc:`running your service<../howto/add-storage-space>`. Adding storage will not affect or interrupt the operations of your service. 

When you add storage to your service, the Aiven platform provisions the extra disk space and dynamically adds it to your running instances. The total amount of storage you can add to your service is based on your service plan and the cloud provider.

In a clustered service such as Apache Cassandra or Apache Kafka, the additional storage is equally divided between the nodes. In a shared service, each node receives the total shared capacity of the added storage. 

Pricing for dynamic disk sizing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you add storage when you create a service, the cost is included as part of your service's total cost and is shown in the service summary. The cost of adding storage to a running service is shown in the Aiven Console when you add it. 

The total price you see is the cost of the additional storage and any backups associated with it. You can also see these storage usage costs in your invoices.

Limitations
~~~~~~~~~~~

- Maximum storage size depends on the plan and the service type. It can go as high as five times the base storage size of the plan. 
- Storage optimization is performed at the next maintenance update after a change to the storage size. Due to limitations on the cloud provider, there is a limit on how many times storage can be increased between two maintenance updates. If this limit is reached, you see a prompt to perform a maintenance update for performance optimization.

.. topic:: Avoid hitting the limit of times you increase the storage
    
   Each time you increase the storage size, plan with foresight so that the amount of the disk space you add is sufficient and you don't need to add it again any time soon.

- If there is an ongoing maintenance update, you cannot add storage until the maintenance is completed.

It is unlikely that any performance degradation from additional disk storage would be noticeable in your clients, but it is possible.

Next steps
----------
For instructions on how to add or remove disk storage in the Aiven Console, see :doc:`Add or remove storage <../howto/add-storage-space>`. 
