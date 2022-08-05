Apache Flink® for operators
===========================

Aiven for Apache Flink® is currently available on AWS or GCP cloud environments; all services and infrastructure are single-tenant and dedicated solely to a single customer. Choose between single-node and three-node Apache Flink® clusters, depending on your requirements:

* Single-node clusters are not highly available, but support automatic failover. They start from 4GB RAM/2 vCPU and extend up to 32GB/8 vCPU. This setup is a good option for proof of concepts and preliminary testing for development purposes.

* Three-node clusters are highly available, support automatic failover, and range from 4GB RAM/2 vCPU to 32GB/8 vCPU.

Our product page provides you detailed information about the available plans and pricing. 

Cluster deployment
------------------

Aiven for Apache Flink® is configured to use the `HashMap state backend <https://ci.apache.org/projects/flink/flink-docs-stable/api/java/org/apache/flink/runtime/state/hashmap/HashMapStateBackend.html>`_. This means that `state <https://ci.apache.org/projects/flink/flink-docs-release-1.15/docs/concepts/stateful-stream-processing/#what-is-state>`_ is stored in memory, which can impact the performance of jobs that require keeping a very large state. We recommend you provision your platform accordingly.

The Flink cluster executes applications in `session mode <https://ci.apache.org/projects/flink/flink-docs-release-1.15/docs/deployment/overview/#session-mode>`_, so you can deploy multiple Flink jobs on the same cluster to use the available resources effectively.

Scaling a Flink cluster
'''''''''''''''''''''''

Each node is equipped with a TaskManager and JobManager. We recommend that you scale up your cluster to add more CPU and memory for the TaskManager before attempting to scale out. This approach makes the best use of the resources available in the nodes.

By default, each created TaskManager is configured with a single slot for best isolation between jobs. One slot is equivalent to one running data pipeline or job. We highly recommend that you adjust this setting for your use case. You can change this setting with ``number_of_task_slots`` under **Overview** > **Advanced configuration** in the Aiven web console.

.. note::
 Adjusting the task slots per TaskManager requires a cluster restart.	



Cluster restart strategy
''''''''''''''''''''''''

The cluster’s default restart strategy is configured to Failure Rate. This controls Flink’s restart behaviour in cases of failures during the execution of jobs. Administrators can overwrite this setting in the advanced configuration options for the service.

For more information on the available options, see the `Apache Flink® documentation on fault tolerance <https://ci.apache.org/projects/flink/flink-docs-master/docs/deployment/config/#fault-tolerance>`_.

Disaster recovery
'''''''''''''''''

Aiven has configured periodic checkpoints to be persisted externally in object storage. These allow Flink to recover state and positions in the data streams to provide failure-free execution.

Security considerations
-----------------------

All services run on a dedicated virtual machine with end-to-end encryption, and all nodes are firewall-protected.

The credentials used for data flow integrations between Flink and other Aiven services have read/write permissions on the clusters. You can set up separate clusters for writing processed data from Flink and restrict access there if you need more strict access management than our default setup offers. This also minimizes the risk of accidental write events to the source cluster.


