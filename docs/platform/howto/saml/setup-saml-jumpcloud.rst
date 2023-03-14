Set up SAML with JumpCloud
===========================

This article explains how to set up SAML with `JumpCloud <https://jumpcloud.com/>`_ for an organization in Aiven. For more information on SAML and instructions for other identity providers, see the :doc:`Set up SAML authentication </docs/platform/howto/saml/saml-authentication>` article.

Prerequisite steps in Aiven Console
------------------------------------

#. In the organization, click **Admin**.

#. Select **Authentication**.

#. Click **Add authentication method**.

#. Enter a name and select SAML. You can also select the teams that users will be added to when they sign up or log in through this authentication method.

You are shown two parameters needed to set up the SAML authentication in JumpCloud:

* Metadata URL
* ACS URL

Configure SAML on JumpCloud
----------------------------

#. In the `JumpCloud admin console <https://console.jumpcloud.com/login>`_, go to **SSO**.

#. Select **Custom SAML App**.

#. Set the ``IdP Entity ID`` to the ``Metadata URL`` from the Aiven Console.

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

You can use the **Signup URL** to invite new users, or the **Account link URL** for those that already have an Aiven user account.

Troubleshooting
---------------

If you have issues, you can use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_ to check the process step by step. 
