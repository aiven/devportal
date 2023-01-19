Aiven for Flink applications
============================

Aiven for Flink Applications are containers that include all elements related to a Flink job and help build your data processing pipeline, such as source and sink tables, data processing logic, and other necessary metadata. Applications are the starting point for running a Flink job within the Aiven Flink service. The `Aiven Console <https://console.aiven.io/>`_ provides a user-friendly, guided wizard to help you build and deploy applications, create source and sink tables, write transformation statements, and validate and ingest data using the interactive query feature.

Each application created and deployed in the Aiven for Apache Flink service performs a specific task making it easy to manage and understand different applications within the Aiven for Apache Flink service. For example, you can create an application to get user IDs from one topic and publish them on another topic.

Additionally, you create new versions of an application for specific tasks or functions. However,  only one version of an application can run at a time. You can run multiple applications within the Aiven for Apache Flink service.
Applications significantly improve the developer experience and simplify the development and deployment of Flink applications.

Features of Aiven for Flink applications
----------------------------------------
Some of key feature of Aiven for Flink applications include: 

* **Intuitive Interface:** The Aiven console provides a user-friendly, guided wizard to help you quickly build and deploy your applications.
* **Source and sink tables:** You can easily create source and sink tables and write transformation statements to transform data.
* **Interactive query:**  The interactive query feature allows you to validate and preview your data before deploying it.
* **Start and stop:** You can easily stop and start your application anytime.
* **Versioning:** You can create new versions of your application for different purposes.
* **Savepoints:** You can stop your application with savepoints, allowing you to restart it to a previous state at a later time.
* **Scalability:** You can scale your cluster depending on the demands of your specific application by parallelizing the applications into multiple tasks and executing them concurrently in a cluster.

Limitations 
------------
* **Concurrent applications:** You can create and run up to 4 concurrent applications in the Aiven for Apache Flink service.
* **Savepoints:** You can store up to 10 savepoints history per application deployment, allowing you to easily roll back to previous versions of your application if necessary. If you exceed this limit, you must clear the savepoints history before creating a new application version.

Flink Application status
------------------------
Flink applications can have different statuses based on their current execution status. The status of a Flink application is closely related to the state of its savepoints.

* **Running:** Indicates that the application is currently running and can be viewed with its version.
* **Finished:** Indicates that the application has been stopped with a savepoint.
* **Canceled:** Status indicates that the application has been stopped without a savepoint,
* **Failed:** Indicates that the application has failed to run.

Additionally, there are transient statuses such as:

* **SAVING_AND_STOP:** Indicates that the application version is being saved in a savepoint, and the application is being stopped.
* **CANCELLING_REQUESTED:** Indicates that application is in the process of being stopped without a savepoint.
* **DELETE_REQUESTE:** Indicates the application has been requested to be deleted.

