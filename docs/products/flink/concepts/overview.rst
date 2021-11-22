Service overview
================

This article gives you an overview of the service plans and features available in Aiven for Apache Flink beta.

You can run Aiven for Apache Flink on AWS or GCP cloud environments. Various deployment options are available, ranging from fully managed access over the public internet to subnet deployments under your own cloud account. All services and infrastructure are single-tenant and dedicated solely to a single customer.

Aiven offers single-node and three-node Apache Flink clusters:

* Single-node clusters are not highly available, but support automatic failover. They start from 4GB RAM/2 vCPU and extend up to 32GB/8 vCPU. This setup is a good option for proof of concepts and preliminary testing for development purposes.

* Three-node clusters are highly available, support automatic failover, and range from 4GB RAM/2 vCPU to 32GB/8 vCPU.

Our product page provides you detailed information about the available plans and pricing. 


Managed service features
------------------------

**Default deployment configuration**
  Aiven for Apache Flink is configured to use the `HashMap state backend <https://ci.apache.org/projects/flink/flink-docs-stable/api/java/org/apache/flink/runtime/state/hashmap/HashMapStateBackend.html>`_. This means that the amount of `state <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/concepts/stateful-stream-processing/#what-is-state>`_ kept depends on the amount of memory available in the cluster. 

  The Flink cluster executes applications in `session mode <https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/deployment/overview/#session-mode>`_, so you can deploy multiple Flink jobs on the same cluster to use the available resources effectively.

**Scaling a Flink cluster**
  Each node is equipped with a TaskManager and JobManager. We recommend that you scale up your cluster to add more CPU and memory for the TaskManager before attempting to scale out. This approach makes the best use of the resources available in the nodes.

  By default, each created TaskManager is configured with a single slot for best isolation between jobs. One slot is equivalent to one running data pipeline or job. We highly recommend that you adjust this setting for your use case. You can change this setting with ``number_of_task_slots`` under **Overview** > **Advanced configuration** in the Aiven web console.

  .. note::
     Adjusting the task slots per TaskManager requires a cluster restart.	

**Cluster restart strategy**
  The cluster’s default restart strategy is configured to Failure Rate. This controls Flink’s restart behaviour in cases of failures during the execution of jobs. Administrators can overwrite this setting in the advanced configuration options for the service.

  For more information on the available options, see the `Apache Flink documentation on fault tolerance <https://ci.apache.org/projects/flink/flink-docs-master/docs/deployment/config/#fault-tolerance>`_.

**Disaster recovery**
  Aiven has configured periodic checkpoints to be persisted externally in object storage. These allow Flink to recover state and positions in the data streams to provide failure-free execution.

**End-to-end security**
  All services run on a dedicated virtual machine with end-to-end encryption, and all nodes are firewall-protected.

**Cluster logging, metrics, and alerting**
  Administrators can configure log and metrics integrations to Aiven services so that you can monitor the health of your service.

  These integrations allow you to

  * push service logs to an index in Aiven for OpenSearch
  * push service metrics to M3, InfluxDB, or PostgreSQL services on Aiven
  * create custom OpenSearch or Grafana dashboards to monitor the service 

  The platform also has alert policies to notify you via email when a key metric rises above or below a set threshold, such as low memory or high CPU consumption. For information on setting the addresses for these emails, see `this article <http://help.aiven.io/en/articles/5234705-technical-emails>`_.


Apache Flink features
---------------------

**Flink SQL**
  Apache Flink enables you to develop streaming applications using standard SQL. The :doc:`Aiven web console provides an SQL editor <supported_syntax_sql_editor>` to explore the table schema and create SQL queries to process streaming data.

**Built-in data flow integration with Aiven for Apache Kafka**
  Connect with Aiven for Apache Kafka as a source or sink for your data.

  * Autocompletion for finding existing topics in a connected Kafka service when you create data tables.
  * Choose the table format when reading data from Kafka - JSON, Apache Avro, Confluent Avro, Debezium CDC.
  * Supports :doc:`upsert Kafka connectors <kafka_connectors>`, which allow you to produce a changelog stream, where each data record represents an update or delete event.

**Built-in data flow integration with Aiven for PostgreSQL**
  Connect with Aiven for PostgreSQL as a source or sink for your data. The Aiven web console features autocompletion for finding existing databases in a connected PostgreSQL service when you create data tables.

**Automate workflows**
  Automate workflows for managing Flink services with :doc:`Aiven Terraform Provider </docs/tools/terraform>`. See the `Flink data source <https://registry.terraform.io/providers/aiven/aiven/latest/docs/data-sources/flink>`_ for details.


Limitations
-----------

* State is kept in memory, which can impact the performance of jobs that require keeping a very large state.
* User-defined functions are not supported.
* The Apache Flink CLI tool cannot be used with this service as it requires access to the JobManager in production, which is currently not exposed to customers.
* Job-level settings are not yet supported. Each job inherits the cluster-level settings.
* Flame graphs, marked as an experimental feature in Apache Flink 1.13, are not enabled in the Flink web UI.
* The credentials used for data flow integrations between Flink and other Aiven services have read/write permissions on the clusters.

  As a workaround for more strict access management on the source cluster, you can set up separate clusters for writing processed data from Flink. This minimizes the risk of accidental write events to the source cluster.


Known issues
------------

* Running jobs must be manually restarted after powering off the cluster or when changing service plans.
* Cancelled and failed jobs cannot be restarted.
* Jobs and tables cannot be edited after they are created.
* TaskManager logs are not visible for multi-node clusters in the Flink web UI.
* If the service that is configured as a source is powered off, creating a new job prompts an internal server error. If you see this error, check that your source services are powered on.
* While we have aimed to make the error messages more informative, you may see error messages directly rendered as-is from Flink. These messages are technical in nature and include a stack trace of the exception.
