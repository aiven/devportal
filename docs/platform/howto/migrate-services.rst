Migrating services
==================

When spinning a new Aiven service, you are not tied to a cloud provider or region. Your services can be migrated to better match your needs. Services can be moved to another cloud provider, or another region within the same provider, or both.

1. Log in to the `Aiven console <https://console.aiven.io/>`_.
2. Go to your **Services**, and open the service you want to scale.
3. On the **Overview** tab, scroll down to **Migrate Cloud**. 
4. Select the new service plan and new tier, if required.
5. Click **Migrate**.

Your service will be in a *Rebalancing* state, and once complete will be on the new cloud. The service will still be accessible through the process. 

You can also use the :ref:`dedicated service update function <avn-cli-service-update>` to create a new service user via the :doc:`Aiven CLI </docs/tools/cli>`.