Disaster Recovery
##################

**Disaster recovery** is one of the primary use cases for MirrorMaker 2. MirrorMaker 2 replicates data between Apache Kafka® clusters, including clusters located in different data centres. Thus it's possible to minimise the period of unavailability of Apache Kafka.

However, it's important to remember that **MirrorMaker 2 doesn't provide synchronous replication**, so it's possible that the latest records accepted into a topic in the source cluster might not be replicated to the target cluster before the source cluster fails.

MirrorMaker 2 is based on Kafka Connect, and as such there are tradeoffs between throughput and out-of-order or duplicated records.

There is no one-size-fits-all disaster recovery solution. Various requirements such as the nature of the data, its volume, acceptable ops overhead, and costs should be taken into account. 

.. note:: MM2 can be set up using any Aiven standard provisioning method Console, API, CLI, and TF.

Consumer requirements
---------------------

* Ability to process out-of-order records
  
* Tolerate duplicate records

Disaster recovery building blocks
----------------------------------
1. Data replication performed by MirrorMaker 2. The replication flow is the way for copying data between clusters.
2. Offset translation performed by MirrorMaker 2.
3. Monitoring of the replication process.
4. Disaster recovery playbooks, that must be written and tested.