Manage user two-factor authentication
=====================================

The two-factor authentication (also known as 2-Step verification or 2FA) in Aiven allows further securing logins by requiring a second authentication code in addition to the user password. Currently, Aiven supports two-factor authentication using the `Google Authenticator <https://en.wikipedia.org/wiki/Google_Authenticator>`_ mobile application. Find in this article information on how to manage your two-factor authentication settings. 

.. _setup-2fa:

Set up two-factor authentication
--------------------------------

Find the steps in how to set up the two-factor authentication in your account. You need to perform steps on both your phone and in your user account.

1. Log in to the `Aiven web console <https://console.aiven.io>`_.
2. Click **User information**, then select **Authentication** tab.
3. Click the button next to "Disabled" to enable the feature. Enter your password to confirm the action.
4. Install the Google Authenticator application to your mobile device
5. On your mobile, open the Google Authenticator application and add a new entry by selecting the **Scan a QR code** button.
6. Point the camera to the QR code visible on the Aiven web console. A new "Aiven" entry will be added to Google Authenticator list of applications.
7. Enter a generated number sequence from the Google Authenticator app to the confirmation code field on the Aiven web console.
8. Click in **Enable Two-Factor Auth** button.

Optionally, you can also choose in your Google Authenticator app to **Enter a setup key** instead of the **Scan a QR code**. You can find the secret key for the manual configuration below the generated QR code on the Aiven web console. You can proceed with the manual configuration by writing the secret in your Google authenticator.

.. _disable-2fa:

Disable user two-factor authentication
--------------------------------------

If you need to disable two-factor authentication settings from your account, you can do it by following the steps:

1. Log in to the `Aiven web console <https://console.aiven.io>`_.
2. Click **User information**, then select **Authentication** tab.
3. On **Two-factor authentication**, click in the slider to show *Disabled*

With those steps, you can disable your user's two-factor authentication. Disabling two-factor authentication means that you no longer need to provide both the password and a time-based authentication code generated to login into your account. 

Reset user two-factor authentication
------------------------------------

If you have lost access to your two-factor authenticator for some reason like phone damage or loss, you will not be able to sign in. However, you can regain access to your account by resetting your password on the `Aiven web console <https://console.aiven.io>`_, and completing the password reset steps. 

.. important::
    
    Resetting your Aiven password will automatically disable the two-factor authentication from your account.

If you still have access to the original device and wish to switch to another, you can turn off the 2FA authentication as described on :ref:`disable user two-factor authentication<disable-2fa>`. After that, you can enroll a new device as described in :ref:`set up two-factor authentication <setup-2fa>`.
