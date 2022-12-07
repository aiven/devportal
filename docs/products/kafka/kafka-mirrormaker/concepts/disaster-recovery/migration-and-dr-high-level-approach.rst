Migration and Disaster Recovery high level approach
####################################################

MirrorMaker 2 (MM2) is the standard replication tool packaged with the Apache Kafka® and can be run as a managed service on the Aiven platform. Under the hood, MM2 utilizes Kafka Connect to both consume from one Kafka cluster and then simultaneously produce to a second cluster. MM2 can be used to enable either an Active-Passive disaster recovery (DR) architecture or an active-active (HA) architecture.

**Migration**

Migrating a Apache Kafka® cluster to Aiven will utilize the same pattern as DR. In this case however, you will need to utilize an external Kafka integration via the Aiven platform and can use this registered integration in the replication flow to migrate data from an external Kafka cluster to an Aiven for Apache Kafka cluster.

MirrorMaker 2 (MM2) is the standard replication tool packaged with the Apache Kafka® and can be run as a managed service on the Aiven platform. Under the hood, MM2 utilizes Kafka Connect to both consume from one Kafka cluster and then simultaneously produce to a second cluster. MM2 can be used to enable either an Active-Passive disaster recovery (DR) architecture or an active-active (HA) architecture.


**Setup**

MM2 is enabled on the Aiven platform as a service integration between two Aiven for Apache Kafka® clusters or a Kafka cluster and an external Kafka integration. Once the integration is created MM2 uses the concept of replication flows to direct traffic in the desired direction between Kafka clusters.

MM2 can be set up using any Aiven standard provisioning method Console, API, CLI, and TF.