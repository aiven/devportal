Savepoints
==========

Savepoints in Aiven for Apache Flink® are snapshots of the current state of your :doc:`Flink application <../howto/create-flink-applications>`. They are created when stopping an application deployment and allow you to restart it later on without losing any progress or state. 

Additionally, savepoints play a crucial role in disaster recovery for Aiven for Apache Flink Service. In the event of a failure or interruption, you can use savepoints to resume or restart your application (or Flink job) from the last known state, ensuring that you do not lose any progress.

When using Aiven for Apache Flink, you need to explicitly trigger the creation of savepoints for an application when you stop it. 