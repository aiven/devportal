Add identity providers 
=======================

You can give your organization users access to Aiven through an identity provider (IdP). 

To set up single sign-on through an IdP for your organization:

1. Add the identity provider in the `Aiven Console <https://console.aiven.io/>`_ .
2. Configure SAML on your IdP.
3. Finalize the setup in the Aiven Console using information from your IdP.
4. Link your users to the identity provider.


Step 1. Add the IdP in the Aiven Console
-----------------------------------------

#. In the organization, click **Admin**.

#. Click **Identity providers**.

#. Click **Add identity provider**.

#. Select an IdP and enter a name.

#. On the **Configuration** step are two parameters that you need to set up the SAML authentication in your IdP:

* Metadata URL
* ACS URL


Step 2. Configure SAML on your IdP
-----------------------------------

Use the metadata URL and ACS URL from the Aiven Console to configure a new application in your IdP. Setup instructions are available for these specific providers:

* :doc:`Auth0 </docs/platform/howto/saml/add-auth0-idp>`
* :doc:`FusionAuth </docs/platform/howto/saml/add-fusionauth-idp>`
* :doc:`Microsoft Azure Active Directory </docs/platform/howto/saml/add-azure-idp>`
* :doc:`Okta </docs/platform/howto/saml/add-okta-idp>`
* :doc:`OneLogin </docs/platform/howto/saml/add-onelogin-idp>`
* :doc:`Google </docs/platform/howto/saml/add-google-idp>`

If your provider isn't listed, contact the support team at support@Aiven.io for help with the configuration.


Step 3. Finish the configuration in Aiven 
------------------------------------------

Go back to the Aiven Console to complete setting up the IdP: 

#. Enter the **IDP URL**, **Entity Id**, and **SAML Certificate** details.

#. Click **Next**. 

#. Configure the security options for this IdP:
   
   * Require authentication context: This lets the IdP enforce stricter security measures to help prevent unauthorized access, such as requiring multi-factor authentication.
   
   * Require assertion to be signed: The IdP will check for a digital signature. This security measure ensures the integrity and authenticity of the assertions by verifying that they were issued by a trusted party and have not been tampered with. 
   
   * Sign authorization request sent to IdP: A digital signature is added to the request to verify its authenticity and integrity.

#. Click **Next** and complete the setup.


Step 4. Link your users to the identity provider
--------------------------------------------------

Your organization users should automatically be able to use the identity provider to sign up and log in to Aiven. You can also handle this manually using URLs:

#. On the **Identity providers** page, click the name of the IdP.

#. In the **Overview** section there are two URLs:

   * **Signup URL**: Users that don't have an Aiven user account can use this to create a new Aiven user linked to this IdP.

   * **User account link URL**: Users that already have an Aiven user account can link their existing Aiven user with this IdP.

#. Send the appropriate URL to your organization users. If you set up a different IdP before and are now switching to a new IdP, existing users need to log in with the new account link URL to finish the setup.

When a user clicks on the link, they will be redirected to a page to link their Aiven user account with the IdP:

* For existing users that are already logged into the Aiven Console

  #. Click on the **Link profile** button. You are redirected to your IdP's authentication page.
  #. Once logged in to the provider, you will be redirected back to the Aiven Console and the IdP is linked to your profile. You can use the IdP for all future logins.

* For existing users that are not logged into the Aiven Console

  #. Click on the **Login** button.  
  #. On the login page of the Aiven Console, log in as usual. You are redirected to your IdP's authentication page.
  #. Once logged in to the provider, you are redirected back to the Aiven Consoleand the IdP is linked to your profile. You can use the IdP for all future logins.

* For new users without an Aiven user account

  #. Click **Sign up**. You are redirected to your IdP's authentication page.
  #. Once logged in to the provider, you are redirected back to the Aiven sign up page.
  #. Complete the sign up process. The IdP is linked to your profile and you can use it for all future logins.
