Set up SAML with Auth0
=========================

This article explains how to set up SAML with `Auth0 <https://auth0.com/>`_ for an organization in Aiven. For more information on SAML and instructions for other identity providers, see the :doc:`Enable SAML authentication </docs/platform/howto/saml/saml-authentication>` article.

Prerequisite steps in the Aiven Console
----------------------------------------

#. In the organization, click **Admin**.

#. Select **Authentication**.

#. Click **Add authentication method**.

#. Enter a name and select SAML. You can also select the teams that users will be added to when they sign up or log in through this authentication method.

You are shown two parameters needed to set up the SAML authentication in Auth0:

* Metadata URL
* ACS URL

Set up on Auth0
----------------

#. `Register <https://auth0.com/signup>`_ for an Auth0 account or sign into `your existing Auth0 account <https://manage.auth0.com>`_.

#. Select **Applications** and **Create Application**. 

#. Enter an application name.

#. Choose **Regular Web Applications**.

#. Click **Create**. 

#. After your application is created, go to the ``Addons`` tab.

#. Enable the **SAML 2 WEB APP** option.

#. Click on the **SAML 2 WEB APP** option. This opens the ``Settings`` tab.

#. Set the ``Application Callback URL`` to the ``ACS URL`` provided by the Aiven Console.

#. In the ``Settings`` section, under ``Application Callback URL``, remove the existing configuration and add the following field mapping configuration:

.. code-block:: shell

   {
     "email": "email",
     "first_name": "first_name",
     "identity": "email",
     "last_name": "last_name"
     "mapUnknownClaimsAsIs": true
   }

#. Click **Enable** and **Save**.

#. On the **Usage** tab, make a note of the ``Identity Provider Login URL``,  ``Issuer URN``, and the ``Identity Provider Certificate``. These are needed for the SAML configuration in the Aiven Console.

Finish the configuration in Aiven
---------------------------------

1. From the Aiven console **Authentication** tab, click on **Set SAML configuration**

2. Set the ``SAML IDP URL`` as the ``Identity Provider Login URL`` from Auth0 

3. Set the ``SAML Entity ID`` as the ``Issuer`` from Auth0 (example: ``urn:dev-i-fiqy2a.us.auth0.com``)

4. Paste the certificate from Auth0 into ``SAML Certificate``

5. Save that and you are good to go! Make sure the authentication method is enabled and you can then use the **Signup URL** to invite new people and **Account link URL** for those that already have an Aiven login.

If you have issues, you can use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_ to  check the process step by step. The errors shown in the tracker should help you to debug the issues. If it does not work, you can request help by sending an email at support@Aiven.io.
