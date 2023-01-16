Aiven for Apache Flink® managed service features
================================================

As a fully managed distributed data stream processing platform, deployable in the cloud of your choice, some of the key features of a managed Flink service include the following:

Cluster deployment mode
-----------------------
Aiven for Apache Flink® is configured to use the `HashMap state backend <https://ci.apache.org/projects/flink/flink-docs-stable/api/java/org/apache/flink/runtime/state/hashmap/HashMapStateBackend.html>`_. This means that the `state <https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/#what-is-state>`_ is stored in memory, which can impact the performance of jobs that require keeping a very large state. We recommend you provision your platform accordingly.

The Flink cluster executes applications in `session mode <https://nightlies.apache.org/flink/flink-docs-stable/docs/deployment/overview/#session-mode>`_ so you can deploy multiple Flink jobs on the same cluster, thus effectively utilizing the available resources.

Scaling a Flink cluster
-----------------------
Each node is equipped with a TaskManager and JobManager. We recommend scaling up your cluster to add more CPU and memory for the TaskManager before attempting to scale out, so you make the best use of the resources with a minimum number of nodes. 

By default, each TaskManager is configured with a single slot for maximum job isolation. It is highly recommended that you modify this option to match your requirements.

.. warning:: Adjusting the task slots per TaskManager requires a cluster restart.	

Cluster restart strategy
------------------------
The default restart strategy of the cluster is set to `Failure Rate`. This controls how Apache Flink restarts in case of failures during job execution. Administrators can change this setting in the advanced configuration options of the service.

For more information on available options, refer to `Apache Flink fault tolerance <https://nightlies.apache.org/flink/flink-docs-master/docs/deployment/config/#fault-tolerance>`_ documentation. 

Disaster recovery
-----------------
Periodic checkpoints have been configured to be persisted externally in object storage. They allow Flink to recover states and positions in the streams by giving the application the same semantics as a failure-free execution. For information on checkpoints, see :doc:`Checkpoints <../concepts/checkpoints>`. 

Security considerations
-----------------------
All services run on a dedicated virtual machine with end-to-end encryption, and all nodes are firewall-protected.
The credentials used for data flow integrations between Flink and other Aiven services have read/write permissions on the clusters. You can set up separate clusters for writing processed data from Flink and restrict access if you need more strict access management than our default setup offers. This also minimizes the risk of accidental write events to the source cluster.

Cluster logging, metrics, and alerting
--------------------------------------
Log and metrics integration to Aiven services are available for administrators to configure so you can monitor the health of your service. 

By enabling these integrations, you can:

- Push service logs into an index in Aiven for OpenSearch®.
- Push service metrics to M3®, InfluxDB®, or PostgreSQL® services on Aiven.
- Create custom OpenSearch or Grafana® dashboards to monitor the service. 

