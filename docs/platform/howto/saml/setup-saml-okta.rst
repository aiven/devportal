Setting up SAML authentication with Okta
========================================

SAML ( *Security Assertion Markup Language* ) is a standard for
exchanging authentication and authorization data between an identity
provider and a service provider. To read more about SAML check the :doc:`dedicated page <saml-authentication>`.

The following is the procedure to setup SAML with `Okta <https://www.okta.com/>`_.

Prerequisite steps in Aiven
-----------------------------------

1. Login to the `Aiven Console <https://console.aiven.io>`_

2. Under *Projects* in the top left, click the drop down arrow and
then on **See All Accounts**

3. Click on the Account you want to edit or create a new one

4. Select the **Authentication** tab

5. Create a new Authentication Method, call it *Okta* (or similar) and then
choose the team to add invited people to (or leave it blank)


Setup on Okta
-------------

This is a two step process. We will first create the SAML SP-Initiated
authentication flow, then create a bookmark app that will redirect to
the Aiven console's login page.

1. Login to the ``Admin`` portal and navigate to the ``Applications`` tab. 
   Click on the ``Create a new app integration`` button. You should see the ``Create SAML Integration`` form:

2. Select **SAML 2.0** for the ``Sign on method``, then click ``Next``.

Okta configuration
~~~~~~~~~~~~~~~~~~

3. In the following form, you can give the app a name (e.g. "Aiven SAML"), 
   logo and set it's visibility for your Okta users. Once this is done, click ``Next``.

   .. list-table::
      :widths: 10 90
      :header-rows: 1
      :align: left

      * - Parameter
        - Value
      * - ``Single sign on URL``
        - | ``https://api.aiven.io/v1/sso/saml/account/{account_id}/method/{account_auth_method_id}/acs``
          .. note::
             This value is visible in Aiven Console on the newly created Authentication method page.
      * - ``Audience URI (SP Entity ID)``
        - | ``https://api.aiven.io/v1/sso/saml/account/{account_id}/method/{account_auth_method_id}/metadata``
          .. note::
             This value is visible in Aiven Console on the newly created Authentication method page.
      * - ``Default RelayState``
        - | ``https://console.aiven.io/ - Aiven Console``
          | ``https://console.gcp.aiven.io/ - GCP Marketplace Console``
          | ``https://console.aws.aiven.io/ - AWS Marketplace Console``
          .. important:: 
             This is the homepage of the Aiven Console and is important for IdP initiated sign-on to function correctly.

4. ``Attribute statements`` should have an entry where ``name`` is ``email`` and ``value`` ``user.email``

5. Once this is done, click ``Next`` then ``Finish``. You will be redirect to your application in Okta.

6. Once the application is created, you need to provide the application data to Aiven. These data can be found in the ``Sign On`` tab of the application on Okta, after clicking the ``View Setup Instructions``.

   .. image:: /images/platform/howto/saml/okta-view-saml-instructions.png
      :alt: View SAML setup instructions in Okta

   This will open a new tab where you will get the following required information to
   finalize the setup to use Okta with Aiven in the next step.

   * ``Identity Provider Signle Sign-On URL``
   
   * ``Identity Provider Issuer``

   * ``X.509 Certificate``

Finish the configuration in Aiven
---------------------------------

7. You can then go back to **Aiven Console** and finalize the configuration in the **Authentication** method page.

   .. list-table::
      :header-rows: 1
      :align: left

      * - Parameter
        - | Value 
          | ``from the SAML setup instrctions in previous step``
      * - ``SAML IDP Url`` 
        - ``Identity Provider Signle Sign-On URL``
      * - ``SAML Entity ID`` 
        - ``Identity Provider Issuer``
      * - ``SAML Certificate`` 
        - ``X.509 Certificate``

   .. important::
      Toggle ``Enable IdP login`` and ``Enable authentication method`` before clicking ``Edit Method`` to save the settings.

8. When this is done use the ``Account Link URL`` on the authentication configuration page to link your Okta account and Aiven profile. You can also invite other members of your team to login or signup to Aiven using Okta via the Signup link shown in the Authentication method page.
   
   .. note::
      Remember that they will need to be assigned to the Aiven application in Okta for it to be possible.**

Assigning users to the Okta application
---------------------------------------

For your users to be able to login using SAML, you need to assign to the
Okta application you just created. To do that, go to the ``Assignments``
tab of the application. Then click on the ``Assign`` drop-down button and assign
individual users or groups to the application.

Troubleshooting
---------------

Authentication failed
~~~~~~~~~~~~~~~~~~~~~

When launching Aiven SAML application getting the following error.

   **Authentication Failed**

   Login failed.  Please contact your account administrator for more details.

Check Okta authentication in Aiven console if **Enable IdP login** and **Enable authentication method** are
enabled.


Invalid ``RelayState``
~~~~~~~~~~~~~~~~~~~~~~

If you get this error, it means that you are attempting an IdP-initiated auth flow, i.e. you clicked the Aiven SAML app from the
Okta UI. Previously, Aiven did not support IdP-initiated flows, but now it is possible if you set the Default ``RelayState`` in Okta to the corresponding console of your account.

| ``https://console.aiven.io/ - Aiven Console``
| ``https://console.gcp.aiven.io/ - GCP Marketplace Console``
| ``https://console.aws.aiven.io/ - AWS Marketplace Console``

My Okta password does not work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure that you use the ``Account Link URL`` to add the Okta
Authentication method to your Aiven profile. Once linked, you should get
the choice of multiple sign-in methods as well as see the other
Authentication method in ``User Information`` -> ``Authentication``.