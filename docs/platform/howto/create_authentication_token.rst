Create an authentication token
==============================

You can use the Aiven web console to create an authentication token for use with the Aiven command-line interface (CLI) or API. 
To learn more about using authentication token for Aiven resources, refer to :doc:`../concepts/authentication-tokens`.

To create an authentication token:

1. Log in to the `Aiven web console <https://console.aiven.io/>`_.

2. Click the user icon in the top-right corner of the page.

3. Click **Authentication** tab and scroll down to *Authentication tokens*.

4. Click the **Generate token** button.

5. Enter a description (optional) and a time limit (optional) for the token. Leave the *Max age hours* field empty if you do not want the token to expire.

6. Click **Generate token**.

7. Click the **Copy** icon or select and copy the access token.

   .. note::
       You cannot get the token later after you close this view.

8. Store the token safely and treat this just like a password.

9. Click **Close**.

You can now use the authentication token to access your Aiven resources from the CLI or API.