Authentication tokens
=====================

An authentication token allows a user to programmatically access resources instead of using their username and password. The usage of authentication tokens rather than user credentials has many benefits:

- Multiple tokens can be generated for different apps or use cases unlike a single set of user credentials for everything.
- The limited lifespan of authentication tokens reduce the security risk of being exposed.

.. mermaid::

    sequenceDiagram 
        Client->>+Server: Here's my username/password. Give me a token.
        Server-->>-Client: Your username/password is valid. Here's a token. 
        Client->>+Server: Here's a token. Show me a list of my resources.
        Server-->>-Client: Your token is valid. Here's a list of your resources.

How Aiven manages user sessions using authentication tokens
-----------------------------------------------------------

Each time a user signs in to Aiven either via the web console, Aiven command line client, or direct REST API call, the server creates a new authentication token associated with the user.

The user can configure the expiry when requesting the token. It is also possible to configure the token to extend its expiry when it is used, so that it will remain valid while it is in active use.

Token counts
------------

The system has hard limits for how many valid authentication tokens are allowed per user. This limit is different for tokens that are created as a result of sign in operation and for tokens created explicitly. The max token count is **10** for user created tokens but the system never invalidates the tokens unless they expire or they are explicitly revoked. For automatically created tokens the limit is **1000** but when this limit is reached the system automatically deletes tokens that have been used least recently to avoid going above the limit.

Therefore, an old token can stop working even if it hasn't expired nor been explicitly revoked. To avoid running into problems with this behavior, configure your tokens with expiry times that suit their use case. This is mostly relevant for automation which automatically creates a new token each time it runs. The Aiven web console automatically revokes the current token when signing out and the Aiven command line client also provides a sign out command (``avn user logout``).

Considerations for working with tokens
--------------------------------------

Limit token expiry
''''''''''''''''''

Think about how long the token needs to be valid for; this varies depending on what the token is used for.

* If you're doing a video recording for a demo, you can set the token to expire in an hour. This means that even if you have exposed the token during your work, it will no longer work by the time the video is published.

* For server side use within the build process, such as on the CI server, a token with long-term validity and/or refresh interval is appropriate.

* For a situation where the token could ever be accessible, keep the expiry time short, and generate a new token for each operation.

The longer a token lives, the higher the risk of exposure. Follow the IT security best practises established by your company and refrain from allowing human users to share the same token.

Use appropriate user accounts
'''''''''''''''''''''''''''''

Especially when working with tokens for automation rather than personal or one-off use, generate the tokens for a user account that has the appropriate access permissions that the tokens should have. If you are the admin, then it is not recommended to give a token for your own account to automation services that may only need read access.

Rotate tokens regularly
'''''''''''''''''''''''

It is also good practice to rotate your authorization tokens on a regular basis, for example each month. You can have as many tokens active at one time as you need, so you can create a new token, replace it as needed, check everything works, and then remove the old token once you are confident that all changes have completed successfully.


.. note::

    Follow :doc:`Create an authentication token <../howto/create_authentication_token>` to check how you can create an authentication token from the Aiven console or the Aiven CLI.