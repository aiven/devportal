SAML authentication on Aiven for OpenSearch® 
====================================================

SAML (Security Assertion Markup Language) is a standard protocol for exchanging authentication and authorization data between an identity provider (IdP) and a Service Provider (SP). SAML enables users to authenticate themselves to a service provider with credentials from a trusted third-party identity provider without the need to create and manage separate user accounts for each service provider.

SAML authentication on Aiven for OpenSearch® can enhance the authentication process for users, providing increased security and a more streamlined experience. With SAML, OpenSearch can delegate authentication and authorization to a trusted external identity provider, reducing security risks and simplifying user management. Additionally, SAML allows for Single Sign-On (SSO) functionality, enabling users to access several OpenSearch instances without the need to log in multiple times.


Prerequisites
---------------
* Aiven for OpenSearch® version 2.4 or later is required. If you are using an earlier version, upgrade to the latest version.
* OpenSearch Security management must be enabled on the Aiven for OpenSearch® service.
* You will need a SAML identity provider (IdP), the Metadata URL, and IdP entity ID.


Configre SAML on IdP
--------------------

Enabling SAML SSO Authentication for Aiven for OpenSearch requires the configuration of SAML with an Identity Provider (IdP). Since Aiven for OpenSearch supports multiple IdPs, the steps for configuring SAML with your IdP may differ depending on the IdP you are using. It is recommended to refer to your IdP's documentation for detailed instructions on configuring SAML applications.

To enable SAML SSO authentication, make sure you have correctly configured your IdP and have the following two critical parameters:

* **IdP Metadata URL**: The IdP metadata URL provides essential metadata about your IdP, including the certificate used for signing the SAML response.
* **IdP Entity ID** : The IdP Entity ID is the identifier that the IdP uses to recognize itself. To establish trust between Aiven and OpenSearch, Aiven uses the Entity ID value for OpenSearch.



Enable SAML SSo authentication via Aiven Console
--------------------------------------------------
To enable SAML authentication for your Aiven for OpenSearch service, follow these steps: 

1. On your Aiven for OpenSearch service, navigate to the **Users** tab.
2. In the **SAML SSO Authentication** section, select **Enable SAML**. 
3. On the **Configure SAML Authentication** screen, enter the following details: 
   
   * **SSO URL**: This is a distinct URL assigned to each Aiven for OpenSearch service and serves as the destination where the Identity Provider (IdP) sends SAML responses after a user has been authenticated successfully. It is a fixed URL that cannot be modified.
   * **IdP Metadata URL**: Enter the URL of your SAML Identity Provider's (IdP) metadata that Aiven will use to authenticate users.
   * **IdP Entity ID**: Enter the unique identifier assigned to your Identity Provider (IdP). This identifier assists Aiven in distinguishing between various IdPs.
   * **SP Entity ID**: E Enter the unique identifier the IdP uses to recognize and authenticate Aiven for OpenSearch as the service provider.
   * **SAML roles key**: This is an optional field that allows you to map SAML roles to Aiven for OpenSearch roles.
   * **SAML subject key**: This is also an optional field that allows you to map SAML subject to Aiven for OpenSearch users.

4. Select **Enable**.
5. In the SAML SSO Authentication section, you can see the SAML method configured with the status set to **Enabled**. 


