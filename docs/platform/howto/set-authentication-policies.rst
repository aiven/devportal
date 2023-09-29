Set authentication policies for organization users 
===================================================

The authentication policy for your organization specifies the ways that users can access your organization on the Aiven platform. 

You can, for example, restrict organization users to using single sign-on through a :doc:`verified domain </docs/platform/howto/manage-domains>`. Alternatively, you can allow them to create a password or use third-party authentication providers like Google, Microsoft, and GitHub. For an added layer of security, you can enforce two-factor authentication for password logins.

:doc:`Managed users </docs/platform/concepts/managed-users>` cannot log in with disabled authentication methods. Users that are not managed can log in with disabled methods, but they won't have access to the organization if they do.

Set an authentication policy 
------------------------------

To set an authentication policy for all users in an organization:

#. In the organization, click **Admin**.

#. Click **Authentication**.

#. Click the toggle for each authentication method that you want to allow.

* Passoword authentication: users log in using their email address and password
* Third-party authentication: users can log in using one of the supported providers (Google, Mircosoft, or GitHub)
* Organization SSO: users from a :doc:`verified domain </docs/platform/howto/manage-domains>` can log in using an identity provider

#. Click **Save changes**.


