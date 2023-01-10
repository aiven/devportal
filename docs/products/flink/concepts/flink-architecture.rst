Aiven for Apache Flink® architecture
====================================

Apache Flink is an open-source distributed stream processing framework that allows you to process data in real-time. At a high level, it has a runtime architecture consisting of two types of processes: a **JobManager** and one or more **TaskManager**.

JobManager
-----------
The JobManager is the central coordination point of Flink and is responsible for managing the execution of Flink jobs. It is responsible for scheduling tasks, managing task execution, and coordinating the overall execution of the Flink application. In other words, Flink provides an exactly-once processing guarantee, only if JobManager is always up and running.

Some of the responsibilities of the JobManager include:

- **Scheduling tasks:** The JobManager decides when to schedule the next task (or set of tasks) for execution based on the availability of resources and the dependencies between tasks.
- **Monitoring task execution:** The JobManager monitors the execution of tasks and responds to finished tasks or execution failures.
- **Coordinating checkpoints:** The JobManager coordinates the execution of checkpoints, which are periodic snapshots of the state of the Flink application. Checkpoints are used to enable recovery of the Flink application in the event of a failure.
- **Coordinating recovery on failures:** In the event of a failure, the JobManager coordinates recovery by re-executing failed tasks or rolling back to a previous checkpoint.

In a high-availability setup, there may be multiple JobManagers running in the cluster, with one JobManager designated as the leader and the others as standby JobManagers. 

The JobManager in Apache Flink consists of three main components: **ResourceManager**, **Dispatcher**, and **JobMaster**. The ResourceManager is responsible for managing the allocation and deallocation of resources in the Flink cluster. Additionally, ResourceMaanger is responsible for managing **Task slots** - the unit of resource scheduling in a Flink cluster.

TaskManger
----------
TaskManager is responsible for executing the tasks assigned to them by the JobManager and exchanging data with other TaskManagers as needed. This direct communication between TaskManagers allows for efficient data exchange and helps improve the Flink runtime performance.
TaskManagers also communicate with the JobManager to report progress and request necessary resources. This enables the JobManager to monitor the progress of tasks and to allocate resources accordingly to ensure optimal performance.

In addition to the JobManager and TaskManager processes, Apache Flink also has a number of other components, including **DataStream API** and **DataSet API** for submitting jobs to the Flink runtime, a configuration system for setting up and tuning the Flink runtime, and a number of libraries and connectors for working with various data sources and sinks.

For more information, see `Flink Architecture <https://nightlies.apache.org/flink/flink-docs-master/docs/concepts/flink-architecture/>`_.

