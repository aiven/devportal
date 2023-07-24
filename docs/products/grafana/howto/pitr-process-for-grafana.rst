Point-in-time recovery (PITR) process for Aiven for Grafana®
============================================================

The Point-in-Time Recovery (PITR) process allows you to restore your Grafana service using a backup from a specific point in time. When you initiate the restore using the PITR backup for Grafana, a new service will be created to host the restored data. Follow the steps below to perform PITR for Aiven for Grafana:


1. Navigate to the backup tab of Grafana service

2. Click **Fork & restore**.

.. image:: /images/products/grafana/grafana-pitr-fork-restore.png
    :alt: click 'Fork & restore' from backup tab of Grafana service from Aiven console

3. After you have clicked the button, a new popup will appear to change specifics for the service restore

.. image:: /images/products/grafana/grafana-pitr-new-db-fork-popup.png
    :alt: popup for setting specifics of the service restore.

4. Click **Create fork** to create the new forked service.

5. You will be redirected to the **Overview** page of the newly forked service. The service is in the **Rebuilding** status while it is being created. Once the service is ready, the status changes to **Running**. 

.. image:: /images/products/grafana/grafana-pitr-after-fork.png
    :alt: restore is rebuilding after clicking 'create fork'

.. Tip::
    Service may have more than 1 backup file. Make sure to select the correct PITR backup from the dropdown list 'Select backup to fork from'.