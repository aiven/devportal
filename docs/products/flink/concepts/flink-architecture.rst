Aiven for Apache Flink® Architecture
====================================

Apache Flink is an open-source distributed stream processing framework that allows you to process data in real-time. At a high level, it has a runtime architecture consisting of two types of processes: a **JobManager** and one or more **TaskManager**.

JobManager
-----------
The JobManager is the central coordination point of Flink and is responsible for managing the execution of Flink jobs. It is responsible for scheduling tasks, managing task execution, and coordinating the overall execution of the Flink application. In other words, Flink provides an exactly-once processing guarantee, only if JobManager is always up and running.

In a high-availability setup, there may be multiple JobManagers running in the cluster, with one JobManager designated as the leader and the others as standby JobManagers. 

The JobManager in Apache Flink consists of three main components: **ResourceManager**, **Dispatcher**, and **JobMaster**. The ResourceManager is responsible for managing the allocation and deallocation of resources in the Flink cluster. Additionally, ResourceMaanger is responsible for managing **Task slots** - the unit of resource scheduling in a Flink cluster.

TaskManger
----------
TaskManager is responsible for executing the tasks assigned to them by the JobManager and exchanging data with other TaskManagers as needed. This direct communication between TaskManagers allows for efficient data exchange and helps improve the Flink runtime's performance.
TaskManagers also communicate with the JobManager to report progress and request necessary resources. This enables the JobManager to monitor the progress of tasks and to allocate resources accordingly to ensure optimal performance.

In addition to the JobManager and TaskManager processes, Apache Flink also has a number of other components, including **DataStream API** and **DataSet API** for submitting jobs to the Flink runtime, a configuration system for setting up and tuning the Flink runtime, and a number of libraries and connectors for working with various data sources and sinks.

For more information, see `Flink Architecture <https://nightlies.apache.org/flink/flink-docs-master/docs/concepts/flink-architecture/>`_.

