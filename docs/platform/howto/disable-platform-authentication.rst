Disable platform authentication
===============================

If you have already :doc:`set up a SAML authentication <saml/saml-authentication>` method then you might want to disable the default password-based platform authentication method to prevent it being used to access projects within your account.

Here are the steps to follow to disable platform authentication:

1. Log in to the `Aiven Console<https://console.aiven.io/>`_ using your alternative authentication (for example, SAML) method. 

.. warning::

   You must not be logged in with any open sessions using the password-based platform authentication.
   
2. From the top-right corner of the `Aiven Console<https://console.aiven.io/>`_, click on **User information** and then click **Authentication** tab.

3. Use the toggle switch under the *Authentication methods* section to turn off platform authentication for the **Aiven Password** method.

.. warning::

    Once you disable platform authentication, you'll receive an error if you try to login using the Aiven CLI without supplying a token. 

Check out :doc:`the dedicated CLI docs <../../tools/cli/account/account-authentication-method>` to learn how to view and update account authentication methods from the Aiven CLI.