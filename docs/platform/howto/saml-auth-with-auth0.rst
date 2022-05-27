Setting up SAML with Auth0
==========================

Using Auth0 as an Identity Provider (IdP) with Aiven SAML Authentications
--------------------------

You first need to create an Aiven account and an Aiven account authentication method. Account is a top level concept that can be associated with multiple different projects and with which you can make corporate level configuration like the authentication setup. You can do this in the `Aiven Console <https://console.aiven.io>`_.

Creating the Aiven account
--------------------------

Once you have logged into the Aiven Console, you should see your projects in the top left of your screen. Click the current project to open the project select and click See all projects. This should open a Projects & Accounts modal.

.. image:: /images/platform/howto/see-all-projects.png

On the Projects & Accounts modal, click on Create account  and you will be taken to a page where you provide a name, project(s) to link it to and the option to invite other admins.

.. image:: /images/platform/howto/console-aiven-account-create.png

Once created, you will see an overview of the account just created. A tab, called Authentication, will let you add a new method (in this case: SAML) and configure them.

.. image:: /images/platform/howto/authentication-methods.png

Clicking on Add Authentication Method creates a dialog where you can name your method, specify the type and a default team you would want members to join.

.. image:: /images/platform/howto/add-authentication-method.png

Once you click Add, you will see the configuration URLs for your Identity Provider (do not worry about making a note of these, you can access them at any time).

.. image:: /images/platform/howto/configuration-urls.png

For now, we are done with the Aiven side of this, let's move on to Auth0 and creating our logon.

Creating the Auth0 Application
------------------------------

Head to auth0.com and login (or signup), from the dashboard, you will see an option for Applications. 

.. image:: /images/platform/howto/auth0-applications.png

Click on Create Application and you can select Regular Web Applications as the type. Click Create  and you will be taken through to an overview of the application. We will not be using the Quickstart  here, so we will focus on Settings and Add-ons. 

.. image:: /images/platform/howto/create-application-auth0.png

Once your application has been created, click on the Settings icon and then go to the Add-ons tab. Enable the SAML 2.0 Web App and click on it to open the settings dialog.

.. image:: /images/platform/howto/addon-saml-web-app-auth0.png

You will need to set the Application Callback URL to the ACS URL provided by the Aiven Console. In the settings, some mapping configuration needs to be done, the following should be added::

    {
    "mappings": {
        "email": "email"
    },
    "nameIdentifierFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
    "nameIdentifierProbes": [
        "email"
    ]
    }

Once done, click Save  and then on the Usage  tab and make a note of the Identity Provider Login URL , this will need to be copied into the SAML config in the Aiven Console. You will also need the Issuer URN (we refer to it as the Entity ID ) and the certificate. Remember to enable your authentication method.

In the Settings  tab, you will see a field for Allowed Callback URLs , copy your Aiven ACS URL  into this box and Save Changes .

Now, you should be good to go. Click on your Account link URL to link your current user account with the Auth0 account to make sure that the whole flow is working!