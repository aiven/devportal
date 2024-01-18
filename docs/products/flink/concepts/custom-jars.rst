Custom JARs in Aiven for Apache Flink®
=================================================

Aiven for Apache Flink enables you to upload, deploy, and manage your own Java code as custom JARs within a :doc:`JAR application </docs/products/flink/howto/create-jar-application>`.  This feature expands the capabilities of Aiven for Apache Flink, allowing you to add custom capabilities that extend beyond the default SQL features. With custom JARs, you can swiftly develop and maximize the potential of your Aiven for Flink application.

.. important:: 
  
    Custom JARs for Aiven for Apache Flink is a :doc:`limited availability feature </docs/platform/concepts/beta_services>`. If you're interested in trying out this feature, contact the sales team at sales@Aiven.io.

What are custom JARs?
-------------------------
Custom JARs are specialized Java Archive files containing code and resources for functionalities beyond standard Java or Apache Flink libraries. The capabilities of any custom JAR are defined by your organization and use cases, allowing for tailored solutions that meet specific technical requirements and objectives.


Why use custom JARs?
---------------------
Using Custom JARs in Aiven for Apache Flink offers several key benefits:

* **Enhanced functionality:** Using custom JARs, you can extend the native capabilities of your Aiven for Apache Flink service, incorporating functionalities that go beyond the core Flink APIs.
* **Code reuse:** This feature allows you to seamlessly reuse and integrate your existing Java code into your Aiven for Apache Flink applications.
* **Simplified management:** Aiven handles the complexities of hosting and operating a Flink service. This streamlined approach requires you only to upload and deploy the JAR file, enabling direct use of its functionalities within the Aiven for Apache Flink application.


Use cases
--------------

Custom JARs can be applied in various scenarios, including but not limited to:

* **Custom data processing and enrichment:** Custom JARs facilitate the processing and enrichment of data from sources not natively supported by Flink's core APIs. This includes implementing unique data processing logic and applying custom functions for data transformation and enrichment.


Related pages
--------------

* :doc:`How to use custom JARs in Aiven for Apache Flink application </docs/products/flink/howto/create-jar-application>`. 
  
