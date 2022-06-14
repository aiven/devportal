Setting up SAML authentication with Azure
=========================================

You first need to create an Aiven account and an Aiven account authentication method. Account is a top level concept that can be associated with multiple different projects and with which you can make corporate level configuration like the authentication setup. You can do this in the `Aiven Console <https://console.aiven.io>`_.

Creating the Aiven account
--------------------------

Once you have logged into the Aiven Console, you should see your projects in the top left of your screen. Click the current project to open the project select and click "See all projects". This should open a "Projects & Accounts" modal.

.. image:: /images/platform/howto/see-all-projects.png
    :alt: View all projects in the Aiven Console

On the "Projects & Accounts" modal, click on "Create account" and you will be taken to a page where you provide a name, project(s) to link it to and the option to invite other admins.

.. image:: /images/platform/howto/console-aiven-account-create.png
    :alt: Create and configure a new account

Once created, you will see an overview of the account just created. A tab, called "Authentication", will let you add a new method (in this case: SAML) and configure them.

.. image:: /images/platform/howto/authentication-methods.png
    :alt: Adding an authentication method

Clicking on "Add Authentication Method" creates a dialog where you can name your method, specify the type and a default team you would want members to join.

.. image:: /images/platform/howto/add-authentication-method.png
    :alt: Configuring authentication methods

Once you click "Add", you will see the configuration URLs for your Identity Provider (do not worry about making a note of these, you can access them at any time).

.. image:: /images/platform/howto/configuration-urls.png
    :alt: Configuration references

For now, we are done with the Aiven side of this, let's move on to Azure and create our application.

Creating the Azure Application
------------------------------

When logged in Azure, go to "Enterprise applications" (either by using the tiles or the search bar), then use the left column navigation to go to "All applications" and click "New application".

.. image:: /images/platform/howto/new-application-azure.png
    :alt: Creating a new application in Azure

Then use the "Add from the gallery" search bar to search and use the "Azure AD SAML Toolkit". You can use anything you like for the App name, such as "Aiven SAML" and click the "Add" button.

.. image:: /images/platform/howto/azure-ad-saml-toolkit.png
    :alt: Adding the Azure AD SAML Toolkit for configuration

Use the navigation to go back the Enterprise applications list. The application might not be visible yet, and it's possible you have to select the "All applications" filter and apply it to be able to see it in the list. Once it's visible in the list, click it to go to its configuration.

Go to the "Single sign-on configuration" using the left column and select "SAML" when ask to select a single sign-on method.

You'll need to edit the "Basic SAML Configuration" settings with the following data:

* Identifier (Entity ID): replace the already configured value with ``https://api.aiven.io/v1/sso/saml/account/{account_id}/method/{account_authentication_method_id}/metadata`` 

* Reply URL (Assertion Consumer Service URL): add the following reply URL ``https://api.aiven.io/v1/sso/saml/account/{account_id}/method/{account_authentication_method_id}/acs`` 

* Sign on URL: set it to ``https://console.aiven.io`` 

Then click "Save" on top of the edition zone.

Next, edit the "Attributes & Claims" section, click "Add a new claim" and create an attribute like so:

.. image:: /images/platform/howto/manage-claim.png
    :alt: Creating a new claim

Finally, download the "Certificate (Base64)" from the SAML Signing Certificate section.

.. image:: /images/platform/howto/download-certificate-azure.png
    :alt: Downloading the Base64 certificate

Assigning users to the Azure application
----------------------------------------

For your users to be able to login using SAML, you need to assign to the Azure application you just created. To do that, use the left column navigation to go to "Users and groups" and click "Add user" on top of the list. You can then select the users that will be able to log in to Aiven with your Azure AD and click on the "Assign" button at the bottom of the page when you're done.

Setting up the Azure Application in Aiven
-----------------------------------------

Once the application is set up, you need to provide the application data to Aiven. This data can be found in the "Single sign-on" settings of the application on Azure. The data we're interrested in is in the "Set up Aiven SAML" section.

.. image:: /images/platform/howto/set-up-aiven-saml-azure.png
    :alt: Providing Azure application details

You can go back to Aiven Console and edit the "Authentication method" configuration.

When this is done you can go to Link Account url (shown in Aiven Console) to finalize linking your Azure account and Aiven profile. You can also invite other members of your team to login or signup to Aiven using Azure via the Signup link shown in the Authentication method page. 

.. Note:: Remember that team members will need to be assigned to the Aiven application in Azure for it to be possible.

Troubleshooting
---------------

**Contact your administrator**

If you get an error message saying contact your administrator, try the following:

Check the AzureAD user profile for the users and see if the "Contact Info" => "Email" field is populated or blank?

If it is blank, there are two possible solutions. 

1. Is the "Identity" => "User Principal Name" field an email address? And the primary email address that users will use to authenticate via Azure SSO? If so, try the solution below. If not, check case #2.

*Solution:* change the "User Attributes & Claims" to be ``email  = user.userprincipalname``. Try the login/registration flows again. If this works, you are done. Do not complete #2.

2. Do you know if all of you user accounts will have the "Contact Info" => "Alternate email" populated?

*Solution:* change the "User Attributes & Claims" to be ``email  = user.othermail``

**Capital letters in email addresses**

If the email addresses in your Azure AD contain capital letters you may receive the following error when trying to use Azure SAML authentication:::

    Error: Changing the email address for single sign-on signups is not allowed

This will be fixed in the future when email addresses are stored and compared case-insensitively in the Aiven platform.

In the meantime as a workaround you can modify the User Claims & Attributes section of the SAML-Based Sign On configured in Azure to transform the email address to lowercase.

In the instructions in the help article above this uses ``Source: Attribute`` and ``email = user.mail``. You should use whatever user attribute you have been using before (probably ``user.mail`` or ``user.userprincipalname``) but select the Transformation source and then use the ``ToLowercase`` transformation.