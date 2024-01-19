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

Go back to the Aiven Console to :ref:`configure the IdP <configure-idp-aiven-console>` and complete the setup.

