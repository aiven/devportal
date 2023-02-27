Request service custom plans
============================

Aiven stock plans are designed to cover most common use cases. The plans are tested and configurations optimized to work well across the different clouds.

Sometimes, for special use cases like very high throughput clusters, the stock plans might not be an optimal fit. In such cases we can create custom plans where the default service configurations are modified to best fit your needs.

.. Note::

   Custom plans can be made available for all the Aiven services types (as example Aiven for Apache Kafka® or Aiven for PostgreSQL®). 
   
   The custom plan starting price is 500 USD/month.

Custom plan variables
---------------------

The following are the variables which may be adjusted in custom plans:

* Amount of storage
* Amount and frequency of backups
* Amount of nodes
* CPU/RAM configuration per node

The possible configurations depend on several factors, such as the selected cloud provider, the region, the available instance types and the service type in
question.

For example, available memory and CPU configurations may depend on restrictions imposed by the cloud provider and the instance types available in the region.

Please feel free to contact us via sales@Aiven.io for a quote and the availability of a custom plan.

Custom plan request
-------------------

For the custom plan request, please provide:

* The **region** and **cloud** you would like the custom plan in (e.g. Google cloud, ``us-east1``)
* The **service type** (e.g. "Kafka" or "PostgreSQL")
* The name of the **Aiven project** you would like the custom plan available for
* The custom attributes changed vs a stock plan (e.g. "a PostgreSQL ``business-4`` but with 900 GB of storage")