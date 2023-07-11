Point-in-time recovery (PITR) process for Aiven for Grafana®
============================================================
When restore from PITR backup for grafana, a new service will be created.

Steps
-----
1. Navigate to the backup tab of Grafana service
2. Click 'Fork & restore'
.. image:: /images/products/grafana/enable-dashboard-previews.png
    :alt: click 'Fork & restore' from backup tab of grafana service from Aiven console
3. After you have clicked the button, a new popup will appear to change specifics for the service restore
.. image:: /images/products/grafana/enable-dashboard-previews.png
    :alt: popup for setting specifics of the service restore.
4. Once you have confirmed all the relevant selections, scroll down to the bottom of the popup and click 'Create fork' 
.. image:: /images/products/grafana/enable-dashboard-previews.png
    :alt: click 'create fork' to start restore.
5. 'Overview' tab will be loaded for the new forked service, the service status will be seen as 'Rebuilding' until the node comes up 
.. image:: /images/products/grafana/enable-dashboard-previews.png
    :alt: restore is rebuilding after clicking 'create fork'

.. Tip::
    Service may have more than 1 backup file. Make sure to select the correct PITR backup from the dropdown list 'Select backup to fork from'.