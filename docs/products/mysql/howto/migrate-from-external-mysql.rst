Migrate to Aiven for MySQL from an external MySQL
=================================================

Aiven for MySQL offers a managed process for migrating from an external MySQL into the Aiven-hosted database.  It supports both a one-off "dump and restore" process and using the ongoing replication functionality built-in to MySQL. The process will first do a ``mysqldump`` to seed the schema and bulk-copy the data; if the preconditions are met for ongoing replication then it will configure MySQL as a replica of the external database.

Requirements
------------

To perform a migration from an external MySQL to Aiven for MySQL the following requirements need to be satisfied:

* The source server needs to be publicly available or accessible via a virtual private cloud (VPC) peering connection between the private networks, and any firewalls need to be open to allow traffic between the source and target servers.
* You have a user account on the source server with sufficient privileges to create a user for the replication process.
* `GTID <https://dev.mysql.com/doc/refman/8.0/en/replication-gtids.html>`_ is enabled on the source database.  To review the current GTID setting, run the following command on the source cluster::

    show global variables like 'gtid_mode';

.. Note::
    If you are migrating from MySQL in GCP, you need to enable backups with `PITR <https://cloud.google.com/sql/docs/mysql/backup-recovery/pitr>`_ for GTID to be set to ``on``


Variables
'''''''''

You can use the following variables in the code samples provided:

.. list-table::
  :header-rows: 1
  :widths: 15 60
  :align: left

  * - Variable
    - Description
  * - ``SRC_HOSTNAME``
    - Hostname for source MySQL connection
  * - ``SRC_PORT``
    - Port for source MySQL connection
  * - ``SRC_DATABASE``
    - Database name for source MySQL connection
  * - ``SRC_USERNAME``
    - Username for source MySQL connection
  * - ``SRC_PASSWORD``
    - Password for source MySQL connection
  * - ``SRC_SSL``
    - SSL setting for source MySQL connection
  * - ``DEST_NAME``
    - Name of the destination Aiven for MySQL service
  * - ``DEST_PLAN``
    - Aiven plan for the destination Aiven for MySQL service (e.g. ``startup-4``, ``business-32``, etc) 


Perform the migration
---------------------

1. Create a user in the source database with sufficient privileges for the pre-flight checks, the ``mysqldump``, and the ongoing replication (you can substitute ``%`` in the below command with the IP address of the Aiven for MySQL database, if already existing)::

    create user 'SRC_USERNAME'@'%' identified by 'SRC_PASSWORD';
    grant replication slave on *.* TO 'SRC_USERNAME'@'%';
    grant select, process, event on *.* to 'SRC_USERNAME'@'%'

2. If you don't have an Aiven for MySQL database yet, create it via the :doc:`Aiven Console <../get-started>` or the dedicated :ref:`Aiven CLI command <avn-cli-service-create>`

3. Set the migration details via the ``avn service update`` :ref:`Aiven CLI command <avn-cli-service-update>` substituting the parameters accordingly::

    avn service update \
        -c migration.dbname=SRC_DATABASE \
        -c migration.host=SRC_HOSTNAME \
        -c migration.port=SRC_PORT \
        -c migration.username=SRC_USERNAME \
        -c migration.password=SRC_PASSWORD \
        -c migration.ssl=SRC_SSL \
        DEST_NAME

4. Check the migration status via the dedicated ``avn service migration-status`` :ref:`Aiven CLI command <avn-cli-service-migration-status>`::

    avn --show-http service migration-status DEST_NAME

Whilst the migration process is ongoing, the ``migration_detail.status`` will be ``syncing``::

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

    The migration will initially do a bulk-copy of your data, and then several minutes after that has finished it will use the built-in replication feature of MySQL to commence ongoing data copying.  You can see MySQL's internal status by running ``show replica status`` on the destination database.

Stop the replication
--------------------

If you reach a point where you no longer need the ongoing replication to happen, you can remove the configuration from the destination service via the ``avn service update`` :ref:`Aiven CLI command <avn-cli-service-update>`::

    avn service update --remove-option migration DEST_NAME

