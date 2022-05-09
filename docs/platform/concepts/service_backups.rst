Backups at Aiven
================

All Aiven services have time-based backups, except for Kafka, that are encrypted and securely stored. The backup retention times vary based on the service and the selected service plan. Backups we take for managing the service are not available for download for any service type, as those are compressed and encrypted by our management platform.
    
Whenever the service is powered on from a powered-off state, the restore the latest backup available when the service is rebuilt. We do review any services that are powered off for longer than 180 days. We will send you a notification email in advance to take action before we perform house cleaning and delete the service and backup as part of `periodic cleanup of powered-off services <https://help.aiven.io/en/articles/4578430-periodic-cleanup-of-powered-off-services>`__. If you would still like to keep the powered off service for longer than 180 days, you can avoid this routine cleanup by powering on the service and then powering it back off again.

Depending on the service plan, each service provides different backups with different retention periods:

+---------------------------------------+------------------------------------------+---------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
|                                       | Backup Retention Time based on Service Plan                                                                                                                                                                          |
+ Service Type                          +------------------------------------------+---------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
|                                       | Hobbyist                                 | Startup                                                 | Business                                               | Premium                                                |
+=======================================+==========================================+=========================================================+========================================================+========================================================+
| Aiven for Apache Kafka®               | No backups                               | No backups                                              | No backups                                             | No backups                                             |
+---------------------------------------+------------------------------------------+---------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| Aiven for PostgreSQL® / MySQL         | Single backup only for disaster recovery | 2 days with PITR                                        | 14 days with PITR                                      | 30 days with PITR                                      |
+---------------------------------------+------------------------------------------+---------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| Aiven for OpenSearch®                 | Single backup only for disaster recovery | Hourly backup for 24 hours and Daily backup for 3 days  | Hourly backup for 24 hours and Daily backup for 14 days| Hourly backup for 24 hours and Daily backup for 30 days|
+---------------------------------------+------------------------------------------+---------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| Aiven for Apache Cassandra®           | Plan not available                       | Single day backup                                       | Single day backup                                      | Single day backup                                      |
+---------------------------------------+------------------------------------------+---------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| Aiven for Redis™*                     | Single backup only for disaster recovery | Backup every 12 hours up to 1 day                       | Backup every 12 hours up to 3 days                     | Backup every 12 hours up to 13 days                    |
+---------------------------------------+------------------------------------------+---------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| Aiven for InfluxDB®                   | Plan not available                       | Backup every 12 hours up to 2.5 days                    | Plan not available                                     | Plan not available                                     |
+---------------------------------------+------------------------------------------+---------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| Aiven for Apache Flink®               | Plan not available                       | Hourly backup up to 2 hours                             | Hourly backup up to 2 hours                            | Plan not available                                     |
+---------------------------------------+------------------------------------------+---------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| Aiven for M3                          | Plan not available                       | Single day backup                                       | Daily backup up to 6 days                              | Daily backup up to 13 days                             |
+---------------------------------------+------------------------------------------+---------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| Aiven for M3 Aggregator / Coordinator | Plan not available                       | Plan not available                                      | No backups                                             | No backups                                             |
+---------------------------------------+------------------------------------------+---------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| Aiven for Grafana®                    | Plan not available                       | Single day backup                                       | Daily backup up to 6 days                              | Daily backup up to 13 days                             |
+---------------------------------------+------------------------------------------+---------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| Aiven for ClickHouse®                 | Daily backups up to 2 days               | Daily backups up to 2 days                              | Daily backups up to 14 days                            | Plan not available                                     |
+---------------------------------------+------------------------------------------+---------------------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+

The above table describes only the hourly and daily backups with the number of days of retention. The following section deals with more specific backup strategies for each service type.


Aiven for PostgreSQL®
'''''''''''''''''''''
We take daily full backups and constantly archive WAL segments to cloud object storage. In the event of a node failure, we can reconstruct the latest state from a replica (if using a Business or Premium plan) or from the latest base backup and replaying the latest WAL segments on top of that (if using a Startup plan). You can also supplement this with a remote read replica service which you can even run in a different cloud region or another cloud provider entirely but can be promoted to master if needed.

You may modify the backup time configuration option in Advanced Configuration in Aiven console which will begin shifting the backup schedule to the new time. If there was a recent backup taken, it may take another backup cycle before it starts applying a new backup time. 


For more information refer to :
 - https://developer.aiven.io/docs/products/postgresql/concepts/pg-backups.html
 - https://help.aiven.io/en/articles/653410-aiven-postgresql-high-availability
 - https://help.aiven.io/en/articles/1755229-aiven-for-postgresql-remote-replica

Aiven for MySQL
'''''''''''''''
These databases are automatically backed-up, with full backups daily, and binary logs recorded continuously. All backups are encrypted. We use the open source myhoard software to do this. Myhoard uses Percona XtraBackup internally for taking a full (or incremental) snapshot for MySQL.  You may modify the backup time configuration option in Advanced Configuration in Aiven console which will begin shifting the backup schedule to the new time. If there was a recent backup taken, it may take another backup cycle before it starts applying a new backup time. 

Aiven for Apache Kafka®
'''''''''''''''''''''''
We do not take backups and data durability is determined by the replication of data across the cluster, as in general it's more often used as a transport for data rather than a permanent store and the way how Kafka stores data does not really allow reasonable backup to be implemented using traditional backup strategies. To back up data passing through Kafka, we recommend setting up :doc:`MirrorMaker2<../../products/kafka/kafka-mirrormaker/index>` to replicate the data to another cluster, which could be an Aiven service or a Kafka cluster on your own infrastructure. 

The backup cluster would be running as an independent Kafka service, therefore you have complete freedom of choice in which zone the service should be based. Unlike earlier versions, Mirrormaker2 provides the tools for mapping the offsets between the source and destination, so the user does not need to make this sort of calculation. More details here, under the section "Offset Mapping" in this blog `article <https://blog.cloudera.com/a-look-inside-kafka-mirrormaker-2/>`__.

Another possible way is to set up Kafka-connect to backup the cluster, which helps to be able to sink data from Apache Kafka® to S3 via the dedicated Aiven connector.

More information refer to:
 - https://developer.aiven.io/docs/products/kafka/kafka-connect/howto/s3-sink-prereq.html
 - https://blog.cloudera.com/a-look-inside-kafka-mirrormaker-2/
 - https://developer.aiven.io/docs/products/kafka/kafka-mirrormaker/index.html

Aiven for OpenSearch®
'''''''''''''''''''''
These databases are automatically backed up, encrypted, and stored securely in object storage. The backups are taken every hour and the retention period varies based on the service plan. You can read in our article `how to restore an OpenSearch® backup <https://developer.aiven.io/docs/products/opensearch/howto/restore_opensearch_backup.html>`_.


Aiven for Redis™*
'''''''''''''''''
We offer backups that are taken every 12 hours and for persistence, we support **RBD** and have also recently added the persistence feature which can be controlled by redis_persistence under **Advanced Configuration**. The AOF persistence is currently not supported in Aiven for Redis service.
When persistence is set to ``rdb``, Redis does RDB (Redis Database Backup) dumps every 10 minutes if any key is changed. Also, RDB dumps are done according to the backup schedule for backup purposes. When persistence is ``off``, no RDB dumps and backups are done, so data can be lost at any moment if the service is restarted for any reason or if the service is powered off. Also, the service can't be forked.

Aiven for InfluxDB®
'''''''''''''''''''
We offer backups that are taken every 12 hours with 2.5 days of retention. 
We automatically backup InfluxDB®, encrypt it and then upload it to our S3 account in the same region. When an instance has to be rebuilt, we download the backup and restore it to create the new instance.

Aiven for Apache Cassandra®
'''''''''''''''''''''''''''
We currently support backups taken every 24 hours. The PITR feature is currently not available. Please contact support if you would to be notified once PITR feature is available for Cassandra.