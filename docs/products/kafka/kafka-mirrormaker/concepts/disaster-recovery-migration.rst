Disaster Recovery and Migration
###############################

MirrorMaker 2 is the standard replication tool packaged with the Apache Kafka® and can be run as a managed service on the Aiven platform. MirrorMaker 2 utilizes Kafka Connect to both consume from one Kafka cluster and then simultaneously produce to a second cluster. MirrorMaker 2 can be used to enable either an Active-Passive disaster recovery architecture or an active-active high availability architecture.


Disaster recovery
-----------------

Disaster recovery is one of the primary use cases for MirrorMaker 2. MirrorMaker 2 replicates data between Apache Kafka® clusters, including clusters located in different data centres. Thus it's possible to minimise the period of unavailability of Apache Kafka.

However, it's important to remember that **MirrorMaker 2 doesn't provide synchronous replication**, so it's possible that the latest records accepted into a topic in the source cluster might not be replicated to the target cluster before the source cluster fails.

MirrorMaker 2 is based on Kafka Connect, and as such there are tradeoffs between throughput and out-of-order or duplicated records.

There is no one-size-fits-all disaster recovery solution. Various requirements such as the nature of the data, its volume, acceptable ops overhead, and costs should be taken into account. 


Migration
---------

Migrating a Apache Kafka® cluster to Aiven will utilize the same pattern as disaster recovery. In this case however, you will need to utilize an external Kafka integration via the Aiven platform and can use this registered integration in the replication flow to migrate data from an external Kafka cluster to an Aiven for Apache Kafka cluster.


.. note:: MirrorMaker 2 can be set up using any Aiven standard provisioning method Console, API, CLI, and TF.


Consumer requirements
---------------------

* Ability to process out-of-order records
  
* Tolerate duplicate records