Custom JARs in Aiven for Apache Flink®
=================================================

Aiven for Apache Flink® allows you to upload, deploy, and manage your own Java code with custom JARs. This feature aims to expand the capabilities of Aiven for Apache Flink, allowing you to add custom functions that extend beyond the typical SQL-based features. With Custom JARs, you can swiftly develop and maximize the potential of your Aiven for Flink application.

What are custom JARs?
-------------------------
Java ARchive (JAR) files are package files used in Java to aggregate many class files, metadata, and resources like text and images into a single file for distribution. Custom JARs are Java Archive files containing custom code and resources developed for specific functionalities outside standard Java or Apache Flink libraries.


Why use custom JARs?
---------------------
Using Custom JARs in Aiven for Apache Flink offers several key benefits:

* **Enhanced functionality:** Using custom JARs, you can extend the native capabilities of your Aiven for Apache Flink service, incorporating functionalities that go beyond the core Flink APIs.
* **Code reusability:** This feature allows you to seamlessly reuse and integrate your existing Java code into your Aiven for Apache Flink applications.
* **Simplified management:** The need to deploy and manage separate Flink service is significantly reduced, as custom functionalities can be directly used within the Aiven for Apache Flink application.

Use cases
--------------

Custom JARs can be applied in various scenarios, including but not limited to:

* **Custom data processing and enrichment:** Custom JARs facilitate the processing and enrichment of data from sources not natively supported by Flink's core APIs. This includes implementing unique data processing logic and applying custom functions for data transformation and enrichment.
* **Connector customization:** With custom JARs, it is possible to create and integrate unique connectors tailored to specific data integration needs. This feature enables users to develop and deploy connectors that are not available in Flink's standard offerings, providing a more flexible and customized data flow within their applications.


Related reading
-----------------
* How to use custom JARs in Aiven for Apache Flink application 

