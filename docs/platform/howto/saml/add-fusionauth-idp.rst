Add FusionAuth as an identity provider 
=======================================

Use `FusionAuth <https://fusionauth.io/>`_ to give your organization users single sign-on (SSO) access to Aiven. 


Prerequisite steps in Aiven Console
------------------------------------

Add FusionAuth as an :ref:`identity provider <add-idp-aiven-console>` in the Console. 


.. _configure-saml-fusionauth:

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
----------------------------------

Go back to the Aiven Console to :ref:`configure the IdP <configure-idp-aiven-console>` and complete the setup.
