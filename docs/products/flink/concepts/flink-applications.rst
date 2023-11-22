Aiven for Apache Flink® applications
====================================

An Aiven for Apache Flink® Application is an abstraction layer on top of Apache Flink SQL that includes all the elements related to a Flink job to help build your data processing pipeline. An application contains the definition of source and sink tables, data processing logic, deployment parameters, and other necessary metadata. 

:doc:`Applications `/docs/products/flink/howto/create-flink-applications` are the starting point for running an Apache Flink job within the Aiven managed service. The `Aiven Console <https://console.aiven.io/>`_ provides a user-friendly, guided wizard to help you build and deploy applications, create source and sink tables, write transformation statements, and validate and ingest data using the interactive query feature.

Each application created and deployed in the Aiven for Apache Flink service performs a specific data transformation task allowing you to map and manage different workflows separately within the Aiven for Apache Flink service. For example, you can create an application to get user IDs from one topic and publish them on another topic. You can run multiple applications within the Aiven for Apache Flink service.

Applications significantly improve the developer experience and simplify the development and deployment of Flink applications. Applications are **automatically versioned** on every edit of the underline definition (tables, or transformation SQL), allowing you to experiment with new transformations and revert to a previously stored definition if the result of the edits doesn't meet expectations. 

.. seealso::
    For infromation on how to create applications, see :doc:`Create an Aiven for Apache Flink® application `/docs/products/flink/howto/create-flink-applications`


Features of Aiven for Apache Flink applications
-----------------------------------------------

Some of key feature of Aiven for Flink applications include: 

* **Intuitive Interface**: The `Aiven Console <https://console.aiven.io/>`_ provides a user-friendly, guided wizard to help you quickly build and deploy your applications.
* **Source and sink tables** definition with **SQL autocomplete**: You can create source and sink tables, the SQL autocomplete feature allows you to start from a specific set of pre-filled parameters depending on the type of connector.
* **Interactive query**: The interactive query feature allows you to validate and preview your data in the table or SQL transformation before deploying it.
* **Start and stop**: You can start and stop applications stop and start anytime.
* **Versioning**: By creating a new application version every time you edit the table or data transformation definition, you can keep track of changes and have the ability to revert to a previous version if needed.
* **Savepoints**: You can stop your application with a savepoint, allowing you to restart it from the previous state at a later time.
* **Scalability:** You can parallelize the workload into multiple tasks and executing them concurrently in a cluster

Limitations 
------------

* **Concurrent applications:** You can create and run up to 4 concurrent applications in the Aiven for Apache Flink service.
* **Savepoints:** You can store up to 10 savepoints history per application deployment, allowing you to start from a previous state if necessary. If you exceed this limit, you must clear the savepoints history before creating a new application deployment.

Aiven for Apache Flink application status
-----------------------------------------

Flink applications can have different statuses based on their current execution status. The status of a Flink application is closely related to the state of its savepoints. The most common statuses you will see in the application on Aiven Console include: 

* **CANCELED:** the application has been stopped without a savepoint. 
* **CREATED:** the application has been created but has yet to start running.
* **FAILED:** the application has failed to run. 
* **FINISHED:** the application has been stopped with a savepoint. 
* **INITIALIZING:** the application is in the process of being initialized.
* **RUNNING:** the application is currently running and can be viewed with its version.
* **RESTARTING:** the application is in the process of being restarted. 
* **SAVING_AND_STOP:** the application version is being saved in a savepoint, and the application is being stopped.

Other statuses and transient statuses include:

* **CANCELLING_REQUESTED:** the application is in the process of being stopped without a savepoint.
* **CANCELLING:** the application is in the process of being cancelled.
* **DELETE_REQUESTED:** application has been requested to be deleted.
* **DELETING:** the application is in the process of being deleted.
* **FAILING:** the application is in the process of failing.
* **RESTARTING:** the application is in the process of being restarted.
* **SAVING:** the application is in the process of creating a savepoint.
* **SAVING_AND_STOP_REQUESTED:** the application is in the process of creating a savepoint and stopping.
* **SUSPENDED:** the application has been suspended.

