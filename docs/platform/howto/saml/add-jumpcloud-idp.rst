Add JumpCloud as an identity provider 
======================================

Use `JumpCloud <https://jumpcloud.com/>`_ to give your organization users single sign-on (SSO) access to Aiven. 


Prerequisite steps in Aiven Console
------------------------------------

Add JumpCloud as an :ref:`identity provider <add-idp-aiven-console>` in the Console. 


.. _configure-saml-jumpcloud:

Configure SAML on JumpCloud
----------------------------

#. In the `JumpCloud admin console <https://console.jumpcloud.com/login>`_, go to **SSO**.

#. Select **Custom SAML App**.

#. Set the **IdP Entity ID**.

#. Set the ``Audience URI (SP Entity ID)`` to the ``Metadata URL`` from the Aiven Console.

#. Set the ``ACS URL`` to the one from the Aiven Console.

#. Set the ``Default RelayState`` to the homepage of the Aiven Console, https://console.aiven.io.

#. Add an entry in **Attribute statements** with ``Service Provider Attribute Name`` of ``email`` and ``JumpCloud Attribute Name`` of ``email``.

#. Set the ``Login URL`` to the ``ACS URL`` from the Aiven Console.

#. In **User Groups**, assign the application to your user groups. 

#. Click **Activate**.

#. Download the certificate.

Finish the configuration in Aiven
----------------------------------

Go back to the **Authentication** page in `Aiven Console <https://console.aiven.io/>`_ to enable the SAML authentication method:

1. Select the name of the JumpCloud method that you created.

2. In the SAML configuration section, click **Edit**. 

3. Toggle on **IdP login**.

4. Add the configuration settings from JumpCloud:

* Set the ``SAML IDP URL`` to the ``IDP URL`` from JumpCloud.
* Set the ``SAML Entity ID`` to the ``IdP Entity ID`` from JumpCloud .
* Paste the certificate from JumpCloud into the ``SAML Certificate`` field.

5. Click **Edit method** to save your changes.

6. Toggle on **Enable authentication method** at the top of the page. 

7. In the **Signup and link accounts URLs** section, copy the appropriate link and send it to your users to switch them to the new IdP:
  
* **Signup URL**: For users that don't have an Aiven user account and need to create a new Aiven user linked to this IdP.
* **Account link URL**: For users that already have an Aiven user account to link their existing Aiven user with the configured IdP. 
  
  .. note::
    If you set up a SAML authentication method before and are now switching to a new IdP, existing users need to log in with the new account link URL to finish the setup.

Troubleshooting
---------------

If you have issues, you can use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_ to check the process step by step. 
