Backups at Aiven
================

All Aiven services, except for Apache Kafka® and M3 Aggregator/Coordinator, have time-based backups that are encrypted and securely stored. The backup retention times vary based on the service and the selected service plan. Backups we take for managing the service are not available for download for any service type, as they are compressed and encrypted by our management platform.

Whenever a service is powered on from a powered-off state, we restore the latest backup available.

We review any services that are powered off for longer than 180 days. We will send you a notification email in advance to take action before we perform house cleaning and delete the service and backup as part of `periodic cleanup of powered-off services <https://help.aiven.io/en/articles/4578430-periodic-cleanup-of-powered-off-services>`__. If you would still like to keep the powered off service for longer than 180 days, you can avoid this routine cleanup by powering on the service and then powering it back off again.

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

The above table describes only the hourly and daily backups with the number of days of retention. The following section deals with more specific backup strategies for particular service types.


Aiven for Apache Kafka®
''''''''''''''''''''''''''''''
We do not take backups and data durability is determined by the replication of data across the cluster, as in general it's more often used as a transport for data rather than a permanent store and the way Kafka stores data does not really allow reasonable backup to be implemented using traditional backup strategies.

To back up data passing through Kafka, we recommend setting up :doc:`MirrorMaker 2<../../products/kafka/kafka-mirrormaker/index>` to replicate the data to another cluster, which could be an Aiven service or a Kafka cluster on your own infrastructure.

Using MirrorMaker 2, the backup cluster is running as an independent Kafka service, so you have complete freedom of choice in which zone the service should be based.

Note that MirrorMaker 2 provides tools for mapping between source and target offset, so the user does not need to make this calculation. For more details see the section "Offset Mapping" in the blog post `A look inside Kafka MirrorMaker 2 <https://blog.cloudera.com/a-look-inside-kafka-mirrormaker-2/>`__.

An alternative is to use Kafka Connect to backup the cluster, for instance sinking data from Apache Kafka® to S3 via the `dedicated Aiven connector <https://developer.aiven.io/docs/products/kafka/kafka-connect/howto/s3-sink-prereq.html>`_.

For more information refer to

- `Aiven for Apache Kafka® MirrorMaker 2 <https://developer.aiven.io/docs/products/kafka/kafka-mirrormaker/index.html>`_
- Cloudera's `A look inside Kafka MirrorMaker 2 <https://blog.cloudera.com/a-look-inside-kafka-mirrormaker-2/>`_
- `Configure AWS for an S3 sink connector <https://developer.aiven.io/docs/products/kafka/kafka-connect/howto/s3-sink-prereq.html>`_

Aiven for PostgreSQL®
'''''''''''''''''''''
We take daily full backups and constantly archive WAL segments to cloud object storage. In the event of a node failure, we can reconstruct the latest state from a replica (if using a Business or Premium plan) or from the latest base backup and replaying the latest WAL segments on top of that (if using a Startup plan). You can also supplement this with a remote read replica service which you can even run in a different cloud region or another cloud provider entirely but can be promoted to master if needed.

You may modify the backup time configuration option in **Advanced Configuration** in the Aiven console which will begin shifting the backup schedule to the new time. If there was a recent backup taken, it may take another backup cycle before it starts applying a new backup time.

For more information refer to

- `PostgreSQL® backups <https://developer.aiven.io/docs/products/postgresql/concepts/pg-backups.html>`_
- `High availability <https://developer.aiven.io/docs/products/postgresql/concepts/high-availability.html>`_
- `Create and use read-only replicas <https://developer.aiven.io/docs/products/postgresql/howto/create-read-replica.html>`_

Aiven for MySQL
'''''''''''''''''''''
These databases are automatically backed-up, with full backups daily, and binary logs recorded continuously. All backups are encrypted. We use the open source `myhoard <https://github.com/aiven/myhoard>`_ software to do this.
Myhoard uses `Percona XtraBackup <https://www.percona.com/>`_ internally for taking a full (or incremental) snapshot for MySQL.

You may modify the backup time configuration option in **Advanced Configuration** in the Aiven console which will begin shifting the backup schedule to the new time. If there was a recent backup taken, it may take another backup cycle before it starts applying new backup time.

For more information refer to `MySQL Backups <https://help.aiven.io/en/articles/5199859-mysql-backups>`_.

Aiven for OpenSearch®
''''''''''''''''''''''''''''
These databases are automatically backed up, encrypted, and stored securely in object storage. The backups are taken every hour and the retention period varies based on the service plan.

For more information refer to

- `OpenSearch backups <https://developer.aiven.io/docs/products/opensearch/concepts/backups.html>`_
- `How to restore an OpenSearch® backup <https://developer.aiven.io/docs/products/opensearch/howto/restore_opensearch_backup.html>`_

Aiven for Apache Cassandra®
'''''''''''''''''''''''''''
We currently support backups taken every 24 hours. The PITR feature is currently not available. Please contact support if you would to be notified once the PITR feature is available for Cassandra.


Aiven for Redis™*
''''''''''''''''''''''''
We offer backups that are taken every 12 hours, and for persistence we support **RBD** (Redis Database Backup). The persistence feature can be controlled by ``redis_persistence`` under **Advanced Configuration**. AOF persistence is currently not supported by the Aiven for Redis service.

When persistence is set to ``rdb``, Redis does RDB dumps every 10 minutes if any key is changed. Also, RDB dumps are done according to the backup schedule for backup purposes. When persistence is ``off``, no RDB dumps or backups are done, so data can be lost at any moment if the service is restarted for any reason or if the service is powered off. This also means the service can't be forked.

Aiven for InfluxDB®
'''''''''''''''''''
We offer backups that are taken every 12 hours with 2.5 days of retention. 
We automatically backup InfluxDB®, encrypt it and then upload it to our S3 account in the same region. When an instance has to be rebuilt, we download the backup and restore it to create the new instance.


Access to backups
'''''''''''''''''
The Aiven platform provides a centralised, managed platform for the services outlined above to run across many different cloud providers and regions. Tooling that we have built to provide these backups are open source and available for you to use in your own infrastructure. 

The nature of the Aiven platform is to manage the operational tasks of running complex software at scale so that you are able to focus your efforts on using the services, not maintaining them. This means that we take care of the availability, security, connectivity and backups.
Access to backups of your services is not possible. The backups are encrypted and stored in object storage. If you do need to backup your services, this can be done with the standard tooling for that service. Below, we provide a list of the backup tools used for each service type.

Please note that these tools are merely recommendations and not intended to create a snapshot of your Aiven service; purely to provide access to the data.

- `PostgreSQL <https://www.postgresql.org/docs/14/app-pgdump.html>`__: ``pgdump``
- `MySQL <https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html>`_: ``mysqldump``
- `Redis <https://redis.io/docs/manual/cli/#remote-backups-of-rdb-files>`_: ``redis-cli`` 
- `Cassandra <https://docs.datastax.com/en/archived/cql/3.3/cql/cql_reference/cqlshCopy.html>`_: ``cqlsh`` 
- `OpenSearch <https://github.com/elasticsearch-dump/elasticsearch-dump>`_: ``elasticdump``
- `InfluxDB <https://docs.influxdata.com/influxdb/v1.8/tools/influx-cli/>`_: ``influxd``
