Supported log formats
=====================

Aiven for PostgreSQL® supports setting different log formats which are compatible with popular log analysis tools like ``pgbadger`` or ``pganalyze``.

You can customise this functionality by navigating to your PostgreSQL® service on the `Aiven Console <https://console.aiven.io/>`_.  

From the sidebar on your service's page, select **Service settings**. On the **Service settings** page, navigate to the **Advanced configuration** section, and select **Configure** > **Add configuration options**. Next, you can select the ``pg.log_line_prefix`` parameter and a desired format based on a pre-fixed list.  

The supported log formats are available below with an example of the output:  

* ``'pid=%p,user=%u,db=%d,app=%a,client=%h '``

  .. code-block::

    [pg-user-test-1]2023-01-11T23:58:46.010530[postgresql-14][14-1] pid=625,user=postgres,db=defaultdb,app=[unknown],client=[local] LOG: connection authorized: user=postgres database=defaultdb application_name=aiven-pruned
    [pg-user-test-1]2023-01-11T23:58:46.019705[postgresql-14][15-1] pid=625,user=postgres,db=defaultdb,app=aiven-pruned,client=[local] LOG: disconnection: session time: 0:00:00.010 user=postgres database=defaultdb host=[local]

* ``'%t [%p]: [%l-1] user=%u,db=%d,app=%a,client=%h '``

  .. code-block::

    [pg-user-test-1]2023-01-11T23:59:46.592609[postgresql-14][16-1] 2023-01-11 23:59:46 GMT [949]: [2-1] user=postgres,db=defaultdb,app=[unknown],client=[local] LOG: connection authorized: user=postgres database=defaultdb application_name=aiven-pruned
    [pg-user-test-1]2023-01-11T23:59:46.602035[postgresql-14][17-1] 2023-01-11 23:59:46 GMT [949]: [3-1] user=postgres,db=defaultdb,app=aiven-pruned,client=[local] LOG: disconnection: session time: 0:00:00.010 user=postgres database=defaultdb host=[local]

* ``'%m [%p] %q[user=%u,db=%d,app=%a] '``

  .. code-block::

    [pg-user-test-1]2023-01-12T00:00:57.839867[postgresql-14][18-1] 2023-01-12 00:00:57.839 GMT [1323] [user=postgres,db=defaultdb,app=[unknown]] LOG: connection authorized: user=postgres database=defaultdb application_name=aiven-pruned
    [pg-user-test-1]2023-01-12T00:00:57.849223[postgresql-14][19-1] 2023-01-12 00:00:57.849 GMT [1323] [user=postgres,db=defaultdb,app=aiven-pruned] LOG: disconnection: session time: 0:00:00.010 user=postgres database=defaultdb host=[local]

After selecting one of the available log formats from the drop down menu, select **Save configuration** to have the change take effect.  Once the setting has been enabled, you can navigate to the logs tab on your service page to check if the log format has been successfully changed.

At the moment, the formats available are known to be compatible with majority of the log analysis tools.

For additional information on how to check the service logs, you can visit our :doc:`access service logs </docs/platform/howto/access-service-logs>` documentation.