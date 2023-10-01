Detect and terminate long-running queries
=========================================

Aiven does not terminate any customer queries even if they run indefinitely, but long-running queries can cause issues by locking resources and therefore preventing database maintenance tasks such as backups.

To identify and terminate such long-running queries, you can do it from either:

* `Aiven Console <https://console.aiven.io>`__
* :doc:`MySQL shell <./connect-from-cli>` (``mysql``)


Terminate long running queries from the Aiven Console
-----------------------------------------------------

1. Log in to the `Aiven Console <https://console.aiven.io/>`_.
2. From the **Services** page, select your Aiven for MySQL® service.
3. In your service's page, select **Current queries** from the sidebar.
4. In the **Current queries** page, you can check the query duration and select **Terminate** to stop any long-running queries.

Detect and terminate long running queries via CLI
-------------------------------------------------

You can :doc:`login to your service <./connect-from-cli>` using ``mysqlsh`` or ``mysql``.  Once connected, you can call the following command on the ``mysql`` shell to view all running queries:

.. code-block:: shell
    
    SHOW PROCESSLIST WHERE command = 'Query' AND info NOT LIKE '%PROCESSLIST%';

You can learn more about the ``SHOW PROCESSLIST`` command from the `official documentation <https://dev.mysql.com/doc/refman/8.0/en/show-processlist.html>`_.

You can terminate a query manually using:

.. code-block:: shell

    KILL QUERY pid

where the ``pid`` is the process ID output by the `SHOW PROCESSLIST` command above.

You can learn more about the ``KILL QUERY`` command from the `MySQL KILL documentation <https://dev.mysql.com/doc/refman/8.0/en/kill.html>`_.
