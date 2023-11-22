Dynamic Disk Sizing (DDS)
=========================

Dynamic Disk Sizing (DDS) allows you to add storage to or remove storage from your services. You can add storage during service creation. You can also add it later to a running service without interruption. 

DDS is available for the following services:

- Aiven for Apache Kafka®
- Aiven for PostgreSQL®
- Aiven for MySQL®
- Aiven for OpenSearch®
- Aiven for Apache Cassandra®
- Aiven for M3DB®

.. note::

    DDS is not supported on custom plans.

Why use DDS?
-------------
When creating a service on Aiven, you have a fixed storage allocation based on the plan you choose. Predicting future growth and storage requirements can sometimes be challenging. Upgrading the service plans means paying for more compute resources (or RAM). However, if you only need additional storage, DDS lets you add storage to meet your requirements without upgrading the plan.

Using DDS provides the following benefits: 

- Provides an easy way to increase the disk storage available with the selected service plan.
- You can dynamically add or remove storage without disrupting your running service.
- It is cost-effective as you pay only for the additional storage not the compute resources that are part of an upgraded service plan. 

How does DDS work?
-------------------
You can add disk storage to your service plan when you :doc:`create a new service </docs/platform/howto/create_new_service>` or on demand when you need more storage while :doc:`running your service </docs/platform/howto/add-storage-space>`. Adding storage will not affect or interrupt the operations of your service. 

When you add storage to your service, the Aiven platform provisions the extra disk space and dynamically adds it to your running instances. The total amount of storage you can add to your service is based on your service plan and the cloud provider.

In a clustered service such as Apache Cassandra or Apache Kafka, the additional storage is equally divided between the nodes. In a shared service, each node receives the total shared capacity of the added storage. 

Pricing  
~~~~~~~~
If you add storage when you create a service, the cost is included as part of your service's total cost and is shown in the service summary. 

The cost of adding storage to a running service is shown in `Aiven Console <https://console.aiven.io/>`_ when you add it. The total price you see is the cost of the additional storage and any backups associated with it. You can also see these storage usage costs in your invoices.

Limitations
~~~~~~~~~~~

- Maximum storage size depends on the plan and the service type. It can go as high as five times the base storage size of the plan. 
- Due to cloud provider restrictions, there is a limit on how many times storage can be increased between two maintenance updates. If this limit is reached, you need to perform a maintenance update for performance optimization.
- If there is an ongoing maintenance update, you cannot add storage until the update is completed.

It is unlikely that any performance degradation from additional disk storage would be noticeable in your clients, but it is possible.

Next steps
----------
For instructions on how to add or remove disk storage in `Aiven Console <https://console.aiven.io/>`_, see :doc:`Add or remove storage </docs/platform/howto/add-storage-space>`. 
