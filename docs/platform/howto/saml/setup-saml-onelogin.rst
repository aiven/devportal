Set up SAML with OneLogin
==========================

This article explains how to set up SAML with `OneLogin <https://www.onelogin.com/>`_ for an organization in Aiven. For more information on SAML and instructions for other identity providers, see the :doc:`Set up SAML authentication </docs/platform/howto/saml/saml-authentication>` article.

Prerequisite steps in Aiven Console
------------------------------------

#. In the organization, click **Admin**.

#. Select **Authentication**.

#. Click **Add authentication method**.

#. Enter a name and select SAML. You can also select the groups that users will be added to when they sign up or log in through this authentication method.

You are shown two parameters needed to set up the SAML authentication in OneLogin:

* Metadata URL
* ACS URL

Configure SAML on OneLogin
---------------------------

#. Log in to the `OneLogin Admin console <https://app.onelogin.com/login>`_. 

#. Select **Applications** and click **Add App**. 

#. Search for **SAML Custom Connector (Advanced)** and select it.

#. Change the **Display Name** to ``Aiven``.

#. Add any other visual configurations you want and click **Save**.

#. In the **Configuration** section of the menu, set the following parameters:

   .. list-table::
      :header-rows: 1
      :align: left

      * - Parameter
        - Value
      * - ``ACS URL Validation``
        - ``[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)``
      * - ``ACS URL``
        - ``ACS URL`` from Aiven Console 
      * - ``Login URL``
        - ``https://console.aiven.io``
      * - ``SAML Initiator``
        - ``Service Provider`` (or ``OneLogin`` if your users will sign in through OneLogin)
      * - ``SAML nameID format``
        - ``Email``
   

#. Click **Save**.

#. In the **SSO** section of the menu, set **SAML Signature Algorithm** to ``SHA-256``.

#. Copy the certificate content, ``Issuer URL`` and ``SAML 2.0 Endpoint (HTTP)``. These are needed for the SAML configuration in Aiven Console.

#. Click **Save**

#. Assign users to this application.


Finish the configuration in Aiven
---------------------------------

Go back to the **Authentication** page in `Aiven Console <https://console.aiven.io/>`_ to enable the SAML authentication method:

1. Select the name of the OneLogin method that you created.

2. In the SAML configuration section, click **Edit**. 

3. Add the configuration settings from OneLogin: 

* Set the ``SAML IDP URL`` to the ``SAML 2.0 Endpoint (HTTP)`` from OneLogin. 

* Set the ``SAML Entity ID`` to the ``Issuer URL`` from OneLogin.

* Paste the certificate from OneLogin into ``SAML Certificate``.

4. If you set ``SAML Initiator`` to ``OneLogin`` in your OneLogin application, then toggle on ``IdP login``.

5. Toggle on **Enable authentication method** at the top of the page. 

You can use the **Signup URL** to invite new users, or the **Account link URL** for those that already have an Aiven user account.

.. note::
   You need to assign users in OneLogin for the connection to work. 
   
Troubleshooting
----------------

If you are getting errors, try this:

#. Go to the app in OneLogin and click **Settings**.

#. Under **More Actions**, select **Reapply entitlement Mappings**.

If you continue to have issues, you can use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_ to check the process step by step. 

