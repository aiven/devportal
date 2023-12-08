Enable OpenID Connect authentication on Aiven for OpenSearch® 
================================================================

OpenID Connect (OIDC) is an authentication protocol that builds on top of the OAuth 2.0 protocol. It provides a simple and secure way to verify the identity of a user and obtain basic profile information about them.

Prerequisites
---------------
* Aiven for OpenSearch® version 2 or later is required. If you are using an earlier version, upgrade to the latest version.
* OpenSearch Security management must be :doc:`enabled </docs/products/opensearch/howto/enable-opensearch-security>` on the Aiven for OpenSearch® service.
* An OpenID provider (IdP) that supports the OpenID Connect protocol.


Requirements to enable OpenID Connect
-----------------------------------------

To enable OpenID Connect authentication for Aiven for OpenSearch, you must configure OpenID Connect with an Identity Provider (IdP). Aiven for OpenSearch integrates with various OpenID Connect IdPs, and the exact steps to achieve this differ depending on your chosen IdP. Refer to your Identity Provider's official documentation for specific configuration steps.
To successfully set up OpenID Connect authentication, the following parameters from your IdP:

* **IdP URL**: The URL of your Identity Provider (IdP), which will be used to authenticate users.
* **Client ID**: Credentials your IdP provides when registering Aiven for OpenSearch as a client application. This credential is used to authenticate your Aiven for OpenSearch client application against the IdP and facilitate secure communication.
* **Client Secret**: Credentials your IdP provides when you register Aiven for OpenSearch as a client application.
* **Scope**: The scope of the authentication request specifies the permissions that you want to request from the Identity Provider (IdP). The available and required scopes may vary depending on the IdP you are using. Some common scopes include ``openid``, ``profile``, ``email``. 
* **Roles key and subject key**: Keys that help Aiven for OpenSearch Dashboards understand which part of the returned token contains role information and which part contains the user's identity or name.

.. note:: 
  The **Redirect URL** is automatically generated and available in the Aiven Console. This is the URL to which the Identity Provider (IdP) will redirect users after successful authentication. For more information on how to obtain this URL, see the next section.

Enable OpenID Connect authentication via Aiven Console
--------------------------------------------------------

1. In the `Aiven Console <https://console.aiven.io/>`_, access your Aiven for OpenSearch service where you want to enable OpenID Connect.
2. Select **Users** from the left sidebar.
3. In the **SSO authentication** section, use the **Add method** drop-down and select **OpenID**.
4. On **Configure OpenID Connect authentication** screen, 
   
   * **Redirect URL**: This URL is auto-populated. It is the URL that users will be redirected to after they have successfully authenticated through the IdP.
   * **IdP URL**: Enter the URL of your OpenID Connect Identity Provider. This is the URL that Aiven will use to redirect users to your IdP for authentication.
   * **Client ID**: Enter the ID you obtained during your IdP registration. This ID is used to authenticate your Aiven application with your IdP.
   * **Client Secret**: Enter the secret associated with the Client ID. This secret is used to encrypt communications between your Aiven application and your IdP.
   * **Scope**: The scope of the claims. This is the set of permissions that you are requesting from your IdP. For example, you can request the ``openid``, ``profile``, and ``email`` scopes to get the user's identity, profile information, and email address.
   * **Roles key**: The key in the returned JSON that stores the user's roles. This key is used by Aiven to determine the user's permissions.
   * **Subject key**: This refers to the specific key within the returned JSON that holds the user's name or identifying subject. Aiven uses this key to recognize and authenticate the user. By default, this key is labeled as ``Subject``.

5. **Enable advanced configuration** (Optional) to further fine-tune the authentication process. Aiven for OpenSearch provides the following advanced configuration options:
   
   * **Token handling**: Choose your preferred method for handling the authentication token.
    
     * **HTTP Header**: The authentication token is passed in an HTTP header. 
        
       * **Header name**: Enter the specific name of the HTTP header that will contain the authentication token. The default header name is Authorization.
     * **URL parameter**: The authentication token is passed as a URL parameter. You can specify the parameter name.
   
       * **Parameter name**: Enter the specific URL parameter that will carry the authentication token.

   * **Refresh limit count**: Maximum number of unrecognized JWT key IDs allowed within 10 seconds. Enter the value for the Refresh Limit Count parameter. The default value is 10.
   * **Refresh limit window (ms)**: This is the interval, measured in milliseconds, during which the system will verify unrecognized JWT key IDs. Enter the value for the Refresh Limit Window parameter. The default value is 10,000 (10 seconds).

6. Select **Enable**  to complete the setup and activate the configuration.


Additional resources
---------------------

* `OpenSearch OpenID Connect documentation <https://opensearch.org/docs/latest/security/authentication-backends/openid-connect/>`_