Add OneLogin as an identity provider 
====================================

Use `OneLogin <https://www.onelogin.com/>`_ to give your organization users single sign-on (SSO) access to Aiven. 


Prerequisite steps in Aiven Console
------------------------------------

Add OneLogin as an :ref:`identity provider <add-idp-aiven-console>` in the Console. 


.. _configure-saml-onelogin:

Configure SAML on OneLogin
---------------------------

#. Log in to the `OneLogin Admin console <https://app.onelogin.com/login>`_. 

#. Select **Applications** and click **Add App**. 

#. Search for **SAML Custom Connector (Advanced)** and select it.

#. Change the **Display Name** to ``Aiven``.

#. Add any other visual configurations you want and click **Save**.

#. In the **Configuration** section of the menu, set the following parameters:

   .. list-table::
      :header-rows: 1
      :align: left

      * - Parameter
        - Value
      * - ``ACS URL Validation``
        - ``[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)``
      * - ``ACS URL``
        - ``ACS URL`` from Aiven Console 
      * - ``Login URL``
        - ``https://console.aiven.io``
      * - ``SAML Initiator``
        - ``Service Provider`` (or ``OneLogin`` if your users will sign in through OneLogin)
      * - ``SAML nameID format``
        - ``Email``
   

#. Click **Save**.

#. In the **SSO** section of the menu, set **SAML Signature Algorithm** to ``SHA-256``.

#. Copy the certificate content, ``Issuer URL`` and ``SAML 2.0 Endpoint (HTTP)``. These are needed for the SAML configuration in Aiven Console.

#. Click **Save**

#. Assign users to this application. 


Finish the configuration in Aiven
---------------------------------

Go back to the **Authentication** page in `Aiven Console <https://console.aiven.io/>`_ to enable the SAML authentication method:

1. Select the name of the OneLogin method that you created.

2. In the SAML configuration section, click **Edit**. 

3. Add the configuration settings from OneLogin: 

* Set the ``SAML IDP URL`` to the ``SAML 2.0 Endpoint (HTTP)`` from OneLogin. 

* Set the ``SAML Entity ID`` to the ``Issuer URL`` from OneLogin.

* Paste the certificate from OneLogin into ``SAML Certificate``.

4. If you set ``SAML Initiator`` to ``OneLogin`` in your OneLogin application, then toggle on ``IdP login``.

5. Toggle on **Enable authentication method** at the top of the page. 

6. In the **Signup and link accounts URLs** section, copy the appropriate link and send it to your users to switch them to the new IdP:
  
* **Signup URL**: For users that don't have an Aiven user account and need to create a new Aiven user linked to this IdP.
* **Account link URL**: For users that already have an Aiven user account to link their existing Aiven user with the configured IdP. 
  
  .. note::
    If you set up a SAML authentication method before and are now switching to a new IdP, existing users need to log in with the new account link URL to finish the setup.

   
Troubleshooting
----------------

If you are getting errors, try this:

#. Go to the app in OneLogin and click **Settings**.

#. Under **More Actions**, select **Reapply entitlement Mappings**.

If you continue to have issues, you can use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_ to check the process step by step. 

