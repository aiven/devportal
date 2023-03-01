Manage a cross-region backup
============================

.. important::

   Backup to another region (BTAR) is available on ``:doc:Pro Platform </docs/platform/concepts/pro-platform>``.

Manage a service that has the :doc:`backup to another region (BTAR) feature </docs/platform/concepts/backup-to-another-region>` enabled (a cross-region backup added):

* Change the backup region for the service by selecting another cross-region location.
* Monitor the status status, replication lag, and more.
* Fork and restore the service using :doc:`a cross-region backup </docs/platform/concepts/backup-to-another-region>`.
* Migrate the service.

Prerequisites
-------------

You have at least one :doc:`Aiven service with BTAR enabled </docs/platform/howto/enable-backup-to-another-region>`.

Change a backup region
----------------------

1. Log in to the `Aiven Console <https://console.aiven.io/>`_.
2. From the **Services** view, select an Aiven service on which you'd like to enable BTAR.
3. On your service's page, select **Backups** from the sidebar.
4. On the **Backups** page, select the actions (**...**) menu > **Secondary backup location**.
5. In the **Edit secondary backup location** window, use the **Secondary location** dropdown menu to select a region for your additional backup. Confirm your choice by selecting **Save**.

Monitor a service with BTAR
---------------------------

There are a few things you may want to check for your Aiven service in the context for BTAR:

* What is the status of a secondary backup?

  * Does your service has a backup in another region?
  * What is the target region of the secondary backup?

* What is the replication lag between data availability in the primary region and the secondary region?

Check BTAR status in the console
''''''''''''''''''''''''''''''''

To check out the availability, the status, and the target region of a secondary (BTAR) backup in the `Aiven Console <https://console.aiven.io/>`_, navigate to your **service's page** > **Backups** view > **Secondary backup location** column.

Check replication lag with API
''''''''''''''''''''''''''''''

To check out the target region and the replication lag for a secondary (BTAR) backup of your service, call the `ServiceBackupToAnotherRegionReport <https://api.aiven.io/doc/#tag/Service/operation/ServiceBackupToAnotherRegionReport>`_ endpoint.

Configure the call as follows:

1. Enter YOUR-PROJECT-NAME and YOUR-SERVICE-NAME into the URL.
2. Specify DESIRED-TIME-PERIOD depending on the time period you need the metrics for: select one of the following values for the ``period`` key: ``hour``, ``day``, ``week``, ``month``, or ``year``.

.. code-block:: bash

    curl --request POST                                                                                                      \
        --url https://api.aiven.io/v1/project/YOUR-PROJECT-NAME/service/YOUR-SERVICE-NAME/backup_to_another_region/report    \
        --header 'Authorization: Bearer YOUR-BEARER-TOKEN'                                                                   \
        --header 'content-type: application/json'                                                                            \
        --data '{"period":"DESIRED-TIME-PERIOD"}'

.. topic:: Output

    As an output, you get metrics including replication lags at specific points in time.

.. _fork-and-restore:

Fork and restore a service with BTAR
------------------------------------

You can use the `Aiven Console <https://console.aiven.io/>`_ to recover your service from a backup in another region. To restore your service using BTAR, :doc:`create a fork </docs/platform/howto/console-fork-service>` of the original service in the region where the secondary backup resides.

.. note::

   When you **Fork & restore** from the secondary backup, your new fork service is created in the cloud and region where the secondary backup is located. The fork service gets the same plan that the primary service uses. Backups of the fork service are located in the region where this new service is hosted.

1. Open the `Aiven Console <https://console.aiven.io/>`_ and navigate to your service homepage.
2. Select **Backups** from the sidebar.
3. On the **Backups** page, select **Fork & restore**.
4. In the **New database fork** window, apply the following settings:

   1. As **Source backup location**, select **Secondary location**.
   2. As **Source backup version**, select either **Latest transaction** or **Point in time**.

      .. note::

         For the point-in-time recovery (PITR) option, set up the time to no later than the time of taking the latest backup.

   3. Specify a name for the new fork service.
   4. Select **Create fork**.

Migrate a service with BTAR
---------------------------

You can migrate a service with BTAR the same way you :doc:`migrate a service with a regular backup </docs/platform/howto/migrate-services-cloud-region>`.

.. note::

   When you migrate your service, locations of service backups, both primary and secondary ones, do not change.

Related pages
-------------

* :doc:`About the backup to another region feature in Aiven </docs/platform/concepts/backup-to-another-region>`
* :doc:`Enable BTAR for your Aiven service </docs/platform/howto/enable-backup-to-another-region>`
* :doc:`Disable BTAR for your Aiven service </docs/platform/howto/disable-backup-to-another-region>`
