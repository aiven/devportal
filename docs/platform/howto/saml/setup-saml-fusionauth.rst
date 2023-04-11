Set up SAML authentication with FusionAuth
==========================================

This article explains how to set up SAML with `FusionAuth <https://fusionauth.io/>`_ for an organization in Aiven. For more information on SAML and instructions for other identity providers, see the :doc:`Set up SAML authentication </docs/platform/howto/saml/saml-authentication>` article.

Prerequisite steps in Aiven Console
------------------------------------

First, we need to create a team that the created users will be part of.

#. In the organization, click **Admin**.

#. Select **Organization**.

#. Click **Create team** in the organization details section.

#. Set the **Team name** as ``Developers`` and click **Create team**.

#. After arriving back to the teams page, click on the newly created team and go to the **Projects and Roles** tab.

#. Click **Add projects**, select the project, the desired **Permission level** (e.g. ``Developer``) and click **Add project** to finish setting up the team.

Now, let’s configure the authentication method.

#. In the organization, click **Admin**.

#. Select **Authentication**.

#. Click **Add authentication method**.

#. Name it ``FusionAuth``, select ``SAML`` as the **Method Type** and choose the ``Developers`` team you just created in **Team to autojoin on signup**.

#. Click **Add method** to save.

#. Write down both **Metadata URL** and **ACS URL** values and click **Finish**.

Configure SAML on FusionAuth
----------------------------

We need to generate a custom RSA certificate and upload it to your FusionAuth instance’s Key Master.

Before running it, you need to create an API Key in your FusionAuth instance. Browse to **Settings → API Keys** and click the green plus icon. Set the **Description** as ``Certificate generator`` and locate ``/api/key/import`` in the **Endpoints** section. Click the ``POST`` switch to enable it and confirm generating the key by clicking the blue floppy disk icon.

.. image:: /images/platform/howto/saml/fusionauth/create-api-key.png
   :alt: Creating API Key.

After being redirected back to the API Keys page, click on the ``Key`` for the created item to reveal its actual value and copy it. You’ll have to provide this value to the script soon.

.. image:: /images/platform/howto/saml/fusionauth/grab-api-key.png
   :alt: Grabbing API Key.

Now that your application is ready, clone `this GitHub repository <https://github.com/FusionAuth/fusionauth-example-scripts>`__ and execute the script located in ``rsa-certificate``.

.. code:: shell

   git clone git@github.com:FusionAuth/fusionauth-example-scripts.git
   cd fusionauth-example-scripts/rsa-certificate
   ./generate-certificate

Answer the questions the script will ask you and make sure to give the key a meaningful name, like ``Aiven key``. After finishing, you’ll have a certificate in the Key Master in your FusionAuth instance ready to be used. The script will also print the generated certificate. Write it down.

Now, create an application in your FusionAuth instance. Navigate to **Applications** and click the green plus icon. Name it ``Aiven``, go to the **SAML** tab and toggle the **Enabled** switch.

Paste the **Metadata URL** and **ACS URL** you copied from Aiven to **Issuer** and
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

Scroll down to the **Authentication response** section and change the **Signing key** to the ``Aiven key`` you created above.

Click the blue floppy disk icon to save your application. When redirected to the **Applications** page, view your application details by clicking the magnifying glass.

In **SAML v2 Integration details**, write down both **Entity Id** and **Login URL** fields.

Finish the configuration in Aiven
---------------------------------

Go back to the **Authentication** page in `Aiven Console <https://console.aiven.io/>`_ to enable the SAML authentication method:

1. Select the FusionAuth method that you created.

2. In the SAML configuration section, click **Edit**.

3. Toggle on **IdP login**.

4. Add the configuration settings from FusionAuth:

* ``SAML IDP Url``: the **Login URL** from FusionAuth.
* ``SAML Entity ID``: the **Entity Id** from FusionAuth.
* ``SAML Certificate``: paste the certificate you’ve copied from the ``Generating certificate`` two steps above.

5. Click **Edit method** to save your changes.

6. Toggle on **Enable authentication method** at the top of the page.

You can use the **Signup URL** to invite new users, or the **Account link URL** for those that already have an Aiven user account.

Testing
-------

Open the Signup URL you copied above in an incognito tab or using another browser. You’ll reach the signup page below.

.. image:: /images/platform/howto/saml/fusionauth/login-sso.png
   :alt: Logging in to Aiven.

Click on **Sign up with FusionAuth**, which will redirect you to the FusionAuth login page. Fill in your credentials and submit the form to be taken back to the Aiven console, already logged in and part of the ``Developers`` team.

Troubleshooting
---------------

If you have issues, you can use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_ to check the process step by step.
