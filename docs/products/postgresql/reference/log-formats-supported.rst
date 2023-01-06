Log formats supported
=====================

Aiven for PostgreSQL® supports setting different log formats which are compatible with popular log analysis tools like ``pgbadger`` or ``pganalyze``.

You can use this functionality by navigating to your PostgreSQL® service on the `Aiven console <https://console.aiven.io/>`_.  

Scroll down to the end of the overview page under ``Advanced configuration`` and select the ``Change`` button.  You can then select the ``pg.log_line_prefix`` parameter where there is a set of formats available that can be viewed from the drop down menu:  

* ``'pid=%p,user=%u,db=%d,app=%a,client=%h '``
* ``'%t [%p]: [%l-1] user=%u,db=%d,app=%a,client=%h '``
* ``'%m [%p] %q[user=%u,db=%d,app=%a] '``

After selecting one of the available log formats from the drop down menu, you can click the ``Save advanced configuration`` button to have the change take effect.  Once the setting has been enabled, you can navigate to the logs tab on your service page to check if the log format has been successfully changed.

At the moment, the formats available are known to be compatible with majority of the log analysis tools.

For additional information on how to check the service logs, you can visit our :doc:`access service logs <../../../platform/howto/access-service-logs>` documentation.