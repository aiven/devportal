Point-in-time recovery (PITR) process for Aiven for Grafana®
============================================================

The Point-in-Time Recovery (PITR) process allows you to restore your Grafana service using a backup from a specific point in time. When you initiate the restore using the PITR backup for Grafana, a new service will be created to host the restored data. Follow the steps below to perform PITR for Aiven for Grafana:


1. In the Aiven for Grafana Service, select **Backups** from the left sidebar.

2. Click **Fork & restore**.

3. In the **New Database Fork** dialog, 

   - Provide a name for the new service.
   - Verify that the appropriate Project name is chosen.
   - Select the desired backup from the available options using the drop-down list.
    
     .. Tip::
            If your service has multiple backup files, ensure that you select the correct PITR backup from the dropdown list. 
   - Choose your cloud provider, preferred cloud region, and the service plan accordingly.
    

   .. image:: /images/products/grafana/grafana-pitr-new-db-fork-popup.png
      :alt: popup for setting specifics of the service restore.

4. Click **Create fork** to create the new forked service.

5. You will be redirected to the **Overview** page of the newly forked service. The service is in the **Rebuilding** status while it is being created. Once the service is ready, the status changes to **Running**. 

   .. image:: /images/products/grafana/grafana-pitr-after-fork.png
      :alt: restore is rebuilding after clicking 'create fork'
