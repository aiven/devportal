Scaling services
================

When spinning a new Aiven service, you are not tied to a plan. Your services can be adjusted to better match your needs. Services can be moved to a higher or lower plan, and to a different tier—Startup, Business or Premium.


Scale a service using the console
---------------------------------

1. Log in to the Aiven console. 
2. Go to your **Services**, and open the service you want to scale.
3. On the **Overview** tab, scroll down to **Change Plan**. 
4. Select the new service plan and new tier, if required.
5. Click **Change**.

Your service will be in a *Rebuilding* state, and once complete will be on the new plan. The service will still be accessible through the process. 


Scale a service using the Aiven client (CLI)
--------------------------------------------

1. Prepare the command to scale the service.

2. Add the ``service_to_scale`` parameter to specify the service you want to scale, and the ``service_plan`` for the target plan. For example, if you want to scale your service to ``service_plan``, the command would be something like:

    avn service update --plan service_plan service_to_scale

You can follow the progress of your changes with:

    avn service list




