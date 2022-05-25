Setting up SAML authentication with Google G-Suite
==================================================

You first need to create an Aiven account and an Aiven account authentication method. Account is a top level concept that can be associated with multiple different projects and with which you can make corporate level configuration like the authentication setup. You can do this in Aiven Console.

Creating the Aiven account
--------------------------

Once you have logged into the Aiven Console, you should see your projects in the top left of your screen. Click the current project to open the project select and click See all projects. This should open a Projects & Accounts modal.

.. image:: /images/platform/howto/see-all-projects.png

On the Projects & Accounts modal, click on Create account and you will be taken to a page where you provide a name, project(s) to link it to and the option to invite other admins.

.. image:: /images/platform/howto/console-aiven-account-create.png

Once created, you will see an overview of the account just created. A tab, called Authentication, will let you add a new method (in this case: SAML) and configure them.

.. image:: /images/platform/howto/authentication-methods.png

Clicking on Add Authentication Method creates a dialog where you can name your method, specify the type and a default team you would want members to join.

.. image:: /images/platform/howto/add-auth-method-google.png

Once you click Add, you will see the configuration URLs for your Identity Provider (do not worry about making a note of these, you can access them at any time).

.. image:: /images/platform/howto/configuration-urls.png

For now, we are done with the Aiven side of this, let's move on to G-suite and create our application.

Creating the G-Suite Application
--------------------------------

Go to the SAML apps management in G-Suite and create a new application with the "+" icon in the bottom right corner. Then click the "setup my own custom app" link at the bottom of the opened modal. You will get the following:

.. image:: /images/platform/howto/google-idp-information.png

Download the certificate and note the SSO URL and Entity ID somewhere, it will be needed later.
Click "Next" and set an application name, e.g. "Aiven". Click "Next" again to go to the application configuration. Fill in the form with the following data:

* ACS URL : This value is visible in Aiven Console on the newly created Authentication method page. The URL format is ``https://api.aiven.io/v1/sso/saml/account/{account_id}/method/{account_authentication_method_id}/acs`` 

* Entity ID : This value is visible in Aiven Console on the newly created Authentication method page. The URL format is ``https://api.aiven.io/v1/sso/saml/account/{account_id}/method/{account_authentication_method_id}/metadata`` 

Then click "Next" to set the Attribute Mapping. Add a new mapping with "application attribute" set to email , then chose "Basic information" for "category" and "Primary Email" for "user field". Finally click "Finish" then "OK" in the "Setting up SSO" modal.

You now need to turn on the application for your users. To do that, click "Edit Service", then in "Service Status" select "ON for everyone", then save. You will see a message saying that "Changes may take up to 24 hours to propagate to all users." Note that it truely can take a few hours before the G-Suite SSO with SAML can be used.

Setting up the G-Suite Application in Aiven
-------------------------------------------

Once the application is set up, you need to provide the application data to Aiven. Go back to Aiven Console and update the SAML configuration.

.. image:: /images/platform/howto/account-authentication-google.png

When this is done you can go to the Account link url to finalize linking your G-Suite account and Aiven profile. You can also invite other members of your team to login or signup to Aiven using G-Suite via the Signup link shown in the Authentication method page.