Authentication tokens
=====================

An authentication token allows a user to programmatically access resources instead of using their username-password. The usage of authentication tokens has the following benefits compared to username and password:

- Multiple tokens can be generated for different apps or use cases unlike a single username-password for everything.
- Short lifespan of authentication tokens reduce the security risk of being exposed.

.. mermaid::

    sequenceDiagram 
        Client->>+Server: Here's my username/password. Give me a token.
        Server-->>-Client: Your username/password is valid. Here's a token. 
        Client->>+Server: Here's a token. Show me a list of my resources.
        Server-->>-Client: Your token is valid. Here's a list of your resources.

How Aiven manages user sessions using authentication tokens
-----------------------------------------------------------

Each time a user signs in to Aiven either via the web console, Aiven command line client, or direct REST API call, the server creates a new authentication token associated with the user.
These tokens are set to expire after 30 days (subject to change) but the expiry date is adjusted whenever the token is used so the token may remain valid practically indefinitely if it is used frequently enough.

Token counts
------------

The system has hard limits for how many valid authentication tokens are allowed per user. This limit is different for tokens that are created as a result of sign in operation and for tokens created explicitly. The max token count is **10** for user created tokens but the system never invalidates the tokens unless they expire or they are explicitly revoked. For automatically created tokens the limit is **1000** but when this limit is reached the system automatically deletes tokens that have been used least recently to avoid going above the limit.

Therefore, an old token can stop working even if it hasn't expired nor been explicitly revoked. To avoid running into problems with this behavior you should always make sure you sign out after sign in instead of just discarding your authentication token. This is mostly relevant for automation which automatically signs in. The Aiven web console automatically revokes the current token when signing out and the Aiven command line client also provides a sign out command (avn user logout).

Known limitations
-----------------

Aiven currently only supports authentication tokens that are associated with regular Aiven user accounts and that have the same access level as the user who created the token. There are future plans for allowing tokens that are bound to a project instead and to allow restricting the access scope for tokens.