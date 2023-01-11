Set up SAML with Microsoft Azure Active Directory
=================================================

This article explains how to set up SAML with `Microsoft Azure Active Directory (AD) <https://azure.microsoft.com/en-us/products/active-directory/>`_. For more information on SAML and instructions for other identity providers, see the :doc:`Enable SAML authentication </docs/platform/howto/saml/saml-authentication>` article.


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

#. Log in to Microsoft Azure.
#. Got to **Enterprise applications** either by using the tiles or the search bar.
#. Go to **All applications** and click **New application**.
#. Select the **Add from the gallery** search bar to search and use the **Azure AD SAML Toolkit**.
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

The data you need to finish the setup on Aiven is found in the **Single sign-on** settings. We are interested in the **Set up Aiven SAML** section

1. In the Aiven Console, edit your authentication method and provide the ``SAML IDP URL`` to the ``Login URL`` from Microsoft Azure

2. Set the ``SAML Entity ID`` to the ``Azure AD Identifier`` from Microsoft Azure

3. Paste the certificate you downloaded earlier into ``SAML Certificate``

4. Click on Save 

5. Make sure the authentication method is **enabled**, then use the: 

   * **Signup URL** to invite new people
   * **Account link URL** for people already having an Aiven login


Troubleshooting
---------------

Contact your administrator
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you get an error message suggesting to "contact your administrator", check the following:

1. Navigate to the Microsoft Azure Active Directory user profile for the users
2. Check whether the **Contact Info** => **Email** field is populated or blank
3. If it is blank, there are two possible solutions:

   * If the field **Identity** => **User Principal Name** is an email address.
     
     Change the **User Attributes & Claims** to be ``email = user.userprincipalname`` and try the login/registration flows again.

   * If all user accounts have the **Contact Info** => **Alternate email** populated
  
     Change the **User Attributes & Claims** to be ``email = user.othermail``

If you still have login issues, you can use the `SAML Tracer browser extension <https://addons.mozilla.org/firefox/addon/saml-tracer/>`_ to  check the process step by step. The errors shown in the tracker should help you to debug the issues. If it does not work, you can request help by sending an email at support@Aiven.io.
