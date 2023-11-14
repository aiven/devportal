Set authentication policies for organization users 
===================================================

The authentication policy for your organization specifies the ways that users can access your organization on the Aiven platform: with a password, third-party authentication, or organization single sign-on (SSO). :doc:`Managed users </docs/platform/concepts/managed-users>` cannot log in with disabled authentication methods. Users that are not managed can log in with disabled methods, but they won't have access to the organization if they do.

Authentication types
---------------------

Passwords and two-factor authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With password authentication enabled, users log in with their email address and password. For an added layer of security, you can enforce two-factor authentication (2FA) for password logins for all users in your organization.

When two-factor authentication is required, users will be prompted to set up 2FA using an authenticator app. They won't be able to access any resources in your organization until they do this.

Third-party authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~

With third-party authentication enabled, users can choose to log in using Google, Microsoft, or GitHub.

Organization SSO
~~~~~~~~~~~~~~~~~

You can restrict your organization users to using SSO through a :doc:`verified domain </docs/platform/howto/manage-domains>`.  

Set an authentication policy 
------------------------------

To set an authentication policy for all users in an organization:

#. In the organization, click **Admin**.

#. Click **Authentication**.

#. Click the toggle for each authentication method that you want to allow.

* Password authentication: users log in using their email address and password
* Third-party authentication: users can log in using one of the supported providers (Google, Microsoft, or GitHub)
* Organization SSO: users from a :doc:`verified domain </docs/platform/howto/manage-domains>` can log in using an identity provider

#. Click **Save changes**.


