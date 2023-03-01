Delete a cross-region backup
============================

.. important::

    Backup to another region (BTAR) is available on ``:doc:Pro Platform </docs/platform/concepts/pro-platform>``.

Delete :doc:`an additional service backup </docs/platform/concepts/backup-to-another-region>` from a region other than where primary service backups are stored.

Disable BTAR via console
------------------------

1. Log in to the `Aiven Console <https://console.aiven.io/>`_.
2. From the **Services** view, select an Aiven service on which you'd like to disable BTAR.
3. On your service's page, select **Backups** from the sidebar.
4. On the **Backups** page, select the actions (**...**) menu > **Secondary backup location**.
5. In the **Edit secondary backup location** window, select **Disable**.

Your additional service backup is no longer visible on your service's **Backups** page in the **Secondary backup location** column.

Disable BTAR via CLI
--------------------

To remove secondary backups for your service, use the :ref:`avn service update <avn-cli-service-update>` command to remove all target regions names from the ``additional_backup_regions`` array.

.. code-block:: bash

    avn service update your-sevice-name                   \
        -c additional_backup_regions=[]

Disable BTAR via API
--------------------

To remove secondary backups for your service, use the `ServiceUpdate <https://api.aiven.io/doc/#tag/Service/operation/ServiceUpdate>`_ endpoint to remove all target regions names from the ``additional_backup_regions`` array.

    Existing service > `Update service configuration <https://api.aiven.io/doc/#tag/Service/operation/ServiceUpdate>`_

.. code-block:: bash

    curl --request PUT                                                                  \
    --url https://api.aiven.io/v1/project/YOUR_PROJECT_NAME/service/YOUR_SERVICE_NAME   \
    --header 'Authorization: Bearer YOUR_BEARER_TOKEN'                                  \
    --header 'content-type: application/json'                                           \
    --data
      '{
        "user_config": {
          "additional_backup_regions": []
          }
      }'

.. topic:: Result

   Your service has no longer secondary backups in regions different from its hosting region.

Related pages
-------------

* :doc:`About the backup to another region feature in Aiven </docs/platform/concepts/backup-to-another-region>`
* :doc:`Enable BTAR for your Aiven service </docs/platform/howto/enable-backup-to-another-region>`
* :doc:`Manage BTAR for your Aiven service </docs/platform/howto/manage-backup-to-another-region>`
