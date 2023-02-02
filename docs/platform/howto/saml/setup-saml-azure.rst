Set up SAML with Microsoft Azure Active Directory
=================================================

This article explains how to set up SAML with `Microsoft Azure Active Directory (AD) <https://azure.microsoft.com/en-us/products/active-directory/>`_ for an organization in Aiven. For more information on SAML and instructions for other identity providers, see the :doc:`Set up SAML authentication </docs/platform/howto/saml/saml-authentication>` article.


Prerequisite steps in Aiven Console
------------------------------------

#. In the organization, click **Admin**.

#. Select **Authentication**.

#. Click **Add authentication method**.

#. Enter a name and select SAML. You can also select the teams that users will be added to when they sign up or log in through this authentication method.

You are shown two parameters needed to set up the SAML authentication in Microsoft Azure AD:

* Metadata URL
* ACS URL

Configure SAML on Microsoft Azure
----------------------------------

#. Log in to `Microsoft Azure <https://portal.azure.com/>`_.

#. Got to **Enterprise applications**.

#. Select **All applications**.

#. Click **New application**.

#. Select the **Add from the gallery** search bar and use the **Azure AD SAML Toolkit**.

#. Click **Add**.

#. Go back to the **Enterprise applications** list.

   .. Warning::

    The newly created application might not be visible yet. You can use the **All applications** filter to see the new application.  
    
#. Click on the new application name to open the configuration.

#. Select **Single sign-on** configuration.

#. Select **SAML** as the single sign-on method.

#. Add the following paramters to the **Basic SAML Configuration**:

.. list-table::
      :header-rows: 1
      :align: left

      * - Parameter
        - Value
      * - ``Identifier (Entity ID)``
        - ``https://api.aiven.io/v1/sso/saml/account/{account_id}/method/{account_authentication_method_id}/metadata``
      * - ``Reply URL (Assertion Consumer Service URL)``
        - ``https://api.aiven.io/v1/sso/saml/account/{account_id}/method/{account_authentication_method_id}/acs``
      * - ``Sign on URL``
        - ``https://console.aiven.io``


#. Click **Save**.

#. In the **User Attributes & Claims**, click **Add a new claim**.

#. Create an attribute with the following data:

.. list-table::
      :header-rows: 1
      :align: left

      * - Parameter
        - Value
      * - ``Name``
        - ``email``
      * - ``Source``
        - Select ``Attribute``
      * - ``Source Attribute``
        - ``user.email``

#. Download the **Certificate (Base64)** from the **SAML Signing Certificate** section.

#. Go to **Users and groups** and click **Add user**. 

#. Select the users that you want to use Azure AD to log in to Aiven. 

#. Click **Assign**.


Finish the configuration in Aiven
----------------------------------

Go back to the **Authentication** page in the `Aiven Console <https://console.aiven.io/>`_ to enable the SAML authentication method:

#. Select the name of the Azure AD method that you created.

#. In the SAML configuration section, click **Edit**. 

#. Add the configuration settings from Azure:

  * Set the ``SAML IDP URL`` to the ``Login URL`` from Azure.
  * Set the ``SAML Entity ID`` to the ``Azure AD Identifier`` from Azure.
  * Paste the certificate from Azure into the ``SAML Certificate`` field.

#. Click **Edit method** to save your changes.

#. Toggle on **Enable authentication method** at the top of the page. 

You can use the **Signup URL** to invite new users, or the **Account link URL** for those that already have an Aiven user account.

Troubleshooting
---------------

Error: contact your administrator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you get an error message suggesting you contact your administrator, try these steps: 

#. Go to the Microsoft Azure AD user profile for the users.

#. Check whether the **Contact Info** => **Email** field is blank.

If it is blank, there are two possible solutions:

   * If the field **Identity** => **User Principal Name** is an email address, try changing the **User Attributes & Claims** to ``email = user.userprincipalname``. 

   * If none of the user accounts have a blank **Contact Info** => **Alternate email** field, try changing the **User Attributes & Claims** to ``email = user.othermail``.

If you still have login issues, you can use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_ to check the process step by step. If this doesn't work, get in touch with our support team at support@Aiven.io.
