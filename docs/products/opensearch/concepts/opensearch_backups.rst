Backups
=======

Aiven for OpenSearch databases are automatically backed up, `encrypted <https://help.aiven.io/en/articles/977466-cloud-security-overview>`_, and stored securely in object storage.

Depending on the service plan, we offer single backups for disaster recovery or daily backups with different retention periods:

-  Hobbyist plans: single backup for disaster recovery

-  Startup plans: daily backups with a 2-day retention period

-  Business plans: daily backups with a 14-day retention period

-  Premium plans: daily backups with a 30-day retention period


To allow returning to an earlier point in time, Aiven for OpenSearch uses two kinds of backups - hourly and daily. Each type has its own
backup frequency interval and retention period. Currently, you cannot configure these settings.

Restore from backup
-------------------

Create a :doc:`fork </docs/platform/concepts/database-forking>` of your OpenSearch service, and choose the backup you would like to use as the basis for your new service.

.. note::
    Aiven for OpenSearch currently only supports restoring from daily backups or hourly backups from the previous day.

