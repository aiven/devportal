Enable or disable password authentication
==========================================

Enable your Aiven password
---------------------------

You can authenticate directly with your email and password in the `Aiven Console <https://console.aiven.io/>`_ by enabling your Aiven password:

1. In the `Aiven Console <https://console.aiven.io/>`_, click the **User information** icon.
2. Click **Authentication methods**.
3. On the **Aiven Password** card, click the toggle to enable it. 

You will receive an email to reset your password and complete the process of enabling the password.

Disable your Aiven password
---------------------------

If you :doc:`set up a SAML authentication method <saml/saml-authentication>` and want to disable the password authentication to prevent it being used to access projects within your organization:

1. Log in to the `Aiven Console <https://console.aiven.io/>`_ using your alternative authentication method. 

2. Click on the **User information** icon.

3. Click **Authentication methods**.

4. On the **Aiven Password** card, click the toggle to disable it.

.. warning::

    Once disabled, you'll get an error if you try to log in using the Aiven CLI without a token. 

.. note:: You can also view and update authentication methods :doc:`using the Aiven CLI <../../tools/cli/account/account-authentication-method>`.