Service power cycle
===================

Aiven service power off and power on is more than stopping and starting a service on nodes. For better utilisation of resources on Aiven platform, idle resources will be released and only the necessary data will be kept after power off. The impact on the service is different depending on the service type and plan. 

.. warning:: Depedning on service type and plan, data loss may happen during a service power off, so it is important for users to understand the consequences before powering off a service.

Aiven service power off and power on can be done on `Aiven Console <https://console.aiven.io>`_ or through :doc:`Aiven CLI </docs/platform/howto/pause-from-cli>`.

Power off
-------------

Whenever an Aiven service is powered off:

* All virtual machine(s) of the service will be **removed** from the public cloud.
* The service information and configuration will be stored on Aiven Platform, while service data will be lost if there's no backup available .
* If the service has **time-based** or **PITR (point in time recovery)** backups, they will be kept on Aiven Platform. The backups are listed in the ``Backups`` tab of the service on Aiven Console. Absence of the tab means the service has no backups. For details on backups for different Aiven services on different plans, please refer to :doc:`Backups at Aiven </docs/platform/concepts/service_backups>`.
.. warning:: Aiven does `periodic cleanup of powered-off services <https://help.aiven.io/en/articles/4578430-periodic-cleanup-of-powered-off-services>`_ on services powered off for longer than **180** consecutive days. Notification emails will be sent before actions are taken.
* The message in the **Power Off Confirmation** window will give some hints on the consquence of the power off. Below is an example of powering off an Aiven for Redis service whose data since the latest backup will be lost because the service only has time-based but not PITR backups. 
.. image:: /images/platform/power-off-confirmation.png
    :alt: Power Off Confirmation  
* Moreover, under the ``Backups`` tab, hovering the mouse over the help icon (if it's available) can present some details on the content of the backups. This information suggests what can be restored if the service is powered on later.
.. image:: /images/platform/backup-help-info.png
    :alt: Backup Help Information
.. warning:: For backup enabled Aiven for Apache Kafka® services, topic configuration, schemas and connectors are all backed up, but not the data in topics. Therefore all topic data will be lost on power off. For Kafka services without backups, topic configurations together with all topic data will be lost on power off.


Power on
------------

When a service is powered on, the following things will happen:

* New virtual machine(s) will be created on the specified public cloud for the service.
* Service will be started with the stored configuration parameters.
* The latest time-based backup that is available will be restored. The restore time depends on the network bandwidth and disk IOPS allocated to the service plan as well as the size of the backup. It could take from minutes to hours. Smaller plans with larger backups take longer time than bigger plans with smaller backups. Restore progress can be checked by Aiven support with Aiven Admin CLI. 
* If PITR backup is avilable, the database transaction log (e.g. ``WAL`` for PostgreSQL, ``binlog`` for MySQL) will be replayed to recover the service data to a specific point in time.
* Service will be ready for serving.

.. warning:: Depending on the service plan, backups have different retention periods. Data will be lost after the retention period.

