Migrate
=========

External PostgreSQL databases can be migrated into Aiven using the following methods:
* logical replication
* ``pg_dump`` and ``pg_restore``
* bucardo

Migration Requirements
----------------------

A successful migration to Aiven PostgreSQL has several requirements in terms of versioning and network access:

* Source Database being on PostgreSQL version 10 or newer
* Source server publicly available or accessible via virtual private cloud (VPC) peering connection
* User account with access to the destination cluster from an external IP, as configured in ``pg_hba.conf`` on the source cluster
