Tiered storage backups
========================

In Aiven for Apache Kafka's tiered storage, data that resides in topics with tiered storage will persist across power cycles, as long as segments have been successfully synchronized to the remote storage. Only topics with tiered storage get copied to remote locations, while active data segments remain on local storage due to limitations with Apache Kafka.

.. note:: 
    Remote data can remain vulnerable to accidental or intentional deletions as it stays connected to Apache Kafka brokers. 

To ensure security, Aiven for Apache Kafka employs client-side encryption at rest and multi-stage data integrity checks. The remote data is stored in the same cloud region as the Aiven for Apache Kafka service. 

Metadata backups are automatically restored during regular power cycles, but significant incidents may require manual operator intervention. The backup and restoration procedures for local storage remain separate and unchanged.

