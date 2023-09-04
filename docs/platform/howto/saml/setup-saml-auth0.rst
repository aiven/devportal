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

1. Log in to `your Auth0 account <https://manage.auth0.com>`_.

2. Select **Applications**.

3. Click **Create Application**. 

4. Enter an application name.

5. Choose **Regular Web Applications** and click **Create**. 

6. After your application is created, go to the **Addons** tab.

7. Enable the **SAML 2 WEB APP** option.

8. Click on the **SAML 2 WEB APP** option. The **Settings** tab opens.

9. Set the ``Application Callback URL`` to the ``ACS URL`` from the Aiven Console.

10. In the **Settings** section for the Application Callback URL, remove the existing configuration and add the following field mapping configuration:

.. code-block:: shell

  {
    "email": "email",
    "first_name": "first_name",
    "identity": "email",
    "last_name": "last_name",
    "mapUnknownClaimsAsIs": true
  }

11. Click **Enable** and **Save**.

12. On the **Usage** tab, make a note of the ``Identity Provider Login URL``,  ``Issuer URN``, and ``Identity Provider Certificate``. These are needed for the SAML configuration in Aiven Console.


Finish the configuration in Aiven
----------------------------------

Go back to the **Authentication** page in `Aiven Console <https://console.aiven.io/>`_ to enable the SAML authentication method:

1. Select the name of the Auth0 method that you created.

2. In the SAML configuration section, click **Edit**. 

3. Add the configuration settings from Auth0:

* Set the ``SAML IDP URL`` to the ``Identity Provider Login URL`` from Auth0.
* Set the ``SAML Entity ID`` to the ``Issuer URN`` from Auth0 .
* Paste the certificate from Auth0 into the ``SAML Certificate`` field.

4. Click **Edit method** to save your changes.

5. Toggle on **Enable authentication method** at the top of the page. 

6. In the **Signup and link accounts URLs** section, copy the appropriate link and send it to your users to switch them to the new IdP:
  
* **Signup URL**: For users that don't have an Aiven user account and need to create a new Aiven user linked to this IdP.
* **Account link URL**: For users that already have an Aiven user account to link their existing Aiven user with the configured IdP. 
  
  .. note::
    If you set up a SAML authentication method before and are now switching to a new IdP, existing users need to log in with the new account link URL to finish the setup.

Troubleshooting
---------------

If you have issues, you can use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_ to check the process step by step. 
