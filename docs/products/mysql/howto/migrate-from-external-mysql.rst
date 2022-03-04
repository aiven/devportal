Migrate to Aiven for MySQL from an external MySQL
=================================================

Aiven for MySQL offers a managed process for migrating from an external MySQL into the Aiven-hosted database.  It supports both a one-off "dump and restore" process, and using the ongoing replication functionality built-in to MySQL.  The process will first do a ``mysqldump`` in order to seed the schema and bulk-copy the data; if the preconditions are met for ongoing replication then it will configure MySQL as a replica of the external database.

What you'll need
----------------
    
* The source server is publicly available or there is a virtual private cloud (VPC) peering connection between the private networks, and any firewalls are open to allow traffic between the source and target servers.
* You have user account on the source server with sufficient privileges to create a user for the replication process.

Variables
'''''''''

You can use the following variables in the code samples provided:

==================   =====================================================================================
Variable             Description
==================   =====================================================================================
``SRC_HOSTNAME``     Hostname for source MySQL connection
``SRC_PORT``         Port for source MySQL connection
``SRC_DATABASE``     Database name for source MySQL connection
``SRC_USERNAME``     Username for source MySQL connection
``SRC_PASSWORD``     Password for source MySQL connection
``SRC_SSL``          SSL setting for source MySQL connection
``DEST_NAME``        Name of the Aiven destination MySQL service
``DEST_PLAN``        Aiven plan for the Aiven destination MySQL service (e.g. startup-4, business-32, etc)
==================   =====================================================================================
  
-> Perform the migration
---------------------------

1. Ensure that `GTID <https://dev.mysql.com/doc/refman/8.0/en/replication-gtids.html>`_ is enabled on the source database

To review the current GTID setting, run the following command on the source cluster::

    show global variables like 'gtid_mode';

.. Note::
    If you are migrating from MySQL in GCP, you need to enable backups with `PITR <https://cloud.google.com/sql/docs/mysql/backup-recovery/pitr>`_ for GTID to be set to 'on'

2. Create a user in the source database with sufficient privileges for the pre-flight checks, the ``mysqldump``, and the ongoing replication (you can substitute `%` here for the IP address of the Aiven for MySQL database, if it already exists)::

    create user 'SRC_USERNAME'@'%' identified by 'SRC_PASSWORD';
    grant replication slave on *.* TO 'SRC_USERNAME'@'%';
    grant select,process,event on *.* to 'SRC_USERNAME'@'%'

3. If you don't have an Aiven for MySQL database yet, run the following command to create one via :doc:`../../../tools/cli` substituting the parameters accordingly::

    avn service create -t mysql -p DEST_PLAN DEST_NAME

4. Set the migration details via :doc:`../../../tools/cli` substituting the parameters accordingly::

    avn service update \
        -c migration.dbname=SRC_DATABASE \
        -c migration.host=SRC_HOSTNAME \
        -c migration.port=SRC_PORT \
        -c migration.username=SRC_USERNAME \
        -c migration.password=SRC_PASSWORD \
        -c migration.ssl=SRC_SSL \
        DEST_NAME

5. Check the migration status via :doc:`../../../tools/cli`::

    avn --show-http service migration-status DEST_NAME

Whilst the processing is ongoing, the "migration_detail.status" will be "syncing"::

    {
        "migration": {
            "error": null,
            "method": "replication",
            "seconds_behind_master": 0,
            "source_active": true,
            "status": "done"
        },
        "migration_detail": [
            {
                "dbname": "migration",
                "error": null,
                "method": "replication",
                "status": "syncing"
            }
        ]
    }
    

.. Note::
    The migration will initially do a bulk-copy of your data, and then a few minutes after that has finished it will use the built-in replication feature of MySQL to commence ongoing data copying.

-> Stop the replication
--------------------------

If you reach a point where you no longer need the ongoing replication to happen, you can remove the configuration from the destination service via :doc:`../../../tools/cli`::

    avn service update --remove-option migration DEST_NAME

