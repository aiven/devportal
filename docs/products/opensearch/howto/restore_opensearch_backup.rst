Restore an OpenSearch® backup
=============================

Depending on your service plan, you can restore OpenSearch® backups from a specific day or hour.

To restore a backup:

#. Log in to the `Aiven web console <https://console.aiven.io>`_ and select your OpenSearch service.

#. Click the **Backups** tab.

#. Click **Restore**.

   This opens the *New Database Fork* view where you can create the fork for the backup that you want to restore.

#. Fill in the required details, select the cloud provider, region, and service plan, then click **Create fork**.

#. Once the new service is running, change your application's connection settings to point to it and power off the original service.
