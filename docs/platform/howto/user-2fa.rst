Manage two-factor authentication
==================================

Two-factor authentication (also known as 2-step verification or 2FA) in Aiven provides an extra level of security by requiring a second authentication code in addition to the user password.  

.. _enable-2fa:

Enable two-factor authentication
--------------------------------

To enable two-factor authentication on the `Aiven Console <https://console.aiven.io/>`_:

#. Click the **User information** icon in the top right and select **Authentication**.

#. On the **Aiven Password** method, toggle on **Two-factor authentication**. 

#. Enter your password and click **Next**. 

#. On your mobile device, open your authenticator app and scan the QR code shown in Aiven Console. 

   .. note:: Alternatively, you can enter the TOTP secret from the Aiven Console into your authenticator app.

#. Enter the code from the authenticator app in the **Confirmation code** field in Aiven Console.

#. Click **Enable**.

If you want to change the  mobile device that you use for two-factor authentication, you need to first :ref:`disable two-factor authentication <disable-2fa>` and then enable it on the new device.

.. _disable-2fa:

Disable two-factor authentication
----------------------------------

To disable two-factor authentication on the Aiven Console:

#. Click the **User information** icon in the top right and select **Authentication**.

#. On the **Aiven Password** method, toggle off **Two-factor authentication**. 

#. Enter your password and click **Disable Two-Factor Authentication**.

.. warning::
    
    Disabling two-factor authentication will automatically revoke your existing authentication tokens. 

Reset two-factor authentication
---------------------------------

If you have lost access to your mobile device or authenticator app, you can regain access to your account by resetting your Aiven password: 

#. Log out of Aiven Console.

#. Enter your login email and click **Log in**.

#. Click **Forgot password?**. 

#. Enter your login email and click **Reset your password**.

#. Follow the instructions in the password reset email to set a new password.

#. :ref:`Enable two-factor authentication <enable-2fa>` on your new mobile device or authenticator app.
