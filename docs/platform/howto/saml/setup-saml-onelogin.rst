Set up SAML with OneLogin
==============================

SAML ( *Security Assertion Markup Language* ) is a standard for
exchanging authentication and authorization data between an identity
provider and a service provider. To read more about SAML check the :doc:`dedicated page <saml-authentication>`.

The following is the procedure to setup SAML with `OneLogin <https://www.onelogin.com/>`_.

Prerequisite steps in Aiven
-----------------------------------

1. Login to the `Aiven Console <https://console.aiven.io>`_

2. Under **Projects** in the top left, click the drop down arrow and
then on **See All Accounts**

3. Click on the Account you want to edit or create a new one

4. Select the **Authentication** tab

5. Create a new Authentication Method, call it `OneLogin` (or similar) and then
choose the team to add invited people to (or leave it blank)

Setup on OneLogin
-----------------

1. Enter OneLogin **Administration** portal (top right link by your username)

2. Select **Applications** and then **Add App**. 

3. Search for **SAML Custom Connector (Advanced)** and select it.

3. Change the Display Name to `Aiven`` and add any other visual configurations you like and click **Save**.

OneLogin configuration
~~~~~~~~~~~~~~~~~~~~~~

1. In the **Configuration** section of the menu, set the following parameters:

   .. list-table::
      :header-rows: 1
      :align: left

      * - Parameter
        - Value
      * - ``ACS URL Validation``
        - ``[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)``
      * - ``ACS URL``
        - the ``ACS URL`` displayed in the Aiven authentication method you created
      * - ``Login URL``
        - ``https://console.aiven.io``
      * - ``SAML Initiator``
        - ``Service Provider`` (or ``OneLogin`` if your users will sign in through OneLogin)
      * - ``SAML nameID format``
        - ``Email``
   
2. Click **Save**

2. In the **SSO** section of the menu:

   1. Set ``SAML Signature Algorithm`` to ``SHA-256``

   2. View the certificate and copy the contents

   3. Copy the ``Issuer URL`` and the ``SAML 2.0 Endpoint (HTTP)``

   4. Click **Save**

3. Assign users to this application and head back to Aiven to complete the configuration

Finish the configuration in Aiven
---------------------------------

1. In the new authentication method, click *Edit* next to the SAML configuration

2. Set the ``SAML IDP URL`` as the ``SAML 2.0 Endpoint (HTTP)`` from OneLogin 

3. Set the ``SAML Entity ID`` as the ``Issuer URL`` from OneLogin

4. Paste the certificate from OneLogin into ``SAML Certificate``

5. Do **not** enable ``Enable IdP login`` unless you set ``SAML Initiator`` to ``OneLogin`` in your OneLogin application

6. Save that and you are good to go! Make sure the authentication method is enabled and you can then use the **Signup URL** to invite new people and **Account link URL** for those that already have an Aiven login.


.. note::
   You will need to assign users in OneLogin before the connection will work. If you experience errors, try selecting **Reapply entitlement Mappings** under *More Actions* in the *Settings* of your OneLogin App.

If you have issues, you can use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_ to  check the process step by step. The errors shown in the tracker should help you to debug the issues. If it does not work, you can request help by sending an email at support@Aiven.io.
