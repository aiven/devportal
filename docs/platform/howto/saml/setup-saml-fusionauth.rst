Set up SAML authentication with FusionAuth
==========================================

This article explains how to set up SAML with `FusionAuth <https://fusionauth.io/>`_ for an organization in Aiven. For more information on SAML and instructions for other identity providers, see the :doc:`Set up SAML authentication </docs/platform/howto/saml/saml-authentication>` article.

Prerequisite steps in Aiven Console
------------------------------------

#. In the organization, click **Admin**.

#. Select **Authentication**.

#. Click **Add authentication method**.

#. Enter a name and select SAML. You can also select the teams that users will be added to when they sign up or log in through this authentication method.

#. Click **Add method**.

You are shown two parameters needed to set up the SAML authentication in FusionAuth:

* Metadata URL
* ACS URL

Configure SAML on FusionAuth
----------------------------

The setup on FusionAuth has three parts: 

* create an API key
* generate a custom RSA certificate 
* create an application

First you need to create an API Key in your FusionAuth instance: 

#. In FusionAuth, go to **Settings** > **API Keys**.

#. Click the **Add** icon. 
 
#. Enter a description for the key (for example, "Certificate generator").
 
#. In the **Endpoints** list, find ``/api/key/import``.
  
#. Toggle on **POST**.

#. Click the **Save** icon.

   .. image:: /images/platform/howto/saml/fusionauth/create-api-key.png
      :alt: Creating API Key.

#. On the **API Keys** page, find your new key and click on the value in the **Key** column. 

#. Copy the whole key. You’ll use this for the script.

   .. image:: /images/platform/howto/saml/fusionauth/grab-api-key.png
      :alt: Grabbing API Key.

#. Clone `the FusionAuth example scripts GitHub repository <https://github.com/FusionAuth/fusionauth-example-scripts>`__.

   .. code:: shell

       git clone git@github.com:FusionAuth/fusionauth-example-scripts.git
       cd fusionauth-example-scripts/v3-certificate

#. Run the ``generate-certificate`` script.

   .. code:: shell

      ./generate-certificate

#. Give the key a meaningful name (for example, "Aiven key").

#. Copy the generated certificate that the script creates. You now have a certificate in the **Key Master** in your FusionAuth instance. 

Next, create an application in your FusionAuth instance:

#. In **Applications**, click the **Add** icon.
 
#. Enter a name for the application (for example, "Aiven").
 
#. On the **SAML** tab, and toggle on the **Enabled** switch.

#. Paste the **Metadata URL** and **ACS URL** you copied from the Aiven Console to the **Issuer** and
**Authorized redirect URLs** fields in your FusionAuth application, respectively.

.. list-table::
  :header-rows: 1
  :align: left

  * - Aiven
    - FusionAuth
  * - Metadata URL
    - Issuer
  * - ACS URL
    - Authorized redirect URLs

#. In the **Authentication response** section, change the **Signing key** to the API key you created.

#. Click the **Save** icon to save your application. 

#. On the **Applications** page, click the magnifying glass. 

#. In the **SAML v2 Integration details** section, copy the **Entity Id** and **Login URL**.

Finish the configuration in Aiven
---------------------------------

Go back to the **Authentication** page in `Aiven Console <https://console.aiven.io/>`_ to enable the SAML authentication method:

1. Select the name of the FusionAuth method that you created.

2. In the SAML configuration section, click **Edit**.

3. Toggle on **IdP login**.

4. Add the configuration settings from FusionAuth:

* Set the ``SAML IDP Url`` to the ``Login URL`` from FusionAuth.
* Set the ``SAML Entity ID`` to the ``Entity Id`` from FusionAuth.
* Paste the certificate from the ``Generating certificate`` in FusionAuth into the `SAML Certificate`` field.

5. Click **Edit method** to save your changes.

6. Toggle on **Enable authentication method** at the top of the page.

You can use the **Signup URL** to invite new users, or the **Account link URL** for those that already have an Aiven user account.


.. image:: /images/platform/howto/saml/fusionauth/login-sso.png
   :alt: Logging in to Aiven.


Troubleshooting
---------------

If you have issues, you can use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_ to check the process step by step.
