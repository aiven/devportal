Prevent PostgreSQL full disk issues
===================================

If your Aiven for PostgreSQL service runs out of disk space, the service will start malfunctioning and precluding the proper backups creation. 

To prevent this situation, Aiven automatically detects when your service is running out of free space and stops further write operations by setting the ``default_transaction_read_only``  parameter to ``ON``.

With this setting in place, clients trying to execute write operations will start facing errors like::

    cannot execute CREATE TABLE in a read-only transaction.

To re-enable database writes you need to increase the available space, by either deleting data or upgrading to a larger plan.

Increase free space by upgrading to a larger plan
-------------------------------------------------

When upgrading to a larger plan, new nodes with bigger disk space capacity, are created and replace the original nodes. Once the upgrade is finished and the free space increased, write operations are enabled again.
You can upgrade the Aiven for PostgreSQL service plan via the `Aiven console <https://console.aiven.io/>`_ or :doc:`Aiven CLI </docs/tools/cli>`. 

To perform a plan upgrade via the `Aiven console <https://console.aiven.io/>`_:

* Go to the Aiven for PostgreSQL service page
* In the *Overview* tab scroll down to the **Service plan** section and click on **Upgrade Plan**
* Select the new plan with higher capacity and click **Upgrade**.

Once the new nodes with increased disk capacity are up and running, the disk usage returns to below the critical level and the system automatically sets the ``default_transaction_read_only`` parameter to ``OFF`` allowing write operations again.

.. Note::

    If you temporarily upgrade your service to delete data, you may have to wait for the next backup to complete before you can downgrade to a smaller plan.

Increase free space by deleting data
------------------------------------

To release space from a database, you can also delete data stored in it, but the database read-only mode also prevents them. 
You can enable deletions by either enabling writes for a specific session or for a limited amount of time over the full database.

Enable database writes for a specific session
'''''''''''''''''''''''''''''''''''''''''''''

If you want to enable writes for a session, login to the required database and execute the following command:

::

    SET default_transaction_read_only = OFF;

You can then delete data within your session.

Enable database writes for a limited amount of time
'''''''''''''''''''''''''''''''''''''''''''''''''''

If you want to enable any writes to the database for a limited amount of time, send the following ``POST`` request using :ref:`Aiven APIs </docs/tools/api/index>` and replacing the ``PROJECT_NAME`` and ``SERVICE_NAME`` placeholders:

::

    https://api.aiven.io/v1/project/<PROJECT_NAME>/service/<SERVICE_NAME>/enable-writes

The above API call enables write operations in the target Aiven for PostgreSQL database for 15 minutes, allowing you to delete some data.