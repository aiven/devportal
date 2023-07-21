Set up SAML authentication
===========================

Security Assertion Markup Language (SAML) is a standard for
exchanging authentication and authorization data between an identity
provider (IdP) and a service provider. You can set up SAML authentication in Aiven with your company's favorite authentication
service.

To set up a SAML authentication method for your organization in Aiven, there are three steps:

1. Configure the SAML authentication method in the Aiven Console
2. Configure SAML on your IdP
3. Enable the SAML authentication method in the Aiven Console
4. Log in with the SAML authentication method

Setup instructions for specific providers are available on the following pages:

* :doc:`Set up SAML with Auth0 </docs/platform/howto/saml/setup-saml-auth0>`
* :doc:`Set up SAML with FusionAuth </docs/platform/howto/saml/setup-saml-fusionauth>`
* :doc:`Set up SAML with Microsoft Azure Active Directory </docs/platform/howto/saml/setup-saml-azure>`
* :doc:`Set up SAML with Okta </docs/platform/howto/saml/setup-saml-okta>`
* :doc:`Set up SAML with OneLogin </docs/platform/howto/saml/setup-saml-onelogin>`
* :doc:`Set up SAML with Google </docs/platform/howto/saml/setup-saml-google>`

If your provider isn't listed, contact us at support@Aiven.io so we can assist you with the configuration.

Step 1. Set up the SAML authentication method in Aiven Console
----------------------------------------------------------------

SAML Authentication methods are configured at the organization level:

#. In the organization, click **Admin**.

#. Select **Authentication**.

#. Click on **Add authentication method**.

#. Enter a name and select SAML. You can also select the teams that users will be added to when they sign up or log in through this authentication method.

You are shown the two parameters needed for the SAML authentication setup in your Identity Provider:

* Metadata URL
* ACS URL

Step 2. Configure SAML on your Identity Provider
------------------------------------------------

In your IdP, use the metadata URL and ACS URL to configure a new application. The following table shows how the configuration information provided by Aiven is referred to in some of the more popular IdPs.

.. list-table::
  :header-rows: 1
  :align: left

  * - Aiven
    - Auth0
    - Okta
    - OneLogin
    - Azure Active Directory
    - Centrify
  * - ACS URL
    - Application Callback URL
    - SSO URL
    - Recipient
    - Reply
    - -
  * - Metadata
    - -
    - Audience
    - Audience URI
    - Identifier
    - SP Entity
  * - Email Mapping
    - ``email``
    - ``user.email``
    - ``Email``
    - ``user.mail``
    - ``LoginUser.email``


Step 3. Finish the configuration in Aiven 
------------------------------------------

Go back to the **Authentication** page in the `Aiven Console <https://console.aiven.io/>`_ to enable the SAML authentication method:

#. Select the name of the authentication method that you created.

#. Toggle on **Enable Authentication method**. To let users initiate a login directly from your IdP, toggle on **IdP login**. 

#. In the **SAML configuration** section, click **Edit**.

#. Enter the **IDP URL**, **Entity Id**, and **SAML Certificate** details.

#. Click **Edit method**. 


Step 4. Log in with the SAML authentication method
--------------------------------------------------

After the authentication method is enabled, there are two URLs in the **Signup and link accounts URLs** section:

* **Signup URL**: For users that don't have an Aiven user account to create a new Aiven user linked to the configured IdP.
* **Account link URL**: For users that already have an Aiven user account to link their existing Aiven user with the configured IdP.

Send the appropriate URL to link the authentication method to a new or existing Aiven user. 

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
