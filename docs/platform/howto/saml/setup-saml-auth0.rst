Set up SAML with Auth0
=======================

This article explains how to set up SAML with `Auth0 <https://auth0.com/>`_ for an organization in Aiven. For more information on SAML and instructions for other identity providers, see the :doc:`Set up SAML authentication </docs/platform/howto/saml/saml-authentication>` article.

Prerequisite steps in Aiven Console
------------------------------------

#. In the organization, click **Admin**.

#. Select **Authentication**.

#. Click **Add authentication method**.

#. Enter a name and select SAML. You can also select the teams that users will be added to when they sign up or log in through this authentication method.

You are shown two parameters needed to set up the SAML authentication in Auth0:

* Metadata URL
* ACS URL

Configure SAML on Auth0
------------------------

#. Log in to `your Auth0 account <https://manage.auth0.com>`_.

#. Select **Applications**.

#. Click **Create Application**. 

#. Enter an application name.

#. Choose **Regular Web Applications** and click **Create**. 

#. After your application is created, go to the ``Addons`` tab.

#. Enable the **SAML 2 WEB APP** option.

#. Click on the **SAML 2 WEB APP** option. The ``Settings`` tab opens.

#. Set the ``Application Callback URL`` to the ``ACS URL`` from the Aiven Console.

#. In the ``Settings`` section under ``Application Callback URL``, remove the existing configuration and add the following field mapping configuration:

.. code-block:: shell

   {
     "email": "email",
     "first_name": "first_name",
     "identity": "email",
     "last_name": "last_name"
     "mapUnknownClaimsAsIs": true
   }

#. Click **Enable** and **Save**.

#. On the **Usage** tab, make a note of the ``Identity Provider Login URL``,  ``Issuer URN``, and ``Identity Provider Certificate``. These are needed for the SAML configuration in the Aiven Console.


Finish the configuration in Aiven
----------------------------------

Go back to the **Authentication** page in the `Aiven Console <https://console.aiven.io/>`_ to enable the SAML authentication method:

#. Select the name of the Auth0 method that you created.

#. In the SAML configuration section, click **Edit**. 

#. Add the configuration settings from Auth0:

  * Set the ``SAML IDP URL`` to the ``Identity Provider Login URL`` from Auth0.
  * Set the ``SAML Entity ID`` to the ``Issuer URN`` from Auth0 .
  * Paste the certificate from Auth0 into the ``SAML Certificate`` field.

#. Click **Edit method** to save your changes.

#. Toggle on **Enable authentication method** at the top of the page. 

You can use the **Signup URL** to invite new users, or the **Account link URL** for those that already have an Aiven user account.

Troubleshooting
---------------

If you have issues, you can use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_ to check the process step by step. 
