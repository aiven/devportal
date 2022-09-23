Enable SAML authentication
==========================

SAML (Security Assertion Markup Language) is a standard for
exchanging authentication and authorization data between an identity
provider and a service provider. You can operate it with Aiven so that you
and your collaborators can use your company's favorite authentication
service.

To set up a SAML authentication method with your organization's account in Aiven, there are three steps:

1. Configure the SAML authentication method in the Aiven Console
2. Configure SAML on your Identity Provider (IdP)
3. Enable the SAML authentication method in the Aiven Console
4. Log in with the SAML authentication method


Step 1. Set up the SAML authentication method in the Aiven Console
-------------------------------------------------------------------

SAML Authentication methods are configured at the account level. To configure a new one:

#. In the **Account**, click **Admin**.

#. Select **Authentication** and click on **Add authentication method**.

#. Enter a name and select SAML. You can also select the teams that users will be added to when they sign up or log in through this authentication method.

You are shown the two parameter needed for the SAML authentication setup in your Identity Provider:

* Metadata URL
* ACS URL

Step 2. Configure SAML on your Identity Provider
------------------------------------------------

In your Identity Provider (IdP), use the metadata URL and ACS URL to configure a new application. The table shows how the configuration information provided by Aiven is referred to in the more popular IdPs.

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

Step 3. Enable the SAML authentication method in the Aiven Console
-------------------------------------------------------------------

After creating the application in your IdP, go back to the Authentication page in the Aiven Console to enable the SAML authentication method:

#. Select your authentication method's name.

#. On the page that opens, toggle on **Enable Authentication method**. You can also enable **IdP login**, allowing your users to initiate a login directly from your IdP.

#. In the **SAML config** section, click **Edit**.

#. Enter the **IDP URL**, **Entity Id**, and **SAML Certificate** details.

#. Click **Edit method**. 

..
  Delete these links - waiting on confirmation from Lorna this is fine to do. 

  Detailed instructions exist for the following providers:

  * `Okta <https://help.aiven.io/en/articles/3438800-setting-up-saml-authentication-with-okta>`_
  * `G-Suite <https://help.aiven.io/en/articles/3447699-setting-up-saml-authentication-with-google-g-suite>`_
  * `Azure AD <https://help.aiven.io/en/articles/3557077-setting-up-saml-authentication-with-azure>`_
  * `Auth0 <https://help.aiven.io/en/articles/3808083-setting-up-saml-with-auth0>`_
  * `Centrify <https://help.aiven.io/en/articles/4485814-setting-up-saml-with-centrify>`_


  If your provider isn't in the list, please contact us at
  support@Aiven.io so we can assist you with the configuration of the
  provider of your choice.

Step 4. Log in with the SAML authentication method
--------------------------------------------------

After the authentication method is enabled, there are 2 URLs in the **Signup and link accounts URLs** section:

* Signup URL: For users that don't have an Aiven account to create a new Aiven user linked to the configured IdP.
* Account link URL: For users that already have an Aiven user account to link their existing Aiven user with the configured IdP.

Send the appropriate URL to link the authentication method to a new or existing Aiven user. 

When a user clicks on the link, they will be redirected to a page to link their Aiven account with the SAML account:

* For existing users that are already logged into the Aiven Console

  #. Click on the **Link profile** button. You are redirected to your SAML provider's authentication page.
  #. Once logged in to the provider, you will be redirected back to the Aiven Console. The authentication method is linked to your profile.

* For existing users that are not logged into the Aiven Console

  #. Click on the **Login** button.  
  #. On he login page of the Aiven Console, log in as usual. You are redirected to your SAML provider's authentication page.
  #. Once logged in to the provider, you are redirected back to the Aiven Console. The authentication method is linked to your profile.

* For new users without an Aiven user account

  #. Click **Sign up**. You are redirected to your SAML provider's authentication page.
  #. Once logged in to the provider, you are redirected back to the Aiven sign up page.
  #. Complete the sign up process. Your Aiven profile is linked with your SAML authentication method.