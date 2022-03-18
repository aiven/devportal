Add service user accounts
=========================

This article shows you how to add new users to your Aiven for ClickHouse® service, allowing you to control access grants for different purposes.

1. Log in to the `Aiven web console <https://console.aiven.io/>`_ and select your ClickHouse service.

#. Click **Users & Roles**.

   This page shows you a list of all the users that are currently available in your service. The default ``avnadmin`` user has all available access grants to the service.

   .. tip::
      To view the roles and grants for any of the listed users, click **View Details & Grants** for that user.

#. Enter a name for the new user and select a role.

   The role that you select defines the access grants that are assigned to the user. For more information on roles, :doc:`see this article <grant-privilege>`.

#. Click **Add User**.

   This creates the new user and shows you a summary of the information.

#. Copy the password on screen to a safe place. It can't be accessed again in future, however it can be reset if needed.


