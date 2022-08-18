Enable SAML authentication
==========================

SAML ( *Security Assertion Markup Language* ) is a standard for
exchanging authentication and authorization data between an identity
provider and a service provider. You can operate it with Aiven so that you
and your collaborators can use your company's favorite authentication
service.

Set up the SAML authentication method in the Aiven Console
----------------------------------------------------------

SAML Authentication methods are configured at the *Account* level. To configure a new one:

* Click the **downward facing arrow** next to your current project in the top-left of the Aiven Console.

* In the popup that appears, select **See all projects and accounts**

* Create a new **Account** or select the existing one for which you would like to setup SAML authentication.

* In the *Account* page, select the **Authentication** tab and click on **Add authentication method**.

* Choose a name for your method and, if relevant, select the **Team** that invited members will join automatically once signed up or logged in through this new authentication method.

* You will be shown the following two parameter needed for the SAML authentication setup in your Identity Provider:

  1. Metadata URL
  2. ACS URL


Configure SAML on your Identity Provider (IdP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Navigate to your Identity Provider and configure a new application. The table below shows how the configuration information provided by Aiven is referred to in the more popular Identity Providers.

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

Enable the SAML authentication method in the Aiven Console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once created the application in your Identity Provider, select your authentication method in the Aiven console and click **Edit** next to *SAML configuration*.

In the Edit page, you need to input:

* the URL of your Identity Provider
* the Entity ID
* the certificate details

  .. Tip::

    You can also toggle **Enable IdP login** allowing your users to initiate a login directly from your Identity Provider.

* Save and click on **Enable authentication method**. Once active, you will see 2 URLs:

  1. *Signup URL*: for **new users without an Aiven user account** to create a new Aiven user linked to the configured Identity Provider.
  2. *Account link URL*: **for existing users with an Aiven user account** to link their Aiven user with the configured Identity Provider.

Detailed instructions exist for the following providers:

* `Okta <https://help.aiven.io/en/articles/3438800-setting-up-saml-authentication-with-okta>`_
* `G-Suite <https://help.aiven.io/en/articles/3447699-setting-up-saml-authentication-with-google-g-suite>`_
* `Azure AD <https://help.aiven.io/en/articles/3557077-setting-up-saml-authentication-with-azure>`_
* `Auth0 <https://help.aiven.io/en/articles/3808083-setting-up-saml-with-auth0>`_
* `Centrify <https://help.aiven.io/en/articles/4485814-setting-up-saml-with-centrify>`_


If your provider isn't in the list, please contact us at
support@Aiven.io so we can assist you with the configuration of the
provider of your choice.

Log in with a SAML authentication method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first step is to link the authentication method to your existing Aiven user, if you have one, or create a new Aiven profile associated with it. You'll first need to get an invite link from your Account manager. Once you get the invite link, click on it and you will be taken to a page to manage your Aiven account with your SAML account.

If you already have an Aiven profile and are already logged in the Aiven Console:

* Click on the **Link profile** button.
* You will be redirected to your SAML provider's authentication page.
* Once you've logged in to the provider, you will be redirected back to the Aiven Console, and the authentication method will be linked to your profile.

If you already have an Aiven profile and are not logged in the Aiven Console:

* Click on the **Login** button.
* You will be sent to the login page of the Aiven Console, where you can log in as usual, using your password, your configured SAML provider or Google OAuth.
* After you're logged in to the Aiven Console, you will be redirected to your SAML provider's authentication page.
* Once you've logged in to the provider, you will be redirected back to the Aiven Console, and the authentication method will be linked to your profile.

If you don't have an Aiven profile:

* Click on the **Sign up** button.
* You will be redirected to your SAML provider's authentication page.
* Once you've logged in to the provider, you will be redirected back to the Aiven sign page where you can finish the sign up process.
* Once done, you will have your Aiven profile created and associated with your SAML authentication method.
