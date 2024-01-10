Enable OAuth2/OIDC support for Apache Kafka® REST proxy
========================================================

Secure your Apache Kafka® resources by integrating OAuth 2.0/OpenID Connect (OIDC) with the Karapace REST proxy and enabling REST proxy authorization. This setup ensures that only authorized individuals can manage Apache Kafka resources through both token-based authentication and access control rules.

OAuth2/OIDC token handling
---------------------------

Karapace processes the JSON Web Token (JWT) obtained from the Authorization HTTP header, specifically when employing the Bearer authentication scheme. This allows OAuth2/OIDC credentials to be supplied directly to the REST proxy, which uses the provided token to authorize requests to Apache Kafka. When a Bearer token is presented, Kafka clients configured by Karapace use the SASL OAUTHBEARER mechanism to send the JWT for validation.


Authorization enforcement
----------------------------

In the underlying Aiven for Apache Kafka® service, the default mechanism for authorization, uses the ``sub`` claim from the JWT as the username. This username is then verified against the configured Access Control Lists (ACLs) to authorize user operations on Kafka resources.

While the ``sub`` claim is the default identifier, this setting is configurable. You can specify a different JWT claim for authentication by adjusting the ``kafka.sasl_oauthbearer_sub_claim_name`` parameter. For more information on configuring this, see :ref:`console-authentication`.

To authenticate and authorize a user in Aiven for Apache Kafka, both a service user and an ACL entry describing the permissions are required. The JWT claim value used for authentication must explicitly match the service user in the system. Furthermore, this service user must be associated with an ACL entry that outlines their permissions, ensuring that the identity of the user making the request aligns with both the service user and the ACL entry.



Managing token expiry
------------------------------

With OAuth2/OIDC enabled, Karapace manages Kafka client connections for security and performance. It automatically cleans up idle clients and those with tokens nearing expiration, typically on a 5-minute cycle. This cleanup prevents unauthorized access with expired tokens and clears idle connections.

.. note:: 
    Before your token expires, remove any linked consumers and producers to avoid security issues and service interruptions. After removal, refresh your OAuth2 JWT tokens and reconnect with the new tokens.


Configure OAuth2/OIDC authentication 
--------------------------------------------------------------

To establish OAuth2/OIDC authentication for the Karapace REST proxy, complete the following prerequisites and configuration steps:

Prerequisites
```````````````
* :doc:`Aiven for Apache Kafka® </docs/products/kafka/get-started>` service running with :doc:`OAuth2/OIDC enabled </docs/products/kafka/howto/enable-oidc>`.
* :doc:`Karapace schema registry and REST APIs enabled </docs/products/kafka/karapace/howto/enable-karapace>`.
* Ensure access to an OIDC-compliant provider, such as Auth0, Okta, Google Identity Platform, or Azure.

Configuration via Aiven Console
```````````````````````````````````
1. In `Aiven Console <https://console.aiven.io/>`_, select your project and then choose your Aiven for Apache Kafka® service.
2. On the **Overview** page, scroll down to **Advanced configuration** and select **Configure**.
3. In the **Advanced configuration** screen, select **Add configuration options**.
4. Look for  ``kafka_rest_authorization`` parameter and set it to ``True``. 

Configuration via Aiven CLI
`````````````````````````````

To enable REST proxy authorization, use the following command in the Aiven CLI, replacing ``SERVICE_NAME`` with your actual service name:

.. code:: 
    
    avn service update -c kafka_rest_authorization=true SERVICE_NAME

Disable REST proxy authorization, use: 

.. code:: 
    
    avn service update -c kafka_rest_authorization=false SERVICE_NAME

.. warning:: 
    Enabling Apache Kafka REST proxy authorization can disrupt access for users if the Kafka access control rules have not been configured properly. For more information, see :doc:`Manage Apache Kafka® REST proxy authorization </docs/products/kafka/karapace/howto/manage-kafka-rest-proxy-authorization>`.


