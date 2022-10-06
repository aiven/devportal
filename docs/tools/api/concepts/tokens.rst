Work with API authorization tokens
==================================

The Aiven API uses tokens for authentication. In this article, we cover some of the key considerations when working with API tokens.

Limit token expiry
------------------

Think about how long the token needs to be valid for; this varies depending on what the token is used for.

* When I am doing a one-off demo or video recording, I set my token to expire after one hour. This means that even if I have exposed the token during my work, it will no longer work by the time the video is published.

* For serverside use within the build process, such as on the CI server, a token with long-term validity and/or refresh interval is appropriate.

* For a situation where the token could ever be accessible, keep the expiry time short, and generate a new token for each operation.

Use appropriate user accounts
-----------------------------

Especially when working with tokens for automation rather than personal or one-off use, generate the tokens for a user account that has the appropriate access permissions that the tokens should have. If you are the admin, then it is not recommended to give a token for your own account to automation services that may only need read access.

Rotate tokens regularly
-----------------------

It is also good practice to rotate your authorization tokens on a regular basis, for example each month. You can have as many tokens active at one time as you need, so you can create a new token, replace it as needed, check everything works, and then remove the old token once you are confident that all changes have completed successfully.
