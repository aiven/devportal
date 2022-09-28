Set up SAML with Auth0
=========================

SAML ( *Security Assertion Markup Language* ) is a standard for
exchanging authentication and authorization data between an identity
provider and a service provider. To read more about SAML check the :doc:`dedicated page <saml-authentication>`.

The following is the procedure to setup SAML with `Auth0 <https://auth0.com/>`_.

Prerequisite steps in Aiven
-----------------------------------

1. Login to the `Aiven Console <https://console.aiven.io>`_

2. Under **Projects** in the top left, click the drop down arrow and
then on **See All Accounts**

3. Click on the Account you want to edit or create a new one

4. Select the **Authentication** tab

5. Create a new Authentication Method, call it `Auth0` (or similar), select *Method Type* to be **SAML**, and then
choose the team to add invited people to (or leave it blank)

6. Be sure to make a note of the configuration URLs (metadata URL and ACS URL).

.. note::
   At this point, the state will be ``Pending Configuration``.

Setup on Auth0
----------------

1. `Register <https://auth0.com/signup>`_ for an Auth0 account or sign into `your existing Auth0 account <https://manage.auth0.com>`_. 

2. Select **Applications** and then **Create Application**. 

3. Give your application a name (for example, "Aiven App"), choose "Regular Web Applications", and hit **Create**. 

3. Once your application has been created, go to the **Addons** tab and enable *SAML 2 WEB APP* option.

4. Click on the *SAML 2 WEB APP* option to open the settings dialog.

5. Set the *Application Callback URL*  to the *ACS URL* provided by the Aiven Console.

6. Under the *Application Callback URL*, in the settings section, remove existing codeblock and add the following mapping configuration:

.. code-block:: shell

   {
    "mappings": {
      "email": "email"
    },
    "nameIdentifierFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
    "nameIdentifierProbes": [
      "email"
    ]
   }

7. Once done, click **Enable** and **Save**. From the **Usage** tab, make a note of the ``Identity Provider Login URL``. This will need to be copied into the SAML config in the Aiven Console. You will also need the ``Issuer URN`` (we refer to it as the ``Entity ID``) and the ``Identity Provider Certificate``.

Finish the configuration in Aiven
---------------------------------

1. From the Aiven console **Authentication** tab, click on **Set SAML configuration**

2. Set the ``SAML IDP URL`` as the ``Identity Provider Login URL`` from Auth0 

3. Set the ``SAML Entity ID`` as the ``Issuer URN`` from Auth0

4. Paste the certificate from Auth0 into ``SAML Certificate``

5. Do **not** enable ``Enable IdP login`` unless you set ``SAML Initiator`` to ``Auth0`` in your Auth0 application

6. Save that and you are good to go! Make sure the authentication method is enabled and you can then use the **Signup URL** to invite new people and **Account link URL** for those that already have an Aiven login.

If you have issues, you can use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_ to  check the process step by step. The errors shown in the tracker should help you to debug the issues. If it does not work, you can request help by sending an email at support@Aiven.io.
