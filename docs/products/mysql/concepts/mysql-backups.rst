Understand MySQL backups
========================

Aiven for MySQL databases are automatically backed-up, with full backups daily, and binary logs recorded continuously.
The number of stored backups and backup retention time depends on your `Aiven service plan <https://aiven.io/pricing?product=mysql&tab=plan-comparison>`_. Full backups are version-specific binary backups, which when combined with binlog allow for consistent recovery to a specific point in time (PITR).

MySQL backups and encryption
----------------------------

All Aiven for MySQL backups, uses the `myhoard software <https://github.com/aiven/myhoard>`_ to perform encryptions. Myhoard utilizes `Percona XtraBackup <https://www.percona.com/>`_ internally for taking a full (or incremental) snapshot for MySQL. 

Since `Percona XtraBackup 8.0.23 version <https://jira.percona.com/browse/PXB-1979>`_ the --lock-ddl is enabled by default. This ensures that DDL changes can not be performed while a full backup process is ongoing. This is important to guarantee that the backup service is consistent and can be reliably used for restoration. 


With this feature enabled, if you try to run ``CREATE``, ``ALTER``, ``DROP``, ``TRUNCATE`` or another command, you may receive the message **Waiting for backup lock**. In this case, wait till the backup is complete for running such operations.

More resources
--------------

- Our blog post: `MyHoard, your solution to MySQL backups and restoration <https://aiven.io/blog/introducing-myhoard-your-single-solution-to-mysql-backups-and-restoration>`_
- Read about `Aiven cloud security and data encryption <https://developer.aiven.io/docs/platform/concepts/cloud-security#data-encryption>`_
