Migrating services
==================

When spinning a new Aiven service, you are not tied to a cloud provider or region. Your services can be migrated to better match your needs. Services can be moved to another cloud provider, or another region within the same provider, or both.


Migrate a service using the console
-----------------------------------

1. Log in to the Aiven console. 
2. Go to your **Services**, and open the service you want to scale.
3. On the **Overview** tab, scroll down to **Migrate Cloud**. 
4. Select the new service plan and new tier, if required.
5. Click **Migrate**.

Your service will be in a *Rebalancing* state, and once complete will be on the new cloud. The service will still be accessible through the process. 


Migrate a service using the Aiven client (CLI)
----------------------------------------------

1. Prepare the command to scale the service.

a. You can retrieve the list of available clouds and regions with::

    avn cloud list

2. Add the ``service_to_migrate`` parameter to specify the service you want to migrate, and the ``cloud_region`` for the target plan. For example, if you want to migrate your service to ``cloud_region``, the command would be::

    avn service update --cloud cloud_region service_to_migrate

You can also follow the progress of your changes with::

    avn service list

