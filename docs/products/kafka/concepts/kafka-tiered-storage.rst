Tiered storage in Aiven for Apache Kafka®
===========================================

Discover the tiered storage capability in Aiven for Apache Kafka®. Learn how it works and explore its use cases. Check why you might need it and what benefits you get using it.

Overview
---------

Tiered storage provides the ability to use multiple storage types to store data, such as local disk and cloud storage, based on how frequently it is accessed. With Aiven for Apache Kafka, you can use tiered storage to allocate some of your data to high-speed local disks and move the rest to more cost-efficient remote storage options like AWS S3 and Google Cloud Storage.  

Tiered storage offers multiple benefits, including:

* **Scalability:** Tiered storage allows Aiven for Apache Kafka instances to scale almost infinitely with cloud solutions, eliminating concerns about storage limitations.
* **Cost efficiency:** By moving less frequently accessed data to cost-effective storage tiers, you can realize significant financial savings.
* **Operational speed:** With the bulk of data offloaded to remote storage, service rebalancing in Aiven for Apache Kafka becomes faster, making for a smoother operational experience.
* **Infinite data retention:** With the scalability of cloud storage, you can achieve unlimited data retention, valuable for analytics and compliance.
* **Transparency:** Even older Kafka clients can benefit from tiered storage without needing to be explicitly aware of it.

When and why to use it
------------------------

Understanding when and why to use tiered storage in Aiven for Apache Kafka will help you maximize its benefits, particularly around cost savings and system performance. 

**Scenarios for use:**

* **Long-term data retention**: Many organizations require large-scale data storage for extended periods, either for regulatory compliance or historical data analysis. Cloud services provide an almost limitless storage capacity, making it possible to keep data accessible for as long as required at a reasonable cost. This is where tiered storage becomes especially valuable.
* **High-speed data ingestion**: Tiered storage can offer a solution when dealing with unpredictable or sudden influxes of data. By supplementing the local disks with cloud storage, sudden increases in incoming data can be managed, ensuring optimum system performance. 


Security
--------
Segments are encrypted with 256-bit AES encryption before being uploaded to the remote storage. The encryption keys are not shared with the cloud storage provider and generally do not leave Aiven machines.

Pricing
-------
Tiered storage costs are determined by the amount of remote storage used, measured in GB/hour. The highest usage level within each hour is the basis for calculating charges.




