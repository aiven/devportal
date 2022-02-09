Create a new Aiven service user
================================

Services users are users that only exist in the scope of the corresponding Aiven service. They are unique to this service and not shared with any other services, and can be granted restricted permissions compared to the default ``avnadmin`` user. You can add service users for all the Aiven services, with the exception of Aiven for Apache Flink® and Aiven for Grafana.

Create a new service user using the Aiven console
-------------------------------------------------

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. On the **Services** page, click on the service name.

3. Select the **Users** tab (sometimes called **Users and Roles**):

   a. Enter a name for your service user.

      If a password is required, a new random password will be generated automatically. This can be modified later.

4. Click **Add User** on the right hand side of the console.

   A popup alert will display the result of the operation, for instance:

    Success!
    Service user 'testuser' has been created.


Create a new service user using the Aiven client (CLI)
------------------------------------------------------

1. Prepare the command to add the service user to your service.


2. Add the ``service_target`` parameter to specify the service for which you want to create a new service user, and the ``service_user`` for the new user. For instance, to add the service user ``service_user`` to the service ``service_target``, you would use this command::

    avn service user-create --username service_user service_target

The changes are applied immediately.
