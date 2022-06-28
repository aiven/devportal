Dynamic Disk Sizing
====================

When running a service, you may soon fill up the storage available and notice that the other resources are not limited. Upgrading your plan is an option but then you are paying for additional compute resources (or RAM) that your current usage does not require.

Dynamic Disk Sizing (DDS) is a feature available for: 
- Aiven for Apache Kafka
- Aiven for PostgreSQL
- Aiven for MySQL
- Aiven for OpenSearch
- Aiven for Apache Cassandra
- Aiven for M3DB

You can add up to 2x the original storage amount to any plan, allowing you 3x the initial storage amount. For example, if you are deploying a business-4 PostgreSQL service, the default storage is 80GB, and you can add up to 160GB of additional storage, to give a total of 240GB.

The price you see is the cost of the storage, as well as any backups associated with it.

.. note::
    Dynamic Disk Sizing is not supported on custom plans

How does Dynamic Disk Sizing work?
----------------------------------

When increasing storage, the Aiven platform provisions additional network attached storage and dynamically adds it to your running instances. Your services are not affected or interrupted and you can continue to use your service as normal. 

You can add storage at the time you create a new service. Once created, you can add (and remove) DDS storage by selecting `Edit` or `Add Storage` under the `Service Plan` section of your `Service Overview`` page.

.. note:: 
    It is unlikely that any performance degradation from using network attached storage would be noticeable in your clients but it is a possibility. 

