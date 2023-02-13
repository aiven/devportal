Disaster recovery and migration
###############################

MirrorMaker 2 is the standard replication tool packaged with the Apache Kafka® and can be run as a managed service on the Aiven platform. MirrorMaker 2 uses Kafka Connect to consume from one Kafka cluster and produce simultaneously to a second cluster. You can use MirrorMaker 2 to enable Active-Passive disaster recovery architecture or active-active high availability architecture.

Disaster recovery
-----------------

Disaster recovery is one of the primary use cases for MirrorMaker 2. MirrorMaker 2 replicates data between Apache Kafka® clusters, including clusters located in different data centres. Thus it's possible to minimise the period of unavailability of Apache Kafka.

However, it's important to remember that **MirrorMaker 2 does not offer synchronous replication**, which means that the latest records accepted into a topic in the source cluster may not replicate to the target cluster before the source cluster fails.

As MirrorMaker 2 is based on Kafka Connect, there are tradeoffs between throughput and out-of-order or duplicated records.

It's important to understand that disaster recovery has no one-size-fits-all solution. Different requirements should be considered, such as the data's nature, volume, acceptable ops overhead, and costs.


Migration
---------

Migrating an Apache Kafka® cluster to Aiven will utilize the same pattern as disaster recovery. In this case however, you will need to use an external Kafka integration via the Aiven platform. You can use this registered integration in the replication flow to migrate data from an external Kafka cluster to an Aiven for Apache Kafka cluster.


.. note:: MirrorMaker 2 can be set up using any Aiven standard provisioning method Console, API, CLI, and TF.


Consumer requirements
---------------------

* Ability to process out-of-order records
  
* Tolerate duplicate records