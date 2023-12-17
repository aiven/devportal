
Enable OAUTH2/OIDC authentication for Aiven for Apache Kafka®
===============================================================

OpenID Connect (OIDC) is an authentication protocol built on OAuth 2.0. Aiven for Apache Kafka supports the client credentials flow of OIDC/OAuth2, allowing clients to verify an user's identity using an authorization server's authentication. By activating this, you can use token-based authentication and integrate with identity providers. Setting the JSON Web Key Set (JWKS) JWKS endpoint via the Aiven console activates the OIDC mechanism for Kafka, which triggers a rolling restart of the Kafka brokers. This restart does not cause service downtime.

Prerequisites
-------------
Aiven for Apache Kafka integrates with a wide range of OpenID Connect identity providers (IdPs). However, the exact configuration steps can differ based on your chosen IdP. Refer to your Identity Provider's official documentation for specific configuration guidelines. 

Before proceeding with the setup, ensure you have:

* :doc:`Aiven for Apache Kafka® </docs/products/kafka/getting-started>` service running.
* **Access to an OIDC provider**: Options include Auth0, Okta, Google Identity Platform, Azure, or any other OIDC compliant provider.
* Required configuration details from your OIDC provider:
  
  - **JWKS Endpoint URL**: URL to retrieve the JSON Web Key Set (JWKS).
  - **Subject Claim Name**: Typically "sub"; however, this may vary with your OIDC provider.
  - **Issuer URL or Identifier**: Identifies and verifies the JWT issuer.
  - **Audience Identifier(s)**: Validates the JWT's intended recipients. For multiple audiences, make a note of all.




.. _console-authentication:

Enable OAuth2/OIDC via Aiven Console
-------------------------------------------------------

1. In `Aiven Console <https://console.aiven.io/>`_, select your project and then choose your Aiven for Apache Kafka® service.
2. On the **Overview** page, scroll down to **Advanced configuration** and select **Configure**.
3. In the **Advanced configuration** screen, select **Add configuration options**.
4. Set the following OIDC parameters:

   * ``kafka.sasl_oauthbearer_jwks_endpoint_url``

     * *Description*: Endpoint for retrieving the JSON Web Key Set (JWKS), which enables OIDC authentication. Corresponds to the Apache Kafka parameter ``sasl.oauthbearer.jwks.endpoint.url``.
     * *Value*: Enter the JWKS endpoint URL provided by your OIDC provider.

   * ``kafka.sasl_oauthbearer_sub_claim_name`` (Optional)

     * *Description*: Name of the JWT's subject claim for broker verification. This is optional and typically set to "sub". Corresponds to the Apache Kafka parameter ``sasl.oauthbearer.sub.claim.name``. 
     *  *Value*: Enter "sub" or the specific claim name provided by your OIDC provider if different.

   * ``kafka.sasl_oauthbearer_expected_issuer`` (Optional)

     *  *Description*: Specifies the JWT's issuer for the broker to verify. Corresponds to the Apache Kafka parameter ``sasl.oauthbearer.expected.issuer``. This setting is optional.
     * *Value*: Enter the issuer URL or identifier provided by your OIDC provider.

   * ``kafka.sasl_oauthbearer_expected_audience`` (Optional)

     * *Description*: Validates the intended JWT audience for the broker. Corresponds to the Apache Kafka parameter ``sasl.oauthbearer.expected.audience``. This is optional and is used if your OIDC provider specifies an audience.
     * *Value*: Input the audience identifier(s) given by your OIDC provider. If there are multiple audiences, separate them with commas.
   
   For more information on each corresponding Apache Kafka parameter, see `Apache Kafka documentation <https://kafka.apache.org/documentation/>`_ on configuration options starting with ``sasl.oauthbearer``.


   .. warning:: 

    Adjusting OIDC configurations, such as enabling, disabling, or modifying settings, can lead to a rolling restart of Kafka brokers. As a result, the brokers may temporarily operate with different configurations. To minimize any operational disruptions,  plan to implement these changes during a maintenance window or at a time that ensures a minimal impact on your operations.


5. Select **Save configurations** to save your changes



Enable OAuth2/OIDC via Aiven CLI
------------------------------------

To enable OAuth2/OIDC authentication for your Aiven for Apache Kafka service using :doc:`Aiven CLI </docs/tools/cli>`:

1. Get the name of the Aiven for Apache Kafka service you want to enable OAuth2/OIDC authentication with:

   .. code-block:: bash

      avn service list

   Make a note of the ``SERVICE_NAME`` corresponding to your Aiven for Apache Kafka service.

2. Enable OAuth2/OIDC authentication for your service:

   .. code-block:: bash

      avn service update <SERVICE_NAME> \
          -c kafka.sasl_oauthbearer_expected_audience="my-audience, another-audience" \
          -c kafka.sasl_oauthbearer_expected_issuer="https://my-issuer.example.com" \
          -c kafka.sasl_oauthbearer_jwks_endpoint_url="https://my-jwks-endpoint.example.com/jwks" \
          -c kafka.sasl_oauthbearer_sub_claim_name="custom-sub"

For detailed explanations on the OIDC parameters, refer to the :ref:`console-authentication` section above.



See also
--------
- Enable OAuth2/OIDC support for Apache Kafka® REST proxy 