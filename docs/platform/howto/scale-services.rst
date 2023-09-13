Scale your service
==================

When creating a new Aiven service, you are not tied to a plan. Your services can be adjusted to better match your needs. Services can be moved to a higher or lower plan, and to a different tier—Startup, Business or Premium.


1. Log in to `Aiven Console <https://console.aiven.io/>`_.
2. Go to your **Services**, and select the service you want to scale.
3. On the **Overview** page of your service, scroll down to **Service plan** > **Change plan**. 
4. In the **Change service plan** window, select the new service plan and new tier, if required.
5. Select **Change**.

.. topic:: Result

   Your service is in the *Rebuilding* state. Once the rebuilding is over, your new service plan will be active on your service. The service is still accessible through the plan-change process. 

.. note::

    - You can also use the :ref:`dedicated service update function <avn-cli-service-update>` to scale your service plan via the :doc:`Aiven CLI </docs/tools/cli>`.
    - When you perform a service upgrade or downgrade horizontally, it is required to include any additional disk existing on the service. For example, ``Startup-4`` to ``Business-4`` or ``Business-4`` to ``Startup-4``.
