Tiered storage overview in Aiven Console
========================================

Aiven for Apache Kafka® offers a comprehensive overview of tiered storage, allowing you to understand its usage and make informed decisions. This overview provides insights into various aspects of tiered storage, including billing, settings, and storage details.

.. important:: 
    
   Aiven for Apache Kafka® tiered storage is an early availability feature, which means it has some restrictions on the functionality and service level agreement. It is intended for non-production environments, but you can test it with production-like workloads to assess the performance. To enable this feature, navigate to the :doc:`Feature preview </docs/platform/howto/feature-preview>` page within your user profile.


Access tiered storage overview
--------------------------------

1. In the Aiven Console, choose your project and select your Aiven for Apache Kafka service.
2. From the left sidebar, select **Tiered Storage**. This action will display an overview of tiered storage and its associated details.


Key insights of tiered storage
------------------------------

Get a quick snapshot of the essential metrics and details related to tiered storage:

- **Current billing expenses in USD**: Stay informed about your current tiered storage expenses.
- **Forecasted month cost in USD**: Estimate your upcoming monthly costs based on current usage.
- **Data tiered in bytes**: View the volume of data that has been tiered.
- **Storage overview**: Understand the specifics of the storage mediums in use, including details about the used object storage and SSD storage.


Current tiered storage configurations
---------------------------------------------

This section provides an overview of the current local cache details and retention policy configurations for tiered storage:

- **Local cache**: Shows the current cache configuration.
- **Default local retention time (ms)**: Shows the current local data retention set in milliseconds.
- **Default local retention bytes**: Shows the configured volume of data, in bytes, for local retention.

.. _modify-retention-polices:

Modify retention policies 
`````````````````````````````````

1. In the **Tiered storage settings** section, select the ellipsis (three dots) and select **Update tiered storage settings**.
2. Within **Update tiered storage settings** page, adjust the values for:
   
   - Local Cache
   - Default Local Retention Time (ms)
   - Default Local Retention Bytes
  
3. Confirm your adjustments by selecting **Save changes**.



Graphical view of tiered storage costs
------------------------------------------

Gain a visual understanding of your tiered storage expenses:

- **Hourly expense**: Visualize your hourly expenses through graphical representation.
- **Total Cost and forecast**: Get a clear picture of your overall costs and receive a forecast based on current trends.



Graphical view of tiered storage costs
------------------------------------------

Gain a visual understanding of your tiered storage expenses:

- **Hourly expense**: Visualize your hourly expenses through graphical representation.
- **Total cost and forecast**: Gain insights into your overall costs and receive a forecast. This forecast is an estimate based on your most recent usage patterns and trends. It provides an indicative projection and should not be considered as an exact or fixed value.


Detailed storage overview
-------------------------

Explore the specifics of your storage usage and configurations:

- **Used object storage and SSD storage**:Take a deep dive into the storage mediums in use.
- **Filter by topic**: Narrow down your view to specific topics for focused insights.

