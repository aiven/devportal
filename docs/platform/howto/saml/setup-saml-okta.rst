Set up SAML authentication with Okta
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

.. _setup_saml_okta_setup_okta:

Setup on Okta
-------------

This is a two step process. We will first create the SAML SP-Initiated
authentication flow, then create a bookmark app that will redirect to
the Aiven console's login page.

1. Login to the **Admin** portal and navigate to the **Applications** tab. 
   Click on the **Create a new app integration** button. You should see the **Create SAML Integration** form

2. Select **SAML 2.0** for the **Sign on method**, then click **Next**

3. Give the app a name (e.g. "Aiven SAML"), a logo and set it's visibility for your Okta users, then click **Next**

4. Edit the app configuration setting the following values:


   .. list-table::
      :widths: 10 90
      :header-rows: 1
      :align: left

      * - Parameter
        - Value
      * - ``Single sign on URL``
        - ``https://api.aiven.io/v1/sso/saml/account/{account_id}/method/{account_auth_method_id}/acs``
      * - ``Audience URI (SP Entity ID)``
        - ``https://api.aiven.io/v1/sso/saml/account/{account_id}/method/{account_auth_method_id}/metadata``
      * - ``Default RelayState``
        - ``https://console.aiven.io/`` when using the Aiven Console

          ``https://console.gcp.aiven.io/`` when using Aiven GCP Marketplace Console

          ``https://console.aws.aiven.io/`` when using Aiven AWS Marketplace Console
   
   .. important:: 
      The ``Default RelayState`` is the homepage of the Aiven Console and is foundamental for IdP initiated sign-on to function correctly.

   .. note::
      The ``Single sign on URL`` and ``Audience URI (SP Entity ID)`` values are visible in `Aiven Console <https://console.aiven.io/>`__ on the newly created Authentication method page.

5. The **Attribute statements** should have an entry with:
   
   .. list-table::
      :widths: 10 90
      :header-rows: 1
      :align: left

      * - Parameter
        - Value
      * - ``name``
        - ``email``
      * - ``value``
        - ``user.email``

5. Click ``Next`` then ``Finish``. You will be redirect to your application in Okta.

6. Once the application is created, collect the application data to finish the setup in the `Aiven Console <https://console.aiven.io/>`__. The application data can be found in the **Sign On** tab of the application on Okta, after clicking the **View Setup Instructions**.

   .. image:: /images/platform/howto/saml/okta-view-saml-instructions.png
      :alt: View SAML setup instructions in Okta

   The required information to finalize the setup to use Okta with Aiven are the following:

   * ``Identity Provider Signle Sign-On URL``
   
   * ``Identity Provider Issuer``

   * ``X.509 Certificate``

Finish the configuration in Aiven
---------------------------------

Navigate to `Aiven Console <https://console.aiven.io/>`__ and finalize the configuration in the **Authentication** method page and set the following parameters for the new authentication method:

.. list-table::
   :header-rows: 1
   :align: left

   * - Parameter
     - Value
   * - ``SAML IDP Url`` 
     - ``Identity Provider Signle Sign-On URL``
   * - ``SAML Entity ID`` 
     - ``Identity Provider Issuer``
   * - ``SAML Certificate`` 
     - ``X.509 Certificate``

.. important::
   Enable ``Enable IdP login`` and ``Enable authentication method`` before clicking ``Edit Method`` to save the settings.

Use the **Account Link URL** on the authentication configuration page to link your Okta account and Aiven profile. You can also invite other members of your team to login or signup to Aiven using Okta via the **Signup link** shown in the Authentication method page.
   
.. note::

   New users need to be assigned to the Aiven application in Okta for the login to be successful

Assign users to the Okta application
---------------------------------------

For your users to be able to login using SAML, you need to assign to the
Okta application you just created. To do that, go to the ``Assignments``
tab of the application. Then click on the ``Assign`` drop-down button and assign
individual users or groups to the application.

Troubleshooting
---------------

Authentication failed
~~~~~~~~~~~~~~~~~~~~~

When launching Aiven SAML application getting the following error::

   Authentication Failed

   Login failed.  Please contact your account administrator for more details.

Check Okta authentication in Aiven console if **Enable IdP login** and **Enable authentication method** are
enabled.


Invalid ``RelayState``
~~~~~~~~~~~~~~~~~~~~~~

If you get the ``Invalid RelayState``, then you are attempting an IdP-initiated auth flow, for example by clicking the Aiven SAML app from the Okta UI. Previously, Aiven did not support IdP-initiated flows, but now it is possible if you set the ``Default RelayState`` in Okta to the corresponding console of your account as defined in the :ref:`setup Okta section <setup_saml_okta_setup_okta>`.

The Okta password does not work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure to use the **Account Link URL** to add the Okta Authentication method to your Aiven profile. 

Once linked, you should get the choice of multiple sign-in methods as well as see the other
Authentication method in **User Information** -> **Authentication** section on the `Aiven Console <https://console.aiven.io/>`__.