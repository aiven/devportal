Setting up SAML with OneLogin
===============================

Start with Aiven
----------------

1. Login to the `Aiven console <https://console.aiven.io>`_

2. Under *Projects* in the top left, click the drop down arrow and
then on **See All Accounts**

3. Click on the Account you want to edit or create a new one

4. Select the *Authentication* tab

5. Create a new Authentication Method, call it *OneLogin* (or similar) and then
choose the team to add invited people to (or leave it blank)

OneLogin
---------

1. Enter the *Administration* portal (top right link by your username)

2. Select *Applications* and then **Add App**. Search for `SAML Custom Connector (Advanced)`` and select it.

3. Change the Display Name to `Aiven`` and add any other visual configurations you like and click **Save**.

Configuration
-------------

1. In the *Configuration* section of the menu:
   
   1. Set `ACS URL Validation`` to: `[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)`
   
   2. Set `ACS URL` to the ACS URL in the Aiven authentication method you created
   
   3. Set `Login URL` to https://console.aiven.io
   
   4. Set `SAML Initiator` to `Service Provider` (or `OneLogin` if your users will sign in through OneLogin)
   
   5. Set `SAML nameID format` to `Email`
   
   6. Click **Save**

2. In the *SSO* section of the menu:

   1. Set `SAML Signature Algorithm` to `SHA-256`

   2. View the certificate and copy the contents

   3. Copy the `Issuer URL` and the `SAML 2.0 Endpoint (HTTP)``

   4. Click **Save**

3. Assign users to this application and head back to Aiven to complete the configuration

Aiven
-----

1. In your new authentication method, click *Edit* next to your SAML configuration

2. Set the `SAML IDP URL` as the `SAML 2.0 Endpoint (HTTP)` from OneLogin 

3. Set the `SAML Entity ID` as the `Issuer URL` from OneLogin

4. Paste the certificate from OneLogin into `SAML Certificate``

5. Do not enable `Enable IdP login` unless you set `SAML Initiator` to `OneLogin` in your OneLogin application

6. Save that and you are good to go! Make sure the Method is enabled and you can then use the `Signup URL` to invite new people and `Account link URL` for those that already have an Aiven login.


.. note::
    
   You will need to assign users in OneLogin before the connection will work. If you experience errors, try selecting **Reapply entitlement Mappings** under *More Actions* in the *Settings* of your OneLogin App.

Still having issues? While going through the process, use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_.
The errors shown in there should help you to debug the issue. If it does not work, drop us a message at support@Aiven.io
