Setting up SAML authentication with Okta
========================================

You first need to create an Aiven account and an Aiven account authentication method. Account is a top level concept that can be associated with multiple different projects and with which you can make corporate level configuration like the authentication setup. You can do this in the `Aiven Console <https://console.aiven.io>`_.

Creating the Aiven account
--------------------------

Once you have logged into the Aiven Console, you should see your projects in the top left of your screen. Click the current project to open the project select and click See all projects. This should open a Projects & Accounts modal.

.. image:: /images/platform/howto/see-all-projects.png
    :alt: View all projects in the Aiven Console

On the Projects & Accounts modal, click on Create account and you will be taken to a page where you provide a name, project(s) to link it to and the option to invite other admins.

.. image:: /images/platform/howto/console-aiven-account-create.png
    :alt: Create and configure a new account

Once created, you will see an overview of the account just created. A tab, called Authentication, will let you add a new method (in this case: SAML) and configure them.

.. image:: /images/platform/howto/authentication-methods.png
    :alt: Adding an authentication method

Clicking on Add Authentication Method creates a dialog where you can name your method, specify the type and a default team you would want members to join.

.. image:: /images/platform/howto/add-auth-method-okta.png
    :alt: Adding Okta as the auth method

Once you click Add, you will see the configuration URLs for your Identity Provider (do not worry about making a note of these, you can access them at any time).

.. image:: /images/platform/howto/configuration-urls.png
    :alt: Configuring references

For now, we are done with the Aiven side of this, let's move on to Okta and create our application.

Creating the Okta Application
-----------------------------

This is a two step process. We will first create the SAML SP-Initiated authentication flow, then create a bookmark app that will redirect to the Aiven console's login page.

Creating the SP-Initiated Authentication Application
----------------------------------------------------

Login to the "Admin" portal and navigate to the "Applications" tab. Click on the "Add Application" button, then "Create New App".

Select "SAML 2.0" for the "Sign on method", then click "Next".

In the following form, you can give the app a name (e.g. "Aiven SAML"), logo and set it's visibility for your Okta users. Once this is done, click "Next".

.. image:: /images/platform/howto/admin-okta-admin-apps-saml-wizard.png
    :alt: Configure SAML Okta

Then comes the SAML configuration form. The following fields need to be set:

* Single sign on URL: This value is visible in Aiven Console on the newly created Authentication method page. The URL format is ``https://api.aiven.io/v1/sso/saml/account/{account_id}/method/{account_authentication_method_id}/acs`` 

* Audience URI (SP Entity ID): This value is visible in Aiven Console on the newly created Authentication method page. The URL format is ``https://api.aiven.io/v1/sso/saml/account/{account_id}/method/{account_authentication_method_id}/metadata`` 

* Default RelayState: This is the homepage of the Aiven Console and is important for IdP initiated sign-on to function correctly.
    
    * https://console.aiven.io/ - Aiven Console
    
    * https://console.gcp.aiven.io/ - GCP Marketplace Console

    * https://console.aws.aiven.io/ - AWS Marketplace Console

* "Attribute statements" should have an entry where "name" is email  and "value" user.email


Once this is done, click "Next" then "Finish". You will be redirected to your application in Okta.

Setting up the Okta Application in Aiven
----------------------------------------

Once the application is created, you need to provide the application data to Aiven. This data can be found in the "Sign On" tab of the application on Okta, after clicking the "View Setup Instructions".

.. image:: /images/platform/howto/okta-admin-app.png
    :alt: Proving Okta app details to Aiven

This will open a new tab where you will get the required information to finalize the setup to use Okta with Aiven. From this page, download the certificate file.

You can then go back to Aiven Console and finalize the configuration in the Authentication method page.

.. image:: /images/platform/howto/account-authentication-okta.png
    :alt: Finalizing auth configuration in the Aiven Console

Toggle "Enable IdP login" before clicking "Edit Method" to save the settings.

.. image:: /images/platform/howto/aiven-edit-okta-idp.png
    :alt: Editing Okta IdP

When this is done use the "Account Link URL" on the authentication config page to link your Okta account and Aiven profile. You can also invite other members of your team to login or signup to Aiven using Okta via the Signup link shown in the Authentication method page. Note: Remember that they will need to be assigned to the Aiven application in Okta for it to be possible.

Assigning users to the Okta application
---------------------------------------

For your users to be able to login using SAML, you need to assign them to the Okta application you just created. To do that, click on the Assign Users to App button and assign individual users or groups to the application.

.. image:: /images/platform/howto/okta-assign-applications.png
    :alt: Assigning users to Okta application

Troubleshooting
---------------

**Authentication failed**

When launching the Aiven SAML application and receiving an "Authentication failed" error: check that IdP is enabled in the Okta authentication in the Aiven Console.

.. image:: /images/platform/howto/idp-enabled.png
    :alt: Checking IdP status for Okta

**Invalid ``RelayState``**

If you get this error, it means that you are attempting an IdP-initiated auth flow, i.e. you clicked the Aiven SAML app from the Okta UI. Previously, Aiven did not support IdP-initiated flows, but now it is possible if you set the Default ``RelayState`` in Okta to: 

* https://console.aiven.io/ - Aiven Console

* https://console.gcp.aiven.io/ - GCP Marketplace Console

* https://console.aws.aiven.io/ - AWS Marketplace Console

**My Okta password does not work**

Make sure that you use the "Account Link URL" to add the Okta Authentication method to your Aiven profile. Once linked, you should get the choice of multiple sign-in methods as well as see the other Authentication methods in you user profile.