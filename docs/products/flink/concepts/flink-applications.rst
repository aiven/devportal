Aiven for Apache Flink® applications
====================================

An Aiven for Apache Flink® Application is an abstraction layer that simplifies building data processing pipelines in Apache Flink. It supports two types of applications:

* **SQL applications:**  Built on top of Apache Flink SQL, these applications include elements like source and sink table definitions, data processing logic using SQL, deployment parameters, and other necessary metadata.
* **JAR applications:** This type allows users to upload and deploy custom JAR files, enabling the integration of custom code and resources for specialized functionalities beyond the standard Flink capabilities.

:doc:`Applications </docs/products/flink/howto/create-flink-applications>` are the starting point for running an Apache Flink job within the Aiven managed service. The `Aiven Console <https://console.aiven.io/>`_ provides a user-friendly, guided wizard to help you build and deploy applications, create source and sink tables, write transformation statements, and validate and ingest data using the interactive query feature.

Each application whether SQL or JAR-based, is designed to perform specific data transformation tasks, allowing you to map and manage different workflows within the Aiven for Apache Flink service. For example, you can create a SQL application to process user IDs from one topic and publish them on another, or use a custom JAR application for more specialized data processing needs.

Applications significantly improve the developer experience and simplify the development and deployment of Flink applications. Applications are **automatically versioned** on every edit of the underline definition (tables, transformation SQL, or custom JARs), allowing you to experiment with new transformations and revert to a previously stored definition if the result of the edits doesn't meet expectations. 

.. seealso::
    For infromation on how to create applications, see :doc:`Create an Aiven for Apache Flink® application </docs/products/flink/howto/create-flink-applications>`


Application features
-----------------------------------------------

Some of key feature of Aiven for Flink applications include: 

* **Intuitive interface**: The `Aiven Console <https://console.aiven.io/>`_ provides a user-friendly, guided wizard for building and deploying applications.
* **Source and sink tables** definition with **SQL autocomplete**: For SQL applications, create source and sink tables with guidance from SQL autocomplete based on connector types.
* **Interactive query**: For SQL applications, the interactive query feature allows you to validate and preview your data in the table or SQL transformation before deploying it.
* **Start and stop**: You can start and stop applications stop and start anytime.
* **Versioning**: Creating a new application version after editing the table or data transformation definition allows you to track changes and revert to a previous version when needed.
* **Savepoints**: You can stop your application with a savepoint, allowing you to restart it from the previous state at a later time.
* **Scalability:** You can parallelize the workload into multiple tasks and executing them concurrently in a cluster

Limitations 
------------

* **Concurrent applications:** You can create and run up to 4 concurrent applications in the Aiven for Apache Flink service.
* **Savepoints:** You can store up to 10 savepoints history per application deployment, allowing you to start from a previous state if necessary. If you exceed this limit, you must clear the savepoints history before creating a new application deployment.

Application status
-----------------------------------------

Flink applications can have different statuses based on their execution and savepoint state. Below are the most common statuses you may encounter:

* **CANCELED**: Your application has stopped without creating a savepoint.
* **CREATED**: Your application has been created but has yet to start running.
* **FAILED**: Your application attempted to run but was unsuccessful.
* **FINISHED**: Your application has completed its execution and stopped, with a savepoint created.
* **INITIALIZING**: Your application is in the process of being initialized and preparing to run.
* **RUNNING**: Your application is actively running. You can view its current version.
* **RESTARTING**: Your application is being restarted.
* **SAVING_AND_STOP**: Your application is currently saving its current state in a savepoint and then stopping.

Other statuses and transient statuses include:

* **CANCELLING_REQUESTED**: A stop request for your application has been made without creating a savepoint.
* **CANCELLING**: Your application is currently being stopped.
* **DELETE_REQUESTED**: A request to delete your application has been initiated.
* **DELETING**: Your application is in the process of being removed.
* **FAILING**: Your application is encountering issues and failing.
* **RESTARTING**: Your application is undergoing a restart process.
* **SAVING**: Your application is creating a savepoint.
* **SAVING_AND_STOP_REQUESTED**: A request has been made to save the current state of your application in a savepoint and then stop it.
* **SUSPENDED**: Your application has been suspended. 
