Service power cycle
===================

Aiven serivce power off and power on is different from that on a tranditional platform. For better utilisation of resources on Aiven platform, idle resources will be released and only the necessary data will be kept after power off. The impact on the service is different depending on the service type and plan. 

.. warning:: Data loss may happen during a service power off, so it is important for users to understand the consequence before powering off a service.

Aiven service power off and power on can be done on `Aiven Console <https://console.aiven.io>`_ or through `Aiven CLI <https://docs.aiven.io/docs/platform/howto/pause-from-cli.html>`_.

Power Off
------------

After an Aiven service is powered off:

* All virual machine(s) of the service will be **removed** from the public cloud.
* The service information and configuration will be stored on Aiven Platform, while service data will be lost if there's no backup available .
* If the service has ``time-based`` or ``PITR (Point in time recovery)`` backups, they will be kept on Aiven Platform. The backups are listed in the ``Backups`` tab of the service on Aiven Console. Absence of the tab means the service has no backups. For details on backups for different services of different plans, please refer to `Backups at Aiven <https://docs.aiven.io/docs/platform/concepts/service_backups.html>`_ .
.. note:: Aiven does `periodic cleanup of powered-off services <https://help.aiven.io/en/articles/4578430-periodic-cleanup-of-powered-off-services>`_ on services powered off for longer than **180** consecutive days. Notification emails will be sent before actions are taken.
* The message in the ``Power Off Confirmation`` window will give some hints on the consquence of the power off. Below is the one for Redis service, whose data since the latest backup will be lost because the service only has time-based but not PITR backups. 
.. image:: /images/platform/power-off-confirmation.png
    :alt: Power Off Confirmation  
* Moreover, in ``Backups`` tab, hovering mouse over the help icon (if it's available) can present some details on the content of the backups. That implies what can be restored if the service is powered up later.
.. image:: /images/platform/backup-help-info.png
.. warning:: For backup enabled Kafka services, topic configuration, schemas and connectors are all backed up, but not data in topics. Therefore all topic data will be lost on power off. For Kafka services without backups, topic configurations together with all topic data will be lost on power off.


Power On
------------

When a service is powered on, the following things will happen:

* New virtual machine(s) will be created on the specified public cloud for the service.
* Service will be started with the stored configuration parameters.
* The latest time-based backup available will be restored. The restore time depends on the network bandwidth and disk IOPS allocated to the service plan as well as the size of the backup. It could take from minutes to hours. Smaller plans with larger backups take longer time than bigger plans with smaller backups. Restore progress can be checked by Aiven support with Aiven Admin CLI. 
* If PITR backup is avilable, the database transaction log (e.g. ``WAL`` for PostgreSQL, ``binlog`` for MySQL) will be replayed to recover the service data to a specific point in time.
* Service is ready for serving.

.. warning:: Depending on the service plan, backups have different retention periods. Data will be lost after the retention period.

