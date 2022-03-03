Create a new Aiven service user
================================

Service users are users that only exist in the scope of the corresponding Aiven service. They are unique to this service and not shared with any other services, and can be granted restricted permissions compared to the default ``avnadmin`` user. You can add service users for all the Aiven services, with the exception of Aiven for Apache Flink® and Aiven for Grafana.

1. Log in to the `Aiven console <https://console.aiven.io/>`_.

2. On the **Services** page, click on the service name.

3. Select the **Users** tab (sometimes called **Users and Roles**):

   a. Enter a name for your service user.

      If a password is required, a new random password will be generated automatically. This can be modified later.

4. Click **Add User** on the right hand side of the console.

   A popup alert will display the result of the operation, for instance::

    Success!
    Service user 'testuser' has been created.

YOu can also use the :ref:`dedicated user-create function <avn-service-user-create>` to create a new service user via the :doc:`Aiven CLI </docs/tools/cli>`.
