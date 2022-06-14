Disable platform authentication
===============================

How to prevent users signing in using username and password
-----------------------------------------------------------

If you have already set up an alternative authentication method then you might want to disable the default password-based Platform authentication method to prevent it being used to access projects within your account.

To do this, you must log in to the Aiven Console using your alternative authentication method. You must not be logged in with any open sessions using the password-based Platform authentication.

Navigate to the Authentication tab in your account and then click the button to disable the Platform authentication. If you have an open session which is using that authentication method you will receive an error message. To resolve this, log out of the open session and try again.

.. image:: /images/platform/authentication-method.png
    :alt: Auth methods overview

Using the Aiven CLI
-------------------

Please note that if you are using the avn CLI to make changes to your project then you will need to generate an access token for it manually (rather than using the avn login command).

If you try to use the ``avn login`` command you will see an error like this::

    ERROR	command failed: Error: {"errors":[{"message":"You have not signed in with authentication method that is enabled for the account","status":403}],"message":"You have not signed in with authentication method that is enabled for the account"}

To authenticate the client you should manually generate one from your user profile in the Authentication tab: https://console.aiven.io/profile/auth.

This access token should be stored along with your user account email address in a configuration file at ``~/.config/aiven/aiven-credentials.json``::

    {
    "email": <your_email_address,
    "auth_token": <your_auth_token>
    }

After creating this file you will be able to use the avn client even without platform authentication enabled.