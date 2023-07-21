Create a new Aiven service user
================================

Service users are users that only exist in the scope of the corresponding Aiven service. They are unique to this service and not shared with any other services, and can be granted restricted permissions compared to the default ``avnadmin`` user. You can add service users for all the Aiven services, with the exception of Aiven for Apache Flink® and Aiven for Grafana®.

.. warning::

   By default, the maximum amount of users allowed on a service is 50. 

   If you would like to increase the maximum number of users allowed for a service, :doc:`create a support ticket </docs/platform/howto/project-support-center>` to request an increase.

1. Log in to `Aiven Console <https://console.aiven.io/>`_.

2. On the **Services** page, select your service.

3. On the **Overview** page of your service, select **Users** from the sidebar.
4. In the **Users** page, select **Add service user**.
5. In the **Create a service user** window

   a. Enter a name for your service user.

      If a password is required, a new random password will be generated automatically. This can be modified later.

   b. Set up all the other configuration options (such as authentication, roles, or replication), and select **Add service user**.

.. topic:: Result
   
   A popup alert displays the result of the operation informing about the creation of your new user.

.. note::

    You can :ref:`create a new service user using the Aiven CLI <avn-service-user-create>` as well.
