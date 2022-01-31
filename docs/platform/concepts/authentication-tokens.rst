Authentication tokens
=====================

An authentication token allows a user to programmatically access resources instead of using their username-password. Unlike the username-password combination that has a longer shelf life (in some case, they never expire); you can limit how long an authentication token is valid for or revoke it completely.

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

The system has hard limits for how many valid authentication tokens are allowed per user. This limit is different for tokens that are created as a result of sign in operation and for tokens created explicitly; the limit for explicitly created tokens is small but the system never invalidates the tokens unless they expire or they are explicitly revoked. For automatically created tokens the limit is higher but when the limit is reached the system automatically deletes tokens that have been used least recently to avoid going above the limit.

Therefore, an old token can stop working even if it hasn't expired nor been explicitly revoked. To avoid running into problems with this behavior you should always make sure you sign out after sign in instead of just discarding your authentication token. This is mostly relevant for automation which automatically signs in. The Aiven web console automatically revokes current token when signing out and the Aiven command line client also provides a sign out command (avn user logout).

Note about old authentication tokens
------------------------------------

The sign in API call used to hand out tokens that were not explicitly tracked and couldn't be individually revoked (prior to 2018-06-25). These old tokens remain valid and become automatically tracked whenever they're used so that they can be revoked. If the tokens have not been used they will not appear in the list of currently valid tokens though they will still work if used unless the revoke all action is used. These tokens, if used, also count towards maximum token quota.

Known limitations
-----------------

Aiven currently only supports authentication tokens that are associated with regular Aiven user accounts and that have the same access level as the user who created the token. There are future plans for allowing tokens that are bound to a project instead and to allow restricting the access scope for tokens.