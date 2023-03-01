About backup to another region for Aiven services
=================================================

.. important::

    Backup to another region (BTAR) is available on ``:doc:Pro Platform </docs/platform/concepts/pro-platform>``.

Discover the backup to another region (BTAR) feature, check why use it, and learn how it works.

About BTAR
----------

The backup to another region (BTAR) feature allows existing backup files to be copied from the service's primary backup region to an additional (secondary) region. As a disaster recovery feature, BTAR is particularly useful when the service-hosting region is down since it allows forking the service from an additional copy of the backup residing outside the service-hosting region.

BTAR is currently supported for the following services:

* Aiven for PostgreSQL®
* Aiven for MySQL®

Why use BTAR
------------

BTAR provides an additional level of data resilience, helping you make your data safe and protected. BTAR is a cost-efficient low-complexity disaster recovery feature that allows you to replicate your data in a secondary backup region and recover it there in case of outage, downtime, data loss, or data corruption in the primary backup region.

How BTAR works
--------------

By enabling the backup to another region (BTAR) feature, you create a service backup that is additional to the default backup. This secondary backup is always located in a region of your choice different from the primary backup region.

Secondary backups are generated from primary backups, not from the service itself. For this reason, your secondary backup becomes available only after the primary backup is taken. There might be a data replication lag between the primary region and the secondary region.

Restoring from a secondary backup, for example in case of an outage of the primary region, can be done by creating a fork of the service in the region where the secondary backup is located.

.. mermaid::

    flowchart LR
        subgraph Primary_region
            direction TB
            subgraph Service_X
                end
            subgraph Primary_backups
                direction LR
                PB1
                PB2
                PB3
                PBn
                end
            end
        subgraph Secondary_region
            direction TB
            subgraph Forked_service_X
                end
            subgraph Secondary_backups
                direction LR
                SB1
                SB2
                SB3
                SBn
                end
            end
        Service_X -- Default \n backups --> Primary_backups
        Primary_backups -- Cross-region backups \n if BTAR  enabled --> Secondary_backups
        Secondary_backups -- Secondary backups \n to restore service X --> Forked_service_X
        Service_X -- Forking service X \n if primary region down --> Forked_service_X

Limitations
-----------

* When selecting a cloud region for your additional backup, you need to use the same cloud provider that your service uses.
* When you want to :ref:`restore your service from an additional backup <fork-and-restore>` and you use a point in time to specify the scope of data to be restored, you need to set up the time to no later than the time of the latest backup.
* Secondary backup can only be restored in the region where it was stored.
* Secondary backup is generated only after a primary backup is complete, and there might be a data replication lag between the primary region and the secondary region.

Related pages
-------------

* :doc:`Enable BTAR </docs/platform/howto/enable-backup-to-another-region>`
* :doc:`Manage BTAR </docs/platform/howto/manage-backup-to-another-region>`
* :doc:`Disable BTAR </docs/platform/howto/disable-backup-to-another-region>`
