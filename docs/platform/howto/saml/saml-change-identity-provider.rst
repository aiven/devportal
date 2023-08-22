Change identity providers 
==========================

To change the identity provider (IdP) for your SAML authentication, you first need to set up the new IdP. Then you can link your organization's users to the new IdP with the signup or account link URL.

To change to a new IdP:

#. :doc:`Follow the instructions </docs/platform/howto/saml/saml-authentication>` for setting up the SAML authentication method in Aiven, configuring it on your IdP, and enabling it in Aiven.

#. In the Aiven Console, click **Admin**.

#. Click **Authentication** and select the name of the authentication method that you created.

#. In the **Signup and link accounts URLs** section, copy the appropriate link and send it to your users to switch them to the new IdP:
  
* **Signup URL**: For users that don't have an Aiven user account and need to create a new Aiven user linked to this IdP.
* **Account link URL**: For users that already have an Aiven user account to link their existing Aiven user with the configured IdP. 

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
