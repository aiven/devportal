Add Google as an identity provider 
===================================

Use Google to give your organization users single sign-on (SSO) access to Aiven. 


Prerequisite steps in Aiven Console
------------------------------------

Add Google as an :ref:`identity provider <add-idp-aiven-console>` in the Console. 


.. _configure-saml-google:

Configure SAML on Google
------------------------

1. Log in to Google Admin console.

2. Go to Menu -> Apps -> Web and mobile apps.

3. Click Add App -> Add custom SAML app.

4. On the App Details page, enter a name for the Aiven profile.

5. Click Continue.

6. On the Google Identity Provider details page, Copy the **SSO URL**, **Entity ID** and the **Certificate**. These are needed later for the SAML configuration in Aiven Console.

7. Click Continue.

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

9. Click Finish.

10. Turn on your SAML app.


Finish the configuration in Aiven
----------------------------------

Go back to the Aiven Console to :ref:`configure the IdP <configure-idp-aiven-console>` and complete the setup.