Migrate service to another cloud or region
==========================================

When migrating a service, the migration happens in the background and does not affect your service until the service has been rebuilt at the new region. The migration includes the DNS update for the named service to point to the new region. 
Most of the services have usually no service interruption expected. However, for services like PostgreSQL®, MySQL®, and Redis®*, it may cause a short interruption (5 to 10 seconds) in service while the DNS changes are propagated.

The short interruption mentioned above does not include the potential delays caused by client side library implementation.

When spinning a new Aiven service, you are not tied to a cloud provider or region. Your services can be migrated to better match your needs. Services can be moved to another cloud provider, or another region within the same provider, or both.

1. Log into the `Aiven Console <https://console.aiven.io/>`_, select your project and then select the service you want migrate to another cloud or region.
2. On the service page, click **Service settings** from the sidebar. 
3. In the **Cloud and network** section, click **Actions (...)**. 
4. From the dropdown menu, click **Change cloud or region**. 
5. In the **Migrate service to another cloud** window, select new cloud provider and region.
6. Select **Migrate**.

.. topic:: Result

   Your service is in the *Rebuilding* state. Once the rebuilding is over, your new cloud provider and region will be in use.

.. important::
    
    The service's URI remains the same after the migration. 

.. note::

   You can also use the :ref:`dedicated service update function <avn-cli-service-update>` to migrate a service via the :doc:`Aiven CLI </docs/tools/cli>`.
