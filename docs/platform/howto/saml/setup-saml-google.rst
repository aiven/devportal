Set up SAML with Google
=======================

This article explains how to set up SAML with Google for an organization in Aiven. For more information on SAML and instructions for other identity providers, see the :doc:`Set up SAML authentication </docs/platform/howto/saml/saml-authentication>` article.

Prerequisite steps in Aiven Console
------------------------------------

#. In the organization, click **Admin**.

#. Select **Authentication**.

#. Click **Add authentication method**.

#. Enter a name and select SAML. You can also select the teams that users will be added to when they sign up or log in through this authentication method.

You are shown two parameters needed to set up the SAML authentication in Google:

* Metadata URL
* ACS URL

Configure SAML on Google
------------------------

1. Log in to Google Admin console

2. Go to Menu -> Apps -> Web and mobile apps

3. Click Add App -> Add custom SAML app

4. On the App Details page, enter a name for the Aiven profile

5. Click Continue

6. On the Google Identity Provider details page, Copy the **SSO URL**, **Entity ID** and the **Certificate**. These are needed later for the SAML configuration in Aiven Console.

7. Click Continue

8. In the Service Provider Details window, set the following parameters:

   .. list-table::
      :header-rows: 1
      :align: left

      * - Parameter
        - Value
      * - ``Entity ID``
        - ``Metadata URL`` from Aiven Console
      * - ``ACS URL``
        - ``ACS URL`` from Aiven Console
      * - ``Name ID format``
        - ``EMAIL``
      * - ``App attributes``
        - ``email``

9. Click Finish

10. Configure the User access for the Aiven SAML app

Finish the configuration in Aiven
----------------------------------

Go back to the **Authentication** page in `Aiven Console <https://console.aiven.io/>`_ to enable the SAML authentication method:

1. Select the name of the Google method that you created.

2. In the SAML configuration section, click **Edit**. 

3. Add the configuration settings from Google:

* Set the ``SAML IDP URL`` to the ``SSO URL`` from Google.
* Set the ``SAML Entity ID`` to the ``Entity ID`` from Google .
* Paste the certificate from Google into the ``SAML Certificate`` field.

4. Click **Edit method** to save your changes.

5. Toggle on **Enable authentication method** at the top of the page.

You can use the **Signup URL** to invite new users, or the **Account link URL** for those that already have an Aiven user account.

Troubleshooting
---------------

If you have issues, you can use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_ to check the process step by step. 
