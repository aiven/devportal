Dynamic Disk Sizing
====================

Dynamic disk sizing (DDS) allows you to adjust the amount of disk space for your service from within the Aiven Console by adding additional disk storage. 
With Dynamic disk sizing, you can add additional storage to your services at the time of service creation or on-demand without interruption to meet the growing business needs. 

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
You can add additional disk storage to your service plan when you create a new service on the Aiven console or on-demand when you need more storage while running your service. Adding additional storage will not affect or interrupt the operations of your service. 

When you add additional storage to your service, the Aiven platform provisions additional disk storage and dynamically adds it to your running instances. The total amount of additional storage you can add to your service is based on your service plan and the cloud provider.

In a clustered service (Cassandra or Kafka), the additional storage added will be equally divided between the nodes. In a shared service, each node receives the total shared capacity of the additional storage added. All the additional storage added will remain usable.

Pricing for dynamic disk sizing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you include additional storage at the time of service creation, the additional storage cost is included as part of your service's total cost. It is also visible in the service summary.

If you add additional storage on-demand when your service is running, the cost is calculated based on the total amount of additional storage in GB.

The total price you see is the cost of the storage and any backups associated with it. You can also see the additional storage usage costs in your invoices.

Limitations
~~~~~~~~~~~
- The maximum available additional storage capacity is based on your service plan and the cloud provider.
- Each time additional storage is added to the running service, an additional disk is added to the corresponding nodes. Since the cloud providers may limit the maximum number of disks attached to a node, this limits the number of times you can add additional storage. If this limit is reached, you will see a prompt to perform a maintenance update for performance optimization. You can add additional storage two times until the maximum storage limit is reached.

Next steps
----------
For infromation on how to add additonal disk storage to your service from the Aiven web console, see How to add additional storage. 


.. note:: 

    It is unlikely that any performance degradation from using network attached storage would be noticeable in your clients but it is a possibility. 

