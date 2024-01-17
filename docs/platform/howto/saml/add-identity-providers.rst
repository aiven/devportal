Add identity providers 
=======================

You can give your organization users access to Aiven through an identity provider (IdP). 

To set up single sign-on through an IdP for your organization:

1. Add the identity provider in the Aiven Console.
2. Configure SAML on your IdP.
3. Finalize the setup in the Aiven Console using information from your IdP.

????????
4. Link  Log in with the SAML authentication method
?????????


Step 1. Add the IdP in the Aiven Console
-----------------------------------------

#. In the organization, click **Admin**.

#. Select **Identity providers**.

#. Click on **Add identity provider**.

#. Select an IdP and enter a name.

#. On the **Configuration** step, you are shown two parameters needed for the SAML authentication setup in your IdP:

* Metadata URL
* ACS URL


Step 2. Configure SAML on your IdP
-----------------------------------

In your IdP, use the metadata URL and ACS URL from the Aiven Console to configure a new application. Setup instructions are available for these specific providers:

* :doc:`Auth0 </docs/platform/howto/saml/setup-saml-auth0>`
* :doc:`FusionAuth </docs/platform/howto/saml/setup-saml-fusionauth>`
* :doc:`Microsoft Azure Active Directory </docs/platform/howto/saml/setup-saml-azure>`
* :doc:`Okta </docs/platform/howto/saml/setup-saml-okta>`
* :doc:`OneLogin </docs/platform/howto/saml/setup-saml-onelogin>`
* :doc:`Google </docs/platform/howto/saml/setup-saml-google>`

If your provider isn't listed, contact the support team at support@Aiven.io for help with the configuration.


Step 3. Finish the configuration in Aiven 
------------------------------------------

Go back to the **Authentication** page in the `Aiven Console <https://console.aiven.io/>`_ to enable the SAML authentication method:

#. Select the name of the authentication method that you created.

#. Toggle on **Enable Authentication method**. To let users initiate a login directly from your IdP, toggle on **IdP login**. 

#. In the **SAML configuration** section, click **Edit**.

#. Enter the **IDP URL**, **Entity Id**, and **SAML Certificate** details.

#. Click **Edit method**. 


Step 4. Log in with the identity provider
--------------------------------------------------

After the authentication method is enabled, there are two URLs in the **Signup and link accounts URLs** section:

* **Signup URL**: For users that don't have an Aiven user account to create a new Aiven user linked to the configured IdP.
* **Account link URL**: For users that already have an Aiven user account to link their existing Aiven user with the configured IdP.

Send the appropriate URL to link the authentication method to a new or existing Aiven user. If you set up a SAML authentication method before and are now switching to a new IdP, existing users need to log in with the new account link URL to finish the setup.

When a user clicks on the link, they will be redirected to a page to link their Aiven user account with the SAML account:

* For existing users that are already logged into the Aiven Console

  #. Click on the **Link profile** button. You are redirected to your SAML provider's authentication page.
  #. Once logged in to the provider, you will be redirected back to the Aiven Console. The authentication method is linked to your profile.

* For existing users that are not logged into the Aiven Console

  #. Click on the **Login** button.  
  #. On the login page of the Aiven Console, log in as usual. You are redirected to your SAML provider's authentication page.
  #. Once logged in to the provider, you are redirected back to the Aiven Console. The authentication method is linked to your profile.

* For new users without an Aiven user account

  #. Click **Sign up**. You are redirected to your SAML provider's authentication page.
  #. Once logged in to the provider, you are redirected back to the Aiven sign up page.
  #. Complete the sign up process. Your Aiven profile is linked with your SAML authentication method.
