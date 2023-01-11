Set up SAML authentication with Okta
======================================

This article explains how to set up SAML with `Okta <https://www.okta.com/>`_ for an organization in Aiven. For more information on SAML and instructions for other identity providers, see the :doc:`Enable SAML authentication </docs/platform/howto/saml/saml-authentication>` article. 

Prerequisite steps in the Aiven Console
---------------------=------------------

#. In the organization, click **Admin**.

#. Select **Authentication**.

#. Click **Add authentication method**.

#. Enter a name and select SAML. You can also select the teams that users will be added to when they sign up or log in through this authentication method.

You are shown two parameters needed to set up the SAML authentication in Auth0:

* Metadata URL
* ACS URL

Configure SAML on Okta
-----------------------

This is a two step process. You first create the SAML SP-Initiated
authentication flow, then create a bookmark app that will redirect to
the Aiven Console's login page.

#. Log in to the **Admin** portal.

#. Go to the **Applications** tab. 

#. Click **Create a new app integration**. 

#. Select **SAML 2.0** for the **Sign on method**, then click **Next**.

#. Enter a name for the app and add a logo. 

#. Set it's visibility for your Okta users, then click **Next**.

#. Set the following values in the app configuration:


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
      The ``Default RelayState`` is the homepage of the Aiven Console and is fundamental for IdP initiated sign on to function correctly.

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

5. Click **Next** then **Finish**. You are redirected to your application in Okta.

6. Once the application is created, collect the application data to finish the setup in the `Aiven Console <https://console.aiven.io/>`__. The application data can be found in the **Sign On** tab of the application on Okta, after clicking the **View Setup Instructions**.

   .. image:: /images/platform/howto/saml/okta/okta-view-saml-instructions.png
      :alt: View SAML setup instructions in Okta

   The required information to finalize the setup to use Okta with Aiven are the following:

   * ``Identity Provider Signle Sign-On URL``
   
   * ``Identity Provider Issuer``

   * ``X.509 Certificate``

.. image:: /images/platform/howto/saml/okta/okta-saml-settings.png
   :alt: SAML settings in Okta

Assign users to the Okta application
---------------------------------------

For your users to be able to login using SAML, you need to assign to the
Okta application you just created. To do that, go to the ``Assignments``
tab of the application. Then click on the ``Assign`` drop-down button and assign
individual users or groups to the application.

.. note::

   New users need to be assigned to the Aiven application in Okta for the login to be successful


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

.. image:: /images/platform/howto/saml/okta/okta-edit-method.png
   :alt: Edit authentication method in Aiven Console

.. important::
   Enable ``Enable IdP login`` and ``Enable authentication method`` before clicking ``Edit Method`` to save the settings.

Use the **Account Link URL** on the authentication configuration page to link your Okta account and Aiven profile. You can also invite other members of your team to login or signup to Aiven using Okta via the **Signup link** shown in the Authentication method page.
   

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