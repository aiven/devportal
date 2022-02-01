Apache Flink® for data analysts
===============================

We're actively collating advice, tips, and any limitations of working with Aiven for Apache Flink®. Please let us know if you have questions.

Jobs, tables and tasks
----------------------

Some key points to know before you start working with Aiven for Apache Flink®:

* Jobs and tables cannot be edited after they are created.
* Running jobs must be manually restarted after powering off the cluster or when changing service plans.
* Cancelled and failed jobs cannot be restarted.

Limitations
-----------

In order to run a stable and reliable service, you will see some differences between Aiven for Apache Flink® and a Flink service that you run yourself. The main differences are:

* User-defined functions are not supported.
* The Apache Flink® CLI tool cannot be used with this service as it requires access to the JobManager in production, which is currently not exposed to customers.
* Job-level settings are not yet supported. Each job inherits the cluster-level settings.
* Flame graphs, marked as an experimental feature in Apache Flink® 1.13, are not currently enabled in the Flink web UI.

Troubleshooting
---------------

A collection of common questions and problems, with some suggestions to help you if you encounter them.

TaskManager logs for multi-node clusters
''''''''''''''''''''''''''''''''''''''''

TaskManager logs are not visible for multi-node clusters in the Flink web UI.


Internal server error
'''''''''''''''''''''

There are a number of causes for this error, but if you see this error when creating a new job, then check your source services. If any of the source services are powered off, you will see this error.

Stack traces
''''''''''''

While we have aimed to make the error messages more informative, you may see error messages directly rendered as-is from Flink. These messages are technical in nature and include a stack trace of the exception.

