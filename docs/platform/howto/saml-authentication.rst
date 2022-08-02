SAML authentication
===================

SAML ( *Security Assertion Markup Language* ) is a standard for
exchanging authentication and authorization data between an identity
provider and a service provider. You can use it with Aiven so that you
and your collaborator can use your company’s favorite authentication
service.

Setting up the SAML authentication method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SAML Authentication methods are configured at the *Account* level. To configure a new one, click the *downward facing arrow* next to your current project in the top-left of the Aiven Console.

In the popup that appears, select *See all projects and accounts*, from here you can create a new *Account* or select the existing one you would like to use.

In the *Account* page, select the *Authentication* tab and click the red button to *Add a new authentication method*.

Choose a name for your method and, if relevant, select the *Team* that you would like invited members to join automatically when they sign up or log in through this method.

You will be given the following:

1. Metadata URL
2. ACS URL

Configuring your Identity Provider (IdP)
----------------------------------------

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
    - `email`
    - `user.email`
    - `Email`
    - `user.mail`
    - `LoginUser.email`

Once you have created the application in your Identity Provider, select your authentication method in the Aiven console and click *Edit* next to *SAML configuration*

Here you need to input the URL of your Identity Provider, the Entity ID and the certificate details. You can also toggle *Enable IdP login* here; this allows your users to initiate a login directly from your Identity Provider.

Once you have completed this, you can save and *Enable authentication method*. Once active, you will see 2 URLs:

1. Signup URL:
    For new users without an Aiven user account to create a new Aiven user linked to the configured Identity Provider.
2. Account link URL:
     For existing users with an Aiven user account to link their Aiven user with the configured Identity Provider.

Detailed instructions exist for the following providers:

-  `Okta <https://help.aiven.io/en/articles/3438800-setting-up-saml-authentication-with-okta>`_

-  `G-Suite <https://help.aiven.io/en/articles/3447699-setting-up-saml-authentication-with-google-g-suite>`_

-  `Azure AD <https://help.aiven.io/en/articles/3557077-setting-up-saml-authentication-with-azure>`_

-  `Auth0 <https://help.aiven.io/en/articles/3808083-setting-up-saml-with-auth0>`_

- `Centrify <https://help.aiven.io/en/articles/4485814-setting-up-saml-with-centrify>`_
  

If your provider isn't in the list, please contact us at
support@Aiven.io so we can assist you with the configuration of the
provider of your choice.

Logging in with a SAML authentication method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The first step is to link the authentication method to your existing
  Aiven user, if you have one, or create a new Aiven profile
  associated with it. To do that, you first need to get an invite link
  from your Account manager. Once you get the invite link, click on it
  and you should land on the following page:

.. image:: 3376377-saml-authentication_image1.png

You have an Aiven profile and are logged in to the Aiven Console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Click on the “Link profile” button. You will be redirected to your
  SAML provider’s authentication page. Once you’ve logged in to the
  provider, you will be redirected back to the Aiven Console, and the
  authentication method will be linked to your profile.

You have an Aiven profile and are logged out
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Click on the “Login” button. You will be sent to the login page of the
  Aiven Console, where you can log in as usual, using your password, your configured SAML provider or
  Google OAuth. After you’re logged in to the Aiven Console, you will be
  redirected to your SAML provider’s authentication page. Once you’ve
  logged in to the provider, you will be redirected back to the Aiven
  Console, and the authentication method will be linked to your profile.

You don’t have an Aiven profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Click on the “Sign up” button. You will be redirected to your SAML
  provider’s authentication page. Once you’ve logged in to the provider,
  you will be redirected back to the Aiven sign page where you can
  finish the sign up process. Once this is done, you will have your
  Aiven profile created and associated with your SAML authentication
  method.
