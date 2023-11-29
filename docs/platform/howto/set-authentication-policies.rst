Set authentication policies for organization users 
===================================================

The authentication policy for your organization specifies the ways that users can access your organization on the Aiven platform: with a password, third-party authentication, or organization single sign-on (SSO). 

Authentication types
---------------------

Passwords and two-factor authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With password authentication enabled, users log in with their email address and password. For an added layer of security, you can enforce two-factor authentication (2FA) for password logins for all users in your organization.

When two-factor authentication is required, users won't be able to access any resources in your organization until they set up 2FA.

Third-party authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users can choose to log in using Google, Microsoft, or GitHub.

Organization identity providers (SSO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Organization users are restricted to logging in using SSO through an :doc:`identity provider </docs/platform/howto/saml/saml-authentication>`.  

Set an authentication policy 
------------------------------

To set an authentication policy for all users in an organization:

#. In the organization, click **Admin**.

#. Click **Authentication**.

#. Click the toggle for each authentication method that you want to allow.

#. Click **Save changes**.


